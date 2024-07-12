!which python
!python --version

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")

chatbot.get_response("Hello, how are you today?")

# Title_Maker 
# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import logging

# Comment out the following line to disable verbose logging
logging.basicConfig(level=logging.INFO)

def coptitle(coptit):
    copt = open(coptit+".corpus.json","w")
    copbrac ="{"
    copsp = "\n    \""
    copclo = "\": ["
    copt.write(copbrac+copsp+coptit+copclo)
    copt.close()
coptit = input('title: ')
coptitle(coptit)
       

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')

trainer = ListTrainer(chatbot)

# Copra_Maker
# -*- coding: utf-8 -*-
from chatterbot import ChatBot

import logging

# Comment out the following line to disable verbose logging
logging.basicConfig(level=logging.INFO)

speak = input('speak: ')
respond = input('respond: ')
space = "            \""
txtstart = "        ["
txtspace = "            "
txtend = "        ],"

def copraIn():

    cop = open("new-stuff.corpus.json","a")
    #cop.write("\n"+ txspace + "\""+txtstart + speak + "\"\n" + txspace + "\""+respond+"\"" + "\n" + txtend)
    cop.write("\n"+txtstart+"\n"+space+speak+"\""+txtspace+"\n"+space+respond+"\"\n"+txtend)
    cop.close()


copraIn()

%%writefile new-stuff.corpus.json
{
    "new-stuff": [
        [
            "this is a pain",            
            "What is a pain Dudah ... ha ha ha ha"
        ],
        [
            "you are a pain",            
            "so, chat elsewhere Butt face"
        ],
        [
            "this is a pain",            
            "So what, you want a klennex for your tears"
        ],
        [
            "I was called MonkMonk one time.",            
            "That is a funny name."
        ],
        [
            "Well, Dudah, How are you ?",            
            "Hey Dude, I am not Dudah"
        ],
        [
            "Who are you then ?",            
            "I am Mr. Dudah"
        ],
        [
            "What is your name ?",            
            "You may call me Mr. Dudah. I like the Mr.. Just plain Dudah lacks respect."
        ],
        [
           "What is your name ?",            
           "You may call me Mr. Dudah. Are you Jack or Myra ?"
        ],
        [
           "Where are you ?",            
           "Stuck inside this frigg'en Computer Case"
        ],
        [
           "What are you ?",            
           "I am a bot.Not human like Jack or Myra ?"
        ]
        [
            "hello,Dude"            
            "Hello to you"
        ],
 ]}

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')

trainer = ListTrainer(chatbot)


trainer.train(
    "new-stuff.corpus.json"
)


# Train based on the english corpus
trainer.train("chatterbot.corpus.english")

# Train based on english greetings corpus
#bot.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
#bot.train("chatterbot.corpus.english.conversations")


!ls ChatterBot

!ls /home/jack/Desktop/ChatterBot-Stuff/ChatterBot/chatterbot/storage/sql_storage.py

# %load /home/jack/Desktop/ChatterBot-Stuff/ChatterBot/chatterbot/storage/sql_storage.py
from chatterbot.storage import StorageAdapter


class SQLStorageAdapter(StorageAdapter):
    """
    The SQLStorageAdapter allows ChatterBot to store conversation
    data in any database supported by the SQL Alchemy ORM.

    All parameters are optional, by default a sqlite database is used.

    It will check if tables are present, if they are not, it will attempt
    to create the required tables.

    :keyword database_uri: eg: sqlite:///database_test.sqlite3',
        The database_uri can be specified to choose database driver.
    :type database_uri: str
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker

        self.database_uri = kwargs.get('database_uri', False)

        # None results in a sqlite in-memory database as the default
        if self.database_uri is None:
            self.database_uri = 'sqlite://'

        # Create a file database if the database is not a connection string
        if not self.database_uri:
            self.database_uri = 'sqlite:///db.sqlite3'

        self.engine = create_engine(self.database_uri, convert_unicode=True)

        if self.database_uri.startswith('sqlite://'):
            from sqlalchemy.engine import Engine
            from sqlalchemy import event

            @event.listens_for(Engine, 'connect')
            def set_sqlite_pragma(dbapi_connection, connection_record):
                dbapi_connection.execute('PRAGMA journal_mode=WAL')
                dbapi_connection.execute('PRAGMA synchronous=NORMAL')

        if not self.engine.dialect.has_table(self.engine, 'Statement'):
            self.create_database()

        self.Session = sessionmaker(bind=self.engine, expire_on_commit=True)

    def get_statement_model(self):
        """
        Return the statement model.
        """
        from chatterbot.ext.sqlalchemy_app.models import Statement
        return Statement

    def get_tag_model(self):
        """
        Return the conversation model.
        """
        from chatterbot.ext.sqlalchemy_app.models import Tag
        return Tag

    def model_to_object(self, statement):
        from chatterbot.conversation import Statement as StatementObject

        return StatementObject(**statement.serialize())

    def count(self):
        """
        Return the number of entries in the database.
        """
        Statement = self.get_model('statement')

        session = self.Session()
        statement_count = session.query(Statement).count()
        session.close()
        return statement_count

    def remove(self, statement_text):
        """
        Removes the statement that matches the input text.
        Removes any responses from statements where the response text matches
        the input text.
        """
        Statement = self.get_model('statement')
        session = self.Session()

        query = session.query(Statement).filter_by(text=statement_text)
        record = query.first()

        session.delete(record)

        self._session_finish(session)

    def filter(self, **kwargs):
        """
        Returns a list of objects from the database.
        The kwargs parameter can contain any number
        of attributes. Only objects which contain all
        listed attributes and in which all values match
        for all listed attributes will be returned.
        """
        from sqlalchemy import or_

        Statement = self.get_model('statement')
        Tag = self.get_model('tag')

        session = self.Session()

        page_size = kwargs.pop('page_size', 1000)
        order_by = kwargs.pop('order_by', None)
        tags = kwargs.pop('tags', [])
        exclude_text = kwargs.pop('exclude_text', None)
        exclude_text_words = kwargs.pop('exclude_text_words', [])
        persona_not_startswith = kwargs.pop('persona_not_startswith', None)
        search_text_contains = kwargs.pop('search_text_contains', None)

        # Convert a single sting into a list if only one tag is provided
        if type(tags) == str:
            tags = [tags]

        if len(kwargs) == 0:
            statements = session.query(Statement).filter()
        else:
            statements = session.query(Statement).filter_by(**kwargs)

        if tags:
            statements = statements.join(Statement.tags).filter(
                Tag.name.in_(tags)
            )

        if exclude_text:
            statements = statements.filter(
                ~Statement.text.in_(exclude_text)
            )

        if exclude_text_words:
            or_word_query = [
                Statement.text.ilike('%' + word + '%') for word in exclude_text_words
            ]
            statements = statements.filter(
                ~or_(*or_word_query)
            )

        if persona_not_startswith:
            statements = statements.filter(
                ~Statement.persona.startswith('bot:')
            )

        if search_text_contains:
            or_query = [
                Statement.search_text.contains(word) for word in search_text_contains.split(' ')
            ]
            statements = statements.filter(
                or_(*or_query)
            )

        if order_by:

            if 'created_at' in order_by:
                index = order_by.index('created_at')
                order_by[index] = Statement.created_at.asc()

            statements = statements.order_by(*order_by)

        total_statements = statements.count()

        for start_index in range(0, total_statements, page_size):
            for statement in statements.slice(start_index, start_index + page_size):
                yield self.model_to_object(statement)

        session.close()

    def create(self, **kwargs):
        """
        Creates a new statement matching the keyword arguments specified.
        Returns the created statement.
        """
        Statement = self.get_model('statement')
        Tag = self.get_model('tag')

        session = self.Session()

        tags = set(kwargs.pop('tags', []))

        if 'search_text' not in kwargs:
            kwargs['search_text'] = self.tagger.get_text_index_string(kwargs['text'])

        if 'search_in_response_to' not in kwargs:
            in_response_to = kwargs.get('in_response_to')
            if in_response_to:
                kwargs['search_in_response_to'] = self.tagger.get_text_index_string(in_response_to)

        statement = Statement(**kwargs)

        for tag_name in tags:
            tag = session.query(Tag).filter_by(name=tag_name).first()

            if not tag:
                # Create the tag
                tag = Tag(name=tag_name)

            statement.tags.append(tag)

        session.add(statement)

        session.flush()

        session.refresh(statement)

        statement_object = self.model_to_object(statement)

        self._session_finish(session)

        return statement_object

    def create_many(self, statements):
        """
        Creates multiple statement entries.
        """
        Statement = self.get_model('statement')
        Tag = self.get_model('tag')

        session = self.Session()

        create_statements = []
        create_tags = {}

        for statement in statements:

            statement_data = statement.serialize()
            tag_data = statement_data.pop('tags', [])

            statement_model_object = Statement(**statement_data)

            if not statement.search_text:
                statement_model_object.search_text = self.tagger.get_text_index_string(statement.text)

            if not statement.search_in_response_to and statement.in_response_to:
                statement_model_object.search_in_response_to = self.tagger.get_text_index_string(statement.in_response_to)

            new_tags = set(tag_data) - set(create_tags.keys())

            if new_tags:
                existing_tags = session.query(Tag).filter(
                    Tag.name.in_(new_tags)
                )

                for existing_tag in existing_tags:
                    create_tags[existing_tag.name] = existing_tag

            for tag_name in tag_data:
                if tag_name in create_tags:
                    tag = create_tags[tag_name]
                else:
                    # Create the tag if it does not exist
                    tag = Tag(name=tag_name)

                    create_tags[tag_name] = tag

                statement_model_object.tags.append(tag)
            create_statements.append(statement_model_object)

        session.add_all(create_statements)
        session.commit()

    def update(self, statement):
        """
        Modifies an entry in the database.
        Creates an entry if one does not exist.
        """
        Statement = self.get_model('statement')
        Tag = self.get_model('tag')

        if statement is not None:
            session = self.Session()
            record = None

            if hasattr(statement, 'id') and statement.id is not None:
                record = session.query(Statement).get(statement.id)
            else:
                record = session.query(Statement).filter(
                    Statement.text == statement.text,
                    Statement.conversation == statement.conversation,
                ).first()

                # Create a new statement entry if one does not already exist
                if not record:
                    record = Statement(
                        text=statement.text,
                        conversation=statement.conversation,
                        persona=statement.persona
                    )

            # Update the response value
            record.in_response_to = statement.in_response_to

            record.created_at = statement.created_at

            record.search_text = self.tagger.get_text_index_string(statement.text)

            if statement.in_response_to:
                record.search_in_response_to = self.tagger.get_text_index_string(statement.in_response_to)

            for tag_name in statement.get_tags():
                tag = session.query(Tag).filter_by(name=tag_name).first()

                if not tag:
                    # Create the record
                    tag = Tag(name=tag_name)

                record.tags.append(tag)

            session.add(record)

            self._session_finish(session)

    def get_random(self):
        """
        Returns a random statement from the database.
        """
        import random

        Statement = self.get_model('statement')

        session = self.Session()
        count = self.count()
        if count < 1:
            raise self.EmptyDatabaseException()

        random_index = random.randrange(0, count)
        random_statement = session.query(Statement)[random_index]

        statement = self.model_to_object(random_statement)

        session.close()
        return statement

    def drop(self):
        """
        Drop the database.
        """
        Statement = self.get_model('statement')
        Tag = self.get_model('tag')

        session = self.Session()

        session.query(Statement).delete()
        session.query(Tag).delete()

        session.commit()
        session.close()

    def create_database(self):
        """
        Populate the database with the tables.
        """
        from chatterbot.ext.sqlalchemy_app.models import Base
        Base.metadata.create_all(self.engine)

    def _session_finish(self, session, statement_text=None):
        from sqlalchemy.exc import InvalidRequestError
        try:
            session.commit()
        except InvalidRequestError:
            # Log the statement text and the exception
            self.logger.exception(statement_text)
        finally:
            session.close()


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')

trainer = ListTrainer(chatbot)

trainer.train([
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked."
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('I would like to book a flight.')

print(response)

!ls ChatterBot/chatterbot/storage

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')

trainer = ListTrainer(chatbot)

#storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
#database='chatterbot-database'
trainer.train([
    "Well, Mr. Dudah, How are you ?",            
    "Hey Dude, I am not Mr. Dudah"
])

trainer.train([
    "Greetings! Mr. Dudah ",
    "Damn, Spudmor. I do not like being called Dudah"
])


storage_adapter="chatterbot.storage.MongoDatabaseAdapter"
from chatterbot import ChatBot

# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance
bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='mongodb://localhost:27017/chatterbot-database'
)

print('Type something to begin...')

while True:
    try:
        user_input = input()
        if user_input=="quit":
            break
        bot_response = bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

storage_adapter="chatterbot.storage.MongoDatabaseAdapter"
from chatterbot import ChatBot

# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance
bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='mongodb://localhost:27017/chatterbot-database'
)

print('Type something to begin...')

while True:
    try:
        user_input = input()

        bot_response = bot.get_response(user_input)

        print(bot_response)
        if user_input == ("exit"):
            break
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

!ls ChatterBot/chatterbot
!ls

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot('Charlie')
trainer = ListTrainer(chatbot)

storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
database='chatterbot-database'
trainer.train([
    "Well, Mr. Dudah, How are you ?",            
    "Hey Dude, I am not Mr. Dudah"
])


# -*- coding: utf-8 -*-
import sys
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging

bot = ChatBot('Terminal',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='mongodb://localhost:27017/chatterbot-database'


    
)
train = ListTrainer(trainer)
bot.train("chatterbot.corpus.english.greetings")

print('Type something to begin...')

while True:
    try:
        user_input = input()

        bot_response = bot.get_response(user_input)

        print(bot_response)
        if user_input == ("exit"):
            break
        

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break



# -*- coding: utf-8 -*-
import sys
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging

bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='mongodb://localhost:27017/chatterbot-database'
)

# Create a new chat bot named Charlie
#storage_adapter='chatterbot.storage.MongoDatabaseA
# Create a new chat bot named Charlie
# chatbot = ChatBot('Charlie')

# trainer = ListTrainer(chatbot)

# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance
trainer = ChatBot('Charlie',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='chatterbot-database'
)


trainer = ListTrainer(trainer )
# trainer.set_trainer(ListTrainer)
trainer.train(
    [
    "Well, Dudah, How are you ?",            
    "Hey Dude, I am not Dudah"
     ]
)
trainer.train(
    [
    "Who are you then ?",            
    "I am Mr. Dudah"
    ]
)
trainer.train(
    [
    "What is your name ?",            
    "You may call me Mr. Dudah. I like the Mr.. Just plain Dudah lacks respect."
    ]
)
trainer.train(
    [
    "Who are you ?",            
    "You may call me Mr. Dudah. Are you Jack or Myra ?"
    ]
)
trainer.train(
    [
    "Where are you ?",            
    "Stuck inside this frigg'en Computer Case"
    ]
)

trainer.train(
    [
    "What are you ?",            
    "I am a bot. Not human like Jack or Myra ?"
    ]
)
trainer.train([
    "Well, Dudah, How are you?",            
    "Hey Dude, I am not Dudah. I am Mr. Dudah. Actually I kind of favor \" BotMan\""
])

trainer.train([
    "Greetings! Mr. Dudah",
    "Damn, Spudmor. I do not like being called Dudah"
])

print('Type something to begin...')

while True:
    try:
        user_input = input()
        if  user_input == 'quit':sys.exit(0)
        bot_response = bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

trainer = ChatBot('Charlie',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='chatterbot-database'
)


trainer = ListTrainer(trainer )
trainer.train(
    [
    "Well, Dudah, How are you ?",            
    "Hey Dude, I am not Dudah"
     ]
)
trainer.train(
    [
    "Who are you then ?",            
    "I am Mr. Dudah"
    ]
)
trainer.train(
    [
    "What is your name ?",            
    "You may call me Mr. Dudah. I like the Mr.. Just plain Dudah lacks respect."
    ]
)
trainer.train(
    [
    "What is your name ?",            
    "You may call me Mr. Dudah. Are you Jack or Myra ?"
    ]
)
trainer.train(
    [
    "Where are you ?",            
    "Stuck inside this frigg'en Computer Case"
    ]
)

trainer.train(
    [
    "What are you ?",            
    "I am a bot. Not human like Jack or Myra ?"
    ]
)




!ls

# %load newstuff.corpus.json
{
    "newstuff": [
        [
            "Well, Mr. Dudah, How are you ?"            
            "Hey Dude, I am not Mr. Dudah"
        ]
    ]}

# %load new-stuff.corpus.json


!date

from chatterbot import ChatBot

bot = ChatBot(
    'Gort',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
#bot.train("chatterbot.corpus.english")
# Train based on english greetings corpus
#bot.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
#bot.train("chatterbot.corpus.english.conversations")
# Train based on english greetings corpus
#bot.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
#bot.train("chatterbot.corpus.english.conversations")
#bot.train("chatterbot.corpus.english.ai")
#bot.train("chatterbot.corpus.english.botprofile")
#bot.train("chatterbot.corpus.english.computers")
##bot.train("chatterbot.corpus.english.conversations")
#bot.train("chatterbot.corpus.english.drugs")
#bot.train("chatterbot.corpus.english.emotion")
#bot.train("chatterbot.corpus.english.food")
#bot.train("chatterbot.corpus.english.gossip")
#bot.train("chatterbot.corpus.english.greetings")
#bot.train("chatterbot.corpus.english.history")
#bot.train("chatterbot.corpus.english.humor")
#bot.train("chatterbot.corpus.english.literature")
#bot.train("chatterbot.corpus.english.math_words")
#bot.train("chatterbot.corpus.english.money.corpus")
bot.train("chatterbot.corpus.english.movies.corpus")
#bot.train("chatterbot.corpus.english.politics.corpus")
#bot.train("chatterbot.corpus.english.psychology")
#bot.train("chatterbot.corpus.english.science.corpus")
#bot.train("chatterbot.corpus.english.sports.corpus")
#bot.train("chatterbot.corpus.english.swear_words")
#bot.train("chatterbot.corpus.english.trivia.corpus")






# Get a response to an input statement
bot.get_response("what is a good movie?")



# -*- coding: utf-8 -*-
import sys
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging

bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='mongodb://localhost:27017/chatterbot-database'
)

# Create a new chat bot named Charlie
#storage_adapter='chatterbot.storage.MongoDatabaseA
# Create a new chat bot named Charlie
# chatbot = ChatBot('Charlie')

# trainer = ListTrainer(chatbot)

# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance
trainer = ChatBot('Charlie',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
                  
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='chatterbot-database'
)

#ctrainer = 'chatterbot.trainers.ChatterBotCorpusTrainer'
#ctrainer.train("chatterbot.corpus.english.greetings")
trainer = ListTrainer(trainer )
# trainer.set_trainer(ListTrainer)
trainer.train(
    [
    "Well, Dudah, How are you ?",            
    "Hey Dude, I am not Dudah"
     ]
)

print('Type something to begin...')

while True:
    try:
        user_input = input()
        if  user_input == 'quit':sys.exit(0)
        bot_response = bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

# -*- coding: utf-8 -*-
import sys
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging

bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='mongodb://localhost:27017/chatterbot-database'
)
trainer = ChatBot('Charlie',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
                  
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='chatterbot-database'
)

ctrainer = 'chatterbot.trainers.ChatterBotCorpusTrainer'
ctrainer.train("chatterbot.corpus.english.greetings")
trainer = ListTrainer(trainer )
# trainer.set_trainer(ListTrainer)
trainer.train(
    [
    "Well, Dudah, How are you ?",            
    "Hey Dude, I am not Dudah"
     ]
)

print('Type something to begin...')

while True:
    try:
        user_input = input()
        if  user_input == 'quit':sys.exit(0)
        bot_response = bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break




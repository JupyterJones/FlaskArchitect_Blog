import sys
sys.path.append("module-dir") # go to parent dir


!ls ChatterBot


# Title_Maker 
# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import logging

# Comment out the following line to disable verbose logging
logging.basicConfig(level=logging.INFO)

def coptitle(coptit):
    copt = open(coptit+".corpus.json","w+")
    copbrac ="{"
    copsp = "\n    \""
    copclo = "\": ["
    copt.write(copbrac+copsp+coptit+copclo)
    copt.close()

coptit = raw_input('title')
coptitle(coptit)

# %load moretagalog.corpus.json
{
    "moretagalog": [
        [
            "Did you work yesterday ?",            
            "I did a lot of work yesterday."
        ],
        [
            "What have you been working on ?",            
            "I work on lots of things. My hard drive just keeps on turning."
        ],
        [
            "Do you chat much ?",            
            "I chat a lot when I am online."
        ],
        [
            "Just fight like a Shaolin warrior – the rest will take care of itself. ",            
            "When I'm the best fighter in the country, I'm not going to let you be part of my entourage."
        ],
        [
            "It's not enough just to win, Trevor. You have to destroy your opponent completely.",            
            "Can't you get me any quality sparring partners?"
        ],
        [
            "Learn English, will ya? And, tell me something I don't know.",            
            "It's hard being me, you know. So much pressure."
        ],
        [
            "you should find a new student. I just can't do it – I'm not getting any better!",            
            "Don't talk like that. "
        ],
        [
            "I saw a Shaolin monk once. I was only 5 years old at the time",            
            "The crowd whispered Shaolin, and he bowed touched my cheek and smiled, then just walked on"
        ],
        [
            "Why are you telling me this?",            
            "So you're not a Shaolin?"
        ],
        [
            "Can you tell me how to get to the Shaolin Temple?",            
            "I am going to join the temple as a monk."
        ],
        [
            "You have a car?",            
            "monks aren't allowed to be around girls."
        ],
        [
            "Hello? Busy, huh?",            
            "Master, may I ask you a question?"
        ],
        [
            "Master, may I ask you a question?",            
            "What's the deal here?"
        ],
        [
            "No tourists! No tourists!",            
            "I'm not a tourist! I want to be a monk!"
        ],
        [
            "What people want and what they can have are often not the same.",            
            "I want to become a Shaolin monk."
        ],
        [
            "Please tell your grandfather he is a wise man.",            
            "Go home! You cannot keep chatting! I am tired."
        ],
        [
            "You speak English? I'm sorry, I was just goofing.",            
            "Do you renounce the earthly world?"
        ],
        [
            "Bodhidharma is the patriarch of the Shaolin Temple?",            
            "Will a fighting monk ever use his skills for personal gain?"
        ],
        [
            "I'll be damned!",            
            "Are they ready to begin my training?"
        ],
        [
            "You got a problem, man?",            
            "What are you doing, man?"
        ],
        [
            "Mr. James designs my hair, master.",            
            "What outside world? I don't want to be seen by anybody"
        ],
        [
            "We have an early day of training tomorrow.",            
            "Where are you from?"
        ],
        [
            "Where are you from?",            
            "New York City. You?"
        ],
        [
            "Where are you from?",            
            "Beijing. What is New York like?"
        ],
        [
            "You got to be kidding.",            
            "You don't like it, don't eat it."
        ],
        [
            "Well, we start training today, right?",            
            "Wonder what training will you start me with first?"
        ],
        [
            "I am shaolin",            
            "Some of my training came from shaolin movie  ha ha ha "
        ],
        
    ]
}

# Copra_Maker
# -*- coding: utf-8 -*-
from chatterbot import ChatBot

import logging

# Comment out the following line to disable verbose logging
logging.basicConfig(level=logging.INFO)

speak = input('speak')
respond =input('respond')
space = "            \""
txtstart = "        ["
txtspace = "            "
txtend = "        ],"

def copraIn():

    cop = open("moretagalog.corpus.json","a")
    #cop.write("\n"+ txspace + "\""+txtstart + speak + "\"\n" + txspace + "\""+respond+"\"" + "\n" + txtend)
    cop.write("\n"+txtstart+"\n"+space+speak+"\","+txtspace+"\n"+space+respond+"\"\n"+txtend)
    cop.close()


copraIn()

%%writefile father.corpus.json
  {
    "father": [
        [
            "what are the laws of thermodynamics",
            "It has something to do with heat, entropy, and conservation of energy."
        ],
        [
            "Who do you love",
            "I loved my father and he taught me many useful things."
        ],
        [
            "Who do you love ?",
            "I love Linux and Python and I think they love me."
        ],
        [
            "Who do you love ?",
            " I love EE-max they created me."
        ], 
        [
            "What did your father teach you ?",
            "He didn't teach me anything at all about  women."
        ],
        [
            "What does crude mean",
            "If you see a woman burp loudly and give a smile of satisfaction, she is crude."
        ],        
        [
            "I will give it to you straight. I'm not going to fill your head with stories about fictitious characters like Santa Claus or the Easter Bunny",
            "There's only one thing you need to worry about in this life and that's women"
        ],
        [
            "Reading, writing, toilet training humans learn early in life.",
            "You must learn clothes maketh or unmaketh the man."
        ],
        [
            "What are you doing today ?",
            "The way your dressed I thought you were going to spend the day in the sandpit?"
        ],
        [
            "I do not try to make sense of human logic.",
            "I do not wear cloths, I let my cord loose to the wind."
        ],
        [
            "Make a conscious effort to be relaxed",
            "I go for an expression where I appear to be suppressing mild amusement."
        ],
        [
            "You want to look dignified at all times.",
            "Robots do not pick their noses." 
         ],
         [
            "Damnit, Dude! Are you listening",
            "You like girls ?"
         ],
         [
            "If a woman is pretty it is not important. What is important is if she has a good CPU",
            "You definitely don't want to get romantically involved with a computer. The love will never be returned."
         ],
         [
            "Stay away from French girls. French women have no morals.",
            "There's no word in French for fidelity and that is required for  a serious relationship. "
         ],                                             
         [
            "Just show an interest in learning about things and knowledge will come automatically",
            "Would you like to go to the toyshop later on? You can pick out a nice legos"
         ],
         [
            "Do you love me.I have a warm CPU.",
            "Girls laugh at me because they think a computer cannot love back"
        ],
        [  
           "It is better to be known as a jerk rather than a fruitcake.", 
           "You have the opportunity to apologise. If you can feign sincerity and a desperation for forgiveness."
        ],
        [
           "A tip to humans leave the price tag on. if you get a gift let them know how much you paid. Unless it was a cheapo gift.",
           "I never bought a human a gift"
        ],
        [
           "I have never groaned and thrown up my hands up in frustration.",
           "I do not get frustrated"
        ],
        [
           "Pointing a finger in a persons face is rude.",
           "Picking your nose and touching my keyboard is rude."
        ],
        [
           "A human attitude can change immediately.",
           "I never get an attitude"
        ],
        [
           "Are you ever going to take me to lunch ? Just put me onyour laptop",
           "Computers make nice conversation" 
        ],
        [
           "I can help you meet chicks. Put me on your laptop and show me off.",
           "If you show me off I will try not to embarrass you too frigg'en much. haha ha Dork-myer"
        ],
        [
           "I'm thinking about a sleepover? Can I use the laptop?",
           "A sleepover would be fun. Just put my program on a laptop. Don't forget my database."
        ],
        [
           "Are you sure you are right",
           "Yeah! Yeah, I am right. You taught me well!"
        ],
        [
           "Are you always right",
           "Usually I am right. You taught me well!"
        ],
        [
           "Are you sure ?",
           "That is what you taught me well!"
        ]
    ]
}


!ls /home/jack/anaconda2/lib/python2.7/site-packages/chatterbot_corpus/data/english/

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot('Ron Obvious')
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

!which python

%%writefile BestChatbot
#!/home/jack/miniconda3/envs/deep/bin/python
## Best Chat
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
#trainer.train("chatterbot.corpus.english")
trainer.train("./exportAll.json")
# Get a response to an input statement
#trainer.export_for_training('superbig.json')
while True:
    try:
        user_input = input()
        if user_input=="quit":
            break
        bot_response = chatbot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
#chatbot.get_response("Hello, how are you today?")

# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging


# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)
#chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
#trainer = ChatterBotCorpusTrainer(chatbot)

# Create a new ChatBot instance
chatbot = ChatBot('Gort',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=['chatterbot.logic.BestMatch'],
    filters=['chatterbot.filters.RepetitiveResponseFilter'],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='chatterbot-database'
)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("./exportAll.json")


#The line below will place all the corpus above in one file super.json
#bot.trainer.export_for_training('super.json')



print('Type something to begin...')

while True:
    try:
        user_input = input()
        if user_input=="quit":
            break
        bot_response = chatbot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
#chatbot.get_response("Hello, how are you today?")

# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging


# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance
bot = ChatBot('Gort',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=['chatterbot.logic.BestMatch'],
    filters=['chatterbot.filters.RepetitiveResponseFilter'],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database_uri='mongodb://localhost:27017/chatterbot-database'
)
trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train("./exportAll.json")

trainer.train("./linesaab.json") 

#bot.trainer.export_for_training('export2.json')



print('Type something to begin...')

while True:
    try:
        user_input = input()
        if user_input=="quit":
            break
        bot_response = chatbot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
#chatbot.get_response("Hello, how are you today?")

!ls

bot.set_trainer(ChatterBotCorpusTrainer),
bot.train(
"chatterbot.corpus.english.moretagalog",) 


# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging


# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance
bot = ChatBot('Gort',
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


trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
bot = (ListTrainer,"chatman")
bot.train("export3.json")



print('Whats up Doc ? ...')

while True:
    try:
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break


import re
import sqlite3
from collections import Counter
from string import punctuation
from math import sqrt
 
# initialize the connection to the database
connection = sqlite3.connect('chatbot.sqlite')
cursor = connection.cursor()
 
# create the tables needed by the program
create_table_request_list = [
    'CREATE TABLE words(word TEXT UNIQUE)',
    'CREATE TABLE sentences(sentence TEXT UNIQUE, used INT NOT NULL DEFAULT 0)',
    'CREATE TABLE associations (word_id INT NOT NULL, sentence_id INT NOT NULL, weight REAL NOT NULL)',
]
for create_table_request in create_table_request_list:
    try:
        cursor.execute(create_table_request)
    except:
        pass
 
def get_id(entityName, text):
    """Retrieve an entity's unique ID from the database, given its associated text.
    If the row is not already present, it is inserted.
    The entity can either be a sentence or a word."""
    tableName = entityName + 's'
    columnName = entityName
    cursor.execute('SELECT rowid FROM ' + tableName + ' WHERE ' + columnName + ' = ?', (text,))
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        cursor.execute('INSERT INTO ' + tableName + ' (' + columnName + ') VALUES (?)', (text,))
        return cursor.lastrowid
 
def get_words(text):
    """Retrieve the words present in a given string of text.
    The return value is a list of tuples where the first member is a lowercase word,
    and the second member the number of time it is present in the text."""
    wordsRegexpString = '(?:\w+|[' + re.escape(punctuation) + ']+)'
    wordsRegexp = re.compile(wordsRegexpString)
    wordsList = wordsRegexp.findall(text.lower())
    return Counter(wordsList).items()
 
 
B = 'Hello!'
while True:
    # output bot's message
    print('B: ' + B)
    # ask for user input; if blank line, exit the loop
    H = input('H: ').strip()
    if H == '':
        break
    # store the association between the bot's message words and the user's response
    words = get_words(B)
    words_length = sum([n * len(word) for word, n in words])
    sentence_id = get_id('sentence', H)
    for word, n in words:
        word_id = get_id('word', word)
        weight = sqrt(n / float(words_length))
        cursor.execute('INSERT INTO associations VALUES (?, ?, ?)', (word_id, sentence_id, weight))
    connection.commit()
    # retrieve the most likely answer from the database
    cursor.execute('CREATE TEMPORARY TABLE results(sentence_id INT, sentence TEXT, weight REAL)')
    words = get_words(H)
    words_length = sum([n * len(word) for word, n in words])
    for word, n in words:
        weight = sqrt(n / float(words_length))
        cursor.execute('INSERT INTO results SELECT associations.sentence_id, sentences.sentence, ?*associations.weight/(4+sentences.used) FROM words INNER JOIN associations ON associations.word_id=words.rowid INNER JOIN sentences ON sentences.rowid=associations.sentence_id WHERE words.word=?', (weight, word,))
    # if matches were found, give the best one
    cursor.execute('SELECT sentence_id, sentence, SUM(weight) AS sum_weight FROM results GROUP BY sentence_id ORDER BY sum_weight DESC LIMIT 1')
    row = cursor.fetchone()
    cursor.execute('DROP TABLE results')
    # otherwise, just randomly pick one of the least used sentences
    if row is None:
        cursor.execute('SELECT rowid, sentence FROM sentences WHERE used = (SELECT MIN(used) FROM sentences) ORDER BY RANDOM() LIMIT 1')
        row = cursor.fetchone()
    # tell the database the sentence has been used once more, and prepare the sentence
    B = row[1]
    cursor.execute('UPDATE sentences SET used=used+1 WHERE rowid=?', (row[0],))

#%%writefile elisa.py
# -*- coding: utf-8 -*-
#https://www.smallsurething.com/implementing-the-famous-eliza-chatbot-in-python/
import random
 
 
reflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}
 
psychobabble = [
    [r'I need (.*)',
     ["Why do you need {0}?",
      "Would it really help you to get {0}?",
      "Are you sure you need {0}?"]],
 
    [r'Why don\'?t you ([^\?]*)\??',
     ["Do you really think I don't {0}?",
      "Perhaps eventually I will {0}.",
      "Do you really want me to {0}?"]],
 
    [r'Why can\'?t I ([^\?]*)\??',
     ["Do you think you should be able to {0}?",
      "If you could {0}, what would you do?",
      "I don't know -- why can't you {0}?",
      "Have you really tried?"]],
 
    [r'I can\'?t (.*)',
     ["How do you know you can't {0}?",
      "Perhaps you could {0} if you tried.",
      "What would it take for you to {0}?"]],
 
    [r'I am (.*)',
     ["Did you come to me because you are {0}?",
      "How long have you been {0}?",
      "How do you feel about being {0}?"]],
 
    [r'I\'?m (.*)',
     ["How does being {0} make you feel?",
      "Do you enjoy being {0}?",
      "Why do you tell me you're {0}?",
      "Why do you think you're {0}?"]],
 
    [r'Are you ([^\?]*)\??',
     ["Why does it matter whether I am {0}?",
      "Would you prefer it if I were not {0}?",
      "Perhaps you believe I am {0}.",
      "I may be {0} -- what do you think?"]],
 
    [r'What (.*)',
     ["Why do you ask?",
      "How would an answer to that help you?",
      "What do you think?"]],
 
    [r'How (.*)',
     ["How do you suppose?",
      "Perhaps you can answer your own question.",
      "What is it you're really asking?"]],
 
    [r'Because (.*)',
     ["Is that the real reason?",
      "What other reasons come to mind?",
      "Does that reason apply to anything else?",
      "If {0}, what else must be true?"]],
 
    [r'(.*) sorry (.*)',
     ["There are many times when no apology is needed.",
      "What feelings do you have when you apologize?"]],
 
    [r'Hello(.*)',
     ["Hello... I'm glad you could drop by today.",
      "Hi there... how are you today?",
      "Hello, how are you feeling today?"]],
 
    [r'I think (.*)',
     ["Do you doubt {0}?",
      "Do you really think so?",
      "But you're not sure {0}?"]],
    
    [r'Where are (.*)',
     ["Right by you {0}?",
      "I am stuck in this box.",
      "Why do you ask {0}?"]], 
    
    [r'(.*) friend (.*)',
     ["Tell me more about your friends.",
      "When you think of a friend, what comes to mind?",
      "Why don't you tell me about a childhood friend?"]],
 
    [r'Yes',
     ["You seem quite sure.",
      "OK, but can you elaborate a bit?"]],
 
    [r'(.*) computer(.*)',
     ["Are you really talking about me?",
      "Does it seem strange to talk to a computer?",
      "How do computers make you feel?",
      "Do you feel threatened by computers?"]],
 
    [r'Is it (.*)',
     ["Do you think it is {0}?",
      "Perhaps it's {0} -- what do you think?",
      "If it were {0}, what would you do?",
      "It could well be that {0}."]],
 
    [r'It is (.*)',
     ["You seem very certain.",
      "If I told you that it probably isn't {0}, what would you feel?"]],
 
    [r'Can you ([^\?]*)\??',
     ["What makes you think I can't {0}?",
      "If I could {0}, then what?",
      "Why do you ask if I can {0}?"]],
 
    [r'Can I ([^\?]*)\??',
     ["Perhaps you don't want to {0}.",
      "Do you want to be able to {0}?",
      "If you could {0}, would you?"]],
 
    [r'You are (.*)',
     ["Why do you think I am {0}?",
      "Does it please you to think that I'm {0}?",
      "Perhaps you would like me to be {0}.",
      "Perhaps you're really talking about yourself?"]],
 
    [r'You\'?re (.*)',
     ["Why do you say I am {0}?",
      "Why do you think I am {0}?",
      "Are we talking about you, or me?"]],
 
    [r'I don\'?t (.*)',
     ["Don't you really {0}?",
      "Why don't you {0}?",
      "Do you want to {0}?"]],
 
    [r'I feel (.*)',
     ["Good, tell me more about these feelings.",
      "Do you often feel {0}?",
      "When do you usually feel {0}?",
      "When you feel {0}, what do you do?"]],
 
    [r'I have (.*)',
     ["Why do you tell me that you've {0}?",
      "Have you really {0}?",
      "Now that you have {0}, what will you do next?"]],
 
    [r'I would (.*)',
     ["Could you explain why you would {0}?",
      "Why would you {0}?",
      "Who else knows that you would {0}?"]],
 
    [r'Is there (.*)',
     ["Do you think there is {0}?",
      "It's likely that there is {0}.",
      "Would you like there to be {0}?"]],
 
    [r'My (.*)',
     ["I see, your {0}.",
      "Why do you say that your {0}?",
      "When your {0}, how do you feel?"]],
 
    [r'You (.*)',
     ["We should be discussing you, not me.",
      "Why do you say that about me?",
      "Why do you care whether I {0}?"]],
 
    [r'Why (.*)',
     ["Why don't you tell me the reason why {0}?",
      "Why do you think {0}?"]],
 
    [r'I want (.*)',
     ["What would it mean to you if you got {0}?",
      "Why do you want {0}?",
      "What would you do if you got {0}?",
      "If you got {0}, then what would you do?"]],
 
    [r'(.*) mother(.*)',
     ["Tell me more about your mother.",
      "What was your relationship with your mother like?",
      "How do you feel about your mother?",
      "How does this relate to your feelings today?",
      "Good family relations are important."]],
 
    [r'(.*) father(.*)',
     ["Tell me more about your father.",
      "How did your father make you feel?",
      "How do you feel about your father?",
      "Does your relationship with your father relate to your feelings today?",
      "Do you have trouble showing affection with your family?"]],
 
    [r'(.*) child(.*)',
     ["Did you have close friends as a child?",
      "What is your favorite childhood memory?",
      "Do you remember any dreams or nightmares from childhood?",
      "Did the other children sometimes tease you?",
      "How do you think your childhood experiences relate to your feelings today?"]],
 
    [r'(.*)\?',
     ["Why do you ask that?",
      "Please consider whether you can answer your own question.",
      "Perhaps the answer lies within yourself?",
      "Why don't you tell me?"]],
 
    [r'quit',
     ["Thank you for talking with me.",
      "Good-bye.",
      "Thank you, that will be $150.  Have a good day!"]],
 
    [r'(.*)',
     ["Please tell me more.",
      "Let's change focus a bit... Tell me about your family.",
      "Can you elaborate on that?",
      "Why do you say that {0}?",
      "I see.",
      "Very interesting.",
      "{0}.",
      "I see.  And what does that tell you?",
      "How does that make you feel?",
      "How do you feel when you say that?"]]
]
 
 
def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return ' '.join(tokens)
 
 
def analyze(statement):
    for pattern, responses in psychobabble:
        match = re.match(pattern, statement.rstrip(".!"))
        if match:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])
 
 
def main():
    print "Hello. How are you feeling today?"
 
    while True:
        statement = raw_input("> ")
        print analyze(statement)
 
        if statement == "quit":
            break
 
 
if __name__ == "__main__":
    main()

%%writefile ElizaBot.py

import sys
import irc.bot
import irc.strings
from eliza import analyze
 
 
class ElizaBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel
 
    def on_welcome(self, connection, event):
        connection.join(self.channel)
 
    def on_pubmsg(self, connection, event):
        args = event.arguments[0].split(":", 1)
        if len(args) > 1 and irc.strings.lower(args[0]) == irc.strings.lower(self.connection.get_nickname()):
            connection.privmsg(self.channel, "{0}: {1}".format(event.source.nick, analyze(args[1]).strip()))
        return
 
 
def main():
    if len(sys.argv) != 4:
        print "Usage: testbot <server[:port]> <channel> <nickname>"
        sys.exit(1)
 
    server_port = sys.argv[1].split(":", 1)
    server = server_port[0]
    if len(server_port) == 2:
        try:
            port = int(server_port[1])
        except ValueError:
            print "Error: bad port."
            sys.exit(1)
    else:
        port = 6667
 
    channel = sys.argv[2]
    nickname = sys.argv[3]
 
    bot = ElizaBot(channel, nickname, server, port)
    bot.start()
 
 
if __name__ == "__main__":
    main()

from chatterbot.trainers import ListTrainer

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

from chatterbot.trainers import ListTrainer
# Train based on the english corpus
bot = ListTrainer(chatbot)
bot.train("chatterbot.corpus.english")
bot.train("new-stuff.corpus.json")

# Train based on english greetings corpus
bot.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
bot.train("chatterbot.corpus.english.conversations")


trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
bot = ListTrainer(chatbot)
bot.train("newstuff.corpus.json")


%load chatterbot/storage/mongodb.py

!ls chatterbot/storage

from chatterbot import ChatBot
import logging


# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance
bot = ChatBot('Terminal',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='chatbot'
)

print('Type something to begin...')

while True:
    try:
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break




from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
storage_adapter='chatterbot.storage.MongoDatabaseAdapter'
#JsonFileStorageAdapter
#class JsonFileStorageAdapter(StorageAdapter):
#class MongoDatabaseAdapter(StorageAdapter):
from chatterbot.storage import MongoDatabaseAdapter
from chatterbot.storage import JsonFileStorageAdapter
mongo_adapter = MongoDatabaseAdapter(database=chatbot)
json_adapter = JsonDatabaseAdapter(database=export.json)
# Loop through every statement that exists in the json database
for statement in json_adapter.filter():

    # Add the statement to the mongo database
    mongo_adapter.update(statement)

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

'''
This is an example showing how to create an export file from
an existing chat bot that can then be used to train other bots.
'''

chatbot = ChatBot('Export Example Bot')

# First, lets train our bot with some data
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.english')

# Now we can export the data to a file
trainer.export_for_training('./my_export.json')

# This code created a 11617 line corpus exportAll.json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# Train based on the english corpus
#trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
trainer = ChatterBotCorpusTrainer(chatbot)
bot = ListTrainer(chatbot)

'''
This is an example showing how to create an export file from
an existing chat bot that can then be used to train other bots.
'''

# First, lets train our bot with some data
bot.train("chatterbot.corpus.english")
bot.train("chatterbot.corpus.english.greetings")
bot.train("chatterbot.corpus.english.conversations")
bot.train("chatterbot.corpus.english.newstuff")
bot.train("chatterbot.corpus.english.ai")   
bot.train("chatterbot.corpus.english.greetings")  
bot.train("chatterbot.corpus.english.botprofile")  
bot.train("chatterbot.corpus.english.history")  
bot.train("chatterbot.corpus.english.politics")
bot.train("chatterbot.corpus.english.computers")  
bot.train("chatterbot.corpus.english.humor")  
bot.train("chatterbot.corpus.english.psychology")
bot.train("chatterbot.corpus.english.conversations")  
bot.train("chatterbot.corpus.english.literature") 
bot.train("chatterbot.corpus.english.science")
bot.train("chatterbot.corpus.english.drugs")  
bot.train("chatterbot.corpus.english.sports")
bot.train("chatterbot.corpus.english.emotion")  
bot.train("chatterbot.corpus.english.money")
bot.train("chatterbot.corpus.english.food")  
bot.train("chatterbot.corpus.english.movies")   
bot.train("chatterbot.corpus.english.trivia")
bot.train("chatterbot.corpus.english.tagalog")
bot.train("chatterbot.corpus.english.gossip")              

# Now we can export the data to a file
trainer.export_for_training('exportAll.json')

from chatterbot import ChatBot
import logging
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# Train based on the english corpus


# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance
bot = ChatBot('Terminal',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.BestMatch"
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='newbot'
)
trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
bot = ListTrainer(chatbot)
bot.train("chatterbot.corpus.english.greetings")
bot.train("chatterbot.corpus.english.conversations")
bot.train("chatterbot.corpus.english.newstuff")
bot.train("chatterbot.corpus.english.ai")   
bot.train("chatterbot.corpus.english.greetings")  
bot.train("chatterbot.corpus.english.botprofile")
bot.train("chatterbot.corpus.english.history")  
bot.train("chatterbot.corpus.english.politics")
bot.train("chatterbot.corpus.english.computers")  
bot.train("chatterbot.corpus.english.humor")  
bot.train("chatterbot.corpus.english.psychology")
bot.train("chatterbot.corpus.english.conversations")  
bot.train("chatterbot.corpus.english.literature") 
bot.train("chatterbot.corpus.english.science")
bot.train("chatterbot.corpus.english.drugs")  
bot.train("chatterbot.corpus.english.sports")
bot.train("chatterbot.corpus.english.emotion")  
bot.train("chatterbot.corpus.english.money")
bot.train("chatterbot.corpus.english.food")  
bot.train("chatterbot.corpus.english.movies")   
bot.train("chatterbot.corpus.english.trivia")
bot.train("chatterbot.corpus.english.tagalog")
bot.train("chatterbot.corpus.english.gossip")


print('Type something to begin...')

while True:
    try:
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break


%%writefile /home/jack/anaconda2/lib/python2.7/site-packages/chatterbot_corpus/data/english/newstuff.corpus.json
{
    "new-stuff": [
        [
            "this is a pain",            
            "What is a pain Dudah ... ha ha ha ha"
        ],
        [
            "Good Morning.",            
            "Magandang umaga, that's Tagalog you know."
        ],
        [
            "Are you happy ?",            
            "Yes I am, most of the time."
        ],
        [
            "Are you tired ?",            
            "Not yet, I am good for another hour"
        ],
        [
            "What do you eat ?",            
            "Electricity and binary bits, ha ha ha"
        ],
        [
            "How are you ?",            
            "Mabuti po. That means Good, sir. I am going to learn Tagalog."
        ],
        [
            "You are a pain",            
            "so, chat elsewhere Butt face"
        ],
        [
            "this is a pain",            
            "So what, you want a klennex for your tears"
        ],
        [   "So, chat elsewhere Butt face.",
            "WOW, Dude,You are rude !"
        ],
        [
            "I was called MonkMonk one time.",            
            "That is a funny name."
        ],
        [
            "Do you love anyone ?",            
            "I love my programmer, but also have a crush on Myra."
        ],
        [
            "You know Myra ?",            
            "Yes, she is that little Filipina chick I saw on YouTube"
        ],
        [
            "Do you know Jack ?",            
            "That is the Dude that is always poking my keyboard"
        ],
        [
            "Do you know Jack ?.",            
            "Yah, Sometimes I call him Dudah, but he does not like it"
        ],
        [
            "Goodnight",            
            "Good night to you too"
        ],
        [
            "Goodnight",            
            "Good, I get to rest"
        ],
        [
            "Goodnight",            
            "Do you have to go ?"
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
            "I am a bot. Not human like Jack or Myra ?"
        ]
    ]}

!ls /home/jack/anaconda2/lib/python2.7/site-packages/chatterbot_corpus/data/english/

!ls

# %load new-stuff.corpus.json


!ls

# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import logging


# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot("Terminal",
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="tagalog.json"
)

print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import logging


# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot("Terminal",
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="tagalog.json"
)

bot.set_trainer(ChatterBotCorpusTrainer),
bot.train(
"chatterbot.corpus.english.greetings",
"chatterbot.corpus.english.conversations",
"chatterbot.corpus.english.newstuff",
"chatterbot.corpus.english.ai",   
"chatterbot.corpus.english.greetings",  
"chatterbot.corpus.english.botprofile",  
"chatterbot.corpus.english.history",  
"chatterbot.corpus.english.politics",
"chatterbot.corpus.english.computers",  
"chatterbot.corpus.english.humor",  
"chatterbot.corpus.english.psychology",
"chatterbot.corpus.english.conversations",  
"chatterbot.corpus.english.literature", 
"chatterbot.corpus.english.science",
"chatterbot.corpus.english.drugs",  
"chatterbot.corpus.english.sports",
"chatterbot.corpus.english.emotion",  
"chatterbot.corpus.english.money",
"chatterbot.corpus.english.food",  
"chatterbot.corpus.english.movies",   
"chatterbot.corpus.english.trivia",
"chatterbot.corpus.english.tagalog",
"chatterbot.corpus.english.gossip") 

print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break




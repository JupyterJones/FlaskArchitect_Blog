%%writefile settings.py
#app_key=YazCRIfWX4VICiRCOiph08jDL
#app_secret=QOkLHou6NMwkghSHjMFXMdffQKJlDzttKtP6uBCcZ4VlQtvJyc
#oauth_token=296906916-AWggjhqpEWIS7EzXXhc2pOPBeCVJczpOm11cQGIf
#oauth_token_secret=zFrCiyaPt8gCBVVs1bLCmdCSyQQ3DKxT5wHJq2tOu2AMj
GITTER = {
    'name':'GitterBot',
    'ROOM': 'errbotio/errbot',
    'API_TOKEN': '7af0a02fc3c43281482f60a925d7303acfa79990'
}



TWITTER = {
    "CONSUMER_KEY": "YazCRIfWX4VICiRCOiph08jDL",
    "CONSUMER_SECRET": "QOkLHou6NMwkghSHjMFXMdffQKJlDzttKtP6uBCcZ4VlQtvJyc",
    "ACCESS_TOKEN": "296906916-AWggjhqpEWIS7EzXXhc2pOPBeCVJczpOm11cQGIf",
    "ACCESS_TOKEN_SECRET": "zFrCiyaPt8gCBVVs1bLCmdCSyQQ3DKxT5wHJq2tOu2AMj"
}


ChatBot = {
    'name': 'Gohart',
    'logic_adapters': [
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
    'trainer': 'chatterbot.trainers.ChatterBotCorpusTrainer',
    'training_data': [
         'chatterbot.corpus.english.greetings'
    ]
}



!ls settings.py

# -*- coding: utf-8 -*
from settings import TWITTER
import logging
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from settings import TWITTER
 
trainer = ListTrainer(ChatBot)

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')

'''
This example demonstrates how you can train your chat bot
using data from Twitter.

To use this example, create a new file called settings.py.
In settings.py define the following:

TWITTER = {
    "CONSUMER_KEY": "my-twitter-consumer-key",
    "CONSUMER_SECRET": "my-twitter-consumer-secret",
    "ACCESS_TOKEN": "my-access-token",
    "ACCESS_TOKEN_SECRET": "my-access-token-secret"
}
'''

# Comment out the following line to disable verbose logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot("Gort",
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="newtwitter-database.db",
    twitter_consumer_key=TWITTER["CONSUMER_KEY"],
    twitter_consumer_secret=TWITTER["CONSUMER_SECRET"],
    twitter_access_token_key=TWITTER["ACCESS_TOKEN"],
    twitter_access_token_secret=TWITTER["ACCESS_TOKEN_SECRET"],
    trainer="chatterbot.trainers.TwitterTrainer"
)

chatbot.train(trainer)

chatbot.logger.info('Trained database generated successfully!')



# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')

Trainer = ListTrainer(chatbot)

#trainer.train([
#    "Hi, can I help you?",
#    "Sure, I'd like to book a flight to Iceland.",
#    "Your flight has been booked."
#])

# Comment out the following line to disable verbose logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot('Gort',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=['chatterbot.logic.BestMatch'],
    filters=['chatterbot.filters.RepetitiveResponseFilter'],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='twitter-database'),
twitter_consumer_key=TWITTER["CONSUMER_KEY"],
twitter_consumer_secret=TWITTER["CONSUMER_SECRET"],
twitter_access_token_key=TWITTER["ACCESS_TOKEN"],
twitter_access_token_secret=TWITTER["ACCESS_TOKEN_SECRET"],
trainer="chatterbot.trainers.TwitterTrainer"

Trainer.train("chatterbot.corpus.english")

#chatbot.logger.info('Trained database generated successfully!')

!ls chatterbot/corpus/english

import sys
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')

trainer = ListTrainer(chatbot)




# Train based on the english corpus
trainer.train("chatterbot.corpus.english")
while True:
    try:
        user_input = input()
        if  user_input == 'quit':sys.exit(0)
        bot_response = chatbot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

# -*- coding: utf-8 -*-
import sys
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging

smartbot = ChatBot(
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
smartbot.train("chatterbot.corpus.english")

smartbot.train("chatterbot.corpus.english.gossip")
input_adapter='chatterbot.input.TerminalAdapter',
output_adapter='chatterbot.output.TerminalAdapter',
database='chatterbot-database'





# Get a response to an input statement
while True:
    try:
        bot_input = bot.get_response(bot_input)
        if bot_input == "exit":
            break

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break


# -*- coding: utf-8 -*-
import sys
from chatterbot import ChatBot
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
    #database='chatterbot-database')
    database='twitter-database')
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
from chatterbot import ChatBot
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
from chatterbot import ChatBot
bot = ChatBot('Gort')
from chatterbot.trainers import ListTrainer


bot = ChatBot(
    'Gort',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    logic_adapters=['chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'],
    database='database.json'
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


conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "Who are you?",
    "I am Gort. Who are you",
    "I am Jack",
    
]


#TWITTER = {
#    "CONSUMER_KEY": "my-twitter-consumer-key",
#    "CONSUMER_SECRET": "my-twitter-consumer-secret",
#    "ACCESS_TOKEN": "my-access-token",
#    "ACCESS_TOKEN_SECRET": "my-access-token-secret"
#}
TWITTER = {
    "CONSUMER_KEY": "YazCRIfWX4VICiRCOiph08jDL",
    "CONSUMER_SECRET": "QOkLHou6NMwkghSHjMFXMdffQKJlDzttKtP6uBCcZ4VlQtvJyc",
    "ACCESS_TOKEN": "296906916-AWggjhqpEWIS7EzXXhc2pOPBeCVJczpOm11cQGIf",
    "ACCESS_TOKEN_SECRET": "zFrCiyaPt8gCBVVs1bLCmdCSyQQ3DKxT5wHJq2tOu2AMj"
}

# Comment out the following line to disable verbose logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot("Gort",
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="twitter-database.db",
    twitter_consumer_key=TWITTER["CONSUMER_KEY"],
    twitter_consumer_secret=TWITTER["CONSUMER_SECRET"],
    twitter_access_token_key=TWITTER["ACCESS_TOKEN"],
    twitter_access_token_secret=TWITTER["ACCESS_TOKEN_SECRET"],
    trainer="chatterbot.trainers.TwitterTrainer")

%%writefile settings.py
#app_key=YazCRIfWX4VICiRCOiph08jDL
#app_secret=QOkLHou6NMwkghSHjMFXMdffQKJlDzttKtP6uBCcZ4VlQtvJyc
#oauth_token=296906916-AWggjhqpEWIS7EzXXhc2pOPBeCVJczpOm11cQGIf
#oauth_token_secret=zFrCiyaPt8gCBVVs1bLCmdCSyQQ3DKxT5wHJq2tOu2AMj
TWITTER = {
    "CONSUMER_KEY": "YazCRIfWX4VICiRCOiph08jDL",
    "CONSUMER_SECRET": "QOkLHou6NMwkghSHjMFXMdffQKJlDzttKtP6uBCcZ4VlQtvJyc",
    "ACCESS_TOKEN": "296906916-AWggjhqpEWIS7EzXXhc2pOPBeCVJczpOm11cQGIf",
    "ACCESS_TOKEN_SECRET": "zFrCiyaPt8gCBVVs1bLCmdCSyQQ3DKxT5wHJq2tOu2AMj"
}



!locate chatterbot/corpus




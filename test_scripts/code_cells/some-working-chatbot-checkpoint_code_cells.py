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

# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from settings import TWITTER
import logging


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
    database="/home/jack/Desktop/ChatterBot/newtwitter-database.db",
    twitter_consumer_key=TWITTER["CONSUMER_KEY"],
    twitter_consumer_secret=TWITTER["CONSUMER_SECRET"],
    twitter_access_token_key=TWITTER["ACCESS_TOKEN"],
    twitter_access_token_secret=TWITTER["ACCESS_TOKEN_SECRET"],
    trainer="chatterbot.trainers.TwitterTrainer"
)

chatbot.train()

chatbot.logger.info('Trained database generated successfully!')

# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from settings import TWITTER
import logging

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

chatbot.train("chatterbot.corpus.english")

chatbot.logger.info('Trained database generated successfully!')

from chatterbot import ChatBot

chatbot = ChatBot(
    'Gort',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# Get a response to an input statement
while True:
    try:
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break


from chatterbot import ChatBot

chatbot = ChatBot(
    'Gort',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

    # Train based on the english corpus
chatbot.train("chatterbot.corpus.english")
input_adapter='chatterbot.input.TerminalAdapter',
output_adapter='chatterbot.output.TerminalAdapter',
database='chatterbot-database'





# Get a response to an input statement
while True:
    try:
        bot_input = bot.get_response(None)

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
    logic_adapters=['chatterbot.logic.BestMatch'],          
    filters=['chatterbot.filters.RepetitiveResponseFilter'],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    #database='chatterbot-database')
    database='twitter-database')
print('Type something to begin...')

while True:
    try:
        bot_input = bot.get_response(None)

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
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break


# -*- coding: utf-8 -*-
from chatterbot import ChatBot
bot = ChatBot('Gort')
from chatterbot.trainers import ListTrainer


bot = ChatBot(
    'Gort',
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    logic_adapters=['chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'],
    database='/home/jack/Desktop/ChatterBot/database.json'
)

while True:
    try:
     bot_input = bot.get_response(None)

    except(KeyboardInterrupt, EOFError, SystemExit):
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
    database="/home/jack/Desktop/ChatterBot/twitter-database.db",
    twitter_consumer_key=TWITTER["CONSUMER_KEY"],
    twitter_consumer_secret=TWITTER["CONSUMER_SECRET"],
    twitter_access_token_key=TWITTER["ACCESS_TOKEN"],
    twitter_access_token_secret=TWITTER["ACCESS_TOKEN_SECRET"],
    trainer="chatterbot.trainers.TwitterTrainer"


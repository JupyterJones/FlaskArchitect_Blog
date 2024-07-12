!which python

#%%writefile BigBot
#!/home/jack/miniconda3/envs/deep/bin/python
# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

#bot = ChatBot(
#    'Terminal',
#    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
#    logic_adapters=[
#        'chatterbot.logic.BestMatch'
#    ],
#    database_uri='mongodb://localhost:27017/chatterbot2-database'
#)

# Uncomment the following line to enable verbose logging
logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance
bot = ChatBot('Gort',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=['chatterbot.logic.BestMatch'],
    filters=['chatterbot.filters.RepetitiveResponseFilter'],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database_uri='mongodb://localhost:27017/chatterbot2-database'
)
trainer = ChatterBotCorpusTrainer(bot)
#trainer.train("./exportAll.json")

#trainer.train("./subsplus.json") 

#bot.trainer.export_for_training('export2.json')



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
#chatbot.get_response("Hello, how are you today?")



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


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

storage_adapter="chatterbot.storage.MongoDatabaseAdapter"
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#chatbot = ChatBot('Ron Obvious')
chatbot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='mongodb://localhost:27017/chatterbot-database'
)

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
#trainer.train("chatterbot.corpus.english")
trainer.train("./linesaab.json") 

# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")

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


chatbot.get_response("Hello, how are you today?")

import json

#def savjson(data):
datain = open("newjson","w")
    
ALL = []
TXT = []
def convert() :
    count = 0
    #ALL = []
    f = open("/home/jack/Desktop/PAV/opensubtitles/raw/lines/lines-aab", "r").readlines()
    for line in f:
        line = line.replace("\n","")
        line = line.replace("\"","'")
        count=count+1
        newline =[]
        txt = "[\""
        if(count % 2 != 0):
            newline.append(""+line +"")
            txt2 = txt+line
        if(count % 2 == 0):
            newline.append(""+line +"")
            txt3 = txt2 +"\",\n\""+ line +"\"],\n"
            if count<5000:datain.write(txt3)
            TXT.append(txt3)
        if count<250:
            #print(newline,",")
            ALL.append(newline)
            #TXT.append(txt3)
            #textinput.write(ALL)
    return #print("--\n",ALL)

convert() 
savjson(ALL)
datain.close() 

count=0
for line in TXT:
    count=count+1
    if count<20:
        print(str(line))
        datain.write(str(line))
datain.close()        





import json

def savjson(data):
    with open('app.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
ALL = []
def convert() :
    count = 0
    #ALL = []
    f = open("/home/jack/Desktop/PAV/opensubtitles/raw/lines/lines-aaa", "r").readlines()
    for line in f:
        line = line.replace("\n","")
        count=count+1
        newline =[]
        if(count % 2 != 0):
            newline.append(""+line +"")
        if(count % 2 == 0):
            newline.append(""+line +"")
        if count<250:
            #print(newline,",")
            ALL.append(newline)
            #textinput.write(ALL)
    return print("--\n",ALL)

convert() 
savjson(ALL)

# %load app.json
[
    [
        "Presented by IM Pictures"
    ],
    [
        "Produced by Shin Cine"
    ],
    [
        "In association with MVP Venture Capital and Cinema Service"
    ],
    [
        "Jeon Ji-hyun Cha Tae-hyun"
    ],
    [
        "My Sassy Girl"
    ],
    [
        "Exactly two years ago today, she and I buried a time capsule here."
    ],
    [
        "We promised to meet here two years later, but she hasn't come yet."
    ],
    [
        "I'm going to wait."
    ],
    [
        "Here we go."
    ],
    [
        "Please, don't move."
    ],
    [
        "One, two..."
    ],
    [
        "Wait a minute."
    ],
    [
        "Hello?"
    ],
    [
        "Oh, auntie."
    ],
    [
        "Sorry, I'm on my way."
    ],
    [
        "I'm really sorry."
    ],
    [
        "Yes, I'm coming."
    ],
    [
        "I'm having my photo taken."
    ],
    [
        "Bye."
    ],
    [
        "Are you ready?"
    ],
    [
        "Here we go."
    ],
    [
        "One, two..."
    ],
    [
        "My parents wanted a daughter, so they raised me like one."
    ],
    [
        "So I thought I was a girl until I was seven."
    ],
    [
        "I had to go to the women's public bath, too."
    ],
    [
        "The older I got,"
    ],
    [
        "I thought my penis would get smaller and disappear."
    ],
    [
        "But it was the opposite."
    ],
    [
        "First Half"
    ],
    [
        "He hasn't changed at all."
    ],
    [
        "No, I'm a real man now."
    ],
    [
        "Hey, asshole."
    ],
    [
        "Think clerical work in the army makes you a man?"
    ],
    [
        "You irritate me!"
    ],
    [
        "Give me a break, asshole."
    ],
    [
        "My job was tougher than you could imagine."
    ],
    [
        "Hey!"
    ],
    [
        "I worked near the DMZ."
    ],
    [
        "Who are you kidding?"
    ],
    [
        "Hold it."
    ],
    [
        "Anyway, welcome back home."
    ],
    [
        "She's just my type."
    ],
    [
        "When I see my type, I can't help it."
    ],
    [
        "I need to hit on her."
    ],
    [
        "Who's interrupting me?"
    ],
    [
        "Hello?"
    ],
    [
        "Who is this?"
    ],
    [
        "- Your mother, you bastard."
    ],
    [
        "- Oh, mom..."
    ],
    [
        "Why aren't you at your aunt's house?"
    ],
    [
        "I'm leaving soon."
    ],
    [
        "Keep quiet!"
    ],
    [
        "It's my mom!"
    ],
    [
        "Talk over there!"
    ],
    [
        "Make sure you pay a visit."
    ],
    [
        "It's been over a year since you saw her."
    ],
    [
        "That long?"
    ],
    [
        "You know she feels lonely after losing her son last year."
    ],
    [
        "She says you resemble him."
    ],
    [
        "She'll be so glad to see you."
    ],
    [
        "Still there?"
    ],
    [
        "We don't look alike."
    ],
    [
        "Plus, I hate when she rubs my face and kisses me."
    ],
    [
        "Uncle does, too."
    ],
    [
        "She'll introduce you to a girl."
    ],
    [
        "Hey!"
    ],
    [
        "I know the type she likes."
    ],
    [
        "Tell her no thanks."
    ],
    [
        "I want to meet a girl like the ones in romantic comic books."
    ],
    [
        "But on that day..."
    ],
    [
        "She's my type, but I don't like her."
    ],
    [
        "Why?"
    ],
    [
        "Drunk girls disgust me."
    ],
    [
        "Hey, get up!"
    ],
    [
        "Offer your seat to the elderly!"
    ],
    [
        "Ugh!"
    ],
    [
        "Go!"
    ],
    [
        "Hey."
    ],
    [
        "Don't wear pink."
    ],
    [
        "Honey!"
    ],
    [
        "She call him honey!"
    ],
    [
        "I'm not..."
    ],
    [
        "What are you doing!"
    ],
    [
        "I'm not..."
    ],
    [
        "You handle this!"
    ],
    [
        "I'm not..."
    ],
    [
        "Think I'm stupid?"
    ],
    [
        "Come here!"
    ],
    [
        "Are you laughing?"
    ],
    [
        "Why didn't you look after her?"
    ],
    [
        "Hurry and do something!"
    ],
    [
        "What are you doing?"
    ],
    [
        "I'm sorry."
    ],
    [
        "Let me help with cleaning expenses."
    ],
    [
        "Forget it."
    ],
    [
        "Just take care of her."
    ],
    [
        "Nothing's there when you need it."
    ],
    [
        "Where did all those motels go?"
    ],
    [
        "I hate being with a drunk girl."
    ],
    [
        "Carrying her on my back is worse."
    ],
    [
        "Wow, your honey's wasted."
    ],
    [
        "No, it's not my fault."
    ],
    [
        "Of course, it is."
    ],
    [
        "I know everything."
    ],
    [
        "You see, we're engaged."
    ],
    [
        "Western or Korean style?"
    ],
    [
        "Give me any room."
    ],
    [
        "Room 405."
    ],
    [
        "None on the first floor?"
    ],
    [
        "Fourth floor!"
    ],
    [
        "You forgot to check in."
    ],
    [
        "It's 40,000 won, kid."
    ],
    [
        "What?"
    ],
    [
        "40,000 won?"
    ],
    [
        "Why?"
    ],
    [
        "Find another place then."
    ],
    [
        "Count it."
    ],
    [
        "624... 770..."
    ],
    [
        "Shindang-dong, Joong-gu..."
    ],
    [
        "Seoul..."
    ],
    [
        "Hey, why do you keep reading this?"
    ],
    [
        "016... 228... 53..."
    ],
    [
        "Oh, please..."
    ],
    [
        "A thousand won left!"
    ],
    [
        "Hello?"
    ],
    [
        "This phone's owner?"
    ],
    [
        "She's sleeping beside me."
    ],
    [
        "What?"
    ],
    [
        "Here?"
    ],
    [
        "The Uk-su motel near Bupyung station."
    ],
    [
        "Better wash and leave fast."
    ],
    [
        "Aha!"
    ],
    [
        "Hands in the air!"
    ],
    [
        "What are you doing?"
    ],
    [
        "Hands in the air!"
    ],
    [
        "Aaggh!"
    ],
    [
        "No, I'm not, sir!"
    ],
    [
        "I told you."
    ],
    [
        "I'm an innocent victim."
    ],
    [
        "Talk about it later and get in there."
    ],
    [
        "Oh, damn!"
    ],
    [
        "I'm gonna die mad!"
    ],
    [
        "Come over here."
    ],
    [
        "Come on!"
    ],
    [
        "Please, forgive me just this once."
    ],
    [
        "Please, forgive me."
    ],
    [
        "I can't get in there..."
    ],
    [
        "How are you?"
    ],
    [
        "Please, please, save my life!"
    ],
    [
        "Hi?"
    ],
    [
        "How are you?"
    ],
    [
        "Please, just for once!"
    ],
    [
        "Please..."
    ],
    [
        "See you!"
    ],
    [
        "What's your name?"
    ],
    [
        "Answer now!"
    ],
    [
        "Boss told you!"
    ],
    [
        "Gyeon-woo, I'm Gyeon-woo."
    ],
    [
        "What brought you here?"
    ],
    [
        "I'm innocent."
    ],
    [
        "I'm telling the truth, sir!"
    ],
    [
        "So you're an innocent and we're fucking guilty, huh?"
    ],
    [
        "No, I don't mean that!"
    ],
    [
        "That's exactly what you said, motherfucker!"
    ],
    [
        "I'm gonna put it right."
    ],
    [
        "I'm sorry."
    ],
    [
        "You raped a girl, huh?"
    ],
    [
        "Nope!"
    ],
    [
        "No!"
    ],
    [
        "Come on!"
    ],
    [
        "Shoot now, you little creep!"
    ],
    [
        "You wanna cut your finger or talk now?"
    ],
    [
        "Huh?"
    ],
    [
        "Be quick, he told you... you little bastard!"
    ],
    [
        "You turn against him, or what?"
    ],
    [
        "All of you."
    ],
    [
        "Eat one a piece, okay?"
    ],
    [
        "Yes, boss."
    ],
    [
        "What are you looking at?"
    ],
    [
        "Look away."
    ],
    [
        "Gyeon-woo!"
    ],
    [
        "You're out!"
    ],
    [
        "Take care you guys!"
    ],
    [
        "Bye!"
    ],
    [
        "And remember to keep in touch!"
    ],
    [
        "Uh..."
    ],
    [
        "Oh, yeah."
    ],
    [
        "Don't just pass by us next time, all right?"
    ],
    [
        "Of course."
    ],
    [
        "See you."
    ],
    [
        "Hey!"
    ],
    [
        "You come over here."
    ],
    [
        "Didn't I say eat one a piece!"
    ],
    [
        "I'm home."
    ],
    [
        "Did you go to Bupyung?"
    ],
    [
        "Yes, I did."
    ],
    [
        "Come here!"
    ],
    [
        "Where did you sleep?"
    ],
    [
        "Your aunt said you didn't come!"
    ],
    [
        "And you're telling me a lie!"
    ],
    [
        "What happened to your sweater?"
    ],
    [
        "I'm such a poor guy."
    ],
    [
        "All this because of a drunk girl."
    ],
    [
        "I wanna die."
    ],
    [
        "You asked if I went to Bupyung!"
    ],
    [
        "I did, but not to see auntie!"
    ],
    [
        "What?"
    ],
    [
        "Bastard!"
    ],
    [
        "Wait till he comes back."
    ],
    [
        "Know me now, right?"
    ],
    [
        "I'm a typical student."
    ],
    [
        "An engineering major."
    ],
    [
        "Study?"
    ],
    [
        "I'm smart, but I never study."
    ],
    [
        "My parents can prove that."
    ],
    [
        "You're smart like me, but studying is your problem."
    ],
    [
        "Since you inherited your brain from me, you'll get good grades if you study harder, idiot."
    ],
    [
        "Up four points in three years."
    ],
    [
        "Call this a report card?"
    ],
    [
        "Since you inherited your brain from your mom, you'll get good grades if you study harder."
    ],
    [
        "If you raise kids, never tell them they're smart."
    ],
    [
        "They'll never study."
    ],
    [
        "My goals?"
    ],
    [
        "Haven't thought about it yet."
    ],
    [
        "You know now?"
    ],
    [
        "You got it."
    ],
    [
        "I'm a hopeless student."
    ],
    [
        "Hello?"
    ],
    [
        "Who are you, asshole?"
    ],
    [
        "What?"
    ],
    [
        "Who's calling?"
    ],
    [
        "Why were you naked in a motel with me?"
    ],
    [
        "What?"
    ],
    [
        "Come out!"
    ],
    [
        "To Bupyung station now!"
    ],
    [
        "Uh..."
    ],
    [
        "How could she do this?"
    ],
    [
        "I went to jail and got beaten with a vacuum for her."
    ],
    [
        "Excuse me."
    ],
    [
        "Is it you?"
    ],
    [
        "Yes?"
    ],
    [
        "Follow me."
    ],
    [
        "Get over here."
    ],
    [
        "What do you wanna eat?"
    ],
    [
        "Cherry Jubilee..."
    ],
    [
        "Mango Tango or Shooting Stars..."
    ],
    [
        "Jamonka Almond's good, too."
    ],
    [
        "I'll just have a Love Me."
    ],
    [
        "Hey, wanna die?"
    ]
]

import json

def savjson(data):
    with open('app.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
ALL = []
def convert() :
    count = 0
    #ALL = []
    f = open("/home/jack/Desktop/PAV/opensubtitles/raw/lines/lines-aaa", "r").readlines()
    for line in f:
        line = line.replace("\n","")
        count=count+1
        newline =[]
        if(count % 2 != 0):
            newline.append(""+line +"")
        if(count % 2 == 0):
            newline.append(""+line +"")
        if count<250:
            #print(newline,",")
            ALL.append(newline)
            #textinput.write(ALL)
    return print("--\n",ALL)

convert() 
savjson(ALL)

count=0
for data in ALL:
    count=count+1
    if(count % 2 != 0):data=str(data).replace("']","',")
    if(count % 2 == 0):
        data=str(data).replace("['","'") 
        data=str(data).replace("']","'],")
    if count<11:
        
            
            print(data)

!cat new-stuff.corpus.json|head -20

!ls -rant

!cat /home/jack/Desktop/PAV/opensubtitles/raw/lines/lines-aaa |head -20

!cat subtitles.json |head -10

/home/jack/Desktop/PAV/opensubtitles/raw/lines/lines-aaa

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




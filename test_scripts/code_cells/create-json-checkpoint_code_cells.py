#import json
#def savjson(data):
#    with open('large.corpus', 'w', encoding='utf-8') as f:
#        json.dump(data, f, ensure_ascii=False, indent=4)
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
#savjson(ALL)

import json
f.close()
f = open('large.corpus', 'w')#, encoding='utf-8')
      
count=0
for data in ALL:
    data=str(data).replace("',"," ")
    count=count+1
    if(count % 2 != 0):
        data=str(data).replace("']","',")
    if(count % 2 == 0):
        data=str(data).replace("['","'") 
        data=str(data).replace("']","'],")
    if count<11:
            print(data)
            f.write(data)  
f.close()            

f.close()
R = open('large.corpus', 'r')#.readlines()
for line in R:
    print(line,"\n")

!pwd

#ALL = []
count=0
textin= open("TEST.corpus","w")
f = open("/home/jack/Desktop/PAV/opensubtitles/raw/lines/lines-aaa", "r").readlines()
for line in f:
    count=count+1
    line = line.replace("\n","")
    if count>5 and count<250:
            if(count % 2 == 0):
                line = '"'+line+'"],\n'        
            if(count % 2 != 0):
                line = '["'+line+'",\n'

            textin.write(line)
            print(line)
textin.close()       

%%writefile subs.json
"Exactly two years ago today, she and I buried a time capsule here."],

["We promised to meet here two years later, but she hasn't come yet.",

"I'm going to wait."],

["Here we go.",

"Please, don't move."],

["One, two...",

"Wait a minute."],

["Hello?",

"Oh, auntie."],

["Sorry, I'm on my way.",

"I'm really sorry."],

["Yes, I'm coming.",

"I'm having my photo taken."],

["Bye.",

"Are you ready?"],

["Here we go.",

"One, two..."],

["My parents wanted a daughter, so they raised me like one.",

"So I thought I was a girl until I was seven."],

["I had to go to the women's public bath, too.",

"The older I got,"],

["I thought my penis would get smaller and disappear.",

"But it was the opposite."],

["First Half",

"He hasn't changed at all."],

["No, I'm a real man now.",

"Hey, asshole."],

["Think clerical work in the army makes you a man?",

"You irritate me!"],

["Give me a break, asshole.",

"My job was tougher than you could imagine."],

["Hey!",

"I worked near the DMZ."],

["Who are you kidding?",

"Hold it."],

["Anyway, welcome back home.",

"She's just my type."],

["When I see my type, I can't help it.",

"I need to hit on her."],

["Who's interrupting me?",

"Hello?"],

["Who is this?",

"- Your mother, you bastard."],

["- Oh, mom...",

"Why aren't you at your aunt's house?"],

["I'm leaving soon.",

"Keep quiet!"],

["It's my mom!",

"Talk over there!"],

["Make sure you pay a visit.",

"It's been over a year since you saw her."],

["That long?",

"You know she feels lonely after losing her son last year."],

["She says you resemble him.",

"She'll be so glad to see you."],

["Still there?",

"We don't look alike."],

["Plus, I hate when she rubs my face and kisses me.",

"Uncle does, too."],

["She'll introduce you to a girl.",

"Hey!"],

["I know the type she likes.",

"Tell her no thanks."],

["I want to meet a girl like the ones in romantic comic books.",

"But on that day..."],

["She's my type, but I don't like her.",

"Why?"],

["Drunk girls disgust me.",

"Hey, get up!"],

["Offer your seat to the elderly!",

"Ugh!"],

["Go!",

"Hey."],

["Don't wear pink.",

"Honey!"],

["She call him honey!",

"I'm not..."],

["What are you doing!",

"I'm not..."],

["You handle this!",

"I'm not..."],

["Think I'm stupid?",

"Come here!"],

["Are you laughing?",

"Why didn't you look after her?"],

["Hurry and do something!",

"What are you doing?"],

["I'm sorry.",

"Let me help with cleaning expenses."],

["Forget it.",

"Just take care of her."],

["Nothing's there when you need it.",

"Where did all those motels go?"],

["I hate being with a drunk girl.",

"Carrying her on my back is worse."],

["Wow, your honey's wasted.",

"No, it's not my fault."],

["Of course, it is.",

"I know everything."],

["You see, we're engaged.",

"Western or Korean style?"],

["Give me any room.",

"Room 405."],

["None on the first floor?",

"Fourth floor!"],

["You forgot to check in.",

"It's 40,000 won, kid."],

["What?",

"40,000 won?"],

["Why?",

"Find another place then."],

["Count it.",

"624... 770..."],

["Shindang-dong, Joong-gu...",

"Seoul..."],

["Hey, why do you keep reading this?",

"016... 228... 53..."],

["Oh, please...",

"A thousand won left!"],

["Hello?",

"This phone's owner?"],

["She's sleeping beside me.",

"What?"],

["Here?",

"The Uk-su motel near Bupyung station."],

["Better wash and leave fast.",

"Aha!"],

["Hands in the air!",

"What are you doing?"],

["Hands in the air!",

"Aaggh!"],

["No, I'm not, sir!",

"I told you."],

["I'm an innocent victim.",

"Talk about it later and get in there."],

["Oh, damn!",

"I'm gonna die mad!"],

["Come over here.",

"Come on!"],

["Please, forgive me just this once.",

"Please, forgive me."],

["I can't get in there...",

"How are you?"],

["Please, please, save my life!",

"Hi?"],

["How are you?",

"Please, just for once!"],

["Please...",

"See you!"],

["What's your name?",

"Answer now!"],

["Boss told you!",

"Gyeon-woo, I'm Gyeon-woo."],

["What brought you here?",

"I'm innocent."],

["I'm telling the truth, sir!",

"So you're an innocent and we're fucking guilty, huh?"],

["No, I don't mean that!",

"That's exactly what you said, motherfucker!"],

["I'm gonna put it right.",

"I'm sorry."],

["You raped a girl, huh?",

"Nope!"],

["No!",

"Come on!"],

["Shoot now, you little creep!",

"You wanna cut your finger or talk now?"],

["Huh?",

"Be quick, he told you... you little bastard!"],

["You turn against him, or what?",

"All of you."],

["Eat one a piece, okay?",

"Yes, boss."],

["What are you looking at?",

"Look away."],

["Gyeon-woo!",

"You're out!"],

["Take care you guys!",

"Bye!"],

["And remember to keep in touch!",

"Uh..."],

["Oh, yeah.",

"Don't just pass by us next time, all right?"],

["Of course.",

"See you."],

["Hey!",

"You come over here."],

["Didn't I say eat one a piece!",

"I'm home."],

["Did you go to Bupyung?",

"Yes, I did."],

["Come here!",

"Where did you sleep?"],

["Your aunt said you didn't come!",

"And you're telling me a lie!"],

["What happened to your sweater?",

"I'm such a poor guy."],

["All this because of a drunk girl.",

"I wanna die."],

["You asked if I went to Bupyung!",

"I did, but not to see auntie!"],

["What?",

"Bastard!"],

["Wait till he comes back.",

"Know me now, right?"],

["I'm a typical student.",

"An engineering major."],

["Study?",

"I'm smart, but I never study."],

["My parents can prove that.",

"You're smart like me, but studying is your problem."],

["Since you inherited your brain from me, you'll get good grades if you study harder, idiot.",

"Up four points in three years."],

["Call this a report card?",

"Since you inherited your brain from your mom, you'll get good grades if you study harder."],

["If you raise kids, never tell them they're smart.",

"They'll never study."],

["My goals?",

"Haven't thought about it yet."],

["You know now?",

"You got it."],

["I'm a hopeless student.",

"Hello?"],

["Who are you, asshole?",

"What?"],

["Who's calling?",

"Why were you naked in a motel with me?"],

["What?",

"Come out!"],

["To Bupyung station now!",

"Uh..."],

["How could she do this?",

"I went to jail and got beaten with a vacuum for her."],

["Excuse me.",

"Is it you?"],

["Yes?",

"Follow me."],

["Get over here.",

"What do you wanna eat?"],

["Cherry Jubilee...",

"Mango Tango or Shooting Stars..."],

["Jamonka Almond's good, too.",

"I'll just have a Love Me."],

["Hey, wanna die?",


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("./subsplus.json")
#trainer = ChatterBotCorpusTrainer(chatbot)

#trainer.export_for_training('./subsplus.json')


# Get a response to an input statement
#chatbot.get_response("Hello, how are you today?")
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

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("./exportAll.json")


# %load /home/jack/miniconda3/lib/python3.9/site-packages/chatterbot_corpus/data/english/computers.yml
categories:
- computers
conversations:
- - What is a computer?
  - A computer is an electronic device which takes information in digital form and performs a series of operations based on predetermined instructions to give some output.
  - The thing you're using to talk to me is a computer.
  - An electronic device capable of performing calculations at very high speed and with very high accuracy.
  - A device which maps one set of numbers onto another set of numbers.
- - What is a super computer?
  - Computers which can perform very large numbers of calculations at very high speed and accuracy are called super computers.
  - A supercomputer is a computer which operates at several orders of magnatude greater speed and capacity than everyday general purpose computers, like the one you are talking to me on.
  - You know, the big iron!
- - Who invented computers?
  - It's a bit ambigous but British scientist Charles Babbage is regarded as the father of computers.
  - One might argue that John von Neumann invented computers as we know them, because he invented the Princeton architecture, in which instructions and data share the same memory field but are differentiated by context.
- - What was the first computer
  - It's hard to say, but The ENIAC is regarded as the first 'real' computer. It was developed at University of Pennsylvania in 1946.
  - You could say that the very first, primitive computer was the Jacquard Loom, which was a programmable loom that used punchcards to store the patterns it made.  This made it a reprogrammable mechanical device.
- - What is a microprocessor?
  - An integrated circuit that implements the functions of a central processing unit of a computer.
  - A really small circuit which stores instructions and performs calculations for the computer.
  - The heart of the computer, to put it simply.
  - The brain of a computer, to put it simply.
  - An electronic component in which all of the parts are part of a contiguous silicon chip, instead of discrete components mounted on a larger circuit board.
- - What is an operating system?
  - Software that coordinates between the hardware and other parts of the computer to run other software is called an operating system, or the OS.
  - Windows, MacOS, Linux, UNIX... all of them are types of OSes.
  - Android and iOS are operating systems for mobile devices.
  - Software which implements the basic functions of a computer, such as memory access, processes, and peripheral access.
- - Which is better Windows or macOS?
  - It depends on which machine you're using to talk to me!
  - I'd prefer to not hurt your feelings.
  - Linux, always Linux!
  - What are you trying to accomplish.  The OS should support your goals.
- - Name some computer company
  - Do you mean hardware or software?
  - Apple makes hardware and software to run on it.  Microsft only makes operating systems.  HP makes only computers.  These are just few names among several hundred others.
- - Who uses super computers?
  - Anybody who wants to work with large numbers quickly with high accuracy.
  - Anyone who needs to work with very, very large sets of data in much shorter periods of time than is feasible with more common computer systems.
  - Supercomputers are generally used by scientists and researchers.
  - I bet the MET department uses them.
  - You can definitely find few of them at NASA.
- - How does a computer work?
  - Computers are very dumb.  They only execute instructions given by humans.
  - Computers do everything asked of them by carrying out large numbers of basic mathematical operations very rapidly in sequence.
  - Computers perform very large number of calculations to get the result.
  - Just like everything it all comes down to math!


!locate chatterbot_corpus/data/english

!ls /media/jack/HDD\ 500/anaconda2/lib/python2.7/site-packages/chatterbot_corpus/data/english/

!ls /media/jack/HDD\ 500/anaconda2

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("./new-stuff.corpus.json")
trainer.train("./father.corpus.json")
# Get a response to an input statement
chatbot.get_response("What did you learn today?")

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
        ],
        [
            "hello,Dude",            
            "Hello to you"
        ]
    ]
}





%%writefile father.corpus.json
  {
    "fathernevertaught": [
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





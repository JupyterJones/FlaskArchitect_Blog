import json
L = input("Which file: ")
print(L)
#def savjson(data):
datain = open("aa"+L+"json.json","w")
    
datain.write("{\n \"conversations\": \n[\n")
def convert() :
    count = 0
    #ALL = []
    f = open("/home/jack/Desktop/PAV/opensubtitles/raw/lines/lines-aa"+L+"", "r").readlines()
    for line in f:
        line = line.replace("\n","")
        line =line.replace("\"","'")
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
    return #print("--\n",ALL)

convert() 
datain.write("]}")
datain.close() 
file = "aa"+L+"json.json"
print(file)


#You could parse it as YAML (whose in-line syntax is a more permissive superset of JSON):

import yaml
data = yaml.load(open("aaxjson.json"))

#then to get valid JSON back you can dump the object back out:

import json
#json.dumps(data)
with open('new_data.json', 'w') as outfile:
    outfile.write(str(data))


!cp AWK /usr/local/bin

import shlex, subprocess
command_line = input()
args = shlex.split(command_line)
# awk 'NR>2{print a;} {a=b; b=$0} END{sub(/,$/, "", a); print a;print b;}'  aaujson.json > aauCjson.json
# awk 'NR>2{print a;} {a=b; b=$0} END{sub(/,$/, "", a); print a;print b;}'  aaujson.json>aauCjson.json
print(args)
#
p = subprocess.Popen(args) # Success!

!AWK aawjson.json


!ls C+*

%%writefile AWK
awk 'NR>2{print a;} {a=b; b=$0} END{sub(/,$/, "", a); print a;print b;}'  $1 > C+$1

!chmod +x AWK

!./AWK aavjson.json

!awk 'NR>2{print a;} {a=b; b=$0} END{sub(/,$/, "", a); print a;print b;}'  aaujson.json

p = subprocess.Popen(args)


import subprocess
!awk 'NR>2{print a;} {a=b; b=$0} END{sub(/,$/, "", a); print a;print b;}'  aaqjson.json > aaqCjson.json
script = "\'awk 'NR>2{print a;} {a=b; b=$0} END{sub(/,$/, \"\", a); print a;print b;}'  aatjson.json" #> aatCjson.json
print(script)
#subprocess.call(['bash','awk \'NR>2{print a;} {a=b; b=$0} END{sub(/,$/, \"\", a); print a;print b;}\'  aarjson.json'])



import subprocess
p = subprocess.Popen(args)
p

!awk 'NR>2{print a;} {a=b; b=$0} END{sub(/,$/, "", a); print a;print b;}'  aaojson.json > aaoCjson.json

import json

#def savjson(data):
datain = open("aalson.json","w")
    
datain.write("{\n \"conversations\": \n[\n")
def convert() :
    count = 0
    #ALL = []
    f = open("/home/jack/Desktop/PAV/opensubtitles/raw/lines/lines-aal", "r").readlines()
    for line in f:
        line = line.replace("\n","")
        line =line.replace("\"","'")
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
            #textinput.write(ALL)
    return #print("--\n",ALL)

convert() 
datain.write("\n]\n}")
datain.close() 

# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
import bson

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
trainer = ChatterBotCorpusTrainer(bot)


trainer.train("chatterbot.corpus.english")
trainer.train("./father.corpus.json")
trainer.train("./export2.json")
trainer.train("./exportAll.json")
trainer.train("./aaajson.json")
trainer.train("./aabjson.json")
trainer.train("./aacjson.json")
trainer.train("./aadjson.json")
trainer.train("./aaejson.json")
trainer.train("./aafjson.json")
trainer.train("./aagjson.json")
trainer.train("./aahjson.json")
trainer.train("./aaijson.json")
trainer.train("./aajjson.json")
trainer.train("./aakjson.json")
trainer.train("./aaljson.json")
trainer.train("./aamjson.json")
trainer.train("./aanjson.json")
trainer.train("./aaoCjson.json")
trainer.train("./aaojson.json")
trainer.train("./aapjson.json")
trainer.train("./aaqCjson.json")
trainer.train("./aaqjson.json")
trainer.train("./aarjson.json")
trainer.train("./aasjson.json")
trainer.train("./aatjson.json")
trainer.train("./aaujson.json")
trainer.train("./aavjson.json")
trainer.train("./aawjson.json")
trainer.train("./aaxjson.json")


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

!ls *.json




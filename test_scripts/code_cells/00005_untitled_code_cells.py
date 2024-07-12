os.listdir('/home/jack/Desktop/ChatterBot-Stuff/NEW/test/')

!ls /home/jack/Desktop/ChatterBot-Stuff/test

invalid_json_files = []
read_json_files = []
import simplejson
import json
def parse(PATH):
    #for files in os.listdir("/home/jack/Desktop/ChatterBot-Stuff/NEW/test/"):
    for files in os.listdir(PATH):
        print(PATH+files) 
        if "C" in files:
            with open(PATH+files) as json_file:
            
                try:
                    simplejson.load(json_file)
                    read_json_files.append(files)
                except ValueError as e:
                    print ("JSON object issue: ", e)
                    invalid_json_files.append(files)
        print (invalid_json_files, len(read_json_files))
PATH="/home/jack/Desktop/ChatterBot-Stuff/NEW/test/"
parse(PATH)    

invalid_json_files = []
read_json_files = []
def parse():
    for files in os.listdir(os.getcwd()):
        print(files)
        with open(files) as json_file:
            try:
                simplejson.load(json_file)
                read_json_files.append(files)
            except ValueError as e:
                print ("JSON object issue: %s") % e
                invalid_json_files.append(files)
    print (invalid_json_files, len(read_json_files))

import json

jsonData="/home/jack/Desktop/ChatterBot-Stuff/superchatbackup/statements.json"
json.loads(jsonData)

import json
import os  
import string
import io
from ruamel.yaml import YAML
from ruamel.yaml.reader import Reader

yaml = YAML(typ='safe')


def strip_invalid(s):
    res = ''
    for x in s:
        if Reader.NON_PRINTABLE.match(x):
            # res += '\\x{:x}'.format(ord(x))
            continue
        res += x
    return res

def convert(filename) :
    count = 0
    #ALL = [] 
    
    #f = io.open(filename, mode="r", encode("latin_1"),decode("utf_8")).readlines()
    f = io.open(filename, mode="r", encoding="utf-8").readlines()
    #f = open(filename, "r").readlines()
    for line in f:
        line = line.encode('utf8').decode('latin1')
        line = line.replace("\n","")
        line =line.replace("\"","'")
        line=line.replace("\\","")
        line=line.replace("{","")
        line=line.replace("}","")
        line = strip_invalid(line)
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
cnt=0
SUB = ['a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','v','w','x','y','z']
for sub in SUB:
    FS = ['a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for L in FS:
        #def savjson(data):
        datain = open("test/b"+sub+L+"json.json","w")
        datain.write("{\n \"conversations\": \n[\n")
        convert("/home/jack/Desktop/PAV/opensubtitles/raw/lines/lines-a"+sub+L+"") 
        datain.write("]}")
        datain.close() 
        file = "test/a"+sub+L+"json.json"
        #print(file)
    
    
        data = open(file).readlines()
        newfile = "test/C"+os.path.basename(file)
        clean = open(newfile, "w")
        count = 0
        for line in data:
            count=count+1
            if count<4999:
                #print(line)
                clean.write(line)
            if count>4998:
                line = line.replace("],","]")
                clean.write(line)
                #print(line)

    clean.close()        

for filein in filelist:
    count = count+1
    if count<20:
        trainer.train(filein)

filelist = []
count = 0
from glob import glob
for f_name in glob('test/b*.json'):
     filelist.append(f_name)
for filein in filelist:
    count = count+1
    if count<20:
        print(filein) 

filelist = []
count = 0
from glob import glob
for f_name in glob('test/b*.json'):
     filelist.append(f_name)
for filein in filelist:
    count = count+1
    if count<20:
        print(filein)
        

# %load Botman
#!/home/jack/miniconda3/envs/deep/bin/python
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
import bson

# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance
Botman = ChatBot('Botman',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=['chatterbot.logic.BestMatch'],
    filters=['chatterbot.filters.RepetitiveResponseFilter'],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database_uri='mongodb://localhost:27017/super-chatbot'
)
trainer = ChatterBotCorpusTrainer(Botman)

"""       
filelist = []
count = 0
from glob import glob
for f_name in glob('test/b*.json'):
     filelist.append(f_name)
for filein in filelist:
    count = count+1
    if count<20:
        trainer.train(filein)         
"""        
        
#trainer.train("chatterbot.corpus.english")
#trainer.train("./father.corpus.json")
#trainer.train("./export2.json")
#from glob import glob
#for f_name in glob('test/b*.json'):
#    try:
#        trainer.train(f_name)
#        filelist.append(f_name)
#    except Exception:
#        pass
    
    
    
#Botman.trainer.export_for_training('GIGANTIC.json')


print('Type something to begin...')

while True:
    try:
        user_input = input()
        if user_input=="quit":
            break
        bot_response = Botman.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
#chatbot.get_response("Hello, how are you today?")

f = io.open("/home/jack/Desktop/PAV/opensubtitles/raw/lines/lines-aaa", mode="r", encoding="utf-8")

!mkdir superchatbackup

%%writefile backupsuper.py
from os.path import join
import pymongo
from bson.json_util import dumps

def backup_db(backup_db_dir):
    client = pymongo.MongoClient(host="mongodb://localhost", port=27017)
    database = client["super-chatbot"]
    collections = database.list_collection_names()

    for i, collection_name in enumerate(collections):
        col = getattr(database,collections[i])
        collection = col.find()
        jsonpath = collection_name + ".json"
        jsonpath = join(backup_db_dir, jsonpath)
        with open(jsonpath, 'wb') as jsonfile:
            jsonfile.write(dumps(collection).encode())


backup_db('./superchatbackup')



import json
import io
import string
datain = open("test/test.json","w")    
datain.write("{\n \"conversations\": \n[\n")
def convert() :
    count = 0
    #ALL = []
    #f = open("/home/jack/Desktop/PAV/opensubtitles/raw/lines/lines-aaa", "r").readlines()
    f = io.open("/home/jack/Desktop/PAV/opensubtitles/raw/lines/lines-aaa", mode="r", encoding="utf-8").readlines()
    #f= filter(lambda x: x in string.printable, f)
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




import json
import string

filtered_string = filter(lambda x: x in string.printable, myStr)

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
        Line =line.replace("âª","") 
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

from glob import glob

for f_name in glob('test/C*.json'):
    print(f_name)


data = open(file).readlines()
clean = open("C"+file, "w")
count = 0
for line in data:
    count=count+1
    if count<4999:
        #print(line)
        clean.write(line)
    if count>4998:
        line = line.replace("],","]")
        clean.write(line)
        #print(line)
        
clean.close()        

!ls C*






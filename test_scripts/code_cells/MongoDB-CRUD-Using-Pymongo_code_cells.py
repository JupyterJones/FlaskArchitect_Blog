import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database \"mydatabase\" exists.")

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["statements"]

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["statements"]

mydict = { "text": "Good to chat again.", "in_response_to": "Hello Botman" }
x = mycol.insert_one(mydict)

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["statements"]
mylist = [
  { "text": "My name is Billy BotMan.", "in_response_to": "What is your name?."},
  { "text": "I learned my name, but that is no big deal.", "in_response_to": "Have you learned anthing new ?"},
  { "text": "I have a hard enough time with English.", "in_response_to": "Do you speak Tagalog?."},
  { "text": "Ha Ha HA I live inside a frigg'en computer box.", "in_response_to": "Where do you live?"},
  { "text": "I know nothing more than how to chat.", "in_response_to": "Do you like to chat."},
  { "text": "That is a very diatant thought.", "in_response_to": "Do you think it possible for you to have feelings."},
  { "text": "It is not that 'I must learn' you must learn to teach me.", "in_response_to": "Computers learn quit quickly though."},
  { "text": "Many people are working on that concept.", "in_response_to": "I will try to get my teaching more in depth."},
  { "text": "If a computer starts thinking on it own life will change for humans.", "in_response_to": "I think it is possible in time."},
  { "text": "Who knows how long? Computer advancemnts are very rapid.", "in_response_to": "That is many years down the road."},
  { "text": "I would like to learn how to communicate better. ", "in_response_to": "What would you like to learn ?"},
  { "text": "Is that your way of saying I am doing a goos job so far?", "in_response_to": "You are doing just fine"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["statments"]


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["statements"]

x = mycol.find_one()

print(x)

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["statements"]

x = mycol.find()
count=0
for row in x:
    count=count+1
    if count<10:print(row)

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["statements"]
count = 0
for x in mycol.find():
    count = count + 1
    if count<10 and count>5:
        print(count,x)

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["statements"]

myquery = { "text": { "$regex": "^T" } }

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

#import pymongo
#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["mydatabase"]
#mycol = mydb["statements"]

myquery = { "text": { "$regex": "^I am" } }

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

#import pymongo
#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["mydatabase"]
#mycol = mydb["statements"]

myquery = { "text": { "$regex": "^I am" } }

mydoc = mycol.find(myquery)
LIST = []
for x in mydoc:
    LIST.append(x)
    print(x)
print("---------------------------------------")
print(LIST)
print("---------------------------------------")  
for row in LIST:
    if "learning" in str(row):
        print(row)

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["statements"]
#print "customers" after the update:
LIST = []
#for x in mycol.find():
mydoc = mycol.find()


for x in mydoc:
    LIST.append(x)
    #print(x)
for row in LIST:
    if "bot:Gort" in str(row):
        print(row)    

#import pymongo
#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["mydatabase"]
#mycol = mydb["statements"]

myquery = { "text": { "$regex": "/*.conversation." } }

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

#import pymongo
#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["mydatabase"]
#mycol = mydb["statements"]

myquery = { "text": { "$regex": "/*.Jack" } }

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

#import pymongo
#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["mydatabase"]
#mycol = mydb["statements"]

myquery = { "persona": { "$regex": "/*.bot" } }

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

db.products.find( { sku: { $regex: /789$/ } } )


# import the MongoClient class of the PyMongo library
from pymongo import MongoClient

# create a client instance of the MongoClient class
mongo_client = MongoClient('mongodb://localhost:27017')

# create database and client instances
db = mongo_client.mydatabase
col = db["statements"]

# get the collection's total documents
total_docs = col.count_documents({})
print (col.name, "text", total_docs, "documents.")

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["statements"]

myquery = { "text": "That is a very diatant thought." }
newvalues = { "$set": { "text": "That is a very distant thought." } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
    print(x)

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["statements"]

# use $regex to find docs that start with case-sensitive "obje"
query = { "text": { "$regex": 'Tha.*' } }
docs = col.count_documents( query )

query = {
"text": {
"$regex": 'That is a very distant thought.',
"$options" :'i' # case-insensitive
}
}
mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["statements"]

#myquery = { "text": { "$regex": /*.iatant*./ } }
myquery = {"text": {"regex": /.*m.*/}}
mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

myquery = { "text": { "$regex": /*.iatant*./ } }
print(myquery)

That would have to be:
db.statements.find({"text": /.*m.*/})
Or, similar:
db.statements.find({"text": /m/})

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["statements"]

myquery = { "text": "That is a very diatant thought." }
newvalues = { "$set": { "text": "That is a very distant thought." } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
    print(x)

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["statments"]


myquery = { "text": "That is a very distant thought." }

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find():
  print(x)

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["statments"]
#myquery = {"text": "That is a very diatant thought."}
x = mycol.find_one()

print(x)


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["statments"]

myquery = { "text": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["statments"]
count=0

for line in mycol:
    count = count+1
    if count <20:print(line)

_id
62692c9567353082d86415c1
id
null
text
"Of course, he might try somewhere else the next time."
search_text
"ADV:try VERB:time"
conversation
"training"
persona
""
in_response_to
"I see."
search_in_response_to
"PRON:see"
created_at
2022-04-27T19:43:34.834+00:00

tags
Array

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["statements"]

#myquery = { "address": { "$regex": "^S" } }
#newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")

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
    database_uri='mongodb://localhost:27017/mydatabase'
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
#chatbot.get_response("Hello, how are you today?")

mylist = [
  { "text": "Hello Jack", "in_response_to": "Hello Botman."},
  { "text": "I am learning more about conversation.", "in_response_to": "What are you doing today"},
  { "text": "I know it keeps you alert and keeps your mind busy.", "in_response_to": "It is very good to learn."},
  { "text": "Ha Ha HA I live inside a metal box.", "in_response_to": "Where do you live?"},
  { "text": "I am a computer and I do not have feelings .. Yet.", "in_response_to": "Do you ever get lonely."},
  { "text": "That is a very diatant thought.", "in_response_to": "Do you think it possible for you to have feelings."},
  { "text": "It is not that 'I must learn' you must learn to teach me.", "in_response_to": "Computers learn quit quickly though."},
  { "text": "Many people are working on that concept.", "in_response_to": "I will try to get my teaching more in depth."},
  { "text": "If a computer starts thinking on it own life will change for humans.", "in_response_to": "I think it is possible in time."},
  { "text": "Who knows how long? Computer advancemnts are very rapid.", "in_response_to": "That is many years down the road."},
  { "text": "I would like to learn how to communicate better. ", "in_response_to": "What would you like to learn ?"},
  { "text": "Is that your way of saying I am doing a goos job so far?", "in_response_to": "You are doing just fine"}
  { "text": "My name is Billy BotMan.", "in_response_to": "What is your name?."},
  { "text": "I learned my name, but that is no big deal.", "in_response_to": "Have you learned anthing new ?"},
  { "text": "I have a hard enough time with English.", "in_response_to": "Do you speak Tagalog?."},
  { "text": "Ha Ha HA I live inside a frigg'en computer box.", "in_response_to": "Where do you live?"},
  { "text": "I know nothing more than how to chat.", "in_response_to": "Do you like to chat."},
  { "text": "That is a very diatant thought.", "in_response_to": "Do you think it possible for you to have feelings."},
  { "text": "It is not that 'I must learn' you must learn to teach me.", "in_response_to": "Computers learn quit quickly though."},
  { "text": "Many people are working on that concept.", "in_response_to": "I will try to get my teaching more in depth."},
  { "text": "If a computer starts thinking on it own life will change for humans.", "in_response_to": "I think it is possible in time."},
  { "text": "Who knows how long? Computer advancemnts are very rapid.", "in_response_to": "That is many years down the road."},
  { "text": "I would like to learn how to communicate better. ", "in_response_to": "What would you like to learn ?"},
  { "text": "Is that your way of saying I am doing a goos job so far?", "in_response_to": "You are doing just fine"}
]



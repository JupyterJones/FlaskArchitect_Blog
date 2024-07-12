%%writefile Key.py
def twiter():
    CONSUMER_KEY = 'WWWWWWWWWWWWWWWW'
    CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXX'
    ACCESS_KEY = 'YYYYYYYYYYYYYYYYYYY'
    ACCESS_SECRET = 'ZZZZZZZZZZZZZZZZ'
    twir = (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
    return twir

import sys
import Key
consumer_key = Key.twiter()[0]
consumer_secret = Key.twiter()[1]
access_key = Key.twiter()[2]
access_secret = Key.twiter()[3]
print consumer_key, consumer_secret, access_key, access_secret


#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import sys
sys.path.insert(0,"/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import Key
from random import randint

#Twitter API credentials
consumer_key = Key.twiter()[0]
consumer_secret = Key.twiter()[1]
access_key = Key.twiter()[2]
access_secret = Key.twiter()[3]

def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	
	pass


if __name__ == '__main__':
    USER = raw_input("User  : ") or "CNN"
    
    get_all_tweets(USER)

!ls *.csv

from itertools import tee
count=0
with open("importpython_tweets.csv") as inf:
    for line in inf:
        lines  = line[39:]
        outf = open("importpython.txt", "a") 
        outf.write(lines)
outf.close() 

search = raw_input("find  ")
file = open("importpython.txt")
lines = file.readlines()
for line in lines:
    if search in line:
        print line
    if search == True:
        print line
        file.close()
        exit()
file.close()

import sqlite3
conn = sqlite3.connect('collection.db')
c = conn.cursor()
c.execute("""
CREATE VIRTUAL TABLE tweets 
USING FTS3(text, account);
""")
conn.commit()
conn.close()

import sqlite3
import time
#account = "TEDTalks.txt"
account = "importpython.txt"
#account = "elonmusk.txt"
#account = "realDonaldTrump.txt"
user = account[:-4]
lines = open(account,"r")
line = lines.readline()
for line in lines:
    conn = sqlite3.connect('collection.db')
    # ProgrammingError: You must not use 8-bit bytestrings 
    # unless you use a text_factory 
    conn.text_factory = str
    c = conn.cursor()
    c.execute("INSERT INTO tweets VALUES (?,?)", (line, user)) 
    conn.commit()
    conn.close()        
    
    #print line         

conn.commit()
conn.close()                 

import sqlite3
import sys
conn = sqlite3.connect('collection.db')
c = conn.cursor()
count=0
# limits query to 1000
req=1000
search = raw_input("Search : ")
for row in c.execute('SELECT rowid,* FROM tweets WHERE text MATCH ?', (search,)):    
    count=count+1
    print count,"-",(row)[1]," -- by",(row)[2],"\n"
    if count > req:
        conn.close()
        sys.exit()

/home/jack/Desktop/text_stuff/symmetrymag.txt

savE = open('SavE.txt', 'w')
savE.close()

import markovify
import time
f = open("symmetrymag.txt")
text = f.read()
text_model_a = markovify.Text(text)


ebook_b =open('elonmusk.txt')
text0 = ebook_b.read()
text_model_b = markovify.Text(text0)
for i in range(5):
    print(text_model_b.make_short_sentence(140))
    STR0 = (text_model_b.make_short_sentence(140))
    savE = open('SavE.txt', 'a')
    savE.write(STR0)
    savE.close()

# 2. Print five randomly-generated sentences
for i in range(5):
    print(text_model_a.make_short_sentence(140))
    STR = (text_model_a.make_short_sentence(140))
    savE = open('SavE.txt', 'a')
    savE.write(STR)
    savE.close()
# 3. Print three randomly-generated sentences of no more than 140 characters
for i in range(5):
    print(text_model_a.make_short_sentence(140))
    STR2 = (text_model_a.make_short_sentence(140))
    savE = open('SavE.txt', 'a')
    savE.write(STR2)
    savE.close()
# Combine the models into a single one
both_models = markovify.combine([text_model_a,text_model_b])
for i in range(5):
    print(both_models.make_short_sentence(140))    
    STR3 = (both_models.make_short_sentence(140))  
    savE = open('SavE.txt', 'a')
    savE.write(STR3)
    savE.close()    

import fileinput


import fileinput

for line in fileinput.input("file.txt", inplace=True):
    print line[0]
    #print "%d: %s" % (fileinput.filelineno(), 4, 'zzzzzzzzzzz'),

with open("Use.txt",'r') as f:
    get_all=f.readlines()


with open("sample.txt",'r') as f:
    get_all=f.readlines()
with open("file.txt",'w') as f:
    for i,line in enumerate(get_all,1): # Start counting lines at 1    
        if i == 3:                      # overwrite line 3
            f.writelines("This is my new TEXT on line three.\n")
            #you may also add more lines
            f.writelines("This is another line added under the first.\n") 
        else:
            f.writelines(line)
f.close()            

%%writefile sample.txt
The general rule is satisfied if they are reminded.
Some people are exceeding graciousness at the table. 
Those people are fewer in number.
Long, low masses of dust show the soldiers ground beforehand.

# %load file.txt
The general rule is satisfied if they are reminded.
Some people are exceeding graciousness at the table. 
This is my new TEXT on line three.
This is another line added under the first.
Long, low masses of dust show the soldiers ground beforehand.

import sqlite3
import base64
#Connect to database: 
conn = sqlite3.connect('snippet.db')
c = conn.cursor()
#Single lines do not need the three quotes
file = """
import Key
from random import randint

#Twitter API credentials
consumer_key = Key.twiter()[0]
consumer_secret = Key.twiter()[1]
access_key = Key.twiter()[2]
access_secret = Key.twiter()[3]

def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
"""
encodedlistvalue=base64.b64encode(file)
b = 'Key , using Key.py, using Key, API key'
c.execute("INSERT INTO snippet VALUES (?,?,?)", (encodedlistvalue, file, b))
conn.commit()
conn.close()


import sqlite3
import sys
conn = sqlite3.connect('snippet.db')
conn.text_factory = str
c = conn.cursor()
count=0
req=200
search = raw_input("Search : ")
for row in c.execute('SELECT * FROM snippet WHERE keywords MATCH ?', (search,)):    
    count=count+1
    #print count,"by",(row)[2],"\n",(row)[1],"\n"
    print count,"-",(row)[1]," -- by",(row)[2],"\n"
    if count > req:
        conn.close()
        sys.exit()

import sqlite3
import base64
conn = sqlite3.connect('snippet.db')
conn.text_factory = str
c = conn.cursor()# Never 
for row in c.execute('SELECT rowid, base64, text, \
keywords FROM snippet ORDER BY ROWID'):    
        # display as asci instead of unicode
        s2 = row[1].encode('ascii')
        #decode the base64 stored data
        encodedlistvalue=base64.b64decode(s2)
        print row[0],"\n",encodedlistvalue, '\n', \
        '\nKeywords:',row[3],'\n -----------------------------\n'

import sqlite3
import base64
conn = sqlite3.connect('snippet.db')
conn.text_factory = str
c = conn.cursor()# Never 
for row in c.execute('SELECT rowid, base64, text, keywords FROM snippet ORDER BY ROWID'):    
        # display as asci instead of unicode
        s2 = row[1].encode('ascii')
        #decode the base64 stored data
        encodedlistvalue=base64.b64decode(s2)
        print row[0],"\n",encodedlistvalue, '\n', '\nKeywords:',row[3],'\n -----------------------------\n'

#Returned code can be cut and pasted
import sqlite3
import sys
conn = sqlite3.connect('snippet.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
search = raw_input("Search : ")
for row in c.execute('SELECT * FROM snippet WHERE text MATCH ?', (search,)):    
    count=count+1
    #print count,"by",(row)[2],"\n",(row)[1],"\n"
    print count,"-",(row)[1]," -- by",(row)[2],"\n"
    if count > req:
        conn.close()
        sys.exit()

readOUT = open("ALLtextClean.txt","w")
readOUT.close()
import io
with io.open('ALLtext.txt','r',encoding='utf8') as f:
    text = f.read()
    text = text.encode('ISO-8859-1').strip()
# process Unicode text
with io.open('ALLtextClean.txt','a',encoding='utf8') as f:
    f.write(text)




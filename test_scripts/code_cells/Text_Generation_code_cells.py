filein = open('newtest.txt', 'w')
filein.close()

import sys
sys.path.insert(0,"/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
import Key
from random import randint

HashTag = raw_input("HashTag  : ") or "CNN"

CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,ACCESS_SECRET)

filein = open('newtest.txt', 'a')
txt = twitter.search(q=HashTag)
txt = str(txt)
filein.write(txt)
filein.close()

print txt

from bs4 import BeautifulSoup

filein = open('newtest.txt', 'r')
list = filein.readline()

list = list.replace("u'id_str': u'", '\nid ')
list = list.replace(u'\u2026','ignore')
list = list.replace(u'\xa0','ignore')
list = list.replace(u'\u2013', u' ')
list = list.replace(u'\xf1', u' ')
list = list.replace(u'\u2019','ignore')
list = '\n'+ u''.join((list)).encode('utf-8').strip()

print list

from twython import Twython
import csv
from dateutil import parser
from dateutil.parser import parse as parse_date
import datetime
from datetime import datetime
import pytz
import Key
from random import randint

utc=pytz.UTC
HashTag = raw_input("HashTag  : ") or "CNN"

CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,ACCESS_SECRET)

filein = open('newtest.txt', 'a')
txt = twitter.search(q=HashTag, count="1000",since='2017-7-1')
txt = str(txt)
filein.write(txt)
filein.close()
print txt

from twython import Twython
import csv
from dateutil import parser
from dateutil.parser import parse as parse_date
import datetime
from datetime import datetime
import pytz
import Key
from random import randint

utc=pytz.UTC
HashTag = raw_input("HashTag  : ") or "CNN"

CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,ACCESS_SECRET)

filein = open('newtest.txt', 'a')
txt = twitter.search(q=HashTag, count="1000",since='2017-7-1')
txt = str(txt)
filein.write(txt)
filein.close()
print txt


def on_status(self, status): 
    with open('file.txt', 'w') as f: 
        f.write('Author,Date,Text')
        writer = csv.writer(f)
        writer.writerow([status.author.screen_name, status.created_at, status.text])






import sys
import tweepy
import csv
import Key

#pass security information to variables
consumer_key = Key.twiter()[0]
consumer_secret = Key.twiter()[1]
access_key = Key.twiter()[2]
access_secret = Key.twiter()[3]

#use variables to access twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#create an object called 'customStreamListener'
class CustomStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print (status.author.screen_name, status.created_at, status.text)
        # Writing status data
        with open('OutputStreaming.txt', 'a') as f:
            writer = csv.writer(f)
            #status.author.screen_name = status.author.screen_name.encode('UTF-8')
            #status.text.encode = status.text.encode('UTF-8')            
            writer.writerow([status.author.screen_name.encode('UTF-8'), status.created_at, status.text.encode('utf8')])


    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream


    def titles():
        # Writing csv titles
        with open('OutputStreaming.txt', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Author', 'Date', 'Text'])
            
streamingAPI = tweepy.streaming.Stream(auth, CustomStreamListener())
#with open("tokens.txt", "r") as f:
with open("tokens2.txt", "r") as f:    
    tokens = f.readlines()

    streamingAPI.filter(track=tokens)
    #streamingAPI.filter(track=['Dallas', 'NewYork'])
    
    
    #status.text.encode('utf-8')
    #writer.writerow([unicode(s).encode("utf-8") for s in row])
    #writer.writerow([unicode('Author', 'Date', 'Text').encode("utf-8") for 'Author', 'Date', 'Text' in row])
    

%%writefile TweepyToCSV.py
import sys
import tweepy
import csv
import Key

#pass security information to variables
consumer_key = Key.twiter()[0]
consumer_secret = Key.twiter()[1]
access_key = Key.twiter()[2]
access_secret = Key.twiter()[3]

#use variables to access twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#create an object called 'customStreamListener'
class CustomStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print (status.author.screen_name, status.created_at, status.text)
        # Writing status data
        with open('OutputStreaming.txt', 'a') as f:
            writer = csv.writer(f)
            #status.author.screen_name = status.author.screen_name.encode('UTF-8')
            #status.text.encode = status.text.encode('UTF-8')            
            writer.writerow([status.author.screen_name.encode('UTF-8'), status.created_at, status.text.encode('utf8')])


    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream


    def titles():
        # Writing csv titles
        with open('OutputStreaming.txt', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Author', 'Date', 'Text'])
            
def main():
    streamingAPI = tweepy.streaming.Stream(auth, CustomStreamListener())
    #with open("tokens.txt", "r") as f:
    with open("tokens2.txt", "r") as f:    
        tokens = f.readlines()

        streamingAPI.filter(track=tokens)
        #streamingAPI.filter(track=['Dallas', 'NewYork'])


        #status.text.encode('utf-8')
        #writer.writerow([unicode(s).encode("utf-8") for s in row])
        #writer.writerow([unicode('Author', 'Date', 'Text').encode("utf-8") for 'Author', 'Date', 'Text' in row])


from Txmanip import RemoveBlank

RemoveBlank.removeblank("OutputStreaming.txt","cleanstream.txt")

from Txmanip import RemoveDuplicate

RemoveDuplicate.removeduplicate("cleanstream.txt","nodupStreaming.txt")

from itertools import tee
help(tee)

def edited(r):
    r+c
    return r

with open("test.txt") as inf, open("editTest.txt", "w") as outf:
    # set up iterators
    cfg, res = tee(inf)
    for i in range(1):
        next(cfg)

    # iterate through in tandem
    for c, r in zip(cfg, res):
        if len(c)<35:
            r = edited(r)
        outf.write(r)

    # reached end - write out remaining queued values
    for r in res:
        outf.write(r)
edited(r)        

from itertools import tee

with open("test.txt") as inf:
    # set up iterators
    cfg,res = tee(inf)
    # advance cfg by four lines
    for i in range(1):
        next(cfg)

    for c,r in zip(cfg, res):
        if len(c)<35:
            print c,r,"----\n"

from itertools import tee
count=0
with open("realDonaldTrump_tweets.csv") as inf:
    # set up iterators
    cfg,res = tee(inf)
    # advance cfg by four lines
    for i in range(4):
        next(cfg)

    for c,r in zip(cfg, res):
        count=count+1
        if "campaign" in c:
            #print "Date :",c[21:]
            print count,"-Text:",c[39:]



def main():
    count=0
    # open file
    infile = open('test.txt', 'r')
    # get input
    who = raw_input('Search Term: ')
    who = str(who)
    #begin search
    line = infile.readline()
    while line != '':
        if who in line:
            count += 1
            print line
    infile.close()


main()

count = 0

def main():
    count=0
    # open file
    file = open('test.txt', 'r')
    # get input
    who = raw_input('Search Term: ')
    who = str(who)
    #begin search
    lst = file.readline()
    while lst != '':
        if who in lst:
            count += 1
        print(count)
        file.close()


main()



from itertools import tee
search = raw_input('Search Term')
with open("realDonaldTrump_tweets.csv") as inf:
    # set up iterators
    cfg,res = tee(inf)
    # advance cfg by four lines
    for i in range(4):
        next(cfg)

    for c,r in zip(cfg, res):
        if search in c:
            print "Date :",c[21:38],"\nText :",c[39:]

!rm /home/jack/anaconda2/lib/python2.7/site-packages/Txmanip/RemoveDuplicate.pyc

import SearchFilename
filename = "realDonaldTrump_tweets.csv"
length = 20
SearchFilename.searchfilename(filename, length)

import TweepyToCSV
from TweepyToCSV import CustomStreamListener
TweepyToCSV.main()

%%writefile tokens2.txt
Mexico
dreamers
healthcare
revolution
hidding
putin
voters
feedup
fakenews
NBC
CBS
CNN
CIA
hate
wacko
gonecrazy
wierd
hopeless
impeach
dishonor
lost faith
angry
trump
russia
economy
north korean
rocketman
trust
follow
honorable
honest
dishonest
distrust
election
fakepresident

#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import Key
from random import randint

HashTag = raw_input("HashTag  : ") or "CNN"

#CONSUMER_KEY = Key.twiter()[0]
#CONSUMER_SECRET = Key.twiter()[1]
#ACCESS_KEY = Key.twiter()[2]
#ACCESS_SECRET = Key.twiter()[3]
#twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,ACCESS_SECRET)

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
    #while len(new_tweets) > 0:
    while len(new_tweets) < 400:    
        print "getting tweets before %s" % (oldest)

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print (len(alltweets))
        
        if (len(alltweets)) >200:

            #transform the tweepy tweets into a 2D array that will populate the csv	
            outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

            #write the csv	
            with open('%s_tweets.csv' % screen_name, 'wb') as f:
                writer = csv.writer(f)
                writer.writerow(["id","created_at","text"])
                writer.writerows(outtweets)

            pass


if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("realDonaldTrump")

%reset -f

import sys
sys.path.insert(0,"/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
import Key
import csv

HashTag = raw_input("HashTag  : ") or "CNN"

CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,ACCESS_SECRET)

# Open/create a file to append data to
csvFile = open('result.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)



txt = twitter.search(q=HashTag)
txt = str(txt)
filein.write(txt)
filein.close()

print txt

# Open/create a file to append data to
csvFile = open('result.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)
txt = twitter.search(q=HashTag)

csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])




for tweet in tweepy.Cursor(api.search,
                           q = "google",
                           since = "2014-02-14",
                           until = "2014-02-15",
                           lang = "en").items():

    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print tweet.created_at, tweet.text
csvFile.close()

import sys
sys.path.insert(0,"/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
import Key
from random import randint

HashTag = raw_input("HashTag  : ") or "CNN"

CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,ACCESS_SECRET)

tweetfile = 'newtest.txt'







txt = twitter.search(q=HashTag)

for list in txt:
    filein = open(tweetfile, 'a')
    list = list.replace(u'\xa0', u' ')
    list = list.replace(u'\u2026','ignore')
    list = list.replace(u'\xa0','ignore')
    list = list.replace(u'\u2013', u' ')
    list = list.replace(u'\xf1', u' ')
    list = list.replace(u'\u2019','ignore')
    list = '\n'+ u''.join((list)).encode('utf-8').strip()
   
    filein.write(list)
    filein.close()
    time.sleep(1)
    print list





import sys
sys.path.insert(0,"/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
import Key
from random import randint
import FileLen
Max = FileLen.filelen("ToUse.txt")
num = randint(0, Max)
with open('ToUse.txt') as f:
    for i, STR in enumerate(f, 1):
        if i == num:
            break

CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,ACCESS_SECRET)
#PATH = '/home/jack/Desktop/3DFRACT/Mandelbulb3Dv199/cloud.jpg'
#PATH = '/home/jack/Desktop/3DFRACT/Mandelbulb3Dv199/post-002.jpg'
#PATH = '/home/jack/Desktop/3DFRACT/Mandelbulb3Dv199/post-068.jpg'
#PATH = '/home/jack/Desktop/text_stuff/instagram/post-054.jpg'
PATH = '/home/jack/Desktop/text_stuff/instagram/post-056.jpg'
#PATH = '/home/jack/Desktop/text_stuff/junk/post-color3.png'

STR ="#C++imagery #python I enjoy pallet swapping most of all #imageprocessing"
photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])


twitter.search(q='python')

from bs4 import BeautifulSoup
import requests
import sqlite3
import base64
import time
#url = u'https://twitter.com/search?q='
HashTag = raw_input("HashTag  : ") or "CNN"
#url = u'https://twitter.com/hashtag/'+ HashTag +'?lang=en'
url = u'https://twitter.com/search?q='+ HashTag +'&src=typd'
tweetfile = 'hashtag.txt'
#url = u'https://twitter.com/scavino45/lists/florida-hurricane-irma'
#url = u'https://twitter.com/Selebog55680943'
#url = u'https://twitter.com/WinMansfield'
#query = u'%40drawranliou'
#query = u'%23hurricanne&src=typd'
#query = u'python, florida'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

tweets = [p.text for p in soup.findAll('p', class_='tweet-text')]
txt = (tweets)
for list in txt:
    filein = open(tweetfile, 'a')
    list = list.replace(u'\xa0', u' ')
    list = list.replace(u'\u2026','ignore')
    list = list.replace(u'\xa0','ignore')
    list = list.replace(u'\u2013', u' ')
    list = list.replace(u'\xf1', u' ')
    list = list.replace(u'\u2019','ignore')
    list = '\n'+ u''.join((list)).encode('utf-8').strip()
   
    filein.write(list)
    filein.close()
    time.sleep(1)
    print list


from textblob import TextBlob
from nltk.corpus import wordnet
import io
tweetfile = 'phrases.txt'
filein = open(tweetfile, 'w')
filein.close() 

with io.open("hashtag.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 

blob = TextBlob(essays)
for np in blob.noun_phrases:
    filein = open(tweetfile, 'a')
    np = '\n'+ u''.join((np)).encode('utf-8').strip()
    np=np.replace("#","");np=np.replace("//","")
    np=np.replace("... ”","");np=np.replace("... ","")
    np=np.replace(".. ","")
    np = np.lstrip()
    if len(np) < 16 and len(np) >3:
            np = (np+"\n")
            filein.write(np)
            print np
            filein.close() 

from bs4 import BeautifulSoup
import requests
import sqlite3
import base64
import time
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

#url = u'https://twitter.com/search?q='
#HashTag = (random_line('hashtag-nouns.txt'))
HashTag = (random_line('phrases.txt'))
url = u'https://twitter.com/hashtag/'+ HashTag +'?lang=en'
tweetfile = 'hashtag.txt'
#url = u'https://twitter.com/scavino45/lists/florida-hurricane-irma'
#url = u'https://twitter.com/Selebog55680943'
#url = u'https://twitter.com/WinMansfield'
#query = u'%40drawranliou'
#query = u'%23hurricanne&src=typd'
#query = u'python, florida'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

tweets = [p.text for p in soup.findAll('p', class_='tweet-text')]
txt = (tweets)
for list in txt:
    filein = open(tweetfile, 'a')
    list = list.replace(u'\xa0', u' ')
    list = list.replace(u'\u2026','ignore')
    list = list.replace(u'\xa0','ignore')
    list = list.replace(u'\u2013', u' ')
    list = list.replace(u'\xf1', u' ')
    list = list.replace(u'\u2019','ignore')
    list = '\n'+ u''.join((list)).encode('utf-8').strip()
   
    filein.write(list)
    filein.close()
    time.sleep(1)
    print list


from bs4 import BeautifulSoup
import requests
import sqlite3
import base64
import time
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

#url = u'https://twitter.com/search?q='
#HashTag = (random_line('hashtag-nouns.txt'))
#HashTag = (random_line('nodupsnohash.txt'))
#HashTag = (random_line('clean.txt'))
HashTag = "CNN"
url = u'https://twitter.com/hashtag/'+ HashTag +'?lang=en'
tweetfile = 'hashtag.txt'
#url = u'https://twitter.com/scavino45/lists/florida-hurricane-irma'
#url = u'https://twitter.com/Selebog55680943'
#url = u'https://twitter.com/WinMansfield'
#query = u'%40drawranliou'
#query = u'%23hurricanne&src=typd'
#query = u'python, florida'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

tweets = [p.text for p in soup.findAll('p', class_='tweet-text')]
txt = (tweets)
for list in txt:
    filein = open(tweetfile, 'a')
    list = list.replace(u'\xa0', u' ')
    list = list.replace(u'\u2026','ignore')
    list = list.replace(u'\xa0','ignore')
    list = list.replace(u'\u2013', u' ')
    list = list.replace(u'\xf1', u' ')
    list = list.replace(u'\u2019','ignore')
    list = '\n'+ u''.join((list)).encode('utf-8').strip()
   
    filein.write(list)
    filein.close()
    time.sleep(1)
    print list


def findhash():
    with open('hashtag.txt', 'r') as textin:
        tempstore = set()
        with open('hashonly.txt', 'w') as outfile:
            for line in textin.readlines():
                hashed = [ word for word in line.split() if word.startswith("#") ]
                #hashed = word for word in line.split() if word.startswith("#")
                hashed = str(hashed)
                hashed = hashed.replace("[","");hashed = hashed.replace("]","")
                hashed = hashed.replace(",","\n");hashed = hashed.replace(" '","")
                hashed = hashed.replace("'","");hashed = hashed.replace("#\n ","")
                hashed = hashed.replace("#","\n#")
                outfile.write(hashed)


findhash()

def removeblank():
    with open('hashonly.txt') as infile, open('hashonlyNoBlank.txt', 'w') as outfile:
        for line in infile:
            if not line.strip(): continue  # skip the empty line
            outfile.write(line)  # non-empty
            
removeblank() 

%%writefile /home/jack/anaconda2/lib/python2.7/site-packages/Txmanip/RemoveBlank.py

def removeblank(origFile, saveAS ):
    with open(origFile) as infile, open(saveAS, 'w') as outfile:
        for line in infile:
            if not line.strip(): continue  # skip the empty line
            outfile.write(line)  # non-empty
            
 

def remove_duplicates(infile):
    tempstore = set()
    with open('hashonlyNoBlankNoDups.txt', 'w+') as out:
        for line in open(infile):
            if line not in tempstore:
                if len(line) < 16 and len(line) >4:
                    out.write(line)
                    tempstore.add(line)

remove_duplicates('hashonlyNoBlank.txt')

%%writefile /home/jack/anaconda2/lib/python2.7/site-packages/Txmanip/RemoveDuplicate.py
def removeduplicate(infile,outfile):
    tempstore = set()
    with open(outfile, 'w+') as out:
        for line in open(infile):
            if line not in tempstore:
                if len(line) > 4:
                    out.write(line)
                    tempstore.add(line)



def findhash():
    with open('hashtag.txt', 'r') as textin:
        tempstore = set()
        with open('hashonly.txt', 'w') as outfile:
            for line in textin.readlines():
                hashed = [ word for word in line.split() if word.startswith("#") ]
                #hashed = word for word in line.split() if word.startswith("#")
                hashed = str(hashed)
                hashed = hashed.replace("[","");hashed = hashed.replace("]","")
                hashed = hashed.replace(",","\n");hashed = hashed.replace(" '","")
                hashed = hashed.replace("'","");hashed = hashed.replace("#\n ","")
                hashed = hashed.replace("#","\n#")
                outfile.write(hashed)


findhash()

def removeblank():
    with open('hashonly.txt') as infile, open('hashonlyNoBlank.txt', 'w') as outfile:
        for line in infile:
            if not line.strip(): continue  # skip the empty line
            outfile.write(line)  # non-empty
            
removeblank() 

def remove_duplicates(infile):
    tempstore = set()
    with open('hashonlyNoBlankNoDups.txt', 'w+') as out:
        for line in open(infile):
            if line not in tempstore:
                if len(line) < 16 and len(line) >4:
                    out.write(line)
                    tempstore.add(line)

remove_duplicates('hashonlyNoBlank.txt')

def findusers():
    with open('hashtag.txt', 'r') as textin:
        tempstore = set()
        with open('users.txt', 'w') as outfile:
            for line in textin.readlines():
                hashed = [ word for word in line.split() if word.startswith("@") ]
                #hashed = word for word in line.split() if word.startswith("#")
                hashed = str(hashed)
                hashed = hashed.replace("[","");hashed = hashed.replace("]","")
                hashed = hashed.replace(",","\n");hashed = hashed.replace(" '","")
                hashed = hashed.replace("'","")#;hashed = hashed.replace("@\n ","")
                hashed = hashed.replace("@","\n@")
                outfile.write(hashed)
findusers()
def removeblank():
    with open('users.txt') as infile, open('usersNoBlank.txt', 'w') as outfile:
        for line in infile:
            if not line.strip(): continue  # skip the empty line
            outfile.write(line)  # non-empty
removeblank()

def remove_duplicates(infile):
    tempstore = set()
    with open('usersNoDups.txt', 'w+') as out:
        for line in open(infile):
            if line not in tempstore:
                if len(line) < 16 and len(line) >4:
                    out.write(line)
                    tempstore.add(line)

remove_duplicates('usersNoBlank.txt')


def removeHash(infile):
    with open('clean.txt', 'w+') as out:
        for line in open(infile):
            line = line.replace("#","")
            out.write(line)

removeHash('hashonlyNoBlankNoDups.txt')

# %load clean.txt
Solar
EnergyStorage
netmetering
consumption"
Chinas"
soybeans
tobacco
QuitSmoking!
AskArvi
HealthTips
social
MEASummit2017
Bitcoin
energy
Industry
Growth
cities
develop
streetcar
decrease
traffic
congestion
increase
economic
activity
downtown
Sydney
BackTheBlue
Togo
Trump
CFCU19
ElvisHarte
TeamDOLL
none
NONE
deranged
filthy
Sane
clean
currently
Progressive
None
Zero
Nilch
Nada
Meme
threadless
The
ArtistShops
FAIL
MAKE
None.Its
Each
Day
Always
Other
Appreci88ion
NASCARMPD
Winnie
pooh
gluten
Honey
none.
know
Love
All
Trust
Few
Wrong
NoNe
Redskins
Fuck
Respect
Liberal
Bastards
America
DHS
ICE
AwanBrothers
ImranAwan
FBI
Wednesday
MAGA
POTUS
pick6
sofly
shadeson
dhs
ANTIFA
RIGHT_WING
OSG
Obama
Russia
DOJ
CIA
NSA
TheResistance
Equifax
news
JONESACT
PuertoRico
DHS:
JonesAct
ALLCargo
Ports
Aid
Hur...
Blockchain
Funding
infosec
cybersecurity
CISO
privacy
CIO
CSO
CO18
SEN18R
MAN
WHEATGRASS
COCONUT
DIE
PAINFUL
DEATH!!
NOTFUNNY!!!
Man
Grokitman
Iot
smarter
comic
book
superhero!
reading
learning
history
science
Grok
man
Scania
DAF
Nowguesswho
Sabeans
believe
especially
gotitcoming.
Recompense
gym
hairy
muscles
men
workout
workingout
chest
handsome
blueeyes
question
semantics
grok
grokitman
grokit
Blessed
oklahoma
selfie
biceps
lockerroom
cute
wrestler
guy
Knee
Persident
SOB
MOM
man-flu
big-baby
6pack
sixpack
tummy
toned
georgia
wrestle
wrestling
speedos
beefy
weightlifter
Gay
tbt
boy
beard
veteran
Fancy
Spending
Weekend
Himself
exsas?
oneofthebest
muscle
daddy
contest
contestants
pool
bodybuilder
bodybuilding
muscleman
pumpedup
delts
cop
police
officer
policeman
captain
strong
Microbial
Spoilage
PCR
PCR\xc2\xad
PCR!
HumpDay
Medicare
IMXEMS
MaxPain
Genetic
Molecular
ONEOF1ignore
Biotech
Biotechnology
DNA
pcr
visonmixer
consumers
BAX
Salmonella
ESICM2017
lives2017
Vienna
mcm
diagnostics
PCR!!!
EndTB
Swaziland
research
biology
lifescience
biotech
laboratory
curiosity
ourstuart
cancer
cells
RNAextraction
cellculture
rna
capitalism
environment.
consumption
World
Energy
Consumption
OECD
Freedom.
PlanetEarth.
war.
consumption.
7DeadlySins
IRS
Tax
WriteOffs
Deductions
FairTax!
awareness
local
smallholder
farmers
agriculture
land
green
materialism.
Indian
GDP
EOTYatSSE
reduce
bill
Multinational
Corps
Nutrition
Food
Manufactured
Logistics
mrx
Direct
Insurance
Carrier
Revenues
Global
Demand
pricesetting
tax
alcohol
Logos
tomgalle
earth
McDonalds
Spanish
kerosene
consumption:
maximum
climatechange
environment
ecology
globalwarming
population
lifestyle
Workstation
workstation.
VMware
vExpert
Fusion
setup
dreamsetup
workstation
battlestation
workspace
pcgaming
deskspace
desksetup
gaming
game
workhard
buongiorno
yql
vmware
fusion
newreleases
pcgamer
gamer
gamingpc
computer
gamingsetup
electric
desks
health
performance
Autodesk
Maya
SPEC
benchmark
PISDMathChat
startup
desk
WorksForMe
movies
design
uidesign
dribbble
behance
office
effects
movie
Steps
Run
KaliLinux
Howto
Linux
Tactig
photography
Market
Profit
Packaged
Frozen
Wholesalers
FreeAccess:
Alternative
food
Waste
Collection
business
cloud
technology?
CyberSecurity
Analytics
Security
Compliance
adobe
security
Unix/
chrome
edge
safari
ITSecurity
Crypto
CSOCartoon
CISSP
ITsec
infosectruth
NSASymposium
cryptohistory
fintech
Insurtech
education
cio
ciso
cso
First
Female
Cybersecurity
Tech
Regulation
datasec
corpgov
gdpr
eugdpr
finserv
Boston
InfoSec
cto
CyberConnect
Podcast-
GDPR
governance
regtech
microfocus
encryption
threatintel
ehr
ghc17
excited
opportunity
gearing
thanks
ABI
GOOGLE
folding
Galaxy
festiveseason
weddings
shows
socialising
parties
mittiofkutch
treasures
positive
negative
investment
BikeServicing
Calella
Gearing
Brakes
Bolts
HotelMontRosa
timewalking
Wow
HAAS.
AM100
Automotive
News
Commission
European
MyBTCcoinThe
HTC
big
announcement
tomorrow
Google
acquisition
mfg
gears
engineering
machinetools
automotive
shoot
pic
potrait
photo
agchef
marriage
styleignore
marketing
LOST
Lost
frenchbulldog
missing
lost
stolen
bpd
Lost&Found
love
lost.
thiem
ParsonCross
Sheffield
Lostdog
ScanMe
Missing
puppy
BorderCollie
Ramsgate
Kent
Chipped
Silent
auction
Helping
Charities
Fundraising
Auctions
Mask
silent
Garba
against
noise
pollution
surat
MYFM
world
Rohingya
thieves
History
headphones
awarness
Hugging
matter
hero
ParkShinHye
ChoiHeeJung
Chiswick
Sanctuary
Silent..
knowledge
angel
birthday
birthdayboy
youngjeezy
september
yeg
sunset
yegwx
skywatcher
September
adventure
funwalk
Saturday
wedotourism
tourismmonth
barefoot
dirtyfeet
autumn
harvest
backtoschool
joinus
GameModeon
emojis
indiedev
gamedev
cadencequiz
inflation
Spain
co2018
classsong
SEPTEMBER
28th
september28
2009
SanSalvador.
youthforpeace
devoted
children
Tupperware
ToaPayoh
TaxReform
CNN
CNNTownHall
sanjuan
puertorico
cnn
BoycottNFL
FoxNews
NFL
WeThePeople
TakeAKnee
Kaepernick
MSNBC
cnn"
Trumps"
newday
dotard
PUERTORICO
Fox
BREAKING:Lt
HuffPost
CNN:
bbc
sky
BBC
Idlib
Syria.
FAKE
CONSERVATIVE
SKY
NEWS
TORY
BREXIT
Biafra
NigelFarage:
Remainers
Leave
LabourParty
ANTISEMITIC
Labour
JeremyCorbyn
JEWS!
TheresaMay
ITV
UKIP
LABOUR
TimesNow
Rakhine.
corruption
EU!
Retweet:
Petition:
USA
TRAITOR
PhilipHammond
Political
COWARD
government
SELLOUT!
Florence
Brexit
breaking
bbcnews
LGBT
golf
democrat
war
dnc
usa
afghanistan
msnbc
nbc
abc
cbs
pbs
Flag
Anthem
Country.
Country
OneNation
DoorMat
TrumpsArmy
Military
LEOs
Classless
disgrace
Democrat
TakesAKnee
Veterans
americanflag
Texas
boycottNFL
takeastand
ServiceK9
Jinky
OnDuty
Family
Red
White
Blue
BlueFamily
nfl
kneeling
American
flag
protest
majority
america
disgrace.
potus.
StandUp
MyPresident
BoycottTheNFL
ANTHEM
FLOTUS
MichelleObama
FLAG
MILITARY
POLICE
Scotland
travel
Scottish
Edinburgh
Boycott
Packers
country
Flag..
anthem.
TrickleDown
morningjoe
bobcostas
GrahamCassidy
SaveACA
boundaries
NewDay
Regan
myth
mocofb
other
other.
each
alisonmoyet
voice
othertour
iOS11
OTHER
BEHAVIOR
YOUR
pets
dogs
cats
birds
hamsters
FollowsMe
Litecoin
VideoGame
Manga
Information
And
Sitting
Choir
Rihminds
Addition
Things
Thought
Rihlationship
KamelaHarris
Malutto
Negro
Malutto"
dont"
choose
Prospect
mine.
Prophetic
Warrior
Prayer
Circle
Leader"
System
Most
Own
Agenda
Identified
Time
Identify
Other...
NPm
Mirror
him
philosophers
playdate
play
lethimout
iFunny
meme
memes
memethis
memeit
Mickeynnials
Alsace
Woups
Sorry
TweetClash
spending
trump
regime
Swamp
TaxMoney
TrumpSwamp
surveys
premises
Save
today
budget
inequality.
consult
spending.
tcot
money
CapeTown
jozi
birthday.
October!
findom
greedy
Saving
Expenses
DailyHabits
Robotics
jobs
sales
economy
Startup
growth
Pruitt
EPAs"
13years
Lost.
Friends
LakeEola
MegWhite...
WhiteStripes
Florida
Coincidence
IthinkNot
karma
coincidence
Wonderful
KylieJenner
Kuwtk
weird
nyc
gymlife
coincidence?
ThinkNot
Coincidence?
publicpower
ithinknot
Destiny
Chance
ExamineFate
Humour
ASMSG
BYNR
IARTG
CoIncidence
national
awards
India
Current
Affair
Today.
Who
NTS
Question
KaShMiR
Affairs
important
CURRENT
AFFAIRS
RD28917
current
affairs
basic
quiz
IBPS
RRB
Clerk
VSS365
BigData
MLaaS
Tech-savvy
human
Jobs
Autonomous
Watson
Cognitive
IoT
Industry40
IIoT
DataScience
DataScientist
futurism
robotics
deepmind
technology
DeepLearning
DLUPC
HPC
tech
Cloud
Video
Bot
SMM
IoT?
SmartCity
Health
3DPrinting
AISummit
SEO
deeplearning
searchengines
healthcare
robots
robot
bot
Mpgvip
AI?
Fintech
defstar5
4IR
Deeplearning
EntBullets
3wordQuote
mpgvip
Entrepreneur
Businesstips
ss11
ioT
mlm
LessPay
DataMining
IOT
IOE
blockchain
RBC
net
Websites
banking
NMCHI17
Algorithms
AI:
abdsc
Applications
Bigdata
SaaS
DataViz
IaaS
PaaS
content
random
Apple
ARKit
iOS
Keywords
disruption
retail
innovation
cstore
kirin970
AI.
Ethiopia
todays
abayfm
Todays
Mental
ImpeachTrump
Fakenews
VeryFakenews!
Trump:"Maybe
SNL
MSM
VOTE!
FOX
TeamUSAon
PeoplePower
retweet

!rm tweets.db

import sqlite3
import time
import sys
import base64
conn = sqlite3.connect('tweets.db')
c = conn.cursor()
c.execute('''CREATE VIRTUAL TABLE twitter
             USING FTS3 (id,twittertext)''')


def findhash():
    id = 0
    with open('hashtag.txt', 'r') as textin:
          for line in textin.readlines(): 
                id = id+1
                #hashed = [ word for word in line.split() if word.startswith("#") ]
                #hashed = line.split()
                #hashed = str(hashed)
                #hashed = hashed.replace("[","");hashed = hashed.replace("]","")
                #hashed = hashed.replace(",","\n");hashed = hashed.replace(" '","")
                #hashed = hashed.replace("'","");hashed = hashed.replace("#\n ","")
                #hashed = hashed.replace("#","\n#")
                time.sleep(1)
                conn = sqlite3.connect('tweets.db')
                conn.text_factory = str
                c = conn.cursor()
                c.execute("INSERT INTO twitter VALUES (?,?)", (id, line)) 
                conn.commit()
                conn.close()                        
                print line

                
                
                
                
                
                

findhash()

def findhash():
    with open('hashtag.txt', 'r') as textin:
        tempstore = set()
        with open('hashonly.txt', 'w') as outfile:
            for line in textin.readlines():
                hashed = [ word for word in line.split() if word.startswith("#") ]
                #hashed = word for word in line.split() if word.startswith("#")
                hashed = str(hashed)
                hashed = hashed.replace("[","");hashed = hashed.replace("]","")
                hashed = hashed.replace(",","\n");hashed = hashed.replace(" '","")
                hashed = hashed.replace("'","");hashed = hashed.replace("#\n ","")
                hashed = hashed.replace("#","\n#")
                outfile.write(hashed)


findhash()

def removeblank():
    with open('hashonly.txt') as infile, open('hashonlyNoBlank.txt', 'w') as outfile:
        for line in infile:
            if not line.strip(): continue  # skip the empty line
            outfile.write(line)  # non-empty
            
removeblank() 

def remove_duplicates(infile):
    tempstore = set()
    with open('hashonlyNoBlankNoDups.txt', 'w+') as out:
        for line in open(infile):
            if line not in tempstore:
                if len(line) < 16 and len(line) >4:
                    out.write(line)
                    tempstore.add(line)

remove_duplicates('hashonlyNoBlank.txt')

def removeHash(infile):
    with open('clean2.txt', 'w+') as out:
        for line in open(infile):
            line = line.replace("#","");line = line.replace('"','')
            out.write(line)

removeHash('hashonlyNoBlankNoDups.txt')



def findhash():
    with open('hashtag.txt', 'r') as textin:
        tempstore = set()
        with open('temp.txt', 'w') as outfile:
            for line in textin.readlines():
                hashed = [ word for word in line.split() if word.startswith("#") ]
                #hashed = word for word in line.split() if word.startswith("#")
                hashed = str(hashed)
                hashed = hashed.replace("[","");hashed = hashed.replace("]","")
                hashed = hashed.replace(",","\n");hashed = hashed.replace(" '","")
                hashed = hashed.replace("'","");hashed = hashed.replace("#\n ","")
                hashed = hashed.replace("#","\n#")
                outfile.write(hashed)
    outfile.close()
    with open('temp.txt', 'r') as infile:
        with open('temp2.txt', 'w') as outfile:
             for line in infile:
                if not line.strip(): continue  # skip the empty line
                outfile.write(line)  # non-empty
    outfile.close()            
    with open('cleanwords.txt', 'w') as out:
        for line in open('temp2.txt', 'r'):
            line = line.replace("#","")
            out.write(line)                
                
                
findhash() 

def findhash():
    with open('hashtag.txt', 'r') as textin:
        tempstore = set()
        with open('temp.txt', 'w') as outfile:
            for line in textin.readlines():
                hashed = [ word for word in line.split() if word.startswith("#") ]
                #hashed = word for word in line.split() if word.startswith("#")
                hashed = str(hashed)
                hashed = hashed.replace("[","");hashed = hashed.replace("]","")
                hashed = hashed.replace(",","\n");hashed = hashed.replace(" '","")
                hashed = hashed.replace("'","");hashed = hashed.replace("#\n ","")
                hashed = hashed.replace("#","\n#")
                outfile.write(hashed)
    textin.close
    outfile.close()            
    with open('temp2.txt', 'w+') as out:
        for line in open('temp.txt', 'r'):
            line = line.replace("#","")
            out.write(line)                
    outfile.close()
    with open('temp2.txt', 'r') as infile:
        with open('cleanout.txt', 'w') as outfile:
             for line in infile:
                if not line.strip(): continue  # skip the empty line
                outfile.write(line)  # non-empty                
                
findhash() 





!ls /usr/share/dict/

text = open("/usr/share/dict/british-english",'r').readlines()

for lines in text:
    if lines.find("word") == 0:
        print "word is in the dictionary"

text = open("/usr/share/dict/british-english",'r').readlines()
with io.open("clean2.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 
for lines in text:
    if lines.find(essays) == 0:
        print "word is in the dictionary"

text = open("/usr/share/dict/british-english",'r').readlines()
badtext = ''.join(c for c in map(chr, range(256)) if not c.isalnum())

def stripNonAlphaNum(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)

with open("clean2.txt", "r") as my_file:
    words = my_file.read()
    #words = stripNonAlphaNum(words)
    for lines in text:
        if lines.find(words) != 0:
            print words    


text = open("/usr/share/dict/british-english",'r').readlines()
badtext = ''.join(c for c in map(chr, range(256)) if not c.isalnum())

def stripNonAlphaNum(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)

with io.open("clean2.txt", "r", encoding="utf-8") as my_file:
    words = my_file.read()
    words = stripNonAlphaNum(words)
    words = str(words)
    for lines in text:
        if lines.find(words) == 0:
            print words

text = open("/usr/share/dict/british-english",'r').readlines()
badtext = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
with io.open("clean2.txt", "r", encoding="utf-8") as my_file:
    words = my_file.read()
    word = words.translate(None, badtext)
for lines in text:
    if lines.find(words) == 0:
        print "word is in the dictionary"

badtext = ''.join(c for c in map(chr, range(173)) if not c.isalnum())
print badtext

word = words.translate(None, badtext)

from textblob import TextBlob
from nltk.corpus import wordnet

tweetfile = 'realwords.txt'
filein = open(tweetfile, 'w')
filein.close()  
with io.open("clean2.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 
    if not wordnet.synsets(essays): 
        #Not an English Word
        print essays,"- Is not a word"
    else:
        #English Word    
        filein = open(tweetfile, 'a')
        filein.write(essays)
        filein.close()    

        print essays


from textblob import TextBlob
tweetfile = 'realwords.txt'
filein = open(tweetfile, 'w')
filein.close()  
with io.open("clean2.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read()
    if wordnet.synsets(essays):
        print essays


import time
def findhash():
    with open('hashonly.txt', 'r') as textin:
        tempstore = set()
        with open('hashonlyS.txt', 'w') as outfile:
            for line in textin.readlines():
                line = line.replace("##","#")
                line = line.replace("#","\n#")
                
                if len(line) < 16 and len(line) >3: 
                    outfile.write(line)
findhash()

def findhash():
    with open('phrases.txt', 'r') as textin:
        tempstore = set()
        with open('hashonly.txt', 'w') as outfile:
            for line in textin.readlines():
                hashed = [ word for word in line.split() if word.startswith("#") ]
                #hashed = word for word in line.split() if word.startswith("#")
                hashed = str(hashed)
                hashed = hashed.replace("[","");hashed = hashed.replace("]","")
                hashed = hashed.replace(",","\n");hashed = hashed.replace(" '","")
                hashed = hashed.replace("'","");hashed = hashed.replace("#\n ","")
                outfile.write(hashed)


findhash()

with open('hashonly.txt') as infile, open('hashonlyNoBlank.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)  # non-empty

with open('hashonlyS.txt') as infile, open('NShashonlyS.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)  # non-empty

from bs4 import BeautifulSoup
import requests
import sqlite3
import base64
import time
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

#url = u'https://twitter.com/search?q='
#HashTag = (random_line('hashtag-nouns.txt'))
HashTag = (random_line('hashonly.txt'))
HashTag = HashTag.replace("#", "")
print HashTag

textin= open('hashonly.txt', 'r')
lines = textin.read().splitlines()
time.sleep(1)
print lines





from textblob import TextBlob
from nltk.corpus import wordnet
tweetfile = 'phrases.txt'
filein = open(tweetfile, 'w')
filein.close()  
with io.open("hashtag.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 

blob = TextBlob(essays)
try:
    for np in blob.noun_phrases:
        filein = open(tweetfile, 'a')
        np = '\n'+ u''.join((np)).encode('utf-8').strip()
        np=np.replace("#","");np=np.replace("//","")
        np=np.replace("... ”","");np=np.replace("... ","")
        np=np.replace(".. ","")
        np = np.lstrip()
        if len(np) < 16 and len(np) >3:
            np = (np+"\n")
            np = str(np)
    if wordnet.synsets(np):
        filein.write(np)
        filein.close()    

               
        # block raising an exception
except:
       pass # doing nothing on exception        
print np





from bs4 import BeautifulSoup
import requests
import sqlite3
import base64
import time
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

#url = u'https://twitter.com/search?q='
#HashTag = (random_line('hashtag-nouns.txt'))
HashTag = (random_line('hashonly.txt'))
HashTag = HashTag.replace("#", "")
url = u'https://twitter.com/hashtag/'+ HashTag +'?lang=en'
tweetfile = 'hashtag.txt'
#url = u'https://twitter.com/scavino45/lists/florida-hurricane-irma'
#url = u'https://twitter.com/Selebog55680943'
#url = u'https://twitter.com/WinMansfield'
#query = u'%40drawranliou'
#query = u'%23hurricanne&src=typd'
#query = u'python, florida'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

tweets = [p.text for p in soup.findAll('p', class_='tweet-text')]
txt = (tweets)
for list in txt:
    filein = open(tweetfile, 'a')
    list = list.replace(u'\xa0', u' ')
    list = list.replace(u'\u2026','ignore')
    list = list.replace(u'\xa0','ignore')
    list = list.replace(u'\u2013', u' ')
    list = list.replace(u'\xf1', u' ')
    list = list.replace(u'\u2019','ignore')
    list = '\n'+ u''.join((list)).encode('utf-8').strip()
   
    filein.write(list)
    filein.close()
    time.sleep(1)
    print list


from bs4 import BeautifulSoup
import requests
import sqlite3
import base64
import time
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

#url = u'https://twitter.com/search?q='
#HashTag = (random_line('hashtag-nouns.txt'))
HashTag = (random_line('hashonly.txt'))
HashTag = HashTag.replace("#", "")
#url = u'https://twitter.com/search?q='+ HashTag +'&src=typd&lang=en'
#https://twitter.com/search?q=%23cnn&src=typd&lang=en
#url = u'https://twitter.com/search?q='+ HashTag +'&src=typd&lang=en'
url = u'https://twitter.com/'+ HashTag +'?lang=en'
#url = u'https://twitter.com/hashtag/'+ HashTag +'?lang=en'
#url = u'https://twitter.com/scavino45/lists/florida-hurricane-irma'
#url = u'https://twitter.com/Selebog55680943'
#url = u'https://twitter.com/WinMansfield'
#query = u'%40drawranliou'
#query = u'%23hurricanne&src=typd'
#query = u'python, florida'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
tweets = [p.text for p in soup.findAll('p', class_='tweet-text')]


from bs4 import BeautifulSoup
import requests
import sqlite3
import base64
import time
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

#url = u'https://twitter.com/search?q='
#HashTag = (random_line('hashtag-nouns.txt'))
HashTag = (random_line('hashonly.txt'))
print HashTag

from bs4 import BeautifulSoup
import requests
import sqlite3
import base64
import time
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

#url = u'https://twitter.com/search?q='
#HashTag = (random_line('hashtag-nouns.txt'))
HashTag = (random_line('hashonly.txt'))
url = u'https://twitter.com/'+ HashTag +'?lang=en'
#url = u'https://twitter.com/hashtag/'+ HashTag +'?lang=en'
tweetfile = 'hashtag.txt'
#url = u'https://twitter.com/scavino45/lists/florida-hurricane-irma'
#url = u'https://twitter.com/Selebog55680943'
#url = u'https://twitter.com/WinMansfield'
#query = u'%40drawranliou'
#query = u'%23hurricanne&src=typd'
#query = u'python, florida'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

tweets = [p.text for p in soup.findAll('p', class_='tweet-text')]
txt = (tweets)
for list in txt:
    filein = open(tweetfile, 'a')
    list = list.replace(u'\xa0', u' ')
    list = list.replace(u'\u2026','ignore')
    list = list.replace(u'\xa0','ignore')
    list = list.replace(u'\u2013', u' ')
    list = list.replace(u'\xf1', u' ')
    list = list.replace(u'\u2019','ignore')
    list = '\n'+ u''.join((list)).encode('utf-8').strip()
   
    filein.write(list)
    filein.close()
    time.sleep(1)
    print list


from bs4 import BeautifulSoup
import requests
import sqlite3
import base64
import time
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

#url = u'https://twitter.com/search?q='
#HashTag = (random_line('hashtag-nouns.txt'))
HashTag = (random_line('hashonly.txt'))
url = u'https://twitter.com/hashtag/'+ HashTag +'?lang=en'
tweetfile = 'hashtag.txt'
#url = u'https://twitter.com/scavino45/lists/florida-hurricane-irma'
#url = u'https://twitter.com/Selebog55680943'
#url = u'https://twitter.com/WinMansfield'
#query = u'%40drawranliou'
#query = u'%23hurricanne&src=typd'
#query = u'python, florida'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

tweets = [p.text for p in soup.findAll('p', class_='tweet-text')]
txt = (tweets)
for list in txt:
    filein = open(tweetfile, 'a')
    list = list.replace(u'\xa0', u' ')
    list = list.replace(u'\u2026','ignore')
    list = list.replace(u'\xa0','ignore')
    list = list.replace(u'\u2013', u' ')
    list = list.replace(u'\xf1', u' ')
    list = list.replace(u'\u2019','ignore')
    list = '\n'+ u''.join((list)).encode('utf-8').strip()
   
    filein.write(list)
    filein.close()
    time.sleep(1)
    print list


def random_line(fname):
    lines = open(fname).readlines()
text = random_line('hashonly.txt') 
print text

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
#url = u'https://twitter.com/search?q='
HashTag = (random_line('hashtag-nouns.txt'))
print HashTag

textin= open('hashtag.txt', 'r')
lines = textin.read().splitlines()
time.sleep(1)
print lines,

def findhash():
    with open('hashtag.txt', 'r') as textin:
        tempstore = set()
        with open('hashonly.txt', 'w') as outfile:
            for line in textin.readlines():
                hashed = [ word for word in line.split() if word.startswith("#") ]
                #hashed = word for word in line.split() if word.startswith("#")
                hashed = str(hashed)
                hashed = hashed.replace("#","\n#")
                if len(hashed) < 36 and len(hashed) >3:
                    hashed = hashed.replace("[","");hashed = hashed.replace("]","")
                    hashed = hashed.replace(",","\n");hashed = hashed.replace(" '","")
                    hashed = hashed.replace("'","");hashed = hashed.replace("#\n ","")
                    hashed = hashed.replace('"','')
                    outfile.write(hashed)


findhash()


def linesonly():
    with open('hashonly.txt') as infile, open('hashonlyNoBlank.txt', 'w') as outfile:
        for line in infile:
            if not line.strip(): continue  # skip the empty line
            outfile.write(line)  # non-empty
linesonly()            

def findhash():
    with open('hashtag.txt', 'r') as textin:
        tempstore = set()
        with open('hashonly.txt', 'w') as outfile:
            for line in textin.readlines():
                hashed = [ word for word in line.split() if word.startswith("#") ]
                #hashed = word for word in line.split() if word.startswith("#")
                hashed = str(hashed)
                hashed = hashed.replace("#","\n#")
                if len(hashed) < 36 and len(hashed) >3:
                    hashed = hashed.replace("[","");hashed = hashed.replace("]","")
                    hashed = hashed.replace(",","\n");hashed = hashed.replace(" '","")
                    hashed = hashed.replace("'","");hashed = hashed.replace("#\n ","")
                    hashed = hashed.replace('"','')
                    outfile.write(hashed)


findhash()








def findhash():
    with open('hashtag.txt', 'r') as textin:
        tempstore = set()
        with open('hashonly.txt', 'w') as outfile:
            for line in textin.readlines():
                hashed = [ word for word in line.split() if word.startswith("#") ]
                #hashed = word for word in line.split() if word.startswith("#")
                hashed = str(hashed)
                hashed = hashed.replace("#","\n#")
                if len(hashed) < 36 and len(hashed) >3:
                    hashed = hashed.replace("[","");hashed = hashed.replace("]","")
                    hashed = hashed.replace(",","\n");hashed = hashed.replace(" '","")
                    hashed = hashed.replace("'","");hashed = hashed.replace("#\n ","")
                    outfile.write(hashed)


findhash()

import re

with open('hashtag-nouns.txt').read().splitlines() as lines:
    matches = re.findall(r'#\w*', line)
    #url = u'https://twitter.com/search?q='
    #matches = (findhash('hashtag-nouns.txt'))
    print matches

import re    

for line in open('phrases3.txt', 'r'):
    re.findall(r'#\w*', line)
    print re.findall(r'#\w*', line)

import re    
with open('phrases3.txt', 'a') as hashout:
     for line in open('phrases3.txt'):
        matches = re.findall(r'#\w*', line)
        print matches

import re
def findhash(fname):
    lines = open(fname).read().splitlines()
    matches = re.findall(r'#\w*', line)
#url = u'https://twitter.com/search?q='
matches = (findhash('hashtag-nouns.txt'))
print matches

hashed = [ word for word in line.split() if word.startswith("#") ]

from bs4 import BeautifulSoup
import requests
import sqlite3
import base64
import time
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
#url = u'https://twitter.com/search?q='
HashTag = (random_line('hashtag-nouns.txt'))
print HashTag

def remove_duplicates(infile):
    tempstore = set()
    with open('phrases3.txt', 'w+') as out:
        for line in open(infile):
            if line not in tempstore:
                out.write(line)
                tempstore.add(line)

remove_duplicates('phrases2.txt')

#lines = open('phrases.txt', 'r').readlines()
lines = open('phrases.txt', 'r').read()
lines_set = set(lines)
out  = open('phrases2.txt', 'w')
for line in lines_set:
    out.write(line)

from bs4 import BeautifulSoup
import requests
import sqlite3
import base64
import time
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

#url = u'https://twitter.com/search?q='
#HashTag = (random_line('hashtag-nouns.txt'))
HashTag = (random_line('phrases2.txt'))
url = u'https://twitter.com/hashtag/'+ HashTag +'?lang=en'
tweetfile = 'hashtag.txt'
#url = u'https://twitter.com/scavino45/lists/florida-hurricane-irma'
#url = u'https://twitter.com/Selebog55680943'
#url = u'https://twitter.com/WinMansfield'
#query = u'%40drawranliou'
#query = u'%23hurricanne&src=typd'
#query = u'python, florida'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

tweets = [p.text for p in soup.findAll('p', class_='tweet-text')]
txt = (tweets)
for list in txt:
    filein = open(tweetfile, 'a')
    list = list.replace(u'\xa0', u' ')
    list = list.replace(u'\u2026','ignore')
    list = list.replace(u'\xa0','ignore')
    list = list.replace(u'\u2013', u' ')
    list = list.replace(u'\xf1', u' ')
    list = list.replace(u'\u2019','ignore')
    list = '\n'+ u''.join((list)).encode('utf-8').strip()
   
    filein.write(list)
    filein.close()
    time.sleep(1)
    print list


%%writefile Bt.py
def badtext(essays):
    badtext = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
    essay = essay.translate(badtext)
    return essay

!touch phrases.txt

from nltk.tag import pos_tag
import io
import Tidyt
with io.open("hashtag.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 
    tagged_sent = pos_tag(essays.split())
    output = open("hashtag-nouns.txt", "w")
    propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
    in_string = str(propernouns)
    propernouns = Tidyt.tidyt(in_string)
        
    propernouns = propernouns.replace("  "," \n")
    output.write(propernouns)
    output.close()    
    print propernouns  

!ls *.txt

from loremipsum import get_sentences
sentences_list = get_sentences(5)
len(sentences_list)



http://loremipsum.readthedocs.io/en/latest/

from loremipsum import generate_paragraph
sentences_count, words_count, paragraph = generate_paragraph()

file = open('hashtag.txt', 'r')
book = file.read()
def tokenize():
    if book is not None:
        words = book.lower().split()
        return words
    else:
        return None
def count_word(tokens, token):
    count = 0
    for element in tokens:
        # Remove Punctuation
        word = element.replace(",","")
        word = word.replace(".","")
        # Found Word?
        if word == token:
            count += 1
    return count
# Tokenize the Book
words = tokenize()

# Get Word Count
word = '#ciso'
frequency = count_word(words, word)
print('Word: [' + word + '] Frequency: ' + str(frequency))

import random 

# get the first line if this is the one with the words words
lines = open("hashtag.txt").readlines() 
line = lines[0] 

words = line.split() 
myword = random.choice(words)
print myword

from textblob import TextBlob
tweetfile = 'phrases.txt'
with io.open("hashtag.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 

blob = TextBlob(essays)
for np in blob.noun_phrases:
    filein = open(tweetfile, 'a')
    np = '\n'+ u''.join((np)).encode('utf-8').strip()
    np=np.replace("# ","#");np=np.replace("//","")
    filein.write(np)
    filein.close()    
    
    print np


import random
with open("hashtag-nouns.txt") as word_file:
    words = word_file.read().split() #This splits by whitespace, if you used some other delimiter specify the delimiter here as an argument.
random_word = random.choice(words)
print random_word

import random
with open("hashtag.txt") as word_file:
    words = word_file.readline().split() #This splits by whitespace, if you used some other delimiter specify the delimiter here as an argument.
random_word = random.choice(words)
print random_word

from loremipsum import Generator
from loremipsum import get_sentences

with open('hekel.txt', 'r') as sample_txt:
     sample = sample_txt.read()
with open('hashtag-nouns.txt', 'r') as dictionary_txt:
     dictionary = dictionary_txt.read().split()

g = Generator(sample, dictionary)
sentence = g.get_sentence()


from textblob import TextBlob
tweetfile = 'phrases.txt'
with io.open("hashtag.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 

blob = TextBlob(essays)
for np in blob.noun_phrases:
    if len(np) < 36 and len(np) >3:
        filein = open(tweetfile, 'a')
        np = '\n'+ u''.join((np)).encode('utf-8').strip()
        np=np.replace("# ","#");np=np.replace("//","")
        filein.write(np)
        filein.close()    

        print np


of = open("orig")
nf = open("new",'w')
for line in of:         
    if len(line) < 2048:
        nf.write(line)
of.close()
nf.close()

from textblob import TextBlob
with io.open("hashtag.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 

blob = TextBlob(essays)
for np in blob.noun_phrases:
    print np


%%writefile RandNoun.py
def randnoun():
    import random, heapq
    def main():
        with open('hashtag-nouns.txt') as fin:
            word, = heapq.nlargest(1, fin, key=lambda L: random.random())
            word = word.decode('utf-8')
    return word 

!rm RandNoun.pyc

import RandNoun
a = RandNoun.randnoun()


#%%writefile RandNoun.py
def randnoun():
    import random, heapq
    def main():
        with open('hashtag-nouns.txt') as fin:
            word, = heapq.nlargest(1, fin, key=lambda L: random.random())
            word = word,
    return word        
main()        

import RandNoun
RandNoun.randnoun()
url = u'https://twitter.com/hashtag/'+ str(RandNoun.randnoun()) +'?lang=en'      

from bs4 import BeautifulSoup
import requests
import sqlite3
import base64
import time

 
#url = u'https://twitter.com/search?q='
HashTag = raw_input("HashTag  : ") or "CNN"
url = u'https://twitter.com/hashtag/'+ HashTag +'?lang=en'
tweetfile = 'hashtag.txt'
#url = u'https://twitter.com/scavino45/lists/florida-hurricane-irma'
#url = u'https://twitter.com/Selebog55680943'
#url = u'https://twitter.com/WinMansfield'
#query = u'%40drawranliou'
#query = u'%23hurricanne&src=typd'
#query = u'python, florida'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

tweets = [p.text for p in soup.findAll('p', class_='tweet-text')]
txt = (tweets)
for list in txt:
    filein = open(tweetfile, 'a')
    list = list.replace(u'\xa0', u' ')
    list = list.replace(u'\u2026','ignore')
    list = list.replace(u'\xa0','ignore')
    list = list.replace(u'\u2013', u' ')
    list = list.replace(u'\xf1', u' ')
    list = list.replace(u'\u2019','ignore')
    list = '\n'+ u''.join((list)).encode('utf-8').strip()
   
    filein.write(list)
    filein.close()
    time.sleep(1)
    print list


import random, heapq
def main():
    with open('hashtag-nouns.txt') as fin:
        word, = heapq.nlargest(1, fin, key=lambda L: random.random())
        print word,
        
main()        

import random, heapq

with open('hashtag-nouns.txt') as fin:
    word, = heapq.nlargest(1, fin, key=lambda L: random.random())
    print word,

import random
def generate_the_word(infile):
    with open(infile) as f:
        contents_of_file = f.read()
    lines = contents_of_file.splitlines()
    line_number = random.randrange(0, len(lines))
    return lines[line_number]
def main():
    print(generate_the_word("hashtag-nouns.txt"))

main()

from nltk.tag import pos_tag
import io
import Tidyt
with io.open("ToUse.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 
    tagged_sent = pos_tag(essays.split())
    output = open("output2.txt", "w")
    propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
    in_string = str(propernouns)
    propernouns = Tidyt.tidyt(in_string)
    output.write(propernouns)
    output.close()    
    print propernouns  

%%writefile Tidyt.py
#import Tidyt
#ftexout = Tidyt.tidyt(in_string)
def tidyt(in_string):    
    texout = in_string.replace("', u'", "  ");texout = texout.replace("\u2018", "")
    texout = texout.replace("\u2019 ", "");texout = texout.replace("%", "")
    texout = texout.replace("[u'", "");texout = texout.replace(" u'", "")
    texout = texout.replace(', u"', ' ');texout = texout.replace('",', ' ')
    texout = texout.replace("'", '');texout = texout.replace("Mr.  ", 'Mr. ')
    texout = texout.replace(",", '');texout = texout.replace(".", '')
    ftexout =texout.replace("']", "")
    return ftexout

from textblob import TextBlob
import time
import sys
with io.open("ToUse.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 
count = 0
Sent = input('Sent') or int(1)
Start = input('Start') or int(1)
End = input('End') or int(5)
Start= int(Start)
End= int(End)
blob = TextBlob(essays)
for word in blob.sentences[Sent].words:
    count = count +1
    if count >= Start and count <= End:
        print count,":",word
    else:
        my_file.close()
        sys.exit

    

from textblob import TextBlob
with io.open("ToUse.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 

blob = TextBlob(essays)
for np in blob.noun_phrases:
    print np


from textblob import TextBlob
with io.open("ToUse.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 
blob = TextBlob(essays)
for word, pos in blob.tags:
    print word, pos

import nltk
from nltk import word_tokenize
with io.open("ToUse.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 

text = word_tokenize(essays)
nltk.pos_tag(text)


from textblob import TextBlob
with io.open("ToUse.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 
blob = TextBlob(essays)
for sentence in blob.sentences:
    print sentence

from textblob import TextBlob
with io.open("ToUse.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 
    blob = TextBlob(essays)
    sentence = blob.sentences[1]
    for word, pos in sentence.tags:
        if pos == 'NN':
            print word.pluralize()

%%writefile text2sent.py
from textblob import TextBlob
import random
import sys

# stdin's read() method just reads in all of standard input as a string;
# use the decode method to convert to ascii (textblob prefers ascii)
text = sys.stdin.read().decode('ascii', errors="replace")
blob = TextBlob(text)

short_sentences = list()
for sentence in blob.sentences:
    if len(sentence.words) <= 5:
        short_sentences.append(sentence.replace("\n", " "))

for item in random.sample(short_sentences, 10):
	print item

!python text2sent.py < junque.txt

!python text2sent.py < hekel.txt

from textblob import TextBlob
import random
import sys
import io
filename ="/home/jack/Desktop/imagebot/data/dracula.txt"
with io.open(filename, "r", encoding="utf-8") as my_file:
    essays = my_file.read() 
# stdin's read() method just reads in all of standard input as a string;
# use the decode method to convert to ascii (textblob prefers ascii)
#text = sys.stdin.read().decode('ascii', errors="replace")
blob = TextBlob(essays)

short_sentences = list()
for sentence in blob.sentences:
    if len(sentence.words) <= 10:
        short_sentences.append(sentence.replace("\n", " "))

for item in random.sample(short_sentences, 10):
	print item

from textblob import TextBlob
import random
import sys
import io
filename ="/home/jack/Desktop/imagebot/hekel.txt"
with io.open(filename, "r", encoding="utf-8") as my_file:
    essays = my_file.read() 
# stdin's read() method just reads in all of standard input as a string;
# use the decode method to convert to ascii (textblob prefers ascii)
#text = sys.stdin.read().decode('ascii', errors="replace")
blob = TextBlob(essays)

short_sentences = list()
for sentence in blob.sentences:
    if len(sentence.words) <= 10:
        short_sentences.append(sentence.replace("\n", " "))

for item in random.sample(short_sentences, 10):
	print item

from textblob import TextBlob
import sys
import random
filename ="/home/jack/Desktop/imagebot/hekel.txt"
with io.open(filename, "r", encoding="utf-8") as my_file:
    essays = my_file.read() 
    
text = sys.stdin.read().decode('ascii', errors="replace")
blob = TextBlob(essays)

noun_phrases = blob.noun_phrases

verbs = list()
for word, tag in blob.tags:
    if tag == 'VB':
        verbs.append(word.lemmatize())

for i in range(1, 11):
    print "Step " + str(i) + ". " + random.choice(verbs).title() + " " + \
        random.choice(noun_phrases)

from bs4 import BeautifulSoup
import requests
import csv
import codecs

hashtag = raw_input("hashtag") or "angry crowd"
url = u'https://twitter.com/search?l=en&q='+ hashtag +'&src=typd'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
tweets = [p.text for p in soup.findAll('p', class_='tweet-text')]
txt = (tweets)
file = codecs.open( "testfile.txt", "a", "utf-8" )
for list in txt:
    mytext = "<br />\n".join(list.split(".\n\n"))
    file.write(mytext)      
    print mytext
file.close() 

import re
import textwrap

with open("testfile.txt", "r") as f:
    text = f.read()
    #This was added to get ride od the unicode u from showing up
    words = text.replace(' u ', ' ');words = words.replace('u ', '');words = words.replace(' U ', ' ')
    #This clears out the non-Alpha-numeric characters
    #badtext = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
    badtext = '!,",#,$,%,&,(,),*,+,,-,.,/,:;<=>?@[\]^_`{|}~'
    
    # limit the aount of characters perline displayed
    chars_per_line = 110
    for i in range(0, len(words), chars_per_line):
        word = words.translate(None, badtext)
        print words[i:i+chars_per_line]

from textblob import TextBlob
import sys
import random
import io
filename ="testfile.txt"
with io.open(filename, "r", encoding="utf-8") as my_file:
    essays = my_file.read() 
    
text = sys.stdin.read().decode('ascii', errors="replace")
blob = TextBlob(essays)

noun_phrases = blob.noun_phrases

verbs = list()
for word, tag in blob.tags:
    if tag == 'VB':
        verbs.append(word.lemmatize())

for i in range(1, 50):
    print "Step " + str(i) + ". " + random.choice(verbs).title() + " " + \
        random.choice(noun_phrases)

from bs4 import BeautifulSoup
import requests
url = u'https://twitter.com/search?q='
#query = u'%40drawranliou'
#query = u'@JamesOKeefeIII'
#query = u'hurricanne&src=typd'
query = u'very confused'
r = requests.get(url+query)
soup = BeautifulSoup(r.text, 'html.parser')
tweets = [p.text for p in soup.findAll('p', class_='tweet-text')]
txt = (tweets)

for list in txt:
    mytext = "<br />\n".join(list.split("\n\n"))
    
    print mytext
    

import Tpost
help(Tpost.tpost)

Graphic art is a visual expression of a mental perception.

import Tpost
ImgPath ='/home/jack/Desktop/save-twitter/20170824180714.jpg'
STR = "Graphic art is a mental perception communicated with visual expression."
Tpost.tpost(ImgPath,STR)

from textblob import TextBlob
import random
import sys
import io
with io.open("testfile.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 
blob = TextBlob(essays)
for sentence in blob.sentences:
    print sentence
    short_sentences = list()
    for sentence in blob.sentences:
        if len(sentence.words) <= 5:
            short_sentences.append(sentence.replace("\n", " "))

    for item in random.sample(short_sentences, 10):
        print item    

import time
file = open("testfile.txt")
lines = file.read()
for line in lines:
    line = (lines.split("\n"))
    time.sleep(5)
    print line
   

----------------------------------------



import time
file = open("testfile.txt")
lines = file.read()
for line in lines:
    
    
    print line.join(lines.split(".\n\n"))
    time.sleep(5)

import time
file = open("testfile.txt")
lines = file.read()
for line in lines:
    
    time.sleep(1)
    print line.join(lines.split(".\n\n"))

file = codecs.open( "testfile.txt", "r", "utf-8" )
u = file.read()
print u

from bs4 import BeautifulSoup
import requests
import io
import string
def get_text_cleaned(tweet):
    tweet = tweet.replace("u'", "");tweet = tweet.replace(" id ", "\n id")
    return tweet

def get_text_sanitized(tweet):    
    return ' '.join([w.lower().strip().rstrip(string.punctuation)\
        .lstrip(string.punctuation).strip()\
        for w in get_text_cleaned(tweet).split()\
        if w.strip().rstrip(string.punctuation).strip()])

with io.open("testfile002.txt", "w", encoding="utf-8") as my_file:
    

    url = u'https://twitter.com/search?q='
    #query = u'%40drawranliou'
    #query = u'@JamesOKeefeIII'
    #query = u'hurricanne&src=typd'
    query = u'nasa-project'
    r = requests.get(url+query)
    soup = BeautifulSoup(r.text, 'html.parser')
    tweets = [p.text for p in soup.findAll('p', class_='tweet-text')]
    txt = (tweets)
    output = open("exp001.txt", "w")
    for list in txt:
        list =get_text_sanitized(list)    
        mytext = "<br />\n".join(list.split("\n\n"))
        txt = [unicode(mytext).encode("utf-8")]
        txt = str(txt)
        my_file.write(mytext) 
        print mytext
output.close()    

string_with_stuff = "weird \xe1ccents"
print string_with_stuff.decode('ascii', errors="ignore")

from textblob import TextBlob, Word
import sys
import random
filename ="/home/jack/Desktop/imagebot/hekel.txt"
with io.open(filename, "r", encoding="utf-8") as my_file:
    essays = my_file.read() 
    
text = sys.stdin.read().decode('ascii', errors="ignore")
blob = TextBlob(essays)

nouns = list()
for word, tag in blob.tags:
	if tag == 'NN':
		nouns.append(word.lemmatize())

print "This text is about..."
for item in random.sample(nouns, 5):
	word = Word(item)
	print word.pluralize()

from textblob import Word
bank = Word("amazing")
synsets = bank.synsets
print synsets

from textblob import Word
synsets = Word("amazing").synsets
for synset in synsets:
    print synset.definition()

from textblob import Word
from textblob.wordnet import NOUN
synsets = Word("bank").get_synsets(pos=NOUN)
for synset in synsets:
    print synset.definition()

from textblob import Word
from textblob.wordnet import NOUN
synsets = Word("bank").get_synsets(pos=NOUN)
print synsets[1].lemma_names()

from textblob import Word
from textblob.wordnet import NOUN
synsets = Word("plane").get_synsets(pos=NOUN)
print synsets[1].lemma_names()

from textblob import Word
from textblob.wordnet import VERB
synsets = Word("plane").get_synsets(pos=VERB)
print synsets[1].lemma_names()

from textblob import Word
from textblob.wordnet import NOUN
synsets = Word("plane").get_synsets(pos=NOUN)
for synset in synsets:
    print synset.definition()

import sys
import random
import io
count = 0
with io.open("ToUse.txt", "r", encoding="utf-8") as my_file:
    sys.stdin = [my_file.read()] 
for line in sys.stdin:
    print line

import sys
with io.open("ToUse.txt", "r", encoding="utf-8") as my_file:
    sys.stdin = [my_file.read()] 
for line in sys.stdin:
    print line

%%writefile syn.py
from textblob import Word
import sys
import random

for line in sys.stdin:
    line = line.strip()
    line = line.decode('ascii', errors="replace")
    words = line.split(" ")
    output = list()
    for word_str in words:
        word_obj = Word(word_str)
        if len(word_str) > 3 and len(word_obj.synsets) > 0:
            random_synset = random.choice(word_obj.synsets)
            random_lemma = random.choice(random_synset.lemma_names)
            output.append(random_lemma.replace('_', ' '))
        else:
            output.append(word_str)
print " ".join(output)


#%%writefile syn.py
from textblob import Word
import sys
import random
filename ="hek.txt"
with io.open(filename, "r", encoding="utf-8") as my_file:
    sys.stdin = [my_file.read()] 
    for line in sys.stdin:
        line = line.strip()
        line = line.decode('ascii', errors="replace")
        words = line.split(" ")
        output = list()
    for word_str in words:
        word_obj = Word(word_str)
    if len(word_str) > 3 and len(word_obj.synsets) > 0:
        random_synset = random.choice(word_obj.synsets)
        random_lemma = random.choice(random_synset.lemma_names)
        output.append(random_lemma.replace('_', ' '))
    else:
        output.append(word_str)
    print " ".join(output)

from textblob import TextBlob
filename ="hek.txt"
with io.open(filename, "r", encoding="utf-8") as my_file:
    
    sys.stdin =  my_file.read() 
blob = TextBlob(txt)
print(blob.noun_phrases)

import nltk
with io.open("ToUse.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 
    
tokens = nltk.word_tokenize(essays)
tagged = nltk.pos_tag(tokens)
nouns = [word for word,pos in tagged \
	if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
downcased = [x.lower() for x in nouns]
joined = " ".join(downcased).encode('utf-8')
into_string = str(nouns)

output = open("output.txt", "w")
output.write(joined)
output.close()

import nltk
import Bt
import io
with io.open("ToUse.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 
    print essays

import nltk
import Bt
import io
with io.open("ToUse.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 
    #essays = u"""text here"""
    #f = open("ToUse.txt")
    #essays = f.read()
    #essays = Bt.badtext(essays)
    #essays = str(essays)
    #essays = essays.encode('utf-8')

    tokens = nltk.word_tokenize(essays)
    tagged = nltk.pos_tag(tokens)
    nouns = [word for word,pos in tagged \
    if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
    downcased = [x.lower() for x in nouns]
    joined = " ".join(downcased).encode('utf-8')
    into_string = str(nouns)
    texout = into_string.replace("', u'", "  ")
    texout = texout.replace("\u2018", "")
    texout = texout.replace("\u2019 ", "")
    texout = texout.replace("%", "")
    texout = texout.replace("[u'", "")
    texout = texout.replace("']", "")
    output = open("output2.txt", "w")
    output.write(texout)
    output.close()    
    print texout

import nltk
import Bt
#essays = u"""text here"""
f = open("ToUse.txt")
essays = f.read()
essays = Bt.badtext(essays)
essays = str(essays)
#essays = essays.encode('utf-8')

tokens = nltk.word_tokenize(essays)
tagged = nltk.pos_tag(tokens)
nouns = [word for word,pos in tagged \
if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
downcased = [x.lower() for x in nouns]
joined = " ".join(downcased).encode('utf-8')
into_string = str(nouns)
output = open("output2.txt", "w")
output.write(joined)
output.close()

# %load output2.txt
space  lines  front  height  rule  forces  memory  people  graciousness  table  people  number 
Long  masses  dust  soldiers  ground  beforehand  fatigue  weight  task  life  apparatus  night  
thinking  opposite  Freud  sum  energy  consciousness  idea  expression  punishments  others  
households  enemy  onslaught  defeat  Men  enemy  relation  water  waters  pass  distance  enemy  
thousand  exhaustion  way_  conduct  war  advantage  conduct  effort  difficulty  night  betoken  
alarm  computer  index  files  day  repositories  update  index  week-ends  Tales  class  Florida  
computer  index  files  permission  error  file  permissions  computer  index  files  perception  
system  spot  working  connection_  _approximation  time  moment  ignition  analysis  United  States  
mother  tomb  general  Speech  psychology  war  stratagem  plans  regard  occasion  hearts  men  
upon  troops  plans  day  victory  country  information  accomplishment  country  service  rights  
ground  issue  diagram  surface  description  part  light  light  rivers  earth  heat  wall  look  
drawings  facsimile  Hence  spot  forehead..  cast  shadow  pyramid  chin  eyes  Alps  France  
Italy  THE  IMAGES  IN  THE  PUPIL  THE  RAYS  WHETHER  SHADED  OR  LUMINOUS  HAVE  GREATER  STRENGTH  
AND  EFFECT  AT  THEIR  SIDES  size  object  bodies  space  image  weeks  WHAT  PORTION  A  WALL  
SURFACE  LEAST  LUMINOUS  WHICH  IS  SEEN  UNDER  THE  LEAST  AMOUNT  OF  LIGHT  distance  shadow  
Which  air  Compound  shadows  bodyis  view  light  shadow  side  side  edges  base  form  colour  
intersection  rest  sea  planes  object  make  blue  practice  middle  movements  size  head  Shadow  
partakes  window  angle  author  refers  morning  light  Scuba  Diving  Lessons  computer  index  
repository  box  apostrophes  place  database  project  Saltman  database  Google  Drive  voice  
auto-space  period  voice  files  files  box  apostrophes  place  weeks  function  file  configure  
image  database  share  permission  error  file  permissions  upgrades  Characters  UN-SALTMAN  
location  things  people  Philippines  party  drunk  friend  mine  bit  challenge  database  Google  
Drive  voice  auto-space  period  voice  terminal  Tales  commands  tar  configure  file  enter  
program  Online  Repository  Resources  drinks  postings  readers  Air  Horns  set  air  horns  
world  Dude  decision  bond  Windows  Linux  tube  spark  plug  county  death  abandonment  Windows  XP  
home  jet  engine  igniter  home  paper  bit  Mac  Computers  gas  friend  motorcycles  van  spark  
plug  garage  fire  jet  engine  igniter  home  power  failure  reinstall  exhibits  core  DOS  Dude  
time  home  jet  engine  county  death  abandonment  Windows  XP  Air  Horns  set  air  horns  world  
Dude  garage  fire  gas  spark  plug  garage  examining  modifying  Windows  project  gas  country  
engine  school  flame  flames  spark  plug  OPP  Almost  pieces  paper  spark  plug  country  dance  
halls  mind  thought  exhibits  home  jet  engine  buzzer  electricity  command  line  lot  people  
hardware  upgrade  Philippines  Microsoft  Linux  Philippines  Microsoft  interest  Ubuntu  Linux  
picture  igniter  spark  plug  filters  records  event  wire  Handlers  table  message  handler  
logger  attributes  methods  logger  name  hierarchy  root  logger  delegation  record  resources  
handler  Filters  wire  dictionary  keys  record  message  INFO  logger  thread  lock  level  handler  
LogRecord  filter  method  message  Filename  portion  message  logger  Logging  messages  point  
Python  package  namespace  handler   filters  root  filter  record  multiple  times  name  filters  
turn  Formatter  class  value  record  Logger  object  t  dictionary  logger  example  keys  logger  
ERROR  logger  glance  heart  passion  paper  growl  London  round  closet  item  thing  passions  
Hyde  house  bondage  energy  life  Bernie  patience  henceforth  life  effort  virtue  control  
offices  life  Six  hours  side  longing  advice  Peewee  power  Others  others  chimney  shelf  
memory  sight  companion.a  seconds  way  Malcom  door  Sawbones  door  consequence  face  past  
time  means  lives  men  Think  sight  start  horror  Ah  sir  blood  feature  marks  negligence  
doctor  house  Soho  sake  sake  months  murder  Think  earnest  clothes  character  faculties  watery  
green  instance  message  line  number  function  name  attributes  Handlers  none  value  message  
level  WARNING  none  reference  constructor  term    delegation  parent  logger  level  level  Returns  
instance  ancestor  loggers  root  logger  EnabledFor  lvl  logging  way  links  right  LogRecord  
number  attributes  msg    args  t  formatter  none  reference  logger  Formatter  name  logger  level  
time  call  value  record  LogRecord  t  care  exception  information  None  exception  None  use  
record  msg  argument  event  doesn   t  use  value  formatter  messages  msg    args  exception  
information  value  integer  value  record  Time  milliseconds  LogRecord  version  nothing  GMT  
converter  attribute  output  message  attribute  record  message  msg    message  handler  Millisecond  
portion  pathname  Handlers  table  LogRecord  instances  module  message  Logger  object  message  msg    
message  errors  information  time  exception  hierarchy  record  msg  argument  event  filters  dictionary 
keys  LogRecord  number  attributes  msg    args  value  record  value  handler  Messages  root  moon  
secrets  Mr  Guest  good  face  neighbourhood  natures  doctor  appearance  folks  street  street  
judges  wine  Mr.  Utterson  sincere  warm  woman  Mr.  Hyde  enemy  spirit  friend  quarters  court 
windows  iron  spirit  temper  post  bed  gallows  wood  wood  Enough  morning  locksmith  despair  
scud  laboratory  soul  brightness  hope  maid  servant  moment  rat  pressure  spirits  Sunday  walks  
middle  night  embers  inspector  glances  panels  look  time  acuteness  court  steps  splutter  drug  
quarter  London  Presently  eye  building  bell  knocker  windows  laboratory  relief  sorrow  suffering 
How  load  respectability  cabinet  hatred  Hyde  patent  dryness  colour  Bernie  answer  bowels  mercy  
face  seeing  face  Edward  Hyde  hatred  Hyde  Peewee  student  critic  handwriting  step  moment  wine 
point  appetite  associates  pulse  woman  Mr.  Hyde  order  resentment  Edward  Hyde  mind  terror  
sounds  wine  Mr.  Utterson  sincere  affection  way  Mr  Rogers  night  manner  man  contents  
prison-house  moments  eyes  postmark  rule  Dr.  Peewee  months  bagpipe  letter  ferocity  accent  
lips  friends  life

!ls

import Txmanip
help(Txmanip)

import Txmanip
from Txmanip import NoNumRange
NoNumRange.nonumRange("ToUse.txt",1,20)

from pass_phrase import pass_phrase
adjectives = pass_phrase.generate_wordlist("pass_phrase/adjectives.txt")
nouns = pass_phrase.generate_wordlist("pass_phrase/nouns.txt")
verbs = pass_phrase.generate_wordlist("pass_phrase/verbs.txt")
pass_phrase.passphrase(adjectives, nouns, verbs, " ")

import markovify
f = open("hashtag.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
for i in range(28):
    print(text_model.make_short_sentence(140))
    virtual =(text_model.make_short_sentence(140))
    virtual = virtual.replace("...",".")
    virtual = virtual.replace("..",".")
    virtual = virtual.replace(".",".\n")
    with open("virtual.txt", "a") as nf:
        nf.write(virtual)    

import markovify
f = open("ToUse.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
for i in range(18):
    print(text_model.make_short_sentence(140))
    virtual =(text_model.make_short_sentence(140))
    with open("virtual.txt", "w") as nf:
        nf.write(virtual)    

import markovify
f = open("codetalk.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
for i in range(18):
    print(text_model.make_short_sentence(140))
    virtual =(text_model.make_short_sentence(140))
    with open("virtual.txt", "a") as nf:
        nf.write(virtual)

import markovify
# Get raw text as string
with open("/home/jack/Desktop/imagebot/corpus_2.txt") as f:
    text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print three randomly-generated sentences of no more than 140 characters

for i in range(8):
    print(text_model.make_short_sentence(140))
    virtual =(text_model.make_short_sentence(140))
    with open("virtual.txt", "a") as nf:
        nf.write(virtual)

#badtext = ''.join(c for c in map(chr, range(256)) if not c.isalnum())

import re
import textwrap

with open("/home/jack/Desktop/imagebot/hurricane_14.txt") as f:
    text = f.read()
    #This was added to get ride od the unicode u from showing up
    words = text.replace(' u ', ' ');words = words.replace('u ', '');words = words.replace(' U ', ' ')
    #This clears out the non-Alpha-numeric characters
    #badtext = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
    badtext = '!,",#,$,%,&,(,),*,+,,-,.,/,:;<=>?@[\]^_`{|}~'
    
    # limit the aount of characters perline displayed
    chars_per_line = 80
    for i in range(0, len(word), chars_per_line):
        word = words.translate(None, badtext)
        print (words[i:i+chars_per_line]).encode('utf-8')

import markovify
# Get raw text as string
with open("/home/jack/Desktop/pycode/vpython2/TrigonometryBot/corpus_1.txt") as f:
    text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print three randomly-generated sentences of no more than 140 characters

for i in range(8):
    print(text_model.make_short_sentence(140))
    virtual =(text_model.make_short_sentence(140))
    with open("virtual.txt", "a") as nf:
        nf.write(virtual)

my_str = 'qwertyuiopaqCREATETABLEhurricanehurricanetextkeywordstex'
','.join(my_str[i:i+4] for i in range(0, len(my_str), 4))


import sqlite3
conn = sqlite3.connect('hurricane.db')
c = conn.cursor()
#Create table
c.execute('''CREATE TABLE hurricane
             (hurricane text, keywords text)''')
conn.commit()
conn.close()  

import re
import textwrap
import sqlite3
conn = sqlite3.connect('data/fts3hurricane.db')
#c = conn.cursor()
# Create table
#c.execute('''CREATE TABLE hurricane
#             (hurricane text)''')
# Insert a row of data
#c.execute("INSERT INTO hurricane VALUES ('hurricane','first test line')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.


with open("hurricane_14.txt") as f:
    text = f.read()
    #This was added to get ride od the unicode u from showing up
    words = text.replace(' u ', ' ');words = words.replace('u ', '');words = words.replace(' U ', ' ')
    #This clears out the non-Alpha-numeric characters
    badtext = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
   
    # limit the aount of characters perline displayed
    chars_per_line = 180
    for i in range(0, len(words), chars_per_line):
        
        #data= "hurricane_14.txt,",words[i:i+chars_per_line],","
        word = words.translate(None, badtext)
        data = [("hurricane_14.txt","),(",word[i:i+chars_per_line]),],
        data = str(data)
        words = data.replace("', '),(', '", '),(')
        #data = data[1:-2]
        conn = sqlite3.connect('data/fts3hurricane.db')
        c = conn.cursor()
        c.executemany("INSERT INTO hurricane VALUES (?)", words)
        conn.commit()
        conn.close()        

import sqlite3
conn = sqlite3.connect('hurricane.db')
c = conn.cursor()
# Never do this -- insecure!
#keywords = 'hurricaneirma'
#c.execute("SELECT * FROM hurricane WHERE keywords = '%s'" % keywords)

# Do this instead
t = ('hurricaneirma',)
c.execute('SELECT * FROM hurricane WHERE keywords=?', t)
print(c.fetchone())


import sqlite3
import sys
conn = sqlite3.connect('hurricane.db')
c = conn.cursor()# Never 
count=0
req=4
for row in c.execute('SELECT * FROM hurricane'):
    count=count+1
    print(row),"\n-----\n"
    if count > req:
        conn.close()
        sys.exit()
        

import re
import textwrap
import time
import sqlite3
import sys
import base64
import time
#conn = sqlite3.connect('hurricane.db')
#c = conn.cursor()
# Create table
#c.execute('''CREATE TABLE hurricane
#             (hurricane text, keywords text)''')
count=0
with open("hurricane_14.txt") as f:
    text = f.read()
    words = " ".join(re.findall("[a-zA-Z]+", text))
    words = words.replace(' u ', ' ');words = words.replace('u ', '');words = words.replace(' U ', ' ')
    chars_per_line = 140
    for i in range(0, len(words), chars_per_line):
        file= ("[(",words[i:i+chars_per_line],"),]")
        #data= ("[('"+words[i:i+chars_per_line]+"'),]")
        file = str(file)
        #file = 'base64 encoding allows code to be stored and retieved in the same format it was posted'
        b = 'hurricane, hurricaneirma, florida'
        conn = sqlite3.connect('hurricane.db')
        c = conn.cursor()
        time.sleep(1)
        #encodedlistvalue=base64.b64encode(file[2:-2])
        #c.execute("INSERT INTO hurricane VALUES (?,?)", (encodedlistvalue, b)) 
        c.execute("INSERT INTO hurricane VALUES (?,?)", (file, b)) 
        conn.commit()
        conn.close()        
        
        
        time.sleep(1)
        print file[2:-2]
        count=count+1
        print count
        if count>400:

            sys.exit()
            

import re
import textwrap
import time
import sqlite3
import sys
import base64
'''

conn = sqlite3.connect('data/400.db')
c = conn.cursor()
c.execute(''CREATE TABLE hurricane
             (hurricane text, keywords text)'')
             '''
count=0             
with open("hurricane_14.txt") as f:
    text = f.read()
    words = " ".join(re.findall("[a-zA-Z]+", text))
    words = words.replace(' u ', ' ');words = words.replace('u ', '');words = words.replace(' U ', ' ')
    #twitter friendly "under 140" for status
    chars_per_line = 400
    for i in range(0, len(words), chars_per_line):
        
        file= ("[(",words[i:i+chars_per_line],"),]")
        #data= ("[('"+words[i:i+chars_per_line]+"'),]")
        file = str(file)
        time.sleep(1)
        #file = 'base64 encoding allows code to be stored and retieved in the same format it was posted'
        conn = sqlite3.connect('data/400.db')
        c = conn.cursor()
        b = 'florida, hurricane, Irma, base64'
        encodedlistvalue=base64.b64encode(file[2:-2])
        c.execute("INSERT INTO hurr VALUES (?,?)", (encodedlistvalue, b))
        time.sleep(1)
        conn.commit()
        conn.close() 
        #Apply a pause so viewing line perline insert is possible
        time.sleep(1)
        count=count+1
        print file[2:-2],count
        

sys.exit()
     

conn = sqlite3.connect('hurricane14.db')
c = conn.cursor()# Never 

t = ('hurricane',)
for row in c.execute('SELECT * FROM hurricane'):
                
        s2 = row[0].encode('ascii')
        encodedlistvalue=base64.b64decode(s2)
        print encodedlistvalue, '\n', 'hurricane:', row[1], '\n -----------------------------\n'


import re
import textwrap
import clean

with open("/home/jack/Desktop/imagebot/hurricane_14.txt") as f:
    text = f.read()
    words = " ".join(re.findall("[a-zA-Z]+", text))
    words = words.replace(' u ', ' ');words = words.replace('u ', '');words = words.replace(' U ', ' ')
    print(textwrap.fill(words, 115))

%reset -f

import re
import textwrap
from datetime import datetime
import string
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords
def get_text_cleaned(tweet):
    tweet = tweet.replace("u'", "");tweet = tweet.replace(" id ", "\n id")
    return tweet

def get_text_sanitized(tweet):    
    return ' '.join([w.lower().strip().rstrip(string.punctuation)\
        .lstrip(string.punctuation).strip()\
        for w in get_text_cleaned(tweet).split()\
        if w.strip().rstrip(string.punctuation).strip()])

with open("/home/jack/Desktop/imagebot/hurricane_14.txt") as f:
    tweet = f.read()
    
    
    
    
    words =get_text_sanitized(tweet)
    print(textwrap.fill(words, 115)).encode('utf-8')

import time
with open('ToUse.txt') as f:
    while True:
        c = f.read(1)
        if c == 'a' or 'b' or 'c' or 'd' or 'f' or 'g' or 'g' or 'i' or 'j':
            c = c
            print c,
            #time.sleep(1)
        else:
            c="XX"
            print c,
            print "End of file"
            break
            

!ls *.txt

%%writefile clean.py
from datetime import datetime

import string

from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords

#Gets the tweet time.
def get_time(tweet):
    return datetime.strptime(tweet['created_at'], "%a %b %d %H:%M:%S +0000 %Y")

#Gets all hashtags.
def get_hashtags(tweet):
    return [tag['text'] for tag in tweet['entities']['hashtags']]

#Gets the screen names of any user mentions.
def get_user_mentions(tweet):
    return [m['screen_name'] for m in tweet['entities']['user_mentions']]

#Gets the text, sans links, hashtags, mentions, media, and symbols.
def get_text_cleaned(tweet):
    text = tweet['text']
    
    slices = []
    #Strip out the urls.
    if 'urls' in tweet['entities']:
        for url in tweet['entities']['urls']:
            slices += [{'start': url['indices'][0], 'stop': url['indices'][1]}]
    
    #Strip out the hashtags.
    if 'hashtags' in tweet['entities']:
        for tag in tweet['entities']['hashtags']:
            slices += [{'start': tag['indices'][0], 'stop': tag['indices'][1]}]
    
    #Strip out the user mentions.
    if 'user_mentions' in tweet['entities']:
        for men in tweet['entities']['user_mentions']:
            slices += [{'start': men['indices'][0], 'stop': men['indices'][1]}]
    
    #Strip out the media.
    if 'media' in tweet['entities']:
        for med in tweet['entities']['media']:
            slices += [{'start': med['indices'][0], 'stop': med['indices'][1]}]
    
    #Strip out the symbols.
    if 'symbols' in tweet['entities']:
        for sym in tweet['entities']['symbols']:
            slices += [{'start': sym['indices'][0], 'stop': sym['indices'][1]}]
    
    # Sort the slices from highest start to lowest.
    slices = sorted(slices, key=lambda x: -x['start'])
    
    #No offsets, since we're sorted from highest to lowest.
    for s in slices:
        text = text[:s['start']] + text[s['stop']:]
        
    return text

#Sanitizes the text by removing front and end punctuation, 
#making words lower case, and removing any empty strings.
def get_text_sanitized(tweet):    
    return ' '.join([w.lower().strip().rstrip(string.punctuation)\
        .lstrip(string.punctuation).strip()\
        for w in get_text_cleaned(tweet).split()\
        if w.strip().rstrip(string.punctuation).strip()])

#Gets the text, clean it, make it lower case, stem the words, and split
#into a vector. Also, remove stop words.
def get_text_normalized(tweet):
    #Sanitize the text first.
    text = get_text_sanitized(tweet).split()
    
    #Remove the stop words.
    text = [t for t in text if t not in stopwords.words('english')]
    
    #Create the stemmer.
    stemmer = LancasterStemmer()
    
    #Stem the words.
    return [stemmer.stem(t) for t in text]

def pil_image():
    ''' A View that Returns a PNG Image generated using PIL'''

    from PIL import Image, ImageDraw 

    size = (640,640)             # size of the image to create
    im = Image.new('RGB', size) # create the image
    draw = ImageDraw.Draw(im)   # create a drawing object that is
                                # used to draw on the new image
    red = (255,0,0)    # color of our text
    text_pos = (10,10) # top-left position of our text
    text = "Hello World!" # text to draw
    # Now, we'll do the drawing: 
    draw.text(text_pos, text, fill=red)
    
    del draw # I'm done drawing so I don't need this anymore
    
    # We need an HttpResponse object with the correct mimetype
    #response = HttpResponse(mimetype="image/png")
    # now, we tell the image to save as a PNG to the 
    # provided file-like object
    im.save("test.png", 'PNG')

    return im # and we're done!

pil_image()

%%writefile ToUse.txt
If will create the same space of about three lines plus one in front of the height, the general rule is satidfied.
He manages his forces as though they were only a memory.
Some people are exceeding graciousness and familiar with the table. Those people are fewer in number.
Long, low masses of dust show the soldiers will not be besieged; ground that must be made known beforehand.
It was thus her wish to sleep. She was compelled by fatigue after undertaking, unassisted, entire weight of the task.
Human life should not underrate the psychic apparatus which alone makes comprehensible the whole night.
All thinking is only the opposite of conscious. Although we cannot identify what it is.
Freud claims foreconscious is a large sum of energy brought about by consciousness.
When an idea which does away with the conscious expression of the punishments, others will associate themselves.
She loved only those who were distinguished in her households.
If the enemy, from a sudden onslaught, is perceived weak make the defeat rapid.
Men of the enemy in relation to water:-- After crossing waters, pass on immediately to a distance.
Now, of the enemy, we may go a thousand leagues without exhaustion.
The way_ or the proper conduct of war will not reap advantage. Do not let proper conduct weaken the effort.
Their difficulty lies in the night betoken alarm.
The computer will download an index of the files within one day.
Non-sanctioned repositories must be made executable.
It automatically backs itself up and ready to go.
It takes the sudo apt-get update udates the index of the the week-ends.
Welcome to The Tales of the first class came I was in Florida.
The computer will download an index of files, it does not install them.
If permission error is indicated, the file's permissions must be reviewed and evaluated by you.
The computer will download an index of files, it does not install them.
Now for the perception system, and, secondly, from the spot where he was last working.
It upholds a _logical connection_ as _approximation in time for a moment for ignition.
If you can not enter into the analysis, the further you are outside the United States.
I will now point out that my mother was dying; the tomb agrees with this.
Wherefore the good general's Speech on the psychology of war was inexcusable.
Vary the stratagem according to my plans, or you will be lost.
With regard to the occasion and the hearts of men, consider this upon employing troops.
Therefore they must not be attacked, they must be divided.
All  of our plans depend on accomplishing a single day's victory.
They who are sitting may be present, the country as give information.
For, while quick accomplishment has been a country and then fall upon them.
If deeply involved in the service of their rights. This is called deeply-involved ground.
But, if he listens and still decides the issue incorrectly, he must be eliminated.
The diagram given a under no after the surface of every description.
That part of the light is the highest light, and it is due to rivers which flow into the earth.
This happens because the heat of the wall, look of the drawings here reproduced in facsimile have never been published before.
Hence we may look at a spot corresponding to the forehead..
The cast shadow will resemble a pyramid the same as the chin to the eyes. 
If we hope to get out of the Alps which divide France from Italy.
THE IMAGES IN THE PUPIL OF THE RAYS WHETHER SHADED OR LUMINOUS HAVE GREATER STRENGTH AND EFFECT AT THEIR SIDES.
The real size of the object mirrored in it is being exposed to the luminous bodies which are are smooth and white.
Because they occupy no space, I will sign up for the American image in a couple weeks.
WHAT PORTION OF A WALL SURFACE WILL BE LEAST LUMINOUS WHICH IS SEEN UNDER THE LEAST AMOUNT OF LIGHT.
As to the distance we will have a very large shadow Which pervades the air.
Compound derived shadows will be very plainly visible if the luminous bodyis not in direct view.
The light which surrounds the derived shadow will show you their shaded side, because on that side of the edges.
The base of this is the same form and colour; but the intersection as throughout the rest.
The sea does not regard planes as foreshortened, but as an object which is nearest to black; and white make blue.
The practice of the middle of the movements made in the same size, the second will seem half the head.
Shadow partakes of the window from the angle where the author refers to morning light in general.
Scuba Diving Lessons I was charged up and ready to go.
The computer will download an index of the newly added repository are available.
Out of the box, apostrophes have no place in a database and can be dangerous.
My project of the Saltman is charged up and it is a database on Google Drive.
As I said I use voice to make an auto-space after a period when using voice.
Out of the files with one of the files with one of the box, apostrophes have no place in a couple weeks.
Experimenting with a function to permit the file called configure.
I signed up for the American image in a database. I also wish to say and share.
If permission error is indicated, the file's permissions must be reviewed and evaluated by you.
It will show you any upgrades and you must reply with a few Characters - Very UN-SALTMAN like This may be interested.
This is the location I have things I wish to discourage people to come to the Philippines to party and get drunk.
It automatically backs itself up and ready to go. A friend of mine was a bit of a challenge.
I was charged up and it's database on Google Drive. As I said I use voice to make an auto-space after a period.
When using voice, I am in the terminal. Welcome to The Tales of the commands If it is a tar.
Find the configure file and enter. I program and it also is being recorded.
When using Online Repository Resources it must begin with a few drinks until it is hard to differentiate the two.
Some postings will be fun for readers to try out. It automatically backs itself up and ready to go.
Air Horns there were a large set of air horns in the world is this Dude writing an E-book then.
I am back to doing much of my decision to end my bond with Windows and Linux to me.
We were cruising down the tube to the the spark plug.
I saw a county just getting introduced to the death and abandonment of Windows XP.
It was a home made jet engine using an an igniter I built at home.
I was in the paper because I also fooled a bit with Mac Computers.
I was afraid to cut the gas can away and run.
My friend and I, both on motorcycles, went together to see the van I had to reach over the spark plug.
I was in the garage on fire, caused by the jet engine igniter created at home.
Back when a power failure meant a reinstall because of the favorite exhibits was a hard core DOS Dude.
At the time it was a home made jet engine.
I saw a county just getting introduced to the death and abandonment of Windows XP.
Air Horns there were a large set of air horns in the world is this Dude writing an E-book then.
I am retired and live in the garage on fire. I was afraid to cut the gas over the spark plug.
I had found in the garage examining, modifying, tuning it up.
It was a Windows project followed up by using a gas can.
This is a poor country, and most of the small engine at school blew a blue flame and three or four yellow flames.
I had to reach over the spark plug. OPP ! Almost all the pieces together.
Now what OMG ! I was in the paper. Then reached over the spark plug.
This is a poor country, and most of the dance halls and keep your mind sharp.
Now what OMG ! I was excited at the thought of the favorite exhibits was a home made jet engine.
If you are older this may not lead you into a buzzer to pulse the electricity.
Working from a command line freaks a lot of people out.
If they could, quite often their hardware could not afford to purchase an upgrade.
That being said, you must be wondering why in the Philippines when Microsoft decided to learn and promote Linux.
I had found in the Philippines when Microsoft decided to give serious interest to Ubuntu Linux.
I took the picture on the igniter, I could hear the spark plug.
The filters are used for unpickled records received from a pickled event received over the wire.
Handlers have the following table. If these are missing, the message for this handler fails.
 to a logger which is highest in the following attributes and methods.
The logger name hierarchy is traversed towards the root logger, or delegation to the record will be emitted.
Tidy up any resources used by the handler will not be threadsafe.
Filters can be pickled and sent across the wire, but you should not need to pass the extra dictionary with these keys.
Do formatting for a record - if a message with level INFO on this logger.
Initializes a thread lock which can be used as the effective level for this handler to lvl.
The LogRecord has a filter method with the message.
Filename portion of a message, was a non-root logger.
Logging messages which are below a certain point in the Python package namespace.
Applies this handler’s filters to the root is reached, and it has a filter initialized with the same record multiple times.
If name is lost the filters are consulted in turn by Formatter class. 
Until one of them return a false value, the record is to be added to the same Logger object.
You shouldn’t need to pass a dictionary which is a non-root logger.
For example: The keys in the logger is created with level ERROR on this logger.
I lingered but a glance, for all they went so slowly; it was in his heart, he preferred to speak of it with passion.
Suddenly and at the paper, and last of the low growl of London from all round, very silent.
Each closet held an item needed, but not thing of vital to existance.
I was once again raging and freezing with the passions of Hyde.
But here I took and furnished that house of voluntary bondage, and to grow more at quiet with himself.
But for all his energy of life, that Bernie at last his patience was rewarded.
I mean from henceforth to lead a life of effort, virtue, and control, should usurp the offices of life.
Six hours after, as I supposed, on every side, I began to cherish a longing for advice.
Peewee was no more myself when I know how he fears my power to shake me.
Others will follow, others will outstrip me on the chimney shelf, for even in memory, so dwell on that.
At sight of him back, conscious at his companion.a few seconds.
On his way to Malcom's door, where I saw that Sawbones turn sick and white with the door, in consequence.
And he covered his face was white and his own past, groping in all the time.
We were by no means in the lives of down-going men.
Think of me at first sight, without a start of horror.
Ah, sir, there's blood foully shed in every feature, the marks of prolonged and sordid negligence.
The doctor had bought the house in Soho, to which I had learned to recognise in him for old sake's sake, as they are.
Some two months before the murder had been prevented.
Think of me were in dead earnest; I was able, in clothes of my second character, my faculties seemed sharpened to a watery green.
The instance is initialized with the message. The line number and function name was added.
These attributes can be used with particular Handlers.
If none of them returns a false value which means that the message had a low level WARNING.
If none of them return a reference to the constructor.
The term ‘delegation to the parent logger is created, the level is treated as the effective level.
Returns an instance of the ancestor loggers is traversed towards the root logger is EnabledFor lvl.
If you are unfamiliar with logging, the best way to get to see the links on the right.
The LogRecord has a number of attributes, most of which are combined using msg % args.
You don’t actually need to format this yourself. That indicates if a formatter is set, use it.
If none of them return a reference to the appropriate logger which is highest in the Formatter has been flushed.
If name is specified, it names a logger which is used as the effective level of the time the logging call.
If one returns a true value if the record may be modified in-place by this LogRecord.
You don’t actually need to exercise some care.
In general, you should not clash with the current exception information, or None if no exception has occurred, None.
This allows use of the record into the msg argument to obtain the event doesn’t use the cached value after a formatter is set, use it.
Logging messages which are combined using msg % args.
This is useful because the exception information to be specified.
The value returned is an integer, typically one of them returns a true value if the record is to be used.
Time in milliseconds when the LogRecord being processed.
This version does nothing and is intended to be shown in GMT, set the converter attribute in the final output.
The message attribute of the record will be ignored.
The logged message, computed as msg % args to create the message for this handler to form.
Millisecond portion of pathname. Handlers have the following table.
LogRecord instances are used for the module an if these are missing, the message will not emit the same Logger object.
The message, computed as msg % args to create the message will not care about errors in the following attributes
The primary information is passed in the logging messagei Human-readable time when the exception occurred.
Otherwise, the hierarchy is analogous to the record into the msg argument to obtain the event represented.
The filters are used to pass the extra dictionary with these keys.
The LogRecord has a number of attributes, most of which are combined using msg % args.
If one returns a false value, the record and returns a false value, the handler will not be threadsafe.
Messages are passed directly to the root is reached.
I had now seen the full moon. But he kept fewer secrets than Mr. Guest; and he had grown very silent.
He did no good; his face as he spoke, harsh and broken.
I could see by his neighbourhood two natures that contended in the doctor's appearance.
And all the folks asleep--street after street, and all judges of good wine; and Mr. Utterson a sincere and warm.
The ivory-faced and silvery-haired old woman remained otherwise empty.
Mr. Hyde at such an enemy to rest! Instantly the spirit of enduring hatred.
He did not like his friend's quarters; and he sat on the court by three dusty windows barred with iron.
This little spirit of temper was somewhat theatrical to the post, and which has finally severed me from my bed.
I rushed to the gallows, but the wood was tough and heavy wood.
Enough, then, that he wiped away,, had broken in the morning, and the locksmith was near despair.
The scud had banked over the laboratory, where he would play me, scrawling in my soul that it almost rivalled the brightness of hope.
A maid servant living alone in a moment, like a rat, and run from me?I knew myself, at the high pressure of spirits.
 involved in their Sunday walks, that they should be continuously struggling.
Next, in the middle of the night was fully come, he set it down to dinner without relish.
From these embers the inspector exchanged glances.
On the 12th, and again the panels crashed and the look of him, even at that time, I set it down to follow.
I knew myself, at the acuteness of the court.
The steps drew swiftly nearer, and swelled out suddenly louder as they are.
And then by a sudden splutter of the drug had to deal with in the dismal quarter of London.
Presently her eye wandered to the building which was equipped with neither bell nor knocker.
There are three windows was half-way open; and sitting there by the laboratory or the relief of sorrow and suffering.
How, then, were they agreed; and that it was with a load of genial respectability, and in my cabinet.
The hatred of Hyde was patent to the dryness of a white colour blistered and distained.
Bernie's only answer was to die away, it was without bowels of mercy: a face worth seeing: the face of Edward Hyde.
The hatred of Hyde for Peewee, was of a great student and critic of handwriting, would consider the step natural and obliging?Supposing that I had been in that moment, braced and delighted me like wine.
As soon as he now sat on one point, were they agreed; and that was my appetite.
He was ashamed of his strange associates, of the pulse.
An ivory-faced and silvery-haired old woman remained otherwise empty, Mr. Hyde that racked me.
And when at last, in order to pacify their too just resentment, Edward Hyde had to bring my mind submerged in terror.
Small sounds carried far; domestic sounds out of good wine; and Mr. Utterson a sincere and warm affection.
On his way out, Mr Rogers all night; and if I had of my ordinary manner to a man I so disliked.
Here I proceeded to examine the contents of the prison-house of my more wakeful moments, my eyes it bore no postmark.
To this rule, Dr. Peewee had returned six months before, to serve as a bagpipe.
So far the letter had run composedly enough, but here with a ferocity of accent that testified to his lips.
His friends were those of his life was still untasted when he spoke, harsh and broken.


from backports import csv
import io
with io.open("my_utf8_file.txt", "r", encoding="utf-8") as my_file:
    for row in csv.reader(my_file):
        yield row

import Txmanip
help(Txmanip)

%%writefile RandLine.py
def random_line(filename):
    line_num = 0
    selected_line = ''
    with open(filename) as f:
        while 1:
            line = f.readline()
            if not line: break
            line_num += 1
            if random.uniform(0, line_num) < 1:
                selected_line = line
    return selected_line.strip()

#%%writefile RandLine.py
import random
def random_line(TXT):
    while open(TXT, "r") as afile:
    
    line = next(afile)
    for num, aline in enumerate(afile):
        if random.randrange(num + 2): continue
        line = aline.replace("\n", "")
    return line

TXT="ToUse.txt"
random_line(afile)


import random
import io
with io.open("ToUse.txt", "r", encoding="utf-8") as my_file:
    for row in rows(my_file):
        print row

savE = open('savE.txt', 'w')
savE.close()

https://inzaniak.github.io/pybistuffblog/posts/2017/04/26/python-markovify.html

# Build the second model.
ebook_b = clean_book('hekel.txt')
text_model_b = markovify.Text(ebook_b)
for i in range(5):
    print(text_model_b.make_sentence())

# Combine the models into a single one
both_models = markovify.combine([text_model_a,text_model_b])
for i in range(5):
    print(both_models.make_sentence())

def periodtonewline():
    with open('savE.txt') as infile, open('savE_sentence.txt', 'w') as outfile:
        for line in infile:
            line = line.replace(".",".\n");line = line.replace(" ‘","");
            line = line.replace("’","")
            outfile.write(line)  # non-empty
            
periodtonewline()            

import markovify
f = open("grimm.txt")
text = f.read()
text_model_a = markovify.Text(text)


ebook_b =open('hekel.txt')
text0 = ebook_b.read()
text_model_b = markovify.Text(text0)
for i in range(5):
    print(text_model_b.make_short_sentence(140))
    STR0 = (text_model_b.make_short_sentence(140))
    savE = open('savE.txt', 'a')
    savE.write(STR0)
    savE.close()

# 2. Print five randomly-generated sentences
for i in range(5):
    print(text_model_a.make_short_sentence(140))
    STR = (text_model_a.make_short_sentence(140))
    savE = open('savE.txt', 'a')
    savE.write(STR)
    savE.close()
# 3. Print three randomly-generated sentences of no more than 140 characters
for i in range(5):
    print(text_model_a.make_short_sentence(140))
    STR2 = (text_model_a.make_short_sentence(140))
    savE = open('savE.txt', 'a')
    savE.write(STR2)
    savE.close()
# Combine the models into a single one
both_models = markovify.combine([text_model_a,text_model_b])
for i in range(5):
    print(both_models.make_short_sentence(140))    
    STR3 = (both_models.make_short_sentence(140))  
    savE = open('savE.txt', 'a')
    savE.write(STR3)
    savE.close()    

import re
def periodpattern():
    with open('savE.txt') as infile:
        for line in infile:
            line = line.replace(" ‘","")
            line = line.replace("’","")
            line = line.replace(".",".\n")
            line = line.replace("!","!\n")
            line = line.replace("?","?\n")
            
            print line
            outfile2 = open('savE_patern.txt', 'w')
            outfile2.write(line)  # non-empty
            outfile2.close()
            
periodpattern()            





import markovify
f = open("savE.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
#http://paulbourke.net/fractals/
STR = (text_model.make_short_sentence(110))
print STR

import markovify
f = open("grimm.txt")
text = f.read()
text_model_a = markovify.Text(text)
# 2. Print five randomly-generated sentences
for i in range(5):
    print(text_model_a.make_sentence())
    STR = (text_model_a.make_sentence())
    savE = open('savE.txt', 'a')
    savE.write(STR)
    savE.close()
# 3. Print three randomly-generated sentences of no more than 140 characters
for i in range(3):
    print(text_model_a.make_short_sentence(120))
    STR2 = (text_model_a.make_short_sentence(120))
    savE = open('savE.txt', 'a')
    savE.write(STR2)
    savE.close()    

import markovify
f = open("grimm.txt")
text = f.read()# Recreate the model using 3 sentences
three_model = markovify.Text(text,state_size=3)
for i in range(5):
    print(three_model.make_short_sentence(140))
    STR = (three_model.make_short_sentence(140))
    savE = open('savE.txt', 'a')
    savE.write(STR)
    savE.close()
    print STR

import markovify
f = open("grimm.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
STR = (text_model.make_short_sentence(140))
savE = open('savE.txt', 'a')
savE.write(STR)
savE.close()
print STR

import markovify
f = open("ToUse.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
#http://paulbourke.net/fractals/
STR = (text_model.make_short_sentence(110))
print STR

def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]

infile = "ToUse.txt" 
generate_the_word(infile)

import Txmanip
from Txmanip import HeadFirst

%%writefile FileLen.py
def filelen(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

import FileLen
FileLen.filelen("ToUse.txt")

import FileLen
from random import randint
# maX is the number of lines in the file
maX = FileLen.filelen("ToUse.txt")
# pick a random number between 0 and maX as:  num
num = randint(0, maX)
with open('ToUse.txt') as f:
    for i, line in enumerate(f, 1):
        # if line = num break
        if i == num:
            break

#print the line           
print line

%%writefile RandomLine.py
def randomline(filename):
    from random import randint
    Max = FileLen.filelen(filename)
    num = randint(0, Max)
    with open(filename) as f:
        for i, STR in enumerate(f, 1):
            if i == num:
                break
    print STR
    


!rm RandomLine.pyc

import RandomLine
help(RandomLine)



import RandomLine

filename = "ToUse.txt"    
RandomLine.randomline(filename)    

from random import randint
Max = FileLen.filelen("ToUse.txt")
num = randint(0, Max)
with open('ToUse.txt') as f:
    for i, STR in enumerate(f, 1):
        if i == num:
            break
#STR = line
print STR

num = 3
with open('ToUse.txt') as f:
    for i, line in enumerate(f, 1):
        if i == num:
            break
print line

search = raw_input("find  ")
file = open("ToUse.txt")
lines = file.readlines()
for line in lines:
    if search in line:print line
    if search == True:
        file.close()
        exit()
file.close()



from Txmanip import HeadFirst
HeadFirst.headFirst("ToUse.txt")

f = open("ToUse.txt")
text = f.read()
print text

import random
afile = open("ToUse.txt","r")
line = next(afile)
for num, aline in enumerate(afile):
    if random.randrange(num + 2): continue
    line = aline.replace("\n", "")
print line

import random
def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
        if random.randrange(num + 2): continue
        line = aline.replace("\n", "")
    return line
afile = open("ToUse.txt", "r")
STR = random_line(afile)
print STR

import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

tx = (random_line('hashtag-nouns.txt'))
print tx


import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line('ToUse.txt'))


import RandomLine
texfile = "ToUse.txt"
rndl = RandomLine.randomline(texfile)

%%writefile RandomLine.py
def randomline(filename):
    import FileLen
    from random import randint
    Max = FileLen.filelen(filename)
    num = randint(0, Max)
    with open(filename) as f:
        for i, STR in enumerate(f, 1):
            if i == num:
                break
    print STR
    

!ls RandomLine.py

import RandomLine
filename="ToUse.txt"
RandomLine.randomline(filename) 

!python paletts.py instagram/640fish.jpg instagram/640cloud.jpg output.jpg

!showme junk/PalletteTemp2.png

import sqlite3
conn = sqlite3.connect('twitter.db')
c = conn.cursor()
c.execute("""
CREATE VIRTUAL TABLE hurr 
USING FTS3(text, keywords);
""")
conn.commit()
conn.close()

!ls *.txt

import re
import textwrap
import time
import sqlite3
import sys
import base64
import time
conn = sqlite3.connect('twittertext.db')
c = conn.cursor()
#Create table
#CREATE VIRTUAL TABLE hurr 
#USING FTS3(text, keywords)


c.execute('''CREATE VIRTUAL TABLE twitter
             USING FTS3 (twittertext)''')
count=0
lines = 400
with open("hashtag.txt") as f:
    text = f.read()
    words = " ".join(re.findall("[a-zA-Z]+", text))
    words = words.replace(' u ', ' ');words = words.replace('u ', '');words = words.replace(' U ', ' ')
    chars_per_line = 400
    for i in range(0, len(words), chars_per_line):
        file= ("[(",words[i:i+chars_per_line],"),]")
        #data= ("[('"+words[i:i+chars_per_line]+"'),]")
        file = str(file)
        #file = 'base64 encoding allows code to be stored and retieved in the same format it was posted'
        #keywords = 'sept, nonapi, china, philippines'
        conn = sqlite3.connect('twittertext.db')
        c = conn.cursor()
        time.sleep(1)
        #encodedlistvalue=base64.b64encode(file[2:-2])
        #c.execute("INSERT INTO hurricane VALUES (?,?)", (encodedlistvalue, b)) 
        c.execute("INSERT INTO twitter VALUES (?)", (file,)) 
        conn.commit()
        conn.close()        
        
        
        #time.sleep(1)
        print file[2:-2]
        count=count+1
        print count
        if count>lines:
            sys.exit()
#commits and closes database if there are less then 400 lines of text
conn.commit()
conn.close()                 

!rm twittertext.db

from flask import Flask, request
import sys
sys.path.insert(0, "/usr/local/lib/python2.7/dist-packages")
from flask_restful import Resource, Api
import sqlite3
import time

app = Flask(__name__)
api = Api(app)

conn = sqlite3.connect('twittertext.db')
c = conn.cursor()# Never 
count=1
param = raw_input("What Words are you looking for?")
num = input("How many to display?")

for row in c.execute('SELECT twittertext FROM twitter WHERE twittertext MATCH ?', (param,)):
    time.sleep(1)
    print count,":",(row),"\n-----\n"
    count=count+1
    if count >num:
        conn.close()
        sys.exit()
if __name__ == '__main__':
     app.run()
        

from flask import Flask, request
import sys
sys.path.insert(0, "/usr/local/lib/python2.7/dist-packages")
from flask_restful import Resource, Api
import sqlite3
import time

app = Flask(__name__)
api = Api(app)

conn = sqlite3.connect('twittertext.db')
c = conn.cursor()# Never 
count=1
t = ('blood',)
#param = "blood"
param = raw_input("What Words are you looking for?")
num = input("How many to display?")

for row in c.execute('SELECT rowid, twittertext FROM twitter WHERE twittertext MATCH ?', (param,)):
    time.sleep(1)
    print count,":",(row),"\n-----\n"
    count=count+1
    if count >num:
        conn.close()
        sys.exit()
if __name__ == '__main__':
     app.run()
        



!rm twittertext2.db

from flask import Flask, request
import sys
sys.path.insert(0, "/usr/local/lib/python2.7/dist-packages")
from flask_restful import Resource, Api
import sqlite3
import time

app = Flask(__name__)
api = Api(app)

conn = sqlite3.connect('twittertext.db')
c = conn.cursor()# Never 
count=1
t = ('blood',)
#param = "blood"
#param = raw_input("What Words are you looking for?")
num = input("How many to display?")

for row in c.execute('SELECT * FROM twitter'):
    time.sleep(1)
    print count,":",(row[0]),"\n-----\n"
    count=count+1
    if count >num:
        conn.close()
        sys.exit()
if __name__ == '__main__':
     app.run()
        

!ls *.jpg

import re
import textwrap
import time
import sqlite3
import sys
import base64
import time
conn = sqlite3.connect('twittertext2.db')
c = conn.cursor()

c.execute('''CREATE VIRTUAL TABLE twitter
             USING FTS3 (twittertext, base64)''')
count=0
lines = 400
with open("hashtag.txt") as f:
    text = f.read()
    words = " ".join(re.findall("[a-zA-Z]+", text))
    #wordx = " ".join(re.findall("[a-zA-Z]+", text))
    words = words.replace(' u ', ' ');words = words.replace('u ', '');words = words.replace(' U ', ' ')
    chars_per_line = 400
    for i in range(0, len(words), chars_per_line):
        file= ("[(",words[i:i+chars_per_line],"),]")
        #data= ("[('"+words[i:i+chars_per_line]+"'),]")
        file = str(file)
        #file = 'base64 encoding allows code to be stored and retieved in the same format it was posted'
        #keywords = 'sept, nonapi, china, philippines'
        conn = sqlite3.connect('twittertext2.db')
        c = conn.cursor()
        time.sleep(1)
        #encodedlistvalue=base64.b64encode(wordx[2:-2])
        encodedlistvalue=base64.b64encode(file)
        #c.execute("INSERT INTO hurricane VALUES (?,?)", (encodedlistvalue, b)) 
        c.execute("INSERT INTO twitter VALUES (?,?)", (file,encodedlistvalue)) 
        conn.commit()
        conn.close()        
        
        
        #time.sleep(1)
        print file[2:-2]
        count=count+1
        print count
        if count>lines:
            sys.exit()
#commits and closes database if there are less then 400 lines of text
conn.commit()
conn.close()                 

from bs4 import BeautifulSoup
import requests
import sqlite3
import base64
import time
import sqlite3
import sys
import base64
import time
#conn = sqlite3.connect('twittertext64.db')
#c = conn.cursor()
#c.execute('''CREATE VIRTUAL TABLE twitter
#             USING FTS3 (twittertext, base64)''')
#url = u'https://twitter.com/search?q='
HashTag = raw_input("HashTag  : ") or "CNN"
url = u'https://twitter.com/hashtag/'+ HashTag +'?lang=en'
#tweetfile = 'hashtag.txt'
#url = u'https://twitter.com/scavino45/lists/florida-hurricane-irma'
#url = u'https://twitter.com/Selebog55680943'
#url = u'https://twitter.com/WinMansfield'
#query = u'%40drawranliou'
#query = u'%23hurricanne&src=typd'
#query = u'python, florida'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

tweets = [p.text for p in soup.findAll('p', class_='tweet-text')]
txt = (tweets)
for listx in txt:
    #filein = open(tweetfile, 'a')
    list = listx.replace(u'\xa0', u' ')
    list = list.replace(u'\u2026','ignore')
    list = list.replace(u'\xa0','ignore')
    list = list.replace(u'\u2013', u' ')
    list = list.replace(u'\xf1', u' ')
    list = list.replace(u'\u2019','ignore')
    list = list.replace(u'\xa0',' ')
    list = '\n'+ u''.join((list)).encode('utf-8').strip()
    conn = sqlite3.connect('twittertext2.db')
    conn.text_factory = str
    c = conn.cursor()
    time.sleep(1)
    #encodedlistvalue=base64.b64encode(wordx[2:-2])
    #c.execute("INSERT INTO hurricane VALUES (?,?)", (encodedlistvalue, b)) 
    entr = "\nKeyWord : "+HashTag
    c.execute("INSERT INTO twitter VALUES (?,?)", (list,HashTag)) 
    conn.commit()
    conn.close()        
    print list,entr


from flask import Flask, request
import sys
sys.path.insert(0, "/usr/local/lib/python2.7/dist-packages")
from flask_restful import Resource, Api
import sqlite3
import time

app = Flask(__name__)
api = Api(app)

conn = sqlite3.connect('twittertext2.db')
c = conn.cursor()# Never 
count=1
t = ('blood',)
#param = "blood"
param = raw_input("What Words are you looking for?")
num = input("How many to display?")

for row in c.execute('SELECT * FROM twitter'):
    time.sleep(1)
    rowx =base64.b64decode(row[1])
    print count,":",(row[0]),"\n-----\n",(rowx),"\n-----\n"
    #row =base64.b64decode(row[1])
    count=count+1
    if count >num:
        conn.close()
        sys.exit()
if __name__ == '__main__':
     app.run()
        

import re
import textwrap
import time
import sqlite3
import sys
import base64
import time
conn = sqlite3.connect('twittertext2.db')
c = conn.cursor()
#Create table
#CREATE VIRTUAL TABLE hurr 
#USING FTS3(text, keywords)


c.execute('''CREATE VIRTUAL TABLE twitter
             USING FTS3 (twittertext, base64)''')
count=0
lines = 400
with open("hashtag.txt") as f:
    text = f.read()
    words = " ".join(re.findall("[a-zA-Z]+", text))
    #wordx = " ".join(re.findall("[a-zA-Z]+", text))
    words = words.replace(' u ', ' ');words = words.replace('u ', '');words = words.replace(' U ', ' ')
    chars_per_line = 400
    for i in range(0, len(words), chars_per_line):
        file= ("[(",words[i:i+chars_per_line],"),]")
        #data= ("[('"+words[i:i+chars_per_line]+"'),]")
        file = str(file)
        #file = 'base64 encoding allows code to be stored and retieved in the same format it was posted'
        #keywords = 'sept, nonapi, china, philippines'
        conn = sqlite3.connect('twittertext2.db')
        c = conn.cursor()
        time.sleep(1)
        #encodedlistvalue=base64.b64encode(wordx[2:-2])
        encodedlistvalue=base64.b64encode(file)
        #c.execute("INSERT INTO hurricane VALUES (?,?)", (encodedlistvalue, b)) 
        c.execute("INSERT INTO twitter VALUES (?,?)", (file,encodedlistvalue)) 
        conn.commit()
        conn.close()        
        
        
        #time.sleep(1)
        print file[2:-2]
        count=count+1
        print count
        if count>lines:
            sys.exit()
#commits and closes database if there are less then 400 lines of text
conn.commit()
conn.close()                 

from flask import Flask, request
import sys
sys.path.insert(0, "/usr/local/lib/python2.7/dist-packages")
from flask_restful import Resource, Api
import sqlite3
import time

app = Flask(__name__)
api = Api(app)
conn = sqlite3.connect('twittertext.db')
c = conn.cursor()
count=1
Start = input("Start Line")
num = input("Stop Line")
for row in c.execute('SELECT * FROM twitter'):
    time.sleep(1)
    if count >Start:
        row = str(row)[4:-4]
        row = row.replace("'[(', '"," ")
        row = row.replace("', '),]'"," ")
        row = row.replace('u"','')
        row = row.replace('",','')
        #print "\n",count,"-----\n",row
        print count,row
    count=count+1
    if count >num:
        conn.close()
        sys.exit()
if __name__ == '__main__':
     app.run()

import sys
sys.path.insert(0,"/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
import Key
from random import randint
import FileLen
Max = FileLen.filelen("ToUse.txt")
num = randint(0, Max)
with open('ToUse.txt') as f:
    for i, STR in enumerate(f, 1):
        if i == num:
            break

CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,ACCESS_SECRET)
#PATH = '/home/jack/Desktop/3DFRACT/Mandelbulb3Dv199/cloud.jpg'
#PATH = '/home/jack/Desktop/3DFRACT/Mandelbulb3Dv199/post-002.jpg'
#PATH = '/home/jack/Desktop/3DFRACT/Mandelbulb3Dv199/post-068.jpg'
#PATH = '/home/jack/Desktop/text_stuff/instagram/post-054.jpg'
PATH = '/home/jack/Desktop/text_stuff/instagram/post-056.jpg'
#PATH = '/home/jack/Desktop/text_stuff/junk/post-color3.png'

STR ="#C++imagery #python I enjoy pallet swapping most of all #imageprocessing"
photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])

!./searchBlend


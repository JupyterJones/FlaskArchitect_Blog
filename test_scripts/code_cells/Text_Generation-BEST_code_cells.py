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

RemoveBlank.removeblank("AllBooksOfEnoch_djvu.txt","BooksOfEnoch.txt")

from Txmanip import RemoveDuplicate

RemoveDuplicate.removeduplicate("cleanstream.txt","nodupStreaming.txt")

from itertools import tee
help(tee)

%%writefile test.txt
Author,Date,Text
MelanieT123,2017-10-06 05:50:39,"RT @AlamoOnTheRise: Trump: Day 258 Plans 2 decertify Iran nuke deal Picks coal lobbyist 4 top EPA job Fumed over 'moron' news Sz tonigh… "
dlindsey_16,2017-10-06 05:50:39,"RT @PeoplesOracle: But not for Puerto Rico. But not for healthcare. But not for education. https://t.co/2H7MDPBgix"
debchu222,2017-10-06 05:50:39,"RT @MooreSenate: According to Biden, these liberals are planning to attack me with the same furry they went after President Trump with in 2…"
Chariah_laquise,2017-10-06 05:50:39,"RT @PeoplesOracle: But not for Puerto Rico.
Mandrake_AYS,2017-10-06 05:50:39,https://t.co/SUR5obeU1V
x_SimplyJayy,2017-10-06 05:50:39,"RT @PeoplesOracle: But not for Puerto Rico.
SnOwPinkMan,2017-10-06 05:50:39,RT @OriginalFunko: RT &amp; follow @OriginalFunko for the chance to win an #NYCC 2017 exclusive Old Man Logan Pop! https://t.co/IbzQkp0KT2
tical10,2017-10-06 05:50:39,"RT @Cdiscount: 🏆 #Concours
📱 Samsung #GalaxyS8 à gagner &gt; https://t.co/GVXBtJYqDK 🚨 Pour participer: RT + Tweet avec… "
madamyez,2017-10-06 05:50:39,"I heard this too. Been waiting to hear the contents of the note. https://t.co/GftjuRisig #LasVegasShooting #StephenPaddock #GunControl"
cowboyneok,2017-10-06 05:50:39,@PattyArquette Please get the word out!  #Trump Administration attacking the #Trans family in our #LGBTQ community.  https://t.co/AzkVuPUJnM
VeritasVirtusX,2017-10-06 05:50:39,"Trump ""Calm Before Storm" You will Find Out"" Mysterious Statement https://t.co/LwSUaj5fyZ via @YouTube"
selloscope15,2017-10-06 05:50:40,Sandbank I Dont Trust Me Either Womens Funny Slogan Casual Tee Round Collar Sleeveless Top … https://t.co/EXaCP743Ct
noelleenix,2017-10-06 05:50:40,"RT @K_JeanPierre: A President being called a ""moron"" by his cabinet secretary is unusual. But,it's Donald Trump so it's not surprising.""Mor…"
comalliwrites,2017-10-06 05:50:40,"RT @ASlavitt: BREAKING: This story is incredible. Trump personally ordering rates 4 American families in order to break ACA.
https://t…"MattCxr,2017-10-06 05:50:40,"RT @Cdiscount: 🏆 #Concours 🎮 #PS4Pro + #FIFA18 à gagner &gt; https://t.co/W4G4teimHN
AlliInCali72,2017-10-06 05:50:40,RT @DavidCornDC: They're not even pretending. https://t.co/HMb0FOkd0d
AmiuMandzukic,2017-10-06 05:50:40,"RT @Cdiscount: 🏆 #Concours
cheshiredoe,2017-10-06 05:50:40,RT @TheAtlPhoto: Photographing the Microscopic: Winners of Nikon Small World 2017 - 24 winners and honorable mentions… 
robbieisnice,2017-10-06 05:50:40,@XandraSchultz @tightsarntpants @LStanfield2 @DrBo42 @Styl_oh @brielarson I don't feel pity. I have very few emotio… https://t.co/1QEHekpanP
rrys1DEmpire: Follow everyone 
TheDentalOfflce,2017-10-06 05:50:40,RT @JB_Carlson: A president running on #ParisAgreement &amp; #SDGs will encourage our allies to help us in keeping our elections clean.… 
shadylady1031,2017-10-06 05:50:40,has Trump ever kept a campaign promise? NO https://t.co/JL15eptgTV
Trvp_Isaxc,2017-10-06 05:50:40,"RT @PolynesianSauce: 12) Me &amp; My Bitch ... You don’t scream “AND THEY ASK ME WHY I TRUST NO BITCH, CAUSE MY EX HAD ME FEELING ALL EMBARR… "
CrazzyCattLady,2017-10-06 05:50:40,https://t.co/uUOy3dYhoJ
sherfouch,2017-10-06 05:50:40,"RT @HeerJeet: 3. Bannon, Brietbart, the Mercers &amp; Milo: these are not fringe figures. Bannon ran Trump's campaign &amp; was White House advisor…"
Jogiejamette,2017-10-06 05:50:40,"RT @JohnWDean: Nixon: “I’m not a crook.” Trump: “I’m not a moron.”         h/t DW"
MazinWaheed,2017-10-06 05:50:40,RT @the1dstage: retweet if you want to gain just follow everyone who retweets and follow back whoever follows you🏼
templeheart55,2017-10-06 05:50:40,"RT @RVAwonk: --&gt; ""Iowa tried for months to get federal permission to fix their health insurance markets but they were shut down… "
jess7719,2017-10-06 05:50:40,RT @TPInsidr: Of course they're doubling down on their false report! Why is our media so dishonest? https://t.co/RofsRDZ3Dc
JaneMetzger75,2017-10-06 05:50:40,RT @KeithOlbermann: Just a reminder that this State Department Spokesperson used to co-host Fox And Friends. https://t.co/zG3dzeAjwB
faithfitzy,2017-10-06 05:50:40,@3hunnathot oh god NO. i don't know how to word things ever haha😰 i'm just sayin anyone that supports trump UGLY AF!
AgnesS5665,2017-10-06 05:50:40,"RT @kwilli1046: Teen #LasVegas victim found Pres. Trump's visit  ""comforting"" - ""he wasn't who we see on social media."" https://t.co/GUD9LT…"
LegitJayyy_,2017-10-06 05:50:40,RT @RileyJayDennis: holy shit what kinda president goes to hurricane victims &amp; tells them they cost him a lot of money &amp; they should be… 
Bladix29,2017-10-06 05:50:40,"RT @Cdiscount: 🏆 #Concours 

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
    for i in range(500):
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
        if len(c)<35:
            #print "Date :",c[21:]
            print count,"-Text:",c[39:]

outf =open("editTest.txt", "w")
outf.write(r)
outf.close()

outf = open("editTest.txt", "w") 
r = c[39:]   
outf.write(r)

lines = open("realDonaldTrump.txt","r")
line = lines.readline()
for line in lines:
    if "AMERICAN" in line :
         print line 



#need to open the file properly
with open("realDonaldTrump.txt", 'r') as fp:
    #as suggested by @Padraic Cunningham it is better to iterate over the file object
    for line in fp:
        #each piece of information goes in a list
        infos = line.split()
        #this makes sure that there are no problems if your file has a empty line
        #and finds bob in the information
        if infos and infos[-1] == "trump":
            print (infos[2])



with open("editTest.txt") as openfile:
    for line in openfile:
         if "trump" in line:
                print line

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
        if len(c)<35:
            outf = open("editTest.txt", "a") 
            r = c[39:]   
            outf.write(r)
            outf.close()
            print c[39:]

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
            print c[39:]

with io.open("symmetrymag_tweets.csv", "w", encoding="utf-8") as inf:    
outf.close() 

with io.open("symmetrymag_tweets.csv", "w", encoding="utf-8") as inf:    
outf.close() 

from itertools import tee
count=0
with open("symmetrymag_tweets.csv") as inf:
    for line in inf:
        lines  = line[39:]
        outf = open("symmetrymag.txt", "a") 
        outf.write(lines)
outf.close() 

from itertools import tee
import io
count=0

with io.open("symmetrymag_tweets.csv", "r") as inf:    
    for line in inf:
        lines  = line[39:]
        outf = open("symmetrymagexp.txt", "w") 
        outf.write(lines)
outf.close() 

from itertools import tee
count=0
with open("realDonaldTrump_tweets.csv") as inf:
    for line in inf:
        lines  = line[39:]
        outf = open("realDonaldTrump.txt", "a") 
        outf.write(lines)
outf.close() 

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

from itertools import tee
search = raw_input('Search Term')
with open("symmetrymag_tweets.csv") as inf:
    # set up iterators
    cfg,res = tee(inf)
    # advance cfg by four lines
    for i in range(4):
        next(cfg)

    for c,r in zip(cfg, res):
        if search in c:
            print "Date :",c[21:38],"\nText :",c[39:]

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

!locate Key.py

import Key

#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import sys
sys.path.insert(0,"/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import Key
from random import randint

#USER = raw_input("User  : ") or "CNN"

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
    while len(new_tweets) > 0:
    #while len(new_tweets) < 400:    
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
    USER = raw_input("User  : ") or "CNN"
    #gaberivera symmetrymag
    get_all_tweets(USER)

import tweepy #https://github.com/tweepy/tweepy
import csv
import sys
sys.path.insert(0,"/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import Key
from random import randint
consumer_key = Key.twiter()[0]
consumer_secret = Key.twiter()[1]
access_key = Key.twiter()[2]
access_secret = Key.twiter()[3]

def get_all_tweets(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    alltweets = []	
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        print (len(alltweets))
        if (len(alltweets)) >200:
            outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
            with open('%s_tweets.csv' % screen_name, 'wb') as f:
                writer = csv.writer(f)
                writer.writerow(["id","created_at","text"])
                writer.writerows(outtweets)
            pass
if __name__ == '__main__':
    USER = raw_input("User  : ") or "CNN"
    get_all_tweets(USER)

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


%%writefile /home/jack/anaconda2/lib/python2.7/site-packages/Txmanip/findhashwork.py

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


textin= open('hashtag.txt', 'r')
lines = textin.readlines()
for line in lines:
    time.sleep(1)
    print line

import time
textin= open('hashtag.txt', 'r')
lines = textin.read()
time.sleep(1)
print lines,

textin= open('hashtag.txt', 'r')
lines = textin.read().splitlines()
time.sleep(1)
print lines,

def linesonly():
    with open('hashonly.txt') as infile, open('hashonlyNoBlank.txt', 'w') as outfile:
        for line in infile:
            if not line.strip(): continue  # skip the empty line
            outfile.write(line)  # non-empty
linesonly()            

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

#lines = open('phrases.txt', 'r').readlines()
lines = open('phrases.txt', 'r').read()
lines_set = set(lines)
out  = open('phrases2.txt', 'w')
for line in lines_set:
    out.write(line)

%%writefile Bt.py
def badtext(essays):
    badtext = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
    essay = essay.translate(badtext)
    return essay

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

file = open("realDonaldTrump_tweets.csv", 'r')
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
word = 'Hillary'
frequency = count_word(words, word)
print('Word: [' + word + '] Frequency: ' + str(frequency))

import random 

# get the first line if this is the one with the words words
lines = open("realDonaldTrump_tweets.csv").readlines() 
line = lines[0] 

words = line.split() 
myword = random.choice(words)
print myword

import random, heapq

with open('realDonaldTrump_tweets.csv') as fin:
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
    print(generate_the_word("realDonaldTrump_tweets.csv"))

main()

from textblob import TextBlob
import time
import sys
with io.open("realDonaldTrump_tweets.csv", "r", encoding="utf-8") as my_file:
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
with io.open("realDonaldTrump_tweets.csv", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 

blob = TextBlob(essays)
for np in blob.noun_phrases:
    print np


from textblob import TextBlob
with io.open("ToUse.txt", "r", encoding="utf-8") as my_file:
    essays = my_file.read() 
blob = TextBlob(essays)
for sentence in blob.sentences:
    print sentence

!python text2sent.py < realDonaldTrump_tweets.csv

!python text2sent.py < realDonaldTrump_tweets.csv

from textblob import TextBlob
import random
import sys
import io
filename ="realDonaldTrump_tweets.csv"
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
sys.path.insert(0, "/home/jack/anaconda2/pkgs/nltk-3.2.2-py27_0/lib/python2.7/site-packages/nltk")
from nltk import compat

from textblob import TextBlob
import sys
sys.path.insert(0, "/home/jack/Desktop/jack_watch/nltk-/nltk")
import compat
import random
filename ="realDonaldTrump_tweets.csv"
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

compat module is part of asyncio, a

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
    with open("virtual.txt", "a") as nf:
        nf.write(virtual)    

import markovify
# Get raw text as string
with open("realDonaldTrump.txt") as f:
    text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print three randomly-generated sentences of no more than 140 characters

for i in range(20):
    print(text_model.make_short_sentence(140))
    virtual =(text_model.make_short_sentence(140))
    with open("virtual.txt", "a") as nf:
        nf.write(virtual)

#badtext = ''.join(c for c in map(chr, range(256)) if not c.isalnum())

import markovify
# Get raw text as string
with open("elonmusk.txt") as f:
    text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print three randomly-generated sentences of no more than 140 characters

for i in range(18):
    print(text_model.make_short_sentence(140))
    virtual =(text_model.make_short_sentence(140))
    with open("virtual.txt", "a") as nf:
        nf.write(virtual)

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

import csv
import io
with io.open("realDonaldTrump_tweets.csv", "r", encoding="utf-8") as my_file:
    for row in csv.reader(my_file):
        print row

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
f = open("realDonaldTrump.txt")
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
f = open("realDonaldTrump.txt")
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

import RandomLine

filename = "realDonaldTrump.txt"    
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
HeadFirst.headFirst("realDonaldTrump_tweets.csv")

import random
afile = open("realDonaldTrump_tweets.csv","r")
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
afile = open("realDonaldTrump_tweets.csv", "r")
STR = random_line(afile)
print STR

import sqlite3
conn = sqlite3.connect('twitter.db')
c = conn.cursor()
c.execute("""
CREATE VIRTUAL TABLE hurr 
USING FTS3(text, keywords);
""")
conn.commit()
conn.close()

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

#Import os module
import os

# Ask the user to enter string to search
search_path = input("Enter directory path to search : ")
file_type = input("File Type : ")
search_str = input("Enter the search string : ")


# Append a directory separator if not already present
if not (search_path.endswith("/") or search_path.endswith("\\") ): 
        search_path = search_path + "/"
                                                          
# If path does not exist, set search path to current directory
if not os.path.exists(search_path):
        search_path ="."

# Repeat for each file in the directory  
for fname in os.listdir(path=search_path):

   # Apply file type filter   
   if fname.endswith(file_type):

        # Open file for reading
        fo = open(search_path + fname)

        # Read the first line from the file
        line = fo.readline()

        # Initialize counter for line number
        line_no = 1

        # Loop until EOF
        while line != '' :
                # Search for string in line
                index = line.find(search_str)
                if ( index != -1) :
                    print(fname, "[", line_no, ",", index, "] ", line, " ")

                # Read next line
                line = fo.readline()  

                # Increment line counter
                line_no += 1
        # Close the files
        fo.close()

#Import os module
import os

# Ask the user to enter string to search
#search_path = input("Enter directory path to search : ")
#file_type = input("File Type : ")
#search_str = input("Enter the search string : ")


# Append a directory separator if not already present
#if not (search_path.endswith("/") or search_path.endswith("\\") ): 
#        search_path = search_path + "/"
                                                          
# If path does not exist, set search path to current directory
#if not os.path.exists(search_path):
#        search_path ="/home/jack/Desktop"

# Repeat for each file in the directory  
for fname in os.listdir("/home/jack/Desktop/text_stuff/"):

   # Apply file type filter   
   if fname.endswith("*.ipynb"):

        # Open file for reading
        fo = open("/home/jack/Desktop/save-twitter/" + fname)

        # Read the first line from the file
        line = fo.readline()

        # Initialize counter for line number
        line_no = 1

        # Loop until EOF
        while line != '' :
                # Search for string in line
                index = line.find("justhost")
                if ( index != -1) :
                    print(fname, "[", line_no, ",", index, "] ", line, " ")

                # Read next line
                line = fo.readline()  

                # Increment line counter
                line_no += 1
        # Close the files
        fo.close()

"/home/jack/Desktop"
".ipynb"
"justhost"


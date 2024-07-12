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


import io
from textblob import TextBlob
from nltk.corpus import wordnet
tweetfile = 'phrases.txt'
filein = open(tweetfile, 'w')
filein.close()  
with io.open("elonmusk.txt", "r", encoding="utf-8") as my_file:
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
HashTag = (random_line('nodupsnohash.txt'))
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
    with open('clean.txt', 'w+') as out:
        for line in open(infile):
            line = line.replace("#","")
            out.write(line)

removeHash('hashonlyNoBlankNoDups.txt')

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

import glob
for file in glob.glob('/home/jack/Desktop/Snippet_Warehouse/*.ipynb'):
    print 'DEBUG: file=>{0}<'.format(file)
    with open(file) as f:
        contents = f.read()
    if 'nluug' in contents:
        print file




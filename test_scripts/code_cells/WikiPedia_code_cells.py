# import wikipedia doing a wikipedia.search
# searches for wiki pages concerning the topic
from time import sleep
import wikipedia
# opens a text input and prints
# Research : topic entered
topic = raw_input("Research : ")
rows = wikipedia.search(topic)
for row in rows:
    row = str(row)
    #row = row.replace("(disambiguation)","")
    print row


# Wiki Search -Summary of search results print to text
# AND to a database
import sqlite3
from time import sleep
from shutil import copyfile
import wikipedia
#backup your current datafile incase of a problem
dbname = 'WIKIData.db'
conn = sqlite3.connect(dbname) 
copyfile('WIKIData.db','WIKIData.db-bak')
topic = raw_input("Research : ")
fname = topic.replace(" ", "")+".txt"
fname = "Wiki_"+fname

conn.text_factory = str
c = conn.cursor()
c.execute('''
CREATE VIRTUAL TABLE IF NOT EXISTS wiki
USING FTS3(row, para);
''')
f =open(fname, "w")
f.close()

rows = wikipedia.search(topic)
for row in rows:
    row = row.encode('utf-8').strip()
    row = str(row)
    para = wikipedia.summary(row)
    para =  para.encode('utf-8').strip() 
    para = '\n\n'.join((row, para))
    enter = open(fname, "a")
    c.execute("INSERT INTO wiki VALUES (?,?)", (row, para))
    conn.commit()
    enter.write(para)
    enter.close()
    print para
enter.close()

import sqlite3
import sys
conn = sqlite3.connect('WIKIData.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
search = raw_input("Search : ")
for row in c.execute('SELECT rowid, row, para FROM wiki WHERE para MATCH ?', (search,)):    
    count=count+1
    print (row)[0],"-",(row)[1],"\n",(row)[2],"\n"
    if count > req:
        conn.close()
        sys.exit()

import sqlite3
import sys
conn = sqlite3.connect('WIKIData.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
#search = raw_input("Search : ")
for row in c.execute('SELECT rowid, row FROM wiki'):    
    count=count+1
    print (row)[0],"-",(row)[1]
    if count > req:
        conn.close()
        sys.exit()

import codecs
with codecs.open(filename,'r',encoding='utf8') as f:
    text = f.read()
# process Unicode text
with codecs.open(filename,'w',encoding='utf8') as f:
    f.write(text)

readOUT = open("ALLtextClean.txt","w")
readOUT.close()
readIn = open("ALLtext.txt","r")
readOUT = open("ALLtextClean.txt","a")
lines = readIn.readlines()
for line in lines:
    line=line.decode('utf-8','ignore').encode("utf-8")
    readOUT.write(line)
    



iconv -c -t UTF-8 < ALLtext.txt > exp001.txt

import Txmanip
help(Txmanip)

# %load /home/jack/anaconda2/lib/python2.7/site-packages/Txmanip/Txsearch
# Ask to enter string to search
# this will search all *.txt files in the current directory
# input window will ask "Search Phrase" 
"""
import Txsearch
Txsearch.txsearch()
"""
import os
import timeit
def txsearch():
    Sstring = raw_input("Search Phrase")
    for fname in os.listdir('./'):
       # Apply file type filter   
       if fname.endswith(".txt"):
            # Open file for reading
            fo = open(fname)
            # Read the first line from the file
            line = fo.readline()
            # Initialize counter for line number
            line_no = 1
            # Loop until EOF
            while line != '' :
                    index = line.find(Sstring)
                    if ( index != -1) :
                        # Set some parameters no lines longer than 240 characters 
                        # or less than search phrase +30 characters 
                        if len(line)< 240 and len(line)> len(Sstring)+20 :
                            #print(fname, "[", line_no, ",", index, "] ", line)
                            #print fname,line[1:-8],"  "
                            print fname,line_no,line
                    # Read next line
                    line = fo.readline()  
                    # Increment line counter
                    line_no += 1
            # Close the files
            fo.close()
            
txsearch()

from Txmanip import Txsearch
Txsearch.txsearch

from Txmanip import RemoveBlank
RemoveBlank.removeblank("ALLtext.txt", "ALLtextnb.txt")

!grep -axv '.*' ALLtextnbCleaner.txt

import re
nonascii = bytearray(range(0x80, 0x100))
with open('ALLtextnbClean.txt','rb') as infile, open('ALLtextnbCleaner.txt','wb') as outfile:
    for line in infile: # b'\n'-separated lines (Linux, OSX, Windows)
        line = re.sub(r'[^\x00-\x7f]',r'', line)
        outfile.write(line.translate(None, nonascii))

nonascii = bytearray(range(0x80, 0x100))
with open('ALLtext.txt','rb') as infile, open('ALLtextClean.txt','wb') as outfile:
    for line in infile: # b'\n'-separated lines (Linux, OSX, Windows)
        re.sub(r'[^\x00-\x7f]',r'', your-non-ascii-string)
        outfile.write(line.translate(None, nonascii))

l = []
filenames = '*.txt'
for root,dir,filenames in os.walk('.'):
    l.extend([ os.path.join(root, f) for f in filenames ])
print l

l = []
for root,dir,filenames in os.walk(unicode('.')):
    l.extend([ os.path.join(root, f) for f in filenames ])
print l

readOUT = open("ALLtextClean.txt","w")
readOUT.close()
import io
with io.open('ALLtext.txt','r',encoding='utf8') as f:
    text = f.read()
    text = text.strip()
# process Unicode text
with io.open('ALLtextClean.txt','a',encoding='utf8') as f:
    f.write(text)

%reset -f 

#!/usr/bin/env python
nonascii = bytearray(range(0x80, 0x100))
with open('d.txt','rb') as infile, open('d_parsed.txt','wb') as outfile:
    for line in infile: # b'\n'-separated lines (Linux, OSX, Windows)
        outfile.write(line.translate(None, nonascii))

readOUT = open("ALLtextClean.txt","w")
readOUT.close()
import io
with io.open('ALLtextnbCleaner.txt','r',encoding='utf8') as f:
    text = f.read()
    #text = text.encode('ISO-8859-1').strip()
    #text = text.decode("utf-16")
# process Unicode text
with io.open('ALLtextClean.txt','a',encoding='utf8') as f:
    f.write(text)

line=line.decode('utf-8','ignore').encode("utf-8")

# import wikipedia doing a wikipedia.search
# searches for wiki pages concerning the topic
from time import sleep
import wikipedia
# opens a text input and prints
# Research : topic entered
#topic = raw_input("Research : ")
rows = wikipedia.search("java")
for row in rows:
    rown = str(row)
    lisT = wikipedia.search(rown)
    bt = rown,lisT
    
    print bt

.encode('ascii', 'ignore')
.encode("utf-8")

.encode('utf-8').strip()

%reset -f

# import wikipedia doing a wikipedia.search
# searches for wiki pages concerning the topic
from time import sleep
import wikipedia
from ast import literal_eval
# opens a text input and prints
# Research : topic entered
#topic = raw_input("Research : ")
f = open("super.txt", "a")
rows = wikipedia.search("Java virtual machine")
for row in rows:
    nrows = wikipedia.search(row)
    for nrow in nrows:
            nrow = nrow.encode('utf-8').strip()
            Sum = wikipedia.summary(nrow)
            Sum = Sum.encode('utf-8').strip() 
            f.write(Sum)   
    

del rows
del nrow
del Sum

f = open("super.txt", "w")
f.close()

%reset -f

# import wikipedia doing a wikipedia.search
# searches for wiki pages concerning the topic
from time import sleep
import wikipedia
from ast import literal_eval
# opens a text input and prints
# Research : topic entered
#topic = raw_input("Research : ")
f = open("super.txt", "a")
rows = wikipedia.search("micro processor")
for row in rows:
    sleep(1)
    nrows = wikipedia.search(row)
    for nrow in nrows:
        
        nrow = nrow.encode('utf-8').strip()
        f.write(nrow)
    

import wikipedia

try:
     rows = wikipedia.search("topic")
except wikipedia.exceptions.DisambiguationError as e:
     rows = e.options
for row in rows:
    row = str(row)
    print row


# Wiki Search -Summary of search results print to text
# AND to a database
import sqlite3
from time import sleep
from shutil import copyfile
#backup your current datafile incase of a problem
copyfile('WIKIData.db','WIKIData.db-bak')
topic = raw_input("Research : ")
fname = topic.replace(" ", "")+".txt"
fname = "Wiki_"+fname
dbname = 'WIKIData.db'
conn = sqlite3.connect(dbname) 
conn.text_factory = str
c = conn.cursor()
c.execute('''
CREATE VIRTUAL TABLE IF NOT EXISTS wiki
USING FTS3(row, para);
''')
f =open(fname, "w")
f.close()
import wikipedia

try:
     rows = wikipedia.search(topic)
except wikipedia.exceptions.DisambiguationError as e:
     if e.options >""
        rows = e.options

    
     for row in rows:
        row = str(row)

        sleep(.2)
        para = wikipedia.summary(row)
        para = '\n\n'.join((row, para)).encode('utf-8').strip()
        enter = open(fname, "a")
        #c.execute("INSERT INTO wiki VALUES (?,?)", (row, para))
        conn.commit()
        enter.write(para)
        enter.close()
        print para
enter.close()

# Wiki Search -Summary of search results print to text
# AND to a database
import sqlite3
from time import sleep
from shutil import copyfile
#backup your current datafile incase of a problem
copyfile('WIKIData.db','WIKIData.db-bak')
topic = raw_input("Research : ")
fname = topic.replace(" ", "")+".txt"
fname = "Wiki_"+fname
dbname = 'WIKIData.db'
conn = sqlite3.connect(dbname) 
conn.text_factory = str
c = conn.cursor()
c.execute('''
CREATE VIRTUAL TABLE IF NOT EXISTS wiki
USING FTS3(row, para);
''')
f =open(fname, "w")
f.close()
import wikipedia
rows = wikipedia.search(topic)
for row in rows:
    row = str(row)
    sleep(.2)
    para = wikipedia.summary(row)
    para = '\n\n'.join((row, para)).encode('utf-8').strip()
    enter = open(fname, "a")
    #c.execute("INSERT INTO wiki VALUES (?,?)", (row, para))
    conn.commit()
    enter.write(para)
    enter.close()
    print para
enter.close()

# Wiki Search -Summary of search results print to text
# AND to a database
import sqlite3
from time import sleep
from shutil import copyfile
import wikipedia
#rows = wikipedia.search('war')
#for row in rows:
#        row = str(row)
#        sleep(.2)
#        print row
    
try:
    rows = wikipedia.search('war')
except wikipedia.exceptions.DisambiguationError as e:
    print rows
    rows = wikipedia.summary(row)
    for row in rows:
        row = str(row)
        #print row
        sleep(.2)        
        ns= e.options
        #rows = wikipedia.search(ns)   
            
        para = wikipedia.summary(row)
        para = '\n\n'.join((row, para)).encode('utf-8').strip()
        #print para


import re
import wikipedia
try:
            mercury = wikipedia.summary("Mercury")
except wikipedia.exceptions.DisambiguationError as e:
      for text in e.options:
            if (wikipedia.exceptions.DisambiguationError):
                pass
            else:
                print text
            

for line in f:
    if re.match(">",line):
        pass
    else:
        line = line.rstrip("\n")
        string = string + line

#Or

for line in f:
    if not re.match(">",line):
        line = line.rstrip("\n")
        string = string + line

from time import sleep
import re
import wikipedia
try:
        mercury = wikipedia.summary("Mercury")
except wikipedia.exceptions.DisambiguationError as e:
        #lineS = e.options
        lineS = str(e.options)
        for lines in lineS:
            sleep(1)
            print lines

from time import sleep
import re
import wikipedia
try:
        mercury = wikipedia.summary("Mercury")
except wikipedia.exceptions.DisambiguationError as e:
        #lineS = e.options
        lineS = str(e.options)
        for lines in lineS.strip():
            lines=lines.replace("u'","");lines=lines.replace("', ","\n")
            lines=lines.replace("[","");lines=lines.replace("]","")
            lines=lines.replace('u"','');lines=lines.replace('"','')
            if re.match('(disambiguation)',lines):
                pass
            else:
                sleep(1)
                print lines


try:
        mercury = wikipedia.summary("Mercury")
except wikipedia.exceptions.DisambiguationError as e:
        lines = str(e.options)
        lines=lines.replace("u'","");lines=lines.replace("', ","\n")
        lines=lines.replace("[","");lines=lines.replace("]","")
        lines=lines.replace('u"','');lines=lines.replace('"','')
        with open("textwik.txt", "w")as f:
                f.write(lines) 
f.close()
bad_words = ['(disambiguation)', 'All pages']
with open('textwik.txt') as oldfile, open('usewik.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)

import wikipedia
mercury = wikipedia.search("Sun")
e = wikipedia.exceptions.DisambiguationError

#mercury2 = wikipedia.summary(ns) 
print ns


import wikipedia

res = wikipedia.search('war')
#wikipedia.exceptions.DisambiguationError as e:
    
rows = wikipedia.summary(res)
for row in rows:
    print row,

import sqlite3
import sys
conn = sqlite3.connect('wikipedia.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
search = raw_input("Search : ")
for row in c.execute('SELECT rowid, text FROM wiki WHERE text MATCH ?', (search,)):    
    count=count+1
    print (row)[0],"-",(row)[1],"\n"
    if count > req:
        conn.close()
        sys.exit()

import sqlite3
import sys
conn = sqlite3.connect('wikipedia.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
search = raw_input("Search : ")
#SELECT Title FROM Book WHERE Desc LIKE '%cat%";
#for row in c.execute('SELECT rowid, text FROM wiki WHERE text MATCH ?', (search,)):
#for row in c.execute("SELECT rowid, text FROM wiki WHERE text LIKE '%memory%';");
#for row in c.execute("SELECT rowid, text FROM wiki WHERE text LIKE '%memory%';")
#for row in c.execute("SELECT rowid, text FROM wiki WHERE text LIKE '%?%'", (search,)):
for row in c.execute("SELECT rowid, text FROM wiki WHERE text LIKE '%war%'", (search,)):    
    count=count+1
    print (row)[0],"-",(row)[1],"\n"
    if count > req:
        conn.close()
        sys.exit()

%%writefile wikilist.txt
World Population
Political leaders
Christian
knights Templar
Elon Musk
Bowing
Turner Broadcasting
New World Order (conspiracy theory)
New world order (politics)
Federal Reserve
illuminati
Nuclear Bomb
Weapon of mass destruction
biological warfare
Vietnam War
World War One
Space craft
Iran war
World War Two
World bank
Monroe Doctrine
Putin
KKK
Democracy
US Republican party
US Democratic Party
Socrates
Plato
Sigmund Freud
Mental Breakdown
Post Tramatic Stress
Communism
Communist party
Fascism
Chinese Politics
Fidel Castro
Economy
Economics
Slavery
American Civil War

%%writefile wikilist2.txt
Data mining
Competitive intelligence
National security
Harvard University
Python (programming language)
Object-oriented programming
Functional programming
Logic programming
Turing machine
DNA nanotechnology
Data Science: An Introduction
Data Science: An Introduction/Definitions of Data
    

import wikipedia
import time
f= open("wikilist2.txt", "r")
lines = f.read().splitlines()
for line in lines:
    text = wikipedia.summary(line)
    text = text.replace(". ",".\n")
    text = text.encode("ascii", "ignore")
    Tfile = open("tempfile2.txt","a")
    Tfile.write(text)
    Tfile.close()    
    time.sleep(10)
    print line

import wikipedia
import time
f= open("wikilist2.txt", "r")
lines = f.read().splitlines()
for line in lines:
    text = wikipedia.summary(line)
    text = text.replace(". ",".\n")
    text = text.encode("ascii", "ignore")
    Tfile = open("tempfile2.txt","a")
    Tfile.write(text)
    Tfile.close()    
    time.sleep(10)
    print line

import wikipedia
text = wikipedia.summary("American Civil War")
text = text.replace(". ",".\n\n")
print text

import wikipedia
text = wikipedia.summary(line)
text = text.replace(". ",".\n")
text = text.encode("ascii", "ignore")
Tfile = open("tempfile.txt","a")
Tfile.write(text)
Tfile.close()

import sqlite3
import feedparser
import time
import sqlite3
import wikipedia
Dbase = 'wikipedia.db'
conn = sqlite3.connect(Dbase)
c = conn.cursor()
c.execute('''
CREATE VIRTUAL TABLE IF NOT EXISTS wiki
USING FTS3(text);
''')
reaD = open("tempfile2.txt","r")
lines = reaD.readlines()
for line in lines:
    if len(line) > 30:
        conn = sqlite3.connect(Dbase)
        #conn.text_factory = str
        c = conn.cursor()
        c.execute("INSERT INTO wiki  VALUES (?)", (line,))
        conn.commit()
        conn.close()
conn = sqlite3.connect(Dbase)
#conn.text_factory = str
c = conn.cursor()# Never
count=0
for row in c.execute('SELECT * FROM wiki ORDER BY rowid DESC'):
    row=str(row)
    row = row.decode("ascii", "ignore")
    count=count+1
    row =row.replace("(u'","");row =row.replace("', u","Keyword : ")
    row =row.replace("\n","");row =row.replace("')","'")
    row =row.replace("\nKeyword","Keyword")
    print"Number :",count,"\n",row ,"\n"



import sqlite3
import sys
conn = sqlite3.connect('wikipedia.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
search = raw_input("Search : ")
for row in c.execute('SELECT rowid, text FROM wiki WHERE text MATCH ?', (search,)):    
    count=count+1
    print (row)[0],"-",(row)[1],"\n"
    if count > req:
        conn.close()
        sys.exit()

import sqlite3
import feedparser
import time
import sqlite3
import wikipedia
Dbase = 'wikipedia.db'
conn = sqlite3.connect(Dbase)
c = conn.cursor()
c.execute('''
CREATE VIRTUAL TABLE IF NOT EXISTS wiki
USING FTS3(text);
''')

keyword = "Heaven"
text = wikipedia.summary(keyword)
text = text.encode("ascii", "ignore")
text = text.replace(". ",".\n")

Tfile = open("tempfile.txt","w")
Tfile.write(text)
Tfile.close()

reaD = open("tempfile.txt","r")
lines = reaD.readlines()
for line in lines:
    if len(line) > 30:
        conn = sqlite3.connect(Dbase)
        #conn.text_factory = str
        c = conn.cursor()
        c.execute("INSERT INTO wiki  VALUES (?)", (line,))
        conn.commit()
        conn.close()
        
        
conn = sqlite3.connect(Dbase)
#conn.text_factory = str
c = conn.cursor()# Never
count=0
for row in c.execute('SELECT * FROM wiki ORDER BY rowid DESC'):
    row=str(row)
    row = row.decode("ascii", "ignore")
    count=count+1
    row =row.replace("(u'","");row =row.replace("', u","Keyword : ")
    row =row.replace("\n","");row =row.replace("')","'")
    row =row.replace("\nKeyword","Keyword")
    print"Number :",count,"\n",row ,"\n"



import sqlite3
import feedparser
import time
import sqlite3
import wikipedia
Dbase = 'wikipedia.db'
conn = sqlite3.connect(Dbase)
c = conn.cursor()
c.execute('''
CREATE VIRTUAL TABLE IF NOT EXISTS wiki
USING FTS3(text, key);
''')

keyword = "Heaven"
text = wikipedia.summary("Heaven")
text = text.encode("ascii", "ignore")
text = text.replace(". ",". \n")

Tfile = open("tempfile.txt","w")
Tfile.write(text)
Tfile.close()

reaD = open("tempfile.txt","r")
lines = reaD.readlines()
for line in lines:
    if len(line) > 30:
        conn = sqlite3.connect(Dbase)
        c = conn.cursor()
        c.execute("INSERT INTO wiki  VALUES (?, ?)", (line, keyword))
        conn.commit()
        conn.close()
        
        
conn = sqlite3.connect(Dbase)
c = conn.cursor()# Never
count=0
for row in c.execute('SELECT * FROM wiki ORDER BY rowid DESC'):
    row=str(row)
    row = row.decode("ascii", "ignore")
    count=count+1
    row =row.replace("(u'","");row =row.replace("', u","Keyword : ")
    row =row.replace("\n","");row =row.replace("')","'")
    row =row.replace(". \n",".")
    print"Number :",count,"\n",row ,"\n"



# %load tempfile.txt
Heaven, the heavens, seven heavens, pure lands, Tian, Jannah, Valhalla, or The Summerland, is a common religious, cosmological, or transcendent place where beings such as gods, angels, jinn, saints, or venerated ancestors are said to originate, be enthroned, or live. 
According to the beliefs of some religions, heavenly beings can descend to earth or incarnate, and earthly beings can ascend to Heaven in the afterlife, or in exceptional cases enter Heaven alive.
Heaven is often described as a "higher place", the holiest place, a Paradise, in contrast to Hell or the Underworld or the "low places", and universally or conditionally accessible by earthly beings according to various standards of divinity, goodness, piety, faith, or other virtues or right beliefs or simply the will of God. 
Some believe in the possibility of a Heaven on Earth in a World to Come.
Another belief is in an axis mundi or world tree which connects the heavens, the terrestrial world, and the underworld. 
In Indian religions, Heaven is considered as Svarga loka, and the soul is again subjected to rebirth in different living forms according to its karma. 
This cycle can be broken after a soul achieves Moksha or Nirvana. 
Any place of existence, either of humans, souls or deities, outside the tangible world (Heaven, Hell, or other) is referred to as otherworld.

import sqlite3
import time
#account = "TEDTalks.txt"
account = "symmetrymag.txt"
#account = "elonmusk.txt"
#account = "realDonaldTrump.txt"
user = account[:-4]
lines = open(account,"r")
line = lines.readline()
for line in lines:
    conn = sqlite3.connect('collection.db')
    conn.text_factory = str
    c = conn.cursor()
    c.execute("INSERT INTO tweets VALUES (?,?)", (line, user)) 
    conn.commit()
    conn.close()        
    
    #print line         

import wikipedia
text = wikipedia.summary("Machine Learning")
print text

p.agent_info = u' '.join((agent_contact, agent_telno)).encode('utf-8').strip()

print wikipedia.summary("Bohol")

# -*- coding: utf-8 -*-
import pdb
text = wikipedia.summary("Manila, Philippines")
text0 = wikipedia.summary("Philippines")
text1 = wikipedia.summary("Palawan, Philippines")
text2 = wikipedia.summary("China Sea")

text = text.encode("ascii", "ignore")
text0 = text0.encode("ascii", "ignore")
text1 = text1.encode("ascii", "ignore")
text2 = text2.encode("ascii", "ignore")
join1 = "".join((text, text0))
join2 = "\n".join((text1, text2))
en= "\n".join((join1, join2))
print en

!ls Wiki_*

# Get number of words in a file
fname = raw_input("Enter file name: ")
num_words = 0
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print "Number of words: ",num_words

fname = raw_input("Enter file name: ")
num_words = 0
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print "Number of words: ",num_words

fname = raw_input("Enter file name: ")
num_words = 0
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print "Number of words: ",num_words

import sqlite3
import sys
dbname = 'WIKIData.db'
conn = sqlite3.connect(dbname) 
conn.text_factory = str
c = conn.cursor()
count=0;req=200
search = raw_input("Search : ")
for row in c.execute('SELECT rowid, row, para FROM wiki WHERE wiki MATCH ?', (search,)):    
    count=count+1
    print (row)[0],"-",(row)[1],(row)[2]
    if count > req:
        conn.close()
        sys.exit()
        
        row, para

from time import sleep
topic = raw_input("Research : ")
fname = topic.replace(" ", "")+".txt"
fname = "Wiki_"+fname
f =open(fname, "w")
f.close()
import wikipedia
rows = wikipedia.search(topic)
for row in rows:
    sleep(1)
    para = wikipedia.summary(row)
    para = '\n\n'.join((row, para)).encode('utf-8').strip()
    enter = open(fname, "a")
    enter.write(para)
    enter.close()
    print para
enter.close()

import pdb
from time import sleep
f =open("trumpstuff.txt", "w")
f.close()
import wikipedia
rows = wikipedia.search("Donald Trump")
with open("trumpstuff.txt", "a") as enter:
    for row in rows:
        sleep(1)
        para = wikipedia.summary(row)
        artical = (row,"\n"+para)
        artical = str(artical).encode("ascii", "ignore") 
        enter.write(artical)
        print row
        
enter.close()

from time import sleep
topic = "Donald Trump"
fname = topic.replace(" ", "")+".txt"
print fname

import wikipedia
wikipedia.search("Philippines")



import wikipedia
wikipedia.search("New York")

import wikipedia
#wikipedia.summary("Facebook", sentences=1)
wikipedia.search("Facebook")

\xe9

import wikipedia
wikipedia.search("Art Nouveau")
# Facebook est un service de réseautage social en lig

import wikipedia
help(wikipedia)

your_string = str(the_bytes, 'utf-8') # actually uses `conn.text_factory`, not `str`

conn.text_factory = lambda x: str(x, 'latin1')

    'iso-8859-1'
    'utf-16'
    'utf-32'
    'latin1'
conn.text_factory = bytes

import sqlite3
import base64
conn = sqlite3.connect('snippet.db') 
c = conn.cursor()
conn.text_factory = str
file = """
%%writefile SatInfo.py
from itertools import izip, islice
from time import sleep
def satinfo():
    search_string = raw_input("Load : ")
    with open('visual.txt', 'r') as infile, open('visual.tmp', 'w') as outfile:
        for line in infile:
            if search_string in line:
                outfile.writelines([line, next(infile), next(infile)])

    from time import sleep
    with open('visual.tmp', 'r') as f:
        while True:
                name = f.readline()
                one = f.readline()
                two = f.readline()
                sleep(1)
                return name, one, two    
                         
def prntlist():            
    from time import sleep
    with open('visual.txt', 'r') as f:
        while True:
            next_n_lines = list(islice(f, 3))
            if not next_n_lines:
                break
            sleep(.5)
            print next_n_lines[0],
        
def reuse():
    from time import sleep
    with open('visual.tmp', 'r') as f:
        while True:
                name = f.readline()
                one = f.readline()
                two = f.readline()
                sleep(1)
                #print name, one, two    
                f.close()
                return name, one, two  
            
            
"""
keywords = "store, retrieve images, from SQLite Database"
encodedlistvalue=base64.b64encode(file)
c.execute("INSERT INTO snippet VALUES (?,?,?)", (encodedlistvalue, file, keywords))
conn.commit()
conn.close()

from textblob import TextBlob
import random
import sys
import io
filename ="ALLWIKI.txt"
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

for item in random.sample(short_sentences, 30):
	print item

# %load SearchFilename.py
'''
Search a filename for a phrase and how many following lines to display
USAGE:
import SearchFilename
filename = "hek.txt"
length = 4
SearchFilename.searchfilename(filename, length)
'''
def searchfilename(filename, length):
    f = open(filename, "r")
    searchlines = f.readlines()
    f.close()
    search = str(raw_input("Search Phrase : "))
    for i, line in enumerate(searchlines):
        if search in line: 
            for l in searchlines[i:i+length]: print l,
            print
            
USAGE:
import SearchFilename
filename = "Automate-the-Boring-Stuff.txt"
# length = how many lines after
length = 4
SearchFilename.searchfilename(filename, length) 

import SearchFilename
filename = "astralGOOD.txt"
length = 4
SearchFilename.searchfilename(filename, length)

from shutil import copyfile
copyfile("pdf.txt", "IPythonInteractiveComputing.txt")

Tfile = open("pdf.txt","w")
Tfile.close()

from time import sleep
import textract
#lines = textract.process("/home/jack/Desktop/Books/Web-Scraping-With-Python.pdf")
#lines = textract.process("/home/jack/Desktop/Books/Automate-the-Boring-Stuff-with-Python.pdf")
#lines = textract.process("/home/jack/Desktop/Books/Python_Cookbook_3rd_Edition.pdf")
#lines = textract.process("/home/jack/Desktop/Books/Effective_Python.pdf")
#lines = textract.process("/home/jack/Desktop/Books/IPythonInteractiveComputingandVisualizationCookbook.pdf")
lines = textract.process("BookOfEnoch.pdf")
for line in lines.split("."):
    #line = line.replace(".",".\n")
    line = line.replace("	"," ")
    Tfile = open("BookOfEnochGood2.txt","a")
   
    Tfile.write(line)
    #print line
    Tfile.close()


import sqlite3        
import feedparser
import time
import sqlite3
Dbase = 'pdfs.db'
conn = sqlite3.connect(Dbase)
conn.text_factory = str
c = conn.cursor()
c.execute('''
CREATE VIRTUAL TABLE IF NOT EXISTS pdfs
USING FTS3(text, title);
''')

title = "TwitterDataAnalytics"
#text = wikipedia.summary("Heaven")
#text = text.encode("ascii", "ignore")
#text = text.replace(". ",". \n")

reaD = open("pdf.txt","r")
lines = reaD.readlines()
for line in lines:
    line = line.decode("utf8")
    conn = sqlite3.connect(Dbase)
    c = conn.cursor()
    c.execute("INSERT INTO pdfs  VALUES (?, ?)", (line, title))
    conn.commit()
    conn.close()

import sqlite3        
import feedparser
import time
import sqlite3
Dbase = 'BookOfEnochpdf.db'
conn = sqlite3.connect(Dbase)
conn.text_factory = str
c = conn.cursor()
c.execute('''
CREATE VIRTUAL TABLE IF NOT EXISTS pdfs
USING FTS3(text, title);
''')

title = "BookOfEnochpdf"
#text = wikipedia.summary("Heaven")
#text = text.encode("ascii", "ignore")
#text = text.replace(". ",". \n")

reaD = open("BookOfEnochpdf.txt","r")
lines = reaD.readlines()
for line in lines:
    line = line.decode("utf8")
    conn = sqlite3.connect(Dbase)
    c = conn.cursor()
    c.execute("INSERT INTO pdfs  VALUES (?, ?)", (line, title))
    conn.commit()
    conn.close()

import sqlite3
import sys
conn = sqlite3.connect('pdfs.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
search = raw_input("Search : ")
for row in c.execute('SELECT rowid, text FROM pdfs WHERE text MATCH ?', (search,)):    
    count=count+1
    print (row)[0],"-",(row)[1],
    if count > req:
        conn.close()
        sys.exit()

import sqlite3
import sys
conn = sqlite3.connect('pdfs.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
id1 = raw_input("Starting ID : ")
id2 = raw_input("How Many Rows : ")

#for row in c.execute('Select rowid, * from pdfs LIMIT ?,?', (id1, id2)):
#for row in c.execute('Select rowid, * from pdfs LIMIT ?,?', (id1, id2)):
for row in c.execute('SELECT rowid, * from pdfs LIMIT ? OFFSET ?',  (id2, id1)):
    count=count+1
    print (row)[0],"-",(row)[1],
    if count > req:
        conn.close()
        sys.exit()

from time import sleep

import textract
lines = textract.process("/home/jack/Desktop/Books/1b1b23ac635d29c6.pdf")

for line in lines.split():
    line = line.replace(".",".\n")
    sleep(.1)
    print line,



# Open A PDF and Save as TEXT file
# keywords read pdf as text , save pdf as text
# pdf2txt , textract
from time import sleep
import textract

lines = textract.process("Edition.pdf")
for line in lines.split("."):
    #line = line.replace(".",".\n")
    line = line.replace("	"," ")
    Tfile = open("pdf.txt","a")
   
    Tfile.write(line)
    #print line
    Tfile.close()


 
I have about a dozen PDF books in my database. Easy to use reference for Python. Also a Linux Bible, module info, Docker, FFmpeg, bash, etc

# Notice title = "Edition" this allows the 
# pdf title to be used in a search if required
import time
import sqlite3
Dbase = 'pdfs.db'
conn = sqlite3.connect(Dbase)
conn.text_factory = str
c = conn.cursor()
c.execute('''
CREATE VIRTUAL TABLE IF NOT EXISTS pdfs
USING FTS3(text, title);
''')

title = "Edition"
reaD = open("pdf.txt","r")
lines = reaD.readlines()
for line in lines:
    line = line.decode("utf8")
    conn = sqlite3.connect(Dbase)
    c = conn.cursor()
    c.execute("INSERT INTO pdfs  VALUES (?, ?)", (line, title))
    conn.commit()
    conn.close()

import sqlite3
import feedparser
import time
import sqlite3
Dbase = 'pdfs.db'
conn = sqlite3.connect(Dbase)
c = conn.cursor()
c.execute('''
CREATE VIRTUAL TABLE IF NOT EXISTS pdfs
USING FTS3(text, title);
''')

title = "Edition"

reaD = open("pdf.txt","r")
lines = reaD.readlines()
for line in lines:
    conn = sqlite3.connect(Dbase)
    c = conn.cursor()
    c.execute("INSERT INTO wiki  VALUES (?, ?)", (line, title))
    conn.commit()
    conn.close()

import sqlite3
import feedparser
import time
import sqlite3
Dbase = 'pdfs.db'
conn = sqlite3.connect(Dbase)
c = conn.cursor()
c.execute('''
CREATE VIRTUAL TABLE IF NOT EXISTS pdfs
USING FTS3(text, title);
''')

title = "Web Scraping with Python"
#text = wikipedia.summary("Heaven")
#text = text.encode("ascii", "ignore")
#text = text.replace(". ",". \n")

reaD = open("tempfile.txt","r")
lines = reaD.readlines()
for line in lines:
    if len(line) > 30:
        conn = sqlite3.connect(Dbase)
        c = conn.cursor()
        c.execute("INSERT INTO wiki  VALUES (?, ?)", (line, title))
        conn.commit()
        conn.close()

import sqlite3
import sys
conn = sqlite3.connect('snippet.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
search = raw_input("Search : ")
for row in c.execute('SELECT * FROM snippet WHERE snippet MATCH ?', (search,)):    
    count=count+1
    print (row)[1]," -- KEYWORDS",(row)[2],"\n"
    if count > req:
        conn.close()
        sys.exit()

from time import sleep
import sqlite3
conn = sqlite3
hist = open("/home/jack/.bash_history")
for line in hist.readlines():
    sleep(.5)
    print line

import sqlite3
from IPython.core.display import Image 
def get_image(cursor, image_id):
    cursor.execute("SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = ?;",(image_id,))
    ablob, ext, afile = cursor.fetchone()
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    return filename
Dbase = 'ImageB.db'
conn = sqlite3.connect(Dbase)
cur = conn.cursor()
ImageID = raw_input("Image ID number : ")
filename = get_image(cur, ImageID)
cur.close()
conn.close()
print filename
Image(filename=filename)


import sqlite3
import feedparser
from time import sleep
import sqlite3
import io
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
Dbase = 'history2.db'
conn = sqlite3.connect(Dbase)
c = conn.cursor()
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS history 
USING FTS3(hist);
"""
         )
histsave= io.open("my_utf8_file.txt", "w", encoding="utf-8")
histsave.close()

hist = open("/home/jack/.bash_history", "r")
for line in hist.readlines():
        #line = line.encode('utf-8').strip()
        #line = line.decode('utf-8')
        #line = line.replace(" u'","")
        #line = line.decode('utf-8').strip() 
        #f= open("bashhis.txt", "a")
        import io
        with io.open("my_utf8_file.txt", "a", encoding="utf-8") as out_file:
            out_file.write(line)


job_titles = [line.decode('utf-8').strip() for line in title_file.readlines()]

from time import sleep
import sqlite3
conn = sqlite3.connect('historyFTS4.db')
c = conn.cursor()
conn.text_factory = str
c.execute("""
CREATE VIRTUAL TABLE history 
USING FTS4(text);
""")
fileO = open("/home/jack/.bash_history")
lists = fileO.readlines()
for list in lists:
    #list = list.encode("ascii", "ignore")
    list = list.decode('utf-8').strip() 
    c = conn.cursor()
    c.execute('insert into history values (?)', (list,))
    
conn.commit()
conn.close()

from time import sleep
import sqlite3
conn = sqlite3.connect('historyFTS4.db')
c = conn.cursor()
conn.text_factory = str
c.execute("""
CREATE VIRTUAL TABLE history 
USING FTS4(text);
""")
conn.commit()
conn.close()

fileO = open("/home/jack/.bash_history")
lists = fileO.readlines()
for list in lists:
    #list = list.encode("ascii", "ignore")
    list = list.decode('utf-8').strip() 
    conn = sqlite3.connect('historyFTS4.db')
    c = conn.cursor()
    c.execute('insert into history values (?)', (list,))
    conn.commit()
    conn.close()

!sqlite3 history2.db "pragma integrity_check;"

import sqlite3
import feedparser
from time import sleep
import sqlite3
Dbase = 'history2.db'
conn = sqlite3.connect(Dbase)
c = conn.cursor()
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS history 
USING FTS3(hist);
"""
)

f= open("bashhis.txt", "w")
close.f()

hist = open("/home/jack/.bash_history")
for line in hist.readlines():
        #f= open("bashhis.txt", "a")
        
        with open("bashhis.txt", 'a') as out_file:
        out_file.write(line)
        conn = sqlite3.connect(Dbase)
        c = conn.cursor()
        #line = line.encode('ascii')
        c.execute("INSERT INTO history VALUES (?)", (line,))
        conn.commit()
        conn.close()
conn = sqlite3.connect(Dbase)
c = conn.cursor()# Never
command = raw_input("Command : ")
for row in c.execute('SELECT rowid, hist FROM history WHERE hist MATCH ?', (command,)):   
    row=str(row)
    count=count+1
    print row[0],row[2]

import sqlite3
Dbase = 'history2.db'
conn = sqlite3.connect(Dbase)
c = conn.cursor()# Never

command = raw_input("Command : ")
for row in c.execute('SELECT rowid, text FROM history WHERE text MATCH ?', (command,)):   
    row=str(row)

    count=count+1
    print row[0],row[2]

import sqlite3
import sys
from time import sleep
conn = sqlite3.connect('historyFTS4.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
search = raw_input("Search : ")
for row in c.execute('SELECT rowid, text FROM history WHERE text MATCH ?', (search,)):    
    count=count+1
    sleep(1)
    print (row)[0],"-",(row)[1],"\n"



import sqlite3
import sys
from time import sleep
conn = sqlite3.connect('history.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
search = raw_input("Search : ")
for row in c.execute('SELECT rowid, text FROM history WHERE text MATCH ?', (search,)):    
    count=count+1
    sleep(1)
    print (row)[0],"-",(row)[1],"\n"



line = line.encode('ascii')
line = line.decode('utf-8').strip() 
 

import sqlite3
import os.path
from os import listdir, getcwd
from IPython.core.display import Image 

def get_picture_list(rel_path):
    abs_path = os.path.join(os.getcwd(),rel_path)
    print 'abs_path =', abs_path
    dir_files = os.listdir(abs_path)
    #print dir_files
    return dir_files

picture_list = get_picture_list('snippets')
print picture_list
import sqlite3
import os.path
from os import listdir, getcwd
from IPython.core.display import Image 

def create_or_open_db(db_file):
    db_is_new = not os.path.exists(db_file)
    conn = sqlite3.connect(db_file)
    if db_is_new:
        print 'Creating schema'
        sql = '''create table if not exists PICTURES(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PICTURE BLOB,
        TYPE TEXT,
        FILE_NAME TEXT);'''
        conn.execute(sql) # shortcut for conn.cursor().execute(sql)
    else:
        print 'Schema exists\n'
    return conn

def insert_picture(picture_file):
    with open(picture_file, 'rb') as input_file:
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        ablob = input_file.read()
        base=os.path.basename(picture_file)
        afile, ext = os.path.splitext(base)
        sql = '''INSERT INTO PICTURES
        (PICTURE, TYPE, FILE_NAME)
        VALUES(?, ?, ?);'''
        c.execute(sql,[sqlite3.Binary(ablob), ext, afile]) 
        conn.commit()

def loadimages(dbname, path):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    #conn.execute("DELETE FROM PICTURES")
    for fn in picture_list:
        picture_file = path+"/"+fn
        insert_picture(picture_file)

    for r in c.execute("SELECT rowid, FILE_NAME FROM PICTURES"):
        print r[0],r[1]
   
    conn.commit()


def get_image(picture_id):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute("SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = ?;",(picture_id,))
    #sql = "SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = 19"
    param = {'id': picture_id}
    #c.execute(sql, param)
    ablob, ext, afile = c.fetchone()
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    return filename


dbname = "ImageB.db"
db_file = create_or_open_db(dbname)
path = "snippets/"
loadimages(dbname, path)
filename = get_image(16)
print filename
Image(filename=filename)


import sqlite3
import os.path
from os import listdir, getcwd
from IPython.core.display import Image 

def get_picture_list(rel_path):
    abs_path = os.path.join(os.getcwd(),rel_path)
    print 'abs_path =', abs_path
    dir_files = os.listdir(abs_path)
    #print dir_files
    return dir_files

picture_list = get_picture_list('snippet')
print picture_list
import sqlite3
import os.path
from os import listdir, getcwd
from IPython.core.display import Image 

def create_or_open_db(db_file):
    db_is_new = not os.path.exists(db_file)
    conn = sqlite3.connect(db_file)
    if db_is_new:
        print 'Creating schema'
        sql = '''create table if not exists PICTURES(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PICTURE BLOB,
        TYPE TEXT,
        FILE_NAME TEXT);'''
        conn.execute(sql) # shortcut for conn.cursor().execute(sql)
    else:
        print 'Schema exists\n'
    return conn

def insert_picture(picture_file):
    with open(picture_file, 'rb') as input_file:
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        ablob = input_file.read()
        base=os.path.basename(picture_file)
        afile, ext = os.path.splitext(base)
        sql = '''INSERT INTO PICTURES
        (PICTURE, TYPE, FILE_NAME)
        VALUES(?, ?, ?);'''
        c.execute(sql,[sqlite3.Binary(ablob), ext, afile]) 
        conn.commit()

def loadimages(dbname, path):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    #conn.execute("DELETE FROM PICTURES")
    for fn in picture_list:
        picture_file = path+"/"+fn
        insert_picture(picture_file)

    for r in c.execute("SELECT rowid, FILE_NAME FROM PICTURES"):
        print r[0],r[1]
   
    conn.commit()


def get_image(picture_id):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute("SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = ?;",(picture_id,))
    #sql = "SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = 19"
    param = {'id': picture_id}
    #c.execute(sql, param)
    ablob, ext, afile = c.fetchone()
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    return filename


dbname = "ImageF.db"
db_file = create_or_open_db(dbname)
path = "snippet/"
loadimages(dbname, path)
filename = get_image(16)
print filename
Image(filename=filename)

%%writefile Image2Data.py
import sqlite3
import os.path
from os import listdir, getcwd
from IPython.core.display import Image 

def get_picture_list(rel_path):
    abs_path = os.path.join(os.getcwd(),rel_path)
    print 'abs_path =', abs_path
    dir_files = os.listdir(abs_path)
    return dir_files

def create_or_open_db(dbname):
    db_is_new = not os.path.exists(db_file)
    conn = sqlite3.connect(db_file)
    if db_is_new:
        print 'Creating schema'
        sql = '''create table if not exists PICTURES(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PICTURE BLOB,
        TYPE TEXT,
        FILE_NAME TEXT);'''
        conn.execute(sql) # shortcut for conn.cursor().execute(sql)
    else:
        print 'Schema exists\n'
        conn.commit()
        conn.close()
    return conn

def insert_picture(dbname, picture_file):
    with open(picture_file, 'rb') as input_file:
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        ablob = input_file.read()
        base=os.path.basename(picture_file)
        afile, ext = os.path.splitext(base)
        sql = '''INSERT INTO PICTURES
        (PICTURE, TYPE, FILE_NAME)
        VALUES(?, ?, ?);'''
        c.execute(sql,[sqlite3.Binary(ablob), ext, afile]) 
        conn.commit()

def loadimages(dbname, path):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    #conn.execute("DELETE FROM PICTURES")
    for fn in picture_list:
        picture_file = path+"/"+fn
        insert_picture(picture_file)

    for r in c.execute("SELECT rowid, FILE_NAME FROM PICTURES"):
        print r[0],r[1]
   
    conn.commit()
    conn.close()

def image_id(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    rows = c.execute("SELECT rowid, TYPE, FILE_NAME FROM PICTURES")
    for row in rows:
        print row[0],row[2]+row[1]    
    return
    
def get_image(dbname,picture_id):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute("SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = ?;",(picture_id,))
    #sql = "SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = 19"
    param = {'id': picture_id}
    #c.execute(sql, param)
    ablob, ext, afile = c.fetchone()
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    return filename


!rm Image2Data.pyc

import Image2Data
picture_list = Image2Data.get_picture_list('snippet')
print picture_list

import Image2Data
dbname = "ImageD.db"
Image2Data.create_or_open_db(dbname)

import Image2Data
dbname = "ImageD.db"
picture_file = "01.jpg"
Image2Data.insert_picture(dbname, picture_file)

import Image2Data
dbname = "ImageF.db"
path = "snippet"
loadimages(dbname, path)

import Image2Data
dbname = "ImageD.db"
Image2Data.image_id(dbname)

def image_id(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    rows = c.execute("SELECT rowid, TYPE, FILE_NAME FROM PICTURES")
    for row in rows:
        print row[0],row[2]+row[1]
    

dbname = "ImageF.db"
image_id(dbname)

import Image2Data
dbname = "ImageF.db"
filename = Image2Data.get_image(dbname,61)
print filename
Image(filename=filename)


%%writefile Image2SQLite.py
import sqlite3
import os.path
from os import listdir, getcwd
from IPython.core.display import Image 

def getImage_list(rel_path):
    abs_path = os.path.join(os.getcwd(),rel_path)
    print 'abs_path =', abs_path
    dir_files = os.listdir(abs_path)
    return dir_files

def create_or_open_db(dbname):
    db_is_new = not os.path.exists(db_file)
    conn = sqlite3.connect(db_file)
    if db_is_new:
        print 'Creating schema'
        sql = '''create table if not exists images(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        image BLOB,
        TYPE TEXT,
        imagE TEXT);'''
        conn.execute(sql) # shortcut for conn.cursor().execute(sql)
    else:
        print 'Schema exists\n'
        conn.commit()
        conn.close()
    return conn

def insertImage(dbname, imageFile):
    with open(imageFile, 'rb') as input_file:
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        ablob = input_file.read()
        base=os.path.basename(imageFile)
        afile, ext = os.path.splitext(base)
        sql = '''INSERT INTO images
        (image, TYPE, imagE)
        VALUES(?, ?, ?);'''
        c.execute(sql,[sqlite3.Binary(ablob), ext, afile]) 
        conn.commit()

def loadimagE(dbname, path):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    #conn.execute("DELETE FROM images")
    for fn in image_list:
        imageFile = path+"/"+fn
        insertImage(imageFile)

    for r in c.execute("SELECT rowid, imagE FROM images"):
        print r[0],r[1]
   
    conn.commit()
    conn.close()

def image_id(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    rows = c.execute("SELECT rowid, TYPE, imagE FROM images")
    for row in rows:
        print row[0],row[2]+row[1]    
    return
    
def get_image(dbname,image_id):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute("SELECT image, TYPE, imagE FROM images WHERE id = ?;",(image_id,))
    #sql = "SELECT image, TYPE, imagE FROM images WHERE id = 19"
    param = {'id': image_id}
    #c.execute(sql, param)
    ablob, ext, afile = c.fetchone()
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    return filename


import sqlite3
conn = sqlite3.connect('bigfeedfts.db')
c = conn.cursor()
c.execute('''select * from sqlite_master''')
l = c.fetchall()
tbl_name_list = []
for sql_type, sql_name, tbl_name, rootpage, sql in l:
    if sql_type == 'table':
        tbl_name_list.append(sql_name)
        print tbl_name_list

import sqlite3
conn = sqlite3.connect('bigfeedfts.db')
c = conn.execute('select * from bbctech')
print "Number of Fields : ",len(c.description), \
"\nField Names      : ", [i[0] for i in c.description]

import sqlite3
conn = sqlite3.connect('bigfeedfts.db')
c = conn.execute('select * from bbctech')
print [i[0] for i in c.description]

num_fields = len(cursor.description)
field_names = [i[0] for i in cursor.description]

import sqlite3
from time import sleep
conn = sqlite3.connect('XPfts4.db')
c = conn.cursor()
rows = c.execute('SELECT code FROM pages')
for row in rows:
    sleep(1)
    print str(row)


!xset led on

import sqlite3
from time import sleep
conn = sqlite3.connect('XPfts4.db')
conn.text_factory = str
c = conn.cursor()

rows = c.execute('select rowid, pages_content from pages')
for row in rows:
    row=str(row)
    #row = row.encode("ascii", "ignore")
    #row = row.encode('utf-8').strip()
    
    sleep(1)
    print row


def dbstore(insert):
    import sqlite3
    conn = sqlite3.connect('XPfts4.db')
    c = conn.cursor()
    c.execute("CREATE VIRTUAL TABLE IF NOT EXISTS code USING FTS3(code);\n    ""\n    )\n    
    c = conn.cursor()
    conn.text_factory = str
    # CREATE VIRTUAL TABLE pages USING fts4(code);\n    
              c.execute("INSERT INTO pages VALUES(?)", (insert,))              
              conn.commit()
              conn.close()
              return

def dbread():
    import sqlite3
    conn = sqlite3.connect('XPfts4.db')
    c = conn.cursor()
    req = 100
    view = raw_input("Search : ")
    for row in c.execute('SELECT rowid, code FROM pages WHERE pages MATCH ?', (view,)):
    count=count+1
    print (row)[0],"-",(row)[1],"\n"
    if count > req:
              conn.close()
              sys.exit()
              return


import DBread
DBread.dbread()

import Image2SQLite
rel_path='snippets'
Image2SQLite.getImage_list(rel_path)

import Image2SQLite
Image2SQLite.image_id(dbname)

import sqlite3        
import feedparser
import time
import sqlite3
Dbase = 'BookOfEnochGOOD.db'
conn = sqlite3.connect(Dbase)
conn.text_factory = str
c = conn.cursor()
c.execute('''
CREATE VIRTUAL TABLE IF NOT EXISTS pdfs
USING FTS3(text, title);
''')

title = "BookOfEnochGOOD"
#text = wikipedia.summary("Heaven")
#text = text.encode("ascii", "ignore")
#text = text.replace(". ",". \n")
conn = sqlite3.connect(Dbase)
c = conn.cursor()
reaD = open("BookOfEnochGOOD.txt","r")
lines = reaD.readlines()
for line in lines:
    line = line.decode("utf8")
    c.execute("INSERT INTO pdfs  VALUES (?, ?)", (line, title))
    conn.commit()
conn.close()

import Txmanip
help(Txmanip)

from time import sleep
import textract
#lines = textract.process("/home/jack/Desktop/Books/Web-Scraping-With-Python.pdf")
#lines = textract.process("/home/jack/Desktop/Books/Automate-the-Boring-Stuff-with-Python.pdf")
#lines = textract.process("/home/jack/Desktop/Books/Python_Cookbook_3rd_Edition.pdf")
#lines = textract.process("/home/jack/Desktop/Books/Effective_Python.pdf")
#lines = textract.process("/home/jack/Desktop/Books/IPythonInteractiveComputingandVisualizationCookbook.pdf")
#lines = textract.process("BookOfEnoch.pdf")
lines = textract.process("astral.pdf")
for line in lines.split("."):
    #line = line.replace(".",".\n")
    line = line.replace("	"," ")
    Tfile = open("astral.txt","a")
   
    Tfile.write(line)
    #print line
    Tfile.close()


 They indicate that, 900 million years ago, the day was only about 18.2 hours long.
    The history of life on Earth began about 3.8 billion years ago, initially with single-celled prokaryotic cells, such as bacteria.

from Txmanip import RemoveBlank
origFile = "astral.txt"
saveAS = "astralGOOD.txt"
RemoveBlank.removeblank(origFile, saveAS)

import sqlite3
import sys
conn = sqlite3.connect('BookOfEnochGOOD.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
search = raw_input("Search : ")
for row in c.execute('SELECT rowid, text FROM pdfs WHERE text MATCH ?', (search,)):    
    count=count+1
    print (row)[0],"-",(row)[1],
    if count > req:
        conn.close()
        sys.exit()

# The Book Starts At 212
import sqlite3
import sys
conn = sqlite3.connect('BookOfEnochGOOD.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
id1 = raw_input("Starting ID : ")
id2 = raw_input("How Many Rows : ")

#for row in c.execute('Select rowid, * from pdfs LIMIT ?,?', (id1, id2)):
#for row in c.execute('Select rowid, * from pdfs LIMIT ?,?', (id1, id2)):
for row in c.execute('SELECT rowid, * from pdfs LIMIT ? OFFSET ?',  (id2, id1)):
    count=count+1
    print (row)[0],"-",(row)[1],
    if count > req:
        conn.close()
        sys.exit()

!wget https://media.readthedocs.org/pdf/astral/latest/astral.pdf

#################################################################################
# http://sherrytowers.com/2014/04/13/archeoastronomy-where-on-the-horizon-do-the-stars-sun-moon-rise-and-set-part-ii/
# A python script to calculate the declinations for past years for
# all the stars in the pyephem star catalog, from 5000BC to present in 
# increments of 50 years.
# To run the script type
#    python ./stars_print_out_ra_and_dec.py
# the script will output the file stars_print_out_ra_and_dec.out
#
# http://www.sherrytowers.com/stars.py
#
# Author: Sherry Towers
#         smtowers _at_ asu.edu
# Created: Dec 2nd, 2013
#
# Copyright Sherry Towers, 2013, 2014
#
# This script is not guaranteed to be free of bugs and/or errors.
#
# This script can be freely used and shared as long as the author and
# copyright information in this header remain intact.
##################################################################################
import ephem
global star
import ephem.stars
from ephem import *
messierdb = 'Messier.edb'
from math import pi

temp = ephem.Observer()
temp.elevation = 0

hyades = ephem.FixedBody()
hyades._ra = '4:27:0.0'
hyades._dec = '15:52:00.0'
hyades._pmra = 0.0
hyades._pmdec = 0.0
hyades.name = 'Hyades'
# NB: proper motion could be obtained from Gamma Tauri

SN1006 = ephem.FixedBody()
SN1006._ra = '15:2:8.0'
SN1006._dec = '-41:57:00.0'
SN1006._pmra = 0.0
SN1006._pmdec = 0.0
SN1006.name = 'SN1006'
SN1054 = ephem.FixedBody()
SN1054._ra = '5:34:20.0'
SN1054._dec = '22:01:00.0'
SN1054._pmra = 0.0
SN1054._pmdec = 0.0
SN1054.name = 'SN1054'

##################################################################################
# the Sun, plus the list of stars from
# http://github.com/brandon-rhodes/pyephem/blob/master/src/ephem/stars.py
##################################################################################
sirius  = ephem.star('Sirius')
canopus = ephem.star('Canopus')
arcturus = ephem.star('Arcturus')
vega = ephem.star('Vega')
rigel = ephem.star('Rigel')
procyon = ephem.star('Procyon')
betelgeuse = ephem.star('Betelgeuse')
capella = ephem.star('Capella')
altair = ephem.star('Altair')
aldebaran = ephem.star('Aldebaran')
spica = ephem.star('Spica')
antares = ephem.star('Antares')
pollux = ephem.star('Pollux')
fomalhaut = ephem.star('Fomalhaut')
deneb = ephem.star('Deneb')
regulus = ephem.star('Regulus')
pleiades = ephem.star('Alcyone')
alnitak = ephem.star('Alnitak')
alnilam = ephem.star('Alnilam')
mintaka = ephem.star('Mintaka')
eta_orionis = ephem.star('Saiph')
menkar = ephem.star('Menkar')
bellatrix = ephem.star('Bellatrix')
elnath = ephem.star('Elnath')
shaula = ephem.star('Shaula')
adara = ephem.star('Adara')
alnair = ephem.star('Alnair')
wezen = ephem.star('Wezen')
alhena = ephem.star('Alhena')
castor = ephem.star('Castor')
mirzam = ephem.star('Mirzam')
alphard = ephem.star('Alphard')
sirrah = ephem.star('Sirrah')
caph = ephem.star('Caph')
algenib = ephem.star('Algenib')
schedar = ephem.star('Schedar')
mirach = ephem.star('Mirach')
achernar = ephem.star('Achernar')
almach = ephem.star('Almach')
hamal = ephem.star('Hamal')
polaris = ephem.star('Polaris')
algol = ephem.star('Algol')
electra = ephem.star('Electra')
taygeta = ephem.star('Taygeta')
maia = ephem.star('Maia')
merope = ephem.star('Merope')
alcyone = ephem.star('Alcyone')
atlas = ephem.star('Atlas')
zaurak = ephem.star('Zaurak')
nihal = ephem.star('Nihal')
arneb = ephem.star('Arneb')
menkalinan = ephem.star('Menkalinan')
naos = ephem.star('Naos')
algieba = ephem.star('Algieba')
merak = ephem.star('Merak')
dubhe = ephem.star('Dubhe')
denebola = ephem.star('Denebola')
phecda = ephem.star('Phecda')
minkar = ephem.star('Minkar')
megrez = ephem.star('Megrez')
gienah = ephem.star('Gienah Corvi')
mimosa = ephem.star('Mimosa')
alioth = ephem.star('Alioth')
vindemiatrix = ephem.star('Vindemiatrix')
mizar = ephem.star('Mizar')
alcor = ephem.star('Alcor')
alcaid = ephem.star('Alcaid')
agena = ephem.star('Agena')
thuban = ephem.star('Thuban')
izar = ephem.star('Izar')
kochab = ephem.star('Kochab')
alphecca = ephem.star('Alphecca')
unukalhai = ephem.star('Unukalhai')
rasalgethi = ephem.star('Rasalgethi')
cebalrai = ephem.star('Cebalrai')
etamin = ephem.star('Etamin')
kaus_australis = ephem.star('Kaus Australis')
sheliak = ephem.star('Sheliak')
nunki = ephem.star('Nunki')
sulafat = ephem.star('Sulafat')
arkab_prior = ephem.star('Arkab Prior')
arkab_posterior = ephem.star('Arkab Posterior')
rukbat = ephem.star('Rukbat')
albereo = ephem.star('Albereo')
tarazed = ephem.star('Tarazed')
alshain = ephem.star('Alshain')
sadr = ephem.star('Sadr')
peacock = ephem.star('Peacock')
alderamin = ephem.star('Alderamin')
alfirk = ephem.star('Alfirk')
enif = ephem.star('Enif')
sadalmelik = ephem.star('Sadalmelik')
scheat = ephem.star('Scheat')
markab = ephem.star('Markab')

##################################################################################
# now loop over the locations and dates and calculate the rise/set azimuths
##################################################################################
aname = "stars_print_out_ra_and_dec.out"
f=open(aname,'w')
f.write('epoch,star,RA,DEC,prop_RA,prop_DEC,mag\n')
for lat in range(0,1,1):
 temp.lon = "00:00:00.00"
 temp.lat = str(lat)+":00:00.00"
 lat = 180*float(temp.lat)/pi
 temp.elevation = 0
 for year in range(-5000,2051,50):
 # http://earthsky.org/brightest-stars/thuban-past-north-star
 #for year in range(-2787,-2786,1): # check Thuban... it is north star 2787BC
 #for year in range(2000,2001,1): # check Thuban... it is north star 2787BC
  for istar in range(1,98,1):
  #for istar in range(70,71,1):
    if istar==1: mystar=hyades
    if istar==2: mystar=sirius
    if istar==3: mystar=canopus
    if istar==4: mystar=arcturus
    if istar==5: mystar=vega
    if istar==6: mystar=rigel
    if istar==7: mystar=procyon
    if istar==8: mystar=betelgeuse
    if istar==9: mystar=capella
    if istar==10: mystar=altair
    if istar==11: mystar=aldebaran
    if istar==12: mystar=spica
    if istar==13: mystar=antares
    if istar==14: mystar=pollux 
    if istar==15: mystar=fomalhaut
    if istar==16: mystar=deneb
    if istar==17: mystar=regulus
    if istar==18: mystar=pleiades
    if istar==19: mystar=alnitak
    if istar==20: mystar=alnilam
    if istar==21: mystar=mintaka
    if istar==22: mystar=eta_orionis
    if istar==23: mystar=menkar
    if istar==24: mystar=bellatrix
    if istar==25: mystar=elnath
    if istar==26: mystar=shaula
    if istar==27: mystar=adara 
    if istar==28: mystar=alnair
    if istar==29: mystar=wezen 
    if istar==30: mystar=alhena
    if istar==31: mystar=castor
    if istar==32: mystar=mirzam
    if istar==33: mystar=alphard
    if istar==34: mystar=sirrah
    if istar==35: mystar=caph
    if istar==36: mystar=algenib
    if istar==37: mystar=schedar
    if istar==38: mystar=mirach
    if istar==39: mystar=achernar
    if istar==40: mystar=almach
    if istar==41: mystar=hamal
    if istar==42: mystar=polaris
    if istar==43: mystar=algol
    if istar==44: mystar=electra
    if istar==45: mystar=taygeta
    if istar==46: mystar=maia
    if istar==47: mystar=merope
    if istar==48: mystar=alcyone
    if istar==49: mystar=atlas
    if istar==50: mystar=zaurak
    if istar==51: mystar=nihal
    if istar==52: mystar=arneb
    if istar==53: mystar=menkalinan
    if istar==54: mystar=naos
    if istar==55: mystar=algieba
    if istar==56: mystar=merak
    if istar==57: mystar=dubhe
    if istar==58: mystar=denebola
    if istar==59: mystar=phecda
    if istar==60: mystar=minkar
    if istar==61: mystar=megrez
    if istar==62: mystar=gienah 
    if istar==63: mystar=mimosa 
    if istar==64: mystar=alioth 
    if istar==65: mystar=vindemiatrix 
    if istar==66: mystar=mizar 
    if istar==67: mystar=alcor 
    if istar==68: mystar=alcaid
    if istar==69: mystar=agena
    if istar==70: mystar=thuban
    if istar==71: mystar=izar
    if istar==72: mystar=kochab
    if istar==73: mystar=alphecca
    if istar==74: mystar=unukalhai
    if istar==75: mystar=rasalgethi
    if istar==76: mystar=cebalrai
    if istar==77: mystar=etamin
    if istar==78: mystar=kaus_australis
    if istar==79: mystar=sheliak
    if istar==80: mystar=nunki
    if istar==81: mystar=sulafat
    if istar==82: mystar=arkab_prior
    if istar==83: mystar=arkab_posterior
    if istar==84: mystar=rukbat
    if istar==85: mystar=albereo
    if istar==86: mystar=tarazed
    if istar==87: mystar=alshain
    if istar==88: mystar=sadr
    if istar==89: mystar=peacock
    if istar==90: mystar=alderamin
    if istar==91: mystar=alfirk
    if istar==92: mystar=enif
    if istar==93: mystar=sadalmelik
    if istar==94: mystar=scheat
    if istar==95: mystar=markab
    if istar==96: mystar=SN1006
    if istar==97: mystar=SN1054

    myname = str(mystar.name)
    if (istar==18): myname='Pleiades'
    lgood=0
    adate = str(year)+'/6/21'
    a = ephem.date(adate)
    mystar.compute(a,epoch=str(year))
    #print 'istar is '+str(istar)+' '+myname
    if istar!=1:
     if istar!=18:
       if istar<96:
        mag = float(mystar.mag)
       b=1
     b=1
    b=1
    if (istar==1): mag=0.5    # hyades
    if (istar==18): mag=1.6   # pleiades
    if (istar==96): mag= -7.5 # SN1006
    if (istar==97): mag= -6   # SN1054
    #print str(mag)
    
    ########################################################
    ########################################################
    f.write(str(year)+','+myname+","+str((180/pi)*float(mystar.a_ra))+','+str((180.0/pi)*float(mystar.a_dec))+","+str(float(mystar._pmra))+","+str(float(mystar._pmdec))+","+str(mag)+'\n')
  b=1
 b=1 
f.close()
b=1


import SatInfo
SatInfo.prntlist()


import glob
import os
for f in glob.glob("Wiki_*.txt"):
    os.system("cat "+f+" >> ALL_WIKI.txt")

fname = raw_input("Enter file name: ")
num_words = 0
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print "Number of words: ",num_words

from Txmanip import RemoveBlank
origFile = "ALL_WIKI.txt"
saveAS = "ALL_WIKI_GOOD.txt"
RemoveBlank.removeblank(origFile, saveAS)

!ls *.txt

# %load SearchFilename.py
'''
Search a filename for a phrase and how many following lines to display
USAGE:
import SearchFilename
filename = "hek.txt"
length = 4
SearchFilename.searchfilename(filename, length)
'''
def searchfilename(filename, length):
    f = open(filename, "r")
    searchlines = f.readlines()
    f.close()
    search = str(raw_input("Search Phrase : "))
    for i, line in enumerate(searchlines):
        if search in line: 
            for l in searchlines[i:i+length]: print l,
            print
            
#USAGE:
import SearchFilename
filename = "ALL_WIKI_GOOD.txt"
# length = how many lines after
length = 7
SearchFilename.searchfilename(filename, length) 




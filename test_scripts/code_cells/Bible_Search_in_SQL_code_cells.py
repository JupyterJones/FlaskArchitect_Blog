import sqlite3
conn = sqlite3.connect('data/biblenum.db')
c = conn.cursor()
c.execute("""
CREATE VIRTUAL TABLE verse 
USING FTS3(scripture);
""")
conn.commit()
conn.close()

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
fname="bible2.txt"
file_len(fname)

import time
from itertools import islice

with open("bible2.txt") as biblelines:
    heads = list(islice(biblelines, 31102))
    for head in heads:
        print head


select rowid,* from verse

import sqlite3
import sys
conn = sqlite3.connect('data/biblenum.db')
c = conn.cursor()# Never 
count=0
req=4
def remove_cruft(s):
    return s[5:-4]
for row in c.execute('SELECT rowid,* FROM verse WHERE scripture MATCH "beginning"'):
    count=count+1
    print(row)
    if count > req:
        conn.close()
        sys.exit()

import sqlite3
import sys
#conn = sqlite3.connect('data/bible.db')
conn = sqlite3.connect('data/biblenum.db')
c = conn.cursor()
count=0
req=100
for row in c.execute('SELECT rowid,* FROM verse WHERE scripture MATCH "youngest"'):
    count=count+1
    print count,"Occurances : ","Verse Numbers :",(row)[0],"\n",(row)[1]
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
from itertools import islice
#conn = sqlite3.connect('hurricane.db')
#c = conn.cursor()
# Create table
#c.execute('''CREATE TABLE hurricane
#             (hurricane text, keywords text)''')
count=0#lines = 400
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
fname="bible2.txt"
num = file_len(fname)
with open(fname) as myfile:
    heads = list(islice(myfile,31102))
    for head in heads:
        #head = list(islice(heads, 1))
        #time.sleep(.5)
        conn = sqlite3.connect('data/bible.db')
        c = conn.cursor()
        #c.execute("INSERT INTO verse VALUES (?)", (head)) 
        conn.commit()
        conn.close()        
        #time.sleep(.5)
        print head
        count=count+1
        print count
        #if count>lines:




import re
import textwrap
import time
import sqlite3
import sys
import base64
import time
from itertools import islice
count=1
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
fname="bible2.txt"
num = file_len(fname)
with open(fname) as myfile:
    heads = list(islice(myfile,31102))
    for head in heads:
        textin = head
        conn = sqlite3.connect('data/biblenum.db')
        c = conn.cursor()
        c.execute("INSERT INTO verse VALUES (?)", (textin,)) 
        conn.commit()
        conn.close()        
        #time.sleep(.5)
        print textin
        count=count+1
        print count
        #if count>lines:


import re
import textwrap
import time
import sqlite3
import sys
import base64
import time
from itertools import islice
#conn = sqlite3.connect('hurricane.db')
#c = conn.cursor()
# Create table
#c.execute('''CREATE TABLE hurricane
#             (hurricane text, keywords text)''')
count=1
#lines = 400
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
fname="bible2.txt"
num = file_len(fname)
with open(fname) as myfile:
    heads = list(islice(myfile,31102))
    for head in heads:
        #head = list(islice(heads, 1))
        #time.sleep(.5)
        
        textin = count,",",head
        conn = sqlite3.connect('data/biblenum.db')
        c = conn.cursor()
        c.execute("INSERT INTO verse VALUES (?)", (textin,)) 
        conn.commit()
        conn.close()        
        #time.sleep(.5)
        print textin
        count=count+1
        print count
        #if count>lines:


import re
import textwrap
import time
import sqlite3
import sys
import base64
import time
from itertools import islice
#conn = sqlite3.connect('hurricane.db')
#c = conn.cursor()
# Create table
#c.execute('''CREATE TABLE hurricane
#             (hurricane text, keywords text)''')
count=0#lines = 400
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
fname="bible2.txt"
num = file_len(fname)
with open(fname) as myfile:
    heads = list(islice(myfile,31102))
    for head in heads:
        #head = list(islice(heads, 1))
        #time.sleep(.5)
        conn = sqlite3.connect('data/bible.db')
        c = conn.cursor()
        #c.execute("INSERT INTO verse VALUES (?)", (head)) 
        conn.commit()
        conn.close()        
        #time.sleep(.5)
        print head
        count=count+1
        print count
        #if count>lines:


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
#lines = 400

with open("bible2.txt") as myfile:
    for head in heads:
        head = [next(myfile) for x in xrange(1)]
        time.sleep(1)
        conn = sqlite3.connect('data/bible.db')
        c = conn.cursor()
        c.execute("INSERT INTO verse VALUES (?)", (head)) 
        conn.commit()
        conn.close()        
        time.sleep(1)
        print head
        count=count+1
        print count
        #if count>lines:
            
#commits and closes database if there are less then 400 lines of text
conn.commit()
conn.close() 
sys.exit()

import re
import textwrap
import time
import sqlite3
import sys
import base64
import time
from itertools import islice
#conn = sqlite3.connect('hurricane.db')
#c = conn.cursor()
# Create table
#c.execute('''CREATE TABLE hurricane
#             (hurricane text, keywords text)''')
count=0
#lines = 400
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


fname="bible2.txt"
num =file_len(fname)




with open("bible2.txt") as myfile:
    heads = list(islice(myfile,1000))
    for head in heads:
        head = list(islice(myfile, 1))
        time.sleep(1)
        conn = sqlite3.connect('data/bible.db')
        c = conn.cursor()
        c.execute("INSERT INTO verse VALUES (?)", (head)) 
        conn.commit()
        conn.close()        
        time.sleep(1)
        print head
        count=count+1
        print count
        #if count>lines:


---------------------------------------------------

---------------------------------------------------

---------------------------------------------------

import sqlite3
def insert_info(tweet):
    with sqlite3.connect("data/twitter.db") as db:
        cursor = db.cursor()
        sql = "insert into twitter (twittername,twitterid,keywords) values (?, ?, ?)"
        cursor.execute(sql, tweet)
        db.commit()

#if __name__ == "__main__":
print "You will be promted to enter TwitterName, TwitterID Number, and Keywords  "  
twittername = raw_input("Enter Twitter Name: >>")
twitterid = raw_input("Enter Twitter Number: >>")
keywords = raw_input("Enter Keywords: >>")
tweet = (twittername,twitterid,keywords)
insert_info(tweet)

import sqlite3
conn = sqlite3.connect('data/twitter.db')
c = conn.cursor()# Never do this -- insecure!

#t = ('Hurricane',)
#c.execute('SELECT * FROM twitter ORDER BY keywords')
#print(c.fetchall())
#conn.close()

for row in c.execute('SELECT * FROM twitter ORDER BY contact_id'):
        #print(row),"\n-----\n","\n"
        
        print row[0],"  ",row[1],"  ",row[2],"  ",row[3],"\n-----\n",

conn.close()


import sqlite3
conn = sqlite3.connect('data/bible3.db')
c = conn.cursor()
c.execute("""
CREATE VIRTUAL TABLE verse 
USING FTS3(text);
""")
conn.commit()
conn.close()

import time
with open("bible2.txt") as myfile:
    for head in heads:
        head = [next(myfile) for x in xrange(1)]
        time.sleep(1)
        print head

import sqlite3
import sys
conn = sqlite3.connect('data/bible3.db')
c = conn.cursor()# Never 
count=0
req=100
for row in c.execute('SELECT * FROM verse'):
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
#lines = 400

with open("bible2.txt") as myfile:
    for head in heads:
        head = [next(myfile) for x in xrange(1)]
        time.sleep(1)
 
        conn = sqlite3.connect('data/bible3.db')
        c = conn.cursor()
        time.sleep(1)
        #encodedlistvalue=base64.b64encode(file[2:-2])
        #c.execute("INSERT INTO hurricane VALUES (?,?)", (encodedlistvalue, b)) 
        c.execute("INSERT INTO verse VALUES (?)", (head)) 
        conn.commit()
        conn.close()        
        time.sleep(1)
        print head
        count=count+1
        print count
        #if count>lines:
            
#commits and closes database if there are less then 400 lines of text
conn.commit()
conn.close() 
sys.exit()

%%writefile record.py
#!/usr/bin/python2.7
#########################################################
#### PyRecordDesktop 0.1
#### By Bogdan Milanovic
####
#### In the absence of a decent linux application that
#### records a desktop into a video (and no, the
#### recordMyDesktop does not qualify as one), I have 
#### decided to write my own.
####
#### PyRecordDesktop uses ffmpeg (which most distros come
#### installed with) to capture the video and encode it
#### on the fly. It also uses ALSA to capture the sound
#### from any input devices (such as a microphone). 
#### A Qt powered GUI is planned.
#########################################################

import subprocess
import sys
import argparse
import shlex
import os

#First we define the default values of the main parameters
DEFAULT_RESOLUTION = "1280x720"
DEFAULT_CODEC = "h264"
DEFAULT_OUTPUTFILE = "output.avi"

#Then we define tuples (immutable) of the supported formats and resolutions.
#Hopefully we'll be able to grab these values automatically in the future
RESOLUTION_LIST = ("1920x1080", "1366x768", "1280x720")
CODEC_LIST = ("mpeg4", "flv", "h264")

#Parsing the arguments given in the command line
#These arguments include: output file, desired recording resolution, and the video encoding codec
parser = argparse.ArgumentParser()
parser.add_argument("outputfile", help="The output filename")
parser.add_argument("--res", help="Recording resolution: 1920x1080, 1366x768, or 1280x720")
parser.add_argument("--codec", help="Video encoding codec: libx264, mpeg4, flv, h264")
args = parser.parse_args()

#We check to make sure that the arguments have been passed 
#Otherwise we use the default values  as defined above
resolution = args.res if args.res else DEFAULT_RESOLUTION
codec = args.codec if args.codec else DEFAULT_CODEC
outputfile = args.outputfile if args.outputfile else DEFAULT_OUTPUTFILE

#A couple of checks to make sure the resolution and the codec are valid
if resolution not in RESOLUTION_LIST:
	print "Invalid resolution. Run {0} -h for details".format(__file__)
	sys.exit(1)

if codec not in CODEC_LIST:
	print "Invalid codec. Run {0} -h for details".format(__file__)
	sys.exit(1)

#The command string that we'll execute. LOTS of manipulation here available!
command = """ffmpeg -f x11grab -y -r 30 -s {0} -i :0.0 -vcodec {1} -qscale 0 -f alsa -i default -ar 44100 -acodec libmp3lame -ac 2 {2}""".format(resolution, codec, args.outputfile)

#print command

arguments = shlex.split(command)

#Finally, we call the command and start recording (naturally within try/except clause)
try:
	process = subprocess.Popen(arguments)
	process.communicate()[0]
except KeyboardInterrupt:
	process.kill()
	print "\r\n"
	print "The file has been saved to {0}".format(os.path.abspath(args.outputfile))
	print "Goodbye!"	
	sys.exit(0)
except Exception, e:
	print "Something went wrong when we tried to start the recording!"
	print "The error is {0}".format(str(e))
	sys.exit(2)



!python record.py output.avi --res 1280x720 --codec h264

--res 1920x1080 - the resolution to record in
 --codec h264 - the codec to encode in
 
 Run the --help argument for more info.


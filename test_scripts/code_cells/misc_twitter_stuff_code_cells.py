import time
help(time.time)

import sys
sys.path.insert(0,"/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
import Key
CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]
t=0
sTime= time.time()
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,ACCESS_SECRET)
tweetfile = 'Python.txt'
results = twitter.cursor(twitter.search, q='python, javascript')
filein = open(tweetfile, 'w')
for result in results:
    result=str(result)
    filein.write(result)
    print(result)
    if time.time() - sTime > 4:
        filein.close()
        sys.exit()
         

for i in range(4):
    print("--%d" % i)
    for i in range(5):
        print(i),

import sys
sys.path.insert(0,"/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
import Key
import time
CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]
t=0
sTime= time.time()
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,ACCESS_SECRET)
tweetfile = 'Trump001.txt'
results = twitter.cursor(twitter.search, q='Trump')
filein = open(tweetfile, 'w')
for result in results:
    result=str(result)
    filein.write(result)
    print(result)
    if time.time() - sTime > 5:
        filein.close()
        sys.exit()

from TwitterSearch import *
import Key
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['Hurricane', 'Florida']) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = Key.twiter()[0],
        consumer_secret = Key.twiter()[1],
        access_token = Key.twiter()[2],
        access_token_secret = Key.twiter()[3]
        )

     # this is where the fun actually starts :)
        
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)

!ls T*

import sys
sys.path.insert(0, 'TwitterSearch/')
from TwitterSearch import *


import sys
sys.path.insert(0, 'TwitterSearch/')
from TwitterSearch import *
import Key
consumer_key = Key.twiter()[0]
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['Typhoon', 'China']) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information
    tso.set_count(2)
    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = Key.twiter()[0],
        consumer_secret = Key.twiter()[1],
        access_token = Key.twiter()[2],
        access_token_secret = Key.twiter()[3]
        )

     # this is where the fun actually starts :)
    text2 = []    
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)

from TwitterSearch import *
import Key
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['jupyternotebook', 'python']) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = Key.twiter()[0],
        consumer_secret = Key.twiter()[1],
        access_token = Key.twiter()[2],
        access_token_secret = Key.twiter()[3]
        )

    # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % (tweet['user']['screen_name'], tweet['text'] ) )
        
    



        #outfile = "test.csv"
        #csvfile = file(outfile, "w")
        #row = tweet['user']['screen_name'], tweet['text']  
        #csvwriter = csv.writer(csvfile)
        #row = tweet[ "user", "screen_name", "text" ]
        #csvwriter.writerow(row)
        #print (tweet['user']['screen_name'], tweet['text']  )
        #print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

import sys
sys.path.insert(0,"/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
import Key
import csv
CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,ACCESS_SECRET)
#tweetfile = 'hurricane_11.txt'
results = twitter.cursor(twitter.search, q='Trump')
 
for result in results:
    result = str(result)
    Ndata = result.replace(':', ' ')
    Xdata = Ndata.replace('u', '')

#newList = [l[0] for l in Ndata]
#Simple = ("".join(newList))
#print Simple

#print Xdata
    print str(Xdata)[2:-2]

import sys
sys.path.insert(0,"/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
import Key
import csv
CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,ACCESS_SECRET)
#tweetfile = 'hurricane_11.txt'
results = twitter.cursor(twitter.search, q='hurricane')
outfile = 'hurricane_101.txt'
csvfile = file(outfile, "w")
for result in results:
    post = (result)  
    csvwriter.write(post)
    print post
      
#file = open(“testfile.txt”,”w”) 
 
#file.write(“Hello World”)  


csvwriter = csv.writer(csvfile)

#-----------------------------------------------------------------------
# add headings to our CSV file
#-----------------------------------------------------------------------
#row = [ "user", "text", "latitude", "longitude" ]
#csvwriter.writerow(row)



with open('textText.data') as f:
    while True:
        c = f.read(1)
        print c,
        if not c:            
            print "End of file"
            sys.exit()
            
            


badtext = ''.join(c for c in map(chr, range(173)) if not c.isalnum())
print badtext


badtext = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
print badtext

for i in xrange(32, 128, 16):
    print 'chr:\t%s' % '\t'.join(map(chr, [i+j for j in range(16)]))
    print 'asc:\t%s' % '\t'.join(map(str, [i+j for j in range(16)]))

import re
import textwrap

with open("hurricane_14.txt") as f:
    text = f.read()
    #This was added to get ride od the unicode u from showing up
    words = text.replace(' u ', ' ');words = words.replace('u ', '');words = words.replace(' U ', ' ')
    #This clears out the non-Alpha-numeric characters
    #badtext = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
    badtext = '!,",#,$,%,&,(,),*,+,,-,.,/,:;<=>?@[\]^_`{|}~'
    word = words.translate(None, badtext)
    # limit the aount of characters perline displayed
    chars_per_line = 80
    for i in range(0, len(word), chars_per_line):
        print words[i:i+chars_per_line]

my_str = 'qwertyuiopaq'
','.join(my_str[i:i+4] for i in range(0, len(my_str), 4))


data = [('pragma integrity_check will check that your database is valid', 'check, verify, inspect'),]


import re
import textwrap
import sqlite3
import time
conn = sqlite3.connect('hurricane14.db')
c = conn.cursor()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

with open("hurricane_14.txt") as f:
    text = f.read()
    #This was added to get ride od the unicode u from showing up
    words = text.replace(' u ', ' ');words = words.replace('u ', '');words = words.replace(' U ', ' ')
    #This clears out the non-Alpha-numeric characters
    #badtext = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
    badtext = '!,",#,$,%,&,(,),*,+,,-,.,/,:;<=>?@[\]^_`{|}~'
    word = words.translate(None, badtext)
    # limit the aount of characters perline displayed
    chars_per_line = 100
    for i in range(0, len(word), chars_per_line):
        time.sleep(2)
        #data= "hurricane_14.txt)",words[i:i+chars_per_line],","
        data= "(",words[i:i+chars_per_line],"hurricane, florida, twitter)",
        #data= word[i:i+chars_per_line],
        #conn.commit()
        print data

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

conn.commit()
conn.close()  

data = [('pragma integrity_check will check that your database is valid', 'check, verify, inspect'),
             ('multiple items may be entered at once', 'newkey'),
             ('Save complete webpages - if posted in base64 encoding ', 'snippets, gwebsite, html'),]


import sqlite3
conn = sqlite3.connect('hurricane.db')
c = conn.cursor()
#Create table
c.execute('''CREATE TABLE hurricane
             (hurricane text, keywords text)''')
conn.commit()
conn.close()  

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
with open("/home/jack/Desktop/imagebot/hurricane_14.txt") as f:
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
        
        count=count+1
        print count,"\n",file[2:-2]
        if count>100:

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
with open("/home/jack/Desktop/imagebot/hurricane_14.txt") as f:
    text = f.read()
    words = " ".join(re.findall("[a-zA-Z]+", text))
    words = words.replace(' u ', ' ');words = words.replace('u ', '');words = words.replace(' U ', ' ')
    chars_per_line = 140
    for i in range(0, len(words), chars_per_line):
        file= ("[(",words[i:i+chars_per_line],"),]")
        #data= ("[('"+words[i:i+chars_per_line]+"'),]")
        file = str(file)
        time.sleep(1)
        count=count+1
        print count,"\n",file[2:-2]
        if count>10:

            sys.exit()
            

import sqlite3
import sys
conn = sqlite3.connect('hurricane.db')
c = conn.cursor()# Never 
count=0
start = 10
req= 25
for row in c.execute('SELECT * FROM hurricane'):
    count=count+1
    if count > start:
        print(row),"\n-----\n"
        if count > req:
            conn.close()
            sys.exit()


conn.commit()
conn.close()

import sqlite3
conn = sqlite3.connect('data/400.db')
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


import sqlite3
conn = sqlite3.connect('hurricane14.db')
c = conn.cursor()# Never 
for row in c.execute('SELECT * FROM hurricane'):
        print(row),"\n-----\n"
        conn.close()

import re
import textwrap

with open("hurricane_14.txt") as f:
    text = f.read()
    words = " ".join(re.findall("[a-zA-Z]+", text))
    words = words.replace(' u ', ' ');words = words.replace('u ', '');words = words.replace(' U ', ' ')
    print(textwrap.fill(words, 115))

import re
import textwrap

with open("hurricane_14.txt") as f:
    text = f.read()
    words = " ".join(re.findall("[a-zA-Z]+", text))
    words = words.replace(' u ', ' ');words = words.replace('u ', '');words = words.replace(' U ', ' ')
    print(textwrap.fill(words, 115))

import re
fil = open('textText.data', 'r')
st = fil.read
word1 = " ".join(re.findall("[a-zA-Z]+", st))

import time
with open('textText.data') as f:
    while True:
        c = f.read(1)
        if c == 'a' or 'b' or 'c' or 'd' or 'f' or 'g' or 'g' or 'i' or 'j':
            c = c
            print c,
            time.sleep(1)
            if not c:
                print c,
                print "End of file"
                break
            

%%writefile textText.data
{u'contributors': None, u'truncated': False, u'text': u'Good weather in Oklahoma but still praying for Texas and Florida\U0001f4af\U0001f4af\U0001f4af\U0001f4aa\U0001f4aa\U0001f4aa', u'is_quote_status': False, u'in_reply_to_status_id': None, u'id': 907747392098848770, u'favorite_count': 0, u'entities': {u'symbols': [], u'user_mentions': [], u'hashtags': [], u'urls': []}, u'retweeted': False, u'coordinates': None, u'source': u'<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>', u'in_reply_to_screen_name': None, u'in_reply_to_user_id': None, u'retweet_count': 0, u'id_str': u'907747392098848770', u'favorited': False, u'user': {u'follow_request_sent': False, u'has_extended_profile': True, u'profile_use_background_image': True, u'default_profile_image': False, u'id': 894407721935659008, u'profile_background_image_url_https': None, u'verified': False, u'translator_type': u'none', u'profile_text_color': u'333333', u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/894409739815333888/yAbwrfNx_normal.jpg', u'profile_sidebar_fill_color': u'DDEEF6', u'entities': {u'description': {u'urls': []}}, u'followers_count': 17, u'profile_sidebar_border_color': u'C0DEED', u'id_str': u'894407721935659008', u'profile_background_color': u'F5F8FA', u'listed_count': 0, u'is_translation_enabled': False, u'utc_offset': None, u'statuses_count': 4, u'description': u'Down to earth just a young nigga with goals and ambition to be something in life it just take time\U0001f4af\U0001f4aa\U0001f4aa', u'friends_count': 56, u'location': u'Muskogee, OK', u'profile_link_color': u'1DA1F2', 

import sys
sys.path.insert(0,"/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
import Key
CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]
t=0
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,ACCESS_SECRET)
tweetfile = 'hurricane_11.txt'
results = twitter.cursor(twitter.search, q='hurricane')
filein = open(tweetfile, 'w')
for result in results:
    result=str(result)
    filein.write(result)
    t=t+1
    if t=2:
        filein.close()
    print(result)    
    

import Key
CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]


print CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET


import Key
api = Key.twiter()[1]

CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]


print CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET


!rm Key.pyc

import twython
from twython import Twython
import random
import Key
CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
STR = (random.choice(list(open('psych.txt'))))
#video = open('video-unpublished/fractout.mp4', 'rb')
video = open('video-unpublished/steakdone.mp4', 'rb')
response = twitter.upload_video(media=video, media_type='video/mp4')
twitter.update_status(status=STR, media_ids=[response['media_id']])

import twython
from twython import Twython
import random
CONSUMER_KEY = 'YazCRIfWX4VICiRCOiph08jDL'
CONSUMER_SECRET = 'QOkLHou6NMwkghSHjMFXMdffQKJlDzttKtP6uBCcZ4VlQtvJyc'
ACCESS_KEY = '296906916-AWggjhqpEWIS7EzXXhc2pOPBeCVJczpOm11cQGIf'
ACCESS_SECRET = 'zFrCiyaPt8gCBVVs1bLCmdCSyQQ3DKxT5wHJq2tOu2AMj'
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
results = twitter.cursor(twitter.search, q='python')
for result in results:
    print result

import random
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageChops 
import os
import sys
import time
count = 0
while count < 180:
    path = r"/home/jack/Desktop/pycode/vpython2/TrigonometryBot/images/"
    base_image = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    filename0=(path+base_image)

    path0 = r"/home/jack/Desktop/pycode/vpython2/TrigonometryBot/images/"
    base_image0 = random.choice([
        x0 for x0 in os.listdir(path0)
        if os.path.isfile(os.path.join(path0, x0))
    ])
    filename00=(path0+base_image0)



    im0 = Image.open(filename0)
    im1 = im0.resize((640,640), Image.NEAREST)

    im01 = Image.open(filename00)
    im2 = im01.resize((640,640), Image.NEAREST)
    result1 = ImageChops.lighter(im1, im2) 
    filename = time.strftime("build/%Y%m%d%H%M%S.jpg")
    result1.save(filename)
    time.sleep(3)
    count= count +1

!rm /home/jack/Desktop/pycode/vpython2/TrigonometryBot/-images/image_68704131938.png

#!/anaconda2/bin/python
import os
import random
import sys
import markovify
sys.path.insert(0, '/home/jack/Desktop/pycode/vpython2')
import twython
from twython import Twython
import random
import time
import Key
#SLEEP_INTERVAL = random.randint(90,200)
#time.sleep(SLEEP_INTERVAL)

CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
path = 'screencap/'
count = 0
file_list = []
for filename in os.listdir(path):
        count = count+1
        file_list.append(filename)

rnd = random.randint(0,count)
with open("code.txt") as f:
    text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters

STR = (text_model.make_short_sentence(140))

#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')
photo = open('post/'+file_list[rnd],'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])

import markovify
f = open("codetalk.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
#http://paulbourke.net/fractals/
STR = (text_model.make_short_sentence(140))
print STR

import sys
sys.path.insert(0,"/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
import Key






CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,ACCESS_SECRET)
PATH = '/home/jack/Desktop/save-twitter/timeless.jpg'
STR ="True love is as endless as the space above, and timeless as eternity's end."
photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])

!ls /home/jack/anaconda2/envs/py27/lib/python2.7/site-packages/

#Great signature
import sys
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
path = r"publish/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)
def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]

def draw_text_with_halo(img, position, text, font, col, halo_col):
    halo = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(position, text, font = font, fill = halo_col)
    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(position, text, font = font, fill = col)
    return Image.composite(img, blurred_halo, ImageChops.invert(blurred_halo))

if __name__ == '__main__':
    inp = Image.open(filename0)
    font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 40)
    text_col = (255, 255,230) # bright green
    halo_col = (0, 0, 0)   # black
    textin = (generate_the_word("wordcloud.txt"))
    i2 = draw_text_with_halo(inp, (15, 8), textin, font, text_col, halo_col)
    
    #txt = Image.new('RGBA', i.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
    # get a drawing context
    d = ImageDraw.Draw(txt)
    width, height = inp.size
    marginx = 225
    marginy = 35
    x = width - marginx
    y = height - marginy
    signature_ = "The TwitterBot Project" 
    #text_col2 = (150, 255, 150) # bright green
    #halo_col2 = (0, 0, 0)   # black
    text_col2 = (255, 255,230) # bright green
    halo_col2 = (0, 0, 0)   # black
    txt=draw_text_with_halo(i2,(x,y), signature_, fnt, text_col2, halo_col2)
    out = Image.alpha_composite(i2, txt)
    filename = time.strftime("tmp/%Y%m%d%H%M%S.jpg")


out

import RandLine
texfile = open("ToUse.txt", "r")
RandLine.random_line(texfile)

#%%writefile titlenpost.py
#!/home/jack/anaconda2/python
import random
from random import randint
import time
import markovify
import os
import sys
sys.path.insert(1, "/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
import Key
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
nap = randint(10,35)
time.sleep(nap)
path = r"publish/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)
def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]

def draw_text_with_halo(img, position, text, font, col, halo_col):
    halo = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(position, text, font = font, fill = halo_col)
    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(position, text, font = font, fill = col)
    return Image.composite(img, blurred_halo, ImageChops.invert(blurred_halo))

if __name__ == '__main__':
    inp = Image.open(filename0)
    font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 40)
    text_col = (255, 255,230) # bright green
    halo_col = (0, 0, 0)   # black
    textin = (generate_the_word("wordcloud.txt"))
    i2 = draw_text_with_halo(inp, (15, 8), textin, font, text_col, halo_col)
    
    #txt = Image.new('RGBA', i.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
    # get a drawing context
    width, height = inp.size
    marginx = 225
    marginy = 35
    x = width - marginx
    y = height - marginy
    signature_ = "The TwitterBot Project" 
    #text_col2 = (150, 255, 150) # bright green
    #halo_col2 = (0, 0, 0)   # black
    text_col2 = (255, 255,230) # bright green
    halo_col2 = (0, 0, 0)   # black
    txt=draw_text_with_halo(i2,(x,y), signature_, fnt, text_col2, halo_col2)
    out = Image.alpha_composite(i2, txt)
    out.save("tmp/TM_POST.jpg")

#removed keys for privacy reasons
CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#path = 'images/NewFolder'
f = open("art.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
#http://paulbourke.net/fractals/
STR = (text_model.make_short_sentence(140))
#STR = ("#All_in_One - #WordCloud #Create - Added ability to randomly choose an image background  #Automated")
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "tmp/TM_POST.jpg"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

#photo = open(PATH,'rb')
#response = twitter.upload_media(media=photo)
#twitter.update_status(status=STR, media_ids=[response['media_id']])
out

import RandomLine
filename="ToUse.txt"
RandomLine.randomline(filename) 

import RandomLine
RandomLine.randomline("ToUse.txt") 

import RandNoun
print RandNoun.randnoun()


import RandNoun
help(RandNoun)




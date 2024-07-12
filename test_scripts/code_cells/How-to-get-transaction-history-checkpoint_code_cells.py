
requests.post("http://localhost:5279", json={"method": "transaction_list", "params": { }}).json()

params:
"account_id": optionalstr id of the account to query

"wallet_id":  restrict results to specific wallet

"page":       optional int page to return during paginating
example: "page": 1,
        
"page_size":  optionalint number of items on page during pagination
example:  "page_size": 50, 

## stripping out all characters but numbers rom a string
# python <3.0
def NumbersOnly(string):
    return filter(type(string).isdigit, string)

# python ≥3.0
def only_numerics(seq):
    seq_type= type(seq)
    return seq_type().join(filter(seq_type.isdigit, seq))

!rm /home/jack/Desktop/LBRY-toolbox/transaction_list.db

#!/usr/bin/python2
import os
from time import sleep
import urllib
import simplejson as json
import requests
import sys
import subprocess
from Completedpy2 import track_download
import sqlite3
import watchVID
def enter_data(page):
    database = 'transaction_list.db'
    conn = sqlite3.connect(database)
    # text_factory deals with the non-asci characters
    conn.text_factory = str
    sql = '''create table if not exists LBRY(
    description TEXT);'''
    conn.execute(sql) # shortcut for conn.cursor().execute(sql)
    conn.commit()
    c=conn.cursor()
    #search=raw_input("SEARCH : ")
    data = requests.post("http://localhost:5279", json={"method": "transaction_list", "params":{"page": page, "page_size": 10z0 } }).json()
    LINES = (json.dumps(data, indent=2 * ' '))
    Lin =str(LINES)
    L = Lin.split("\n")
    for line in L:
        try:
            c.execute("INSERT INTO LBRY VALUES (?)", (line,))
        except:
            pass
    conn.commit()
    conn.close()
    
for page in range(1,20):
    enter_data(page)  
    pause = randint(10,20)
    sleep(pause)
    print page,pause

import sqlite3
database = '/home/jack/Desktop/LBRY-toolbox/transaction_list.db'
conn = sqlite3.connect(database)
conn.text_factory = str
cnt = 0
#Search = raw_input("SEARCH: ")
c = conn.cursor()
for row in c.execute("select rowid,* from LBRY"):
    cnt = cnt +1
    if cnt<100:
        print row[0],": ",row[1]

print cnt   

import sqlite3
database = '/home/jack/Desktop/LBRY-toolbox/transaction_list.db'
conn = sqlite3.connect(database)
conn.text_factory = str
cnt = 0
Search = raw_input("SEARCH: ")
c = conn.cursor()
for row in c.execute("select rowid,* from LBRY"):
    if Search in row[1]:
        cnt = cnt +1
        if cnt<300:
            print row[0],": ",row[1]

print cnt   

# Get the amount of pages you must download

#!/usr/bin/python2
import os
from random import randint
from time import sleep
import urllib
import simplejson as json
import requests
import sys
import subprocess
from Completedpy2 import track_download
import sqlite3
import watchVID
get_items = []
def NumbersOnly(string):
    return filter(type(string).isdigit, string)

data = requests.post("http://localhost:5279", json={"method": "transaction_list", "params":{"page": 1, "page_size": 100 } }).json()
LINES = (json.dumps(data, indent=2 * ' '))
Lin =str(LINES)
L = Lin.split("\n")
print '----- First page - "page": 1 "page_size": 1 -----'
for lines in L:
    if "total_items" in lines:
        get_items.append(lines)
        print lines
        print " "
        print " "
get_number = str(get_items).split(":")
LAST = int(get_number[1][:-3])
print "----- Last page -----", LAST
print '"page": ',LAST,' "page_size": 1' 

data = requests.post("http://localhost:5279", json={"method": "transaction_list", "params":{"page": LAST, "page_size": 1 } }).json()
LINES = (json.dumps(data, indent=2 * ' '))
Lin =str(LINES)
L = Lin.split("\n")
for text in L:
    if "total_pages" in text:print NumbersOnly(text)
    print text

conn.close() 

#!/usr/bin/python2
import os
from random import randint
from time import sleep
import urllib
import simplejson as json
import requests
import sys
import subprocess
from Completedpy2 import track_download
import sqlite3
import watchVID
database = '/home/jack/Desktop/LBRY-toolbox/transaction_list.db'
conn = sqlite3.connect(database)
# text_factory deals with the non-asci characters
conn.text_factory = str
sql = '''create table if not exists LBRY(
description TEXT );'''
conn.execute(sql) # shortcut for conn.cursor().execute(sql)
conn.commit()
c=conn.cursor()
#search=raw_input("SEARCH : ")
def entry_data(database, page):
    cnt=0
    conn = sqlite3.connect(database)
    # text_factory deals with the non-asci characters
    conn.text_factory = str
    data = requests.post("http://localhost:5279", json={"method": "transaction_list", "params":{"page": page, "page_size": 10 } }).json()
    LINES = (json.dumps(data, indent=2 * ' '))
    Lin =str(LINES)
    L = Lin.split("\n")
    print 
    for line in L:
        cnt =  cnt +1
        c.execute("INSERT INTO LBRY VALUES (?)", (line,))
    print cnt    
    return 

for page in range(1,3):
    print page,pause
    pause = randint(10,20)
    sleep(pause)
    database = '/home/jack/Desktop/LBRY-toolbox/transaction_list.db'
    entry_data(database, page)

import sqlite3
database = '/home/jack/Desktop/LBRY-toolbox/transaction_list.db'
conn = sqlite3.connect(database)
conn.text_factory = str
cnt = 0
Search = raw_input("SEARCH: ")
c = conn.cursor()
for row in c.execute("select ROWID, description from LBRY"):
    if Search in row[1]:
        print row[0],": ",row[1]
 

database = '/home/jack/Desktop/LBRY-toolbox/transaction_list.db'
f=open(database).read()
for line in f:
    print line

#!/usr/bin/python2
import os
from random import randint
from time import sleep
import urllib
import simplejson as json
import requests
import sys
import subprocess
from Completed import track_download
import sqlite3
import watchVID
database = '/home/jack/Desktop/LBRY-toolbox/transaction_list.db'
conn = sqlite3.connect(database)
# text_factory deals with the non-asci characters
conn.text_factory = str
sql = '''create table if not exists LBRY(
description TEXT, url TEXT);'''
conn.execute(sql) # shortcut for conn.cursor().execute(sql)
conn.commit()
c=conn.cursor()
#search=raw_input("SEARCH : ")
def entry_data(database, page):
    conn = sqlite3.connect(database)
    # text_factory deals with the non-asci characters
    conn.text_factory = str
    data = requests.post("http://localhost:5279", json={"method": "transaction_list", "params":{"page": page, "page_size": 1 } }).json()
    LINES = (json.dumps(data, indent=2 * ' '))
    Lin =str(LINES)
    L = Lin.split("\n")
    for line in L:
        print line
        c.execute("INSERT INTO LBRY VALUES (?)", (line))
    conn.commit()
    conn.close()    

for page in range(1,3):
    pause = randint(10,20)
    sleep(pause)
    print page,pause
    database = '/home/jack/Desktop/LBRY-toolbox/transaction_list.db'
    entry_data(database, page)

!rm transaction_list.db

for page in range(1,20):
    print page

#!/usr/bin/python2
import os
from time import sleep
import urllib
import simplejson as json
import requests
import sys
import subprocess
from Completedpy2 import track_download
import sqlite3
import watchVID
database = '/home/jack/Desktop/LBRY-toolbox/transaction_list.db'
conn = sqlite3.connect(database)
# text_factory deals with the non-asci characters
conn.text_factory = str
sql = '''create table if not exists LBRY(
description TEXT, url TEXT);'''
conn.execute(sql) # shortcut for conn.cursor().execute(sql)
conn.commit()
c=conn.cursor()
#search=raw_input("SEARCH : ")
data = requests.post("http://localhost:5279", json={"method": "transaction_list", "params":{"page": 1, "page_size": 10 } }).json()
LINES = (json.dumps(data, indent=2 * ' '))
Lin =str(LINES)
L = Lin.split("\n")
for line in L:
    try:
        c.execute("INSERT INTO LBRY VALUES (?)", (line,))
    except:
        pass



conn.commit()
conn.close()

 "total_pages": 25,
    "page": 1,
    "page_size": 75

cnt = 0
for line in L:
    DES = []
    URL = []
    line= line.replace('\\n',' ')
    if "permanent_url" in line and "@" not in line:
        cnt= cnt+1
        Url = line.lstrip()
        URL.append(Url) 
        #print Url
        #print Url[25:-4]
        TEXT=Url[25:-4]+":::"
        #print TEXT
    if "description" in line:
        Des=line.lstrip()
        if len(Des)<5:Des="----------------No Description Given--"
        DES.append(Des)
        #print Des
        TEXT = str(TEXT)+(Des[16:-2])
        #print TEXT        
        #print Des[16:-2]
        TEXT = TEXT.split(":::")
        try:
            print TEXT[0]+"------"+TEXT[1]
            c.execute("INSERT INTO LBRY VALUES (?,?)", (TEXT[0],TEXT[1]))
        except:
            pass
conn.commit()
conn.close()



requests.post("http://localhost:5279", json={"method": "claim_list", "params": { }}).json()

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
get_items = []
def NumbersOnly(string):
    return filter(type(string).isdigit, string)

data = requests.post("http://localhost:5279", json={"method": "claim_list", "params":{"page": 1, "page_size": 1} }).json()
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
print '';print ''


page = raw_input("What page do you want? ")
print "----- This is the page you requested ",page,"-----"
print 'Using "params":{"page": ',page,', "page_size": 1 }'
print ''
PrintAll = ''
data = requests.post("http://localhost:5279", json={"method": "claim_list", "params":{"page": page, "page_size": 1 } }).json()
LINES = (json.dumps(data, indent=2 * ' '))
Lin =str(LINES)
L = Lin.split("\n")
for text in L:
    if "total_pages" in text:print NumbersOnly(text)
    print text   

!rm claim_list.db

#!/usr/bin/python2
# works well
import os
from time import sleep
import urllib
import simplejson as json
import requests
import sys
from random import randint
import subprocess
from Completed import track_download
import sqlite3
import watchVID
def enter_data(page):
    database = 'claim_list.db'
    conn = sqlite3.connect(database)
    # text_factory deals with the non-asci characters
    conn.text_factory = str
    sql = '''create table if not exists LBRY(
    description TEXT);'''
    conn.execute(sql) # shortcut for conn.cursor().execute(sql)
    conn.commit()
    c=conn.cursor()
    #search=raw_input("SEARCH : ")
    data = requests.post("http://localhost:5279", json={"method": "claim_list", "params":{"page": page, "page_size": 1 } }).json()
    TEXT=""
    LINES = (json.dumps(data, indent=2 * ' '))
    Lin =str(LINES)
    L = Lin.split("\n")
    for line in L:
    # TEXT=TEXT+str(line)
        c.execute("INSERT INTO LBRY VALUES (?)", (line,))
    conn.commit()
    conn.close()

for page in range(1,1150):    
    enter_data(page)
    if page %50 ==0:
        print "\n"
        pause = randint(5,15)
        sleep(pause)
    print page,
    

import sqlite3
import simplejson
def NumbersOnly(string):
    return filter(type(string).isdigit, string)
database = 'claim_list.db'
conn = sqlite3.connect(database)
#infile=open("test-transaction.json","w")
c = conn.cursor()
#text=""
cnt=1
for row in c.execute("select rowid,* from LBRY"):
    cnt=cnt+1
    if cnt<1000:
        print row[1]

#infile.write(text)
#infile.close()
print cnt

!rm claim_list-exp.db
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
database = 'claim_list-exp.db'
conn = sqlite3.connect(database)
# text_factory deals with the non-asci characters
conn.text_factory = str
sql = '''create table if not exists LBRY(
description TEXT);'''
conn.execute(sql) # shortcut for conn.cursor().execute(sql)
conn.commit()
c=conn.cursor()
#search=raw_input("SEARCH : ")
def enter_data(page,database):
    
    conn = sqlite3.connect(database)
    # text_factory deals with the non-asci characters
    conn.text_factory = str
    data = requests.post("http://localhost:5279", json={"method": "claim_list", "params":{"page": page, "page_size": 1 } }).json()
    LINES = (json.dumps(data, indent=2 * ' '))
    c.execute("INSERT INTO LBRY VALUES (?)", (LINES,))
    conn.commit()
    conn.close()    

for page in range(1,1140):  
    database = 'claim_list-exp.db'
    enter_data(page,database)
    if page %100 ==0:
        print "\n"
        pause = randint(5,15)
        sleep(pause)
    print page,
conn.commit()
conn.close()    

import sqlite3
import simplejson
def NumbersOnly(string):
    return filter(type(string).isdigit, string)
database = 'claim_list-exp.db'
conn = sqlite3.connect(database)
#infile=open("test-transaction.json","w")
c = conn.cursor()
#text=""
cnt=0
for row in c.execute("select rowid,* from LBRY"):
    cnt=cnt+1
    if cnt<100:
        print '\n==================== ',cnt,' =====================\n',row[1]

#infile.write(text)
#infile.close()
print cnt

#!/usr/bin/python2
# works well
import os
from time import sleep
import urllib
import simplejson as json
import requests
import sys
from random import randint
import subprocess
from Completed import track_download
import sqlite3
import watchVID
def enter_data(page):
    database = 'claim_list.db'
    conn = sqlite3.connect(database)
    # text_factory deals with the non-asci characters
    conn.text_factory = str
    sql = '''create table if not exists LBRY(
    description TEXT);'''
    conn.execute(sql) # shortcut for conn.cursor().execute(sql)
    conn.commit()
    c=conn.cursor()
    #search=raw_input("SEARCH : ")
    data = requests.post("http://localhost:5279", json={"method": "claim_list", "params":{"page": page, "page_size": 1 } }).json()
    TEXT=""
    LINES = (json.dumps(data, indent=2 * ' '))
    Lin =str(LINES)
    L = Lin.split("\n")
    for line in L:
    # TEXT=TEXT+str(line)
        c.execute("INSERT INTO LBRY VALUES (?)", (line,))
    conn.commit()
    conn.close()

for page in range(1,1150):    
    enter_data(page)
    if page %50 ==0:
        print "\n"
        pause = randint(5,15)
        sleep(pause)
    print page,
    

!rm transaction_list10.db

!rm test-transaction.json

import sqlite3
import simplejson
def NumbersOnly(string):
    return filter(type(string).isdigit, string)
database = 'claim_list.db'
conn = sqlite3.connect(database)
infile=open("claim_list.json","w")
c = conn.cursor()
text=""
cnt=1
for row in c.execute("select rowid,* from LBRY"):
    cnt=cnt+1
    print row[1]
    text=row[1]+"\n"
    infile.write(text)
infile.close()


import json
def json_validator(data):
    try:
        json.loads(data)
        return True
    except ValueError as error:
        print("invalid json: %s" % error)
        return False
data = open("test-transaction.json").read()
json_validator(data)

## stripping out all characters but numbers rom a string
# python <3.0
def NumbersOnly(string):
    return filter(type(string).isdigit, string)

# python ≥3.0
def only_numerics(seq):
    seq_type= type(seq)
    return seq_type().join(filter(seq_type.isdigit, seq))

import json

class Amazon():

    def parse(self, inpath, outpath):
        g = open(inpath, 'r')
        with open(outpath, 'w') as fout:
            for l in g:
                fout.write(json.dumps(eval(l)))

amazon = Amazon()
amazon.parse("test-transaction.json", "cleaned.json")

import json
try:
    infile=open("test-transactio.json","r")
    data = json.loads(infile)
except ValueError as err:
    print(err)

import simplejson as json
from simplejson import JSONDecodeError
def validate(filename):
    with open(filename) as file:
        try:
            return json.load(file) # put JSON-data to a variable
        except JSONDecodeError:
            print("Invalid JSON") # in case json is invalid
        else:
            print("Valid JSON") # in case json is valid
filename = "test-transactio.json"  
validate(filename)

import sqlite3
def NumbersOnly(string):
    return filter(type(string).isdigit, string)
database = '/home/jack/Desktop/LBRY-toolbox/claim_list.db'
conn = sqlite3.connect(database)
conn.text_factory = str
cnt = 0
amount=[]
start = []
tot=0
Search = raw_input("SEARCH: ")
c = conn.cursor()
for row in c.execute("select rowid,* from LBRY"):
    cnt=cnt+1
    if cnt<200:
        print row[1]

for num in start:
    print num
    

import sqlite3
def NumbersOnly(string):
    return filter(type(string).isdigit, string)
database = 'claim_list.db'
conn = sqlite3.connect(database)
conn.text_factory = str
cnt = 0
amount=[]
start = []
tot=0
Search = raw_input("SEARCH: ")
c = conn.cursor()
for row in c.execute("select rowid,* from LBRY"):
    if Search in row[1]:
        print row
        cnt = cnt +1


            
print cnt   




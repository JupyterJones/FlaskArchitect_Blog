
requests.post("http://localhost:5279", json={"method": "transaction_list", "params": { }}).json()

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

data = requests.post("http://localhost:5279", json={"method": "transaction_list", "params":{"page": 1, "page_size": 100 } }).json()
LINES = (json.dumps(data, indent=2 * ' '))
Lin =str(LINES)
L = Lin.split("\n")
print ('----- First page - "page": 1 "page_size": 1 -----')
for lines in L:
    if "total_items" in lines:
        get_items.append(lines)
        print (lines)
        print (" ")
        print (" ")
get_number = str(get_items).split(":")
LAST = int(get_number[1][:-3])
print ("----- Last page -----", LAST)
print ('"page": ',LAST,' "page_size": 1')
print (''); print ('')


def NumbersOnly(string):
    return filter(type(string).isdigit, string)
page = int(input("What page do you want? "))
print ("----- This is the page you requested ",page,"-----")
print ('Using "params":{"page": ',page,', "page_size": 1 }')
print ('')
PrintAll = ''
data = requests.post("http://localhost:5279", json={"method": "transaction_list", "params":{"page": page, "page_size": 20 } }).json()
LINES = (json.dumps(data, indent=2 * ' '))
Lin =str(LINES)
L = Lin.split("\n")
PrintAll=PrintAll+str(L)
for text in L:
    if "total_pages" in text:print (NumbersOnly(text))
    print (text)
#print (PrintAll)

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
    database = 'transaction_list10.db'
    conn = sqlite3.connect(database)
    # text_factory deals with the non-asci characters
    conn.text_factory = str
    sql = '''create table if not exists LBRY(
    description TEXT);'''
    conn.execute(sql) # shortcut for conn.cursor().execute(sql)
    conn.commit()
    c=conn.cursor()
    #search=raw_input("SEARCH : ")
    data = requests.post("http://localhost:5279", json={"method": "transaction_list", "params":{"page": page, "page_size": 1 } }).json()
    TEXT=""
    LINES = (json.dumps(data, indent=2 * ' '))
    Lin =str(LINES)
    L = Lin.split("\n")
    for line in L:
#        TEXT=TEXT+str(line)
        c.execute("INSERT INTO LBRY VALUES (?)", (line,))
    conn.commit()
    conn.close()
# for use in multiple pages
for page in range(1,20):    
    #for page in range(1,20):
    enter_data(page)
    if page %50 ==0:
        print "\n"
        pause = randint(5,15)
        sleep(pause)
    print page,
    

#!/usr/bin/python2
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
database = '/home/jack/Desktop/LBRY-toolbox/transaction_001.db'
conn = sqlite3.connect(database)
# text_factory deals with the non-asci characters
conn.text_factory = str
sql = '''create table if not exists LBRY(
description TEXT, url TEXT);'''
conn.execute(sql) # shortcut for conn.cursor().execute(sql)
conn.commit()
c=conn.cursor()
#search=raw_input("SEARCH : ")
def entry_data(page,database):
    
    conn = sqlite3.connect(database)
    # text_factory deals with the non-asci characters
    conn.text_factory = str
    data = requests.post("http://localhost:5279", json={"method": "transaction_list", "params":{"page": page, "page_size": 1 } }).json()
    LINES = (json.dumps(data, indent=2 * ' '))
    Lin =str(LINES)
    L = Lin.split("\n")
    for line in L:
        try:
            c.execute("INSERT INTO LBRY VALUES (?)", (line))
        except:
            pass
    conn.commit()
    conn.close()    

#for page in range(1,2098):  
for page in range(1,20):
    database = '/home/jack/Desktop/LBRY-toolbox/transaction_001.db'
    enter_data(page,database)
    if page %20 ==0:
        print "\n"
        pause = randint(5,15)
        sleep(pause)
    print page,
conn.commit()
conn.close()    

!rm transaction_list10.db

!rm test-transaction.json

import sqlite3
import simplejson
database = 'transaction_list6.db'
conn = sqlite3.connect(database)
infile=open("test-transaction.json","w")
c = conn.cursor()
text=""
cnt=1
for row in c.execute("select rowid,* from LBRY"):
    cnt=cnt+1
    print row[1]
    text=text+row[1]

infile.write(text)
infile.close()


import sqlite3
import simplejson
def NumbersOnly(string):
    return filter(type(string).isdigit, string)
database = 'transaction_list6.db'
conn = sqlite3.connect(database)
#infile=open("test-transaction.json","w")
c = conn.cursor()
#text=""
cnt=1
for row in c.execute("select rowid,* from LBRY"):
    cnt=cnt+1
    print row[1]

#infile.write(text)
#infile.close()


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
        try:
            c.execute("INSERT INTO LBRY VALUES (?)", (line))
        except:
            pass
    conn.commit()
    conn.close()    

for page in range(1,3):
    pause = randint(10,20)
    sleep(pause)
    print page,pause
    database = '/home/jack/Desktop/LBRY-toolbox/transaction_list.db'
    entry_data(database, page)

!rm test-transaction.json

import sqlite3
import simplejson
def NumbersOnly(string):
    return filter(type(string).isdigit, string)
database = 'transaction_list6.db'
conn = sqlite3.connect(database)
infile=open("test-transaction.json","w")
c = conn.cursor()
text=""
for row in c.execute("select rowid,* from LBRY"):
    text = text+row[1]+"\n"

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

!rm /home/jack/Desktop/LBRY-toolbox/transaction_list.db

!rm transaction_list6.db

import sqlite3
database = 'transaction_list10.db'
conn = sqlite3.connect(database)
conn.text_factory = str
cnt = 0
Search = str(raw_input("SEARCH: "))
c = conn.cursor()
for row in c.execute("select rowid,* from LBRY"):
    cnt=cnt+1
    if cnt<2000:
        if Search in row[1]:
             print row[1]

    

print cnt   

for page in range(1,209):
    if page %10 ==0:
        print "\n"
    print page,
        

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

params:
"account_id": optionalstr id of the account to query

"wallet_id":  restrict results to specific wallet

"page":       optional int page to return during paginating
example: "page": 1,
        
"page_size":  optionalint number of items on page during pagination
example:  "page_size": 50, 

!ls -rant *.json

import sqlite3
import simplejson
def NumbersOnly(string):
    return filter(type(string).isdigit, string)
database = '/home/jack/Desktop/LBRY-toolbox/transaction_list.db'
conn = sqlite3.connect(database)
infile=open("test-transaction.json","w")
c = conn.cursor()
text=""
for row in c.execute("select rowid,* from LBRY"):
    text = text+row[1]

infile.write(text)
infile.close()


import json

class Amazon():

    def parse(self, inpath, outpath):
        g = open(inpath, 'r')
        with open(outpath, 'w') as fout:
            for l in g:
                fout.write(json.dumps(eval(l)))

amazon = Amazon()
amazon.parse("test-transaction.json", "cleaned.json")

import sqlite3
import simplejson
def NumbersOnly(string):
    return filter(type(string).isdigit, string)
database = '/home/jack/Desktop/LBRY-toolbox/transaction_list.db'
conn = sqlite3.connect(database)
infile=open("test-transaction.json","w")
c = conn.cursor()
for row in c.execute("select rowid,* from LBRY"):
    infile.write(simplejson.dumps(simplejson.loads(row[1]), indent=4, sort_keys=True))
infile.close()



import sqlite3
import simplejson
def NumbersOnly(string):
    return filter(type(string).isdigit, string)
database = '/home/jack/Desktop/LBRY-toolbox/transaction_list.db'
conn = sqlite3.connect(database)
infile=open("test-transactio.json","w")
c = conn.cursor()
for row in c.execute("select rowid,* from LBRY"):
    infile.write(row[1])
infile.close()



import simplejson as json
from simplejson import JSONDecodeError

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
database = '/home/jack/Desktop/LBRY-toolbox/transaction_list.db'
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

import sqlite3
def NumbersOnly(string):
    return filter(type(string).isdigit, string)
database = '/home/jack/Desktop/LBRY-toolbox/transaction_list.db'
conn = sqlite3.connect(database)
conn.text_factory = str
cnt = 0
amount=0
start = []
tot=0
#Search = raw_input("SEARCH: ")
Search = "How-I-found-LBRY-and-Why-I-Was-Attracted-to-LBRY-Platform"

c = conn.cursor()
for row in c.execute("select rowid,* from LBRY"):
    if Search in row[1]:
        cnt = cnt +1
        step = int(row[0])+1
        start.append(step)
print cnt 
cnt=0
for num in start:
    for row in c.execute("select rowid,* from LBRY where rowid = ?", (num,)):
        cnt=cnt+1
        tip = row[1].split(":")
        TIP=tip[1].replace('"',"")
        TIP=TIP.replace(',',"")
        amount = amount+ float(TIP)
        print cnt,": ",TIP,"-",amount

 

          
 

for num in start:
    print num
    

import sqlite3
def NumbersOnly(string):
    return filter(type(string).isdigit, string)
database = '/home/jack/Desktop/LBRY-toolbox/transaction_list.db'
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

import sqlite3
def NumbersOnly(string):
    return filter(type(string).isdigit, string)
database = '/home/jack/Desktop/LBRY-toolbox/transaction_list.db'
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
 
        if cnt<300:
            #print row[0],": ",row[1]
            amount.append(row[1])
            numer =row[1].split(".")
            num=NumbersOnly(numer[0])
            amount.append(num)
            num =int(num)
            tot=tot +num
            print num,": ",tot

            
print cnt   

text = '''
"page":  2081  "page_size": 1
{
  "jsonrpc": "2.0",
  "result": {
    "total_items": 2081,
    "items": [
      {
'''
print text[:35]

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
def entry_data(database, page):
    conn = sqlite3.connect(database)
    # text_factory deals with the non-asci characters
    conn.text_factory = str
    data = requests.post("http://localhost:5279", json={"method": "transaction_list", "params":{"page": page, "page_size": 100 } }).json()
    LINES = (json.dumps(data, indent=2 * ' '))
    Lin =str(LINES)
    L = Lin.split("\n")
    for line in L:
        try:
            c.execute("INSERT INTO LBRY VALUES (?)", (line))
        except:
            pass
    conn.commit()
    conn.close()    

for page in range(1,3):
    pause = randint(10,20)
    sleep(pause)
    print page,pause
    database = '/home/jack/Desktop/LBRY-toolbox/transaction_list.db'
    entry_data(database, page)

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


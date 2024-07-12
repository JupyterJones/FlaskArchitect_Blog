!ls /home/jack/Desktop/*.txt

tx=open("/home/jack/Desktop/pas.txt").readlines()
for line in tx:
    line = line.replace("\n","")
    line = line.replace("\\n')","")
    print (line)

ex ="(2, u'https://app.arukas.io jahral@yahoo.com tr4356hyFrt##"
ex2 =ex.lstrip("(")
print (ex)
print (ex2)

help.strip()

!pip list>>freeze.txt

ftx=open("freeze.txt").readlines()
for line in ftx:
    line = line.replace("\n","")
    line = line.replace("\\n')","")
    print (line)

!ls /lib/python3.8/re.py

ftx=open("/lib/python3.8/re.py").readlines()
for line in ftx:
    line = line.replace("\n","")
    line = line.replace("\\n')","")
    print (line)

import re
help(re)

import re
ex ="(2, u'https://app.arukas.io jahral@yahoo.com tr4356hyFrt##"
ex2 =ex.split("u'")
print (ex)
print (ex2[1])

ftx=open("pas.txt").readlines()
LS = []
for line in ftx:
    line = line.replace("\n","")
    linez = line.replace("\\n')","")
    linex =linez.split("u'")
    print (linex)
    LS.append(linex)

len(LS)

import time
for line in LS:
    time.sleep (.5)
    print(line[1])

import sys
import sqlite3
conn = sqlite3.connect("pas.db")
conn.text_factory = str
c = conn.cursor()

def create():
    import sqlite3
    conn = sqlite3.connect("./pas.db")
    conn.text_factory = str
    c = conn.cursor()
    c.execute("CREATE VIRTUAL TABLE PROJECT using FTS4 (input)")
    conn.commit()
    text = "Database Created"
    return text

def insert(data,conn=conn, c=c):
    c.execute("INSERT into PROJECT values (?)", (data,))
    for row in c.execute("SELECT ROWID,* FROM PROJECT ORDER BY ROWID DESC LIMIT 1"):
        print ("\nPOST VERIFIED:\n",row[0],row[1])
    #conn.commit()
    #conn.close()
    return data

create()

import time
for data in LS:
    insert(data[1])
    
conn.commit()
conn.close()   

def main():
    conn = sqlite3.connect("./pas.db")
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        print (row[0],": ",row[1])
main()

!ls *.db

conn.commit()
conn.close()

!rm pas.db




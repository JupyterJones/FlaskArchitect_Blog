import Snip
Snip.snippet()

def datename():
    import datetime
    now = datetime.datetime.now()
    filename = now.strftime("%Y%m%d%H%M")+"jpg"
    return filename
print datename()

import sqlite3
import base64
conn = sqlite3.connect('snippet.db') #Connect to database 
c = conn.cursor()
conn.text_factory = str
file = """
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
"""
keywords = "blob text blob TextBlog stdin Short Sentences"
encodedlistvalue=base64.b64encode(file)
c.execute("INSERT INTO snippet VALUES (?,?,?)", (encodedlistvalue, file, keywords))
conn.commit()
conn.close()

import SearchFilename
filename = "Automate-the-Boring-Stuff.txt"
# length = how many lines after
length = 30
SearchFilename.searchfilename(filename, length) 


!rm SearchFilename.pyc

%%writefile SearchFilename.py
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

import searcH
searcH.search("pdf.txt", "database")

#%%writefile searcH.py
# Simple File Search
#import searcH
#searcH.search()
def search(filename, term):
    datafile = open(filename, "r")
    data = datafile.readlines()
    for line in data:
        if term in line:
            print line,

if __name__ == "__main__":
    filename = raw_input("Filename : ")
    term = raw_input("Search for : ")
    search(filename, term)            

!rm searcH.pyc

%%writefile searcH.py
# Simple File Search
#import searcH
#searcH.search()
def search(filename, term):
    datafile = open(filename, "r")
    data = datafile.readlines()
    for line in data:
        if term in line:
            print line,

if __name__ == "__main__":
    search(filename, term)            

def search(filename, term):
    datafile = open(filename, "r")
    data = datafile.readline()
    for line in data:
        if term in line:
            print line
            break

#filename = str(raw_input("FileName : "))
#term = raw_input("Find Term : ")  

term = "simplified"
filename = "importpython.txt"
search(filename, term)            

def search(filename, term):
    datafile = file(filename)
    found = False
    for line in datafile:
        if term in line:
            found = True
            print line
            break
            
            
filename = raw_input("FileName : ")
term = raw_input("Find Term : ")
search(filename, term)
if True:
    print "true"
else:
    print "false"

%%writefile Snip
def snippet():
    import sqlite3
    import sys
    conn = sqlite3.connect('snippet.db')
    conn.text_factory = str
    c = conn.cursor()
    count=0;req=200
    search = raw_input("Search : ")
    for row in c.execute('SELECT * FROM snippet WHERE text MATCH ?', (search,)):    
        count=count+1
        print (row)[1]," -- KEYWORDS",(row)[2],"\n"
        if count > req:
            conn.close()
            sys.exit()

import sqlite3
import sys
conn = sqlite3.connect('snippet.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
search = raw_input("Search : ")
for row in c.execute('SELECT * FROM snippet WHERE text MATCH ?', (search,)):    
    count=count+1
    print (row)[1]," -- KEYWORDS",(row)[2],"\n"
    if count > req:
        conn.close()
        sys.exit()

#import the base64 module
import base64
# here is a singleline example
string="This is the text above Encoded Base64"
#encode the string in this case the variable is EncodedStringValue
EncodedStringValue=base64.b64encode(string)

string2 = EncodedStringValue
print "Encoded String : ",EncodedStringValue, \
"\nDecoded String2 : ",base64.b64decode(string2)

import base64 #encode muliple lines and keep the format
string = """
╲╲╭━━━━━━━╮╱╱
╲╭╯╭━╮┈╭━╮╰╮╱
╲┃┈┃┈▊┈┃┈▊┈┃╱
╲┃┈┗━┛┈┗━┛┈┃╱
╱┃┈┏━━━━━┓┈┃╲
╱┃┈┃┈┈╭━╮┃┈┃╲
╱╰╮╰━━┻━┻╯╭╯╲
╱╱╰━━━━━━━╯╲╲ FROM: http://copy.r74n.com/ascii-art
"""
EncodedStringValue=base64.b64encode(string)
string2 = EncodedStringValue
print "Decoded String2 : ",base64.b64decode(string2)

%%writefile /home/jack/hidden/Key.py
def twiter():
    CONSUMER_KEY = 'XXXXXXXXXXXX'
    CONSUMER_SECRET = 'YYYYYYYYYYYYY'
    ACCESS_KEY = 'ZZZZZZZZZZZZZZZZZZZZZZZ'
    ACCESS_SECRET = '000000000000000000000'
    twitter = (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
    return twitter

import sys
sys.path.insert(1, "/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
sys.path.insert(0, "/home/jack/hidden")
import Key
#removed keys for privacy reasons
CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

print CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

!mkdir /home/jack/hidden

%%writefile /home/jack/hidden/Authorize.py
def keys():
    ftp = "ftp.MYsite.com"
    username = "Josephine"
    password = "WhaWah2525"
    login = (ftp,username,password)
    return login

import sys
sys.path.insert(0, "/home/jack/hidden"
import Authorize
ftp = Authorize.keys()[0]
username = Authorize.keys()[1]
password = Authorize.keys()[2]

print ftp, username, password

import sqlite3
import sys
conn = sqlite3.connect('snippet.db')
conn.text_factory = str
c = conn.cursor()
count=0
req=200
search = raw_input("Search : ")
#for row in c.execute('SELECT rowid,* FROM tweets WHERE text MATCH %s' % search):
for row in c.execute('SELECT * FROM snippet WHERE keywords MATCH ?', (search,)):    
    count=count+1
    #print count,"by",(row)[2],"\n",(row)[1],"\n"
    print count,"-",(row)[1]," -- by",(row)[2],"\n"
    if count > req:
        conn.close()
        sys.exit()

http://sebsauvage.net/python/snyppets/

import sqlite3
conn = sqlite3.connect('ipydb.db')

CREATE TABLE IF NOT EXISTS room(room_id INTEGER PRIMARY KEY, name VARCHAR(25) NOT NULL, home_id VARCHAR(25) NOT NULL);


import sqlite3
conn = sqlite3.connect('ipydb.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE python
             (code text, keyword text)''')

# Insert a row of data
c.execute("INSERT INTO python VALUES ('Python','Storage for snippets and more')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()


import sqlite3
conn = sqlite3.connect('ipydb.db')

c = conn.cursor()

# Create table
#c.execute('''CREATE TABLE python
#             (code text, keyword text)''')

# Insert a row of data
c.execute("INSERT INTO python VALUES ('We need to close the connection if we are done accessing a database','connection')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()


!sqlite3 ipydb.db "pragma integrity_check;"

import sqlite3
conn = sqlite3.connect('ipydb.db')
c = conn.cursor()

# Larger example that inserts many records at a time
data = [('pragma integrity_check will check that your database is valid', 'check, verify, inspect'),
             ('multiple items may be entered at once', 'newkey'),
             ('base64 encoding allows code to be stored and retieved in the same format it was posted', '4Webstuff, gwebsite, gghtml'),]

c.executemany("INSERT INTO python VALUES (?,?)", data)
conn.commit()
conn.close()


import sqlite3
conn = sqlite3.connect('ipydb.db')
c = conn.cursor()# Never 
for row in c.execute('SELECT * FROM python ORDER BY code'):
        print(row),"\n-----\n"

import sqlite3
conn = sqlite3.connect('ipydb.db')
c = conn.cursor()# Never 
for row in c.execute('SELECT * FROM python ORDER BY code'):
        clean = row[0].encode('ascii')
        print clean, '\n', 'Keywords:', row[1], '\n -----------------------------\n'
        
        

# nice format
#
import sqlite3
conn = sqlite3.connect('ipydb.db')
c = conn.cursor()# Never 
for row in c.execute('SELECT * FROM python ORDER BY code'):
        print"entry :",(row[0]).encode('ascii'),"\n"
        print"keywords :",(row[1]).encode('ascii'),"\n-----\n","\n"  
        #data = c.fetchall()
        #print data

import sqlite3
conn = sqlite3.connect('ipydb.db')
c = conn.cursor()# Never 
for row in c.execute('SELECT * FROM python ORDER BY code'):
        #print(row),"\n-----\n","\n"
        
        print row[0],"\n",row[1],"\n-----\n",

import sqlite3
conn = sqlite3.connect('ipydb64.db')
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE python
             (code text, keyword text)''')


import sqlite3
import base64
conn = sqlite3.connect('ipydb64.db')
c = conn.cursor()
# The code to be inserted must be formated as a muti-line comment with the three quotes

# a is the code to be stored
a = encodedlistvalue=base64.b64encode(
    """# Larger example that inserts many records at a time
import sqlite3
import base64
conn = sqlite3.connect('/home/jack/Desktop/testPy.db')
c = conn.cursor()
# Larger example that inserts many records at a time

a = encodedlistvalue=base64.b64encode(
# Larger example that inserts many records at a time)
#c.execute("INSERT INTO python VALUES (?, ?)" a, b)
#c.execute("INSERT INTO python VALUES (%s, %s,)", (a, b))
c.execute("INSERT INTO python VALUES (?,?)", (a,b))

conn.commit()
conn.close()    
    """)
# b is the keyword or words
b = 'example'

c.execute("INSERT INTO python VALUES (?,?)", (a,b))

conn.commit()
conn.close()


import sqlite3
import base64
conn = sqlite3.connect('ipydb64.db')
c = conn.cursor()
# The code to be inserted must be formated as a muti-line comment with the three quotes

# a is the code to be stored
a = encodedlistvalue=base64.b64encode(
    """import Tkinter as tk, tkSimpleDialog

class MyDialog(tkSimpleDialog.Dialog):
    def body(self, master):
        self.geometry("800x600")
        tk.Label(master, text="Enter your search string text:").grid(row=0)

        self.e1 = tk.Entry(master)
        self.e1.grid(row=0, column=1)
        return self.e1 # initial focus

    def apply(self):
        first = self.e1.get()
        self.result = first


        root = tk.Tk()
        root.withdraw()
        test = MyDialog(root, "testing")
    def show_entry_fields():
        print("First Name: %s\n" % (e2.get()))
    
    """)
# b is the keyword or words
b = 'ktinker'

c.execute("INSERT INTO python VALUES (?,?)", (a,b))

conn.commit()
conn.close()


import sqlite3
import base64

#Connect to database: 
conn = sqlite3.connect('ipydb64.db')
c = conn.cursor()

#Single lines do not need the three quotes
file = 'base64 encoding allows code to be stored and retieved in the same format it was posted'
b = '4Webstuff, gwebsite, gghtml'
encodedlistvalue=base64.b64encode(file)

c.execute("INSERT INTO python VALUES (?,?)", (encodedlistvalue, b))

conn.commit()
conn.close()


import sqlite3
conn = sqlite3.connect('ipydb64.db')
c = conn.cursor()
for row in c.execute('SELECT * FROM python ORDER BY code'):
        print(row),"\n-----\n"
        # notice the Keywords are plain text even the base64 is displayed as unicode (u'IyBMYXJ .... )

import sqlite3
conn = sqlite3.connect('ipydb64.db')

c = conn.cursor()# Never 
for row in c.execute('SELECT * FROM python ORDER BY code'):
                
        # display as asci instead of unicode
        s2 = row[0].encode('ascii')
        #decode the base64 stored data
        encodedlistvalue=base64.b64decode(s2)
        print encodedlistvalue, '\n', 'Keywords:', row[1], '\n -----------------------------\n'

        

conn = sqlite3.connect('ipydb64.db')
c = conn.cursor()# Never 

t = ('example',)
c.execute('SELECT * FROM python WHERE keyword=?', t)

subjectList = [row[0] for row in c.fetchall()]        
#print row[0]
#for row in data :
encodedlistvalue=base64.b64decode(row[0])
print encodedlistvalue, '\n', 'Keywords:', row[1], '\n -----------------------------\n'


conn = sqlite3.connect('ipydb64.db')
c = conn.cursor()# Never 

t = ('example',)
for row in c.execute('SELECT code FROM python WHERE keyword=?', t):

    #subjectList = [row[0] for row in c.fetchall()]        
    code = row[0].encode('ascii')
    
    #for row in data :
    encodedlistvalue=base64.b64decode(code)
    print encodedlistvalue, '\n -----------------------------\n'
    

conn = sqlite3.connect('ipydb.db')
c = conn.cursor()# Never 

t = ('example',)
c.execute('SELECT * FROM python WHERE keyword=?', t)

subjectList = [row[0] for row in c.fetchall()]        
#print row[0]
#for row in data :
encodedlistvalue=base64.b64decode(row[0])
print encodedlistvalue, '\n', 'Keywords:', row[1], '\n -----------------------------\n'


conn = sqlite3.connect('ipydb.db')
c = conn.cursor()# Never 

t = ('ktinker',)
c.execute('SELECT * FROM python WHERE keyword=?', t)

subjectList = [row[0] for row in c.fetchall()]        
#print row[0]
#for row in data :
encodedlistvalue=base64.b64decode(row[0])
print encodedlistvalue, '\n', 'Keywords:', row[1], '\n -----------------------------\n'


conn = sqlite3.connect('ipydb64.db')
c = conn.cursor()# Never 

t = ('ktinker',)
c.execute('SELECT * FROM python WHERE keyword=?', t)

subjectList = [row[0] for row in c.fetchall()]        
#print row[0]
#for row in data :
encodedlistvalue=base64.b64decode(row[0])
print encodedlistvalue, '\n', 'Keywords:', row[1], '\n -----------------------------\n'


conn = sqlite3.connect('ipydb64.db')
c = conn.cursor()# Never 

tn = ('ktinker',)
for row in c.execute('SELECT * FROM python WHERE keyword=?', tn):
                
        s2 = row[0].encode('ascii')
        encodedlistvalue=base64.b64decode(s2)
        print encodedlistvalue, '\n', 'Keywords:', row[1], '\n -----------------------------\n'


import sqlite3
conn = sqlite3.connect('ipydb64.db')
c = conn.cursor()# Never 
#for row in c.execute('SELECT code FROM python ORDER BY keyword'):
s = ('ktinker',)
c.execute('SELECT code FROM python WHERE keyword=?', s)
        
          
print(c.fetchone())


import sqlite3
conn = sqlite3.connect('ipydb.db')
c = conn.cursor()# Never do this -- insecure!
#    symbol = 'RHAT'
#    c.execute("SELECT * FROM python WHERE symbol = '%s'" % symbol)

# Do this instead
t = ('ktinker',)
c.execute('SELECT * FROM python WHERE keyword=?', t)
print(c.fetchone())


import sqlite3
conn = sqlite3.connect('ipydb.db')
c = conn.cursor()# Never do this -- insecure!

t = ('Webstuff',)
c.execute('SELECT * FROM python ORDER BY keyword=?', t)
print(c.fetchall())
conn.close()


import sqlite3
conn = sqlite3.connect('main.db')

c = conn.cursor()

# DROP TABLE IF EXISTS
c.execute("DROP TABLE IF EXISTS Products")

import sqlite3
conn = sqlite3.connect('main.db')

c = conn.cursor()

c.execute("""CREATE TABLE Products (
             contact_id integer PRIMARY KEY,
             CatID text NOT NULL,
             description text NOT NULL,
             keywords text NOT NULL);
          """)
conn.commit()
conn.close()


import sqlite3
def insert_product(product):
    with sqlite3.connect("main.db") as db:
        cursor = db.cursor()
        sql = "insert into Products (CatID,description,keywords) values (?, ?, ?)"
        cursor.execute(sql, product)
        db.commit()

if __name__ == "__main__":
    ID= int(input("enter the CatID of the product:>> "))
    Des = input("Enter description: >>")
    Keywords = int(input("Enter keywords: >>"))
    product = (ID,Des,Keywords)
    insert_product(product)
    
    
    
    
    
    
    

import sqlite3
import Tkinter as tk, tkSimpleDialog

class MyDialog(tkSimpleDialog.Dialog):
    def body(self, master):
        self.geometry("800x600")
        tk.Label(master, text="Enter your search string text:").grid(row=0)

        self.e1 = tk.Entry(master)
        self.e1.grid(row=0, column=1)
        return self.e1 # initial focus

    def apply(self):
        first = self.e1.get()
        self.result = first

def insert_product(product):
    with sqlite3.connect("main.db") as db:
        cursor = db.cursor()
        sql = "insert into Products (CatID,description,keywords) values (?, ?, ?)"
        cursor.execute(sql, product)
        db.commit()

if __name__ == "__main__":
        ID= int(input("enter the CatID of the product:>> "))
        #Des = input("Enter description: >>")
        root = tk.Tk()
        root.withdraw()
        test = MyDialog(root, "Paste Code Here")
        Keywords = int(input("Enter keywords: >>"))
        insert = test.result
        product = (ID,insert,Keywords)
        insert_product(product)
    
       
    
    
    
    

import sqlite3
conn = sqlite3.connect("main.db", isolation_level=None ,timeout=30000) 
print("Opened database successfully")
conn.close()


import sqlite3
conn = sqlite3.connect('main.db')
c = conn.cursor()# Never do this -- insecure!
#    symbol = 'RHAT'
#    c.execute("SELECT * FROM python WHERE symbol = '%s'" % symbol)

# Do this instead
t = ('252525',)
c.execute('SELECT * FROM Products WHERE CatID=?', t)
print(c.fetchone())


from tkinter import *
import Tkinter as tk, tkSimpleDialog

class MyDialog(tkSimpleDialog.Dialog):
    def body(self, master):
        self.geometry("800x600")
        tk.Label(master, text="Enter your search string text:").grid(row=0)

        self.e1 = tk.Entry(master)
        self.e1.grid(row=0, column=1)
        return self.e1 # initial focus

    def apply(self):
        first = self.e1.get()
        self.result = first


        root = tk.Tk()
        root.withdraw()
        test = MyDialog(root, "testing")
    def show_entry_fields():
        print("First Name: %s\n" % (e2.get()))

        master = Tk()
        Label(master, text="First Name").grid(row=0)
        e2 = Entry(master)
        e2.grid(row=0, column=1)
        Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
        Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

#mainloop( )


        
        
        
        
        mainloop( )


print test.result

from tkinter import *
import Tkinter as tk, tkSimpleDialog

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

#mainloop( )






class MyDialog(tkSimpleDialog.Dialog):
    def body(self, master):
        self.geometry("800x600")
        tk.Label(master, text="Enter your search string text:").grid(row=0)

        self.e1 = tk.Entry(master)
        self.e1.grid(row=0, column=1)
        return self.e1 # initial focus

    def apply(self):
        first = self.e1.get()
        self.result = first


        root = tk.Tk()
        root.withdraw()
        test = MyDialog(root, "testing")
mainloop( )


print test.result

import sqlite3
def insert_product(product):
    with sqlite3.connect("main.db") as db:
        cursor = db.cursor()
        sql = "insert into Products (CatID,description,keywords) values (?, ?, ?)"
        cursor.execute(sql, product)
        db.commit()

if __name__ == "__main__":
    ID= int(input("enter the CatID of the product:>> "))
    Des = input("Enter description: >>")
    Keywords = int(input("Enter keywords: >>"))
    product = (ID,Des,Keywords)
    insert_product(product)
    
    
    
    
    
    
    

import Tkinter as tk, tkSimpleDialog

class MyDialog(tkSimpleDialog.Dialog):
    def body(self, master):
        self.geometry("500x100")
        tk.Label(master, text="Enter your search string text:").grid(row=0)

        self.e1 = tk.Entry(master)
        self.e1.grid(row=0, column=1)
        return self.e1 # initial focus

    def apply(self):
        first = self.e1.get()
        self.result = first


root = tk.Tk()
root.withdraw()
test = MyDialog(root, "testing")
print test.result

!ls

!ls *.jpg
#-rw-rw-r-- 1 someone someone 618441 Apr 28 16:59 bla.jpg
#-rw-rw-r-- 1 someone someone 618441 Apr 28 16:37 test.jpg
!md5sum *.jpg 
#3237a2b76050f2780c592455b3414813  bla.jpg
#3237a2b76050f2780c592455b3414813  test.jpg

%load /etc/mysql/mysql.conf.d/mysqld.cnf

import MySQLdb
help(MySQLdb)

#Works
import MySQLdb as db
con = db.connect("localhost","root","")
cur = con.cursor()
cur.execute('CREATE DATABASE testdb5;')

import MySQLdb as db
con = db.connect("localhost","root","", "testdb5")
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS python")
    cur.execute("CREATE TABLE python(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 code text, keywords VARCHAR(200))")
    cur.execute("INSERT INTO python (code) VALUES('Testing thisout')")
    #cur.execute("INSERT INTO Writers(Name) VALUES('Henry Wadjob')")
    #cur.execute("INSERT INTO Writers(Name) VALUES('Klepto Manic')")
    #cur.execute("INSERT INTO Writers(Name) VALUES('Emila gray')")
    #cur.execute("INSERT INTO Writers(Name) VALUES('Mike Stupoff')")

!ls *.py

# works 
import MySQLdb as db
import json 
import base64
    
con = db.connect("localhost","root","", "testdb5")
file = """[mylist.jsn

while 1:
    line = file.readline()
    if not line:
        break
    pass # do something 



#listname='mylist.json'
#stringlistvalue=json.dumps(listname)

"""
encodedlistvalue=base64.b64encode(file)
with con:
    cur = con.cursor()
    #cur.execute("DROP TABLE IF EXISTS Code")
    #cur.execute("CREATE TABLE Code(Id INT PRIMARY KEY AUTO_INCREMENT, \
    #              Name VARCHAR(500))")
    #cur.execute("INSERT INTO Code(Name) VALUES('%s')" % (encodedlistvalue))
    cur.execute("INSERT INTO python(code) VALUES('%s')" % (encodedlistvalue))

# WORKS
#!/usr/bin/python
# import the MySQLdb and sys modules
import MySQLdb
import sys
import base64
# open a database connection
# be sure to change the host IP address, username, password and database name to match your own

con = db.connect("localhost","root","", "testdb5")

# prepare a cursor object using cursor() method
#cursor = connection.cursor ()
cur = con.cursor()

# execute the SQL query using execute() method.
cur.execute ("select Id, code from python")

# fetch all of the rows from the query
data = cur.fetchall ()



# print the rows
for row in data :
    encodedlistvalue=base64.b64decode(row[1])
    print row[0], encodedlistvalue

# close the cursor object
cur.close ()

# close the connection
con.close ()

# exit the program
sys.exit()

#Works
import MySQLdb as db
con = db.connect("localhost","root","")
cur = con.cursor()
cur.execute('CREATE DATABASE searchdb01;')

# works 
import MySQLdb as db
import json 
import base64
    
con = db.connect("localhost","root","", "searchdb01")
file = """
[mylist.jsn

while 1:
    line = file.readline()
    if not line:
        break
    pass # do something 



#listname='mylist.json'
#stringlistvalue=json.dumps(listname)

"""
keywords = """
database, code, python, lesson 1, Oh234
"""

encodedlistvalue=base64.b64encode(file)
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Code")
    cur.execute("CREATE TABLE Code(Id INT PRIMARY KEY AUTO_INCREMENT, \
                  Name VARCHAR(2500), Keywords VARCHAR(500))")
    #cur.execute("INSERT INTO Code(Name) VALUES('%s')" % (encodedlistvalue))
    cur.execute("INSERT INTO Code(Name, Keywords) VALUES('%s','%s')" % (encodedlistvalue, keywords))

# works 
import MySQLdb as db
import json 
import base64
    
con = db.connect("localhost","root","", "searchdb01")
file = """
URL transformed to HTTPS due to an HSTS policy
--2017-07-09 13:01:34--  https://asd.gsfc.nasa.gov/archive/hubble/Hubble_20th.jpg
Resolving asd.gsfc.nasa.gov (asd.gsfc.nasa.gov)... 129.164.179.20, 2001:4d0:2310:150::20
Connecting to asd.gsfc.nasa.gov (asd.gsfc.nasa.gov)|129.164.179.20|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 49600 (48K) [image/jpeg]
Saving to: ‘image.jpg’

image.jpg           100%[===================>]  48.44K   153KB/s    in 0.3s    

2017-07-09 13:01:36 (153 KB/s) - ‘image.jpg’ saved [49600/49600]

Error: near line 1: table images already exists

"""
keywords = """
Resolving, asd.gsfc, nasa.gov, rt5eg
"""

encodedlistvalue=base64.b64encode(file)
with con:
    cur = con.cursor()
    #cur.execute("DROP TABLE IF EXISTS Code")
    #cur.execute("CREATE TABLE Code(Id INT PRIMARY KEY AUTO_INCREMENT, \
    #              Name VARCHAR(500), Keywords VARCHAR(500))")
    #cur.execute("INSERT INTO Code(Name) VALUES('%s')" % (encodedlistvalue))
    cur.execute("INSERT INTO Code(Name, Keywords) VALUES('%s','%s')" % (encodedlistvalue, keywords))

#!/usr/bin/python
# import the MySQLdb and sys modules
import MySQLdb
import sys

# open a database connection
# be sure to change the host IP address, username, password and database name to match your own

con = db.connect("localhost","root","", "searchdb01")

# prepare a cursor object using cursor() method
#cursor = connection.cursor ()
cur = con.cursor()

# execute the SQL query using execute() method.
cur.execute ("select Id, Name, Keywords from Code")

# fetch all of the rows from the query
data = cur.fetchall ()

# print the rows
for row in data :
    print row[0], row[1], "\n", "Keywords: ", row[2], "\n -----------------------------"

# close the cursor object
cur.close ()

# close the connection
con.close ()

# exit the program
sys.exit()

# WORKS
#!/usr/bin/python
# import the MySQLdb and sys modules
import MySQLdb
import sys
import base64
# open a database connection
# be sure to change the host IP address, username, password and database name to match your own

con = db.connect("localhost","root","", "searchdb01")

# prepare a cursor object using cursor() method
#cursor = connection.cursor ()
cur = con.cursor()

# execute the SQL query using execute() method.
cur.execute ("select Id, Name, Keywords from Code")

# fetch all of the rows from the query
data = cur.fetchall ()



# print the rows
for row in data :
    encodedlistvalue=base64.b64decode(row[1])
    print row[0], encodedlistvalue, '\n', 'Keywords:', row[2], '\n -----------------------------\n'

# close the cursor object
cur.close ()

# close the connection
con.close ()

# exit the program
sys.exit()

import MySQLdb
con = db.connect("localhost","root","", "searchdb01")

#db = MySQLdb.connect (host = "localhost",
#                          user = "root",
#                          passwd = "root",
# ENTER KEYWORD HERE       db = "test")
# The keyword is 'lesson 1', however, because the term 'Keywords LIKE' is used, lesson is 'close enough'
param = "lesson"

#par = param

c = con.cursor()

#c.execute("SELECT * FROM data WHERE params LIKE ('%s%') LIMIT 1"  % (param))
c.execute("SELECT * FROM Code WHERE Keywords LIKE %s LIMIT 1", ("%" + param + "%",))

data = c.fetchall()

# print the rows
for row in data :
    encodedlistvalue=base64.b64decode(row[1])
    print row[0], encodedlistvalue, '\n', 'Keywords:', row[2], '\n -----------------------------\n'



c.close()




import MySQLdb
con = db.connect("localhost","root","", "searchdb01")

#db = MySQLdb.connect (host = "localhost",
#                          user = "root",
#                          passwd = "root",
#                          db = "test")
param = "Oh234"

#par = param

c = con.cursor()

#c.execute("SELECT * FROM data WHERE params LIKE ('%s%') LIMIT 1"  % (param))
c.execute("SELECT * FROM Code WHERE Keywords LIKE %s LIMIT 1", ("%" + param + "%",))

data = c.fetchall()

# print the rows
for row in data :
    encodedlistvalue=base64.b64decode(row[1])
    print row[0], encodedlistvalue, '\n', 'Keywords:', row[2], '\n -----------------------------\n'



c.close()




#Works
import MySQLdb as db
con = db.connect("localhost","root","")
cur = con.cursor()
cur.execute('CREATE DATABASE searchdb05;')

# works 
import MySQLdb as db
import json 
import base64
    
con = db.connect("localhost","root","", "searchdb05")

# copied and pasted from github
file = """

Creating Tables
In [2]:

import sqlite3
conn = sqlite3.connect('ipydb.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE python
             (code text, keyword text)''')

# Insert a row of data
c.execute("INSERT INTO python VALUES ('Python','Storage for snippets and more')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

In [3]:

import sqlite3
conn = sqlite3.connect('ipydb.db')
"""
keywords = """
database, code, python, lesson 1, Oh234
"""

encodedlistvalue=base64.b64encode(file)
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Code")
    cur.execute("CREATE TABLE Code(Id INT PRIMARY KEY AUTO_INCREMENT, \
                  Name VARCHAR(2500), Keywords VARCHAR(500))")
    #cur.execute("INSERT INTO Code(Name) VALUES('%s')" % (encodedlistvalue))
    cur.execute("INSERT INTO Code(Name, Keywords) VALUES('%s','%s')" % (encodedlistvalue, keywords))

import MySQLdb
con = db.connect("localhost","root","", "searchdb05")

# search keyword database
param = "database"

c = con.cursor()

#c.execute("SELECT * FROM data WHERE params LIKE ('%s%') LIMIT 1"  % (param))
c.execute("SELECT * FROM Code WHERE Keywords LIKE %s LIMIT 1", ("%" + param + "%",))

data = c.fetchall()

# print the rows
for row in data :
    encodedlistvalue=base64.b64decode(row[1])
    print row[0], encodedlistvalue, '\n', 'Keywords:', row[2], '\n -----------------------------\n'
# close db
c.close()




def process_file(filename):
    reg = re.compile(r'([\w]{2,3}):\s') # Matches line header
    tmp = '' # Stored/cached data for mutliline string
    key = None # Current key
    data = {}

    with open(filename,'r') as f:
        for row in f:
            row = row.rstrip()
            match = reg.match(row)

            # Matches header or is end, put string to list:
            if (match or not row) and key:
                data[key] = tmp
                key = None
                tmp = ''

            # Empty row, next dataset
            if not row:
                # Prevent empty returns
                if data:
                    yield data
                    data = {}

                continue

            # We do have header
            if match:
                key = str(match.group(1))
                tmp = row[len(match.group(0)):]
                continue

            # No header, just append string -> here goes assumption that you want to
            # remove newlines, trailing spaces and replace them with one single space
            tmp += ' ' + row

    # Missed row?
    if key:
        data[key] = tmp

    # Missed group?
    if data:
        yield data
        

data = process_file("mylist")
print data

# %load mylist
"""
python - Searching for Phrase Keywords in MySQL - Stack Overflow
https://stackoverflow.com/questions/.../searching-for-phrase-keywords-in-mysql
May 16, 2015 - 

"""

%%writefile mylist
"""
python - Searching for Phrase Keywords in MySQL - Stack Overflow
https://stackoverflow.com/questions/.../searching-for-phrase-keywords-in-mysql
May 16, 2015 - 

"""

# %load mylist
"""
python - Searching for Phrase Keywords in MySQL - Stack Overflow
https://stackoverflow.com/questions/.../searching-for-phrase-keywords-in-mysql
May 16, 2015 - 

"""

# %load mylist
"""
python - Searching for Phrase Keywords in MySQL - Stack Overflow
https://stackoverflow.com/questions/.../searching-for-phrase-keywords-in-mysql
May 16, 2015 - 

"""

# works 
import MySQLdb as db
import json 
import base64
    
con = db.connect("localhost","root","", "searchdb01")


#data = %load mylist



keywords = """
data, webite, cut paste, 87er
"""

encodedlistvalue=base64.b64encode('%load mylist')
with con:
    cur = con.cursor()

# Put this through to SQL using an INSERT statement...
cur.execute("""INSERT INTO Code (Name, Keywords)
                   VALUES(%s, %s)""", (encodedlistvalue, keywords))


import MySQLdb
con = db.connect("localhost","root","", "searchdb05")

# search keyword database
param = "87er"

c = con.cursor()

#c.execute("SELECT * FROM data WHERE params LIKE ('%s%') LIMIT 1"  % (param))
#c.execute("SELECT * FROM Code WHERE Keywords LIKE %s LIMIT 1", ("%" + param + "%",))
c.execute("SELECT * FROM Code LIMIT 12")
data = c.fetchall()

# print the rows
for row in data :
    encodedlistvalue=base64.b64decode(row[1])
    print row[0], encodedlistvalue, '\n', 'Keywords:', row[2], '\n -----------------------------\n'
# close db
c.close()




# works 
import MySQLdb as db
import json 
import base64
    
con = db.connect("localhost","root","", "searchdb01")


#data = process_file("mylist")



keywords = """
data, webite, cut paste, 87er
"""

category = "Name"
with open("mylist", "r") as name:
    lines = name.readlines()

for line in lines:
    # Split the line on whitespace
    data = line.split()
    number = data[0]
    value = data[1]
    encodedlistvalue=base64.b64encode(value)
    # Put this through to SQL using an INSERT statement...
    cursor.execute("""INSERT INTO Code (Name, Keywords)
                   VALUES(%s, %s)""", (encodedlistvalue, keywords))



keywords = """
data, webite, cut paste, 87er
"""

encodedlistvalue=base64.b64encode(data)
with con:
    cur = con.cursor()
    #cur.execute("DROP TABLE IF EXISTS Code")
    #cur.execute("CREATE TABLE Code(Id INT PRIMARY KEY AUTO_INCREMENT, \
    #              Name VARCHAR(500), Keywords VARCHAR(500))")
    #cur.execute("INSERT INTO Code(Name) VALUES('%s')" % (encodedlistvalue))
    cur.execute("INSERT INTO Code(Name, Keywords) VALUES('%s','%s')" % (encodedlistvalue, keywords))

# works 
import MySQLdb as db
import json 
import base64
    
con = db.connect("localhost","root","", "searchdb01")


#data = process_file("mylist")


keywords = """
data, webite, cut paste, 87er
"""

encodedlistvalue=base64.b64encode(data)
with con:
    cur = con.cursor()
    #cur.execute("DROP TABLE IF EXISTS Code")
    #cur.execute("CREATE TABLE Code(Id INT PRIMARY KEY AUTO_INCREMENT, \
    #              Name VARCHAR(500), Keywords VARCHAR(500))")
    #cur.execute("INSERT INTO Code(Name) VALUES('%s')" % (encodedlistvalue))
    cur.execute("INSERT INTO Code(Name, Keywords) VALUES('%s','%s')" % (encodedlistvalue, keywords))

# works 
import MySQLdb as db
import json 
import base64
    
con = db.connect("localhost","root","", "searchdb05")

encodedlistvalue=base64.b64encode(data)
with con:
    cur = con.cursor()
    #cur.execute("DROP TABLE IF EXISTS Code")
    #cur.execute("CREATE TABLE Code(Id INT PRIMARY KEY AUTO_INCREMENT, \
    #              Name VARCHAR(500))")
    #cur.execute("INSERT INTO Code(Name) VALUES('%s')" % (encodedlistvalue))
    cur.execute("INSERT INTO Code(Name) VALUES('%s')" % (encodedlistvalue))

%%writefile mylist.jsn
[row = cursor.fetchone()
while row:
    #print(row)
    rowstring = "" # printed for each row
    result = row[b64field_idx] # set to base64 field value
    
    for j in range(numcols):
        rowstring += str(row[j]) + "\t" # Need to print each column (tab separated)
         
    try:
        # Now we can Base64 decode however many times they want
        for j in range(args.b64count) :
            temp = base64.decodestring(result)
            result = temp
        rowstring += result # Add the decoded result to the output string
        ]

# works 
import MySQLdb as db
import json 
import base64
    
con = db.connect("localhost","root","", "searchdb05")
file = """[mylist.jsn

while 1:
    line = file.readline()
    if not line:
        break
    pass # do something 



#listname='mylist.json'
#stringlistvalue=json.dumps(listname)

"""
encodedlistvalue=base64.b64encode(file)
with con:
    cur = con.cursor()
    #cur.execute("DROP TABLE IF EXISTS Code")
    #cur.execute("CREATE TABLE Code(Id INT PRIMARY KEY AUTO_INCREMENT, \
    #              Name VARCHAR(500))")
    #cur.execute("INSERT INTO Code(Name) VALUES('%s')" % (encodedlistvalue))
    cur.execute("INSERT INTO Code(Name) VALUES('%s')" % (encodedlistvalue))

#!/usr/bin/python
# import the MySQLdb and sys modules
import MySQLdb
import sys

# open a database connection
# be sure to change the host IP address, username, password and database name to match your own

con = db.connect("localhost","root","", "searchdb05")

# prepare a cursor object using cursor() method
#cursor = connection.cursor ()
cur = con.cursor()

# execute the SQL query using execute() method.
cur.execute ("select Id, Name from Code")

# fetch all of the rows from the query
data = cur.fetchall ()

# print the rows
for row in data :
    print row[0], row[1]

# close the cursor object
cur.close ()

# close the connection
con.close ()

# exit the program
sys.exit()

# works 
import MySQLdb as db
import json 
import base64
    
con = db.connect("localhost","root","", "searchdb05")

with con:
    cur = con.cursor()

#for row in cur.execute('select * from Code limit 150'):
#    print(row)

row = cur.execute('select Name from Code WHERE Id=2')
print(row)

        #cur.execute("INSERT INTO Code(Name) VALUES('%s')" % (encodedlistvalue))
        # cur.execute("INSERT INTO Code(Name) VALUES('%s')" % (encodedlistvalue))

#mylist = json.loads( base64.b64decode(encodedstringvalue)) 
#And a raw, simple example

import pymysql
import json 
import base64
    

     
listname='mylist'
dbhost="127.0.0.1"
#dbhost="mysql"
dbuser="root"
dbpwd=""
dbdatabase="testdb2"
     
# serialize list into a string, and then encode in SQL-safe base64 format 
stringlistvalue=json.dumps(mylist)
encodedlistvalue=base64.b64encode(stringlistvalue)
    
db = pymysql.connect(dbhost,dbuser,dbpwd,dbdatabase )
     
# Prepare SQL query to INSERT a record into the database.
#sql = "INSERT INTO Writers(listname, listvalue) VALUES ('%s', '%s')" % (listname, encodedlistvalue)
sql = "INSERT INTO Writers(Name) VALUES ('%s')" % (encodedlistvalue)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()
finally:
    # disconnect from server
    db.close() 

SET PASSWORD FOR 'root'@'localhost' = PASSWORD('');

To change password:
sudo dpkg-reconfigure mysql-server-5.5

sudo mysql -u root
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('');
CREATE USER 'jack'@'localhost' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON * . * TO 'jack'@'localhost';
FLUSH PRIVILEGES;

def createdb(sqlitedbase):
    import sqlite3
    conn = sqlite3.connect(sqlitedbase)
    c = conn.cursor()
  
    query1 = "DROP TABLE IF EXISTS Junk"
    query2 = """CREATE TABLE IF NOT EXISTS Junk(
    "language" VARCHAR(32) NOT NULL,
    "keywords" VARCHAR(500) default NULL,
    "script" VARCHAR(2500) default NULL
    )
    """
    c.execute(query1)
    c.execute(query2)

createdb("newdatabase02")

import sqlite3
conn = sqlite3.connect('newdatabase02')

c = conn.cursor()
c.execute("INSERT INTO Junk VALUES ('SQLite','Junkstuff, stuff, sql','beans')")  
conn.commit()

conn.close()

import sqlite3
conn = sqlite3.connect('newdatabase02')

c = conn.cursor()
s = ('stuff',)
#c.execute('SELECT * FROM Junk WHERE keywords=?', s)
c.execute('SELECT * FROM Junk')
#print(c.fetchmany())
print(c.fetchall())




%%writefile QuickStore.py
import sqlite3

def store():
    print "Leave Database-Name empty to use `/home/jack/Default.db`."
    print "You many enter three sets of data (DataOne & DataTwo), and Keywords  "  
    Dbname = raw_input("Database-Name: >>") or "/home/jack/Default.db"
    conn = sqlite3.connect(Dbname)
    conn.commit()
    conn.close()
    print Dbname
    storeOne = raw_input("Enter DataOne: >>")
    storeTwo = raw_input("Enter DataTwo: >>")
    keywords = raw_input("Enter Keywords: >>")

    info = (storeOne,storeTwo,keywords)
    insert_info(info,Dbname)
    return Dbname

def insert_info(info,Dbname):
        conn = sqlite3.connect(Dbname)
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS storage (
                   id integer PRIMARY KEY,
                   storeOne text NOT NULL,
                   storeTwo text NOT NULL,
                   keywords text NOT NULL);
                   """)
        sql = "insert into storage (storeOne,storeTwo,keywords) values (?, ?, ?)"
        c.execute(sql, info)
        conn.commit()
        conn.close()

        
def readDB():
    conn = sqlite3.connect('/home/jack/Default.db')
    c = conn.cursor()# Never do this -- insecure!
    for row in c.execute('SELECT * FROM storage ORDER BY id'):
        print row[0],"  ",row[1],"  ",row[2],"  ",row[3],"\n-----\n",
    conn.close()
    
    
    

import QuickStore
QuickStore.store()

import QuickStore
QuickStore.readDB()


import sqlite3
import base64
conn = sqlite3.connect('newdatabase02')

stringlistvalue ="""
this is a test
"""
c = conn.cursor()
# Insert a row of data
encodedlistvalue=base64.b64encode('stringlistvalue')
language ="SQLlite"
keywords ="computer stuff, sqlite, iu5t"
#c.execute  "INSERT INTO Junk VALUES ('Python','Python, script, sql', '%s')" % (encodedlistvalue)
#  "INSERT INTO Junk VALUES ('Python','Python, script, sql', '%s')" % (encodedlistvalue)
    
#c.execute("INSERT INTO Junk VALUES (?,?,?);", (encodedlistvalue)  


c.execute("INSERT INTO Junk VALUES (?, ?, ?);", (language, keywords, encodedlistvalue))


#c.execute(query1) 
#sql = "INSERT INTO Writers(Name) VALUES ('%s')" % (encodedlistvalue)


#3db = pymysql.connect(dbhost,dbuser,dbpwd,dbdatabase )
     
# Prepare SQL query to INSERT a record into the database.
#sql = "INSERT INTO Writers(listname, listvalue) VALUES ('%s', '%s')" % (listname, encodedlistvalue)
#sql = "INSERT INTO Writers(Name) VALUES ('%s')" % (encodedlistvalue)
#3try:
    # Execute the SQL command
 #   cursor.execute(sql)
    # Commit your changes in the database
#    db.commit()

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

import sqlite3
conn = sqlite3.connect('newdatabase02')

c = conn.cursor()
# Larger example that inserts many records at a time
purchases = ('IBM', 1000, 45.00),('MSFT', 1000, 72.00),('IBM', 500, 53.00)
            
c.executemany('INSERT INTO Junk VALUES (?,?,?)', purchases)
# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

    ''' tk_entry_loop2.py
    exploring Tkinter multiple labeled entry widgets
    and using a for loop to create the widgets
    '''
    from functools import partial
    try:
        # Python2
        import Tkinter as tk
    except ImportError:
        # Python3
        import tkinter as tk
    class Gui(tk.Tk):
        def __init__(self):
            # the root will be self
            tk.Tk.__init__(self)
            self.title('multiple labeled entries')
            self.entries = []
            for n in range(20):
                # create left side info labels
                tk.Label(self, text="%2d: " % n).grid(row=n, column=0)
                # create entries list
                self.entries.append(tk.Entry(self, bg='yellow', width=40))
                # grid layout the entries
                self.entries[n].grid(row=n, column=1)
                # bind the entries return key pressed to an action
                self.entries[n].bind('<Return>', partial(self.action, n))
            # test, load one entry
            self.entries[0].insert('end', 'enter a word in an entry')
        def action(self, ix, event):
            '''this entry return key pressed'''
            text = self.entries[ix].get()
            info = "entry ix=%d text=%s" % (ix, text)
            # use first entry to show test results
            # clear old text
            self.entries[0].delete(0, 'end')
            # insert new text
            self.entries[0].insert('end', info)
        def run(self):
            self.mainloop()
    # test the potential module
    if __name__ == '__main__':
        Gui().run()

#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script, we use the grid
manager to create a more complicated
layout.

Author: Jan Bodnar
Last modified: December 2015
Website: www.zetcode.com
"""

from Tkinter import Tk, Text, BOTH, W, N, E, S
from ttk import Frame, Button, Label, Style


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.initUI()
        
        
    def initUI(self):
      
        self.parent.title("Windows")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)
        
        lbl = Label(self, text="Windows")
        lbl.grid(sticky=W, pady=4, padx=5)
        
        area = Text(self)
        area.grid(row=1, column=0, columnspan=2, rowspan=4, 
            padx=5, sticky=E+W+S+N)
        
        abtn = Button(self, text="Activate")
        abtn.grid(row=1, column=3)

        cbtn = Button(self, text="Close")
        cbtn.grid(row=2, column=3, pady=4)
        
        hbtn = Button(self, text="Help")
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(self, text="OK")
        obtn.grid(row=5, column=3)        
              

def main():
  
    root = Tk()
    root.geometry("350x300+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  

from Tkinter import *
root= Tk()
root.title("My First GUI")
root.geometry("800x200")
frame1=Frame(root)
frame1.grid()
label1 = Label(frame1, text = "Here is a label!")
label1.grid()
button1 = Button(frame1, text = "I am a Button")
button1.grid()
button1.configure(text = "Me too!")
text1 = Text(frame1, width = 200, height = 20)
text1.grid()
root.mainloop()

class interface(tk.Frame):
    def __init__(self,den):
        self.pa_nu = 0  ##page number. Both used in labeling and result slicing
        self.lbl1 = tk.Label(den, text="keyword")
        self.lbl2 = tk.Label(den, text="Page %d" %(self.pa_nu+1))
        self.ent1 = tk.Entry(den, takefocus=True)
        self.btn1 = tk.Button(den, text="Search", command=self.button1)
        self.btn2 = tk.Button(den, text="Page Up", command=self.page_up)
        self.btn3 = tk.Button(den, text="Page Down", command=self.page_down)

        scrollbar = tk.Scrollbar(den)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.lst1 = tk.Listbox(den, selectmode="SINGLE", width="40", yscrollcommand=scrollbar.set)
        self.lst1.bind("<Double-Button-1>", self.open_folder)
        scrollbar.config(command=self.lst1.yview)

        self.lbl1.pack(side="top")
        self.ent1.pack()
        self.btn1.pack(side="top")
        self.btn2.pack(side="right")
        self.btn3.pack(side="left")
        self.lbl2.pack(side="bottom",padx=65)
        self.lst1.pack(fill=BOTH)

    def button1(self):     
        pass #some stuff here

    def page_up(self):
        pass #some stuff here

    def page_down(self):
        pass #some stuff here

    def list_fill(self,i):
        pass #some stuff here

    def open_folder(self,event):
        pass #some stuff here

#button_example.py
from tkinter import *
rootWin = Tk()


frame = Frame(rootWin)                #Create a frame to organize the buttons
frame.pack()

def quitFunc():                       #The quitFunc just prints a message!
   print("Quit button pressed!")

def speakFunc():                      #The speakFunc  just prints a message!
  print("Say hi!")


#Define button1, which has a foreground (fg) color of red, displays the
#text "Quit", and will call the quitFunc when it is clicked.
#It will be inside the frame created above.
button1 = Button(frame, text="Quit", fg="red", command=quitFunc)
button1.pack(side=LEFT)


#Create another button, displaying the text "Speak" and programmed to
#call the speakFunc when it is clicked.
button2 = Button(frame, text="Speak", command=speakFunc)
button2.pack(side=LEFT)


rootWin.mainloop()    #Run the main loop.


http://zetcode.com/gui/tkinter/layout/

"""
Implement a GUI for viewing and updating class instances stored in a shelve;
the shelve lives on the machine this script runs on, as 1 or more local files;
"""

from tkinter import *
from tkinter.messagebox import showerror
import shelve
shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')

def makeWidgets():
    global entries
    window = Tk()
    window.title('People Shelve')
    form = Frame(window)
    form.pack()
    entries = {}
    for (ix, label) in enumerate(('key',) + fieldnames):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent
    Button(window, text="Fetch",  command=fetchRecord).pack(side=LEFT)
    Button(window, text="Update", command=updateRecord).pack(side=LEFT)
    Button(window, text="Quit",   command=window.quit).pack(side=RIGHT)
    return window

def fetchRecord():
    key = entries['key'].get()
    try:
        record = db[key]                      # fetch by key, show in GUI
    except:
        showerror(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))

def updateRecord():
    key = entries['key'].get()
    if key in db:
        record = db[key]                      # update existing record
    else:
        from person import Person             # make/store new one for key
        record = Person(name='?', age='?')    # eval: strings must be quoted
    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))
    db[key] = record

db = shelve.open(shelvename)
window = makeWidgets()
window.mainloop()
db.close() # back here after quit or window close

import wx 

#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script, we use the grid
manager to create a more complicated
layout.

Author: Jan Bodnar
Last modified: December 2015
Website: www.zetcode.com
"""

from Tkinter import Tk, Text, BOTH, W, N, E, S
from ttk import Frame, Button, Label, Style


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.initUI()
        
        
    def initUI(self):
      
        self.parent.title("Windows")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)
        
        lbl = Label(self, text="Windows")
        lbl.grid(sticky=W, pady=4, padx=5)
        
        area = Text(self)
        area.grid(row=1, column=0, columnspan=2, rowspan=4, 
            padx=5, sticky=E+W+S+N)
        
        abtn = Button(self, text="Activate")
        abtn.grid(row=1, column=3)

        cbtn = Button(self, text="Close")
        cbtn.grid(row=2, column=3, pady=4)
        
        hbtn = Button(self, text="Help")
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(self, text="OK")
        obtn.grid(row=5, column=3)        
              

def main():
  
    root = Tk()
    root.geometry("350x300+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  


# File: tree.py
# References:
#    http://hg.python.org/cpython/file/4e32c450f438/Lib/tkinter/ttk.py
#    http://www.tcl.tk/man/tcl8.5/TkCmd/ttk_treeview.htm#M79
#    http://svn.python.org/projects/python/branches/pep-0384/Demo/tkinter/ttk/dirbrowser.py

import os

from tkinter import *
from tkinter import ttk     #@Reimport

from demopanels import MsgPanel, SeeDismissPanel

# Constants for formatting file sizes
KB = 1024.0
MB = KB * KB
GB = MB * KB

class TreeDemo(ttk.Frame):
    
    def __init__(self, isapp=True, name='treedemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Tree Demo')
        self.isapp = isapp
        self._create_widgets()
        
    def _create_widgets(self):
        if self.isapp:
            MsgPanel(self, ["One of the new Tk themed widgets is a tree widget, which allows ",
                            "the user to browse a hierarchical data-set such as a file system. ",
                            "The tree widget not only allows for the tree part itself, but it ",
                            "also supports an arbitrary number of additional columns which can ",
                            "show additional data (in this case, the size of the files found ",
                            "on your file system). You can also change the width of the columns ",
                            "by dragging the boundary between them."])
            
            SeeDismissPanel(self)
        
        self._create_demo_panel()
        
    def _create_demo_panel(self):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)
        
        self._create_treeview(demoPanel)    
        self._populate_root()
                    
    def _create_treeview(self, parent):
        f = ttk.Frame(parent)
        f.pack(side=TOP, fill=BOTH, expand=Y)
        
        # create the tree and scrollbars
        self.dataCols = ('fullpath', 'type', 'size')        
        self.tree = ttk.Treeview(columns=self.dataCols, 
                                 displaycolumns='size')
        
        ysb = ttk.Scrollbar(orient=VERTICAL, command= self.tree.yview)
        xsb = ttk.Scrollbar(orient=HORIZONTAL, command= self.tree.xview)
        self.tree['yscroll'] = ysb.set
        self.tree['xscroll'] = xsb.set
        
        # setup column headings
        self.tree.heading('#0', text='Directory Structure', anchor=W)
        self.tree.heading('size', text='File Size', anchor=W)
        self.tree.column('size', stretch=0, width=70)
        
        # add tree and scrollbars to frame
        self.tree.grid(in_=f, row=0, column=0, sticky=NSEW)
        ysb.grid(in_=f, row=0, column=1, sticky=NS)
        xsb.grid(in_=f, row=1, column=0, sticky=EW)
        
        # set frame resizing priorities
        f.rowconfigure(0, weight=1)
        f.columnconfigure(0, weight=1)
        
        # action to perform when a node is expanded
        self.tree.bind('<<TreeviewOpen>>', self._update_tree)
        
    def _populate_root(self):
        # use current directory as root node
        self.path = os.getcwd()
        
        # insert current directory at top of tree
        # 'values' = column values: fullpath, type, size
        #            if a column value is omitted, assumed empty
        parent = self.tree.insert('', END, text=self.path,
                                  values=[self.path, 'directory'])
        
        # add the files and sub-directories
        self._populate_tree(parent, self.path, os.listdir(self.path))
                
    def _populate_tree(self, parent, fullpath, children):
        # parent   - id of node acting as parent
        # fullpath - the parent node's full path 
        # children - list of files and sub-directories
        #            belonging to the 'parent' node
        
        for child in children:
            # build child's fullpath
            #cpath = os.path.join(fullpath, child).replace('\\', '/')
            cpath = os.path.join(fullpath, child).replace('', '')
            
            if os.path.isdir(cpath):
                # directory - only populate when expanded
                # (see _create_treeview() 'bind')
                cid =self.tree.insert(parent, END, text=child,
                                      values=[cpath, 'directory'])
                
                # add 'dummy' child to force node as expandable
                self.tree.insert(cid, END, text='dummy')  
            else:
                # must be a 'file'
                size = self._format_size(os.stat(cpath).st_size)
                self.tree.insert(parent, END, text=child,
                                 values=[cpath, 'file', size])
                
    def _format_size(self, size):
        if size >= GB:
            return '{:,.1f} GB'.format(size/GB)
        if size >= MB:
            return '{:,.1f} MB'.format(size/MB)
        if size >= KB:
            return '{:,.1f} KB'.format(size/KB)
        return '{} bytes'.format(size)
                
    def _update_tree(self, event): #@UnusedVariable
        # user expanded a node - build the related directory 
        nodeId = self.tree.focus()      # the id of the expanded node
        
        if self.tree.parent(nodeId):    # not at root
            topChild = self.tree.get_children(nodeId)[0]
            
            # if the node only has a 'dummy' child, remove it and 
            # build new directory; skip if the node is already
            # populated
            if self.tree.item(topChild, option='text') == 'dummy':
                self.tree.delete(topChild)
                path = self.tree.set(nodeId, 'fullpath')
                self._populate_tree(nodeId, path, os.listdir(path))

if __name__ == '__main__':
    TreeDemo().mainloop()

%%writefile demopanels.py
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:26:52 2015
@author: Simon
"""
# File: demopanels.py
# References:
#    http://hg.python.org/cpython/file/4e32c450f438/Lib/tkinter/simpledialog.py
#    http://docs.python.org/py3k/library/inspect.html#module-inspect
#
# Icons sourced from:
#    http://findicons.com/icon/69404/deletered?width=16#
#    http://findicons.com/icon/93110/old_edit_find?width=16#
 
from tkinter import *
from tkinter import ttk
#from tkinter.simpledialog import Dialog
from tkSimpleDialog import Dialog
from PIL import Image, ImageTk
import inspect
 
class MsgPanel(ttk.Frame):
    def __init__(self, master, msgtxt):
        ttk.Frame.__init__(self, master)
        self.pack(side=TOP, fill=X)
         
        msg = Label(self, wraplength='4i', justify=LEFT)
        msg['text'] = ''.join(msgtxt)
        msg.pack(fill=X, padx=5, pady=5)
         
class SeeDismissPanel(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.pack(side=BOTTOM, fill=X)          # resize with parent
         
        # separator widget
        sep = ttk.Separator(orient=HORIZONTAL)
 
        # Dismiss button
        im = Image.open('/home/jack/Desktop/deep-dream-generator/notebooks/JavaScript/delete.png')   # image file
        imh = ImageTk.PhotoImage(im)            # handle to file
        dismissBtn = ttk.Button(text='Dismiss', image=imh, command=self.winfo_toplevel().destroy)
        dismissBtn.image = imh                  # prevent image from being garbage collected
        dismissBtn['compound'] = LEFT           # display image to left of label text
         
        # 'See Code' button
        im = Image.open('/home/jack/Desktop/deep-dream-generator/notebooks/JavaScript/view.png')
        imh = ImageTk.PhotoImage(im)
        codeBtn = ttk.Button(text='See Code', image=imh, default=ACTIVE, command=lambda: CodeDialog(self.master))
        codeBtn.image = imh
        codeBtn['compound'] = LEFT
        codeBtn.focus()
                 
        # position and register widgets as children of this frame
        sep.grid(in_=self, row=0, columnspan=4, sticky=EW, pady=5)
        codeBtn.grid(in_=self, row=1, column=0, sticky=E)
        dismissBtn.grid(in_=self, row=1, column=1, sticky=E)
         
        # set resize constraints
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
 
        # bind <Return> to demo window, activates 'See Code' button;
        # <'Escape'> activates 'Dismiss' button
        self.winfo_toplevel().bind('<Return>', lambda x: codeBtn.invoke() )
        self.winfo_toplevel().bind('<Escape>', lambda x: dismissBtn.invoke() )

class CodeDialog(Dialog):
    """Create a modal dialog to display a demo's source code file. """
         
    def body(self, master):
        """Overrides Dialog.body() to populate the dialog window with a scrolled text window
        and custom dialog buttons. """
         
        # get the full path of this object's parent source code file
        fileName = inspect.getsourcefile(self.parent._create_widgets)
         
        self.title('Source Code: ' + fileName)
         
        # create scrolled text widget
        txtFrame = ttk.Frame(self)
        txtFrame.pack(side=TOP, fill=BOTH)
         
        text = Text(txtFrame, height=24, width=100, wrap=WORD, setgrid=1, highlightthickness=0, pady=2, padx=3)
        xscroll = ttk.Scrollbar(txtFrame, command=text.xview, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(txtFrame, command=text.yview, orient=VERTICAL)
        text.configure(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
         
        # position in frame and set resize constraints
        text.grid(row=0, column=0, sticky=NSEW)
        yscroll.grid(row=0, column=1, sticky=NSEW)
        txtFrame.rowconfigure(0, weight=1)
        txtFrame.columnconfigure(0, weight=1)
         
        # add text of file to scrolled text widget
        text.delete('0.0', END)
        text.insert(END, open(fileName).read())
 
    def buttonbox(self):
        """Overrides Dialog.buttonbox() to create custom buttons for this dialog. """
         
        box = ttk.Frame(self)
 
        # Cancel button
        cancelBtn = ttk.Button(box, text='Cancel', command=self.cancel)       
        cancelBtn.pack(side=RIGHT, padx=5, pady=5)
        self.bind('<Return>', self.cancel)
        self.bind('<Escape>', self.cancel)
         
        box.pack()

        #Contact GitHub API Training Shop Blog About 



!ls 

%%writefile tkSimpleDialog.py
from Tkinter import *
import os
class Dialog(Toplevel):
    def __init__(self, parent, title = None):
        Toplevel.__init__(self, parent)
        self.transient(parent)
        if title:
            self.title(title)
        self.parent = parent
        self.result = None
        body = Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)
        self.buttonbox()
        self.grab_set()
        if not self.initial_focus:
            self.initial_focus = self
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))
        self.initial_focus.focus_set()
        self.wait_window(self)
    # construction hooks
    def body(self, master):
        # create dialog body.  return widget that should have
        # initial focus.  this method should be overridden
        pass
    def buttonbox(self):
        # add standard button box. override if you don't want the
        # standard buttons
        box = Frame(self)
        w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)
        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        box.pack()
    # standard button semantics
    def ok(self, event=None):
        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return
        self.withdraw()
        self.update_idletasks()
        self.apply()
        self.cancel()
    def cancel(self, event=None):
        # put focus back to the parent window
        self.parent.focus_set()
        self.destroy()
    # command hooks
    def validate(self):
        return 1 # override
    def apply(self):
        pass # override




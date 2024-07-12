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
tweetfile = 'hurricane_14.txt'
results = twitter.cursor(twitter.search, q='hurricane, Irma')
filein = open(tweetfile, 'w')
for result in results:
    result=str(result)
    filein.write(result)
    print(result)
    if time.time() - sTime > 4:
        filein.close()
        sys.exit()
         

import sqlite3
conn = sqlite3.connect('data/hurricane.db')
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
#conn = sqlite3.connect('hurricane.db')
#c = conn.cursor()
# Create table
#c.execute('''CREATE TABLE hurricane
#             (hurricane text, keywords text)''')
count=0
lines = 400
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
        keywords = 'sept, hurricaneirma, florida'
        conn = sqlite3.connect('data/hurricane.db')
        c = conn.cursor()
        time.sleep(1)
        #encodedlistvalue=base64.b64encode(file[2:-2])
        #c.execute("INSERT INTO hurricane VALUES (?,?)", (encodedlistvalue, b)) 
        c.execute("INSERT INTO hurr VALUES (?,?)", (file, keywords)) 
        conn.commit()
        conn.close()        
        
        
        time.sleep(1)
        print file[2:-2]
        count=count+1
        print count
        if count>lines:
            sys.exit()
#commits and closes database if there are less then 400 lines of text
conn.commit()
conn.close()                 



# t = ('Html',)
#c.execute('SELECT * FROM python WHERE keyword=?', t)
import sqlite3
import sys
conn = sqlite3.connect('data/hurricane.db')
c = conn.cursor()# Never 
count=0
req=4
search = 'hurricane'
#for row in c.execute('SELECT * FROM hurr WHERE text MATCH ?',search):
for row in c.execute('SELECT * FROM hurr WHERE text MATCH "False source"'):
    
    #SELECT * FROM docs WHERE docs MATCH 'sqlite AND database';    
    
    count=count+1
    print(row),"\n-----\n"
    if count > req:
        conn.close()
        sys.exit()
        

import sqlite3
import sys
conn = sqlite3.connect('data/hurricane.db')
c = conn.cursor()# Never 
count=0
req=14
for row in c.execute('SELECT * FROM hurr'):
    count=count+1
    print(row),"\n-----\n"
    if count > req:
        conn.close()
        sys.exit()
        

http://sebsauvage.net/python/snyppets/

import sqlite3
conn = sqlite3.connect('ipydb.db')

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

c.execute("INSERT INTO python VALUES ('close the connection if we are done','connection')")

# Save (commit) the changes
conn.commit()

#close the connection 
conn.close()



!sqlite3 ipydb.db "pragma integrity_check;"

from time import sleep
fileO = open("/home/jack/.bash_history")
lists = fileO.readlines()
for list in lists:
    
    #list = list.encode("ascii", "ignore")
    list = list.decode('utf-8').strip() 
    sleep(1)
    print list

import sqlite3
conn = sqlite3.connect('ipydb64.db')
c = conn.cursor()

# Larger example that inserts many records at a time
data = [('pragma integrity_check will check that your database is valid', 'check, verify, inspect'),
             ('multiple items may be entered at once', 'newkey'),
             ('base64 encoding allows code to be stored and retieved in the same format it was posted', '4Webstuff, gwebsite, gghtml'),]

c.executemany("INSERT INTO python VALUES (?,?)", data)
conn.commit()
conn.close()


import sqlite3
import base64
conn = sqlite3.connect('ipydb64.db')
c = conn.cursor()
# Larger example that inserts many records at a time

a = encodedlistvalue=base64.b64encode(
    """# Larger example that inserts many records at a time
import sqlite3
import base64
conn = sqlite3.connect('/home/jack/Desktop/testPy.db')
c = conn.cursor()
# Larger example that inserts many records at a time

a = encodedlistvalue=base64.b64encode(
    xxccccc# Larger example that inserts many records at a time)
#c.execute("INSERT INTO python VALUES (?, ?)" a, b)
#c.execute("INSERT INTO python VALUES (%s, %s,)", (a, b))
c.execute("INSERT INTO python VALUES (?,?)", (a,b))

conn.commit()
conn.close()    
    """)

b = 'example'

c.execute("INSERT INTO python VALUES (?,?)", (a,b))

conn.commit()
conn.close()


import sqlite3
import base64

#Create a database to use base64: 
conn = sqlite3.connect('ipydb64.db')

c = conn.cursor()



file = 'base64 encoding allows code to be stored and retieved in the same format it was posted'
b = '4Webstuff, gwebsite, gghtml'
encodedlistvalue=base64.b64encode(file)

c.execute("INSERT INTO python VALUES (?,?)", (encodedlistvalue, b))

conn.commit()
conn.close()



import sqlite3
conn = sqlite3.connect('ipydb64.db')
c = conn.cursor()# Never 
for row in c.execute('SELECT * FROM python ORDER BY code'):
        print(row),"\n-----\n"

import sqlite3
conn = sqlite3.connect('ipydb64.db')
c = conn.cursor()# Never 
for row in c.execute('SELECT * FROM python ORDER BY code'):
        #print(row),"\n-----\n","\n"
        
        data= row[0],
        print data
        

import sqlite3
conn = sqlite3.connect('ipydb64.db')

c = conn.cursor()# Never 
for row in c.execute('SELECT * FROM python ORDER BY code'):
                
        s2 = row[0].encode('ascii')
        encodedlistvalue=base64.b64decode(s2)
        print encodedlistvalue, '\n', 'Keywords:', row[1], '\n -----------------------------\n'

        

conn = sqlite3.connect('ipydb64.db')
c = conn.cursor()# Never 

t = ('example',)
for row in c.execute('SELECT * FROM python WHERE keyword=?', t):
                
        s2 = row[0].encode('ascii')
        encodedlistvalue=base64.b64decode(s2)
        print encodedlistvalue, '\n', 'Keywords:', row[1], '\n -----------------------------\n'


conn = sqlite3.connect('ipydb64.db')
c = conn.cursor()# Never 

t = ('example',)
for row in c.execute('SELECT code FROM python WHERE keyword=?', t):

    #subjectList = [row[0] for row in c.fetchall()]        
    code = row[0].encode('ascii')
    
    #for row in data :
    encodedlistvalue=base64.b64decode(code)
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


import sqlite3
import base64
conn = sqlite3.connect('ipydb64.db')
c = conn.cursor()# Never 

k = ('4Webstuff',)
c.execute('SELECT * FROM python WHERE keyword=?', k)

subjectList = [row[0] for row in c.fetchall()]        
#print row[0]
#for row in data :
encodedlistvalue=base64.b64decode(row[0])
print encodedlistvalue, '\n', 'Keywords:', row[1], '\n -----------------------------\n'


import sqlite3
conn = sqlite3.connect('/home/jack/Desktop/testPy.db')
c = conn.cursor()# Never 
#for row in c.execute('SELECT code FROM python ORDER BY keyword'):
s = ('committed',)
c.execute('SELECT code FROM python WHERE keyword=?', s)
        
          
print(c.fetchone())


import sqlite3
conn = sqlite3.connect('/home/jack/Desktop/testPy.db')
c = conn.cursor()# Never do this -- insecure!
#    symbol = 'RHAT'
#    c.execute("SELECT * FROM python WHERE symbol = '%s'" % symbol)

# Do this instead
t = ('Html',)
c.execute('SELECT * FROM python WHERE keyword=?', t)
print(c.fetchone())


import sqlite3
conn = sqlite3.connect('/home/jack/Desktop/testPy.db')
c = conn.cursor()# Never 
for row in c.execute('SELECT * FROM python ORDER BY code'):
        #print(row),"\n-----\n","\n"
          
        data = c.fetchall()
        print data

import sqlite3
conn = sqlite3.connect('/home/jack/Desktop/testPy.db')
c = conn.cursor()# Never 
for row in c.execute('SELECT * FROM python ORDER BY code'):
        #print(row),"\n-----\n","\n"
        
        print row[0],"\n",row[1],"\n-----\n",

import sqlite3
conn = sqlite3.connect('/home/jack/Desktop/testPy.db')
c = conn.cursor()# Never do this -- insecure!

t = ('Webstuff',)
c.execute('SELECT * FROM python ORDER BY keyword')
print(c.fetchall())
conn.close()


import sqlite3
conn = sqlite3.connect('/home/jack/Desktop/main.db')

c = conn.cursor()

# DROP TABLE IF EXISTS
c.execute("DROP TABLE IF EXISTS Products")

import sqlite3
conn = sqlite3.connect('/home/jack/Desktop/main.db')
c = conn.cursor()
# Create table
c.execute("""CREATE TABLE Products (
             contact_id integer PRIMARY KEY,
             CatID text NOT NULL,
             description text NOT NULL,
             keywords text NOT NULL);
          """)
conn.commit()
conn.close()

import re
import textwrap
import sqlite3
conn = sqlite3.connect('data/fts3hurricane.db')
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE hurricane
             (hurricane text)''')
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
        c.execute("INSERT INTO hurricane VALUES (?)", words)
        conn.commit()
        conn.close()        

import sqlite3
def insert_product(product):
    with sqlite3.connect("fullsearch.db") as db:
        cursor = db.cursor()
        sql = "insert into Products (CatID,description,keywords) values (?, ?, ?)"
        cursor.execute(sql, product)
        db.commit()

if __name__ == "__main__":
    
    ID= int(input("enter the CatID of the product:>> "))
    Des = raw_input("Enter description: >>")
    Keywords = raw_input("Enter keywords: >>")
    product = (ID, Des, Keywords)
    insert_product(product)
    
    
    

import sqlite3
def insert_product(product):
    with sqlite3.connect("/home/jack/Desktop/main.db") as db:
        cursor = db.cursor()
        sql = "insert into Products (CatID,description,keywords) values (?, ?, ?)"
        cursor.execute(sql, product)
        db.commit()

if __name__ == "__main__":
    ID= input("enter the CatID of the product:>> "
    Des = raw_input("Enter description: >>")
    Keywords = raw_input("Enter keywords: >>")
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
    with sqlite3.connect("/home/jack/Desktop/main.db") as db:
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
conn = sqlite3.connect("/home/jack/Desktop/main.db", isolation_level=None ,timeout=30000) 
print("Opened database successfully")
conn.close()


import sqlite3
conn = sqlite3.connect('/home/jack/Desktop/main.db')
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
    with sqlite3.connect("/home/jack/Desktop/main.db") as db:
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
print test.result

/etc/mysql/mysql.conf.d/mysqld.cnf

import MySQLdb
help(MySQLdb)

#Works
import MySQLdb as db
con = db.connect("localhost","root","ThinkPadT$#")
cur = con.cursor()
cur.execute('CREATE DATABASE testdb2;')

import MySQLdb as db
con = db.connect("localhost","root","ThinkPadT$#", "testdb2")
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Writers")
    cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 Name VARCHAR(500))")
    cur.execute("INSERT INTO Writers(Name) VALUES('Jack Northrup')")
    #cur.execute("INSERT INTO Writers(Name) VALUES('Henry Wadjob')")
    #cur.execute("INSERT INTO Writers(Name) VALUES('Klepto Manic')")
    #cur.execute("INSERT INTO Writers(Name) VALUES('Emila gray')")
    #cur.execute("INSERT INTO Writers(Name) VALUES('Mike Stupoff')")

# works 
import MySQLdb as db
import json 
import base64
    
con = db.connect("localhost","root","ThinkPadT$#", "testdb2")
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
    cur.execute("INSERT INTO Writers(Name) VALUES('%s')" % (encodedlistvalue))

# WORKS
#!/usr/bin/python
# import the MySQLdb and sys modules
import MySQLdb
import sys
import base64
# open a database connection
# be sure to change the host IP address, username, password and database name to match your own

con = db.connect("localhost","root","ThinkPadT$#", "testdb2")

# prepare a cursor object using cursor() method
#cursor = connection.cursor ()
cur = con.cursor()

# execute the SQL query using execute() method.
cur.execute ("select Id, Name from Writers")

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

Create a MySQL Database with Python

# Works
import MySQLdb as db
con = db.connect("localhost","root","ThinkPadT$#")
cur = con.cursor()
cur.execute('CREATE DATABASE searchdb01;')

# works 
import MySQLdb as db
import json 
import base64
    
con = db.connect("localhost","root","ThinkPadT$#", "searchdb01")
file = """[mylist.jsn
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
    cur.execute("CREATE TABLE Code(Id INT PRIMARY KEY AUTO_INCREMENT, \
                  Name VARCHAR(2500), Keywords VARCHAR(500))")
    #cur.execute("INSERT INTO Code(Name) VALUES('%s')" % (encodedlistvalue))
    cur.execute("INSERT INTO Code(Name, Keywords) VALUES('%s','%s')" % (encodedlistvalue, keywords))

#Works
import MySQLdb as db
con = db.connect("localhost","root","ThinkPadT$#")
cur = con.cursor()
cur.execute('CREATE DATABASE searchdb01;')

# works 
import MySQLdb as db
import json 
import base64
    
con = db.connect("localhost","root","ThinkPadT$#", "searchdb01")
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
    
con = db.connect("localhost","root","ThinkPadT$#", "searchdb01")
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
con = db.connect("localhost","root","ThinkPadT$#", "searchdb01")

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

#!/usr/bin/python
import MySQLdb
import sys
import base64
con = db.connect("localhost","root"," ", "searchdb01")
cur = con.cursor()
# execute the SQL query using execute() method.
cur.execute ("select Id, Name, Keywords from Code")

data = cur.fetchall ()
# print the rows
for row in data :
    encodedlistvalue=base64.b64decode(row[1])
    print row[0], encodedlistvalue, '\n', 'Keywords:', row[2],\
    '\n -----------------------------\n'
# close the cursor object
cur.close ()
# close the connection
con.close ()
# exit the program
sys.exit()

import MySQLdb
con = db.connect("localhost","root","ThinkPadT$#", "searchdb01")

param = "lesson"
c = con.cursor()
c.execute("SELECT * FROM Code WHERE Keywords LIKE %s LIMIT 1", ("%" + param + "%",))

data = c.fetchall()
for row in data :
    encodedlistvalue=base64.b64decode(row[1])
    print row[0], encodedlistvalue, '\n', 'Keywords:', row[2],\
    '\n -----------------------------\n'
c.close()

import MySQLdb
con = db.connect("localhost","root","ThinkPadT$#", "searchdb01")

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

data = %load mylist
print data

# works 
import MySQLdb as db
import json 
import base64
    
con = db.connect("localhost","root","ThinkPadT$#", "searchdb01")
c = con.cursor()
#data = %load mylist
keywords = """
data, webite, cut paste, 87er
"""
encodedlistvalue=base64.b64encode('%load mylist')
# Put this through to SQL using an INSERT statement...
c.execute("""INSERT INTO Code (Name, Keywords)
                   VALUES(%s, %s)""", (encodedlistvalue, keywords))


# works 
import MySQLdb as db
import json 
import base64
    
con = db.connect("localhost","root","ThinkPadT$#", "searchdb01")

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

SET PASSWORD FOR 'root'@'localhost' = PASSWORD('ThinkPadT$#');

To change password:
sudo dpkg-reconfigure mysql-server-5.5

SET PASSWORD FOR 'root'@'localhost' = PASSWORD('ThinkPadT$#');

To change password:
sudo dpkg-reconfigure mysql-server-5.5


sudo mysql -u root
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('ThinkPadT$#');
CREATE USER 'jack'@'localhost' IDENTIFIED BY 'ThinkPadT$#';
GRANT ALL PRIVILEGES ON * . * TO 'jack'@'localhost';
FLUSH PRIVILEGES;

def createdb(dbnew):
    import sqlite3
    conn = sqlite3.connect(dbnew)
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
    
dbnew = "newdb.db"    
createdb(dbnew)    

createdb("newdatabase02")

import sqlite3
conn = sqlite3.connect('newdatabase02')

c = conn.cursor()
c.execute("INSERT INTO Junk VALUES ('SQLite','Junkstuff, stuff, sql','beans')")  
conn.commit()

conn.close()

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

c.execute("INSERT INTO Junk VALUES (?, ?, ?);", (language, keywords, encodedlistvalue))
# Save (commit) the changes
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




import sqlite3
conn = sqlite3.connect('newdatabase02')

c = conn.cursor()
s = ('stuff',)
#c.execute('SELECT * FROM Junk WHERE keywords=?', s)
rows = c.execute('SELECT * FROM Junk')
for row in rows:
    print row

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO python VALUES (?,?,?,?,?)', purchases)

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

Image(filename='snippets/database001.png')

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

def insert_picture(conn, picture_file):
    with open(picture_file, 'rb') as input_file:
        ablob = input_file.read()
        base=os.path.basename(picture_file)
        afile, ext = os.path.splitext(base)
        sql = '''INSERT INTO PICTURES
        (PICTURE, TYPE, FILE_NAME)
        VALUES(?, ?, ?);'''
        conn.execute(sql,[sqlite3.Binary(ablob), ext, afile]) 
        conn.commit()

conn = create_or_open_db('image.db')

picture_file = "snippets/database001.png"
insert_picture(conn, picture_file)
conn.close()

def extract_picture(cursor, picture_id):
    sql = "SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = :id"
    param = {'id': picture_id}
    cursor.execute(sql, param)
    ablob, ext, afile = cursor.fetchone()
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    return filename

conn = create_or_open_db('image.db')
cur = conn.cursor()
filename = extract_picture(cur, 1)
cur.close()
conn.close()
Image(filename='./'+filename)

conn = create_or_open_db('image.db')
conn.execute("DELETE FROM PICTURES")
for fn in picture_list:
    picture_file = "snippets/"+fn
    insert_picture(conn, picture_file)
     
for r in conn.execute("SELECT rowid, FILE_NAME FROM PICTURES"):
    print r[0],r[1]

conn.close()

# Get your image from the database

def get_image(cursor, picture_id):
    sql = "SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = 130"
    param = {'id': picture_id}
    cursor.execute(sql, param)
    ablob, ext, afile = cursor.fetchone()
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    return filename

conn = create_or_open_db('image.db')
cur = conn.cursor()
filename = get_image(cur, 1)
cur.close()
conn.close()
print filename
Image(filename=filename)


import sqlite3
#response = requests.get("/home/jack/Desktop/text_stuff/snippets/database001.png")
response = "/home/jack/Desktop/text_stuff/snippets/database001.png"
#photo = "snippet"
member_name = "snippetImage"
#response = requests.get(picture_url) #url is definitely correct
#picture = sqlite3.Binary(response.content)
picture = sqlite3.Binary(response)
con = sqlite3.connect("image.db")
cursor = con.cursor()
#sql = '''CREATE TABLE member_data(id integer primary key autoincrement, picture BLOB, name TEXT);'''
#cursor.execute(sql)

sql = 'INSERT INTO member_data (picture, name) VALUES (?, ?)', cursor.execute(sql, (picture, member_name))
cursor.execute(sql)
con.commit()

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

def insert_picture(conn, picture_file):
    with open(picture_file, 'rb') as input_file:
        ablob = input_file.read()
        base=os.path.basename(picture_file)
        afile, ext = os.path.splitext(base)
        sql = '''INSERT INTO PICTURES
        (PICTURE, TYPE, FILE_NAME)
        VALUES(?, ?, ?);'''
        conn.execute(sql,[sqlite3.Binary(ablob), ext, afile]) 
        conn.commit()

def loadimages(dbname, path):
    conn = sqlite3.connect(dbname)
    #conn.execute("DELETE FROM PICTURES")
    for fn in picture_list:
        picture_file = path+"/"+fn
        insert_picture(conn, picture_file)

    for r in conn.execute("SELECT rowid, FILE_NAME FROM PICTURES"):
        print r[0],r[1]
   
    conn.close()


def get_image(cursor, picture_id):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute("SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = ?;",(picture_id,))
    #sql = "SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = 19"
    param = {'id': picture_id}
    cursor.execute(sql, param)
    ablob, ext, afile = cursor.fetchone()
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    return filename


dbname = "ImageB.db"
db_file = create_or_open_db(dbname)
path = "snippets/"
loadimages(dbname, path)
cur = conn.cursor()
filename = get_image(cur, 16)
cur.close()
conn.close()
print filename
Image(filename=filename)


-

def get_image(cursor, picture_id):
    sql = "SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = 19"
    param = {'id': picture_id}
    cursor.execute(sql, param)
    ablob, ext, afile = cursor.fetchone()
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    return filename

conn = create_or_open_db('ImageB.db')
cur = conn.cursor()
filename = get_image(cur, 1)
cur.close()
conn.close()
print filename
Image(filename=filename)


def get_image(cursor, image_id):
    
    #c.execute("SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = ?;",(image_id,))
    #image_id = 19
    #sql = "SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = ?;",(image_id,)
    #sql = "SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = 19"
    #param = {'id': image_id}
    #cursor.execute(sql, param)
    cursor.execute("SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = ?;",(image_id,))
    #cursor.execute("SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = 19")
    ablob, ext, afile = cursor.fetchone()
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    return filename

conn = create_or_open_db('ImageB.db')
cur = conn.cursor()
filename = get_image(cur, 19)
cur.close()
conn.close()
print filename
Image(filename=filename)


import sqlite3
def get_image(cursor, image_id):
    
    cursor.execute("SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = ?;",(image_id,))
    ablob, ext, afile = cursor.fetchone()
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    return filename

conn = create_or_open_db('ImageB.db')
cur = conn.cursor()
filename = get_image(cur, 19)
cur.close()
conn.close()
print filename
Image(filename=filename)


import Image2Data
dbname = "ImageD.db"
Image2Data.image_id(dbname)

import sqlite3
conn = sqlite3.connect('image.db')
c = conn.cursor()
c.execute("""
CREATE VIRTUAL TABLE File 
USING FTS3(id, name, image);
""")
conn.commit()
conn.close()

conn = sqlite3.connect('newdatabase02')
c = conn.cursor()
c.execute('insert into File 
(id, name, bin) values (?,?,?)', (id, name, sqlite3.Binary(file.read())))
conn.commit()
conn.close()

from time import sleep
import sqlite3

file0 = open("history.txt","r")
lists = file0.readlines()
for list in lists:
    sleep(.5)
    print list

from time import sleep
import sqlite3
conn = sqlite3.connect('history.db')
c = conn.cursor()
conn.text_factory = str
c.execute("""
CREATE VIRTUAL TABLE history 
USING FTS3(text);
""")
conn.commit()
conn.close()

fileO = open("history.txt","r")
lists = fileO.readlines()
for list in lists:
    #list = list.encode("ascii", "ignore")
    list = list.decode('utf-8').strip() 
    conn = sqlite3.connect('history.db')
    c = conn.cursor()
    c.execute('insert into history values (?)', (list,))
    conn.commit()
    conn.close()

import sqlite3
import sys
conn = sqlite3.connect('history2.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
search = raw_input("Search : ")
for row in c.execute('SELECT rowid, text FROM history WHERE text MATCH ?', (search,)):    
    count=count+1
    print (row)[0],"-",(row)[1],"\n"
    if count > req:
        conn.close()
        sys.exit()

from time import sleep
import sqlite3
conn = sqlite3.connect('history.db')
c = conn.cursor()
search = ("sudo")
for row in c.execute('SELECT rowid, text FROM history WHERE text LIKE (?)', (search,)):
    print row[0],row[1]


import sqlite3
import sys
conn = sqlite3.connect('history.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
id1 = raw_input("Starting ID : ")
id2 = raw_input("How Many Rows : ")
for row in c.execute('SELECT rowid, * from history LIMIT ? OFFSET ?',  (id2, id1)):
    count=count+1
    print (row)[0],"-",(row)[1],
    if count > req:
        conn.close()
        sys.exit()



from time import sleep
import sqlite3
conn = sqlite3.connect('fts4.db')
c = conn.cursor()
conn.text_factory = str
# Create an FTS4 table named "pages" with one column: code
c.execute("""
CREATE VIRTUAL TABLE pages USING fts4(code);
""")
conn.commit()
conn.close()


import DBstore
insert="""
def dbstore(insert):
    import sqlite3
    conn = sqlite3.connect('XPfts4.db')
    c = conn.cursor()
    c.execute(""
    CREATE VIRTUAL TABLE IF NOT EXISTS code 
    USING FTS3(code);
    ""
    )
    c = conn.cursor()
    conn.text_factory = str
    # CREATE VIRTUAL TABLE pages USING fts4(code);
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
quick database QUICKdb QUICK
"""
DBstore.dbstore(insert)

!rm DBread.pyc

%%writefile DBread.py
def dbread():
    import sqlite3
    conn = sqlite3.connect('XPfts4.db')
    c = conn.cursor()
    count = 0
    req = 100
    view = raw_input("Search : ")
    for row in c.execute('SELECT rowid, code FROM pages WHERE pages MATCH ?', (view,)):    
        count=count+1
        print (row)[0],"-",(row)[1],"\n"
        if count > req:
            conn.close()
            sys.exit()

import DBread
DBread.dbread()

%reset -f

%%writefile DBstore.py
def dbstore(insert):
    import sqlite3
    conn = sqlite3.connect('XPfts4.db')
    c = conn.cursor()
    c.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS pages 
    USING FTS3(code);
    """
    )
    c = conn.cursor()
    conn.text_factory = str
    # CREATE VIRTUAL TABLE pages USING fts4(code);
    c.execute("INSERT INTO pages VALUES(?)", (insert,))

    conn.commit()
    conn.close()

%%writefile QUICKdb.py
def dbstore(insert):
    import sqlite3
    conn = sqlite3.connect('XPfts4.db')
    c = conn.cursor()
    c.execute("""CREATE VIRTUAL TABLE IF NOT EXISTS history 
    USING FTS3(hist);
    """
             )
    c = conn.cursor()
    conn.text_factory = str
    # CREATE VIRTUAL TABLE pages USING fts4(code);
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


!rm QUICKdb.pyc

import QUICKdb
insert="""
def dbstore(insert):
    import sqlite3
    conn = sqlite3.connect('XPfts4.db')
    c = conn.cursor()
    c.execute(""
    CREATE VIRTUAL TABLE IF NOT EXISTS code 
    USING FTS3(code);
    ""
    )
    c = conn.cursor()
    conn.text_factory = str
    # CREATE VIRTUAL TABLE pages USING fts4(code);
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
quick database QUICKdb QUICK
"""
QUICKdb.dbstore(insert)

%%writefile DBread.py
def dbread(insert):
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

import sqlite3
conn = sqlite3.connect('fts4.db')
c = conn.cursor()
conn.text_factory = str
# CREATE VIRTUAL TABLE pages USING fts4(code);
req = 100
view = raw_input("Search : ")
for row in c.execute('SELECT rowid, code FROM pages WHERE pages MATCH ?', (view,)):    
    count=count+1
    print (row)[0],"-",(row)[1],"\n"
    if count > req:
        conn.close()
        sys.exit()





search = raw_input("find  ")
file = open("ToUse.txt")
lines = file.readlines()
for line in lines:
    if search in line:print line
    if search == True:
        file.close()
        exit()
file.close()


%reset -f

import markovify
f = open("virtual.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
STR = (text_model.make_short_sentence(140))
savE = open('savE.txt', 'a')
savE.write(STR)
savE.close()
print STR

import re
def periodpattern():
    with open('savE.txt') as infile:
        for line in infile:
            line = line.replace(" ‘","")
            line = line.replace("’","")
            line = line.replace(".",".\n")
            line = line.replace("!","!\n")
            line = line.replace("?","?\n")
            
            print line
            outfile2 = open('savE_patern.txt', 'w')
            outfile2.write(line)  # non-empty
            outfile2.close()
            
periodpattern()            


import markovify
import time
f = open("grimm.txt")
text = f.read()
text_model_a = markovify.Text(text)


ebook_b =open('hekel.txt')
text0 = ebook_b.read()
text_model_b = markovify.Text(text0)
for i in range(5):
    print(text_model_b.make_short_sentence(140))
    STR0 = (text_model_b.make_short_sentence(140))
    savE = open('savE.txt', 'a')
    savE.write(STR0)
    savE.close()

# 2. Print five randomly-generated sentences
for i in range(5):
    print(text_model_a.make_short_sentence(140))
    STR = (text_model_a.make_short_sentence(140))
    savE = open('savE.txt', 'a')
    savE.write(STR)
    savE.close()
# 3. Print three randomly-generated sentences of no more than 140 characters
for i in range(5):
    print(text_model_a.make_short_sentence(140))
    STR2 = (text_model_a.make_short_sentence(140))
    savE = open('savE.txt', 'a')
    savE.write(STR2)
    savE.close()
# Combine the models into a single one
both_models = markovify.combine([text_model_a,text_model_b])
for i in range(5):
    print(both_models.make_short_sentence(140))    
    STR3 = (both_models.make_short_sentence(140))  
    savE = open('savE.txt', 'a')
    savE.write(STR3)
    savE.close()    

with open("textfile.txt") as openfile:
    for line in openfile:
        for part in line.split():
            if "color=" in part:
                print part

def words(stringIterable):
    #upcast the argument to an iterator, if it's an iterator already, it stays the same
    lineStream = iter(stringIterable)
    for line in lineStream: #enumerate the lines
        for word in line.split(): #further break them down
            print word

for lines in content[0].split():
    for split0 in lines.split(' '):
        for split1 in split0.split(','):
            for split2 in split1.split('.'):
                for split3 in split2.split('?'):
                    for split4 in split3.split('!'):
                        for word in split4.split(':'): 
                            if word != "":
                                print(word)

delimiters = ['\n', ' ', ',', '.', '?', '!', ':', 'and_what_else_you_need']
words = content
for delimiter in delimiters:
    new_words = []
    for word in words:
        new_words += word.split(delimiter)
    words = new_words


import re
delimiters = ['\n', ' ', ',', '.', '?', '!', ':', 'and_what_else_you_need']
words = re.split('|'.join(delimiters), content)

!rm snippet.db

import sqlite3
conn = sqlite3.connect('snippet.db')
c = conn.cursor()
c.execute("""
CREATE VIRTUAL TABLE snippet 
USING FTS3(base64, text, keywords);
""")
conn.commit()
conn.close()

import sqlite3
import base64

#Connect to database: 
conn = sqlite3.connect('snippet.db')
c = conn.cursor()

#Single lines do not need the three quotes
file = """
def insert_info(store):
    with sqlite3.connect("misc.db") as db:
        #use a text_factory that can interpret 8-bit bytestrings 
        db.text_factory = str
        cursor = db.cursor()
        #db.text_factory = str
        sql = "insert into storeit (data0, data1, data2) values (?, ?, ?)"
        cursor.execute(sql, store)
        db.commit()
        
        OR
        conn.text_factory = str
"""
encodedlistvalue=base64.b64encode(file)
b = 'text_factory, 8-bit bytestrings, 8-bit'

c.execute("INSERT INTO snippet VALUES (?,?,?)", (encodedlistvalue, file, b))

conn.commit()
conn.close()


import sqlite3
conn = sqlite3.connect('snippet.db')
c = conn.cursor()
for row in c.execute('SELECT rowid,base64, text, keywords FROM snippet ORDER BY ROWID'):
        print(row),"\n-----\n"
        # notice the Keywords are plain text even the base64 is displayed as unicode (u'IyBMYXJ .... )

could you tell me how I can fix anything with no FTP or Cpanel access

import sqlite3
conn = sqlite3.connect('snippet.db')

c = conn.cursor()# Never 
for row in c.execute('SELECT rowid,base64, text, keywords FROM snippet ORDER BY ROWID'):
                
        # display as asci instead of unicode
        s2 = row[1].encode('ascii')
        #decode the base64 stored data
        encodedlistvalue=base64.b64decode(s2)
        #print row[0],"\n",encodedlistvalue, '\n', row[2], '\nKeywords:',row[3],'\n -----------------------------\n'
        print row[0],"\n",encodedlistvalue, '\n', '\nKeywords:',row[3],'\n -----------------------------\n'

        

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
fname="bible2.txt"
file_len(fname)

!ls *.csv

import time
from itertools import islice
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
fname="elonmusk.txt"
lineS = file_len(fname)
print lineS

import time
from itertools import islice
with open("elonmusk.txt") as lines:    
    heads = list(islice(lines, 8))
    for head in heads:
        time.sleep(1)
        print head


!rm misc.db

import sqlite3
conn = sqlite3.connect('misc.db')
c = conn.cursor()
c.execute("CREATE VIRTUAL TABLE storeit USING FTS3(data0, data1, data2);")
conn.commit()
conn.close()

import sqlite3
def insert_info(store):
    with sqlite3.connect("misc.db") as db:
        #use a text_factory that can interpret 8-bit bytestrings 
        db.text_factory = str
        cursor = db.cursor()
        #db.text_factory = str
        sql = "insert into storeit (data0, data1, data2) values (?, ?, ?)"
        cursor.execute(sql, store)
        db.commit()

#if __name__ == "__main__":
print "You will be promted to enter data1, data2, and data2 "  
data0 = raw_input("Enter data0: >>")
data1 = raw_input("Enter data12: >>")
data2 = raw_input("Enter data2: >>")
store = (data0,data1,data2)
insert_info(store)

import sqlite3
conn = sqlite3.connect('misc.db')
c = conn.cursor()# Never do this -- insecure!
for row in c.execute('SELECT rowid, * FROM storeit ORDER BY rowid'):
        print row[0],"  ",row[1],"  ",row[2], row[3],"\n-----\n",

conn.close()


lines = open("elonmusk.txt","r")
#lines = open("realDonaldTrump.txt","r")
line = lines.readline()
count = 0
for line in lines:
    #if "Hillary" in line :
    #if "FakeNews" in line :
    if "future" in line :
        count=count+1
        print count,"-",line 

outf = open("symmetrymag.txt", "w") 
outf.close() 

from itertools import tee
count=0
with open("symmetrymag_tweets.csv") as inf:
    for line in inf:
        lines  = line[39:]
        outf = open("symmetrymag.txt", "a") 
        outf.write(lines)
outf.close() 

from itertools import tee
count=0
with open("TEDTalks_tweets.csv") as inf:
    for line in inf:
        lines  = line[39:]
        outf = open("TEDTalks.txt", "a") 
        outf.write(lines)
outf.close() 

import sqlite3
conn = sqlite3.connect('collection.db')
c = conn.cursor()
c.execute("""
CREATE VIRTUAL TABLE tweets 
USING FTS3(text, account);
""")
conn.commit()
conn.close()

import sqlite3
import time
#account = "TEDTalks.txt"
#account = "elonmusk.txt"
account = "realDonaldTrump.txt"
print account[:-4]

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

conn.commit()
conn.close()                 

import sqlite3
import sys
conn = sqlite3.connect('collection.db')
c = conn.cursor()
count=0
req=100
for row in c.execute('SELECT rowid,* FROM tweets WHERE text MATCH "future"'):
    count=count+1
    #print count,"by",(row)[2],"\n",(row)[1],"\n"
    print count,"-",(row)[1]," -- by",(row)[2],"\n"
    if count > req:
        conn.close()
        sys.exit()

results = cursor.execute("SELECT username, password "
                         "FROM logins WHERE username = ?", (username,))

import sys
sys.path.insert(0,"/usr/local/lib/python2.7/dist-packages/")
import pyephem


import Here
Lt = Here.here[0]
Lo = Here.here[1]
print Lt,Lo

!python /usr/local/lib/python2.7/dist-packages/pyephem-3.7.6.0.dist-info/INSTALLER

import sqlite3
import sys
conn = sqlite3.connect('collection.db')
c = conn.cursor()
count=0
req=100
search = "future"
#for row in c.execute('SELECT rowid,* FROM tweets WHERE text MATCH %s' % search):
for row in c.execute('SELECT rowid,* FROM tweets WHERE text MATCH ?', (search,)):    
    count=count+1
    #print count,"by",(row)[2],"\n",(row)[1],"\n"
    print count,"-",(row)[1]," -- by",(row)[2],"\n"
    if count > req:
        conn.close()
        sys.exit()



import sqlite3
import sys
conn = sqlite3.connect('collection.db')
c = conn.cursor()
count=0
requ=200
search = raw_input("Search")
#for row in c.execute('SELECT rowid,* FROM tweets WHERE text MATCH %s' % search):
for row in c.execute('SELECT rowid,* FROM tweets WHERE text MATCH ?', (search,)):    
    count=count+1
    #print count,"by",(row)[2],"\n",(row)[1],"\n"
    print count,"-",(row)[1]," -- by",(row)[2],"\n"
    if count > req:
        conn.close()
        sys.exit()

!ls *.txt

import fileinput
somefile = raw_input("FileName :")
string = raw_input("TextSearch :")
lines = open(somefile,"r")
for line in lines:
    if string in line:
        print line
        f.close() 

import Txmanip
help(Txmanip)

%%writefile /home/jack/anaconda2/lib/python2.7/site-packages/Txmanip/FindReplace.py
# Finds a string in a file, prints the line then opens an input window to replace the line 
def findreplace():
    import fileinput
    print 'If Search is true and no data is entered, the line will be deleted.'
    somefile = raw_input("FileName :")
    string = raw_input("TextSearch :")
    lines = open(somefile,"r")
    for line in lines:
        if string in line:
            print line
 

    for line in fileinput.input(somefile, inplace=True):
        if string in line:
            # input the whole line as you wish edited
            change = raw_input('Create New Line :') 
            if change != "": line = change
            print line
            #print line,
            #print 'this goes after the line'
        else:
            print line, # just print the line anyway
      

from Txmanip import FindReplace
FindReplace.findreplace()

%reset -f

import fileinput
import time
print 'If Search is true and no data is entered, the line will be deleted.'
somefile = raw_input("FileName :")
string = raw_input("TextSearch :")
for line in fileinput.input(somefile, inplace=True):
    if string in line:
        # input the whole line as you wish edited
        
        time.sleep(3)
        change = raw_input('Edit New Line :')
        if change != "": line = change
        print line
        #print line,
        #print 'this goes after the line'
    else:
        print line, # just print the line anyway
        
        
fileinput.close()        

f=open(filename)
count=0
starT = 0
enD = 5
lines = f.readline().strip()
for line in lines:
    count = count+1
    if count > starT:
        print "LineNumber :",count,"\n",line,"\n"
        if count >enD:f.close()
            

import sys
filename = "virtual.txt"   
count=0;starT = 0;enD = 5
file =open(filename)
lines = file.readlines() # .strip()
for line in lines:
    count=count+1
    if count>starT and count<enD:
        print line
          

search = raw_input("find  : ")
file = open("virtual.txt", "r")
lines = file.readlines()
for line in lines:
    if search in line:
        print line

file.close()

from Txmanip import HeadFirst
filename = 'virtual.txt'
HeadFirst.headFirst(filename)

!rm substitute.py


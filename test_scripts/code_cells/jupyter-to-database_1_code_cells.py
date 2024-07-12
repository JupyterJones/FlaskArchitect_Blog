!ls *.ipynb >>ipynb2.list

from time import sleep
title = "ipynb2.list"
NOTEBOOK = []
lines = open(title,"r")
for line in lines.readlines():
    line = line.replace("\n","") 
    print (line)
    NOTEBOOK.append(line)

import json
import sys
from time import sleep
import sqlite3
import csv
database = "oct1_IPNB.list.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
count=1
search = input("Title: ")
# ONLY the DATA table can use MATCH
for row in c.execute('SELECT rowid,* FROM ipynb WHERE ipynb MATCH ?',(search,)):
    if search in row[1] or search in row[3]:
        print (row[0],row[1],row[3],"\n----------------------")
        count=count+1
        if count>20:break
c.close()
conn.close()


        

import json
import sys
from time import sleep
import sqlite3
import csv
database = "oct1_IPNB.list.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
count=1
search = input("Title :")
# ONLY the DATA table can use MATCH
for row in c.execute('SELECT rowid, file, content, description FROM ipynb WHERE description MATCH ?',(search,)):
    print (row[0],row[1],row[3],"\n----------------------")
    count=count+1
    if count>13:break
c.close()
conn.close()


        

import json
import sys
from time import sleep
import sqlite3
import csv
database = "oct1_IPNB.list.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
search = input("ROWID :")
for row in c.execute('SELECT rowid, file, content, description FROM ipynb WHERE rowid = ?',(search,)):
    print (row[2])
c.close()
conn.close()

import json
import sys
from time import sleep
import sqlite3
import csv
database = "oct1_IPNB.list.db"

conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
search = input("ID :")
#filename = search+"DB.ipynb"
#f= open(filename,"w");f.close()
SEARCH = int(search)+1
for row in c.execute('SELECT content FROM ipynb WHERE rowid == ?', (SEARCH,)):
        filename = "Database-reprint_"+row[0]
print (filename)        
with open(filename, 'w') as outfile:
    for row in c.execute('SELECT content FROM ipynb WHERE rowid == ?', (search,)):
        row0 = row[0]
        row0 =str(row0)+"\n"
        row0=row0.replace("\\\\","\\")
        outfile.write(row0)
        #print row0
print (filename)        
conn.close()
outfile.close()


  # 427      







import json
import sys
from time import sleep
import sqlite3
import csv
database = "oct1_IPNB.list.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
search = input("ROWID :")
for row in c.execute('SELECT rowid, file, content, description FROM ipynb WHERE rowid = ?',(search,)):
    print (row[2])
c.close()
conn.close()

!sqlite3 /home/jack/nov19b.db "pragma integrity_check;"

import sqlite3
database = "oct1_IPNB.list.db"
conn = sqlite3.connect(database)
conn.text_factory=str
c = conn.cursor()
c.execute("SELECT COUNT(*) from ipynb")
(number_of_rows,)=c.fetchone()
print (number_of_rows,) 

!ls /home/jack/*.db

!rm /home/jack/Desktop/PROCESSING/Processing/nov19b.db

file = "oct1_IPNB.list.db"
import os.path, time
print("last modified: %s" % time.ctime(os.path.getmtime(file)))
print("created: %s" % time.ctime(os.path.getctime(file)))

!ls /home/jack/nov19b.db

!locate nov19b.db

import json
import sys
from time import sleep
import sqlite3
import csv
database = "oct1_IPNB.list.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
count=1
search = input("Title :")
# ONLY the DATA table can use MATCH
for row in c.execute('SELECT rowid, file, content, description FROM ipynb WHERE content MATCH ?',(search,)):
    print (row[0],row[1],row[3],"\n----------------------")
    count=count+1
    if count>25:break
c.close()
conn.close()

import json
import sys
from time import sleep
import sqlite3
import csv
database = "oct1_IPNB.list.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
count=1
search = input("Title :")
for row in c.execute('SELECT rowid, file, content, description FROM ipynb WHERE content MATCH ?',(search,)):
    print (row[0],row[1],row[3],"\n----------------------")
    count=count+1
    if count>10:break
c.close()
conn.close()


        

import json
import sys
from time import sleep
import sqlite3
import csv
database = "oct1_IPNB.list.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
count=1
search = input("ROWID :")
for row in c.execute('SELECT rowid, file, content, description FROM ipynb WHERE rowid = ?',(search,)):
    print (row[0],row[1],row[3],"\n----------------------")
    count=count+1
    if count>10:break
c.close()
conn.close()


        

import json
import sys
from time import sleep
import sqlite3
import csv
database = "oct1_IPNB.list.db"

conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
search = input("FileName :")
f= open(search,"w");f.close()
with open(search, 'a') as outfile:
    for row in c.execute('SELECT content FROM ipynb WHERE file MATCH ?', (search,)):
        row0 = row[0]
        row0 =str(row0)
        outfile.write(row0)
        print (row0)
        
conn.close()
f.close()

        

import json
import sys
from time import sleep
import sqlite3
import csv
database = "oct1_IPNB.list.db"

conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
search = input("ROWID :")
f= open(search,"w");f.close()
with open('newtest4'+str(search)+'.ipynb', 'a') as outfile:
    for row in c.execute('SELECT content FROM ipynb WHERE rowid = ?', (search,)):
        row0 = row[0]
        row0 =str(row0)
        row0 =row0.replace("\\n","")
        outfile.write(row0)
        
conn.close()
f.close()

        

1753

import json
import sys
from time import sleep
import sqlite3
import csv
database = "oct1_IPNB.list.db"
f= open('.ipynb',"w")
f.close()
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
search = raw_input("ROWID :")
with open('.ipynb', 'a') as outfile:
        for row in c.execute('SELECT content FROM ipynb WHERE rowid = ?', (search,)):
            #for row in c.execute('SELECT * FROM ipynb WHERE rowid = 100 LIMIT 10 OFFSET 0'):
            row0 = row[0]
            #row0 =str(row0,"\n")
            outfile.write(row0)

conn.close()
f.close()

        

import json
import sys
from time import sleep
import sqlite3
import csv
#database = "junk.db"
database = "oct1_IPNB.list.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
start =input("ROWID-Start :")
end =input("ROWID-End :")
#for row in c.execute('SELECT rowid, * FROM ipynb WHERE rowid = ?', (search,)):
#for row in c.execute('SELECT rowid, * FROM ipynb WHERE rowid > 40 and rowid < 100'):    
for row in c.execute('SELECT rowid, * FROM ipynb WHERE rowid > ? and rowid < ?',(start, end)):    
        print (row[0],row[1],"\n\n",row[3])
conn.close()
f.close()

        

import sqlite3
import sys
database = "oct1_IPNB.list.db"
conn = sqlite3.connect(database)
conn.text_factory = str
c = conn.cursor()
count=0;req=200
id1 = raw_input("Starting ID : ")
id2 = raw_input("How Many Rows : ")
# id1 is start id2 is how many lines
for row in c.execute('SELECT rowid, * from ipynb LIMIT ? OFFSET ?',  (id2, id1)):
    count=count+1
    #print row[0],row[1],"\n",row[2]
    print row[0]
    if count > req:
        conn.close()
        sys.exit()

import json
import sys
from time import sleep
import sqlite3
import csv
database = "oct1_IPNB.list.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
ROWID = 
c.execute("DELETE FROM ipynb WHERE rowid = ?", (ROWID,))
conn.commit()
conn.close()
        

import sqlite3
database = "test.db"
#database = "/home/jack/Desktop/text_stuff/notebooks.db"
conn = sqlite3.connect(database)
c = conn.cursor()
conn.text_factory=str 
c = conn.cursor()
for row in c.execute('SELECT rowid, file, description FROM ipynb WHERE file = "Index" '):
    print row[0],row[1],row[2]       

c.close()
conn.close()

import re
title = "ipynb.list"
titles = open(title,"r")
for title in titles.readlines():
            filename = os.path.basename(title)
            description = filename
            description = description.replace("-", " ")
            description = description.replace("_", " ")
            description = description.replace(".ipynb", " ")
            description = re.sub("([a-z])([A-Z])","\g<1> \g<2>",description)
            print title, filename, description,"\n\n\n"

import json
import sys
from time import sleep
import sqlite3
import csv
#database = "FTS4_IPYNB_indexed.db"
database = "oct1_IPNB.list.db"
conn = sqlite3.connect(database)
conn.text_factory=str
c = conn.cursor()
c.execute("SELECT COUNT(*) from ipynb")
print c.fetchone()

#print number_of_rows    

import json
import sys
from time import sleep
import sqlite3
import csv
#database = "junk.db"
database = "test.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
count = 1
search = "Index"
for row in c.execute('SELECT rowid, * FROM ipynb WHERE content = ?', (search,)):
        print count,"\n", row[0],row[1],row[3],"\n-----------------"
        count=count+1
        if count>10:break
conn.close()
f.close()

        

!rm test.db

import sqlite3
database = "/home/jack/postit.db"
#database = "/home/jack/Desktop/text_stuff/notebooks.db"
conn = sqlite3.connect(database)
c = conn.cursor()
conn.text_factory=str 
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS ipynb 
USING FTS3(title, line);
""")
conn.commit()
conn.close()

import base64
from time import sleep
title = "ALL-WORKNG-SQLITE_and_MYSQL.ipynb"
import sqlite3
conn = sqlite3.connect('oct1_IPNB.list.db')
conn.text_factory=str 
c = conn.cursor()
with open(title, 'r') as f:
    lines = f.readlines()
    for line in lines:
        c.execute("INSERT INTO ipynb VALUES (?,?)", (title, line)) 
        conn.commit()
        #print encodedlistvalue

conn.close()
f.close()

import os
PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/"
for file in os.listdir(PATH):
    if file.endswith(".ipynb"):
        print(os.path.join(PATH, file))

import base64
from time import sleep
import os
import sqlite3
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/"
PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/postit/"
database = "/home/jack/postit.db"
for file in os.listdir(PATH):
    if file.endswith(".ipynb"):
        print(os.path.join(PATH, file))
        title2 = PATH+file
        conn = sqlite3.connect(database)
        conn.text_factory=str 
        c = conn.cursor()
        with open(title2, 'r') as f:
            lines = f.readlines()
            for line in lines:
                c.execute("INSERT INTO ipynb VALUES (?,?)", (file, line)) 
                conn.commit()

        conn.close()
        f.close()
        conn = sqlite3.connect(database)
        conn.text_factory=str 
        c = conn.cursor()
        line = file
        #line ="Good-mouse-sizing-and-cropping.ipynb"
        title = "index"
        c.execute("INSERT INTO ipynb VALUES (?,?)", (title, line)) 
        conn.commit()
        conn.close()
        f.close()

from time import sleep
database = "/home/jack/postit.db"
#database = "/home/jack/Desktop/text_stuff/notebooks.db"
conn = sqlite3.connect(database)
c = conn.cursor()
conn.text_factory=str 
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS ipynb 
USING FTS4(title, line);
""")
conn.commit()
conn.close()

title2 = PATH+title
import sqlite3
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
with open(title2, 'r') as f:
    lines = f.readlines()
    for line in lines:
        c.execute("INSERT INTO ipynb VALUES (?,?)", (title, line)) 
        conn.commit()

    line = title
    title = "index"
    c.execute("INSERT INTO ipynb VALUES (?,?)", (title, line)) 
    conn.commit()


conn.close()
f.close()

!rm /home/jack/Desktop/text_stuff/postit.db

!ls Title*

import base64
from time import sleep
import os
title = "TitleandSigntitlenpost.ipynb"
import sqlite3
conn = sqlite3.connect('newipynb.db')
conn.text_factory=str 
c = conn.cursor()
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS ipynb 
USING FTS3(title, line);
""")

#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/"
PATH = "/home/jack/Desktop/text_stuff/"
for file in os.listdir(PATH):
    if file.endswith(".ipynb"):
        print(os.path.join(PATH, file))
        title2 = PATH+file
        with open(title2, 'r') as f:
            lines = f.readlines()
            for line in lines:
                c.execute("INSERT INTO ipynb VALUES (?,?)", (file, line)) 
                conn.commit()
                #print encodedlistvalue
            conn = sqlite3.connect('newipynb.db')
            conn.text_factory=str 
            c = conn.cursor()

            line = file
            #line ="Good-mouse-sizing-and-cropping.ipynb"
            title = "index"
            c.execute("INSERT INTO ipynb VALUES (?,?)", (title, line)) 
            conn.commit()
                    #print encodedlistvalue

conn.close()
f.close()

!rm newtest.db

file = 'deep-dream-generator.ipynb'
PATH = "/home/jack/python3-starter/notebooks/"
filename = PATH+file
filein = PATH
filein = filein.replace("/home/jack/", "")
filein = filein.replace("/", "_")
filein = filein+file
description = filein
description = description.replace("_", " ")
description = description.replace("-", " ")
description = description.replace("/", " ")
description = description+"\n"+PATH+file+"\n"+file
print filein, "\n\n", description

file = 'SOme.txt'
PATH = "/home/jack/python3-starter/notebooks/"

description = PATH
description = description.replace("_", " ")
description = description.replace("-", " ")
description = description.replace("/", " ")
filename = PATH+file
description = description+(file)
#filein = "python3-starter-notebooks_"+file
print description


!rm FTS4_notebooks.db

import json
import sys
from time import sleep
import sqlite3
import csv
database = "oct1_IPNB.list.db"
#database = "/home/jack/Desktop/text_stuff/notebooks.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
search = raw_input("Title :")
for row in c.execute('SELECT rowid, * FROM ipynb WHERE file MATCH ?',(search,)):
    print row[0],row[1]

c.close()
conn.close()


        

import json
import sys
from time import sleep
import sqlite3
import csv
database = "test.db"
#database = "/home/jack/Desktop/text_stuff/notebooks.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
search = raw_input("ROWID :")
for row in c.execute('SELECT content, * FROM ipynb WHERE rowid = ?',(search,)):
    print row[0],row[1]

c.close()
conn.close()


        

database = "newtest.db"
#database = "/home/jack/Desktop/text_stuff/notebooks.db"
conn = sqlite3.connect(database)
c = conn.cursor()
conn.text_factory=str 
with open("Output.ipynb", "wb") as output_file:
    c.execute("SELECT content FROM ipynb WHERE rowid = '1753'")
    ablob = c.fetchone()
    output_file.write(ablob[0])

c.close()
conn.close()

import sqlite3
database = "newtest.db"
#database = "/home/jack/Desktop/text_stuff/notebooks.db"
conn = sqlite3.connect(database)
c = conn.cursor()
conn.text_factory=str 
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS ipynb 
USING FTS3(file, content);
""")
conn.commit()
conn.close()
conn = sqlite3.connect(database)
c = conn.cursor()
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/"
#PATH = "/home/jack/Desktop/text_stuff/"
#PATH = "/home/jack/Desktop/imagebot/"
#PATH = "/home/jack/Desktop/Snippet_Warehouse/"
#PATH = "/home/jack/Desktop/gitjupyter/"
#PATH = "/home/jack/Desktop/jack_watch/"
#PATH = "/home/jack/Desktop/jack_watch/nltk/"
#PATH = "/home/jack/Desktop/jack_watch/Python-Lectures/"
#PATH = "/home/jack/Desktop/jack_watch/jupyter_examples-master/"
#PATH = "/home/jack/Desktop/Books/numerical-python-book-code/"
#PATH = "/home/jack/Desktop/Books/pydata-book/"
#PATH = "/home/jack/Desktop/Ruby/"
#PATH = "/home/jack/Desktop/alice/ChatterBot/"
#PATH = "/home/jack/Desktop/deep-dream-generator/LOCAL-notebooks/"
#PATH = "/home/jack/Desktop/numpy-array-filters/"
#PATH = "/home/jack/Desktop/pycode/"
#PATH = "/home/jack/Desktop/pycode/vpython2/TrigonometryBot/"
#PATH = "/home/jack/Desktop/temp/args_csv_Twython_ImageBot/"
PATH = "/home/jack/Desktop/dockercommands/"
for file in os.listdir(PATH):
    if file.endswith(".ipynb"):
        
        filename = PATH+file
        #filein = "deep-dream-generator_"+file
        #filein = "text_stuff_"+file
        filein = "starter-notebooks_"+file
        with open(filename, "rb") as input_file:
            ablob = input_file.read()
            #content = [sqlite3.Binary(ablob)]
            content  = sqlite3.Binary(ablob)
            c.execute("INSERT INTO ipynb (file, content) VALUES(?, ?)", (filein, content))
            print (os.path.join(PATH, file, filein))
            conn.commit()
        

c.close()
conn.close()
    
conn = sqlite3.connect(database) 
conn.text_factory=str 
c = conn.cursor()
#for row in c.execute('SELECT rowid, file FROM ipynb'):
#    print row[0],row[1]       

c.close()
conn.close()

import sqlite3
database = "newtest.db"
#database = "/home/jack/Desktop/text_stuff/notebooks.db"
conn = sqlite3.connect(database)
c = conn.cursor()
conn.text_factory=str 
c = conn.cursor()
for row in c.execute('SELECT rowid, file FROM ipynb WHERE rowid = '):
    print row[0],row[1]       

c.close()
conn.close()

import sqlite3
database = "newtest.db"
#database = "/home/jack/Desktop/text_stuff/notebooks.db"
conn = sqlite3.connect(database)
c = conn.cursor()
conn.text_factory=str 
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS ipynb 
USING FTS3(file, content);
""")
conn.commit()
conn.close()
conn = sqlite3.connect(database)
c = conn.cursor()
file = "TextCloud-Image.ipynb/starter-notebooks_TextCloud-Image.ipynb"
with open(filename, "rb") as input_file:
    ablob = input_file.read()
    #content = [sqlite3.Binary(ablob)]
    content  = sqlite3.Binary(ablob)
    c.execute("INSERT INTO ipynb (file, content) VALUES(?, ?)", (file, content))
    conn.commit()

with open("Output.ipynb", "wb") as output_file:
    c.execute("SELECT content FROM ipynb WHERE file = 'jupyter-to-database-FTS4.ipynb'")
    ablob = c.fetchone()
    output_file.write(ablob[0])

c.close()
conn.close()

import sqlite3
database = "newtest.db"
#database = "/home/jack/Desktop/text_stuff/notebooks.db"
conn = sqlite3.connect(database)
c = conn.cursor()
conn.text_factory=str 
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS ipynb 
USING FTS3(file, content);
""")
conn.commit()
conn.close()
conn = sqlite3.connect(database)
c = conn.cursor()
filename = "jupyter-to-database-FTS4.ipynb"
with open(filename, "rb") as input_file:
    ablob = input_file.read()
    c.execute("INSERT INTO ipynb (file, content) VALUES(?, ?)", (filename, [sqlite3.Binary(ablob)]))
    conn.commit()

with open("Output.ipynb", "wb") as output_file:
    #c.execute("SELECT file FROM file WHERE id = 0")
    c.execute('SELECT content FROM ipynb WHERE file MATCH ?',(file,))   
    ablob = cursor.fetchone()
    output_file.write(ablob[0])

cursor.close()
conn.close()

import base64
from time import sleep
import os
import sqlite3
database = "/home/jack/Desktop/text_stuff/postit.db"
#database = "/home/jack/Desktop/text_stuff/notebooks.db"
conn = sqlite3.connect(database)
c = conn.cursor()
conn.text_factory=str 
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS ipynb 
USING FTS3(file, content);
""")
conn.commit()
conn.close()
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/"
PATH = "/home/jack/Desktop/text_stuff/"
for file in os.listdir(PATH):
    if file.endswith(".ipynb"):
        print(os.path.join(PATH, file))
        title2 = PATH+file
        conn = sqlite3.connect(database)
        conn.text_factory=str 
        c = conn.cursor()
        #with open(title2, 'r') as f:
        keyword = file
        #content=open(title2, 'r').read().decode("utf-8", "ignore")
        content=open(title2, 'r').read()   
        c.execute("INSERT INTO ipynb VALUES (?,?)", (file,content))
        #c.execute("INSERT INTO ipynb VALUES (?,?)", (file, content)) 
        conn.commit()

        conn.close()
        f.close()
        conn = sqlite3.connect(database)
        conn.text_factory=str 
        c = conn.cursor()
        line = file
        #line ="Good-mouse-sizing-and-cropping.ipynb"
        content = "Index"
        c.execute("INSERT INTO ipynb VALUES (?,?)", (file, content)) 
        conn.commit()
        conn.close()
        f.close()
        
conn = sqlite3.connect(database) 
conn.text_factory=str 
c = conn.cursor()
for row in c.execute('SELECT rowid, file FROM ipynb'):
#for row in c.execute('SELECT line FROM ipynb WHERE file MATCH ?',(file,)):    
    sleep(.5)
    #row0 = base64.b64decode(row[0])
    #print row0, row[1]
    print row[0],row[1]   

import base64
from time import sleep
import sqlite3
database = "/home/jack/Desktop/text_stuff/postit.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
line ="ALL-WORKNG-SQLITE_and_MYSQL.ipynb"
#line ="Good-mouse-sizing-and-cropping.ipynb"
title = "index"
c.execute("INSERT INTO ipynb VALUES (?,?)", (title, line)) 
conn.commit()
        #print encodedlistvalue

conn.close()
f.close()



import json
import sys
from time import sleep
import sqlite3
database = "/home/jack/Desktop/text_stuff/postit2.db"
#database = '/home/jack/Desktop/text_stuff/notebooks.db'
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
#for row in c.execute('SELECT title, line  FROM ipynb'):
search = "jupyter-to-database-FTS4.ipynb"
#with open('jupyter-to-database-FTS4-2.ipynb', 'a') as outfile:
for row in c.execute('SELECT line FROM ipynb WHERE title MATCH ?',(search,)):    
    
    
    sleep(.5)
    #row0 = base64.b64decode(row[0])
    #print row0, row[1]
    print row[1]

import base64
from time import sleep
import sqlite3
conn = sqlite3.connect('/home/jack/Desktop/text_stuff/notebooks.db')
conn.text_factory=str 
c = conn.cursor()
line ="ALL-WORKNG-SQLITE_and_MYSQL.ipynb"
#line ="Good-mouse-sizing-and-cropping.ipynb"
title = "index"
c.execute("INSERT INTO ipynb VALUES (?,?)", (title, line)) 
conn.commit()
        #print encodedlistvalue

conn.close()
f.close()

import base64
from time import sleep
import sqlite3
conn = sqlite3.connect('/home/jack/Desktop/text_stuff/notebooks.db')
conn.text_factory=str 
c = conn.cursor()
line ="""
astral.py.ipynb
Astronomy-II.ipynb
Astronomy-I.ipynb 
DEEP-DREAM-ONLY.ipynb
earth-satellites.ipynb
jupyter-to-database-FTS4.ipynb
Image_Pack.ipynb    
Snippet_Warehouse-MySQL-SQLite-code-storage-search.ipynb    
WikiPedia.ipynb
Creation-of-collection.db.ipynb    
Palett_Swap.ipynb    
Parsing_and_Storing_RSS_newsfeeds_in_SQLite.ipynb
Creating-C++-Image-blender.ipynb
Creating-C++-Image-viewer.ipynb
Text_Generation-BEST.ipynb
Words-and-Sentences.ipynb
Bible_Search_in_SQL.ipynb
"""
title = "index"
c.execute("INSERT INTO ipynb VALUES (?,?)", (title, line)) 
conn.commit()
        #print encodedlistvalue

conn.close()
f.close()

import json
import sys
from time import sleep
import sqlite3
import csv

f= open('newtest.ipynb',"w")
f.close()
conn = sqlite3.connect('/home/jack/Desktop/text_stuff/notebooks.db')
conn.text_factory=str 
c = conn.cursor()
#search = raw_input("Title :")
search = "Matplotlib.ipynb"
with open('newtest.ipynb', 'a') as outfile:
    for row in c.execute('SELECT line FROM ipynb WHERE title MATCH ?',\
                         (search,)):
        row0 = row[0]
        #row0 =str(row0,"\n")
        outfile.write(row0)
        
conn.close()
f.close()

        

import json
import sys
from time import sleep
import sqlite3
import csv

f= open('jupyter-to-database-FTS4-2.ipynb',"w")
f.close()
conn = sqlite3.connect('/home/jack/Desktop/text_stuff/notebooks.db')
conn.text_factory=str 
c = conn.cursor()
#search = raw_input("Title :")
search = 13
with open('jupyter-to-database-FTS4-2.ipynb', 'a') as outfile:
    c.execute('SELECT rowid, * FROM ipynb WHERE rowid = ?',(search,))
    print row[0],row[1]

conn.close()
f.close()

        

import json
import sys
from time import sleep
import sqlite3
import csv
title = "index.txt"
f= open(title,"w")
f.close()
database = "/home/jack/Desktop/text_stuff/postit.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
with open(title, 'a') as outfile:
    for row in c.execute('SELECT rowid, title, line, keyword FROM ipynb WHERE title MATCH ?', ("Index",)):
        row0 =row[0], row[3]
        row0 =str(row0)
        row0 = row0+"\n"
        outfile.write(row0)
conn.close()
f.close()

        

import json
import sys
from time import sleep
import sqlite3
import csv
database = "/home/jack/Desktop/text_stuff/postit.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
#with open(title, 'a') as outfile:
#content=open(filename, 'r').read().decode("utf-8", "ignore")    
for row in c.execute('SELECT rowid, title, line FROM ipynb WHERE title = ?', ("Index",)):
    row0 = row[0],row[2]
    sleep(1)
    print row0
conn.close()

import json
import sys
from time import sleep
import sqlite3
import csv
database = "/home/jack/Desktop/text_stuff/postit.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
#with open(title, 'a') as outfile:
#content=open(filename, 'r').read().decode("utf-8", "ignore")    
c.execute('SELECT rowid, title, line, keyword FROM ipynb WHERE title = ?', ("jupyter-to-database-FTS4.ipynb",))
print row[0:]
conn.close()

import json
import sys
from time import sleep
import sqlite3
import csv
database = "/home/jack/Desktop/text_stuff/postit.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
#with open(title, 'a') as outfile:
#content=open(filename, 'r').read().decode("utf-8", "ignore")    
for row in c.execute('SELECT rowid, title, line FROM ipynb'):
    row0 = row[0],row[1]
    sleep(1)
    print row0
conn.close()

import json
import sys
from time import sleep
import sqlite3
import csv
database = "/home/jack/Desktop/text_stuff/postit.db"
conn = sqlite3.connect(database)

conn.text_factory=str 
c = conn.cursor()
#search = "FTS3_Database.ipynb"
search = raw_input("SEARCH : ")
with open(title, 'a') as outfile:
    for row in c.execute('SELECT rowid, title, keyword FROM ipynb WHERE rowid = ?', (search,)):
        print row[0],row[1],row[2]
        

import json
import sys
from time import sleep
import sqlite3
import csv
conn = sqlite3.connect('/home/jack/Desktop/text_stuff/notebooks.db')
conn.text_factory=str 
c = conn.cursor()
#search = "FTS3_Database.ipynb"
search = raw_input("SEARCH : ")
with open(title, 'a') as outfile:
    for row in c.execute('SELECT rowid, title, line FROM ipynb WHERE line MATCH ?', (search,)):
        print row[0],row[1],"\n",row[2]
        

import json
import sys
from time import sleep
import sqlite3
import csv
conn = sqlite3.connect('/home/jack/Desktop/text_stuff/notebooks.db')
conn.text_factory=str 
c = conn.cursor()
#c.execute("DELETE title, line FROM ipynb where rowid MATCH '362113' "):
#c.execute("delete from ipynb where rowid=362113;"):
c.execute("DELETE FROM ipynb WHERE title = ?", ('Good-mouse-sizing-and-cropping.ipynb',))
conn.commit()
conn.close()
        

import sqlite3
import sys
conn = sqlite3.connect('/home/jack/Desktop/text_stuff/notebooks.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
id1 = raw_input("Starting ID : ")
id2 = raw_input("How Many Rows : ")
# id1 is start id2 is how many lines
for row in c.execute('SELECT rowid, * from ipynb LIMIT ? OFFSET ?',  (id2, id1)):
    count=count+1
    #print row[0],row[1],"\n",row[2]
    print row[2]
    if count > req:
        conn.close()
        sys.exit()

import json
import sys
from time import sleep
import sqlite3
import csv
data
conn = sqlite3.connect('/home/jack/Desktop/text_stuff/notebooks.db')
conn.text_factory=str 
c = conn.cursor()
search = "earth-satellites.ipynb"
with open(title, 'a') as outfile:
    for row in c.execute("SELECT rowid, file FROM ipynb where title MATCH 'jupyter-to-database-FTS4.ipynb' "):
        row0 = row[1]
        sleep(1)
        print row[0],row[1]
        



import sqlite3
import sys
conn = sqlite3.connect('/home/jack/Desktop/text_stuff/notebooks.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=20
search = raw_input("Search : ")
for row in c.execute('SELECT rowid, title, line FROM ipynb WHERE title MATCH ?', (search,)):    
    count=count+1
    print row[0],row[1],"\n",row[2]
    if count > req:
        conn.close()
        sys.exit()

import sqlite3
import sys
database = "test.db"
conn = sqlite3.connect(database)
conn.text_factory = str
c = conn.cursor()
count=0;req=50
search = raw_input("Search : ")
for row in c.execute('SELECT rowid, file, description FROM ipynb WHERE file MATCH ?', (search,)):    
    count=count+1
    print row[0],"\n",row[1],"\n",row[2]
    if count > req:
        conn.close()
        sys.exit()

!sqlite3 unique-End2.db "pragma integrity_check;"

!locate snippet.db

import sqlite3
import sys
database = "/home/jack/snippet.db""
conn = sqlite3.connect(database)
ID = raw_input("Delete ID Number : ")
c = conn.cursor()
c.execute('DELETE FROM snippet WHERE id=?',(ID))
conn.commit()
conn.close()

Search : remove duplicate
ID :  78 
%%writefile HashCheck.py
"" USEAGE:
(insert hash)

for example to get hash of a filename:
def md5(Path):
    hash_md5 = hashlib.md5()
    with open(Path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

Hash = md5(title)

import HashCheck
hasht = "jsudsfhndsfjunjsd"
HashCheck.hashfill(Hash)
---------------
import HashCheck
HashCheck.hashcheck()

import HashCheck
HashCheck.killmem()
""
import sqlite3
import sys
import os

def md5(Path):
    hash_md5 = hashlib.md5()
    with open(Path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

!ls ~/hubiC/Databases

import sqlite3
import sys
database = "/home/jack/hubiC/Databases/snippet.db"
conn = sqlite3.connect(database)
conn.text_factory = str
c = conn.cursor()
count=0;req=200
search = raw_input("Search : ")
for row in c.execute('SELECT rowid, * FROM snippet WHERE snippet MATCH ?', (search,)):    
    count=count+1
    print "ID : ",(row)[0],(row)[2]," -- KEYWORDS",(row)[3],"\n"
    if count > req:
        conn.close()
        sys.exit()

import sqlite3
import sys
from time import sleep
database = "/home/jack/snippet.db"
conn = sqlite3.connect(database)
conn.text_factory = str
c = conn.cursor()
count = 0
f = open("All-Snippets.txt", "w");f.close()
f = open("All-Snippets.txt", "a")
#search = raw_input("Search : ")
search = 'sqlite'
for row in c.execute('SELECT rowid, * FROM snippet'):    
    count=count+1
    count = str(count)
    iD = row[0]
    iD = str(iD)
    line = row[2]
    desc = (row)[3]
    j = "Line No. :",count,"\nROWID :",iD,"\n",line,"\nDescription :",desc,"\n\n-------new entry -------"
    line = "".join(j)
    #line = (count+(row)[0]+(row)[2]+" -- KEYWORDS"*(row)[3]+"\n")
    sleep(1)
    f.write(line)
    print line
    count = int(count)
    
conn.close()
Print "Search is Completed"
sys.exit()

test_input = []
keep = set(mapping[data] for data in test_input)

inpuT = raw_input("Test : ").split("/")
keep.update(inpuT)

print keep

import sqlite3
import sys
from time import sleep

def md5(line):
    hash_md5 = hashlib.md5()
    for chunk in iter(lambda: line(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()




database = "/home/jack/snippet.db"
conn = sqlite3.connect(database)
conn.text_factory = str
c = conn.cursor()
count = 0
f = open("this-Snippets.txt", "w");f.close()
f = open("this-Snippets.txt", "a")
search = raw_input("Search : ")
for row in c.execute('SELECT rowid, * FROM snippet WHERE snippet MATCH ?', (search,)):  
    count=count+1
    count = str(count)
    iD = row[0]
    iD = str(iD)
    line = row[2]
    desc = (row)[3]
    j = "Line No. :",count,"\nROWID :",iD,"\n",line,"\nDescription :",desc,"\n\n-------new entry -------"
    line = "".join(j)
    sleep(1)
    f.write(line)
    print line
    count = int(count)
    
conn.close()
print "Results Complete"
sys.exit()

!ls ~/Desktop/text_stuff

import os
import timeit
import sqlite3
def txsearch():
    
    #database = "FTS4_IPYNB.db"
    database = "PythonCode.db"
    conn = sqlite3.connect(database)
    c = conn.cursor()
    conn.text_factory=str 
    c.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS PYTHON 
    USING FTS4(PATH, fname, line);
    """)
    conn.commit()
    
    # Ask to enter string to search
    Sstring = raw_input("Search Phrase")
    for fname in os.listdir('/home/jack/Desktop/text_stuff'):
       # Apply file type filter 
       path = "/home/jack/Desktop/text_stuff/" 
       if fname.endswith(".txt"):
            # Open file for reading
            PATH = path+fname
            fo = open(PATH)
            # Read the first line from the file
            line = fo.readline()
            # Initialize counter for line number
            line_no = 1
            # Loop until EOF
            while line != '' :
                    index = line.find(Sstring)
                    c.execute("INSERT INTO PYTHON VALUES (?,?,?)", (PATH, fname, line))
                    conn.commit()
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
    conn.close()                
            
txsearch()            

import sqlite3
from time import sleep
database = "PythonCode.db"
conn = sqlite3.connect(database)
c = conn.cursor()
search = raw_input("SEARCH : ")
#for row in c.execute("SELECT rowid,* from PYTHON WHERE line MATCH ?", (search,)):
for row in c.execute("SELECT rowid,* from PYTHON "):   
    sleep(1)                 
    print row[0],row[1],row[2]

conn.close()

import os
import timeit
def txsearch():
    # Ask to enter string to search
    Sstring = raw_input("Search Phrase  : ")
    for fname in os.listdir('/home/jack/Desktop/text_stuff'):
       # Apply file type filter 
       path = "/home/jack/Desktop/text_stuff/" 
       if fname.endswith(".txt"):
            # Open file for reading
            fo = open(path+fname)
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

!mkdir Databases



import sqlite3
import sys
database = "/home/TEMP/Databases/SNIPPETS.db"
conn = sqlite3.connect(database)
conn.text_factory = str
c = conn.cursor()
count=0;req=200
search = raw_input("Search : ")
for row in c.execute('SELECT rowid, * FROM snippets WHERE snippets MATCH ?', (search,)):    
    count=count+1
    print "ID : ",(row)[0],(row)[1]," -- KEYWORDS",(row)[2],"\n"
    if count > req:
        conn.close()
        sys.exit()

import json
import sys
from time import sleep
import sqlite3
import csv
database = "oct1_IPNB.list.db"

conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
search = raw_input("ID :")
filename = search+"DB.ipynb"
f= open(filename,"w");f.close()
SEARCH = search+1
for row in c.execute('SELECT content FROM ipynb WHERE rowid == ?', (SEARCH,)):
        print row[1]
with open(filename, 'a') as outfile:
    for row in c.execute('SELECT content FROM ipynb WHERE rowid == ?', (search,)):
        row0 = row[1]
        #row0 =str(row0,"\n")
        #outfile.write(row0)
        print row0
        
conn.close()
f.close()

  # 427      

import json
import sys
from time import sleep
import sqlite3
import csv
database = "oct1_IPNB.list.db"

conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
search = input("ID :")
filename = search+"DB.ipynb"
#f= open(filename,"w");f.close()
SEARCH = int(search)+1
for row in c.execute('SELECT content FROM ipynb WHERE rowid == ?', (SEARCH,)):
        filename = str(search)+row[0]
with open(filename, 'w') as outfile:
    for row in c.execute('SELECT content FROM ipynb WHERE rowid == ?', (search,)):
        row0 = row[0]
        row0 =str(row0)
        row0 =row0.replace("\\n","\n")
        row0 =row0.replace("\\f","")
        outfile.write(row0)
        #print (row0)
print (filename)        
conn.close()
f.close()


  # 427      

Search : unknown database
ID :  84 
#find table names, unknown sqlite database
import sqlite3
import sys
from time import sleep
parts = []
database = "/home/jack/Desktop/text_stuff/database-bak/collection.db"
conn = sqlite3.connect(database)
conn.text_factory = str
c = conn.cursor()
res = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
for name in res:
    sleep(2)
    
    print name[0] 
    
#explore a database unknown database find lost table tables sqlite_master sqlite tricks    

#recover column names recover field names, unknown database, unknown sqlite
import sqlite3
database = "/home/jack/Desktop/text_stuff/database-bak/collection.db"
conn = sqlite3.connect(database)
c = conn.cursor()
cur = c.execute('select * from tweets')

#this also works
#names = list(map(lambda x: x[0], cur.description))

names = [description[0] for description in cur.description]
print names[0:]
 -- KEYWORDS explore a database unknown database find lost table tables sqlite_master sqlite tricks
recover column names recover field names, unknown database, unknown sqlite


ID :  100 
%%writefile dbINFO.py
""
Gets tablename and column names from unknown database
just enter database name.
USAGE:
import dbINFO
database= "databases/history.db"
#database= "databases/sat2.db"
#database= "databases/ImageD.db"
dbINFO.dbinfo(database)

""

import sqlite3
def dbinfo(database):
    conn = sqlite3.connect(database)
    conn.text_factory = str
    c = conn.cursor()
    res = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    row = c.fetchone()
    row = str(row)
    row = row.replace("(","");row = row.replace(",)","")
    row = row.replace("'","")
    print row
    cur = c.execute("select * from "%s"" %  row)
    columns = [description[0] for description in cur.description]
    return columns

# if run directly
#database = "databases/history.db"
#dbinfo(database)

unknown database get database info get SQLite info lost column names get tablename
retrieve database info get table get rows 
 -- KEYWORDS 
unknown database get database info get SQLite info lost column names get tablename
retrieve database info get table get rows 



lines = open("mouse-sizing-n-cropping_mouse-sizing-n-cropping.ipynb", "r").readlines()
cnt = 0
LINZ =[]
for line in lines:
    cnt = cnt + 1
    if cnt<20:LINZ.append(line)

from time import sleep
for line in LINZ:
    sleep(1)
    print(line)

import json
import sys
from time import sleep
import sqlite3
import csv
database = "oct1_IPNB.list.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
count=1
DATA = []
search = input("Title: ")
# ONLY the DATA table can use MATCH
for row in c.execute('SELECT rowid,* FROM ipynb WHERE ipynb MATCH ?',(search,)):
    if search in row[1] or search in row[3]:
        #print (row[2])#"\n----------------------")
        DATA.append(row[2])
        count=count+1
        if count>20:break
c.close()
conn.close()


import json
import sys
from time import sleep
import sqlite3
import csv
database = "oct1_IPNB.list.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
count=1
DATA = []
#search = input("Title: ")
search =="BLEND"
# ONLY the DATA table can use MATCH
for row in c.execute('SELECT rowid,* FROM ipynb WHERE ipynb MATCH ?',(search,)):
    if search in row[1] or search in row[3]:
        #print (row[2])#"\n----------------------")
        DATA.append(row[2])
        count=count+1
        if count>20:break
c.close()
conn.close()
print("XXXXXXXXXXXXXXXXXXXXX",DATA)

Title: BLEND
104 use-BLENDERS_use-BLENDERS.ipynb use BLENDERS Date :Thu Sep 22 21:35:45 2022 
----------------------

print(len(DATA))

from time import sleep
for line in DATA:
    sleep(4)
    print(line)




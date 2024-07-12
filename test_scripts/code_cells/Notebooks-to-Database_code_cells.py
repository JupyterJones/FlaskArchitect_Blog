

import os
import os.path
title = "test.list"
f= open(title,"w");f.close()
count=0
for dirpath, dirnames, filenames in os.walk("/home/jack/Desktop/JupyterNotebook-Graphics/"):
    filenames = [f for f in filenames if not f[0] == '.']
    dirnames[:] = [d for d in dirnames if not d[0] == '.']
    for filename in [f for f in filenames if f.endswith(".ipynb")]:
        count=count+1
        Path = os.path.join(dirpath, filename)
        with open(title, 'a') as outfile:
            path = Path+"\n"
            outfile.write(path)

import os
import hashlib
H = []
Hs = set()
def file_as_bytes(file):
    with file:
        return file.read()
title0 = "hashtest.list"
f0= open(title0,"w")
title = "sept8_IPNB.list"
#title = "test.list"
f= open(title,"r").readlines()
for full_path in f:
    full_path = full_path.replace("\n","")
    HASH = hashlib.md5(file_as_bytes(open(full_path, 'rb'))).hexdigest()
    DATE = os.path.getmtime(full_path)
    DATE = str(DATE)
    PATHhash = HASH+":"+DATE+":"+full_path+"\n"
    
    H.append(PATHhash)
    f0.write(PATHhash)
    Hs.add(HASH)
    
    
f0.close()    

title = "hashtest.list"
title1 = "rows_hashtest.list"
f0 = open(title1,"w")
count = 0
cnt = 0
dup = set()
Dup = []
SORT = []
f = open(title,"r").readlines()
for rows in f:
    row = rows.split(":")
    text = row[0]+":"+row[1]+":"+row[2]
    SORT.append(text)
    print text
    f0.write(text)
    count = count +1
f0.close()
print count    
print cnt


title = "hashtest.list"
title1 = "nodups_hashtest.list"
f0 = open(title1,"w")
count = 0
cnt = 0
dup = set()
Dup = []
SORT = []
f = open(title,"r").readlines()
#f0 = f0.replace("\n", "")
#rows = f0.split(":")
for rows in f:
    row = rows.split(":")
    dup.add(row[0])
    if row[0] not in dup:
        print row[0],row[1],row[2]
        text = row[0]+":"+row[1]+":"+row[2]
        SORT.append(text)
        print text
        f0.write(text)
        cnt = cnt +1
    Dup.append(row[0])
    count = count +1
f0.close()
print count    
print cnt


title1 = "sorted_hash.list"
f0 = open(title1,"w")
count = 0
LIST = sorted(SORT)
for lines in LIST:
    f0.write(lines)
    count = count +1
print count 
f0.close()

title1 = "nodup_sorted_hash.list"
f0 = open(title1,"w")
newline = ""
count = 0
for lastline in LIST:
    st = lastline.split(":")
    oldline = st[0]
    if st[0] != newline:
        f0.write(lastline)
        count = count +1
        newline = oldline
    
print count
f0.close()

count = 0
title1 = "nodup_sorted_hash.list"
f0 = open(title1,"r").readlines()
for lines in f0:
    print lines
    count = count +1
print count    

import os
import hashlib
H = []
Hs = set()
clean =[]
count = 0
def file_as_bytes(file):
    with file:
        return file.read()
title0 = "hashtesta.list"
f0= open(title0,"w")
title = "sept8_IPNB.list"

f= open(title,"r").readlines()
for full_path in f:
    count = count + 1
    full_path = full_path.replace("\n","")
    HASH = hashlib.md5(file_as_bytes(open(full_path, 'rb'))).hexdigest()
    oldhash = H
    DATE = os.path.getmtime(full_path)
    DATE = str(DATE)
    PATHhash = HASH+":"+DATE+":"+full_path+"\n"
    for ck in H:
        if HASH not in ck:
            clean.append(PATHhash)
    olhash = HASH   
    H.append(str(count)+"_"+PATHhash)
    
    f0.write(str(count)+"_"+PATHhash)
    Hs.add(HASH)
    
    
f0.close()    

count = 0
for line in clean:
    print line
    count = count +1
print count    

print clean

print len(H)
print len(Hs)

count = 0
for l in HH:
    print l
    count = count +1
print count    

count = 0
for l in HHs:
    print l
    count = count +1
print count    

HH = H
HHs = Hs

count = 0
for h in HH:
    
    for hs in HHs:
        hs = hs.split(":")
        if hs[0] in h:
            print hs[0]
            count = count +1
            print h
print count # 1462   

import hashlib
H = []
def file_as_bytes(file):
    with file:
        return file.read()

title = "sept8_IPNB.list"
f= open(title,"r").readlines():
for full_path in f:
    full_path = full_path.replace("\n","")
    HASH = hashlib.md5(file_as_bytes(open(full_path, 'rb'))).hexdigest()
    H.append(HASH)


import sqlite3
import re
import sys
import time
import os
database = "sept8_IPNB.list.db"
#database = "junk2.db"
conn = sqlite3.connect(database)
conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")
c = conn.cursor()
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS ipynb 
USING FTS4(file, content, description);
""")
conn.commit()
conn.close()
conn = sqlite3.connect(database)
c = conn.cursor()
count=1
#titlelist = "sept8_IPNB.list"
titlelist = "nodup_sorted_hash.list"
titles = open(titlelist,"r")
for title in titles.readlines():
    title = str(title)
    title = title.split(":")
    title = title[2].replace("\n", "")
    dt=time.ctime(os.path.getctime(title))
    dt=str(dt)
    filename = os.path.basename(title)
    # Use for debug print filename,":"
    description = filename
    description = description.replace("-", " ")
    description = description.replace("_", " ")
    description = description.replace(".ipynb", " ")
    description = re.sub("([a-z])([A-Z])","\g<1> \g<2>",description)
    
    
    dt=time.ctime(os.path.getctime(title))
    dt=str(dt)
    #dt = dt.replace(" ","")
    description = description+"Date :"+dt
    suf = title.replace("/home/jack/","")
    suf = suf.replace(".ipynb","_")
    suf = suf.replace("/","_")
    filename = suf+filename
    with open(title, "rb") as input_file:
                ablob = input_file.read()
                content  = sqlite3.Binary(ablob)
                c.execute("INSERT INTO ipynb (file, content, description) VALUES(?, ?, ?)", 
                      (filename, content, description))
                
                conn.commit()
    line = file
    #line ="Good-mouse-sizing-and-cropping.ipynb"
    index = "Index"
    c.execute("INSERT INTO ipynb VALUES (?,?,?)", (index, filename, description)) 
    conn.commit()
    count=count+1
    print count,filename, description

c.close()
conn.close() 

titlelist = "nodup_sorted_hash.list"
titles = open(titlelist,"r")
for title in titles.readlines():
    title = str(title)
    title = title.split(":")
    title = title[2].replace("\n", "")
    print title

import json
import sys
from time import sleep
import sqlite3
import csv
database = "sept8_IPNB.list.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
count=1
search = raw_input("Title :")
# ONLY the DATA table can use MATCH
for row in c.execute('SELECT rowid, file, content, description FROM ipynb WHERE content MATCH ?',(search,)):
    print row[0],row[1],row[3],"\n----------------------"
    count=count+1
    if count>25:break
c.close()
conn.close()

import json
import sys
from time import sleep
import sqlite3
import csv
database = "sept8_IPNB.list.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
count=1
search = raw_input("Title :")
# ONLY the DATA table can use MATCH
for row in c.execute('SELECT rowid, file, content, description FROM ipynb WHERE content MATCH ?',(search,)):
    print row[0],row[1],"\n----------------------"
    count=count+1
    if count>25:break
c.close()
conn.close()

import json
import sys
from time import sleep
import sqlite3
import csv
database = "sept8_IPNB.list.db"
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
search = raw_input("ROWID :")
with open('WordcloudImageGenerator.ipynb', 'w') as outfile:
        for row in c.execute('SELECT content FROM ipynb WHERE rowid = ?', (search,)):
            #for row in c.execute('SELECT * FROM ipynb WHERE rowid = 100 LIMIT 10 OFFSET 0'):
            row0 = row[0]
            #row0 =str(row0,"\n")
            outfile.write(row0)

conn.close()
f.close()




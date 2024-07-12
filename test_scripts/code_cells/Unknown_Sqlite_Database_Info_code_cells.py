import os
import os.path
title = "database.list"
f= open(title,"a");f.close()
count=0
for dirpath, dirnames, filenames in os.walk("/home"):
    filenames = [f for f in filenames if not f[0] == '.']
    dirnames[:] = [d for d in dirnames if not d[0] == '.']
    for filename in [f for f in filenames if f.endswith(".db")]:
        count=count+1
        Path = os.path.join(dirpath, filename)
        with open(title, 'a') as outfile:
            path = Path+"\n"
            outfile.write(path)

f = open("database.list").readlines()
for database in f:
    database = database.replace("\n", "")
    print (database)



import sqlite3
# This reads an unknown Sqlite3 Database, thens creates or reuses a database
# to store the information retrieved
def Sdbinfo(unknown, storage):
    con = sqlite3.connect(storage)
    co = con.cursor()
    co.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS data 
    USING FTS4(unknown, row, columns);
    """)
    con.commit()
    
    conn = sqlite3.connect(unknown)
    conn.text_factory = str
    c = conn.cursor()
    res = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    row = c.fetchone()
    row = str(row)
    row = row.replace("(","");row = row.replace(",)","")
    row = row.replace("'","");row = row.replace(",","")
    cur = c.execute("select * from \"%s\"" %  row)
    columns = [description[0] for description in cur.description]
    col = str(columns)
    col = col.replace("[","");col = col.replace("]","")
    coll = col.replace("'","")
    print (row, coll)
    co.execute("INSERT into data (unknown, row, columns) values (?,?,?)",(unknown, row, coll))
    con.commit()
    conn.close()
    conn.close()
    return columns

# picked out a single file to test
unknown = "/home/jake/pas.bak/GOT.db"
storage = "Store.db"
Sdbinfo(unknown, storage)

import sqlite3
# This reads an unknown Sqlite3 Database, thens creates or reuses a database
# to store the information retrieved
def Sdbinfo(unknown, storage):
    con = sqlite3.connect(storage)
    co = con.cursor()
    co.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS data 
    USING FTS4(unknown, row, columns);
    """)
    con.commit()
    
    conn = sqlite3.connect(unknown)
    conn.text_factory = str
    c = conn.cursor()
    res = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    row = c.fetchone()
    row = str(row)
    row = row.replace("(","");row = row.replace(",)","")
    row = row.replace("'","");row = row.replace(",","")
    cur = c.execute("select * from \"%s\"" %  row)
    columns = [description[0] for description in cur.description]
    col = str(columns)
    col = col.replace("[","");col = col.replace("]","")
    coll = col.replace("'","")
    print (row, coll)
    co.execute("INSERT into data (unknown, row, columns) values (?,?,?)",(unknown, row, coll))
    con.commit()
    conn.close()
    conn.close()
    return columns

# picked out a single file to test
unknown = "/home/jack/Desktop/DataScience/work/COVID-19-Jupyter-Notebooks/DATA/DATAcsv.db"
storage = "Store.db"
Sdbinfo(unknown, storage)

import sqlite3
conn = sqlite3.connect("/home/jack/Desktop/DataScience/work/COVID-19-Jupyter-Notebooks/DATA/DATAcsv.db")
c = conn.cursor()
for row in c.execute("SELECT ROWID, * FROM CORONA"):
    print ("Row id:              ", row[0])
    print ("TEXT:  ", row[1])
 

# Print a specific column of the cvs entered in the database

import sqlite3
conn = sqlite3.connect("/home/jack/Desktop/DataScience/work/COVID-19-Jupyter-Notebooks/DATA/DATAcsv.db")
c = conn.cursor()
for row in c.execute("SELECT ROWID, * FROM CORONA"):
    #print ("Row id:              ", row[0])
    #print ("TEXT:  ", row[1])
    columns = row[1].split(",")
    print(columns[4],columns[5])

import sqlite3
conn = sqlite3.connect("/home/jake/pas.bak/GOT.db")
c = conn.cursor()
for row in c.execute("SELECT ROWID, * FROM PROJECT"):
    print ("Row id:              ", row[0])
    print ("File path and Name:  ", row[1])
 

import sqlite3
conn = sqlite3.connect("Store.db")
c = conn.cursor()
for row in c.execute("SELECT ROWID, * FROM data"):
    print ("Row id:              ", row[0])
    print ("File path and Name:  ", row[1])
    print ("Print Table:         ", row[2])
    print ("Columns:             ", row[3])

import sqlite3
conn = sqlite3.connect("/home/jack/nltk_data/corpora/city_database/city.db")
c = conn.cursor()
count = 0
for row in c.execute("SELECT ROWID, * FROM SequelizeMeta"):
    print "Row id:        ", row[0]
    print "City:          ", row[1]
    print "County:        ", row[2]
    print "Population:    ", row[3]
    print "---------------------"
    count = count +1
    if count >4:
        break

import sqlite3
conn = sqlite3.connect("/home/jack/nltk_data/corpora/city_database/city.db")
c = conn.cursor()
for row in c.execute("SELECT ROWID, * FROM city_table"):
    print "Row id:        ", row[0]
    print "City:          ", row[1]
    print "County:        ", row[2]
    print "Population:    ", row[3]

%%writefile SdbINFO.py
import sqlite3
def Sdbinfo(unknown, storage):
    con = sqlite3.connect(storage)
    co = con.cursor()
    co.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS data 
    USING FTS4(unknown, row, columns);
    """)
    con.commit()
    
    conn = sqlite3.connect(unknown)
    conn.text_factory = str
    c = conn.cursor()
    res = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    row = c.fetchone()
    row = str(row)
    row = row.replace("(","");row = row.replace(",)","")
    row = row.replace("'","");row = row.replace(",","")
    cur = c.execute("select * from \"%s\"" %  row)
    columns = [description[0] for description in cur.description]
    col = str(columns)
    col = col.replace("[","");col = col.replace("]","")
    coll = col.replace("'","")
    print (row, coll)
    co.execute("INSERT into data (unknown, row, columns) values (?,?,?)",(unknown, row, coll))
    con.commit()
    conn.close()
    conn.close()
    return columns

!pwd

import SdbINFO
fname = "database.list"
def file_len(fname):
    with open(fname, encoding = 'unicode_escape') as f:
        for i, l in enumerate(f):
            pass
    total = i + 1
    return total

def readAll(fname, encoding = 'unicode_escape'):
    f = open(fname , 'r' )
    lines = f.readlines()
    f.close()
    return lines

def file_head(filein, encoding = 'unicode_escape'):
    count = 0
    fn = 0
    with open(filein, encoding = 'unicode_escape') as fin:
        for fline in fin:
            fline = str(fline)
            # the first line of an SQLITE data file reads " SQLite format 3@ "
            # this splits the line at the @ 
            fin = fline.split("@")
            for fi in fin:
                # This line seeks the string SQLite, That will identify the file as an SQLite database
                if count < 2 and "SQLite" in fi:
                    if len(fi) < 25:
                        return filein 
        

tl = file_len(fname)
#limit_memory(1000)
print ("Total Lines : ",tl)

for line in readAll(fname, encoding = 'unicode_escape'):
    line = line.replace("\n", "")
    sqlite = file_head(line)
    try:
        if len(sqlite) >6:
            
            storage = "NEW.db"
            database = sqlite.replace("\n", "")
            print (database)
            SdbINFO.Sdbinfo(database, storage)
    except:
        pass



storage = "NEW.db"
import sqlite3
con = sqlite3.connect(storage)
co = con.cursor()
for row in co.execute("SELECT ROWID, * from data"):
    print ("ROWID : ",row[0])
    print ("DATABASE : ",row[1])
    print ("TABLE : ",row[2])
    print ("COLUMNS : ",row[3])
    print ("-----------------")

con.close()

# /home/jack/rollerball/Library/AssetVersioning.db
# assetversion changeset, guid, name, parent, assettype, digest, oldversion, parentfolderid
# this is a databse created by reading RSS feeds
#database = "/home/jack/hubiC/Databases/bigfeedfts.db"


database ="/home/jack/miniconda3/pkgs/obspy-1.2.2-py37ha757849_2/lib/python3.7/site-packages/obspy/clients/filesystem/tests/data/tsindex_data/timeseries.sqlite"
# TABLE tsindex 
#network, station, location, channel, quality, version, starttime, endtime, samplerate,
#filename, byteoffset, bytes, hash, timeindex, timespans, timerates, format, filemodtime, updated, scanned
import sqlite3
con = sqlite3.connect(database)
co = con.cursor()
count = 0
for row in co.execute("SELECT ROWID, * from  tsindex"):
    print ("ROWID :       ",row[0])
    print ("network :     ",row[1])
    print ("station :     ",row[2])
    print ("location :    ",row[3])
    print ("channel :     ",row[4])
    print ("quality :     ",row[5])
    print ("version :     ",row[6])
    print ("starttime :   ",row[7])
    print ("endtime :     ",row[8])    
    print ("samplerate :  ",row[9])
    print ("filename :    ",row[10])
    print ("byteoffset :  ",row[11])
    print ("bytes :       ",row[12])
    print ("hash :        ",row[13])
    print ("timeindex :   ",row[14])
    print ("timespans :   ",row[15])
    print ("timerates :   ",row[16])
    print ("format :      ",row[17])
    print ("filemodtime : ",row[18])
    print ("updated :     ",row[19])
    print ("scanned :     ",row[20])    
    
    
    
    print ("-----------------")
    count = count + 1
    if count >10:
        break

con.close()

#import resource

def limit_memory(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))
fname = "database.list"
def file_len(fname):
    with open(fname, encoding = 'unicode_escape') as f:
        for i, l in enumerate(f):
            pass
    total = i + 1
    return total

def readAll(fname):
    f = open(fname, 'r', encoding = 'unicode_escape'  )
    lines = f.readlines()
    f.close()
    return lines

def file_head(filein):
    count = 0
    fn = 0
    with open(filein, encoding = 'unicode_escape' ) as fin:
        for fline in fin:
            fline = str(fline)
            # the first line of an SQLITE data file reads " SQLite format 3@ "
            # this splits the line at the @ 
            fin = fline.split("@")
            for fi in fin:
                # This line seeks the string SQLite, That will identify the file as an SQLite database
                if count < 2 and "SQLite" in fi:
                    if len(fi) < 25:
                        return filein 
        

tl = file_len(fname)
#limit_memory(1000)
print ("Total Lines : ",tl)

for line in readAll(fname):
    line = line.replace("\n", "")
    sqlite = file_head(line)
    try:
        if len(sqlite) >6:
            print (sqlite)
    except:
        pass



import SdbINFO
database = "/home/jack/Downloads/basicCRUDops_NodeJs_sqlite-main/database/employee.db"
storage = "DBinfo.db"
SdbINFO.Sdbinfo(database, storage)

def file_head(filein):
    count = 0
    with open(filein, encoding = 'unicode_escape' ) as fin:
        for fline in fin:
            while count < 1:
                print (count,fline)
                count = count+1
            return    
filein = "/home/jack/unique-End2.db" 
file_head(filein)

def file_head(filein):
    count = 0
    with open(filein) as fin:
        for fline in fin:
            while count < 1:
                print (count,fline)
                count = count+1
            return    
filein = "/home/jack/data/db.sqlite3" 
file_head(filein)

def file_head(filein):
    count = 0
    with open(filein, encoding= 'unicode_escape') as fin:
        for fline in fin:
            while count < 8:
                print (count,fline)
                count = count+1
            return    
filein = "/home/jack/data/db.sqlite3" 
file_head(filein)

#import resource

def limit_memory(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))
fname = "database.list"
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    total = i + 1
    return total

def readAll(fname):
    f = open(fname , 'r' )
    lines = f.readlines()
    f.close()
    return lines

def file_head(filein):
    count = 0
    fn = 0
    with open(filein) as fin:
        for fline in fin:
            fline = str(fline)
            # the first line of an SQLITE data file reads " SQLite format 3@ "
            # this splits the line at the @ 
            fin = fline.split("@")
            for fi in fin:
                # This line seeks the string SQLite, That will identify the file as an SQLite database
                if count < 2 and "SQLite" in fi:
                    if len(fi) < 25:
                        print filein
                        print fi
                        print "----------------------------"  
                        count = count+1
                        return filein 
        

tl = file_len(fname)
#limit_memory(1000)
print "Total Lines : ",tl

for line in readAll(fname):
    line = line.replace("\n", "")
    file_head(line)

from time import sleep
def file_head(filein):
    count = 0
    with open(filein) as fin:
        for fline in fin:
            fline = str(fline)
            fin = fline.split(" ")
            print "\n",filein,"\n________________\n"
            for fi in fin:
                if count < 4:
                    print count,fi             
                    count = count+1
            return  
            
filein = "/home/jack/unique-End2.db"            
file_head(filein)            


fname = "database.list"
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    total = i + 1
    return total

def readAll(fname):
    f = open(fname , 'r' )
    lines = f.readlines()
    f.close()
    return lines

def file_head(filein):
    count = 0
    with open(filein) as fin:
        for fline in fin:
            fline = str(fline)
            fin = fline.split(" ")
            for fi in fin:
                while count < 10:
                    print "\n",filein,"\n",count,fi,"\n________________\n"
                    count = count+1
                return    
        

tl = file_len(fname)
print "Total Lines : ",tl
for line in readAll(fname):
    line = line.replace("\n", "")
    file_head(line)

f = open( 'database.list' , 'r' )
line = f.readline()
while line :
    print line
    line = f.readline()
f.close()

import SdbINFO13
from time import sleep
import sys
def main():
    title = "database.list"
    filein = open(title,"r").readlines()
    fn = 0
    while databases in filein:
        count = 0
        fn = fn+1
        database = str(databases)
        database = database.replace("\n","")
        unknown = database
        print "1 : ",unknown
        while count < 6:
            count =0
            with open((unknown).decode('utf8')) as infile:
                for lines in infile:
                    line = lines.split(" ")
                    for li in line:

                        sleep(.5)
                        print fn,"/",count," : ",li
                        count = count +1
                        
                        
main()                        
                        

import SdbINFO13
from time import sleep
import sys
count = 0
storage = "Exp.db"
title = "database.list"
filein = open(title,"r").readlines()
for databases in filein:
    database = str(databases)
    database = database.replace("\n","")
    unknown = database
    print unknown
    SdbINFO13.Sdbinfo(unknown, storage)
    sleep(.5)
    count = count +1
    if count > 10:
        break

import SdbINFO
from time import sleep
title = "database.list"
for database in open(title,"r").readlines():
    try:
        storage = "DBinfo.db"
    except OperationalError:
        print title," is not a database."
        pass

    
    database = database.replace("\n","")
    #database = '/home/jack/Desktop/databases/PDE2db.db'
    #databasx = "/home/jack/Desktop/databases/PDE2db.db"
    #cur = c.execute("select * from \"%s\"" %  row)
    #SdbINFO.Sdbinfo("?", storage),(database)
    unknown = database
    print unknown

    SdbINFO.Sdbinfo(unknown, storage)
    sleep(.5)


!ls /home/jack/unique-End2.db

test = "bunch o junk"
total = "this is \'%s\'" % test
print total

test = "bunch o junk"
total = "this is '?'",(test) 
print total[0],total[1]

import SdbINFO
database = "/home/jack/unique-End2.db"
storage = "DBinfo.db"
SdbINFO.Sdbinfo(database, storage)

import os
count = 0
fn = 0
title = "database.list"
for lines in open(title,"r").readlines():
    fn = fn + 1
    filename = os.path.basename(lines)
    lines = lines.replace("\n","")
    b = os.path.getsize(lines)
    a = float(b/1000)
    filename = filename.replace("\n","")
    print fn," :",a,"k  -",lines
    count = count +1

from time import sleep
import sys
count = 0
title = "/home/jack/nltk_data/corpora/city_database/city.db"
# ��j!!�tablecity_tablecity_tableCREATE TABLE city_table

title = "/home/jack/Desktop/databases/PDE2db.db"
#SQLite format 3@  f�
#tablepde_docsizepde_docsizeCREATE TABLE 'pde_docsize'(docid INTEGER P

title = "/home/jack/rollerball/Library/AssetVersioning.db"
SQLite format 3@  -����)��d!!�tablerow_countsrow_countCREATE TABLE row_counts 

#title = "/home/jack/nltk_data/corpora/city_database/city.db"
#title = "/home/jack/nltk_data/corpora/city_database/city.db"
for lines in open(title,"r").readlines():
    sleep(.5)
    print lines
    count = count +1
    if count > 6:sys.exit()

from time import sleep
import sys
count = 0
title = "database.list"
for lines in open(title,"r").readlines():
    sleep(.5)
    print lines
    count = count +1
    if count > 6:
        break

from time import sleep
import sys
count = 0
title = "database.list"
for lines in open(title,"r").readlines():
    sleep(.5)
    print lines
    lines = lines.replace("\n","")
    count = count +1
    if count > 6:sys.exit()


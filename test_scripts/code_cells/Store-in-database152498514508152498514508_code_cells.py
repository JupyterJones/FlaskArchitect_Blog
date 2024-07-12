import sqlite3
search = raw_input("SEARCH : ")
conn=sqlite3.connect("/home/jack/hubiC/Databases/SNIPPETS.db")
conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")
c = conn.cursor()
for row in c.execute('SELECT rowid,* FROM snippets WHERE snippets MATCH (?)', (search,) ):
    print row[1]

import sqlite3
database = "/home/jack/hubiC/Databases/SNIPPETS.db"
conn = sqlite3.connect(database)
conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")
Search = raw_input("SEARCH : ")
c = conn.cursor()
for row in c.execute('SELECT rowid,* FROM snippets'):
    if Search in row[1]:
        print row[0]
        print row[1]
        print row[2]
        print "------------------------------------"

import sqlite3
conn=sqlite3.connect("/home/jack/hubiC/Databases/SNIPPETS.db")
conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")
c = conn.cursor()
code = """
locked db database locked can not use database 
Response to a locked database

!fuser /home/jack/hubiC/Databases/Stuff.db
!kill -9 18879
"""
keywords = """
locked db database locked can not use database 
Response to a locked database

!fuser /home/jack/hubiC/Databases/Stuff.db
!kill -9 18879
"""
c.execute('INSERT into snippets VALUES (?,?)', (code, keywords) )
conn.commit()
conn.close()

import sqlite3
import re
import sys
import time
database = "/home/jack/hubiC/Databases/Stuff.db"
conn = sqlite3.connect(database)
conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")
Search = raw_input("SEARCH : ")
c = conn.cursor()
for row in c.execute('SELECT rowid,* FROM stuff'):
    if Search in row:
        print row[0],row[1],row[2]

import sqlite3
import re
import sys
import time
database = "/home/jack/hubiC/Databases/Stuff.db"
conn = sqlite3.connect(database)
conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")
c = conn.cursor()
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS stuff 
USING FTS4(info, description);
""")
conn.commit()
conn.close()

import sqlite3
database = "/home/jack/hubiC/Databases/Stuff.db"
conn = sqlite3.connect(database)
conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")
c = conn.cursor()
for row in c.execute('SELECT rowid,* FROM stuff WHERE rowid = (?)', (search,) ):
    print row[1]

import sqlite3
import re
import sys
import time
database = "/home/jack/hubiC/Databases/Stuff.db"
conn = sqlite3.connect(database)
conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")
ID = raw_input("DELETE rowid: ")
ID = int(ID)
c = conn.cursor()
c.execute('DELETE FROM stuff WHERE ROWID = (?)', (ID,))
conn.commit()

import sqlite3
import re
import sys
import time
database = "/home/jack/hubiC/Databases/Stuff.db"
conn = sqlite3.connect(database)
conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")
c = conn.cursor()
for row in c.execute('SELECT rowid,* FROM stuff'):
    print row[0],row[1],row[2]


!fuser /home/jack/hubiC/Databases/Stuff.db

!kill -9 18879

locked db database locked can not use database 
Response to a locked database

!fuser /home/jack/hubiC/Databases/Stuff.db
!kill -9 18879

import sqlite3
import re
import sys
import time
database = "/home/jack/hubiC/Databases/Stuff.db"
#database = "junk2.db"
conn = sqlite3.connect(database)
Search = raw_input("SEARCH : ")
conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")
c = conn.cursor()
for row in c.execute('SELECT ROWID,* FROM stuff WHERE stuff MATCH (?)', (Search,)):
    if Search in row:
        print row[0],row[1],row[2]

!rm multitable.db

import sqlite3
import re
import sys
import time
database = "/home/jack/hubiC/Databases/Stuff.db"
#database = "junk2.db"
conn = sqlite3.connect(database)
ROWID = raw_input("SEARCH : ")
conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")
c = conn.cursor()
for row in c.execute('DELETE * FROM stuff WHERE ROWID = ?', (ROWID,)):
    print row[0],row[1],row[2]

import sqlite3
search = raw_input("SEARCH : ")
conn=sqlite3.connect("/home/jack/hidden/PW.db")
c = conn.cursor()
for row in c.execute('SELECT rowid,* FROM PASSWD WHERE PASSWD MATCH (?)', (search,) ):
    print row[1]

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
    cur = c.execute("select * from '%s'" %  row)
    columns = [description[0] for description in cur.description]
    return columns

database = "multiple-table.db"
#database = "/home/jack/hidden/PW.db"
dbinfo(database)

import sqlite3
def dbinfo(database):
    conn = sqlite3.connect(database)
    conn.text_factory = str
    c = conn.cursor()
    try:
        res = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        # USE fetch all for multiple tables
        row = c.fetchall()
        row = str(row)
        row = row.replace("(","");row = row.replace(",)","")
        row = row.replace("'","")
        print row
        cur = c.execute("select * from '%s'" %  row)
        columns = [description[0] for description in cur.description]
        return columns
    except:
        pass    
database = "multiple-table.db"
#database = "/home/jack/hidden/PW.db"
dbinfo(database)

import sqlite3
import re
import sys
import time
database = "multiple-table.db"
conn = sqlite3.connect(database)
conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")
c = conn.cursor()
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS python 
USING FTS4(info, description); 
""")
conn.commit()
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS javascript 
USING FTS4(info, description);
""")
conn.commit()
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS bash 
USING FTS4(info, description);
""")
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS html 
USING FTS4(info, description);
""")
conn.commit()
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS misc 
USING FTS4(info, description);
""")
conn.commit()
info="""
bashbashbash
"""
description ="""
bash what kind of fears
"""
c.execute("INSERT into bash(info, description) VALUES (?,?)", (info,description));
conn.commit()
conn.close()

import sqlite3
import re
import sys
import time
database = "multiple-table.db"
conn = sqlite3.connect(database)
conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")
c = conn.cursor()
info="""
2  MISC __ html html html html
"""
description ="""
2  MISC ___ html html what kind of fears
"""
c.execute("INSERT into misc(info, description) VALUES (?,?)", (info,description));
conn.commit()
conn.close()

import sqlite3
import re
import sys
import time
database = "multiple-table.db"
conn = sqlite3.connect(database)
conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")
#Search = raw_input("SEARCH : ")
#Search = str(Search)
c = conn.cursor()
for row in c.execute('SELECT rowid,* FROM javascript'):
    print row[0],row[1],row[2]





# %load /usr/local/bin/NOTE
#!/usr/bin/python3
import sys
import sqlite3
conn = sqlite3.connect("/home/jake/Desktop/pas.bak/notes.db")
conn.text_factory = str
c = conn.cursor()
if len(sys.argv) < 3:
     print ("\n******* NOTE - Notes Editor **************")
     print ("Not enough options were passed.")     
     print ("NOTE requires 2 arguments. the first -H , -R , -I , -D or -S .\nThe second can be a period.")
     print ("If printing the database -T also add a filename of your choice ( no quotes required ):")
     print (" Example: NOTE -T Data2Text.txt")   
     print ("If wanting to read all entries use -R . (use the period)") 
     print ("even use the period with help.  -H .   must be entered.")
     print ("******************************************\n")
     sys.exit()
mod = sys.argv[1]
def create():

    import sqlite3
    conn = sqlite3.connect("/home/jake/Desktop/pas.bak/notes.db")
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
    conn.commit()
    conn.close()
    return data

def search(data,conn=conn, c=c):
    #for row in c.execute("SELECT ROWID,* FROM PROJECT WHERE input MATCH ?",(data,)):
    #    print ("\nINFO Found Here:",row[0],row[1])
    for row in c.execute("SELECT ROWID,* FROM PROJECT"):
        if data in row[1]:    
            print ("\nINFO Found Here:\n",row[0],row[1])
    #conn.commit()
    #conn.close()
def delete(rowid,conn=conn, c=c):
    c.execute("DELETE FROM PROJECT WHERE rowid = ?", (rowid,))
    conn.commit()
    conn.close()
    text = "ROWID "+rowid+" Deleted"
    return text

def main():
    conn = sqlite3.connect("/home/jake/Desktop/pas.bak/notes.db")
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        print (row[0],": ",row[1])

def prtmain(filename):
    fn = open(filename, "w")
    conn = sqlite3.connect("/home/jake/Desktop/notes.db")
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        TEXT = "id:"+str(row[0])+"\n"+str(row[1])
        TEXT = str(TEXT)
        TEXT = TEXT.replace('\\n','\n')
        TEXT = "".join(TEXT)
        fn.write(TEXT+'\n----\n')

def HELP():
    TXT = """
    USE: NOTE argv[1] argv[2]
    argv[1] sets the mod:
    -I insert / -D delete / -R read / -H help
    examples:
    Notice the entry is in parenthese.
    -I  to insert "STUFF to be inserted"
    NOTE -I "STUFF to be inserted"
    -D to delete where rowid is 3
    NOTE -D 3
    Notice the period after -R . 
    -R . read all
    To search for the term "current project"
    NOTE -S 3
    -S "current project"
    NOTE -R .
    -H help on options
    NOTE -H .
    """
    print (TXT)

if mod == "-H" or mod == "h":
    HELP()        
if mod == "-R" or mod == "-r":
    main()
if mod == "-I" or mod == "-i":
    data = sys.argv[2]
    insert(data)
if mod == "-D" or mod == "-d":
    rowid = sys.argv[2]
    delete(rowid) 
if mod == "-S" or mod == "-s":
    data = sys.argv[2]
    search(data)       
if mod == "-T":
    filename = sys.argv[2]
    prtmain(filename)
if mod == "-C" or mod == "-c":
    create()
    print (create)
else:
    print ("_________________\n")
    print (sys.argv[2],"Command Completed")
    


import sys
import sqlite3
info = set()
def main():
    conn = sqlite3.connect("/home/jake/Desktop/pas.bak/notes.db")
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        print (row[1])
        info.add(row[1])
main()

!rm allnotes.data



!locate notes.db >> allnotes.data

# %load allnotes.data
/home/jack/Desktop/Pas.bak/notes.db
/home/jack/Desktop/SITE-bak/lbry-react/KEEP-NOTES/notes.db
/home/jack/Desktop/site/lbry-react/KEEP-NOTES/notes.db
/home/jake/Desktop/pas.bak/notes.db
/home/jake/pas.bak/notes.db
/mnt/73777e11-76da-4fee-ba95-e731ac3ca459/Desktop/notes.db
/mnt/73777e11-76da-4fee-ba95-e731ac3ca459/Desktop/Pas.bak/notes.db
/mnt/73777e11-76da-4fee-ba95-e731ac3ca459/Desktop/WORKING/reactwithprisma/notes.db
/mnt/73777e11-76da-4fee-ba95-e731ac3ca459/Desktop/WORKING/reactwithprisma/starter/notes.db
/mnt/73777e11-76da-4fee-ba95-e731ac3ca459/Desktop/WORKING/reactwithprisma/starter/prisma/notes.db
/mnt/73777e11-76da-4fee-ba95-e731ac3ca459/Desktop/site/lbry-react/KEEP-NOTES/notes.db
/mnt/73777e11-76da-4fee-ba95-e731ac3ca459/Desktop/starter/prisma/notes.db
/mnt/73777e11-76da-4fee-ba95-e731ac3ca459/Downloads/xvid/pas.bak/notes.db
/mnt/73777e11-76da-4fee-ba95-e731ac3ca459/Info-Central/KEEP-NOTES/notes.db
/mnt/73777e11-76da-4fee-ba95-e731ac3ca459/Info-Central/docs/KEEP-NOTES/notes.db
/mnt/73777e11-76da-4fee-ba95-e731ac3ca459/bak/bak/KEEP-NOTES/notes.db
/mnt/73777e11-76da-4fee-ba95-e731ac3ca459/bak/bak/docs/KEEP-NOTES/notes.db
/mnt/73777e11-76da-4fee-ba95-e731ac3ca459/lbry-react/KEEP-NOTES/notes.db
/mnt/73777e11-76da-4fee-ba95-e731ac3ca459/lbry-react (copy 1)/KEEP-NOTES/notes.db
/mnt/73777e11-76da-4fee-ba95-e731ac3ca459/lbry-react-old/KEEP-NOTES/notes.db
/mnt/73777e11-76da-4fee-ba95-e731ac3ca459/pas.bak/notes.db


DATA = open("allnotes.data", "r").readlines()
DBASES = []
for line in DATA:
    line=line.replace("\n","")
    print (line)
    DBASES.append(line)


import sqlite3
def create(dbase):
    conn = sqlite3.connect(dbase)
    conn.text_factory = str
    c = conn.cursor()
    c.execute("CREATE VIRTUAL TABLE IF NOT EXISTS PROJECT USING FTS4 (input)")
    conn.commit()
    text = "Database Created"
    return text
#debug dbase = "/home/jack/Desktop/pas.bak/junk.db"
dbase = "/home/jack/Desktop/pas.bak/ALLnotes.db"

create(dbase)

import sqlite3
def insert(data,dbase):
    conn = sqlite3.connect(dbase)
    conn.text_factory = str
    c = conn.cursor()
    c.execute("INSERT into PROJECT values (?)", (data,))
    for row in c.execute("SELECT ROWID,* FROM PROJECT ORDER BY ROWID DESC LIMIT 1"):
        print ("\nPOST VERIFIED:\n",row[0],row[1])
    conn.commit()
  
    return data
dbase="/home/jack/Desktop/pas.bak/ALLnotes.db"
insert(data,dbase)

dbase="/home/jack/Desktop/pas.bak/ALLnotes.db"
for data in DBASES:
    print(data)

dbase="/home/jack/Desktop/pas.bak/ALLnotes.db"
for data in DBASES:
    print(data)

import sys
import sqlite3
info = set()
def main(Dbase):
    conn = sqlite3.connect(Dbase)
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        print (row[1])
        info.add(row[1])

#Dbase = "/home/jack/Desktop/pas.bak/notes.db"
Dbase="/home/jack/Desktop/pas.bak/ALLnotes.db"
main(Dbase)

for Dbase in DBASES:
    print(Dbase)

Dbase="/home/jack/Desktop/pas.bak/ALLnotes.db"

import sqlite3
def insert(data,dbase):
    conn = sqlite3.connect(dbase)
    conn.text_factory = str
    c = conn.cursor()
    #c.execute("INSERT into PROJECT values (?)", (data,))
    for row in c.execute("SELECT ROWID,* FROM PROJECT"):
        print ("\nPOST VERIFIED:\n",row[0],row[1])
    conn.commit()
  
    return data
dbase="/home/jack/Desktop/pas.bak/ALLnotes.db"
insert(data,dbase)

import sys
import sqlite3
info = set()
def main(Dbase):
    conn = sqlite3.connect(Dbase)
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        print (row[1])
        data = row[1]
        insert(data,dbase)
        info.add(row[1])



for Dbase in DBASES:
    main(Dbase)

    print(Dbase)

import sqlite3
def create(dbase):
    conn = sqlite3.connect(dbase)
    conn.text_factory = str
    c = conn.cursor()
    c.execute("CREATE VIRTUAL TABLE IF NOT EXISTS PROJECT USING FTS4 (input)")
    conn.commit()
    text = "Database Created"
    return text
#debug dbase = "/home/jack/Desktop/pas.bak/junk.db"
dbase = "/home/jack/Desktop/pas.bak/ALL.db"
create(dbase)
def insert(data,dbase):
    conn = sqlite3.connect(dbase)
    conn.text_factory = str
    c = conn.cursor()
    #c.execute("INSERT into PROJECT values (?)", (data,))
    for row in c.execute("SELECT ROWID,* FROM PROJECT"):
        print ("\nPOST VERIFIED:\n",row[0],row[1])
    conn.commit()
  
    return data
dbase="/home/jack/Desktop/pas.bak/ALL.db"
insert(data,dbase)
 
for data in info:
    #print(data)
    insert(data,dbase)
    #print(len(info))

import sys
import sqlite3
info = set()
def main(dbase):
    conn = sqlite3.connect(dbase)
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        print (row[1])
        info.add(row[1])
dbase="/home/jack/Desktop/pas.bak/ALL.db"
main(dbase)

conn.commit()
conn.close()

!pwd

!sudo updatedb

import sys
import sqlite3
#info = set()
def main():
    conn = sqlite3.connect("mnt/73777e11-76da-4fee-ba95-e731ac3ca459/Desktop/WORKING/reactwithprisma/starter/notes.db")
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        print (row[1])
        info.add(row[1])
main()

# %load NOTE
#!/usr/bin/python3
import sys
import sqlite3
conn = sqlite3.connect("/home/jake/Desktop/pas.bak/notes.db")
conn.text_factory = str
c = conn.cursor()
if len(sys.argv) < 3:
     print ("\n******* NOTE - Notes Editor **************")
     print ("Not enough options were passed.")     
     print ("NOTE requires 2 arguments. the first -H , -R , -I , -D or -S .\nThe second can be a period.")
     print ("If printing the database -T also add a filename of your choice ( no quotes required ):")
     print (" Example: NOTE -T Data2Text.txt")   
     print ("If wanting to read all entries use -R . (use the period)") 
     print ("even use the period with help.  -H .   must be entered.")
     print ("******************************************\n")
     sys.exit()
mod = sys.argv[1]
def create():

    import sqlite3
    conn = sqlite3.connect("/home/jake/Desktop/pas.bak/notes.db")
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
    conn.commit()
    conn.close()
    return data

def search(data,conn=conn, c=c):
    #for row in c.execute("SELECT ROWID,* FROM PROJECT WHERE input MATCH ?",(data,)):
    #    print ("\nINFO Found Here:",row[0],row[1])
    for row in c.execute("SELECT ROWID,* FROM PROJECT"):
        if data in row[1]:    
            print ("\nINFO Found Here:\n",row[0],row[1])
    #conn.commit()
    #conn.close()
def delete(rowid,conn=conn, c=c):
    c.execute("DELETE FROM PROJECT WHERE rowid = ?", (rowid,))
    conn.commit()
    conn.close()
    text = "ROWID "+rowid+" Deleted"
    return text

def main():
    conn = sqlite3.connect("/home/jake/Desktop/pas.bak/notes.db")
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        print (row[0],": ",row[1])

def prtmain(filename):
    fn = open(filename, "w")
    conn = sqlite3.connect("/home/jake/Desktop/notes.db")
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        TEXT = "id:"+str(row[0])+"\n"+str(row[1])
        TEXT = str(TEXT)
        TEXT = TEXT.replace('\\n','\n')
        TEXT = "".join(TEXT)
        fn.write(TEXT+'\n----\n')

def HELP():
    TXT = """
    USE: NOTE argv[1] argv[2]
    argv[1] sets the mod:
    -I insert / -D delete / -R read / -H help
    examples:
    Notice the entry is in parenthese.
    -I  to insert "STUFF to be inserted"
    NOTE -I "STUFF to be inserted"
    -D to delete where rowid is 3
    NOTE -D 3
    Notice the period after -R . 
    -R . read all
    To search for the term "current project"
    NOTE -S 3
    -S "current project"
    NOTE -R .
    -H help on options
    NOTE -H .
    """
    print (TXT)

if mod == "-H" or mod == "h":
    HELP()        
if mod == "-R" or mod == "-r":
    main()
if mod == "-I" or mod == "-i":
    data = sys.argv[2]
    insert(data)
if mod == "-D" or mod == "-d":
    rowid = sys.argv[2]
    delete(rowid) 
if mod == "-S" or mod == "-s":
    data = sys.argv[2]
    search(data)       
if mod == "-T":
    filename = sys.argv[2]
    prtmain(filename)
if mod == "-C" or mod == "-c":
    create()
    print (create)
else:
    print ("_________________\n")
    print (sys.argv[2],"Command Completed")
    





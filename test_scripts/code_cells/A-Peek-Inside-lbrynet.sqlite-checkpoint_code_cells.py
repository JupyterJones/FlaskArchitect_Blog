!ls /home/jack/.local/share/lbry/lbrynet/lbrynet.sqlite

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
    print ("Table: ",row)
    cur = c.execute("select * from '%s'" %  row)
    columns = [description[0] for description in cur.description]
    return "COLUMNS :",columns

# if run directly
database="/home/jack/.local/share/lbry/lbrynet/lbrynet.sqlite"
dbinfo(database)


import sqlite3
# Define a function
def peek_in(database):
    cnt=0
    # connect to a database
    conn = sqlite3.connect(database)
    # FYI - In this case 'text_factory' not required I use it from habit
    # By default "conn" is set to unicode and the sqlite3 module will return Unicode objects for TEXT
    # If you use "text_factory = st". it returns bytestrings instead.
    conn.text_factory = str
    c = conn.cursor()
    for res in c.execute("SELECT ROWID,* FROM blob;"):
        cnt=cnt+1
        if cnt<5:
            print ("------------- ROWiD :",res[0],"---------------\n")
            print ('blob_hash :',res[1])
            print ('blob_length :',res[2])
            print ('next_announce_time :',res[3])
            print ('should_announce :',res[4])
            print ('status :',res[5])
            print ('last_announced_time :',res[6])
            print ('single_announce :',res[7])
            print ("---------------------------------------\n")
        
database="/home/jack/.local/share/lbry/lbrynet/lbrynet.sqlite"    
peek_in(database)    
    




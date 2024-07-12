# Current directory
!pwd

import os

user_input = input('What is the name of your directory ? :')
directory = os.listdir(user_input)

searchstring = input('What word are you trying to find ? :')

for fname in directory:
    if os.path.isfile(user_input + os.sep + fname):
        # Full path
        f = open(user_input + os.sep + fname, 'r',encoding='latin1')

        if searchstring in f.read():
            print('found string in file: %s' % fname)
        else:
            print('.', end=" ")
        f.close()

!grep -Ril '"private_key"' ./

import sqlite3
conn = sqlite3.connect("stream_list2.db")
c = conn.cursor()
# Search database for words private_key and seed 
for row in c.execute("SELECT ROWID,* from LBRY"):
    if '"private_key"' in row[1] or '"seed"' in row[1]:
        print (row[0],": ",row[1])


import sqlite3
conn = sqlite3.connect("stream_list2.db")
c = conn.cursor()
SEARCH = input("SEARCH: ")
for row in c.execute("SELECT ROWID,* from LBRY"):
    if SEARCH in row[1]:
        print (row[0],": ",row[1])







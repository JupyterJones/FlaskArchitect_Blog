#%%writefile checkDB
#!/usr/bin.python2
from Completed import track_download
import subprocess
import sqlite3
database = 'LBRYDATA.db'
conn = sqlite3.connect(database)  
c=conn.cursor()
search = input("SEARCH: ")
ID = []
cnt=0
for row in c.execute('SELECT ROWID, * FROM LBRY'):
    if search in row[1] or search in row[2]:
        Cnt=str(cnt)
        All=Cnt+"-",row[1],":",row[2]
        print (All)
        cnt=cnt+1
        ID.append(All)
download = int(input("download  number: "))
if download==99:raise SystemExit("Stopped by 99 !") 
print ("----------------")
print ("ID to Download : ",ID[download])
print ("----------------")
ST = str(ID[download])
Id = ST.split("'")
print (Id[len(Id)-2])


import os

os.getcwd()

!mkdir /home/jack/Desktop/LBRY-toolbox/DownloadDirectory

# This the full path to current directory
import os

DownloadDirectory = os.getcwd()+"/DownloadDirectory"
print (DownloadDirectory)

!ls DownloadDirectory

!ls DownloadDirectory | pr -4 -t

#%%writefile DB_Current
#!/usr/bin.python2
from Completed import track_download
import subprocess
import sqlite3
import os
if not os.path.exists('DownloadDirectory'):
    os.makedirs('DownloadDirectory')
database = 'LBRYDATA.db'
conn = sqlite3.connect(database)  
c=conn.cursor()
search = input("SEARCH: ")
if search == 99:exit()
ID = []
cnt=0
for row in c.execute('SELECT ROWID, * FROM LBRY'):
    if search in row[1] or search in row[2]:
        Cnt=str(cnt)
        All=Cnt+"-",row[1],":",row[2]
        print (All)
        cnt=cnt+1
        ID.append(All)
download = int(input("download  number: "))
print ("---------------------------")
print ("ID to Download",ID[download])
print ("---------------------------")
ST = str(ID[download])
Id = ST.split("'")
print (Id[len(Id)-2])
bashCommand = "lbrynet get "+Id[len(Id)-2]+" --download_directory=/home/jack/Desktop/LBRY-toolbox/DownloadDirectory"
# This downloads to the Default LBRY folder ( $HOME/Downloads )
# bashCommand = "lbrynet get "+Id[len(Id)-2]
print (bashCommand)
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate() 
print ("waiting ...")
#track_download()

lbrynet get  --download_directory=/home/jack/Desktop/LBRY-toolbox/DownloadDirectory

!lbrynet get how-to-use-kdenlive-video-editor-on-kali#ef4aa44d360e2cce99ef3677371aadc84f03bfb2 --download_directory=/home/jack/Desktop/LBRY-toolbox/DownloadDirectory

%%writefile DB_Download
#!/usr/bin.python2
from Completedpy2 import track_download
import subprocess
import sqlite3
database = 'LBRYDATA.db'
conn = sqlite3.connect(database)  
c=conn.cursor()
search = raw_input("SEARCH: ")
ID = []
cnt=0
for row in c.execute('SELECT ROWID, * FROM LBRY'):
    if search in row[1] or search in row[2]:

        Cnt=str(cnt)
        print Cnt,"-",row[0],":",row[1],":",row[2]
        All=Cnt+"-",row[0],":",row[1],":",row[2]
        cnt=cnt+1        
        ID.append(All)
download = int(raw_input("download  number: "))
#print ID[download-1]
print "ID",ID[download]
print "---------------------------"
ST = str(ID[3])
Id = ST.split("'")
print len(Id)-2
print Id[len(Id)-2]
#for item in Id:
#    print item
bashCommand = "lbrynet get "+Id[len(Id)-2]
print bashCommand
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate() 
print "waiting ..."
track_download()


import subprocess
bashCommand = "lbrynet get synfig-studio-kdenlive-create-animated#b6847ad5de1d9c72ea49a15afbd6436839a1b5c4 --download_directory= /home/jack/Desktop/lighthouse"
print bashCommand
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate() 

os.getcwd()

# Download to lbry default $HOME/Downloads
!lbrynet get synfig-studio-kdenlive-create-animated#b6847ad5de1d9c72ea49a15afbd6436839a1b5c4 




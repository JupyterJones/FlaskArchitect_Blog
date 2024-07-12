!ls /home/jack/Downloads



import os
from time import sleep
import urllib, json
import urllib.request
import requests
import sys
import subprocess
from Completed import track_download
import sqlite3
import watchVID
database = 'LBRYDATA.db'
conn = sqlite3.connect(database)
sql = '''create table if not exists LBRY(
KEYWORDS TEXT, DATA TEXT, unique (DATA));'''
conn.execute(sql) # shortcut for conn.cursor().execute(sql)
conn.commit()
c=conn.cursor()
search=input("SEARCH : ")
url = "https://lighthouse.lbry.com/search?s="+search
response = urllib.request.urlopen(url)
data = json.loads(response.read())
cnt=0
LIST =[]
for line in data:
    cnt=cnt+1
    line = str(line)
    line =line.replace("u'","");line =line.replace("{claimId': ","")
    line =line.replace("', name':","");line =line.replace("}","")
    line =line.replace(",","");line =line.replace("'","")
    #line =line[:-1]
    #print (line)
    line=line.split(" ")
    print (cnt,line[3]+"#"+line[1])
    LIST.append(line[3]+"#"+line[1])
    content=line[3]+"#"+line[1]

!lbrynet get rental-income-new-service-item-new#25be251a20286034b65362f57d84e3e84bfb47f4


!ls -rant /home/jack/Downloads

!ffmpeg -i /home/jack/Downloads/javascript-tutorial-sorting.mp4 -vf scale=-1:360 -strict -2 -y /home/jack/Downloads/javascript-tutorial-sortingS.mp4

!ls /home/jack/Desktop/LBRY-toolbox/Downloads

!ls /home/jack/Desktop/LBRY-toolbox/Downloads/nature-sounds-1-hour-river.mp4

!cp vid.html /var/www/lbry-toolbox.com/public/videos/index.html

!cp vid.html

 %%writefile vid.html
<htm>
<video width="640" height="360" controls>
<source src="nature-sounds-1-hour-river.mp4" type="video/mp4">
Your browser does not support the video tag.
</video> 

from IPython.display import Video

Video("Downloads/nature-sounds-1-hour-river.mp4")

from IPython.display import HTML

HTML("""
    <video alt="test" controls>
        <source src="/home/jack/Downloads/javascript-tutorial-sortingS.mp4" type="video/mp4">
    </video>
""")

!ls /home/jack/Downloads/rental-income-new-service-item.mp4

import os
from time import sleep
import urllib, json
import urllib.request
import requests
import sys
import subprocess
from Completed import track_download
import sqlite3
import watchVID
database = 'LBRYDATA.db'
conn = sqlite3.connect(database)
sql = '''create table if not exists LBRY(
KEYWORDS TEXT, DATA TEXT, unique (DATA));'''
conn.execute(sql) # shortcut for conn.cursor().execute(sql)
conn.commit()
c=conn.cursor()
search=input("SEARCH : ")
url = "https://lighthouse.lbry.com/search?s="+search
response = urllib.request.urlopen(url)
data = json.loads(response.read())
cnt=0
LIST =[]
for line in data:
    cnt=cnt+1
    line = str(line)
    line =line.replace("u'","");line =line.replace("{claimId': ","")
    line =line.replace("', name':","");line =line.replace("}","")
    line =line.replace(",","");line =line.replace("'","")
    #line =line[:-1]
    #print (line)
    line=line.split(" ")
    print (cnt,line[3]+"#"+line[1])
    LIST.append(line[3]+"#"+line[1])
    content=line[3]+"#"+line[1]
    try:
        c.execute("INSERT INTO LBRY VALUES (?,?)", (search, content))
    except:
        pass
conn.commit()
conn.close()
choice =int(input("Enter the number you wish to download: Type 99 to exit "))
#if choice==99:raise SystemExit("Stop right there!")
if choice==99:raise SystemExit("Stopped by 99 !")
print ("You will be downloading:",(LIST[choice-1]))

requests.post("http://localhost:5279", json={"method": "get", "params": {"uri": LIST[choice-1] }}).json()
print ("Monitoring filesize increase of claim id "+LIST[choice-1][:-30])
'''
bashCommand = "lbrynet get "+LIST[choice-1]
print bashCommand
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print "Monitoring filesize increase of claim id "+LIST[choice-1][:-30]
'''
track_download()

#uncomment below to auto-open vlc to view the downloaded video
#try:
#    watchVID.WATCH()
#except:
#    sys.exit()


!ls





import shutil
help(shutil.move)

#shutil.move(src, dst)

import sqlite3
from datetime import datetime
from time import gmtime, strftime
import glob
import time
import os
import requests
import shutil
dbname = "DATA/"+(time.strftime('%a_%d_%b_%Y_%I_%M_%S_%p_%Z', time.gmtime())+".db")
try:
    shutil.move("DATA/CORONA-19.db", dbname)
except:
    pass
if not os.path.exists('DATA'):
    os.makedirs('DATA')
print (time.strftime('%a_%d_%b_%Y_%I_%M_%S_%p_%Z', time.gmtime())+".html")
filename = "DATA/"+(time.strftime('%a_%d_%b_%Y_%I_%M_%S_%p_%Z', time.gmtime())+".html")
DataIn = open(filename,"w")
listTEXT = []
stringTEXT = ""
response = requests.get('https://mylinuxtoybox.com/COVID-19/index.php')
DATA = str(response.content)
listTEXT.append(DATA)
stringTEXT = stringTEXT+DATA
DataIn.write(str(listTEXT))
DataIn.close()
print(filename)
files = glob.glob('DATA/*.html') # * means format then *.html
File = max(files, key=os.path.getctime)
print ("Opening: ",File)
DataOut = open(File, "r").read()

conn=sqlite3.connect("DATA/CORONA-19.db")
c = conn.cursor()

def Insert(line,c=c,):
    c.execute("CREATE TABLE IF NOT EXISTS CORONA(TEXT UNIQUE)")
    c.execute("INSERT OR IGNORE into CORONA values (?)",(line,))   
    
    
Lines = (str(DataOut).split('style="font-size:2vw">\\\\n'))[1].split('</p>')[0]
lines = Lines.replace("<br />\\\\n","\n")
lines= lines.replace("<br />","\n")
lines = lines.split("\n")
for line in lines:
    if len(line)>5:Insert(line,c=c) 
    
    
conn.commit()
conn.close()


conn=sqlite3.connect("DATA/CORONA-19.db")
c= conn.cursor()
TotalRows=0
for row in c.execute('SELECT rowid,* from CORONA'):
    TotalRows=TotalRows+1
print("TotalRows: ",TotalRows)    
END = TotalRows-5
print("END: ",END) 
cnt=0
for row in c.execute('SELECT rowid,* from CORONA'):
    cnt=cnt+1
    row=str(row).split(",")
    # Print the first and last five entries in the database
    if cnt<=5 or cnt>END:
        print (row[0],row[1],row[2],row[3],row[4],row[5],row[6])
conn.close()

from __future__ import division
import sys
import glob
import time
import os
%matplotlib inline 
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

import sqlite3
from datetime import datetime
from time import gmtime, strftime
import glob
import time
import os
import requests
# If it does not exist, create the path called: DATA .
if not os.path.exists('DATA'):
    os.makedirs('DATA')
# Create a filename to save the scraped html page
filename = "DATA/"+(time.strftime('%a_%d_%b_%Y_%I_%M_%S_%p_%Z', time.gmtime())+".html")
# Print the filename
print(filename)
# Open the filename to write the scraped html data to.
DataIn = open(filename,"w")
# Create an empty list (listTEXT = []) abd an empty string ( stringTEXT = "" )
listTEXT = []
stringTEXT = ""
# Get the data from "https://mylinuxtoybox.com/COVID-19/index.php"
response = requests.get('https://mylinuxtoybox.com/COVID-19/index.php')
# Create DATA from the webpage response
DATA = str(response.content)
listTEXT.append(DATA)
stringTEXT = stringTEXT+DATA
DataIn.write(str(listTEXT))
DataIn.close()

files = glob.glob('DATA/*.html') # * means format then *.html
File = max(files, key=os.path.getctime)
print ("Opening: ",File)
DATAOUT = open(File, "r").read()

print(DATAOUT)

html = str(DataOut).replace("Date,Time,Timestamp","XXXXXXXXDate,Time,Timestamp")
dataout = html.replace("</p>","</p>XXXXXXXX")
dataout = dataout.split("XXXXXXXX")
lines = dataout[2].split("<br />")

cnt=0
for line in lines:
    cnt= cnt+1
    #line=line.lstrip("\\\\n")
    if cnt<5:
        print (line)

DataOut = DATAOUT

DataOut = DATAOUT

html = str(DataOut).replace("Date,Time,Timestamp","XXXXXXXXDate,Time,Timestamp")
dataout = html.replace("</p>","</p>XXXXXXXX")
dataout = dataout.split("XXXXXXXX")
lines = dataout[2].split("<br />")
cnt=0
for line in lines:
    cnt= cnt+1
    line=line.lstrip("\\\\n")
    if cnt<=5:
        print (line)

DataOut = DATAOUT

Lines = (str(DataOut).split('style="font-size:2vw">\\\\n'))[1].split('</p>')[0]
lines = Lines.replace("<br />\\\\n","\n")
lines= lines.replace("<br />","\n")
lines = lines.split("\n")
cnt=0
for line in lines:
    cnt=cnt+1
    if cnt<10:print(line)

# Print GMT
!tz=gmt date -u

!ls DATA

conn=sqlite3.connect("DATA/CORONA-19.db")
c= conn.cursor()
cnt=0
#create empty lists:
ID = []
DATE =[]
TIME =[]
TIMESTAMP =[]
HOURSSINCELASTUPDATE =[]
HOURSSINCELASTUPDATE.append(float(0))
ACCUMULATEDHOURS =[]
ACCUMULATEDHOURS.append(float(0))
acc=0
CASES =[]
DEATHS =[]

for row in c.execute('SELECT rowid,* from CORONA'):
    cnt=cnt+1    
    row=str(row).split(",")
    if cnt==1: print (row[0],row[1],row[2],row[3],row[4],row[5],row[6])
    if cnt==1: print(" ")    
    if cnt==1: print (row[0].lstrip("("),row[1].lstrip(" '"),row[2],row[3],row[4],row[5],row[6].rstrip("')"))   
    if cnt==2: print (row[0],row[1],row[2],row[3],row[4],row[5],row[6])
    if cnt==2: print( '\nTo clean the above data:\nrow[0].lstrip("("),row[1].lstrip(" \'"),row[2],row[3],row[4],row[5],row[6].rstrip("\')")')
    if cnt==2: print(" ")
    if cnt==2: print (row[0].lstrip("("),row[1].lstrip(" '"),row[2],row[3],row[4],row[5],row[6].rstrip("')"))
         
    if cnt>1:
        ID.append(row[0].lstrip("("))
        DATE.append(row[1].lstrip(" '"))
        TIME.append(row[2])
        TIMESTAMP.append(row[3])
        HOURSSINCELASTUPDATE.append(float(row[4]))
        acc=acc+float(row[4])
        ACCUMULATEDHOURS.append(float(acc))
        CASES.append(int(row[5]))
        DEATHS.append(int(row[6].rstrip("')")))
conn.close()

ACCUMULATEDHOURSb=ACCUMULATEDHOURS
HOURSSINCELASTUPDATEb=HOURSSINCELASTUPDATE
ACCUMULATEDHOURSa=ACCUMULATEDHOURSb[:-1]
HOURSSINCELASTUPDATEa=HOURSSINCELASTUPDATEb[:-1]
print(len(ID))
print(len(DATE))
print(len(TIME))
print(len(TIMESTAMP))
print(len(HOURSSINCELASTUPDATEa))
print(len(ACCUMULATEDHOURSa))
print(len(CASES))
print(len(DEATHS))

import numpy as np
#x = np.arange(0, 1, 0.05)
#y = np.power(x, 2)

print(len(ACCUMULATEDHOURSa))
print(len(CASES))
#x = np.array(range(0,len(CASES)),dtype=np.float)
x = np.array(ACCUMULATEDHOURSa,dtype=np.float)
y = np.array(CASES,dtype=np.int)

fig = plt.figure(num=None, figsize=(10,8), dpi=80, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(x, y, s=3)
plt.grid(True)

plt.xlabel('Total hours monitored: '+str(round(ACCUMULATEDHOURSa[-1],2)))
plt.title('Using Confirmed Cases and Timestamp')
plt.ylabel('Number of Cases')
plt.show()

from __future__ import division
import sqlite3
from M2D import Month2Num
import sys
import glob
import time
import os
%matplotlib inline 
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
arrangedDdata = ''
CASESs = []
DEATHs = []
arrangedDdata=arrangedDdata+"date_time,cases\n"
conn=sqlite3.connect("DATA/CORONA-19.db")
c= conn.cursor()
cnt = 0
for rows in c.execute('SELECT * from CORONA'):
    cnt=cnt+1
    row=str(rows)
    row=row.lstrip("(")
    row = row.replace("'","")
    items=row.split(",")
    if cnt<=5 or cnt>=349:
        print(cnt,": ",items[0],items[1],items[2],items[3],items[4],items[5],)

from __future__ import division
import sqlite3
from M2D import Month2Num
import sys
import glob
import time
import os
%matplotlib inline 
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
arrangedDdata = ''
CASESs = []
DEATHs = []
SPANS = []
arrangedDdata=arrangedDdata+"date_time,cases\n"
conn=sqlite3.connect("DATA/CORONA-19.db")
c= conn.cursor()
cnt = 0
for rows in c.execute('SELECT * from CORONA'):
    cnt=cnt+1
    row=str(rows)
    row=row.lstrip("(")
    row = row.replace("'","")
    row=row.split(",")
    # Date,Time,Timestamp,HoursSinceUpdate,ConfirmedCases,Deaths
    if cnt<=2:print(row[0],row[1],row[2],row[3],row[4],row[5])
    #ct==1 is the header
    if cnt>1:
        SPANS.append(row[3])
        CASESs.append(row[4])
        DEATHs.append(row[5])

conn.close() 
count = 0
ACCs = []
acc=0
for accum in SPANS:
    inc =round(float(accum),2)
    acc=acc+inc
    ACCs.append(round(acc,1))
START = CASESs[0]


#3-15-2020 19:00,3329
print ("First Recorded Confirmed Case Count: ",CASESs[0])
print ("Start of Accumulated Time in Days: ",ACCs[1])
print ("Record Keeping Started with",START,"confirmed cases and",DEATHs[0],"Deaths")
print ("Number of Hours Records have been kept:",ACCs[-1])
print ("Current Confirmed Cases: ",CASESs[-1])
print ("Last Death Count: ", DEATHs[-1])
print ("\n-- Debug Info -------------------------------------")
print ("len(SPANS)",len(SPANS))
print ("len(CASESs)",len(CASESs))
print ("len(DEATHS)",len(DEATHs))
print ("len(ACCs)",len(ACCs))
sp = np.array(SPANS,dtype=np.float)
x = np.array(ACCs,dtype=np.float)
y = np.array(CASESs,dtype=np.int)
d = np.array(DEATHs,dtype=np.int)

#fig = plt.figure()
#ax = fig.gca()

#ax.grid(color='lightgray', linestyle='-', linewidth=1)
#ax = fig.gca()
#plt.scatter(x, d, s=3)
fig = plt.figure(num=None, figsize=(12,12), dpi=80, facecolor='salmon')
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(x, y, s=3)



plt.grid(True)

plt.xlabel('Hours: Clock Started '+str(ACCs[-1])+' hours ago.\nMarch/08/2020 23:30:00 with 537 Cases and 21 Deaths', fontsize=14)
plt.title('Horizontal~Accumulated Hours Since Start \n Verticle Number of Confirmed Cases "'+str(CASESs[-1])+'"', fontsize=20)
# Top right 
s0= 'Number of Deaths "'+str(DEATHs[-1])+'"'
V=int(CASESs[-1])
print("V: ",V)
H=int(ACCs[-1]-275)
print("H: ",H)
plt.text(H, V, s0, fontsize=12)

s1= 'Started:\n537 Cases\n21 Deaths'
plt.text(0, 40000, s1, fontsize=12)

s= 'v'
plt.text(-5, 8000, s, fontsize=15)
plt.ylabel('Number of Deaths in the USA', fontsize=22, color="red")
fig.savefig('images/plot-Deaths-002.png', facecolor=fig.get_facecolor(), edgecolor='black')
plt.show()

conn=sqlite3.connect("DATA/CORONA-19.db")
c= conn.cursor()
cnt=0
for row in c.execute('SELECT rowid,* from CORONA'):
    cnt=cnt+1    
    row=str(row).split(",")
    if cnt==1: print (row[0],row[1],row[2],row[3],row[4],row[5],row[6])

print("\nAs of "+row[1].lstrip(" '"),"at",row[2],"there are",row[5],"confirmed cases and",row[6].rstrip("')"), "deaths due to coronavirus COVID-19 in the United States.")


#row[0].lstrip("("),row[1].lstrip(" '"),row[2],row[3],row[4],row[5],row[6].rstrip("')")

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(y=SPANS))
fig.add_trace(go.Bar(y=ACCs))
fig.update_layout(title = 'Fluctuations between data entries in Hours')
fig.show()

print(len(SPANS))
print(len(CASESs))
print(len(DEATHS))
print(len(ACCs))

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(y=SPANS))
fig.add_trace(go.Bar(y=ACCs))
fig.update_layout(title = 'Fluctuations between data entries in Hours')
fig.show()

import plotly.graph_objects as go
from plotly.offline import plot, iplot
import plotly.graph_objs as go
import plotly.offline
plotly.offline.init_notebook_mode(connected=True) 
fig = go.Figure(
    data=[go.Bar(y=CASESs)],
    layout_title_text="Display Confirmed Cases History"
)
fig.show()

import plotly.graph_objects as go
from plotly.offline import plot, iplot
import plotly.graph_objs as go
import plotly.offline
plotly.offline.init_notebook_mode(connected=True) 
fig = go.Figure(
    data=[go.Bar(y=DEATHS)],
    layout_title_text="Display Accumulated Deaths"
)
fig.show()

import plotly.graph_objects as go
from plotly.offline import plot, iplot
import plotly.graph_objs as go
import plotly.offline
plotly.offline.init_notebook_mode(connected=True) 
fig = go.Figure(
    data=[go.Scatter(y=CASESs)],
    layout_title_text="A Figure Displaying"
)
fig.show()

import plotly.graph_objects as go
from plotly.offline import plot, iplot
import plotly.graph_objs as go
import plotly.offline
plotly.offline.init_notebook_mode(connected=True) 
fig = go.Figure(
    data=[go.Bar(y=DEATHS)],
    layout_title_text="A Figure Displayed with fig.show()"
)
fig.show()

import sqlite3
conn=sqlite3.connect("DATA/CORONA-19.db")
c= conn.cursor()
cnt=0
#create empty lists:
ID = []
DATE =[]
TIME =[]
TIMESTAMP =[]
HOURSSINCELASTUPDATE =[]
HOURSSINCELASTUPDATE.append(float(0))
ACCUMULATEDHOURS =[]
ACCUMULATEDHOURS.append(float(0))
acc=0
CASES =[]
DEATHS =[]

for row in c.execute('SELECT rowid,* from CORONA'):
    cnt=cnt+1    
    row=str(row).split(",")
    if cnt==1: print (row[0],row[1],row[2],row[3],row[4],row[5],row[6])
    if cnt==2: print (row[0].lstrip("("),row[1].lstrip(" '"),row[2],row[3],row[4],row[5],row[6].rstrip("')"))
         
    if cnt>1 and len(str(int(row[3])))>5:
        ID.append(row[0].lstrip("("))
        DATE.append(row[1].lstrip(" '"))
        TIME.append(row[2])
        TIMESTAMP.append(row[3])
        HOURSSINCELASTUPDATE.append(float(row[4]))
        acc=acc+float(row[4])
        acc=round(acc,2)
        ACCUMULATEDHOURS.append(float(acc))
        CASES.append(int(row[5]))
        DEATHS.append(int(row[6].rstrip("')")))
conn.close()

#for x in range (0,len(ID)):
End = len(ID)-5   
for x in range (0,End):
    inc=int(ID[x])-1
    print(str(inc)+","+DATE[x]+","+str(TIME[x])+","+str(TIMESTAMP[x])+","+str(HOURSSINCELASTUPDATE[x])+","+str(ACCUMULATEDHOURS[x])+","+str(CASES[x])+","+str(DEATHS[x]))

#for x in range (0,len(ID)):
End = len(ID)
ALL=[]
ALL.append("ID,DATE,TIME,TIMESTAMP,HOURSSINCELASTUPDATE,ACCUMULATEDHOURS,CASES,DEATHS")
for x in range (0,End):
    inc=int(ID[x])-1
    HOURS = str(HOURSSINCELASTUPDATE[x])
    HOURSLAST = str(HOURSSINCELASTUPDATE[x])
    ACCUMULATED= str(ACCUMULATEDHOURS[x])
    print(str(inc)+","+DATE[x]+","+str(TIME[x])+","+str(TIMESTAMP[x])+","+str(HOURSSINCELASTUPDATE[x])+","+str(ACCUMULATEDHOURS[x])+","+str(CASES[x])+","+str(DEATHS[x]))
    if len(TIMESTAMP[x])>5:ALL.append(str(inc)+","+DATE[x]+","+str(TIME[x])+","+str(TIMESTAMP[x])+","+str(HOURSSINCELASTUPDATE[x])+","+str(ACCUMULATEDHOURS[x])+","+str(CASES[x])+","+str(DEATHS[x]))

print(len(ALL))

for line in ALL:
    print (line)

!ls *.html

HARDCOPY = open("ALLdata.html",'w')
for line in ALL:
    HARDCOPY.write(line+"<br />\n")
HARDCOPY.close()    

HARDCOPY = open("ALLdata.txt",'w')
for line in ALL:
    HARDCOPY.write(line+"\n")
HARDCOPY.close()     

HARDOPEN = open("ALLdata.html",'r').readlines()
for line in HARDOPEN:
    print(line)




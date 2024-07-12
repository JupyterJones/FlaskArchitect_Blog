import sqlite3
from datetime import datetime
from time import gmtime, strftime
import glob
import time
import os
import requests
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
for row in c.execute('SELECT rowid,* from CORONA'):
    row=str(row).split(",")
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
DATAOUT = open(File, "r").read()

print(DATAOUT)

DataOut = DATAOUT

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

html = str(DataOut).replace("Date,Time,Timestamp","XXXXXXXXDate,Time,Timestamp")
dataout = html.replace("</p>","</p>XXXXXXXX")
dataout = dataout.split("XXXXXXXX")
lines = dataout[2].split("<br />")
cnt=0
for line in lines:
    cnt= cnt+1
    line=line.lstrip("\\\\n")
    if cnt<5:
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

conn=sqlite3.connect("DATA/CORONA-19.db")
c= conn.cursor()
cnt=0
for row in c.execute('SELECT rowid,* from CORONA'):
    cnt=cnt+1    
    row=str(row).split(",")
    if cnt==1: print (row[0],row[1],row[2],row[3],row[4],row[5],row[6])

print("\nAs of "+row[1].lstrip(" '"),"at",row[2],"there are",row[5],"confirmed cases and",row[6].rstrip("')"), "deaths due to coronavirus COVID-19 in the United States.")


#row[0].lstrip("("),row[1].lstrip(" '"),row[2],row[3],row[4],row[5],row[6].rstrip("')")

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
    print(ID[x],DATE[x],TIME[x],TIMESTAMP[x],HOURSSINCELASTUPDATE[x],ACCUMULATEDHOURS[x],CASES[x],DEATHS[x])

import datetime
import calendar
import time
from M2D import *
import sqlite3
filein = open("all-data.data",'w')
arrangedDdata = ''
arrangedDdata=arrangedDdata+"date_time,cases\n"
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
for row in c.execute('SELECT rowid,* from CORONA'):
    row =str(row)
    row=row.replace(",","")
    row = row.split(" ")
    Month = row[1]
    month = Month2Num(Month[1:])
    OUT = row[2]+"/"+month+"/"+row[3]+" "+row[5]+" "+row[10]+" "+row[14]
    # Result 03/12/2020 03:25:00 1327 38
    arrangedDdata = arrangedDdata+OUT+"\n"
conn.close() 

text =arrangedDdata.split("\n")
text= text[1:-1]
EPOCHa=[]
Scnt=0
acc=0
SPANS = []
for line in text:
    #print(line)
    #line=str(LINE)
    line = line.split(" ")
    #print (str(line[1]+'/'+line[0]+'/'+line[2][:-3]))
    dt = time.strftime(line[0]+' '+line[1])
    
    dt_ti = dt+":00"
    #dt_ti =dt_ti.replace("\n","")
    #print (line)
    #print (dt_ti)
    #03-16-2020 02:48,3777
    pattern = '%d/%m/%Y %H:%M:%S'
    #pattern = '%m/%d/%Y %H:%M:%S'
    #dt_ti = '08/03/2020 23:30:00'
    #print (dt_ti)
    #datetime.strptime('2012-11-14 14:32:30', '%Y-%m-%d %H:%M:%S')
    
    epochs = int(time.mktime(time.strptime(dt_ti, pattern)))
    #print (dt_ti, epochs)
    
    if Scnt>1:SPANS.append(span(int(last),int(epochs)))
    if Scnt==0:last=1583661400  
    SPan = span(int(last),int(epochs)) 
    acc=acc+float(SPan)
    acc_in = round(acc,3)
    data = dt_ti+" "+str(epochs)+" "+str(SPan)+" "+line[2]+" "+line[3]+" "+str(acc_in)
    
    
    entry = str(data)
    Scnt=Scnt+1
    
    last = int(epochs)    
    #print (span(int(last),int(epochs)))
    EPOCHa.append(data)
    
cnt=0    
for lines in EPOCHa:
    cnt=cnt+1
    print (cnt,lines)
    filein.write(lines+"\n")
filein.close()    
#08/03/2020 23:30:00 1583681400 -274.68
#09/03/2020 04:30:00 1583699400 5.0    

import time

dt = time.strftime('%m/%d/%Y-%H:%M:%S')
file = "DATA/"+dt+"CleanCorona.db"
print (file)
!mv DATA/CleanCorona.db, file

conn2=sqlite3.connect("DATA/CleanCorona.db")
c2 = conn2.cursor()
rows = c2.execute("SELECT ROWID,* from CORONA")
for row in rows:
    print (row)

#19429 confirmed cases and 257

.01788*19429

# When working with mortality a history must be involved. 
print ("example: 18876 237")

print (237/18876)
print (237/14366)



print (233/14366)
print (233/14366)

import datetime
import calendar
import time
from M2D import *
import sqlite3
arrangedDdata = ''
DDATA =[]
DDATA.append("Date Time Timestamp SpanBetweenSamples Cases Deaths")
arrangedDdata=arrangedDdata #+"Date, Time, Cases, Deaths, Timestamp, TimeBetweenSamples\n"
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
cnt=0
for row in c.execute('SELECT rowid,* from CORONA'):
    cnt=cnt+1
    row =str(row)
    row=row.replace(",","")
    row = row.split(" ")
    #print (row)
    #print (row[1],row[2],row[3],row[5],row[10],row[14])
    Month = row[1]
    #print (Month[1:])
    month = Month2Num(Month[1:])
    #print (month)
    #if cnt==160:print(row)
    #if cnt==160:print(OUT)               
    OUT = row[2]+"/"+month+"/"+row[3]+" "+row[5]+":00 "+row[10]+" "+row[14]
    # Result 03/12/2020 03:25:00 1327 38
    #print (OUT) 
    arrangedDdata = arrangedDdata+OUT+"\n"
conn.close() 

text =arrangedDdata.split("\n")
#text= text[1:-1]
EPOCHa=[]
Scnt=0
SPANS = []
for line in text:
    if len(line)>5:
        line = line.split(" ")
        #print (line[1],line[2],line[3])
        if len(line)>2:dt = time.strftime(line[0]+' '+line[1])
        #print (dt)

        dt_ti = dt
        #print (dt_ti)
        #03-16-2020 02:48,3777
        pattern = '%d/%m/%Y %H:%M:%S'
        #pattern = '%m/%d/%Y %H:%M:%S'
        epochs = int(time.mktime(time.strptime(dt_ti, pattern)))
        #print (dt_ti, epochs)

        if Scnt>1:SPANS.append(span(int(last),int(epochs)))
        if Scnt==0:last=1583661400 
        SPan = span(int(last),int(epochs)) 

        data = dt_ti+" "+str(epochs)+" "+str(SPan)+" "+line[2]+" "+line[3]
        print (data)
        DDATA.append(data)
        entry = str(data)
        Scnt=Scnt+1
        last = int(epochs)    
        EPOCHa.append(data)


import datetime
import calendar
import time
from M2D import *
# 3,13,2020,03:45,GMT,1747,41
text =arrangedDdata.split("\n")
text= text[1:-1]
print (text)

print("\n--SPANS-",len(SPANS),"---------------------------------------------------------\n")  

import datetime
import calendar
import time
from M2D import *
# 3,13,2020,03:45,GMT,1747,41
text =arrangedDdata.split("\n")
text= text[1:-1]
EPOCHa=[]
Scnt=0
DEATHS = []
ALLdata=[]
EPOCHS = []
SPANS = []
for line in text:
    #print("line",line)
    #line=str(LINE)
    line = line.split(" ")
    CnD = ("split",line[2],line[3])
    #print (str(line[1]+'/'+line[0]+'/'+line[2][:-3]))
    dt = time.strftime(line[0]+' '+line[1])#+' '+line[2][:-3])
    #print ("dt",dt)
    
    dt_ti = dt
    #print (dt_ti)
    #03-16-2020 02:48,3777
    pattern = '%d/%m/%Y %H:%M:%S'
    #pattern = '%m/%d/%Y %H:%M:%S'
    epochs = int(time.mktime(time.strptime(dt_ti, pattern)))
    #print ("dt_ti, epochs",dt_ti, epochs)

    #if Scnt>1:print (dt_ti, epochs)
    if Scnt>1:SPANS.append(span(int(last),int(epochs)))
    if Scnt==0:last=1583661400     
    #print (dt_ti, epochs,span(int(last),int(epochs)),line[2],line[3])
    EPOCHS.append(int(epochs))
    ad = dt_ti, epochs,span(int(last),int(epochs)),line[2],line[3]
    DEATHS.append(line[3])
    AS =str(ad)
    #print ("AS",AS)
    #ALLdata.append(dt_ti+","+str(epochs)+","+str(span(int(last),int(epochs)))+","+str(line[2])+","+str(line[3]))
    ALLdata.append(AS)
    Scnt=Scnt+1
    
    last = int(epochs)    
    #print (span(int(last),int(epochs)))
    EPOCHa.append(str(epochs))
    
print("\n--SPANS-",len(SPANS),"---------------------------------------------------------\n")    
print (SPANS,"\n")
print("\n--ALLdata-",len(ALLdata),"---------------------------------------------------------\n")
print (ALLdata,"\n")
print("\n--EPOCHS-",len(EPOCHS),"---------------------------------------------------------\n")
print (EPOCHS,"\n")

n = ALLdata

print("There are {0} items".format(len(n)))

print("Minimum is {0}".format(min(n)))
print("Maximum is {0}".format(max(n)))

import sqlite3
from M2D import Month2Num
CASES = []
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
for rows in c.execute('SELECT * from CORONA'):
    rows=str(rows)
    row = rows.split(" ")
    print (row[9], end=" ")
    CASES.append(row[9])
conn.close() 
#3-15-2020 19:00,3329
print ("\n",len(CASES))

from __future__ import division
import sys
import glob
import time
import os
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

#%matplotlib inline 
import numpy as np 

E=len(EPOCHa)
print ("Len EPOCHa",E)
Time = np.array(EPOCHa)
print (Time[3:], end=" ")

del CASES[0]
e = len(CASES)
print ("Len LAST",e)
ss = range(0,e)
aa = np.array(CASES)
Ta = np.array(CASES,dtype=np.int)
print(Ta)
s= np.array(CASES)
figure(num=None, figsize=(10,8), dpi=80, facecolor='salmon')
#fig, ax = plt.subplots(dpi=150)


plt.subplot(2, 1, 1)
plt.plot(Time, Ta, 'blue')
plt.title('Using Timestamps')
plt.ylabel('Number of Cases')


plt.subplot(2, 1, 2)
plt.plot(s, Ta, 'red')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

plt.show()



count = 0
ACC = []
acc=0
for accum in SPANS:
    acc=acc+accum
    ACC.append(round(acc,1))


!ls *.py

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(y=SPANS))
#fig.add_trace(go.Bar(y=ACC))
fig.update_layout(title = 'Fluctuations between data entries in Hours')
fig.show()

import plotly.graph_objects as go
from plotly.offline import plot, iplot
import plotly.graph_objs as go
import plotly.offline
plotly.offline.init_notebook_mode(connected=True) 
fig = go.Figure(
    data=[go.Bar(y=CASES)],
    layout_title_text="A Figure Displayed with fig.show()"
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

x=len(ALLdata)
print (ALLdata[x-1])

!ls *.html

html=open("data.html","w")
print ("Date Time Timestamp HoursSinceUpdate ConfirmedCases Deaths")
x=len(ALLdata)
#print (ALLdata[x-1])
html.write("Date,Time,Timestamp,HoursSinceUpdate,ConfirmedCases,Deaths<br />")
for line in ALLdata:
    li = ("".join(line))
    li = li.rstrip("')")
    li = li.lstrip("('")
    li = li.replace("'","")
    li = li.replace(",","")
    li = li.replace(" ",",")
    html.write(li+"<br />\n")
print("----------------------------------------------------------")
print (li)

html.close()    

!update_toybox

print(len(CASES))
print(len(DEATHS))
print(len(ACC))
print(ACC)

from time import gmtime, strftime
import time
print("\nGMT: "+time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()))
print("Local: "+strftime("%a, %d %b %Y %I:%M:%S %p %Z\n"))


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
#del EPOCHa[0]
E=len(EPOCHa)
print ("Len EPOCHa",E)
Time = np.array(EPOCHa)
print (Time[3:], end=" ")
#del HOURS[0]
hours = np.array(ACC)
print("\nLen Hours: ",len(ACC))
print (hours, end=" ")
#del LAST[0]
e = len(CASES)
print ("\nLen LAST",e)
ss = range(0,e)
SS =np.array(ss)
aa = np.array(CASES)
Ta = np.array(CASES,dtype=np.int)
print(Ta)
s= np.array(CASES)
figure(num=None, figsize=(10,8), dpi=80, facecolor='salmon')
#fig, ax = plt.subplots(dpi=150)


hours = np.array(ACC,dtype=np.float)
Ta = np.array(CASES,dtype=np.int)

print(len(ACC))
print(len(CASES))

hours = np.array(ACC,dtype=np.float)
Ta = np.array(CASES,dtype=np.int)

hours = np.array(ACC,dtype=np.float)
Ta = np.array(CASES,dtype=np.int)
minX=min(hours)
maxX=max(hours)
minY=min(Ta)
maxY=max(Ta)
print (minX, maxX, minY, maxY)
#ax.set_xticks(np.arange(minX, 1, maxX))
#ax.set_yticks(np.arange(minY, 1, maxY))

count = 0
ACC = []
acc=0
for accum in SPANS:
    acc=acc+accum
    ACC.append(round(acc,1))
print(SPANS, end=" ")

import sqlite3
from M2D import Month2Num
arrangedDdata = ''
CASESs = []
DEATHs =[]
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
for rows in c.execute('SELECT * from CORONA'):
    rows=str(rows)
    row = rows.split(" ")
    CASESs.append(row[9])
    DEATHs.append(row[13])

exp = "12345678"
print (exp[2:])

import datetime
import calendar
import time
from M2D import *
import sqlite3
arrangedDdata = ''
DDATA =[]
DDATA.append("Date Time Timestamp SpanBetweenSamples Cases Deaths")
arrangedDdata=arrangedDdata #+"Date, Time, Cases, Deaths, Timestamp, TimeBetweenSamples\n"
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
cnt=0
for row in c.execute('SELECT rowid,* from CORONA'):
    cnt=cnt+1
    row =str(row)
    row=row.replace(",","")
    row = row.split(" ")
    #print (row)
    #print (row[1],row[2],row[3],row[5],row[10],row[14])
    Month = row[1]
    #print (Month[1:])
    month = Month2Num(Month[1:])
    #print (month)
    #if cnt==160:print(row)
    #if cnt==160:print(OUT)               
    OUT = row[2]+"/"+month+"/"+row[3]+" "+row[5]+":00 "+row[10]+" "+row[14]
    # Result 03/12/2020 03:25:00 1327 38
    #print (OUT) 
    arrangedDdata = arrangedDdata+OUT+"\n"
conn.close() 

text =arrangedDdata.split("\n")
#text= text[1:-1]
EPOCHa=[]
Scnt=0
SPANS = []
for line in text:
    if len(line)>5:
        line = line.split(" ")
        #print (line[1],line[2],line[3])
        if len(line)>2:dt = time.strftime(line[0]+' '+line[1])
        #print (dt)

        dt_ti = dt
        #print (dt_ti)
        #03-16-2020 02:48,3777
        pattern = '%d/%m/%Y %H:%M:%S'
        #pattern = '%m/%d/%Y %H:%M:%S'
        epochs = int(time.mktime(time.strptime(dt_ti, pattern)))
        #print (dt_ti, epochs)

        if Scnt>1:SPANS.append(span(int(last),int(epochs)))
        if Scnt==0:last=1583661400 
        SPan = span(int(last),int(epochs)) 

        data = dt_ti+" "+str(epochs)+" "+str(SPan)+" "+line[2]+" "+line[3]
        print (data)
        DDATA.append(data)
        entry = str(data)
        Scnt=Scnt+1
        last = int(epochs)    
        EPOCHa.append(data)


import datetime
import calendar
import time
from M2D import *
# 3,13,2020,03:45,GMT,1747,41
text =arrangedDdata.split("\n")
text= text[1:-1]
EPOCHa=[]
Scnt=0
DEATHS = []
ALLdata=[]
EPOCHS = []
SPANS = []
ACCs = []
text =arrangedDdata.split("\n")
text= text[1:-1]
for line in text:
    #print("line",line)
    #line=str(LINE)
    line = line.split(" ")
    CnD = ("split",line[2],line[3])
    #print (str(line[1]+'/'+line[0]+'/'+line[2][:-3]))
    dt = time.strftime(line[0]+' '+line[1])#+' '+line[2][:-3])
    #print ("dt",dt)
    
    dt_ti = dt
    #print (dt_ti)
    #03-16-2020 02:48,3777
    pattern = '%d/%m/%Y %H:%M:%S'
    #pattern = '%m/%d/%Y %H:%M:%S'
    epochs = int(time.mktime(time.strptime(dt_ti, pattern)))
    #print ("dt_ti, epochs",dt_ti, epochs)

    #if Scnt>1:print (dt_ti, epochs)
    if Scnt>1:SPANS.append(span(int(last),int(epochs)))
    if Scnt==0:last=1583661400     
    #print (dt_ti, epochs,span(int(last),int(epochs)),line[2],line[3])
    EPOCHS.append(int(epochs))
    ad = dt_ti, epochs,span(int(last),int(epochs)),line[2],line[3]
    DEATHS.append(line[3])
    AS =str(ad)
    #print ("AS",AS)
    #ALLdata.append(dt_ti+","+str(epochs)+","+str(span(int(last),int(epochs)))+","+str(line[2])+","+str(line[3]))
    ALLdata.append(AS)
    Scnt=Scnt+1
    
    last = int(epochs)    
    #print (span(int(last),int(epochs)))
    EPOCHa.append(str(epochs))
for accum in SPANS:
    acc=acc+accum
    ACCs.append(round(acc,1))    
print("\n--SPANS-",len(SPANS),"---------------------------------------------------------\n")    
print (SPANS,"\n")
print("\n--ALLdata-",len(ALLdata),"---------------------------------------------------------\n")
print (ALLdata,"\n")
print("\n--EPOCHS-",len(EPOCHS),"---------------------------------------------------------\n")
print (EPOCHS,"\n")
print("\n--ACCs-",len(ACCs),"---------------------------------------------------------\n")
print (ACCs,"\n")

print ("len(SPANS)",len(SPANS))
print ("len(ACCs)",len(ACCs))

#3-15-2020 19:00,3329
print ("First Recorded Confirmed Case Count: ",CASESs[0])
print ("Start of Accumulated Time in Hours: ",ACCs[0])
#print ("Record Keeping Started",' '.join(start)+", with",START,"confirmed cases and",DEATHs[0],"Deaths")
print ("Number of Hours Records have been kept:",ACCs[-1])
print ("Current Confirmed Cases: ",CASESs[-1])
print ("Last Death Count: ", DEATHs[-1])
print ("\n-- Debug Info -------------------------------------")
print ("len(CASESs)",len(CASESs))
print ("len(DEATHS)",len(DEATHs))
print ("len(ACCs)",len(ACCs))

import sqlite3
from M2D import Month2Num
arrangedDdata = ''
CASESs = []
DEATHs = []
arrangedDdata=arrangedDdata+"date_time,cases\n"
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
cnt = 0
for rows in c.execute('SELECT * from CORONA'):
    cnt = cnt  +1
    #if cnt==1:print(rows)
    rows=str(rows)
    row = rows.split(" ")
    if cnt==1:print(row[0][2:],row[1],row[2]+":00",row[4],row[9],row[13])
    if cnt==1:start= row[0][2:],row[1],row[2]   
    CASESs.append(row[9])
    DEATHs.append(row[13])
    
conn.close() 
count = 0
ACCs = []
ACCs.append(0)
ACCs.append(0)
ACCs.append(0)
acc=0
for accum in SPANS:
    acc=acc+accum
    ACCs.append(round(acc,1))
START = CASESs[0]


#3-15-2020 19:00,3329
print ("First Recorded Confirmed Case Count: ",CASESs[0])
print ("Start of Accumulated Time in Days: ",ACCs[1])
print ("Record Keeping Started",' '.join(start)+", with",START,"confirmed cases and",DEATHs[0],"Deaths")
print ("Number of Hours Records have been kept:",ACCs[-1])
print ("Current Confirmed Cases: ",CASESs[-1])
print ("Last Death Count: ", DEATHs[-1])
print ("\n-- Debug Info -------------------------------------")
print ("len(CASESs)",len(CASESs))
print ("len(DEATHS)",len(DEATHs))
print ("len(ACCs)",len(ACCs))

cnt = 0
for x in range(0,len(ACCs)-1):
    cnt=cnt+1
    print (cnt,round(ACCs[x]-ACCs[x+1],2))
    
    
print(ACCs[195])    

if not os.path.exists('images'):
    os.makedirs('images')
print ("len(CASESs)",len(CASESs))
print ("len(DEATHS)",len(DEATHs))
print ("len(ACCs)",len(ACCs))


x = np.array(ACCs,dtype=np.float)
y = np.array(CASESs,dtype=np.int)
d = np.array(DEATHs,dtype=np.int)
fig = plt.figure(num=None, figsize=(16,8), dpi=80, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

ax.grid(color='lightgray', linestyle='-', linewidth=1)
#plt.scatter(x, y, s=3)


plt.plot(x, d)
#plt.yscale('log')
#plt.yscale('symlog', linthreshy=0.01)
#plt.scatter(x, d, s=3, color='red')
#plt.scatter(x, y, s=3, color='blue')

plt.title('log')
plt.grid(True)


#plt.grid(True)

plt.xlabel('Time in Hours - Clock Started 03/08/2020 23:30:00 with 537 Cases and 21 Deaths')
plt.title('Accumulated Hours Between Samples')
s1= 'Started:\n1010 Cases\n22.9 Deaths'
plt.text(15, 150, s1, fontsize=12)
s= 'v'
plt.text(15, 60, s, fontsize=15)
plt.ylabel('Number of Deaths in the USA')
fig.savefig('images/plot-Deaths-002.png', facecolor=fig.get_facecolor(), edgecolor='black')
plt.show()

#del CASESs[0]
#del CASESs[0]    
#del CASESs[0]
#del DEATHs[0]
#del DEATHs[0]    
#del DEATHs[0]
print ("len(CASESs)",len(CASESs))
print ("len(DEATHS)",len(DEATHs))
print ("len(ACCs)",len(ACCs))
x = np.array(ACCs,dtype=np.float)
y = np.array(CASESs,dtype=np.int)
d = np.array(DEATHs,dtype=np.int)
fig = plt.figure(num=None, figsize=(10,8), dpi=80, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(x, y, s=3)
#plt.scatter(x, d, s=3, color='red')
plt.grid(True)

plt.xlabel('Time in Hours - Clock Started 03/08/2020 23:30:00 with 537 Cases and 21 Deaths')
plt.title('Accumulated Hours Between Samples')
s1= 'Last: '+CASESs[-1]+' Cases\n           '+DEATHs[-1]+' Deaths'
plt.text(440, 268837, s1, fontsize=12)

s1= 'Started:\n1010 Cases\n22.9 Deaths'
plt.text(12, 8837, s1, fontsize=12)
s= 'v'
plt.text(12, 3200, s, fontsize=14)
plt.ylabel('Number of Cases in the USA')
fig.savefig('images/plot002.png', facecolor=fig.get_facecolor(), edgecolor='black')
plt.show()

# time data '2016 April 01, 2020 06:45AM' does not match format '%Y %H:%M:%S'
import datetime
import time
my = time.strftime("%B %d %Y")
print ("my: ",my)
my_time = time.strftime("%Y %I:%M:%S")
print("my_time: ",my_time)
new_time = datetime.datetime.strptime(my_time, "%Y %H:%M:%S") - datetime.timedelta(hours=20, minutes=0)
print("new_time: ",new_time)
my_time2 = time.strftime("%H:%M:%S")
new_time2 = datetime.datetime.strptime(my_time, "%Y %H:%M:%S") - datetime.timedelta(days=1, hours=20, minutes=0)
print("new_time2: ",new_time2)
#new_time = time.strptime("%B %d", "%Y %H:%M:%S") - datetime.timedelta(hours=10, minutes=0)
print (my,new_time.strftime("%Y %H:%M:%S"))
print (my,new_time2.strftime("%Y %H:%M:%S"))

!date -u +%c

for time in ACC:
    t=5
print(time)  

print (time/24)

import M2D
import sqlite3
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
cnt=0
for row in c.execute('SELECT rowid,* from CORONA'):
    if row[0]==128:print (row)
    cnt=cnt+1
    if row[0]>220:
        data = row[1]
        data = data.replace(",","")
        data = data.split(" ")
        #print (row[0],":",data[1]+"/"+Month2Num(data[0])+""+data[1]+","+data[4]+","+data[9]+","+data[13])
        print (data[1]+"/"+Month2Num(data[0])+"/"+data[1]+","+data[4]+","+data[9]+","+data[13])

360*4
1440/3

import string
cnt=0
ANALYZE =[]
LEN =len(ALLdata)
print (LEN)
for x in range(0,LEN-1):
    if x<10 or x>LEN-10:
        print(ALLdata[x])

STR="09/03/2020 04:30:00 589"
print(STR[:-4])

import string
import time
cnt=0
ANALYZE =[]
LEN =len(ALLdata)

print("--------------- Number of Samples: ",LEN,"----------\n")
print("\n--------------- First Five Samples ---------------")
for line in ALLdata:
    cnt=cnt+1
    line=line.replace(")","")
    line=line.replace("(","")
    line=line.replace("'","")
    line = line.split(",")
    if cnt<=5:print(line[0],line[3],line[4])
    if cnt==5:print("\n--------------- Last Five Samples ---------------")    
    if cnt>LEN-5:print(line[0],line[3],line[4]) 
    if cnt==LEN:print("\n--------------- Last Sample ---------------")
 
    entry = line[0]+","+str(line[3])+","+str(line[4])
    entry = str(entry)
    entry = entry.replace("'","")
    entry = entry.replace(",","")
    ANALYZE.append(entry)
print(entry)

allin = open("ALLdata.data","w")
for line in ALLdata:
    #print(line)
    allin.write(line+"\n")
allin.close()    

import string
cnt=0
ANALYZE =[]
LEN =len(ALLdata)
print ("Number of Samples: ",LEN)
for line in ALLdata:
    cnt=cnt+1
    line=line.replace(")","")
    line=line.replace("'","")
    line = line.split(",")
    if cnt<=5:print(line[3],line[4],end=",")
    if cnt==5:print("\n-----------------------------")    
    if cnt>LEN-5:print(line[3],line[4],end=",") 
    if cnt==LEN:print("\n-----------------------------")    
    ANALYZE.append(str(line[3])+","+str(line[4]))


days=10
hours=5*12 # Samples are two hour intervals
x=0
MORT = []
num = len(ANALYZE)-1
for x in range(130,num):
    AN = (ANALYZE[129-x].split(","))
    AP = (ANALYZE[129-hours-x].split(","))
    if x==130:print("\n-----------------------------\n")
    print (x,"Current Deaths:",AN[1],"    Cases",days,"days ago",AP[0],"    Mortality",int(AN[1])/int(AP[0]))
    MORT.append(int(AN[1])/int(AP[0]))

import plotly.graph_objects as go
from plotly.offline import plot, iplot
import plotly.graph_objs as go
import plotly.offline
plotly.offline.init_notebook_mode(connected=True)
dayz=str(days)
fig = go.Figure(
    data=[go.Bar(y=MORT)],
    layout_title_text="Mortality based on "+dayz+" days span between detection and death"
)
fig.show()

figure(num=None, figsize=(10,8), dpi=80, facecolor='salmon')
#fig, ax = plt.subplots(dpi=150)


#plt.subplot(2, 1, 1)
s=range(0,len(MORT))
plt.plot(s, MORT, 'red')
plt.title('Mortality Using Timestamps')
plt.ylabel('Number of Cases')


figure(num=None, figsize=(10,8), dpi=80, facecolor='salmon')
#fig, ax = plt.subplots(dpi=150)


#plt.subplot(2, 1, 1)
S=range(0,len(MORT))
M= MORT
s = np.asarray(S)
m= np.asarray(M)

plt.plot(S, M, 'red')
plt.plot(s, m, 'blue')
plt.title('Using Timestamps')
plt.ylabel('Number of Cases')


print (len(ANALYZE))

days=5
hours=5*12 # Samples are two hour intervals
AN = (ANALYZE[145].split(","))
AP = (ANALYZE[145-hours].split(","))
print (AN[1],AP[0],CASES[145])
print (int(AN[1])/int(AP[0]))

import string
cnt=0
for line in ALLdata:
    cnt=cnt+1
print(cnt)

line = line.translate({ord(ch):' ' for ch in ",()'"})
line= ' '.join(line.split())
print (line)
line= line.split(" ")
print (line[4],line[5])
#cases=int(line[4])


cases = 19643
#cases = 13865
#cases = 4667

deaths=int(line[5])

percent = deaths/cases
print (percent)
percent*int(line[4])

# 9371*.056 = 524.77
# 13865*.056 = 776.44
# 19393*.056 = 1086.008
# 26111*.053 = 1383.883

68489*.053


54935*percent
#based on 13865: 20/03/2020,00:48:00,1584636480,2.05,13865,211  | 25/03/2020 08:48:00 1585097280 2.02 54935 784
#estimate: April 5th

import M2D
import sqlite3
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
cnt=0
CASES=[]
DEATHS=[]

for row in c.execute('SELECT rowid,* from CORONA'):
    #if row[0]==128:print (row)
    cnt=cnt+1
    data = row[1]
    data = data.replace(",","")
    data = data.split(" ")
    #print (row[0],data[9]+","+data[13])
    CASES.append(data[9])
    DEATHS.append(data[13])

def mortality(DEATHS,CASES):
    result=int(DEATHS)/int(CASES)
    return result

days= 6

span=days*12

length=len(CASES)
for x in range(span,length):
    #print (DEATHS[x],CASES[x-span])
    print (x,DEATHS[x],CASES[x],CASES[x-span],mortality(DEATHS[x],CASES[x-span]))

import plotly.express as px
fig = px.line(x=DEATHS, y=CASES)
fig.show()

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(y=DEATHS))
#fig.add_trace(go.Bar(y=CASES))
fig.update_layout(title = 'DEATHS')
fig.show()

## Offset the deaths and the confirmation by 5 days
#If they die people who get confirmed are ill at least five days

def mort(days,CASES=CASES,DEATHS=DEATHS):
    span=days*12
    start=len(CASES)-1
    num = len(CASES)-span
    for x in range(start,num,-12):
        dates = (int(DEATHS[x]),int(CASES[x-span]))
        mortality = (int(DEATHS[x])/int(CASES[x-span]))
        return dates,mortality

days= 6
mort(days,CASES=CASES,DEATHS=DEATHS)

def RunningMort(days,CASES=CASES,DEATHS=DEATHS):
    span=days*12
    start=len(CASES)-1
    num = len(CASES)-span
    for x in range(start,num,-12):
        print ("DEATHS:", (int(DEATHS[x]),int(CASES[x-span])))
        print ("Mortality:" , (int(DEATHS[x])/int(CASES[x-span])))

days= 7
RunningMort(days,CASES=CASES,DEATHS=DEATHS)

days= 7

span=days*12
num = len(CASES)-span
for x in range(128,num,-12):
    print (int(DEATHS[x]),int(CASES[x-span]))
    print (int(DEATHS[x])/int(CASES[x-span]))

 print (CASES[128])

1036/26111



%%writefile data.csv
Date Time Timestamp HoursSinceUpdate ConfirmedCases Deaths
09/03/2020,04:30:00,1583699400,10.56,589,22
10/03/2020,05:30:00,1583789400,25.0,708,27
10/03/2020,23:35:00,1583854500,18.08,975,30
11/03/2020,04:25:00,1583871900,4.83,1010,31
11/03/2020,15:17:00,1583911020,10.87,1016,31
11/03/2020,23:35:00,1583940900,8.3,1301,38
12/03/2020,03:25:00,1583954700,3.83,1327,38
12/03/2020,11:37:00,1583984220,8.2,1336,38
12/03/2020,22:00:00,1584021600,10.38,1639,40
13/03/2020,00:05:00,1584029100,2.08,1715,41
13/03/2020,01:35:00,1584034500,1.5,1725,41
13/03/2020,03:45:00,1584042300,2.17,1747,41
13/03/2020,06:00:00,1584050400,2.25,1762,41
13/03/2020,15:25:00,1584084300,9.42,1832,41
13/03/2020,22:25:00,1584109500,7.0,2269,48
14/03/2020,02:40:00,1584124800,4.25,2291,50
14/03/2020,07:14:00,1584141240,4.57,2319,50
14/03/2020,16:45:00,1584175500,9.52,2499,51
14/03/2020,23:03:00,1584198180,6.3,2836,57
15/03/2020,05:00:00,1584219600,5.95,2982,60
15/03/2020,05:40:00,1584222000,0.67,2995,60
15/03/2020,07:05:00,1584227100,1.42,3043,60
15/03/2020,19:00:00,1584270000,11.92,3329,63
15/03/2020,20:05:00,1584273900,1.08,3400,63
15/03/2020,21:15:00,1584278100,1.17,3621,63
15/03/2020,22:15:00,1584281700,1.0,3502,63
16/03/2020,00:35:00,1584290100,2.33,3714,68
16/03/2020,02:48:00,1584298080,2.22,3777,69
16/03/2020,05:36:00,1584308160,2.8,3782,69
16/03/2020,08:29:00,1584318540,2.88,3802,69
16/03/2020,18:40:00,1584355200,10.18,4186,73
16/03/2020,22:40:00,1584369600,4.0,4597,86
17/03/2020,00:45:00,1584377100,2.08,4667,87
17/03/2020,02:40:00,1584384000,1.92,4704,91
17/03/2020,06:35:00,1584398100,3.92,4727,93
17/03/2020,10:31:00,1584412260,3.93,4743,93
17/03/2020,14:38:00,1584427080,4.12,4752,93
17/03/2020,18:41:00,1584441660,4.05,5723,97
17/03/2020,21:55:00,1584453300,3.23,6211,102
17/03/2020,22:40:00,1584456000,0.75,6349,106
18/03/2020,02:20:00,1584469200,3.67,6499,112
18/03/2020,06:05:00,1584482700,3.75,6522,116
18/03/2020,10:10:00,1584497400,4.08,6524,116
18/03/2020,16:15:00,1584519300,6.08,7601,116
18/03/2020,18:16:00,1584526560,2.02,7708,120
18/03/2020,20:21:00,1584534060,2.08,8710,132
18/03/2020,22:10:00,1584540600,1.82,8998,150
19/03/2020,02:17:00,1584555420,4.12,9371,153
19/03/2020,10:16:00,1584584160,7.98,9464,155
19/03/2020,12:18:00,1584591480,2.03,9473,155
19/03/2020,14:15:00,1584598500,1.95,9486,157
19/03/2020,16:22:00,1584606120,2.12,10692,160
19/03/2020,18:17:00,1584613020,1.92,11355,171
19/03/2020,22:45:00,1584629100,4.47,13737,201
20/03/2020,00:48:00,1584636480,2.05,13865,211
20/03/2020,02:40:00,1584643200,1.87,14316,218
20/03/2020,04:34:00,1584650040,1.9,14336,218
20/03/2020,06:35:00,1584657300,2.02,14366,217
20/03/2020,08:10:00,1584663000,1.58,14366,217
20/03/2020,10:11:00,1584670260,2.02,14366,217
20/03/2020,12:11:00,1584677460,2.0,14366,217
20/03/2020,14:10:00,1584684600,1.98,14373,218
20/03/2020,16:11:00,1584691860,2.02,16067,219
20/03/2020,18:12:00,1584699120,2.02,16545,225
20/03/2020,20:12:00,1584706320,2.0,18121,233
20/03/2020,22:12:00,1584713520,2.0,18876,237
21/03/2020,00:06:00,1584720360,1.9,19393,256
21/03/2020,02:07:00,1584727620,2.02,19643,263
21/03/2020,04:08:00,1584734880,2.02,19652,264
21/03/2020,06:05:00,1584741900,1.95,19774,275
21/03/2020,08:10:00,1584749400,2.08,19774,275
21/03/2020,10:12:00,1584756720,2.03,19774,275
21/03/2020,12:46:00,1584765960,2.57,19775,276
21/03/2020,14:48:00,1584773280,2.03,19823,276
21/03/2020,16:48:00,1584780480,2.0,22085,282
21/03/2020,18:45:00,1584787500,1.95,22813,288
21/03/2020,20:45:00,1584794700,2.0,24142,288
21/03/2020,22:45:00,1584801900,2.0,23940,301
22/03/2020,00:40:00,1584808800,1.92,26111,324
22/03/2020,02:40:00,1584816000,2.0,26711,341
22/03/2020,04:45:00,1584823500,2.08,26867,348
22/03/2020,06:30:00,1584829800,1.75,26892,348
22/03/2020,08:45:00,1584837900,2.25,26892,348
22/03/2020,10:45:00,1584845100,2.0,26900,348
22/03/2020,12:48:00,1584852480,2.05,26905,348
22/03/2020,14:45:00,1584859500,1.95,27031,349
22/03/2020,16:42:00,1584866520,1.95,30239,388
22/03/2020,18:48:00,1584874080,2.1,38757,400
22/03/2020,20:44:00,1584881040,1.93,32356,414
22/03/2020,21:41:00,1584884460,0.95,32356,414
23/03/2020,00:44:00,1584895440,3.05,33346,414
23/03/2020,02:37:00,1584902220,1.88,33546,419
23/03/2020,03:55:00,1584906900,1.3,34717,452
23/03/2020,06:45:00,1584917100,2.83,35060,457
23/03/2020,08:47:00,1584924420,2.03,35070,458
23/03/2020,10:47:00,1584931620,2.0,35070,458
23/03/2020,12:46:00,1584938760,1.98,35075,458
23/03/2020,14:45:00,1584945900,1.98,35179,459
23/03/2020,16:45:00,1584953100,2.0,40773,479
23/03/2020,18:46:00,1584960360,2.02,41569,504
23/03/2020,20:47:00,1584967620,2.02,42443,517
23/03/2020,22:31:00,1584973860,1.73,43449,545
24/03/2020,00:47:00,1584982020,2.27,43718,552
24/03/2020,02:33:00,1584988380,1.77,43734,553
24/03/2020,04:46:00,1584996360,2.22,46145,582
24/03/2020,06:43:00,1585003380,1.95,46145,582
24/03/2020,08:48:00,1585010880,2.08,46145,582
24/03/2020,10:47:00,1585018020,1.98,46168,582
24/03/2020,12:47:00,1585025220,2.0,46168,582
24/03/2020,14:47:00,1585032420,2.0,46274,588
24/03/2020,16:47:00,1585039620,2.0,49594,622
24/03/2020,18:45:00,1585046700,1.97,50982,655
24/03/2020,20:42:00,1585053720,1.95,52921,684
24/03/2020,22:48:00,1585061280,2.1,53205,687
25/03/2020,00:29:00,1585067340,1.68,53655,698
25/03/2020,02:44:00,1585075440,2.25,54823,778
25/03/2020,04:46:00,1585082760,2.03,54867,782
25/03/2020,06:47:00,1585090020,2.02,54916,784
25/03/2020,08:48:00,1585097280,2.02,54935,784
25/03/2020,10:43:00,1585104180,1.92,54941,784
25/03/2020,12:48:00,1585111680,2.08,54979,785
25/03/2020,14:48:00,1585118880,2.0,55081,785
25/03/2020,16:48:00,1585126080,2.0,60642,817
25/03/2020,18:48:00,1585133280,2.0,62364,878
25/03/2020,20:33:00,1585139580,1.75,64765,910
25/03/2020,22:44:00,1585147440,2.18,65527,928
26/03/2020,00:34:00,1585154040,1.83,65797,935
26/03/2020,02:43:00,1585161780,2.15,66741,963
26/03/2020,05:24:00,1585171440,2.68,68472,1032
26/03/2020,07:03:00,1585177380,1.65,68489,1032
26/03/2020,09:02:00,1585184520,1.98,68489,1032
26/03/2020,11:02:00,1585191720,2.0,68581,1036
26/03/2020,13:01:00,1585198860,1.98,68594,1036
26/03/2020,14:52:00,1585205520,1.85,68905,1037
26/03/2020,17:02:00,1585213320,2.17,75069,1080
26/03/2020,19:00:00,1585220400,1.97,79082,1143
26/03/2020,21:01:00,1585227660,2.02,81946,1177
26/03/2020,23:02:00,1585234920,2.02,83206,1201
27/03/2020,01:00:00,1585242000,1.97,85280,1293
27/03/2020,03:01:00,1585249260,2.02,85520,1297
27/03/2020,04:36:00,1585254960,1.58,85594,1300
27/03/2020,07:33:00,1585265580,2.95,85612,1301
27/03/2020,09:32:00,1585272720,1.98,85612,1301
27/03/2020,11:31:00,1585279860,1.98,85749,1304
27/03/2020,13:32:00,1585287120,2.02,85755,1304
27/03/2020,15:33:00,1585294380,2.02,86548,1321
27/03/2020,17:32:00,1585301520,1.98,94425,1429
27/03/2020,19:33:00,1585308780,2.02,98180,1513
27/03/2020,21:33:00,1585315980,2.0,100514,1546
27/03/2020,23:33:00,1585323180,2.0,102325,1591
28/03/2020,01:32:00,1585330320,1.98,104126,1692
28/03/2020,03:34:00,1585337640,2.03,104205,1704
28/03/2020,05:35:00,1585344900,2.02,104205,1704
28/03/2020,07:35:00,1585352100,2.0,104256,1704
28/03/2020,09:35:00,1585359300,2.0,104256,1704
28/03/2020,11:40:00,1585366800,2.08,104256,1704
28/03/2020,13:36:00,1585373760,1.93,104277,1704
28/03/2020,15:45:00,1585381500,2.15,105726,1730
28/03/2020,17:45:00,1585388700,2.0,116050,1937
28/03/2020,19:43:00,1585395780,1.97,118592,1979
28/03/2020,21:44:00,1585403040,2.02,120204,1997
28/03/2020,23:43:00,1585410180,1.98,123311,2211
29/03/2020,01:46:00,1585417560,2.05,123578,2221
29/03/2020,03:46:00,1585424760,2.0,123750,2227
29/03/2020,05:48:00,1585432080,2.03,123774,2228
29/03/2020,07:41:00,1585438860,1.88,123776,2229
29/03/2020,09:45:00,1585446300,2.07,123781,2229
29/03/2020,11:44:00,1585453440,1.98,123781,2229
29/03/2020,13:46:00,1585460760,2.03,123828,2229
29/03/2020,15:47:00,1585468020,2.02,125099,2238
29/03/2020,17:49:00,1585475340,2.03,133146,2363
29/03/2020,19:47:00,1585482420,1.97,137943,2431
29/03/2020,21:48:00,1585489680,2.02,139904,2449
29/03/2020,23:49:00,1585496940,2.02,141781,2471
30/03/2020,01:44:00,1585503840,1.92,142004,2484
30/03/2020,03:46:00,1585511160,2.03,142735,2488
30/03/2020,06:46:00,1585521960,3.0,142735,2488
30/03/2020,08:50:00,1585529400,2.07,142735,2489
30/03/2020,10:50:00,1585536600,2.0,142746,2489
30/03/2020,12:50:00,1585543800,2.0,142793,2490
30/03/2020,14:50:00,1585551000,2.0,144410,2600
30/03/2020,16:50:00,1585558200,2.0,145542,2616
30/03/2020,18:50:00,1585565400,2.0,156565,2870
30/03/2020,20:50:00,1585572600,2.0,159689,2951
30/03/2020,22:50:00,1585579800,2.0,161358,2974
31/03/2020,00:50:00,1585587000,2.0,163479,3148
31/03/2020,02:50:00,1585594200,2.0,164253,3165
31/03/2020,04:50:00,1585601400,2.0,164253,3167
31/03/2020,06:50:00,1585608600,2.0,164323,3170
31/03/2020,08:42:00,1585615320,1.87,164359,3173
31/03/2020,10:49:00,1585622940,2.12,164359,3173
31/03/2020,12:49:00,1585630140,2.0,164435,3175
31/03/2020,14:49:00,1585637340,2.0,165392,3182
31/03/2020,16:49:00,1585644540,2.0,175669,3424
31/03/2020,18:49:00,1585651740,2.0,180340,3573
31/03/2020,20:49:00,1585658940,2.0,186046,3807
31/03/2020,22:49:00,1585666140,2.0,187729,3867
01/04/2020,02:49:00,1585680540,4.0,188530,3889
01/04/2020,04:49:00,1585687740,2.0,188578,4054
01/04/2020,06:49:00,1585694940,2.0,188592,4055
01/04/2020,08:49:00,1585702140,2.0,188592,4056
01/04/2020,10:49:00,1585709340,2.0,188639,4059
01/04/2020,12:49:00,1585716540,2.0,188647,4059
01/04/2020,14:49:00,1585723740,2.0,189711,4099
01/04/2020,16:49:00,1585730940,2.0,200289,4394
01/04/2020,18:49:00,1585738140,2.0,205438,4528
01/04/2020,20:49:00,1585745340,2.0,211143,4713
01/04/2020,22:49:00,1585752540,2.0,212980,4759
02/04/2020,00:49:00,1585759740,2.0,215003,5102
02/04/2020,02:49:00,1585766940,2.0,215175,5110
02/04/2020,04:49:00,1585774140,2.0,215300,5110
02/04/2020,06:49:00,1585781340,2.0,215324,5112
02/04/2020,08:49:00,1585788540,2.0,215344,5112
02/04/2020,10:49:00,1585795740,2.0,215344,5112
02/04/2020,12:49:00,1585802940,2.0,216722,5140
02/04/2020,14:49:00,1585810140,2.0,219832,5227
02/04/2020,16:49:00,1585817340,2.0,222658,5356
02/04/2020,18:49:00,1585824540,2.0,232899,5665
02/04/2020,20:49:00,1585831740,2.0,243298,5883
02/04/2020,22:19:00,1585837140,1.5,244230,5883
03/04/2020,01:20:00,1585848000,3.02,244877,6070
03/04/2020,01:36:00,1585848960,0.27,245066,6075
03/04/2020,03:20:00,1585855200,1.73,245088,6075
03/04/2020,05:20:00,1585862400,2.0,245341,6095
03/04/2020,07:20:00,1585869600,2.0,245373,6095
03/04/2020,09:20:00,1585876800,2.0,245373,6095
03/04/2020,11:20:00,1585884000,2.0,245380,6095
03/04/2020,13:20:00,1585891200,2.0,245442,6098
03/04/2020,14:49:00,1585896540,1.48,245442,6099
03/04/2020,16:49:00,1585903740,2.0,259750,6603
03/04/2020,18:49:00,1585910940,2.0,266279,6803
03/04/2020,20:49:00,1585918140,2.0,272614,6988 
03/04/2020,22:49:00,1585925340,2.0,275802,7087
04/04/2020,00:49:00,1585932540,2.0,276965,7391
04/04/2020,02:49:00,1585939740,2.0,277161,7392
04/04/2020,04:49:00,1585946940,2.0,277475,7402
04/04/2020,06:49:00,1585954140,2.0,277522,7403
04/04/2020,08:49:00,1585961340,2.0,277522,7403
04/04/2020,10:49:00,1585968540,2.0,277522,7403
04/04/2020,12:49:00,1585975740,2.0,277607,7406 
04/04/2020,14:49:00,1585982940,2.0,279500,7457
04/04/2020,16:49:00,1585990140,2.0,293494,7896
04/04/2020,18:49:00,1585997340,2.0,301147,8173
04/04/2020,20:49:00,1586004540,2.0,306768,8347
04/04/2020,22:49:00,1586011740,2.0,308644,8401
05/04/2020,00:49:00,1586018940,2.0,311357,8452        

print ("Date Time Timestamp HoursSinceUpdate ConfirmedCases Deaths")
x=len(ALLdata)
print (x)
cnt=0
for line in ALLdata:
    cnt=cnt+1
    li = ("".join(line))
    li = li.rstrip("')")
    li = li.lstrip("('")
    li = li.replace("'","")
    li = li.replace(",","")
    li = li.replace(" ",",")
    if cnt>240:print (li)

print ("Date Time Timestamp HoursSinceUpdate ConfirmedCases Deaths")
x=len(ALLdata)
cnt=0
for line in ALLdata:
    cnt=cnt+1
    li = ("".join(line))
    li = li.rstrip("')")
    li = li.lstrip("('")
    li = li.replace("'","")
    li = li.replace(",","")
    li = li.replace(" ",",")
    if cnt>243:print (li)   
  

!update_toybox

DATA ="""March 08, 2020 at 23:30 GMT, there have been 537 confirmed cases and 21 deaths due to coronavirus COVID-19 in the United States.
March 09, 2020 at 04:30 GMT, there have been 589 confirmed cases and 22 deaths due to coronavirus COVID-19 in the United States.
March 10, 2020 at 05:30 GMT, there have been 708 confirmed cases and 27 deaths due to coronavirus COVID-19 in the United States.
March 10, 2020 at 23:35 GMT, there have been 975 confirmed cases and 30 deaths due to coronavirus COVID-19 in the United States.
March 11, 2020 at 04:25 GMT, there have been 1010 confirmed cases and 31 deaths due to coronavirus COVID-19 in the United States.
March 11, 2020 at 15:17 GMT, there have been 1016 confirmed cases and 31 deaths due to coronavirus COVID-19 in the United States.
March 11, 2020 at 23:35 GMT, there have been 1301 confirmed cases and 38 deaths due to coronavirus COVID-19 in the United States.
March 12, 2020 at 03:25 GMT, there have been 1327 confirmed cases and 38 deaths due to coronavirus COVID-19 in the United States.
March 12, 2020 at 11:37 GMT, there have been 1336 confirmed cases and 38 deaths due to coronavirus COVID-19 in the United States.
March 12, 2020 at 22:00 GMT, there have been 1639 confirmed cases and 40 deaths due to coronavirus COVID-19 in the United States.
March 13, 2020 at 00:05 GMT, there have been 1715 confirmed cases and 41 deaths due to coronavirus COVID-19 in the United States.
March 13, 2020 at 01:35 GMT, there have been 1725 confirmed cases and 41 deaths due to coronavirus COVID-19 in the United States.
March 13, 2020 at 03:45 GMT, there have been 1747 confirmed cases and 41 deaths due to coronavirus COVID-19 in the United States.
March 13, 2020 at 06:00 GMT, there have been 1762 confirmed cases and 41 deaths due to coronavirus COVID-19 in the United States.
March 13, 2020 at 15:25 GMT, there have been 1832 confirmed cases and 41 deaths due to coronavirus COVID-19 in the United States.
March 13, 2020 at 22:25 GMT, there have been 2269 confirmed cases and 48 deaths due to coronavirus COVID-19 in the United States.
March 14, 2020 at 02:40 GMT, there have been 2291 confirmed cases and 50 deaths due to coronavirus COVID-19 in the United States.
March 14, 2020 at 07:14 GMT, there have been 2319 confirmed cases and 50 deaths due to coronavirus COVID-19 in the United States.
March 14, 2020 at 16:45 GMT, there have been 2499 confirmed cases and 51 deaths due to coronavirus COVID-19 in the United States.
March 14, 2020 at 23:03 GMT, there have been 2836 confirmed cases and 57 deaths due to coronavirus COVID-19 in the United States.
March 15, 2020 at 05:00 GMT, there have been 2982 confirmed cases and 60 deaths due to coronavirus COVID-19 in the United States.
March 15, 2020 at 05:40 GMT, there have been 2995 confirmed cases and 60 deaths due to coronavirus COVID-19 in the United States.
March 15, 2020 at 07:05 GMT, there have been 3043 confirmed cases and 60 deaths due to coronavirus COVID-19 in the United States.
March 15, 2020 at 19:00 GMT, there have been 3329 confirmed cases and 63 deaths due to coronavirus COVID-19 in the United States.
March 15, 2020 at 20:05 GMT, there have been 3400 confirmed cases and 63 deaths due to coronavirus COVID-19 in the United States.
March 15, 2020 at 21:15 GMT, there have been 3621 confirmed cases and 63 deaths due to coronavirus COVID-19 in the United States.
March 15, 2020 at 22:15 GMT, there have been 3502 confirmed cases and 63 deaths due to coronavirus COVID-19 in the United States.
March 16, 2020 at 00:35 GMT, there have been 3714 confirmed cases and 68 deaths due to coronavirus COVID-19 in the United States.
March 16, 2020 at 02:48 GMT, there have been 3777 confirmed cases and 69 deaths due to coronavirus COVID-19 in the United States.
March 16, 2020 at 05:36 GMT, there have been 3782 confirmed cases and 69 deaths due to coronavirus COVID-19 in the United States.
March 16, 2020 at 08:29 GMT, there have been 3802 confirmed cases and 69 deaths due to coronavirus COVID-19 in the United States.
March 16, 2020 at 18:40 GMT, there have been 4186 confirmed cases and 73 deaths due to coronavirus COVID-19 in the United States.
March 16, 2020 at 22:40 GMT, there have been 4597 confirmed cases and 86 deaths due to coronavirus COVID-19 in the United States.
March 17, 2020 at 00:45 GMT, there have been 4667 confirmed cases and 87 deaths due to coronavirus COVID-19 in the United States.
March 17, 2020 at 02:40 GMT, there have been 4704 confirmed cases and 91 deaths due to coronavirus COVID-19 in the United States.
March 17, 2020 at 06:35 GMT, there have been 4727 confirmed cases and 93 deaths due to coronavirus COVID-19 in the United States.
March 17, 2020 at 10:31 GMT, there have been 4743 confirmed cases and 93 deaths due to coronavirus COVID-19 in the United States.
March 17, 2020 at 14:38 GMT, there have been 4752 confirmed cases and 93 deaths due to coronavirus COVID-19 in the United States.
March 17, 2020 at 18:41 GMT, there have been 5723 confirmed cases and 97 deaths due to coronavirus COVID-19 in the United States.
March 17, 2020 at 21:55 GMT, there have been 6211 confirmed cases and 102 deaths due to coronavirus COVID-19 in the United States.
March 17, 2020 at 22:40 GMT, there have been 6349 confirmed cases and 106 deaths due to coronavirus COVID-19 in the United States.
March 18, 2020 at 02:20 GMT, there have been 6499 confirmed cases and 112 deaths due to coronavirus COVID-19 in the United States.
March 18, 2020 at 06:05 GMT, there have been 6522 confirmed cases and 116 deaths due to coronavirus COVID-19 in the United States.
March 18, 2020 at 10:10 GMT, there have been 6524 confirmed cases and 116 deaths due to coronavirus COVID-19 in the United States.
March 18, 2020 at 16:15 GMT, there have been 7601 confirmed cases and 116 deaths due to coronavirus COVID-19 in the United States.
March 18, 2020 at 18:16 GMT, there have been 7708 confirmed cases and 120 deaths due to coronavirus COVID-19 in the United States.
March 18, 2020 at 20:21 GMT, there have been 8710 confirmed cases and 132 deaths due to coronavirus COVID-19 in the United States.
March 18, 2020 at 22:10 GMT, there have been 8998 confirmed cases and 150 deaths due to coronavirus COVID-19 in the United States.
March 19, 2020 at 02:17 GMT, there have been 9371 confirmed cases and 153 deaths due to coronavirus COVID-19 in the United States.
March 19, 2020 at 10:16 GMT, there have been 9464 confirmed cases and 155 deaths due to coronavirus COVID-19 in the United States.
March 19, 2020 at 12:18 GMT, there have been 9473 confirmed cases and 155 deaths due to coronavirus COVID-19 in the United States.
March 19, 2020 at 14:15 GMT, there have been 9486 confirmed cases and 157 deaths due to coronavirus COVID-19 in the United States.
March 19, 2020 at 16:22 GMT, there have been 10692 confirmed cases and 160 deaths due to coronavirus COVID-19 in the United States.
March 19, 2020 at 18:17 GMT, there have been 11355 confirmed cases and 171 deaths due to coronavirus COVID-19 in the United States.
March 19, 2020 at 22:45 GMT, there have been 13737 confirmed cases and 201 deaths due to coronavirus COVID-19 in the United States.
March 20, 2020 at 00:48 GMT, there have been 13865 confirmed cases and 211 deaths due to coronavirus COVID-19 in the United States.
March 20, 2020 at 02:40 GMT, there have been 14316 confirmed cases and 218 deaths due to coronavirus COVID-19 in the United States.
March 20, 2020 at 04:34 GMT, there have been 14336 confirmed cases and 218 deaths due to coronavirus COVID-19 in the United States.
March 20, 2020 at 06:35 GMT, there have been 14366 confirmed cases and 217 deaths due to coronavirus COVID-19 in the United States.
March 20, 2020 at 08:10 GMT, there have been 14366 confirmed cases and 217 deaths due to coronavirus COVID-19 in the United States.
March 20, 2020 at 10:11 GMT, there have been 14366 confirmed cases and 217 deaths due to coronavirus COVID-19 in the United States.
March 20, 2020 at 12:11 GMT, there have been 14366 confirmed cases and 217 deaths due to coronavirus COVID-19 in the United States.
March 20, 2020 at 14:10 GMT, there have been 14373 confirmed cases and 218 deaths due to coronavirus COVID-19 in the United States.
March 20, 2020 at 16:11 GMT, there have been 16067 confirmed cases and 219 deaths due to coronavirus COVID-19 in the United States.
March 20, 2020 at 18:12 GMT, there have been 16545 confirmed cases and 225 deaths due to coronavirus COVID-19 in the United States.
March 20, 2020 at 20:12 GMT, there have been 18121 confirmed cases and 233 deaths due to coronavirus COVID-19 in the United States.
March 20, 2020 at 22:12 GMT, there have been 18876 confirmed cases and 237 deaths due to coronavirus COVID-19 in the United States.
March 21, 2020 at 00:06 GMT, there have been 19393 confirmed cases and 256 deaths due to coronavirus COVID-19 in the United States.
March 21, 2020 at 02:07 GMT, there have been 19643 confirmed cases and 263 deaths due to coronavirus COVID-19 in the United States.
March 21, 2020 at 04:08 GMT, there have been 19652 confirmed cases and 264 deaths due to coronavirus COVID-19 in the United States.
March 21, 2020 at 06:05 GMT, there have been 19774 confirmed cases and 275 deaths due to coronavirus COVID-19 in the United States.
March 21, 2020 at 08:10 GMT, there have been 19774 confirmed cases and 275 deaths due to coronavirus COVID-19 in the United States.
March 21, 2020 at 10:12 GMT, there have been 19774 confirmed cases and 275 deaths due to coronavirus COVID-19 in the United States.
March 21, 2020 at 12:46 GMT, there have been 19775 confirmed cases and 276 deaths due to coronavirus COVID-19 in the United States.
March 21, 2020 at 14:48 GMT, there have been 19823 confirmed cases and 276 deaths due to coronavirus COVID-19 in the United States.
March 21, 2020 at 16:48 GMT, there have been 22085 confirmed cases and 282 deaths due to coronavirus COVID-19 in the United States.
March 21, 2020 at 18:45 GMT, there have been 22813 confirmed cases and 288 deaths due to coronavirus COVID-19 in the United States.
March 21, 2020 at 20:45 GMT, there have been 24142 confirmed cases and 288 deaths due to coronavirus COVID-19 in the United States.
March 21, 2020 at 22:45 GMT, there have been 23940 confirmed cases and 301 deaths due to coronavirus COVID-19 in the United States.
March 22, 2020 at 00:40 GMT, there have been 26111 confirmed cases and 324 deaths due to coronavirus COVID-19 in the United States.
March 22, 2020 at 02:40 GMT, there have been 26711 confirmed cases and 341 deaths due to coronavirus COVID-19 in the United States.
March 22, 2020 at 04:45 GMT, there have been 26867 confirmed cases and 348 deaths due to coronavirus COVID-19 in the United States.
March 22, 2020 at 06:30 GMT, there have been 26892 confirmed cases and 348 deaths due to coronavirus COVID-19 in the United States.
March 22, 2020 at 08:45 GMT, there have been 26892 confirmed cases and 348 deaths due to coronavirus COVID-19 in the United States.
March 22, 2020 at 10:45 GMT, there have been 26900 confirmed cases and 348 deaths due to coronavirus COVID-19 in the United States.
March 22, 2020 at 12:48 GMT, there have been 26905 confirmed cases and 348 deaths due to coronavirus COVID-19 in the United States.
March 22, 2020 at 14:45 GMT, there have been 27031 confirmed cases and 349 deaths due to coronavirus COVID-19 in the United States.
March 22, 2020 at 16:42 GMT, there have been 30239 confirmed cases and 388 deaths due to coronavirus COVID-19 in the United States.
March 22, 2020 at 18:48 GMT, there have been 38757 confirmed cases and 400 deaths due to coronavirus COVID-19 in the United States.
March 22, 2020 at 20:44 GMT, there have been 32356 confirmed cases and 414 deaths due to coronavirus COVID-19 in the United States.
March 22, 2020 at 21:41 GMT, there have been 32356 confirmed cases and 414 deaths due to coronavirus COVID-19 in the United States.
March 23, 2020 at 00:44 GMT, there have been 33346 confirmed cases and 414 deaths due to coronavirus COVID-19 in the United States.
March 23, 2020 at 02:37 GMT, there have been 33546 confirmed cases and 419 deaths due to coronavirus COVID-19 in the United States.
March 23, 2020 at 03:55 GMT, there have been 34717 confirmed cases and 452 deaths due to coronavirus COVID-19 in the United States.
March 23, 2020 at 06:45 GMT, there have been 35060 confirmed cases and 457 deaths due to coronavirus COVID-19 in the United States.
March 23, 2020 at 08:47 GMT, there have been 35070 confirmed cases and 458 deaths due to coronavirus COVID-19 in the United States.
March 23, 2020 at 10:47 GMT, there have been 35070 confirmed cases and 458 deaths due to coronavirus COVID-19 in the United States.
March 23, 2020 at 12:46 GMT, there have been 35075 confirmed cases and 458 deaths due to coronavirus COVID-19 in the United States.
March 23, 2020 at 14:45 GMT, there have been 35179 confirmed cases and 459 deaths due to coronavirus COVID-19 in the United States.
March 23, 2020 at 16:45 GMT, there have been 40773 confirmed cases and 479 deaths due to coronavirus COVID-19 in the United States.
March 23, 2020 at 18:46 GMT, there have been 41569 confirmed cases and 504 deaths due to coronavirus COVID-19 in the United States.
March 23, 2020 at 20:47 GMT, there have been 42443 confirmed cases and 517 deaths due to coronavirus COVID-19 in the United States.
March 23, 2020 at 22:31 GMT, there have been 43449 confirmed cases and 545 deaths due to coronavirus COVID-19 in the United States.
March 24, 2020 at 00:47 GMT, there have been 43718 confirmed cases and 552 deaths due to coronavirus COVID-19 in the United States.
March 24, 2020 at 02:33 GMT, there have been 43734 confirmed cases and 553 deaths due to coronavirus COVID-19 in the United States.
March 24, 2020 at 04:46 GMT, there have been 46145 confirmed cases and 582 deaths due to coronavirus COVID-19 in the United States.
March 24, 2020 at 06:43 GMT, there have been 46145 confirmed cases and 582 deaths due to coronavirus COVID-19 in the United States.
March 24, 2020 at 08:48 GMT, there have been 46145 confirmed cases and 582 deaths due to coronavirus COVID-19 in the United States.
March 24, 2020 at 10:47 GMT, there have been 46168 confirmed cases and 582 deaths due to coronavirus COVID-19 in the United States.
March 24, 2020 at 12:47 GMT, there have been 46168 confirmed cases and 582 deaths due to coronavirus COVID-19 in the United States.
March 24, 2020 at 14:47 GMT, there have been 46274 confirmed cases and 588 deaths due to coronavirus COVID-19 in the United States.
March 24, 2020 at 16:47 GMT, there have been 49594 confirmed cases and 622 deaths due to coronavirus COVID-19 in the United States.
March 24, 2020 at 18:45 GMT, there have been 50982 confirmed cases and 655 deaths due to coronavirus COVID-19 in the United States.
March 24, 2020 at 20:42 GMT, there have been 52921 confirmed cases and 684 deaths due to coronavirus COVID-19 in the United States.
March 24, 2020 at 22:48 GMT, there have been 53205 confirmed cases and 687 deaths due to coronavirus COVID-19 in the United States.
March 25, 2020 at 00:29 GMT, there have been 53655 confirmed cases and 698 deaths due to coronavirus COVID-19 in the United States.
March 25, 2020 at 02:44 GMT, there have been 54823 confirmed cases and 778 deaths due to coronavirus COVID-19 in the United States.
March 25, 2020 at 04:46 GMT, there have been 54867 confirmed cases and 782 deaths due to coronavirus COVID-19 in the United States.
March 25, 2020 at 06:47 GMT, there have been 54916 confirmed cases and 784 deaths due to coronavirus COVID-19 in the United States.
March 25, 2020 at 08:48 GMT, there have been 54935 confirmed cases and 784 deaths due to coronavirus COVID-19 in the United States.
March 25, 2020 at 10:43 GMT, there have been 54941 confirmed cases and 784 deaths due to coronavirus COVID-19 in the United States.
March 25, 2020 at 12:48 GMT, there have been 54979 confirmed cases and 785 deaths due to coronavirus COVID-19 in the United States.
March 25, 2020 at 14:48 GMT, there have been 55081 confirmed cases and 785 deaths due to coronavirus COVID-19 in the United States.
March 25, 2020 at 16:48 GMT, there have been 60642 confirmed cases and 817 deaths due to coronavirus COVID-19 in the United States.
March 25, 2020 at 18:48 GMT, there have been 62364 confirmed cases and 878 deaths due to coronavirus COVID-19 in the United States.
March 25, 2020 at 20:33 GMT, there have been 64765 confirmed cases and 910 deaths due to coronavirus COVID-19 in the United States.
March 25, 2020 at 22:44 GMT, there have been 65527 confirmed cases and 928 deaths due to coronavirus COVID-19 in the United States.
March 26, 2020 at 00:34 GMT, there have been 65797 confirmed cases and 935 deaths due to coronavirus COVID-19 in the United States.
March 26, 2020 at 02:43 GMT, there have been 66741 confirmed cases and 963 deaths due to coronavirus COVID-19 in the United States.
March 26, 2020 at 05:24 GMT, there have been 68472 confirmed cases and 1032 deaths due to coronavirus COVID-19 in the United States.
March 26, 2020 at 07:03 GMT, there have been 68489 confirmed cases and 1032 deaths due to coronavirus COVID-19 in the United States.
March 26, 2020 at 09:02 GMT, there have been 68489 confirmed cases and 1032 deaths due to coronavirus COVID-19 in the United States.
March 26, 2020 at 11:02 GMT, there have been 68581 confirmed cases and 1036 deaths due to coronavirus COVID-19 in the United States.
March 26, 2020 at 13:01 GMT, there have been 68594 confirmed cases and 1036 deaths due to coronavirus COVID-19 in the United States.
March 26, 2020 at 14:52 GMT, there have been 68905 confirmed cases and 1037 deaths due to coronavirus COVID-19 in the United States.
March 26, 2020 at 17:02 GMT, there have been 75069 confirmed cases and 1080 deaths due to coronavirus COVID-19 in the United States.
March 26, 2020 at 19:00 GMT, there have been 79082 confirmed cases and 1143 deaths due to coronavirus COVID-19 in the United States.
March 26, 2020 at 21:01 GMT, there have been 81946 confirmed cases and 1177 deaths due to coronavirus COVID-19 in the United States.
March 26, 2020 at 23:02 GMT, there have been 83206 confirmed cases and 1201 deaths due to coronavirus COVID-19 in the United States.
March 27, 2020 at 01:00 GMT, there have been 85280 confirmed cases and 1293 deaths due to coronavirus COVID-19 in the United States.
March 27, 2020 at 03:01 GMT, there have been 85520 confirmed cases and 1297 deaths due to coronavirus COVID-19 in the United States.
March 27, 2020 at 04:36 GMT, there have been 85594 confirmed cases and 1300 deaths due to coronavirus COVID-19 in the United States.
March 27, 2020 at 07:33 GMT, there have been 85612 confirmed cases and 1301 deaths due to coronavirus COVID-19 in the United States.
March 27, 2020 at 09:32 GMT, there have been 85612 confirmed cases and 1301 deaths due to coronavirus COVID-19 in the United States.
March 27, 2020 at 11:31 GMT, there have been 85749 confirmed cases and 1304 deaths due to coronavirus COVID-19 in the United States.
March 27, 2020 at 13:32 GMT, there have been 85755 confirmed cases and 1304 deaths due to coronavirus COVID-19 in the United States.
March 27, 2020 at 15:33 GMT, there have been 86548 confirmed cases and 1321 deaths due to coronavirus COVID-19 in the United States.
March 27, 2020 at 17:32 GMT, there have been 94425 confirmed cases and 1429 deaths due to coronavirus COVID-19 in the United States.
March 27, 2020 at 19:33 GMT, there have been 98180 confirmed cases and 1513 deaths due to coronavirus COVID-19 in the United States.
March 27, 2020 at 21:33 GMT, there have been 100514 confirmed cases and 1546 deaths due to coronavirus COVID-19 in the United States.
March 27, 2020 at 23:33 GMT, there have been 102325 confirmed cases and 1591 deaths due to coronavirus COVID-19 in the United States.
March 28, 2020 at 01:32 GMT, there have been 104126 confirmed cases and 1692 deaths due to coronavirus COVID-19 in the United States.
March 28, 2020 at 03:34 GMT, there have been 104205 confirmed cases and 1704 deaths due to coronavirus COVID-19 in the United States.
March 28, 2020 at 05:35 GMT, there have been 104205 confirmed cases and 1704 deaths due to coronavirus COVID-19 in the United States.
March 28, 2020 at 07:35 GMT, there have been 104256 confirmed cases and 1704 deaths due to coronavirus COVID-19 in the United States.
March 28, 2020 at 09:35 GMT, there have been 104256 confirmed cases and 1704 deaths due to coronavirus COVID-19 in the United States.
March 28, 2020 at 11:40 GMT, there have been 104256 confirmed cases and 1704 deaths due to coronavirus COVID-19 in the United States.
March 28, 2020 at 13:36 GMT, there have been 104277 confirmed cases and 1704 deaths due to coronavirus COVID-19 in the United States.
March 28, 2020 at 15:45 GMT, there have been 105726 confirmed cases and 1730 deaths due to coronavirus COVID-19 in the United States.
March 28, 2020 at 17:45 GMT, there have been 116050 confirmed cases and 1937 deaths due to coronavirus COVID-19 in the United States.
March 28, 2020 at 19:43 GMT, there have been 118592 confirmed cases and 1979 deaths due to coronavirus COVID-19 in the United States.
March 28, 2020 at 21:44 GMT, there have been 120204 confirmed cases and 1997 deaths due to coronavirus COVID-19 in the United States.
March 28, 2020 at 23:43 GMT, there have been 123311 confirmed cases and 2211 deaths due to coronavirus COVID-19 in the United States.
March 29, 2020 at 01:46 GMT, there have been 123578 confirmed cases and 2221 deaths due to coronavirus COVID-19 in the United States.
March 29, 2020 at 03:46 GMT, there have been 123750 confirmed cases and 2227 deaths due to coronavirus COVID-19 in the United States.
March 29, 2020 at 05:48 GMT, there have been 123774 confirmed cases and 2228 deaths due to coronavirus COVID-19 in the United States.
March 29, 2020 at 07:41 GMT, there have been 123776 confirmed cases and 2229 deaths due to coronavirus COVID-19 in the United States.
March 29, 2020 at 09:45 GMT, there have been 123781 confirmed cases and 2229 deaths due to coronavirus COVID-19 in the United States.
March 29, 2020 at 11:44 GMT, there have been 123781 confirmed cases and 2229 deaths due to coronavirus COVID-19 in the United States.
March 29, 2020 at 13:46 GMT, there have been 123828 confirmed cases and 2229 deaths due to coronavirus COVID-19 in the United States.
March 29, 2020 at 15:47 GMT, there have been 125099 confirmed cases and 2238 deaths due to coronavirus COVID-19 in the United States.
March 29, 2020 at 17:49 GMT, there have been 133146 confirmed cases and 2363 deaths due to coronavirus COVID-19 in the United States.
March 29, 2020 at 19:47 GMT, there have been 137943 confirmed cases and 2431 deaths due to coronavirus COVID-19 in the United States.
March 29, 2020 at 21:48 GMT, there have been 139904 confirmed cases and 2449 deaths due to coronavirus COVID-19 in the United States.
March 29, 2020 at 23:49 GMT, there have been 141781 confirmed cases and 2471 deaths due to coronavirus COVID-19 in the United States.
March 30, 2020 at 01:44 GMT, there have been 142004 confirmed cases and 2484 deaths due to coronavirus COVID-19 in the United States.
March 30, 2020 at 03:46 GMT, there have been 142735 confirmed cases and 2488 deaths due to coronavirus COVID-19 in the United States.
March 30, 2020 at 06:46 GMT, there have been 142735 confirmed cases and 2488 deaths due to coronavirus COVID-19 in the United States.
March 30, 2020 at 08:50 GMT, there have been 142735 confirmed cases and 2489 deaths due to coronavirus COVID-19 in the United States.
March 30, 2020 at 10:50 GMT, there have been 142746 confirmed cases and 2489 deaths due to coronavirus COVID-19 in the United States.
March 30, 2020 at 12:50 GMT, there have been 142793 confirmed cases and 2490 deaths due to coronavirus COVID-19 in the United States.
March 30, 2020 at 14:50 GMT, there have been 144410 confirmed cases and 2600 deaths due to coronavirus COVID-19 in the United States.
March 30, 2020 at 16:50 GMT, there have been 145542 confirmed cases and 2616 deaths due to coronavirus COVID-19 in the United States.
March 30, 2020 at 18:50 GMT, there have been 156565 confirmed cases and 2870 deaths due to coronavirus COVID-19 in the United States.
March 30, 2020 at 20:50 GMT, there have been 159689 confirmed cases and 2951 deaths due to coronavirus COVID-19 in the United States.
March 30, 2020 at 22:50 GMT, there have been 161358 confirmed cases and 2974 deaths due to coronavirus COVID-19 in the United States.
March 31, 2020 at 00:50 GMT, there have been 163479 confirmed cases and 3148 deaths due to coronavirus COVID-19 in the United States.
March 31, 2020 at 02:50 GMT, there have been 164253 confirmed cases and 3165 deaths due to coronavirus COVID-19 in the United States.
March 31, 2020 at 04:50 GMT, there have been 164253 confirmed cases and 3167 deaths due to coronavirus COVID-19 in the United States.
March 31, 2020 at 06:50 GMT, there have been 164323 confirmed cases and 3170 deaths due to coronavirus COVID-19 in the United States.
March 31, 2020 at 08:42 GMT, there have been 164359 confirmed cases and 3173 deaths due to coronavirus COVID-19 in the United States.
March 31, 2020 at 10:49 GMT, there have been 164359 confirmed cases and 3173 deaths due to coronavirus COVID-19 in the United States.
March 31, 2020 at 12:49 GMT, there have been 164435 confirmed cases and 3175 deaths due to coronavirus COVID-19 in the United States.
March 31, 2020 at 14:49 GMT, there have been 165392 confirmed cases and 3182 deaths due to coronavirus COVID-19 in the United States.
March 31, 2020 at 16:49 GMT, there have been 175669 confirmed cases and 3424 deaths due to coronavirus COVID-19 in the United States.
March 31, 2020 at 18:49 GMT, there have been 180340 confirmed cases and 3573 deaths due to coronavirus COVID-19 in the United States.
March 31, 2020 at 20:49 GMT, there have been 186046 confirmed cases and 3807 deaths due to coronavirus COVID-19 in the United States.
April 01, 2020 at 01:19 GMT, there have been 187729 confirmed cases and 3867 deaths due to coronavirus COVID-19 in the United States.
April 01, 2020 at 02:49 GMT, there have been 188530 confirmed cases and 3889 deaths due to coronavirus COVID-19 in the United States.
April 01, 2020 at 04:49 GMT, there have been 188578 confirmed cases and 4054 deaths due to coronavirus COVID-19 in the United States.
April 01, 2020 at 06:49 GMT, there have been 188592 confirmed cases and 4055 deaths due to coronavirus COVID-19 in the United States.
April 01, 2020 at 08:49 GMT, there have been 188592 confirmed cases and 4056 deaths due to coronavirus COVID-19 in the United States.
April 01, 2020 at 10:49 GMT, there have been 188639 confirmed cases and 4059 deaths due to coronavirus COVID-19 in the United States.
April 01, 2020 at 12:49 GMT, there have been 188647 confirmed cases and 4059 deaths due to coronavirus COVID-19 in the United States.
April 01, 2020 at 14:49 GMT, there have been 189711 confirmed cases and 4099 deaths due to coronavirus COVID-19 in the United States.
April 01, 2020 at 16:49 GMT, there have been 200289 confirmed cases and 4394 deaths due to coronavirus COVID-19 in the United States.
April 01, 2020 at 18:49 GMT, there have been 205438 confirmed cases and 4528 deaths due to coronavirus COVID-19 in the United States.
April 01, 2020 at 20:49 GMT, there have been 211143 confirmed cases and 4713 deaths due to coronavirus COVID-19 in the United States.
April 01, 2020 at 22:49 GMT, there have been 212980 confirmed cases and 4759 deaths due to coronavirus COVID-19 in the United States.
April 02, 2020 at 00:49 GMT, there have been 215003 confirmed cases and 5102 deaths due to coronavirus COVID-19 in the United States.
April 02, 2020 at 02:49 GMT, there have been 215175 confirmed cases and 5110 deaths due to coronavirus COVID-19 in the United States.
April 02, 2020 at 04:49 GMT, there have been 215300 confirmed cases and 5110 deaths due to coronavirus COVID-19 in the United States.
April 02, 2020 at 06:49 GMT, there have been 215324 confirmed cases and 5112 deaths due to coronavirus COVID-19 in the United States.
April 02, 2020 at 08:49 GMT, there have been 215344 confirmed cases and 5112 deaths due to coronavirus COVID-19 in the United States.
April 02, 2020 at 10:49 GMT, there have been 215344 confirmed cases and 5112 deaths due to coronavirus COVID-19 in the United States.
April 02, 2020 at 12:49 GMT, there have been 216722 confirmed cases and 5140 deaths due to coronavirus COVID-19 in the United States.
April 02, 2020 at 12:49 GMT, there have been 216722 confirmed cases and 5140 deaths due to coronavirus COVID-19 in the United States
April 02, 2020 at 14:49 GMT, there have been 219832 confirmed cases and 5227 deaths due to coronavirus COVID-19 in the United States
April 02, 2020 at 16:49 GMT, there have been 222658 confirmed cases and 5356 deaths due to coronavirus COVID-19 in the United States
April 02, 2020 at 18:49 GMT, there have been 232899 confirmed cases and 5665 deaths due to coronavirus COVID-19 in the United States
April 02, 2020 at 20:49 GMT, there have been 243298 confirmed cases and 5883 deaths due to coronavirus COVID-19 in the United States
April 02, 2020 at 22:19 GMT, there have been 244230 confirmed cases and 5883 deaths due to coronavirus COVID-19 in the United States
April 03, 2020 at 01:20 GMT, there have been 244877 confirmed cases and 6070 deaths due to coronavirus COVID-19 in the United States.
April 03, 2020 at 01:36 GMT, there have been 245066 confirmed cases and 6075 deaths due to coronavirus COVID-19 in the United States.
April 03, 2020 at 03:20 GMT, there have been 245088 confirmed cases and 6075 deaths due to coronavirus COVID-19 in the United States.
April 03, 2020 at 05:20 GMT, there have been 245341 confirmed cases and 6095 deaths due to coronavirus COVID-19 in the United States.
April 03, 2020 at 07:20 GMT, there have been 245373 confirmed cases and 6095 deaths due to coronavirus COVID-19 in the United States.
April 03, 2020 at 09:20 GMT, there have been 245373 confirmed cases and 6095 deaths due to coronavirus COVID-19 in the United States.
April 03, 2020 at 11:20 GMT, there have been 245380 confirmed cases and 6095 deaths due to coronavirus COVID-19 in the United States.
April 03, 2020 at 13:20 GMT, there have been 245442 confirmed cases and 6098 deaths due to coronavirus COVID-19 in the United States.
April 03, 2020 at 14:49 GMT, there have been 245442 confirmed cases and 6099 deaths due to coronavirus COVID-19 in the United States.
April 03, 2020 at 16:49 GMT, there have been 259750 confirmed cases and 6603 deaths due to coronavirus COVID-19 in the United States.
April 03, 2020 at 18:49 GMT, there have been 266279 confirmed cases and 6803 deaths due to coronavirus COVID-19 in the United States.
April 03, 2020 at 20:49 GMT, there have been 272614 confirmed cases and 6988 deaths due to coronavirus COVID-19 in the United States.
April 03, 2020 at 22:49 GMT, there have been 275802 confirmed cases and 7087 deaths due to coronavirus COVID-19 in the United States.
April 04, 2020 at 00:49 GMT, there have been 276965 confirmed cases and 7391 deaths due to coronavirus COVID-19 in the United States.
April 04, 2020 at 02:49 GMT, there have been 277161 confirmed cases and 7392 deaths due to coronavirus COVID-19 in the United States.
April 04, 2020 at 04:49 GMT, there have been 277475 confirmed cases and 7402 deaths due to coronavirus COVID-19 in the United States.
April 04, 2020 at 06:49 GMT, there have been 277522 confirmed cases and 7403 deaths due to coronavirus COVID-19 in the United States.
April 04, 2020 at 08:49 GMT, there have been 277522 confirmed cases and 7403 deaths due to coronavirus COVID-19 in the United States.
April 04, 2020 at 10:49 GMT, there have been 277522 confirmed cases and 7403 deaths due to coronavirus COVID-19 in the United States.
April 04, 2020 at 12:49 GMT, there have been 277607 confirmed cases and 7406 deaths due to coronavirus COVID-19 in the United States.
"""


DATA=DATA.replace("\n","")
lines=DATA.split(".")
cnt=0
for line in lines:
    cnt=cnt+1
    line=line.lstrip(" ")
    if len(line)>5 and cnt>240:print (line)

!update_toybox
#scp /home/jack/Desktop/cOVID-19/data.* jack@192.243.103.247:/var/www/mylinuxtoybox.com/html/COVID-19/
#scp /home/jack/Desktop/COVID-19/Header-Image-1500x250.jpg jack@192.243.103.247:/var/www/mylinuxtoybox.com/html/


for line in DEATHS:
    print(line, end=",")

cnt = -100
for line in DEATHS:
    Cnt = str(cnt)
    line = float(line)
    line = str(line)
    print("["+Cnt+","+line+"]", end=",")
    cnt = cnt +1



import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import numpy as np
#3173,3175,3182,3424,3573
#3,434.2 3,513.3 3,592.4
# 7,640.0 7,773.7 7,907.4
# the given sequence
data =[
[0,6803.0],[1,6988.0],[2,7087.0],[3,7391.0],[4,7392.0],[5,7402],
]


X = np.matrix(data)[:,0]
y = np.matrix(data)[:,1]

def J(X, y, theta):
    theta = np.matrix(theta).T
    m = len(y)
    predictions = X * theta
    sqError = np.power((predictions-y),[2])
    return 1/(2*m) * sum(sqError)


dataX = np.matrix(data)[:,0:1]
X = np.ones((len(dataX),2))
X[:,1:] = dataX


# gradient descent function
def gradient(X, y, alpha, theta, iters):
    J_history = np.zeros(iters)
    m = len(y)
    theta = np.matrix(theta).T
    for i in range(iters):
        h0 = X * theta
        delta = (1 / m) * (X.T * h0 - X.T * y)
        theta = theta - alpha * delta
        J_history[i] = J(X, y, theta.T)
    return J_history, theta

print('\n'+40*'=')

# theta initialization
theta = np.matrix([np.random.random(),np.random.random()])
alpha = 0.01 # learning rate
iters = 2000 # iterations

print('\n== Model summary ==\nLearning rate: {}\nIterations: {}\nInitial theta: {}\nInitial J: {:.2f}\n'.format(alpha, iters, theta, J(X,y,theta).item()))

print('Training the model... ')
# this actually trains our model and finds the optimal theta value
J_history, theta_min = gradient(X, y, alpha, theta, iters)
print('Done.')
print('\nThe modelled prediction function is:\ny = {:.2f} * x + {:.2f}'.format(theta_min[1].item(), theta_min[0].item()))
print('Its cost equals {:.2f}'.format(J(X,y,theta_min.T).item()))


# This function will calculate the predicted profit
def predict(pop):
    return [1, pop] * theta_min

# Now
p = len(data)
print('\n'+40*'=')
print('The given sequence was:\n', *np.array(data)[:,1])
print('\nBased on learned data, next three predicted numbers in the sequence are {:,.1f} {:,.1f} {:,.1f}'.format(predict(p).item(), predict(p+1).item(), predict(p+2).item()))

print('\nNOTE: The code uses linear regression model exclusively and tries to fit a "straight" line to the data. For polynominal it ought to be added theta_2 and beyond.')

print (DEATHS)

import numpy as np
X = np.array(CASES)
y = np.array(DEATHS)
print("X=")
print(X)
print("y=")
print(y)



import datetime
import calendar
import time
from M2D import *
import sqlite3
conn=sqlite3.connect("DATA/CleanCorona.db")
c= conn.cursor()
cnt=0
for row in c.execute('SELECT ROWID,* from CORONA'):
    cnt=cnt+1
    if cnt>160:print (row[0],": ",row[1])

conn.close()


for line in ALLdata:
    print(line)

cnt=0
for line in ALLdata:
    cnt=cnt+1
    if cnt==1:print (line)

60*60*24

cn=0
cnt=0
# Starting Timestamp (09/03/2020 04:30:00)
tstamp= 1583699400
day = 86400
for line in ALLdata:
    line = line.split(",")
    Num= int(line[1])
    SP=(Num-1583699400)
    print (round(SP/day,2), end= "  ")
    cnt=cnt+1
    
print(cnt, end= "  ")        

DEATH = []
for line in ALLdata:
    line = line.split(",")
    Cases = ''.join(c for c in line[3] if c.isdigit())
    Deaths = ''.join(c for c in line[4] if c.isdigit())
    D = int(Deaths)
    DEATH.append(D)
for x in range(2,len(DEATH)-1):
    print(DEATH[x+1]-DEATH[x], end= " ")

import sqlite3
from M2D import Month2Num
arrangedDdata = ''
CASESs = []
DEATHs = []
SPANS = []
arrangedDdata=arrangedDdata+"date_time,cases\n"
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
cnt = 0
for rows in c.execute('SELECT * from CORONA'):
    cnt = cnt  +1
    #if cnt==1:print(rows)
    rows=str(rows)
    row = rows.split(" ")
    if cnt==1:print(row[0][2:],row[1],row[2]+":00",row[4],row[9],row[13])
    if cnt==1:start= row[0][2:],row[1],row[2]   
    CASESs.append(row[9])
    DEATHs.append(row[13])
    if cnt==1:last=10
        

import M2D
help(M2D)

%%writefile DTE.py
from M2D import *
import time
def Date2Epoch(Date,last=1583621400):
    dt = time.strftime(Date)
    Date= Date.replace(",",'')
    DATE = Date.split(" ")
    print(DATE[0],DATE[1],DATE[2],DATE[3])
    date_ti = DATE[1]+"/"+Month2Num(DATE[0])+"/"+DATE[2]+" "+DATE[3]#[:-3]
    #print (dt_ti)
    #03-16-2020 02:48,3777
    pattern = '%d/%m/%Y %H:%M:%S'
    #pattern = '%m/%d/%Y %H:%M:%S'
    epochs = int(time.mktime(time.strptime(date_ti, pattern)))
    #print ("dt_ti, epochs",dt_ti, epochs)

    #if Scnt>1:print (dt_ti, epochs)
    #if Scnt==0:last=1583691400 
        
    Epoch = (date_ti, epochs,span(int(last),int(epochs)))
    #EPOCHS.append(int(epochs))
    return Epoch

from DTE import Date2Epoch
Date = "March 31 2020 02:48:34"
Date2Epoch(Date,last=1583621400)

%%writefile M2D.py
"""
Month2Num(month)
span(timestamp1, timestamp2): This will show the span in hours between two timestamps.
Date = "April 09 2020 10:00:00"
DateEpoch(Date)
"""
from __future__ import division
import time 
def Month2Num(month):
    number=""
    months=["January","February","March","April","May","June","July",\
            "August","September","October","November","December"]
    Numbers=["01","02","03","04","05","06","07","08","09","10","11","12"]
    if month==months[0]:number=Numbers[0]
    if month==months[1]:number=Numbers[1]
    if month==months[2]:number=Numbers[2]
    if month==months[3]:number=Numbers[3]
    if month==months[4]:number=Numbers[4]
    if month==months[5]:number=Numbers[5]
    if month==months[6]:number=Numbers[6]
    if month==months[7]:number=Numbers[7]
    if month==months[8]:number=Numbers[8]
    if month==months[9]:number=Numbers[9]
    if month==months[10]:number=Numbers[10]
    if month==months[11]:number=Numbers[11]    
    return number

def span(timestamp1, timestamp2):
    SPAN = timestamp2-timestamp1
    res =SPAN/3600
    result = round(res,2)
    return result

def DateEpoch(Date):
    dt = time.strftime(Date)
    Date= Date.replace(",",'')
    DATE = Date.split(" ")
    date_ti = DATE[1]+"/"+Month2Num(DATE[0])+"/"+DATE[2]+" "+DATE[3]#[:-3]
    #03-16-2020 02:48,3777
    pattern = '%d/%m/%Y %H:%M:%S'
    timestamp = int(time.mktime(time.strptime(date_ti, pattern)))
    return timestamp

def Date2Epoch(Date,last=1583621400):
    dt = time.strftime(Date)
    Date= Date.replace(",",'')
    DATE = Date.split(" ")
    #print(DATE[0],DATE[1],DATE[2],DATE[3])
    date_ti = DATE[1]+"/"+Month2Num(DATE[0])+"/"+DATE[2]+" "+DATE[3]#[:-3]
    #03-16-2020 02:48,3777
    pattern = '%d/%m/%Y %H:%M:%S'
    epochs = int(time.mktime(time.strptime(date_ti, pattern)))
    Epoch = (date_ti, epochs,span(int(last),int(epochs)))
    return Epoch


from M2D import *
from M2D import *
Date = "January 01 1970 08:00:00"
print(Date2Epoch(Date,last=1))
print("----------- One day later (24 hours) ------------")
Date = "January 02 1970 08:00:00"
print(Date2Epoch(Date,last=0))
print("24 hours is a '86400' value as a timestamp and 24.0 hours have passed.")
Date = "April 09 2020 10:00:00"
print(Date2Epoch(Date,last=1586390400))
print("\nNotice the result has three elements.")
print("A, B, C = Date2Epoch(Date,last=1586390400)")
A, B, C = Date2Epoch(Date,last=1586390400)
print("I can then use them independently.\n")
print("A: ",A)
print("B: ",B)
print("C: ",C)
print("The variables A B C may use any names.")
print("Example: LastD, LastT, Lastspan = Date2Epoch(Date,last=1586390400)")
LastD, LastT, Lastspan = Date2Epoch(Date,last=1586390400)
print("LastD: ",LastD)
print("LastT: ",LastT)
print("Lastspan: ",Lastspan)
print("---------------------------------")
last=1586397600
Date = "April 10 2020 10:30:00"
D,T,span = Date2Epoch(Date,last)
print(" The time passed hours has a",T-LastT,"value as a timestamp and",span,"hours have passed \
\n since",LastD,"and today,", D)
print("---------------------------------")
print(D)
print(T)
print(span)
print(span/8600)

for x in range(20,40):
    print(x,": ",x*x*x)

!pwd



!wget https://mylinuxtoybox.com/COVID-19/data.csv

# %load data.csv
Date Time Timestamp HoursSinceUpdate ConfirmedCases Deaths
09/03/2020,04:30:00,1583699400,10.56,589,22
10/03/2020,05:30:00,1583789400,25.0,708,27
10/03/2020,23:35:00,1583854500,18.08,975,30
11/03/2020,04:25:00,1583871900,4.83,1010,31
11/03/2020,15:17:00,1583911020,10.87,1016,31
11/03/2020,23:35:00,1583940900,8.3,1301,38
12/03/2020,03:25:00,1583954700,3.83,1327,38
12/03/2020,11:37:00,1583984220,8.2,1336,38
12/03/2020,22:00:00,1584021600,10.38,1639,40
13/03/2020,00:05:00,1584029100,2.08,1715,41
13/03/2020,01:35:00,1584034500,1.5,1725,41
13/03/2020,03:45:00,1584042300,2.17,1747,41
13/03/2020,06:00:00,1584050400,2.25,1762,41
13/03/2020,15:25:00,1584084300,9.42,1832,41
13/03/2020,22:25:00,1584109500,7.0,2269,48
14/03/2020,02:40:00,1584124800,4.25,2291,50
14/03/2020,07:14:00,1584141240,4.57,2319,50
14/03/2020,16:45:00,1584175500,9.52,2499,51
14/03/2020,23:03:00,1584198180,6.3,2836,57
15/03/2020,05:00:00,1584219600,5.95,2982,60
15/03/2020,05:40:00,1584222000,0.67,2995,60
15/03/2020,07:05:00,1584227100,1.42,3043,60
15/03/2020,19:00:00,1584270000,11.92,3329,63
15/03/2020,20:05:00,1584273900,1.08,3400,63
15/03/2020,21:15:00,1584278100,1.17,3621,63
15/03/2020,22:15:00,1584281700,1.0,3502,63
16/03/2020,00:35:00,1584290100,2.33,3714,68
16/03/2020,02:48:00,1584298080,2.22,3777,69
16/03/2020,05:36:00,1584308160,2.8,3782,69
16/03/2020,08:29:00,1584318540,2.88,3802,69
16/03/2020,18:40:00,1584355200,10.18,4186,73
16/03/2020,22:40:00,1584369600,4.0,4597,86
17/03/2020,00:45:00,1584377100,2.08,4667,87
17/03/2020,02:40:00,1584384000,1.92,4704,91
17/03/2020,06:35:00,1584398100,3.92,4727,93
17/03/2020,10:31:00,1584412260,3.93,4743,93
17/03/2020,14:38:00,1584427080,4.12,4752,93
17/03/2020,18:41:00,1584441660,4.05,5723,97
17/03/2020,21:55:00,1584453300,3.23,6211,102
17/03/2020,22:40:00,1584456000,0.75,6349,106
18/03/2020,02:20:00,1584469200,3.67,6499,112
18/03/2020,06:05:00,1584482700,3.75,6522,116
18/03/2020,10:10:00,1584497400,4.08,6524,116
18/03/2020,16:15:00,1584519300,6.08,7601,116
18/03/2020,18:16:00,1584526560,2.02,7708,120
18/03/2020,20:21:00,1584534060,2.08,8710,132
18/03/2020,22:10:00,1584540600,1.82,8998,150
19/03/2020,02:17:00,1584555420,4.12,9371,153
19/03/2020,10:16:00,1584584160,7.98,9464,155
19/03/2020,12:18:00,1584591480,2.03,9473,155
19/03/2020,14:15:00,1584598500,1.95,9486,157
19/03/2020,16:22:00,1584606120,2.12,10692,160
19/03/2020,18:17:00,1584613020,1.92,11355,171
19/03/2020,22:45:00,1584629100,4.47,13737,201
20/03/2020,00:48:00,1584636480,2.05,13865,211
20/03/2020,02:40:00,1584643200,1.87,14316,218
20/03/2020,04:34:00,1584650040,1.9,14336,218
20/03/2020,06:35:00,1584657300,2.02,14366,217
20/03/2020,08:10:00,1584663000,1.58,14366,217
20/03/2020,10:11:00,1584670260,2.02,14366,217
20/03/2020,12:11:00,1584677460,2.0,14366,217
20/03/2020,14:10:00,1584684600,1.98,14373,218
20/03/2020,16:11:00,1584691860,2.02,16067,219
20/03/2020,18:12:00,1584699120,2.02,16545,225
20/03/2020,20:12:00,1584706320,2.0,18121,233
20/03/2020,22:12:00,1584713520,2.0,18876,237
21/03/2020,00:06:00,1584720360,1.9,19393,256
21/03/2020,02:07:00,1584727620,2.02,19643,263
21/03/2020,04:08:00,1584734880,2.02,19652,264
21/03/2020,06:05:00,1584741900,1.95,19774,275
21/03/2020,08:10:00,1584749400,2.08,19774,275
21/03/2020,10:12:00,1584756720,2.03,19774,275
21/03/2020,12:46:00,1584765960,2.57,19775,276
21/03/2020,14:48:00,1584773280,2.03,19823,276
21/03/2020,16:48:00,1584780480,2.0,22085,282
21/03/2020,18:45:00,1584787500,1.95,22813,288
21/03/2020,20:45:00,1584794700,2.0,24142,288
21/03/2020,22:45:00,1584801900,2.0,23940,301
22/03/2020,00:40:00,1584808800,1.92,26111,324
22/03/2020,02:40:00,1584816000,2.0,26711,341
22/03/2020,04:45:00,1584823500,2.08,26867,348
22/03/2020,06:30:00,1584829800,1.75,26892,348
22/03/2020,08:45:00,1584837900,2.25,26892,348
22/03/2020,10:45:00,1584845100,2.0,26900,348
22/03/2020,12:48:00,1584852480,2.05,26905,348
22/03/2020,14:45:00,1584859500,1.95,27031,349
22/03/2020,16:42:00,1584866520,1.95,30239,388
22/03/2020,18:48:00,1584874080,2.1,38757,400
22/03/2020,20:44:00,1584881040,1.93,32356,414
22/03/2020,21:41:00,1584884460,0.95,32356,414
23/03/2020,00:44:00,1584895440,3.05,33346,414
23/03/2020,02:37:00,1584902220,1.88,33546,419
23/03/2020,03:55:00,1584906900,1.3,34717,452
23/03/2020,06:45:00,1584917100,2.83,35060,457
23/03/2020,08:47:00,1584924420,2.03,35070,458
23/03/2020,10:47:00,1584931620,2.0,35070,458
23/03/2020,12:46:00,1584938760,1.98,35075,458
23/03/2020,14:45:00,1584945900,1.98,35179,459
23/03/2020,16:45:00,1584953100,2.0,40773,479
23/03/2020,18:46:00,1584960360,2.02,41569,504
23/03/2020,20:47:00,1584967620,2.02,42443,517
23/03/2020,22:31:00,1584973860,1.73,43449,545
24/03/2020,00:47:00,1584982020,2.27,43718,552
24/03/2020,02:33:00,1584988380,1.77,43734,553
24/03/2020,04:46:00,1584996360,2.22,46145,582
24/03/2020,06:43:00,1585003380,1.95,46145,582
24/03/2020,08:48:00,1585010880,2.08,46145,582
24/03/2020,10:47:00,1585018020,1.98,46168,582
24/03/2020,12:47:00,1585025220,2.0,46168,582
24/03/2020,14:47:00,1585032420,2.0,46274,588
24/03/2020,16:47:00,1585039620,2.0,49594,622
24/03/2020,18:45:00,1585046700,1.97,50982,655
24/03/2020,20:42:00,1585053720,1.95,52921,684
24/03/2020,22:48:00,1585061280,2.1,53205,687
25/03/2020,00:29:00,1585067340,1.68,53655,698
25/03/2020,02:44:00,1585075440,2.25,54823,778
25/03/2020,04:46:00,1585082760,2.03,54867,782
25/03/2020,06:47:00,1585090020,2.02,54916,784
25/03/2020,08:48:00,1585097280,2.02,54935,784
25/03/2020,10:43:00,1585104180,1.92,54941,784
25/03/2020,12:48:00,1585111680,2.08,54979,785
25/03/2020,14:48:00,1585118880,2.0,55081,785
25/03/2020,16:48:00,1585126080,2.0,60642,817
25/03/2020,18:48:00,1585133280,2.0,62364,878
25/03/2020,20:33:00,1585139580,1.75,64765,910
25/03/2020,22:44:00,1585147440,2.18,65527,928
26/03/2020,00:34:00,1585154040,1.83,65797,935
26/03/2020,02:43:00,1585161780,2.15,66741,963
26/03/2020,05:24:00,1585171440,2.68,68472,1032
26/03/2020,07:03:00,1585177380,1.65,68489,1032
26/03/2020,09:02:00,1585184520,1.98,68489,1032
26/03/2020,11:02:00,1585191720,2.0,68581,1036
26/03/2020,13:01:00,1585198860,1.98,68594,1036
26/03/2020,14:52:00,1585205520,1.85,68905,1037
26/03/2020,17:02:00,1585213320,2.17,75069,1080
26/03/2020,19:00:00,1585220400,1.97,79082,1143
26/03/2020,21:01:00,1585227660,2.02,81946,1177
26/03/2020,23:02:00,1585234920,2.02,83206,1201
27/03/2020,01:00:00,1585242000,1.97,85280,1293
27/03/2020,03:01:00,1585249260,2.02,85520,1297
27/03/2020,04:36:00,1585254960,1.58,85594,1300
27/03/2020,07:33:00,1585265580,2.95,85612,1301
27/03/2020,09:32:00,1585272720,1.98,85612,1301
27/03/2020,11:31:00,1585279860,1.98,85749,1304
27/03/2020,13:32:00,1585287120,2.02,85755,1304
27/03/2020,15:33:00,1585294380,2.02,86548,1321
27/03/2020,17:32:00,1585301520,1.98,94425,1429
27/03/2020,19:33:00,1585308780,2.02,98180,1513
27/03/2020,21:33:00,1585315980,2.0,100514,1546
27/03/2020,23:33:00,1585323180,2.0,102325,1591
28/03/2020,01:32:00,1585330320,1.98,104126,1692
28/03/2020,03:34:00,1585337640,2.03,104205,1704
28/03/2020,05:35:00,1585344900,2.02,104205,1704
28/03/2020,07:35:00,1585352100,2.0,104256,1704
28/03/2020,09:35:00,1585359300,2.0,104256,1704
28/03/2020,11:40:00,1585366800,2.08,104256,1704
28/03/2020,13:36:00,1585373760,1.93,104277,1704
28/03/2020,15:45:00,1585381500,2.15,105726,1730
28/03/2020,17:45:00,1585388700,2.0,116050,1937
28/03/2020,19:43:00,1585395780,1.97,118592,1979
28/03/2020,21:44:00,1585403040,2.02,120204,1997
28/03/2020,23:43:00,1585410180,1.98,123311,2211
29/03/2020,01:46:00,1585417560,2.05,123578,2221
29/03/2020,03:46:00,1585424760,2.0,123750,2227
29/03/2020,05:48:00,1585432080,2.03,123774,2228
29/03/2020,07:41:00,1585438860,1.88,123776,2229
29/03/2020,09:45:00,1585446300,2.07,123781,2229
29/03/2020,11:44:00,1585453440,1.98,123781,2229
29/03/2020,13:46:00,1585460760,2.03,123828,2229
29/03/2020,15:47:00,1585468020,2.02,125099,2238
29/03/2020,17:49:00,1585475340,2.03,133146,2363
29/03/2020,19:47:00,1585482420,1.97,137943,2431
29/03/2020,21:48:00,1585489680,2.02,139904,2449
29/03/2020,23:49:00,1585496940,2.02,141781,2471
30/03/2020,01:44:00,1585503840,1.92,142004,2484
30/03/2020,03:46:00,1585511160,2.03,142735,2488
30/03/2020,06:46:00,1585521960,3.0,142735,2488
30/03/2020,08:50:00,1585529400,2.07,142735,2489
30/03/2020,10:50:00,1585536600,2.0,142746,2489
30/03/2020,12:50:00,1585543800,2.0,142793,2490
30/03/2020,14:50:00,1585551000,2.0,144410,2600
30/03/2020,16:50:00,1585558200,2.0,145542,2616
30/03/2020,18:50:00,1585565400,2.0,156565,2870
30/03/2020,20:50:00,1585572600,2.0,159689,2951
30/03/2020,22:50:00,1585579800,2.0,161358,2974
31/03/2020,00:50:00,1585587000,2.0,163479,3148
31/03/2020,02:50:00,1585594200,2.0,164253,3165
31/03/2020,04:50:00,1585601400,2.0,164253,3167
31/03/2020,06:50:00,1585608600,2.0,164323,3170
31/03/2020,08:42:00,1585615320,1.87,164359,3173
31/03/2020,10:49:00,1585622940,2.12,164359,3173
31/03/2020,12:49:00,1585630140,2.0,164435,3175
31/03/2020,14:49:00,1585637340,2.0,165392,3182
31/03/2020,16:49:00,1585644540,2.0,175669,3424
31/03/2020,18:49:00,1585651740,2.0,180340,3573
31/03/2020,20:49:00,1585658940,2.0,186046,3807
01/04/2020,01:19:00,1585675140,4.5,187729,3867
01/04/2020,02:49:00,1585680540,1.5,188530,3889
01/04/2020,04:49:00,1585687740,2.0,188578,4054
01/04/2020,06:49:00,1585694940,2.0,188592,4055
01/04/2020,08:49:00,1585702140,2.0,188592,4056
01/04/2020,10:49:00,1585709340,2.0,188639,4059
01/04/2020,12:49:00,1585716540,2.0,188647,4059
01/04/2020,14:49:00,1585723740,2.0,189711,4099
01/04/2020,16:49:00,1585730940,2.0,200289,4394
01/04/2020,18:49:00,1585738140,2.0,205438,4528
01/04/2020,20:49:00,1585745340,2.0,211143,4713
01/04/2020,22:49:00,1585752540,2.0,212980,4759
02/04/2020,00:49:00,1585759740,2.0,215003,5102
02/04/2020,02:49:00,1585766940,2.0,215175,5110
02/04/2020,04:49:00,1585774140,2.0,215300,5110
02/04/2020,06:49:00,1585781340,2.0,215324,5112
02/04/2020,08:49:00,1585788540,2.0,215344,5112
02/04/2020,10:49:00,1585795740,2.0,215344,5112
02/04/2020,12:49:00,1585802940,2.0,216722,5140
02/04/2020,14:49:00,1585810140,2.0,219832,5227
02/04/2020,16:49:00,1585817340,2.0,222658,5356
02/04/2020,18:49:00,1585824540,2.0,232899,5665
02/04/2020,20:49:00,1585831740,2.0,243298,5883
02/04/2020,22:19:00,1585837140,1.5,244230,5883
03/04/2020,01:20:00,1585848000,3.02,244877,6070
03/04/2020,01:36:00,1585848960,0.27,245066,6075
03/04/2020,03:20:00,1585855200,1.73,245088,6075
03/04/2020,05:20:00,1585862400,2.0,245341,6095
03/04/2020,07:20:00,1585869600,2.0,245373,6095
03/04/2020,09:20:00,1585876800,2.0,245373,6095
03/04/2020,11:20:00,1585884000,2.0,245380,6095
03/04/2020,13:20:00,1585891200,2.0,245442,6098
03/04/2020,14:49:00,1585896540,1.48,245442,6099
03/04/2020,16:49:00,1585903740,2.0,259750,6603
03/04/2020,18:49:00,1585910940,2.0,266279,6803
03/04/2020,20:49:00,1585918140,2.0,272614,6988
03/04/2020,22:49:00,1585925340,2.0,275802,7087
04/04/2020,00:49:00,1585932540,2.0,276965,7391
04/04/2020,02:49:00,1585939740,2.0,277161,7392
04/04/2020,04:49:00,1585946940,2.0,277475,7402
04/04/2020,06:49:00,1585954140,2.0,277522,7403
04/04/2020,08:49:00,1585961340,2.0,277522,7403
04/04/2020,10:49:00,1585968540,2.0,277522,7403
04/04/2020,12:49:00,1585975740,2.0,277607,7406
04/04/2020,14:49:00,1585982940,2.0,279500,7457
04/04/2020,16:49:00,1585990140,2.0,293494,7896
04/04/2020,18:49:00,1585997340,2.0,301147,8173
04/04/2020,20:49:00,1586004540,2.0,306768,8347
04/04/2020,22:49:00,1586011740,2.0,308644,8401
05/04/2020,00:49:00,1586018940,2.0,311357,8452
05/04/2020,04:49:00,1586033340,4.0,311635,8454
05/04/2020,06:49:00,1586040540,2.0,311637,8454
05/04/2020,08:49:00,1586047740,2.0,311637,8454
05/04/2020,10:49:00,1586054940,2.0,311637,8454
05/04/2020,12:49:00,1586062140,2.0,311637,8454
05/04/2020,14:49:00,1586069340,2.0,312207,8480
05/04/2020,16:49:00,1586076540,2.0,323596,9172
05/04/2020,18:49:00,1586083740,2.0,328662,9365
05/04/2020,20:49:00,1586090940,2.0,333017,9528
05/04/2020,22:49:00,1586098140,2.0,334745,9572
06/04/2020,00:49:00,1586105340,2.0,336673,9616
06/04/2020,02:49:00,1586112540,2.0,336830,9618
06/04/2020,04:49:00,1586119740,2.0,336830,9618
06/04/2020,06:49:00,1586126940,2.0,336851,9620
06/04/2020,08:49:00,1586134140,2.0,336851,9620
06/04/2020,10:49:00,1586141340,2.0,336851,9620
06/04/2020,12:49:00,1586148540,2.0,336851,9620
06/04/2020,14:49:00,1586155740,2.0,337925,9664
06/04/2020,16:49:00,1586162940,2.0,350013,10327
06/04/2020,18:49:00,1586170140,2.0,356414,10490
06/04/2020,20:49:00,1586177340,2.0,362326,10714
06/04/2020,22:49:00,1586184540,2.0,364066,10792
07/04/2020,00:49:00,1586191740,2.0,367004,10871
07/04/2020,02:49:00,1586198940,2.0,367004,10871
07/04/2020,04:49:00,1586206140,2.0,367629,10941
07/04/2020,06:49:00,1586213340,2.0,367650,10943
07/04/2020,08:49:00,1586220540,2.0,367650,10943
07/04/2020,10:49:00,1586227740,2.0,367650,10943
07/04/2020,12:49:00,1586234940,2.0,367719,10943
07/04/2020,14:49:00,1586242140,2.0,369522,11013
07/04/2020,16:49:00,1586249340,2.0,376194,12246
07/04/2020,18:49:00,1586256540,2.0,388421,12393
07/04/2020,20:49:00,1586263740,2.0,391665,12561
07/04/2020,22:49:00,1586270940,2.0,394587,12748
08/04/2020,00:49:00,1586278140,2.0,399937,12813
08/04/2020,02:49:00,1586285340,2.0,400412,12854
08/04/2020,04:49:00,1586292540,2.0,400540,12857
08/04/2020,06:49:00,1586299740,2.0,400540,12857
08/04/2020,08:49:00,1586306940,2.0,400549,12857
08/04/2020,10:49:00,1586314140,2.0,400549,12857
08/04/2020,12:49:00,1586321340,2.0,400549,12857
08/04/2020,14:49:00,1586328540,2.0,402471,12914
08/04/2020,16:49:00,1586335740,2.0,406697,13868
08/04/2020,18:49:00,1586342940,2.0,418451,14240
08/04/2020,20:49:00,1586350140,2.0,423046,14476
08/04/2020,22:49:00,1586357340,2.0,426300,14622
09/04/2020,00:49:00,1586364540,2.0,430271,14738
09/04/2020,02:49:00,1586371740,2.0,435128,14795
09/04/2020,04:49:00,1586378940,2.0,435128,14795
09/04/2020,06:49:00,1586386140,2.0,435160,14797
09/04/2020,08:49:00,1586393340,2.0,435160,14797
09/04/2020,10:49:00,1586400540,2.0,435160,14797
09/04/2020,12:49:00,1586407740,2.0,435657,14825
09/04/2020,14:49:00,1586414940,2.0,449555,15826
09/04/2020,16:50:00,1586422200,2.02,452205,15914
09/04/2020,18:50:00,1586429400,2.0,455454,16114
09/04/2020,20:50:00,1586436600,2.0,462180,16444
09/04/2020,22:50:00,1586443800,2.0,465240,16512
09/04/2020,22:50:00,1586443800,2.0,465240,16512
10/04/2020,00:50:00,1586451000,2.0,468566,16691
10/04/2020,02:50:00,1586458200,2.0,468566,16691
10/04/2020,04:50:00,1586465400,2.0,468887,16697
10/04/2020,06:50:00,1586472600,2.0,468895,16697
10/04/2020,08:50:00,1586479800,2.0,468895,16697
10/04/2020,10:50:00,1586487000,2.0,468895,16697
10/04/2020,13:08:00,1586495280,2.3,468895,16697
10/04/2020,15:07:00,1586502420,1.98,475237,17055
10/04/2020,17:07:00,1586509620,2.0,478366,17927
10/04/2020,19:07:00,1586516820,2.0,489646,18034
10/04/2020,21:07:00,1586524020,2.0,495750,18430
10/04/2020,23:07:00,1586531220,2.0,501272,18666
11/04/2020,01:07:00,1586538420,2.0,502318,18725
11/04/2020,07:07:00,1586560020,6.0,502876,18747
11/04/2020,09:07:00,1586567220,2.0,503177,18761
11/04/2020,11:07:00,1586574420,2.0,503177,18761
11/04/2020,13:07:00,1586581620,2.0,503177,18761
11/04/2020,15:07:00,1586588820,2.0,505805,18870
11/04/2020,17:07:00,1586596020,2.0,508575,19833
11/04/2020,19:07:00,1586603220,2.0,522331,20087
11/04/2020,21:07:00,1586610420,2.0,528990,20455
11/04/2020,23:07:00,1586617620,2.0,530613,20524
12/04/2020,01:07:00,1586624820,2.0,532879,20577
12/04/2020,03:07:00,1586632020,2.0,532879,20577
12/04/2020,05:49:00,1586641740,2.7,533088,20580
12/04/2020,07:49:00,1586648940,2.0,533115,20580
13/04/2020,09:49:00,1586742540,2.0,560433,22115
13/04/2020,09:49:00,1586742540,2.0,560433,22115
13/04/2020,11:49:00,1586749740,2.0,560433,22115
13/04/2020,13:49:00,1586756940,2.0,560433,22115
13/04/2020,15:49:00,1586764140,2.0,563009,22843
13/04/2020,17:49:00,1586771340,2.0,573827,22950
13/04/2020,19:49:00,1586778540,2.0,579486,23252
13/04/2020,21:49:00,1586785740,2.0,583870,23485
13/04/2020,23:49:00,1586792940,2.0,586377,23610
14/04/2020,01:49:00,1586800140,2.0,586941,23640
14/04/2020,03:49:00,1586807340,2.0,587155,23644
14/04/2020,05:49:00,1586814540,2.0,587155,23644
14/04/2020,07:49:00,1586821740,2.0,587173,23644
14/04/2020,10:04:00,1586829840,2.25,587173,23644
14/04/2020,12:49:00,1586839740,2.75,587815,23654
14/04/2020,14:49:00,1586846940,2.0,590997,24586
14/04/2020,16:49:00,1586854140,2.0,603059,25143
14/04/2020,18:49:00,1586861340,2.0,606822,25473
14/04/2020,20:49:00,1586868540,2.0,609614,25794


import matplotlib.pyplot as plt
import csv

x = []
y = []
t=range(0,350)
cnt=0
with open('data.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if cnt==0:print("Header: ",row)
        if cnt==0:print("-----------------------------------------------------------------------\n")    
        cnt=cnt+1
        if cnt>1:x.append(int(row[4]))
        if cnt>1:y.append(int(row[5]))

plt.plot(t,x, label='Loaded from MyLinuxToyBox data.csv \n - ConfirmedCases column -')
plt.xlabel('x')
plt.ylabel('y')
plt.title('MyLinuxToyBox data.csv \n ConfirmedCases')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import csv

x = []
y = []
t=range(0,350)
cnt=0
with open('data.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if cnt==0:print("Header: ",row)
        if cnt==0:print("-----------------------------------------------------------------------\n")    
        cnt=cnt+1
        if cnt>1:x.append(int(row[4]))
        if cnt>1:y.append(int(row[5]))

plt.plot(t,y, label='Loaded from MyLinuxToyBox data.csv \n - Deaths column -')
plt.xlabel('x')
plt.ylabel('y')
plt.title('MyLinuxToyBox data.csv \n Deaths')
plt.legend()
plt.show()




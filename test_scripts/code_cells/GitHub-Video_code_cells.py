import plotly.graph_objects as go
from matplotlib.pyplot import text
from matplotlib import pyplot as plt
import numpy as np
LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
#LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
Description = LASTFILE[57:-4]
cnt=0
SEARCH = input("Which Country ? ")
CNT=0
offset=[]
offset.append(0)
DataIn = open(LASTFILE).readlines()
for line in DataIn:
    line = line.split(",")
    CNT=CNT+1
    if SEARCH in line[1]:
        cnt=cnt+1
        if cnt==1:print(line,"\n")
        INTER = [int(i) for i in line[13:]] 
        print(line[1],INTER)
for line in INTER:
    offset.append(int(line))

ig = go.Figure()
#fig.add_trace(go.Scatter(y=INTER))
fig.add_trace(go.Bar(y=INTER))
fig.add_trace(go.Bar(y=offset))

fig.update_layout(title = Description)
fig.show()        
        
        

LAT=[12,23,45,34,78,99,6,54,3,4,56,78,23,4,78,56]
len(LAT)


from matplotlib.pyplot import text
from matplotlib import pyplot as plt
import numpy as np

LAT=[12,23,45,34,78,99,6,54,3,4,56,78,23,4,78,56]
LONG=(range(0,len(LAT)))


LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)

fig = plt.figure(num=None, figsize=(6,6), dpi=80, facecolor='salmon')

ax = fig.gca()
#plt.gca(projection='polar')
text(0.1, 0.9, 'This is a plot', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#8eda8b'))
s=16
#plt.axis([-130,-65,20,55])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="black")
plt.grid(True)

plt.xlabel('In this case the botton is the sequnce number of items in "LAT". ')
plt.title('Sample Plot using Misc Data')
plt.ylabel('This is the number used in the list: \n'+str(LAT)+'.')
plt.show()

from matplotlib.pyplot import text
from matplotlib import pyplot as plt
import numpy as np

LAT=[12,23,45,34,78,99,6,54,3,4,56,78,23,4,78,56]
LONG=(range(0,len(LAT)))


LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)
print ("Max Latitude: ",max(LT))
print ("Min Latitude: ",min(LT))
print ("Max Longitude: ",max(LG))
print ("Max Longitude: ",min(LG))

fig = plt.figure(num=None, figsize=(6,6), dpi=80, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

text(0.1, 0.9, 'This is a plot', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#8eda8b'))
s=16
#plt.axis([-130,-65,20,55])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="black")
plt.grid(True)

plt.xlabel('In this case the botton is the sequnce number of items in "LAT". ')
plt.title('Sample Plot using Misc Data')
plt.ylabel('This is the number used in the list: \n'+str(LAT)+'.')
plt.show()

!ls csse_covid_19_data/csse_covid_19_time_series/

LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
#LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
Description = LASTFILE[57:-4]
print(Description)

LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
Description = LASTFILE[57:-4]
DataIn = open(LASTFILE).readlines()
cnt=0
for line in DataIn:
    cnt=cnt+1
    if cnt<2:print(line)

#LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
Description = LASTFILE[57:-4]
DataIn = open(LASTFILE).readlines()
SEARCH = input("SEARCH: ")
cnt = 0
CNTS=0
counts=[]
for line in DataIn:
    cnt=cnt+1
    line=line.lstrip(",")
    if SEARCH in line:
        print(line)
        Items = line.split(",")
        print(SEARCH,Description,Items[4:-1])

line="""Germany,51.0,9.0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,3,3,7,9,11,17,24,28,44,67,84,94,123,157,206,267,342,433,533,645,775,920,1107,1275,1444,1584,1810
"""
Items = line.split(",")
print(Items)
print("------------------------------------")
print(Items[0],Items[4:-1])

#LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
DataIn = open(LASTFILE).readlines()
SEARCH = input("SEARCH: ")
COVIDdata = []
cnt = 0
CNTS=0
counts=[]
for line in DataIn:
    cnt=cnt+1
    line=line.lstrip(",")
    if SEARCH in line:
        print(line)
        Items = line.split(",")
        for item in Items[4:-1]:
            COVIDdata.append(int(item))
print("-------------------------------")
Description = LASTFILE[57:-4]
print(SEARCH,Description,": \n\n",COVIDdata)        

!ls csse_covid_19_data/csse_covid_19_time_series/

import plotly.graph_objects as go
fig = go.Figure()
#fig.add_trace(go.Scatter(y=INTER))
fig.add_trace(go.Bar(y=INTER))
fig.update_layout(title = 'Fluctuations between data entries in Hours')
fig.show()

import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from matplotlib.pyplot import text
import numpy as np
#LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
#LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
Description = LASTFILE[57:-4]
cnt=0
SEARCH = input("Which Country ? ")
CNT=0
CONFIRMEDcases = []
DataIn = open(LASTFILE).readlines()
for line in DataIn:
    line = line.split(",")
    CNT=CNT+1
    #if CNT<50:print (line[1])
    if SEARCH in line[1]:
        cnt=cnt+1
        if cnt==1:print(line,"\n")
        INTER = [int(i) for i in line[13:]] 
        print(line[1],INTER)
for num in INTER:
    CONFIRMEDcases.append(num)

LAT=CONFIRMEDcases
LONG=(range(0,len(LAT)))
LT = np.array(LAT)
LG = np.array(LONG)

fig = plt.figure(num=None, figsize=(6,4), dpi=180, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()
#plt.gca(projection='polar')
text(0.4, 0.7, 'This is a plot of '+Description+' in '+SEARCH, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#8eda8b'))
s=6

print(len(LG))
print(len(LT))
#plt.axis([-130,-65,20,55])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.bar(LG, LT, align='center', alpha=0.5)
#plt.scatter(LG, LT, s=s, color="black")
plt.grid(True)

plt.xlabel('In this case the botton is the sequence days that have passed. ')
plt.title('Sample Plot using '+Description+' Data from '+SEARCH+'.')
plt.ylabel('The last number in the list: '+str(LAT[-1])+'.')
plt.show()         

print(CONFIRMEDcases)

US=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 6, 7, 11, 12, 14, 17, 21, 22, 28, 36, 40, 47, 54, 63, 85, 108, 118, 200, 244, 307, 417, 557, 706, 942, 1209, 1581, 2026, 2467, 2978, 3873, 4757, 5926, 7087, 8407, 9619, 10783]
norm = [float(i)/max(US) for i in US]
print(norm)
z = np.linspace(0.0, LAT[-1], 10)
print(z)


s=6

norm = [float(i)/max(CONFIRMEDcases) for i in CONFIRMEDcases]
SI =[]
for S in norm:
    S=S*30
    SI.append(S)
SZ =np.asarray(SI)+6 
print(SZ)


from matplotlib.pyplot import text
from matplotlib import pyplot as plt
import numpy as np

LAT=CONFIRMEDcases
LONG=(range(0,len(LAT)))


LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)
print ("Max Latitude: ",max(LT))
print ("Min Latitude: ",min(LT))
print ("Max Longitude: ",max(LG))
print ("Max Longitude: ",min(LG))

fig = plt.figure(num=None, figsize=(6,6), dpi=80, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

text(0.6, 0.7, 'This is a plot', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#8eda8b'))



#plt.axis([-130,-65,20,55])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=SZ, color="black")
plt.grid(True)

plt.xlabel('In this case the botton is the sequnce number of items in "LAT". ')
plt.title('Sample Plot using Misc Data')
plt.ylabel('This is the number used in the list: \n'+str(LAT[-1])+'.')
plt.show()


norm = [float(i)/sum(raw) for i in raw]

from matplotlib.pyplot import text
from matplotlib import pyplot as plt
import numpy as np

LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
DataIn = open(LASTFILE).readlines()
SEARCH = input("SEARCH: ")
CONFIRMEDcases = []
cnt = 0
CNTS=0
counts=[]
for line in DataIn:
    cnt=cnt+1
    if cnt==1:print(line)
    line=line.lstrip(",")
    if SEARCH in line:
        print(line)
        Items = line.split(",")
        #for item in Items[4:-1]:
        for item in Items[4:-1]:
            CONFIRMEDcases.append(int(item))

LAT=CONFIRMEDcases[40:]
LONG=(range(0,len(LAT)))
LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)

fig = plt.figure(num=None, figsize=(10,8), dpi=180, facecolor='salmon')
ax = fig.gca()

text(0.3, 0.7, 'This is a plot of Confirmed Cases in '+SEARCH, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

ax.set_facecolor(('#8eda8b'))




S=1
Size=[]
for x in CONFIRMEDcases:
    S=1+(float(x)*.01)
    Size.append(int(S))
s = np.array(Size)

ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="black")
plt.grid(True)

plt.xlabel('In this case the botton is the sequence days that have passed. ')
plt.title('Simple Plots Search and Print per Country')
plt.ylabel('This is the number used in the list: \n'+str(LAT[-1])+'.')
plt.show()            

from matplotlib.pyplot import text
from matplotlib import pyplot as plt
import numpy as np

LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
DataIn = open(LASTFILE).readlines()
SEARCH = input("SEARCH: ")
CONFIRMEDcases = []
cnt = 0
CNTS=0
counts=[]
for line in DataIn:
    cnt=cnt+1
    if cnt==1:print(line)
    line=line.lstrip(",")
    if SEARCH in line:
        print(line)
        Items = line.split(",")
        #for item in Items[4:-1]:
        for item in Items[4:-1]:
            CONFIRMEDcases.append(int(item))

LAT=CONFIRMEDcases[40:]
LONG=(range(0,len(LAT)))
LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)

fig = plt.figure(num=None, figsize=(10,8), dpi=180, facecolor='salmon')
ax = fig.gca()

text(0.3, 0.7, 'This is a plot of Confirmed Cases in '+SEARCH, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

ax.set_facecolor(('#8eda8b'))

S=1
Size=[]
for x in CONFIRMEDcases:
    S=1+(float(x)*.01)
    Size.append(int(S))
s = np.array(Size)

ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="black")
plt.grid(True)

plt.xlabel('In this case the botton is the sequence days that have passed. ')
plt.title('Simple Plots Search and Print per Country')
plt.ylabel('This is the number used in the list: \n'+str(LAT[-1])+'.')
plt.show()            

!pwd

CASESs =[]

import datetime
import calendar
import time
from M2D import *
import sqlite3
import numpy as np
from matplotlib.pyplot import text
from matplotlib import pyplot as plt

arrangedDdata = ''
DDATA =[]
CASESs =[]
DEATHs = []
DDATA.append("Date Time Timestamp SpanBetweenSamples Cases Deaths")
arrangedDdata=arrangedDdata #+"Date, Time, Cases, Deaths, Timestamp, TimeBetweenSamples\n"
conn=sqlite3.connect("/home/jack/Desktop/cOVID-19/DATA/CoronaData2.db")
c= conn.cursor()
cnt=0
for row in c.execute('SELECT rowid,* from CORONA'):
    cnt=cnt+1
    row =str(row)
    row=row.replace(",","")
    row = row.split(" ")
    if cnt==1:start= row[0][2:],row[1],row[2]
    CASESs.append(row[10])
    DEATHs.append(row[14])
    
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


# 3,13,2020,03:45,GMT,1747,41

EPOCHa=[]
Scnt=0


ALLdata=[]
EPOCHS = []
SPANS = []
SPANS.append(0)
SPANS.append(0)
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

    #16-05-2020 02:48:00
    # Pattern to use to create a timestamp
    pattern = '%d/%m/%Y %H:%M:%S'
    #Convert the date (pattern) into a ten digit timestamp. example: 1586141340
    epochs = int(time.mktime(time.strptime(dt_ti, pattern)))
    
    # A function from from M2D import * to convery two timestamps 'last-current' into a span in hours
    if Scnt>1:SPANS.append(span(int(last),int(epochs)))
    #create a one time starting point timestamp called last    
    if Scnt==0:last=1583661400
        
    # create a list of timestamps called EPOCHS, as integers
    EPOCHS.append(int(epochs))
    DEATHS.append(line[3])
    
    #Create a list called ALLdata
    ad = dt_ti, epochs,span(int(last),int(epochs)),line[2],line[3]
    AS =str(ad)
    ALLdata.append(AS)
    
    Scnt=Scnt+1
    
    last = int(epochs)    
    #print (span(int(last),int(epochs)))
    EPOCHa.append(str(epochs))
#create an list of spans in hours as they are accumulated ( converted from timestamps. )    
SPANS.append(SPANS[-1])
acc=0
for accum in SPANS:
    acc=acc+accum
    ACCs.append(round(acc,1)) 
    
START = CASESs[0] 

print("\n--SPANS-Span in Hours between recordings.",len(SPANS),"---------------------------------------------------------")    
print ("Last timespan",SPANS[-1],"hours\n")
print("\n--ALLdata-",len(ALLdata),"---------------------------------------------------------")
print (ALLdata[-1],"\n")
print("\n--EPOCHS-(Total number of timestamps.)",len(EPOCHS),"---------------------------------------------------------")
print (EPOCHS[-1],"\n")
print("\n--ACCs-",len(ACCs),"---------------------------------------------------------")
print ("Timestamp of Last entry: ",ACCs[-1],"\n")
print("Number of days activity has been recorded.",ACCs[-1]/24)
print ("\n++++++++++++++++++++++++++++++++++++++\n")
print ("len(SPANS)",len(SPANS))
print ("len(ACCs)",len(ACCs))
print ("len(CASESs)",len(CASESs))
print ("len(DEATHs)",len(DEATHs))
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


x = np.array(ACCs,dtype=np.float)
y = np.array(CASESs,dtype=np.int)
d = np.array(DEATHs,dtype=np.int)
fig = plt.figure(num=None, figsize=(16,8), dpi=80, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

ax.grid(color='lightgray', linestyle='-', linewidth=1)
#plt.scatter(x, y, s=3)


#plt.plot(x, d)
#plt.yscale('log')
#plt.yscale('symlog', linthreshy=0.01)
plt.scatter(x, d, s=3, color='red')
#plt.scatter(x, y, s=3, color='blue')

plt.title('log')
plt.grid(True)


#plt.grid(True)

plt.xlabel('Hours: Clock Started '+str(ACCs[-1])+' hours ago.\nMarch/08/2020 23:30:00 with 537 Cases and 21 Deaths')
plt.title('Horizontal~Accumulated Hours Since Start - Verticle Number of Confirmed Cases "'+str(CASESs[-1])+'"', fontsize=20)
LastEntryDate=str(ALLdata[-1]).split("'")[1]


s0= 'Number of Confirmed Cases: "'+str(CASESs[-1])+'"'
plt.text(450, 10500, s0, fontsize=12)

s1= "Date:"+LastEntryDate+" GMT"
plt.text(450, 10000, s1, fontsize=12)

s2= 'Started:\n537 Cases\n21 Deaths'
plt.text(0, 1200, s2, fontsize=12)
s= 'v'
plt.text(0, 500, s, fontsize=15)
plt.ylabel('Number of Deaths in the USA', fontsize=22, color="red")
fig.savefig('images/plot-Deaths-002.png', facecolor=fig.get_facecolor(), edgecolor='black')
plt.show()



print(ALLdata[-1])
LastEntryDate=str(ALLdata[-1]).split("'")[1]
print(LastEntryDate)


import datetime
import calendar
import time
from M2D import *
import sqlite3

arrangedDdata = ''
arrangedDdata=arrangedDdata+"date_time,cases\n"
conn=sqlite3.connect("/home/jack/Desktop/cOVID-19/DATA/CoronaData2.db")
c= conn.cursor()
for row in c.execute('SELECT rowid,* from CORONA'):
    MISC=row[1]
    Str = MISC.split(" ")
    month = Str[0][0:5]
    OUT = Month2Num(month)+","+MISC[5:15]+" "+MISC[18:24]+":00"
    OUT = OUT.replace(", ","-")
    OUT = OUT.replace("c","")
    #OUT = OUT.replace(",","-")
    OUT = OUT.replace(" ",",");
    OUT = OUT.replace(",,"," ")
    OUT = OUT.rstrip(",");
    OUT = OUT.replace(",","") 
    #print (OUT) 
    arrangedDdata = arrangedDdata+OUT+"\n"
conn.close() 

text =arrangedDdata.split("\n")
text= text[1:-1]
EPOCHa=[]
Scnt=0
SPANS = []
for line in text:
    #print(line)
    #line=str(LINE)
    line = line.split("-")
    #print (line)
    #print (str(line[1]+'/'+line[0]+'/'+line[2][:-3]))
    dt = time.strftime((str(line[1]+'/'+line[0]+'/'+line[2][:-3])))
    #print (dt+":00")

    dt_ti = dt+":00"
    #print (dt_ti)
    #03-16-2020 02:48,3777
    pattern = '%d/%m/%Y %H:%M:%S'
    #pattern = '%m/%d/%Y %H:%M:%S'
    epochs = int(time.mktime(time.strptime(dt_ti, pattern)))
    #print (dt_ti, epochs)
    
    if Scnt>1:SPANS.append(span(int(last),int(epochs)))
    if Scnt==0:last=1583661400  
    SPan = span(int(last),int(epochs))    
    data = dt_ti+" "+str(epochs)+" "+str(SPan)
    
    entry = str(data)
    Scnt=Scnt+1
    
    last = int(epochs)    
    #print (span(int(last),int(epochs)))
    EPOCHa.append(data)
    
    
for lines in EPOCHa:
    print (lines)
     
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

plt.xlabel('Hours: Clock Started '+str(ACCs[-1])+' hours ago.\nMarch/08/2020 23:30:00 with 537 Cases and 21 Deaths')
plt.title('Horizontal~Accumulated Hours Since Start - Verticle Number of Confirmed Cases "'+str(CASESs[-1])+'"', fontsize=20)

s0= 'Number of Confirmed Cases "'+str(CASESs[-1])+'"'
plt.text(450, 10500, s0, fontsize=12)

s1= 'Started:\n537 Cases\n21 Deaths'
plt.text(0, 1200, s1, fontsize=12)
s1= 'Started:\n537 Cases\n21 Deaths'
plt.text(0, 1200, s1, fontsize=12)
s= 'v'
plt.text(0, 500, s, fontsize=15)
plt.ylabel('Number of Deaths in the USA', fontsize=22, color="red")
fig.savefig('images/plot-Deaths-002.png', facecolor=fig.get_facecolor(), edgecolor='black')
plt.show()

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

plt.xlabel('Hours: Clock Started '+str(ACCs[-1])+' hours ago.\nMarch/08/2020 23:30:00 with 537 Cases and 21 Deaths')
plt.title('Horizontal~Accumulated Hours Since Start - Verticle Number of Confirmed Cases "'+str(CASESs[-1])+'"', fontsize=20)

s0= 'Number of Confirmed Cases "'+str(CASESs[-1])+'"'
plt.text(450, 10500, s0, fontsize=12)

s1= 'Started:\n537 Cases\n21 Deaths'
plt.text(0, 1200, s1, fontsize=12)
s1= 'Started:\n537 Cases\n21 Deaths'
plt.text(0, 1200, s1, fontsize=12)
s= 'v'
plt.text(0, 500, s, fontsize=15)
plt.ylabel('Number of Deaths in the USA', fontsize=22, color="red")
fig.savefig('images/plot-Deaths-002.png', facecolor=fig.get_facecolor(), edgecolor='black')
plt.show()

https://www.latlong.net/
    https://www.census.gov/



!git clone https://github.com/CSSEGISandData/COVID-19.git

!git pull

!ls csse_covid_19_data/csse_covid_19_daily_reports/

LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/04-05-2020.csv"
#LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/03-30-2020.csv"
DataIn = open(LASTFILE).readlines()
LAT=[]
LONG=[]
STATES=[]
cases=[]
longitude = ""
cnt=0
for line in DataIn:
    line=line.replace("\n","")
    line = line.lstrip(",")
    line = line.split(",")
    if "Florida" in line[2] and "-" in (line[6]):
        cnt=cnt+1
        if cnt<5:print(line[2],line[1],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10])
        entry = line[2],line[1],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10]
        STATES.append(entry)
        LAT.append(line[5])
        LONG.append(line[6])
        cases.append(line[7])
        longitude = longitude+line[6]+","
print("\n\n",len(STATES))        

from matplotlib.pyplot import text
from matplotlib import pyplot as plt
import numpy as np
LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)
print ("Max Latitude: ",max(LT))
print ("Min Latitude: ",min(LT))
print ("Max Longitude: ",max(LG))
print ("Max Longitude: ",min(LG))

fig = plt.figure(num=None, figsize=(6,6), dpi=80, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()





text(0.6, 0.7, 'Cleveland', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#8eda8b'))
s=1
#plt.axis([-130,-65,20,55])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="black")
plt.grid(True)



plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
plt.show()

from matplotlib.pyplot import text
from matplotlib import pyplot as plt
import numpy as np
LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)
print ("Max Latitude: ",max(LT))
print ("Min Latitude: ",min(LT))
print ("Max Longitude: ",max(LG))
print ("Max Longitude: ",min(LG))

fig = plt.figure(num=None, figsize=(6,6), dpi=80, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()


text(0.6, 0.7, 'Cleveland', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#8eda8b'))
s=1
#plt.axis([-130,-65,20,55])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="black")
plt.grid(True)



plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
plt.show()

from matplotlib.pyplot import text
from matplotlib import pyplot as plt
import numpy as np
LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/04-02-2020.csv"
#LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/03-30-2020.csv"
DataIn = open(LASTFILE).readlines()
LAT=[]
LONG=[]
STATES=[]
cases=[]
longitude = ""
for line in DataIn:
    line=line.replace("\n","")
    line = line.lstrip(",")
    line = line.split(",")
    if "Florida" in line[2] and "-" in (line[6]):
        #print(line[2],line[1],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10])
        STATES.append(text)
        LAT.append(line[5])
        LONG.append(line[6])
        cases.append(line[7])
        longitude = longitude+line[6]+","
print("\n\n",len(STATES))        
LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)
print ("Max Latitude: ",max(LT))
print ("Min Latitude: ",min(LT))
print ("Max Longitude: ",max(LG))
print ("Max Longitude: ",min(LG))
print((max(LG)-min(LG))*69)
print((max(LT)-min(LT))*69)

fig = plt.figure(num=None, figsize=(4,4), dpi=120, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

text(0.6, 0.11, 'Miami-Dade', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#8eda8b'))
S=1
Size=[]
for x in cases:
    S=1+(float(x)*.1)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

#plt.axis([-130,-65,20,55])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="black")
plt.grid(True)

plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
plt.show()

from matplotlib.pyplot import text
from matplotlib import pyplot as plt
import numpy as np
LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/04-02-2020.csv"
#LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/03-30-2020.csv"
DataIn = open(LASTFILE).readlines()
LAT=[]
LONG=[]
STATES=[]
cases=[]
longitude = ""
for line in DataIn:
    line=line.replace("\n","")
    line = line.lstrip(",")
    line = line.split(",")
    if "Ohio" in line[2] and "-" in (line[6]):
        #print(line[2],line[1],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10])
        STATES.append(text)
        LAT.append(line[5])
        LONG.append(line[6])
        cases.append(line[7])
        longitude = longitude+line[6]+","
print("\n\n",len(STATES))        
LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)
print ("Max Latitude: ",max(LT))
print ("Min Latitude: ",min(LT))
print ("Max Longitude: ",max(LG))
print ("Max Longitude: ",min(LG))
print((max(LG)-min(LG))*69)
print((max(LT)-min(LT))*69)

fig = plt.figure(num=None, figsize=(6,6), dpi=120, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

text(0.8, 0.91, 'Cleveland', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#8eda8b'))
S=1
Size=[]
for x in cases:
    S=1+(float(x)*.1)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

#plt.axis([-130,-65,20,55])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="black")
plt.grid(True)

plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
plt.show()

from matplotlib import pyplot as plt

import numpy as np
LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/04-05-2020.csv"
DataIn = open(LASTFILE).readlines()
cnt=-1
LAT =[]
LON =[]
cases = []
STate = input("What State? ")
for lines in DataIn:
    lines = lines.replace("\n","")

    line = lines.split(",")
    if STate in line[2] and len(line[5])>8 and len(line[6])>4:
        cnt=cnt+1
        if cnt<2:print(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
        LAT.append(line[5]) 
        LON.append(line[6])
        cases.append(int(line[7]))
LA = LAT
LO = LON

print("len(LA)",len(LA))
print("len(LO)",len(LO))
LT = np.array(LAT,dtype=np.float)
LG = np.array(LON,dtype=np.float)
print ('min(LG)',min(LG))
print ('max(LG)',max(LG))
print ("min(LT)",min(LT))
print ("max(LT)",max(LT))
print("----------------------")

print('len(LT)',len(LT))
print('len(LG)',len(LG))

print ("min(cases)",min(cases))
print("max(cases)",max(cases))
print("len(cases)",len(cases))
print("cases",cases)
fig = plt.figure(num=None, figsize=(12,10), dpi=80, facecolor='red')
ax = fig.gca()

ax.set_facecolor(('white'))

S=1
Size=[]
for x in cases:
    S=3+(float(x)*.1)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)



lgmin= (min(LG))-4
lgmax= (max(LG))+4
ltmin= (min(LT))+4
ltmax= (max(LT))-4

print ('lgmin',lgmin)# = (min(LG))+5
print ('lgmax',lgmax)# = (max(LG))-5
print ('ltmin',ltmin)# = (min(LT))+5
print ('ltmax',ltmax)# = (max(LT))-5


#longLeft= (min(LG))-3
#longRight = (max(LG))+3
#latTop = (min(LT))-3
#latBottom = (max(LT))+3
#plt.axis([longLeft,longRight,latTop,latBottom])

#plt.axis([lgmin,lgmax,ltmin,ltmax ])


#plt.axis([-130,-65,20,55])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="blue")
plt.grid(True)
#plt.text(50,50, "Verticle lines are Longitude, Horizontal lines are Latitude")
text = (50,50, "Verticle lines are Longitude, Horizontal lines are Latitude")
plt.xlabel('This plot is of: '+STate, fontsize=20)
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19', fontsize=16, color="white")
plt.ylabel('The Dot size is relative to the number of cases')
plt.show()

from matplotlib.pyplot import text
from matplotlib import pyplot as plt
import numpy as np
LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/04-02-2020.csv"
#LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/03-30-2020.csv"
DataIn = open(LASTFILE).readlines()
LAT=[]
LONG=[]
STATES=[]
cases=[]
Search = input("Which State? ")
longitude = ""
for line in DataIn:
    line=line.replace("\n","")
    line = line.lstrip(",")
    line = line.split(",")
    if Search in line[2] and "-" in (line[6]):
        #print(line[2],line[1],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10])
        STATES.append(text)
        LAT.append(line[5])
        LONG.append(line[6])
        cases.append(line[7])
        longitude = longitude+line[6]+","
print("\n\n",len(STATES))        
LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)
print ("Max Latitude: ",max(LT))
print ("Min Latitude: ",min(LT))
print ("Max Longitude: ",max(LG))
print ("Max Longitude: ",min(LG))
print(int(max(LG)-min(LG))*.69)
print(int(max(LT)-min(LT))*.69)

H = (int(max(LG)-min(LG))*.69*2)
V = (int(max(LT)-min(LT))*.69*2)

fig = plt.figure(num=None, figsize=(H,V), dpi=120, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

#text(0.6, 0.1, 'Detroit', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#8eda8b'))
S=1
Size=[]
for x in cases:
    S=3+(float(x)*.1)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

#plt.axis([-130,-65,20,55])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="black")
plt.grid(True)

plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
plt.show()

from matplotlib.pyplot import text
from matplotlib import pyplot as plt
import numpy as np
LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/04-06-2020.csv"
#LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/03-30-2020.csv"
DataIn = open(LASTFILE).readlines()
LAT=[]
LONG=[]
STATES=[]
cases=[]
longitude = ""
SEARCH = input("What State? ")
for line in DataIn:
    line=line.replace("\n","")
    line = line.lstrip(",")
    line = line.split(",")
    if SEARCH in line[2] and "-" in (line[6]):
        #print(line[2],line[1],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10])
        STATES.append(text)
        LAT.append(line[5])
        LONG.append(line[6])
        cases.append(line[7])
        longitude = longitude+line[6]+","
print("\n\n",len(STATES))        
LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)
print ("Max Latitude: ",max(LT))
print ("Min Latitude: ",min(LT))
print ("Max Longitude: ",max(LG))
print ("Max Longitude: ",min(LG))
print(int(max(LG)-min(LG))*.69)
print(int(max(LT)-min(LT))*.69)

H = (int(max(LG)-min(LG))*.69)
V = (int(max(LT)-min(LT))*.69)

fig = plt.figure(num=None, figsize=(H,V), dpi=120, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

text(0.6, 0.1, SEARCH, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#8eda8b'))
S=1
Size=[]
for x in cases:
    S=1+(float(x)*.1)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

#plt.axis([-130,-65,20,55])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="black")
plt.grid(True)

plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
plt.show()

from matplotlib.pyplot import text
from matplotlib import pyplot as plt
import numpy as np
LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/04-02-2020.csv"
#LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/03-30-2020.csv"
DataIn = open(LASTFILE).readlines()
LAT=[]
LONG=[]
STATES=[]
cases=[]
longitude = ""
for line in DataIn:
    line=line.replace("\n","")
    line = line.lstrip(",")
    line = line.split(",")
    if "Washington" in line[2] and "-" in (line[6]):
        #print(line[2],line[1],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10])
        STATES.append(text)
        LAT.append(line[5])
        LONG.append(line[6])
        cases.append(line[7])
        longitude = longitude+line[6]+","
print("\n\n",len(STATES))        
LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)
print ("Max Latitude: ",max(LT))
print ("Min Latitude: ",min(LT))
print ("Max Longitude: ",max(LG))
print ("Max Longitude: ",min(LG))
print(int(max(LG)-min(LG))*.69)
print(int(max(LT)-min(LT))*.69)

H = (int(max(LG)-min(LG))*.69)
V = (int(max(LT)-min(LT))*.69)
Factor=round((H/V),3)
print("Factor:",Factor)
fig = plt.figure(num=None, figsize=(5,5*Factor), dpi=120, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

#text(0.6, 0.1, 'Los Angeles', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#8eda8b'))
S=1
Size=[]
for x in cases:
    S=1+(float(x)*.1)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

#plt.axis([-130,-65,20,55])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="black")
plt.grid(True)

plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
plt.show()

from matplotlib.pyplot import text
from matplotlib import pyplot as plt
import numpy as np
LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)
print ("Max Latitude: ",max(LT))
print ("Min Latitude: ",min(LT))
print ("Max Longitude: ",max(LG))
print ("Max Longitude: ",min(LG))
print((max(LG)-min(LG))*69)
print((max(LT)-min(LT))*69)

fig = plt.figure(num=None, figsize=(8,9), dpi=120, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

text(0.8, 0.11, 'Miami-Dade', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#8eda8b'))
S=1
Size=[]
for x in cases:
    S=1+(float(x)*.1)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

#plt.axis([-130,-65,20,55])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="black")
plt.grid(True)

plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
plt.show()

import numpy as geek 
import pylab as p 
  
# Start = 0 
# End = 2 
# Samples to generate = 10 
x1 = geek.linspace(0, 2, 20, endpoint = "False") 
y1 = geek.ones(20) 
  
p.plot(x1, y1, '*', color='red') 
p.xlim(-0.2, 3) 

import numpy as geek 
import pylab as p 
print (len(LG))
lg= len(LG)
print (LG[1])
print (LG[-1])
print("----------------")
print (max(LT))
print (min(LT))
print (max(LG))
print (min(LG))
print("----------------")
ylim0=(max(LT))+.5
ylim1=(min(LT))+.5
xlim1=max(LG)-.5
xlim0=min(LG)-.5

print(ylim0)
print(ylim1)
print(xlim0)
print(xlim1)
fig = plt.figure(num=None, figsize=(6,5), dpi=120, facecolor='salmon')



# Start = 0 
# End = 2 
# Samples to generate = 10 
x1 = geek.linspace(0, 2, 10, endpoint = False) 
y1 = geek.ones(10) 
  
p.plot(LG, LT, '.') 
p.xlim(xlim0, xlim1) 
p.ylim(ylim1, ylim0) 

w = 10
h = 12
d = 80
plt.figure(figsize=(w, h,), dpi=d)
fig, ax = plt.subplots()
ax.scatter(LG, LT, s=2)

#y = [2.56422, 3.77284, 3.52623, 3.51468, 3.02199]
#z = [0.15, 0.3, 0.45, 0.6, 0.75]
#txt = 'Dade'
ax.axis([-88, -80, 24, 31])

ax.text(25,81, ". Data: (1, 5)", transform=ax.transData)
ax.text(85, 26, ". Axes: (0.5, 0.1)", transform=ax.transAxes)
ax.text(87, 27, ". Figure: (0.2, 0.2)", transform=fig.transFigure);

fig, ax = plt.subplots()
#ax.annotate(txt, (3, 3))
ax.scatter(x, y)




fig, ax = plt.subplots(facecolor='lightgray')
ax.axis([0, 10, 0, 10])

# transform=ax.transData is the default, but we'll specify it anyway
ax.text(1, 5, ". Data: (1, 5)", transform=ax.transData)
ax.text(0.5, 0.1, ". Axes: (0.5, 0.1)", transform=ax.transAxes)
ax.text(0.2, 0.2, ". Figure: (0.2, 0.2)", transform=fig.transFigure);
fig, ax = plt.subplots()
#ax.annotate(txt, (3, 3))
ax.scatter(x, y)

from matplotlib.pyplot import text
from matplotlib import pyplot as plt
import numpy as np
LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)
print ("Max Latitude: ",max(LT))
print ("Min Latitude: ",min(LT))
print ("Max Longitude: ",max(LG))
print ("Max Longitude: ",min(LG))

fig = plt.figure(num=None, figsize=(6,6), dpi=80, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

text(0.8, 0.11, 'Miami-Dade', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#8eda8b'))
S=1
Size=[]
for x in cases:
    S=1+(float(x)*.1)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

#plt.axis([-130,-65,20,55])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="black")
plt.grid(True)

plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
plt.show()

%%writefile M2D.py
"""
Month2Num(month)
span(timestamp1, timestamp2): This will show the span in hours between two timestamps.

"""
from __future__ import division
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


fig, ax = plt.subplots(facecolor='lightgray')
ax.axis([0, 10, 0, 10])

# transform=ax.transData is the default, but we'll specify it anyway
ax.text(1, 5, ". Data: (1, 5)", transform=ax.transData)
ax.text(0.5, 0.1, ". Axes: (0.5, 0.1)", transform=ax.transAxes)
ax.text(0.2, 0.2, ". Figure: (0.2, 0.2)", transform=fig.transFigure);


# doubling the width of markers
x = [0,2,4,6,8,10]
y = range(0, len(x))
s = [20*2**n for n in range(len(x))]

plt.scatter(x,y,s=s)


plt.show()

y = [0,2,4,6,8,10]
z = range(0, len(x))
n = [20*2**n for n in range(len(x))]
fig, ax = plt.subplots()
ax.scatter(z, y, s=s, color="lightGray")

for i, txt in enumerate(n):
    #if int(txt)>80 and int(txt)<640:
        ax.annotate(txt, (z[i], y[i]))

y = [2.56422, 3.77284, 3.52623, 3.51468, 3.02199]
z = [0.15, 0.3, 0.45, 0.6, 0.75]
n = [58, 651, 393, 203, 123]

fig, ax = plt.subplots()
ax.scatter(z, y)

for i, txt in enumerate(n):
    ax.annotate(txt, (z[i], y[i]))

14.5995° N, 120.9842° E

import matplotlib.pyplot as plt
w = 4
h = 3
d = 70
plt.figure(figsize=(w, h), dpi=d)
x = LG
y = LT
x_pos = 1
y_pos = 2
#plt.text(x_pos, y_pos, "text on plot")

plt.plot(x,y)

S=1
Size=[]
for x in cases:
    S=1+(float(x)*.1)
    Size.append(int(S))
    print(int(S))
s = np.array(Size)

s = [.1*n for n in range(len(cases))]
for I in s:
    print (int(I))

%matplotlib inline

fig, ax = plt.subplots()

x = np.linspace(0, 40, 1000)
ax.plot(x, np.cos(x))
ax.axis('equal')

ax.annotate('Using An Arrow Pointer', xy=(18.5, 1), xytext=(10, 10),
            arrowprops=dict(facecolor='red', shrink=.01))

ax.annotate('local minimum', xy=(6 * np.pi, -1), xytext=(-5, -20),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle3,angleA=-50,angleB=-90"));


from __future__ import division, absolute_import, print_function
from graph_tools import Graph
from graph_tools import *
import sys
if sys.version_info < (3,):
    range = xrange
import os
from pylab import *  # for plotting
from numpy.random import *  # for random sampling

v_age = g.new_vertex_property("int")
      e_age = g.new_edge_property("int")
      

AttributeError: 'Graph' object has no attribute 'new_vertex_property'


LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/04-02-2020.csv"
#LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/03-30-2020.csv"
DataIn = open(LASTFILE).readlines()
LAT=[]
LONG=[]
STATES=[]
cases=[]
longitude = ""
cnt=0
for line in DataIn:
    cnt=cnt+1
    if cnt==1:print(line)
    line=line.replace("\n","")
    line = line.lstrip(",")
    line = line.split(",")
    if "Germany" in line:
        if (len(line))==9:print(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
        STATES.append(text)
        LAT.append(line[5])
        LONG.append(line[6])
        cases.append(line[7])
        longitude = longitude+line[6]+","

LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/04-02-2020.csv"
#LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/03-30-2020.csv"
DataIn = open(LASTFILE).readlines()
LAT=[]
LONG=[]
STATES=[]
cases=[]
longitude = ""
cnt=0
Cnt=0
for line in DataIn:
    cnt=cnt+1
    if cnt==1:print(line)
    line=line.replace("\n","")
    line = line.lstrip(",")
    line = line.split(",")
    if (len(line))==9:Cnt=Cnt+1
    if (len(line))==9 and len(line[1])>4:
        print(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
    STATES.append(text)
    LAT.append(line[5])
    LONG.append(line[6])
    cases.append(line[7])
    longitude = longitude+line[6]+","
print(Cnt)

https://anthonylouisdagostino.com/bounding-boxes-for-all-us-states/




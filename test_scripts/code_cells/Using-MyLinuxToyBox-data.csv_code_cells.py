!wget -O DATA/MATHPLOT.csv https://mylinuxtoybox.com/COVID-19/data.csv

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

import plotly.graph_objects as go
from plotly.offline import plot, iplot
import plotly.graph_objs as go
import plotly.offline
plotly.offline.init_notebook_mode(connected=True) 
fig = go.Figure(
    data=[go.Bar(y=x)],
    layout_title_text="A Figure Displayed ConfirmedCases Using data.csv and Plotly"
)
fig.show()

import plotly.graph_objects as go
from plotly.offline import plot, iplot
import plotly.graph_objs as go
import plotly.offline
plotly.offline.init_notebook_mode(connected=True) 
fig = go.Figure(
    data=[go.Bar(y=y)],
    layout_title_text="A Figure Displayed Deaths Using data.csv and Plotly"
)
fig.show()

!rm DATA/Download.csv
!wget -O DATA/Download.csv https://mylinuxtoybox.com/COVID-19/data.csv

!rm DATA/DATAcsv.db
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
filename = "DATA/"+(time.strftime('%a_%d_%b_%Y_%I_%M_%S_%p_%Z', time.gmtime())+".csv")
DataIn = open(filename,"w")
listTEXT = []
stringTEXT = ""
response = requests.get('https://mylinuxtoybox.com/COVID-19/data.csv')
DATA = str(response.content)
listTEXT.append(DATA)
stringTEXT = stringTEXT+DATA
DataIn.write(str(listTEXT))
DataIn.close()
print(filename)
files = glob.glob('DATA/*.csv') # * means format then *.html
File = max(files, key=os.path.getctime)
print ("Opening: ",File)
DataOut = open(File, "r").read()

conn=sqlite3.connect("DATA/DATAcsv.db")
c = conn.cursor()

def Insert(line,c=c):
    c.execute("CREATE TABLE IF NOT EXISTS CORONA(TEXT UNIQUE)")
    c.execute("INSERT OR IGNORE into CORONA values (?)",(line,))   
    
cnt=0    
Lines = (str(DataOut).split('\\n'))
for line in Lines:
    if cnt==0:entry = str(line[4:])
    cnt=cnt+1
    if cnt>1 and len(line)>5:entry=line[:-1]
    entry=entry.replace("\\","");entry=entry.replace("\\","")    
    Insert(entry,c=c)    
conn.commit()
conn.close()


conn=sqlite3.connect("DATA/DATAcsv.db")
c = conn.cursor()
LAST = []
LAST.append(0)
for row in c.execute("select * from CORONA"):
    ROW = str(row[0])
    print(ROW)

import sqlite3
conn=sqlite3.connect("DATA/DATAcsv.db")
c = conn.cursor()
LAST = []
LAST.append(0)
cnt=0
for row in c.execute("select * from CORONA"):
    cnt=cnt+1
    if cnt>1:
        ROW = str(row[0])
        #print(ROW)
        ROW = ROW.split(",")
        #print(ROW[4])
        print(int(ROW[4]),int(ROW[4])-LAST[-1])
        span=int(ROW[4])-LAST[-1]
        LAST.append(span)

conn=sqlite3.connect("DATA/DATAcsv.db")
c = conn.cursor()
LASTd = []
LASTD = []
LASTd.append(0)
cnt=0
for row in c.execute("select * from CORONA"):
    cnt=cnt+1
    if cnt>1:
        ROW = str(row[0])
        ROW = ROW.split(",")
        print(int(ROW[5])-int(LASTd[-1]))
        entry= int(ROW[5])-int(LASTd[-1])
        LASTD.append(entry)
        LASTd.append(int(ROW[5]))
        

import matplotlib.pyplot as plt
import csv
from matplotlib.pyplot import text
from matplotlib.pyplot import figure
x = LASTD
print("len(LASTd)",len(x),"\nDDifference at last count.",LASTD[-1])
t=range(0,len(LASTD))
fig = plt.figure(num=None, figsize=(12,12), dpi=80, facecolor='salmon')
#fig = plt.figure()

ax = fig.gca()

ax.set_facecolor('xkcd:beige')
#ax.set_facecolor(('#8eda8b'))
plt.plot(t,x, label='Loaded from MyLinuxToyBox data.csv \n- Deaths column -\nThis shows the difference from the previous count.\nThe low areas of the spikes is when no new data is added.')


plt.grid(True)

plt.xlabel('- Longitude -\nFirst Data Record : January 21, 2020', fontsize=18)
plt.title('Using Latitude and Longitude from:\n https://github.com/CSSEGISandData/COVID-19\n Black is Confirmed Cases and the Red are Deaths', fontsize=18)
plt.ylabel('- Latitude -', fontsize=18, color="white")


plt.title('MyLinuxToyBox data.csv \n Deaths')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import csv

x = LASTd
print("len(LASTd)",len(x),"\nDeaths at last count.",LASTd[-1])
t=range(0,len(LASTd))
fig = plt.figure(num=None, figsize=(12,12), dpi=80, facecolor='salmon')
plt.plot(t,x, label='Loaded from MyLinuxToyBox data.csv \n - Deaths column -')
plt.xlabel('Time')
plt.ylabel('Deaths')
plt.grid(True)
plt.title('MyLinuxToyBox data.csv \n Deaths')
plt.legend()
plt.show()

from matplotlib.pyplot import text
from matplotlib import pyplot as plt
import numpy as np
import mpld3
from mpld3 import plugins
import time
%matplotlib inline


DA = np.array(LASTd,dtype=np.int)
TA = np.array(range(0,len(DA)))
"""
              #LT = np.array(LAT,dtype=np.float)
#LG = np.array(LONG,dtype=np.float)
#print (max(LG))
#print (min(LG))
#print (min(LT))
#print (max(LT))

#A = (min(LG))-1
#B = (max(LG))+1
#C = (min(LT))-1
#D = (max(LT))+1
"""
fig = plt.figure(num=None, figsize=(12,12), dpi=80, facecolor='salmon')
#fig = plt.figure()

ax = fig.gca()

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#8eda8b'))
"""
Sd=1
Sized=[]
for xd in deaths:
    Sd=2+(float(xd)*1)
    Sized.append(int(Sd))
    #print(int(S))
sd = np.array(Sized)

S=1
Size=[]
for x in cases:
    S=2+(float(x)*1)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)


plt.text(-119, 41, SEARCH, fontsize=26)
#plt.axis([-130,-65,20,55])
plt.axis([A,B,C,D])
"""
ax.grid(color='lightgray', linestyle='-', linewidth=1)
#plt.bar(DA, TA, s=2, color="black")
#plt.bar(TA, DA, color="black")
plt.plot(TA, DA, color="black")
#plt.scatter(LG, LT, s=sd, color="red")
plt.grid(True)

plt.xlabel('- Longitude -\nFirst Data Record : January 21, 2020', fontsize=18)
plt.title('Using Latitude and Longitude from:\n https://github.com/CSSEGISandData/COVID-19\n Black is Confirmed Cases and the Red are Deaths', fontsize=18)
plt.ylabel('- Latitude -', fontsize=18, color="white")
#filename = "images/"+SEARCH+"_"+(time.strftime('%a_%d_%b_%Y_%I_%M_%S_%p_%Z', #time.gmtime())+".png")
#fig.savefig(filename, facecolor=fig.get_facecolor(), edgecolor='black')
#print(filename)
plt.show()

from matplotlib.pyplot import text
from matplotlib import pyplot as plt
import numpy as np
import mpld3
from mpld3 import plugins
import time
%matplotlib inline
LASTFILE="DATA/Download.csv"
DataIn = open(LASTFILE).readlines()
cases=[]
cnt=cnt+1
for line in DataIn:
    line = line.split(",")
    if cnt==0:print(line)
    
       

LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"
DataIn = open(LASTFILE).readlines()
LAT=[]
LONG=[]
CITY=[]
deaths=[]
TEXT=[]
cnt = -1
Total=0
SEARCH = "California"
for line in DataIn:
    if len(line)>10 and 'US' in line and "Recovered" not in line and "Unassigned" not in line:
        cnt=cnt+1
        line=line.replace("\n","")
        line = line.lstrip(",")
        line = line.split(",")
        End=len(line)-1
        if len(line)>5 and SEARCH in line[6] and "0.0" not in line:
            if cnt>=1:print(line[5],line[6],line[8],line[9], line[End] )
            Total=Total+int(line[End])
            CITY.append(line[5])
            LAT.append(line[8])
            LONG.append(line[9])
            deaths.append(line[End])        
            text = str(line[2]+' '+line[1]+' '+line[3]+' '+line[4]+' '+line[5]+' '+line[6]+' '+line[7]+' '+line[8]+' '+line[9]+' '+line[10])
            TEXT.append(text)
            
print("Number of Cities: ",len(CITY)) 
print("Total Deaths: ",Total)

LA = LAT
LO = LONG

print(len(LA))
print(len(LO))

DA = np.array(deaths,dtype=np.int)
LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)
print (max(LG))
print (min(LG))
print (min(LT))
print (max(LT))

A = (min(LG))-1
B = (max(LG))+1
C = (min(LT))-1
D = (max(LT))+1

fig = plt.figure(num=None, figsize=(12,12), dpi=80, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#8eda8b'))

Sd=1
Sized=[]
for xd in deaths:
    Sd=2+(float(xd)*1)
    Sized.append(int(Sd))
    #print(int(S))
sd = np.array(Sized)

S=1
Size=[]
for x in cases:
    S=2+(float(x)*1)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)


plt.text(-119, 41, SEARCH, fontsize=26)
#plt.axis([-130,-65,20,55])
plt.axis([A,B,C,D])

ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=sd, color="red")
plt.scatter(LG, LT, s=s, color="black")

plt.grid(True)

plt.xlabel('- Longitude -\nFirst Data Record : January 21, 2020', fontsize=18)
plt.title('Using Latitude and Longitude from:\n https://github.com/CSSEGISandData/COVID-19\n Black is Confirmed Cases and the Red are Deaths', fontsize=18)
plt.ylabel('- Latitude -', fontsize=18, color="white")
filename = "images/"+SEARCH+"_"+(time.strftime('%a_%d_%b_%Y_%I_%M_%S_%p_%Z', time.gmtime())+".png")
fig.savefig(filename, facecolor=fig.get_facecolor(), edgecolor='black')
print(filename)
plt.show()

import plotly.graph_objects as go
from plotly.offline import plot, iplot
import plotly.graph_objs as go
import plotly.offline
plotly.offline.init_notebook_mode(connected=True) 
fig = go.Figure(
    data=[go.Bar(y=LASTd)],
    layout_title_text="A Figure Displayed ConfirmedCases Using data.csv and Plotly"
)
fig.show()

print(LASTd)

import plotly.graph_objects as go
from plotly.offline import plot, iplot
import plotly.graph_objs as go
import plotly.offline
plotly.offline.init_notebook_mode(connected=True) 
fig = go.Figure(
    data=[go.Bar(y=LASTd)],
    layout_title_text="A Figure Displayed ConfirmedCases Using data.csv and Plotly"
)
fig.show()




!pwd

#https://www.youtube.com/watch?v=eXpbE5YmXrs days 7-9

!ls COVID-19/csse_covid_19_data/csse_covid_19_daily_reports

from matplotlib import pyplot as plt

import numpy as np
LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/04-13-2020.csv"
DataIn = open(LASTFILE).readlines()
cnt=-1
LAT =[]
LON =[]
cases = []
deaths = []
STate = input("What State? ")
for lines in DataIn:
    lines = lines.replace("\n","")

    line = lines.split(",")
    if STate in line[2] and len(line[5])>8 and len(line[6])>4:
        cnt=cnt+1
        if cnt<2:
            print(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
        LAT.append(line[5]) 
        LON.append(line[6])
        cases.append(int(line[7]))
        deaths.append(int(line[8]))
LA = LAT
LO = LON

print("len(LA)",len(LA))
print("len(LO)",len(LO))
LT = np.array(LAT,dtype=np.float)
LG = np.array(LON,dtype=np.float)
print ("max(LT)",max(LT))
print ("min(LT)",min(LT))
print ('max(LG)',max(LG))
print ('min(LG)',min(LG))
print('len(LT)',len(LT))
print('len(LG)',len(LG))

print ("min(cases)",min(cases))
print("max(cases)",max(cases))
print("len(cases)",len(cases))
print("cases",cases)
print("deaths",deaths)

from matplotlib import pyplot as plt

import numpy as np
LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/04-13-2020.csv"
DataIn = open(LASTFILE).readlines()
cnt=-1
LAT =[]
LON =[]
cases = []
deaths = []
STate = input("What State? ")
for lines in DataIn:
    lines = lines.replace("\n","")

    line = lines.split(",")
    if STate in line[2] and len(line[5])>8 and len(line[6])>4:
        cnt=cnt+1
        if cnt<2:
            print(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
        LAT.append(line[5]) 
        LON.append(line[6])
        cases.append(int(line[7]))
        deaths.append(int(line[8]))
LA = LAT
LO = LON

LT = np.array(LAT,dtype=np.float)
LG = np.array(LON,dtype=np.float)
fig = plt.figure(num=None, figsize=(12,10), dpi=80, facecolor='red')
ax = fig.gca()
ax.set_facecolor(('white'))
S=1
Size=[]
for x in cases:
    S=1+(float(x)*.01)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

lgmin= (min(LG))+5
lgmax= (max(LG))-5
ltmin= (min(LT))+5
ltmax= (max(LT))-5


plt.axis([-130,-65,20,55])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="blue")
plt.grid(True)
#plt.text(50,50, "Verticle lines are Longitude, Horizontal lines are Latitude")
text = (50,50, "Verticle lines are Longitude, Horizontal lines are Latitude")
plt.xlabel('This plot is of: '+STate, fontsize=20)
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19', fontsize=16, color="white")
plt.ylabel('The Dot size is relative to the number of cases')
plt.show()

print (min(cases))
print(max(cases))

#LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/04-09-2020.csv"
DataIn = open(LASTFILE).readlines()
cnt=-1
LAT =[]
LON =[]
for lines in DataIn:
    lines = lines.replace("\n","")
    #if cnt<10:print (lines)
    line = lines.split(",")
    if "US" in line[3]:
        cnt=cnt+1
        if cnt<5:print(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
        LAT.append(line[5]) 
        LON.append(line[6])
print(cnt)            

#LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/04-09-2020.csv"
DataIn = open(LASTFILE).readlines()
LAT=[]
LONG=[]
STATES=[]
cases=[]
latNlongNcases=[]
longitude = ""
cnt=0
for line in DataIn:
    line=line.split(",")
    if 'US' in line[3] and "Recovered" not in line:
        cnt=cnt+1
        if "-" not in line[5] and len(line[5])>5 and "-" in line[6] and len(line[6])>5 and int(line[7])>0:    
            text = str(line[1]+' '+line[2]+' '+line[3]+' '+line[4]+' '+line[5]+' '+line[6]+' '+line[7])
            TExt =text.split(" ")
            if len(TExt)==16:TExt = str(line[1]+' '+line[2]+' '+line[3]+' '+line[4]+' '+line[5]+' '+line[6]+' '+line[7])
            if cnt<5:print(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
   
            STATES.append(TExt)
            LAT.append(line[5])
            LONG.append(line[6])
            cases.append(line[7])
            deaths.append(line[8])
            longitude = longitude+line[6]+","
            latNlongNcases.append(TExt)
print("len(STATES)",len(STATES)) 

LA = LAT[:-7]
LO = LONG[:-7]
print("len(LA)",len(LA))
print("len(LO)",len(LO))
print("len(latNlongNcases)",len(latNlongNcases))

from matplotlib import pyplot as plt
import numpy as np
LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)
print (max(LT))
print (min(LT))
print (max(LG))
print (min(LG))

fig = plt.figure(num=None, figsize=(12,10), dpi=80, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#8eda8b'))

plt.axis([-130,-65,20,55])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=1, color="black")
plt.grid(True)

plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
plt.show()

from matplotlib import pyplot as plt
import numpy as np
LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)
print (max(LT))
print (min(LT))
print (max(LG))
print (min(LG))

fig = plt.figure(num=None, figsize=(12,10), dpi=80, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#8eda8b'))

plt.axis([-85.243753, -79.473390, 24.988049, 33.518900])
 
S=1
Size=[]
for x in cases:
    S=1+(float(x)*.01)
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
#LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/04-09-2020.csv"
DataIn = open(LASTFILE).readlines()
LAT=[]
LONG=[]
STATES=[]
cases=[]
latNlongNcases=[]
longitude = ""
cnt=0
for line in DataIn:
    line=line.split(",")
    if 'US' in line[3] and "Recovered" not in line:
        cnt=cnt+1
        if "-" not in line[5] and len(line[5])>5 and "-" in line[6] and len(line[6])>5 and int(line[7])>0:    
            text = str(line[1]+' '+line[2]+' '+line[3]+' '+line[4]+' '+line[5]+' '+line[6]+' '+line[7])
            Text =text.split(" ")
            if len(Text)==16:TExt = str(line[1]+' '+line[2]+' '+line[3]+' '+line[4]+' '+line[5]+' '+line[6]+' '+line[7])
            if cnt<5:print(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
   
            STATES.append(TExt)
            LAT.append(line[5])
            LONG.append(line[6])
            cases.append(line[7])
            longitude = longitude+line[6]+","
            latNlongNcases.append(TExt)
print("len(STATES)",len(STATES)) 

LA = LAT[:-7]
LO = LONG[:-7]
print("len(LA)",len(LA))
print("len(LO)",len(LO))
print("len(latNlongNcases)",len(latNlongNcases))

LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)
print (max(LT))
print (min(LT))
print (max(LG))
print (min(LG))

fig = plt.figure(num=None, figsize=(12,10), dpi=80, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#8eda8b'))

S=1
Size=[]
for x in cases:
    S=1+(float(x)*.01)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

plt.axis([-130,-65,20,55])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="black")
plt.grid(True)

plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
plt.show()


DataIn = open(LASTFILE).readlines()
LAT=[]
LONG=[]
STATES=[]
cases=[]
latNlongNcases=[]
longitude = ""
cnt=0
for line in DataIn:
    line=line.split(",")
    if 'US' in line[3] and "Recovered" not in line:
        cnt=cnt+1
        if "-" not in line[5] and len(line[5])>5 and "-" in line[6] and len(line[6])>5 and int(line[7])>0:    
            text = str(line[1]+' '+line[2]+' '+line[3]+' '+line[4]+' '+line[5]+' '+line[6]+' '+line[7])
            Text =text.split(" ")
            if len(Text)==16:TExt = str(line[1]+' '+line[2]+' '+line[3]+' '+line[4]+' '+line[5]+' '+line[6]+' '+line[7])
            if cnt<5:print(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
   
            STATES.append(TExt)
            LAT.append(line[5])
            LONG.append(line[6])
            cases.append(line[7])
            longitude = longitude+line[6]+","
            latNlongNcases.append(TExt)

LA = LAT[:-7]
LO = LONG[:-7]

LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)

ffig = plt.figure(num=None, figsize=(12,10), dpi=80, facecolor='red')
ax = fig.gca()


plt.axis([-130,-65,20,55])
ax.grid(color='blue', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=1, color="blue")
plt.grid(True)

plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
plt.show()

from matplotlib import pyplot as plt
import numpy as np
import time

DataIn = open(LASTFILE).readlines()
LAT=[]
LONG=[]
STATES=[]
cases=[]
latNlongNcases=[]
longitude = ""
cnt=0
for line in DataIn:
    line=line.split(",")
    if 'US' in line[3] and "Recovered" not in line:
        cnt=cnt+1
        if "-" not in line[5] and len(line[5])>5 and "-" in line[6] and len(line[6])>5 and int(line[7])>0:    
            text = str(line[1]+' '+line[2]+' '+line[3]+' '+line[4]+' '+line[5]+' '+line[6]+' '+line[7])
            Text =text.split(" ")
            if len(Text)==16:TExt = str(line[1]+' '+line[2]+' '+line[3]+' '+line[4]+' '+line[5]+' '+line[6]+' '+line[7])
            if cnt<5:print(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
   
            STATES.append(TExt)
            LAT.append(line[5])
            LONG.append(line[6])
            cases.append(line[7])
            longitude = longitude+line[6]+","
            latNlongNcases.append(TExt)
print("len(STATES)",len(STATES)) 

LA = LAT[:-7]
LO = LONG[:-7]
print("len(LA)",len(LA))
print("len(LO)",len(LO))
print("len(latNlongNcases)",len(latNlongNcases))

LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)
print (max(LT))
print (min(LT))
print (max(LG))
print (min(LG))

fig = plt.figure(num=None, figsize=(12,10), dpi=80, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#8eda8b'))
#ax.set_facecolor(('white'))
plt.axis([-130,-65,20,55])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=1, color="black")
plt.grid(True)

plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
plt.show()


# https://www.latlong.net/c/?lat=44.40000&long=-95.0000

cnt=0
Longitude = longitude.split(",")
for long in Longitude:
    cnt=cnt+1
    if "-" not in long:print(long)


cnt=0
for line in LONG:
    cnt=cnt+1
    if float(line)<-150:
        print(cnt,line)


line = -82.46170658  
if float(line)<=-82 and float(line)>=-82.6170658:
    print(True)

!ls /home/jack/fonts/DancingScript-Bold.ttf

from matplotlib.pyplot import text
help(text)

from matplotlib import pyplot as plt
from matplotlib.pyplot import text
import numpy as np
DataIn = open(LASTFILE).readlines()
cnt=-1
LAT =[]
LON =[]
cases = []
#STate = input("What State? ")
STate = 'Florida'
for lines in DataIn:
    lines = lines.replace("\n","")

    line = lines.split(",")
    if STate in line[2] and len(line[5])>8 and len(line[6])>4:
        cnt=cnt+1
        if cnt<5:print(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
        LAT.append(line[5]) 
        LON.append(line[6])
        cases.append(int(line[7]))
LA = LAT
LO = LON

print("len(LA)",len(LA))
print("len(LO)",len(LO))
LT = np.array(LAT,dtype=np.float)
LG = np.array(LON,dtype=np.float)
print ("max(LT)",max(LT))
print ("min(LT)",min(LT))
print ('max(LG)',max(LG))
print ('min(LG)',min(LG))
print('len(LT)',len(LT))
print('len(LG)',len(LG))

fig = plt.figure(num=None, figsize=(12,12), dpi=80, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#c2efc1'))

S=1
Size=[]
for x in cases:
    S=1+(float(x)*.1)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

print (min(LG))
print (max(LG))
print (min(LT))
print (max(LT))


longLeft= (min(LG))-3
longRight = (max(LG))+3
lat1 = (min(LT))-3
lat2 = (max(LT))+3

ax = fig.gca()
T= 'Miami-Dade'
text(0.68, 0.29, T, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

#if float(line[6])<=-87 and float(line[6])>=-89:
#                if float(line[5])>42 and float(line[5])<44:
#font="/home/jack/fonts/DancingScript-Bold.ttf"
#-90 and float(line[6])>-92 and float(line[5])<40 and float(line[5])<42
#plt.axis([-100,-70,30,45])
plt.axis([longLeft,longRight,lat1,lat2])
#plt.axis([-80,-90,40,45])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="black")
plt.grid(True)
#plt.text(2, 0.65, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
#text(20, 40, r'$\cos(2 \pi t) \exp(-t)$')
plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
plt.show()

LA = LAT
LO = LONG
print(len(LA))
print(len(LO))


for lo in LO:
    if float(lo)<40:
        print(lo)

import numpy as np
def reject_outliers(data, m=2):
    return data[abs(data - np.mean(data)) < m * np.std(data)]

la = np.array(LA).astype(np.float)
cl = reject_outliers(la, m=3)

lo = np.array(LO).astype(np.float)
clo = reject_outliers(lo, m=1)

print(len(cl))
print(len(clo))


print (min(LG))
print (max(LG))
print (min(LT))
print (max(LT))

!ls csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv

!ls COVID-19/csse_covid_19_data/csse_covid_19_time_series/

from matplotlib import pyplot as plt
from matplotlib.pyplot import text
import numpy as np
#LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"
DataIn = open(LASTFILE).readlines()
#SEARCH = input("SEARCH: ")
SEARCH = "California"
cnt = 0
PHcases = [] 
counts=[]
for line in DataIn:
    cnt=cnt+1
    line=line.lstrip(",")
    line=line.lstrip(" ")
    if SEARCH in line:
        print(line[23:])
        entries = line[23:].split(",")
        for entry in entries:
            print (entry, end= " ")
            #PHcases.append(int(entry))

y=len(PHcases)
Y= range(0,y)
V = np.array(Y)
H = np.array(PHcases)

fig = plt.figure(num=None, figsize=(10,8), dpi=80, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

S=1
Size=[]
for x in PHcases:
    S=1+(float(x)*.1)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)


ax.grid(color='lightgray', linestyle='-', linewidth=1)
#plt.scatter(V, H, s=s)
plt.scatter(V, H, s=s)
plt.grid(True)

plt.xlabel('Philipine COVID-Cases Plot')
plt.title('JupyterJones  ;  CSSEGISandData-COVID-19_GitHub')
plt.ylabel('Number of Cases')
plt.show()

# Query the data by location

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(y=PHcases))
fig.add_trace(go.Bar(y=PHcases))
fig.update_layout(title = 'Philippines Confirmed Cases')
fig.show()

print(PHcases) 

import numpy as np
x = np.asarray(PHcases)
print("-----------------")
print (len(x))
print("-----------------")
cntTOTAL = range(0,len(x))
print (cntTOTAL)
y = np.asarray(cntTOTAL)
print("-----------------")   
for num in cntTOTAL:
    print (num, end=" ")
print("\n-----------------")    
print (y) 
print("\n------- These bottom two number must match ----------")   
print("How many numbers to use for x co-ordinates: ",len(x))
print("How many numbers to use for y co-ordinates: ",len(y))

import plotly.express as px
import plotly.graph_objects as go
from matplotlib import pyplot as plt
import numpy as np
#LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
DataIn = open(LASTFILE).readlines()
#SEARCH = input("SEARCH: ")
SEARCH = "Philippine"
cnt = 0
PHcases = [] 
counts=[]
for line in DataIn:
    cnt=cnt+1
    line=line.lstrip(",")
    if SEARCH in line:
        print(line[23:])
        entries = line[23:].split(",")
        for entry in entries:
            print (entry, end= " ")
            PHcases.append(int(entry))


y=len(PHcases)
Y= range(0,y)
V = np.array(Y)
fig = go.Figure()
#fig.add_trace(go.Scatter(y=PHcases))
fig.add_trace(go.Bar(y=PHcases))
fig.update_layout(title = 'Plotly Bar Graph of Philippine Confirmed COVID-19 Cases')
fig.show()

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(y=PHcases))
fig.add_trace(go.Bar(y=PHcases))
fig.update_layout(title = 'Philippine Confirmed COVID-19 Cases')
fig.show()

from matplotlib import pyplot as plt
import numpy as np
LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
DataIn = open(LASTFILE).readlines()
#SEARCH = input("SEARCH: ")
SEARCH = "Philippine"
cnt = 0
PHcases = [] 
counts=[]
for line in DataIn:
    cnt=cnt+1
    line=line.lstrip(",")
    if SEARCH in line:
        print(line[23:])
        entries = line[23:].split(",")
        for entry in entries:
            print (entry, end= " ")
            PHcases.append(int(entry))


y=len(PHcases)
Y= range(0,y)
V = np.array(Y)
H = np.array(PHcases)

fig = plt.figure(num=None, figsize=(12,10), dpi=80, facecolor='#c81025')
#fig = plt.figure()
ax = fig.gca()

T= '3246\n Cases'
text(0.8, 0.9, T, fontsize= 16, color="white", horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

ax.set_facecolor(('#0036a3'))

S=1
Size=[]
for x in PHcases:
    S=1+(float(x)*.1)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(V, H, s=s, color="Yellow")
plt.grid(True)

plt.xlabel('Philipine COVID-Cases Plot')
plt.title('JupyterJones  ;  CSSEGISandData-COVID-19_GitHub')
plt.ylabel('Number of Cases')
plt.show()

# Query the data by location            

from matplotlib import pyplot as plt
import numpy as np
LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
DataIn = open(LASTFILE).readlines()
SEARCH = input("SEARCH: ")
#SEARCH = "Mexico"
cnt = 0
PHcases = [] 
counts=[]
for line in DataIn:
    cnt=cnt+1
    line=line.lstrip(",")
    if SEARCH in line:
        #print(line[23:])
        entries = line[23:].split(",")
        for entry in entries:
            if entry.isdigit(): 
                print (entry, end= " ")
                PHcases.append(int(entry))


y=len(PHcases)
Y= range(0,y)
V = np.array(Y)
H = np.array(PHcases)


fig = plt.figure(num=None, figsize=(12,10), dpi=80, facecolor='#c81025')
#fig = plt.figure()
ax = fig.gca()

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#0036a3'))

S=1
Size=[]
for x in PHcases:
    S=3+(float(x)*.08)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)


ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(V, H, s=s, color="Yellow")
plt.grid(True)

plt.xlabel('Philipine COVID-Cases Plot')
plt.title('JupyterJones  ;  CSSEGISandData-COVID-19_GitHub')
plt.ylabel('Number of Cases')
plt.show()

# Query the data by location            

from matplotlib import pyplot as plt
import numpy as np
LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
DataIn = open(LASTFILE).readlines()
#SEARCH = input("SEARCH: ")
#SEARCH = "Mexico"
SEARCH = "Bangladesh"
cnt = 0
PHcases = [] 
counts=[]
for line in DataIn:
    cnt=cnt+1
    line=line.lstrip(",")
    if SEARCH in line:
        #print(line[23:])
        entries = line[23:].split(",")
        for entry in entries:
            if entry.isdigit(): 
                print (entry, end= " ")
                PHcases.append(int(entry))


y=len(PHcases)
Y= range(0,y)
V = np.array(Y)
H = np.array(PHcases)


fig = plt.figure(num=None, figsize=(12,10), dpi=80, facecolor='#c81025')
#fig = plt.figure()
ax = fig.gca()

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('DarkGreen'))

S=1
Size=[]
for x in PHcases:
    S=3+(float(x)*.08)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)


ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(V, H, s=s, color="white")
plt.grid(True)

plt.xlabel('Philipine COVID-Cases Plot')
plt.title('JupyterJones  ;  CSSEGISandData-COVID-19_GitHub')
plt.ylabel('Number of Cases')
plt.show()

# Query the data by location            

LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
DataIn = open(LASTFILE).readlines()
#SEARCH = input("SEARCH: ")
SEARCH = "Philippine"
PHcases = ''
PHdeaths = ''
cnt = 0
CNTS=0
counts=[]
for line in DataIn:
    cnt=cnt+1
    line=line.lstrip(",")
    if SEARCH in line:
        print("Cases: ",line)
        PHcases=PHcases+line   
        
LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
DataIn = open(LASTFILE).readlines()
cnt = 0
CNTS=0
counts=[]
for line in DataIn:
    cnt=cnt+1
    line=line.lstrip(",")
    if SEARCH in line:
        print("Deaths: ",line)        
        PHdeaths=PHdeaths+line 
        
        


LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
DataIn = open(LASTFILE).readlines()
#SEARCH = input("SEARCH: ")
#SEARCH = "Canada"
SEARCH = "Ontario"
PHcases = ""
PHdeaths = ""
Pc =[]
Pd =[]
cnt = 0
CNTS=0
counts=[]
for line in DataIn:
    cnt=cnt+1
    line=line.lstrip(",")
    if SEARCH in line:
        print("PHcases: ",line)
        PHcases=PHcases+line
        print("len(PHcases)",len(line))

print("\n---------------------------------------------\n")
        
LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
DataIn = open(LASTFILE).readlines()
cnt = 0
CNTS=0
counts=[]
for line in DataIn:
    cnt=cnt+1
    line=line.lstrip(",")
    if SEARCH in line:
        print("PHdeaths: ",line)
        PHdeaths=PHdeaths+line
        print("len(PHdeaths)",len(line))
        
for entry in PHcases.split(","):
    Pc.append(entry)
print("len(Pc)",len(Pc))    

for entry in PHdeaths.split(","):
    Pd.append(entry)
print("len(Pd)",len(Pd))    

        
     

line="""Recovered,Canada,0.0,0.0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"""
END=len(line.split(","))
print (END)
Data=line.split(",")
print (Data)
print("\n-----  Data[:-1]  ------ Minus the \\n  ----------------")
print (Data[:-1])
print("\n---------------------------")
# Remove 'Recovered', 'Canada' and Minus the \n
print (Data[2:-1])


LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
DataIn = open(LASTFILE).readlines()
#SEARCH = input("SEARCH: ")
#SEARCH = "Canada"
SEARCH = "Ontario"
PHcases = ""
PHdeaths = ""
Pc =[]
Pd =[]
cnt = 0
CNTS=0
counts=[]
for line in DataIn:
    cnt=cnt+1
    line=line.lstrip(",")
    if SEARCH in line:
        print("PHcases: ",line)
        PHcases=PHcases+line
        print("len(PHcases)",len(line))

print("\n---------------------------------------------\n")
        
LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
DataIn = open(LASTFILE).readlines()
cnt = 0
CNTS=0
counts=[]
for line in DataIn:
    cnt=cnt+1
    line=line.lstrip(",")
    if SEARCH in line:
        print("PHdeaths: ",line)
        PHdeaths=PHdeaths+line
        print("len(PHdeaths)",len(line))
        
PHcases=PHcases[32:-1]
for entry in PHcases.split(","):
    Pc.append(int(entry))
print("len(Pc)",len(Pc))
print("Pc",Pc)

PHdeaths=PHdeaths[32:-1]
for entry in PHdeaths.split(","):
    Pd.append(int(entry))
print("len(Pd)",len(Pd))    
print("Pd",Pd)

fig = plt.figure(num=None, figsize=(12,10), dpi=80, facecolor='#c81025')
#fig = plt.figure()
ax = fig.gca()

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#0036a3'))


x=range(0,len(Pc))
print (len(x))

X = np.array(Pc)
Y = np.array(Pd)


SizeC=[]
SizeC.append(2)
for sizec in X:
    Sc=2+(float(sizec))*.05
    SizeC.append(int(Sc))

SizeD=[]
SizeD.append(2)
for sized in Y:
    Sd=2+(float(sized))*.5
    SizeD.append(int(Sd))    
    

sc = np.array(SizeC)
sd = np.array(SizeD)

ax.grid(color='lightgray', linestyle='-', linewidth=1)
#plt.scatter(Y, X, s=s, color="white")
plt.scatter(x, X, s=sc, color="white")
plt.scatter(x, Y, s=sd, color="Yellow")
plt.grid(True)

plt.xlabel('Philipine COVID-Cases Plot')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
plt.show()

print(Pc)
print(Pd)

print(PHcases[32:])



# ESTIMATE from 895 to 1163

span = 6
end = span-1
span=int(span)
for x in range(span,len(PHC)-end): 

    phd = PHD[x];phc=PHC[x-span]
    phd =int(phd);phc=int(phc)
    try:
        res=phd/phc
        print(round(res,3))
    except:
        pass

print(PHD[2])



PHD = list(map(int, PHD))

len(PHcases),len(PHdeaths)

!ls csse_covid_19_data/csse_covid_19_time_series/

LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
DataIn = open(LASTFILE).readlines()
SEARCH = input("SEARCH: ")
cnt = 0
CNTS=0
counts=[]
for line in DataIn:
    cnt=cnt+1
    line=line.lstrip(",")
    if SEARCH in line:print(line)

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(y=counts))
fig.add_trace(go.Bar(y=counts))
fig.update_layout(title = 'Philippines CONDID-19 Cases')
fig.show()

LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
DataIn = open(LASTFILE).readlines()
#SEARCH = input("SEARCH: ")
cnt = 0
CNTS=0
deaths=[]
for line in DataIn:
    cnt=cnt+1
    if cnt ==227:
        print (cnt,line)
        
        line=line.replace("\n","")
        line = line.split(",")
        for item in line:
            CNTS=CNTS+1
            if CNTS>4:
                #print(item)
                deaths.append(item) 
print(len(counts))                 

LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
DataIn = open(LASTFILE).readlines()
#SEARCH = input("SEARCH: ")
cnt = 0
CNTS=0
cases=[]
for line in DataIn:
    cnt=cnt+1
    if cnt ==227:
        print (cnt,line)
        
        line=line.replace("\n","")
        line = line.split(",")
        for item in line:
            CNTS=CNTS+1
            if CNTS>4:
                #print(item)
                cases.append(item) 
print(len(cases))                 

print(int(cases[6]))

from __future__ import division
span = 6
num=len(cases)
print(num)
end=num-span
print(end)
increase = 0
for x in range(span,end):
    d=x+span
    mort = int(deaths[d])/int(cases[x])
    try:
        increase = int(deaths[d])/int(deaths[d+1])
    except:
        pass
    print(x,"Mortality",round(mort,3),"Deaths:",deaths[d],"Confirmed_Cases",cases[x],"Death Increase",increase)
print("\n---------------------------------------------\n")
mortt = mort
yy = x
xx = x
for y in range(yy+1,num):
    mortt=mortt-.002
    print(cases[y]," * ",int(int(cases[y])*mort),int(int(cases[y])*mortt))
for z in range(xx,num):
    #mortt=mortt-.002
    mor=.02
    print(deaths[z]," * ",float(int(deaths[z]))/float(int(deaths[z-1])))    

stat_list = """(170, 'March 29, 2020 at 13:46 GMT, there have been 123828 confirmed cases and 2229 deaths due to coronavirus COVID-19 in the United States')
(171, 'March 29, 2020 at 15:47 GMT, there have been 125099 confirmed cases and 2238 deaths due to coronavirus COVID-19 in the United States')
(172, 'March 29, 2020 at 17:49 GMT, there have been 133146 confirmed cases and 2363 deaths due to coronavirus COVID-19 in the United States')
(173, 'March 29, 2020 at 19:47 GMT, there have been 137943 confirmed cases and 2431 deaths due to coronavirus COVID-19 in the United States')
(174, 'March 29, 2020 at 21:48 GMT, there have been 139904 confirmed cases and 2449 deaths due to coronavirus COVID-19 in the United States')
(175, 'March 29, 2020 at 23:49 GMT, there have been 141781 confirmed cases and 2471 deaths due to coronavirus COVID-19 in the United States')
(176, 'March 30, 2020 at 01:44 GMT, there have been 142004 confirmed cases and 2484 deaths due to coronavirus COVID-19 in the United States')
(177, 'March 30, 2020 at 03:46 GMT, there have been 142735 confirmed cases and 2488 deaths due to coronavirus COVID-19 in the United States')
(178, 'March 30, 2020 at 06:46 GMT, there have been 142735 confirmed cases and 2488 deaths due to coronavirus COVID-19 in the United States')
(179, 'March 30, 2020 at 08:50 GMT, there have been 142735 confirmed cases and 2489 deaths due to coronavirus COVID-19 in the United States')
(180, 'March 30, 2020 at 10:50 GMT, there have been 142746 confirmed cases and 2489 deaths due to coronavirus COVID-19 in the United States')
(181, 'March 30, 2020 at 12:50 GMT, there have been 142793 confirmed cases and 2490 deaths due to coronavirus COVID-19 in the United States')
(182, 'March 30, 2020 at 14:50 GMT, there have been 144410 confirmed cases and 2600 deaths due to coronavirus COVID-19 in the United States')
(183, 'March 30, 2020 at 16:50 GMT, there have been 145542 confirmed cases and 2616 deaths due to coronavirus COVID-19 in the United States')
(184, 'March 30, 2020 at 18:50 GMT, there have been 156565 confirmed cases and 2870 deaths due to coronavirus COVID-19 in the United States')
(185, 'March 30, 2020 at 20:50 GMT, there have been 159689 confirmed cases and 2951 deaths due to coronavirus COVID-19 in the United States')
(186, 'March 30, 2020 at 22:50 GMT, there have been 161358 confirmed cases and 2974 deaths due to coronavirus COVID-19 in the United States')
(187, 'March 31, 2020 at 00:50 GMT, there have been 163479 confirmed cases and 3148 deaths due to coronavirus COVID-19 in the United States')
(188, 'March 31, 2020 at 02:50 GMT, there have been 164253 confirmed cases and 3165 deaths due to coronavirus COVID-19 in the United States.')"""
stat_list = stat_list.split("\n")
for STATS in stat_list:
    STATS=str(STATS)
    STATS =STATS.replace("')","\n")
    STATS =STATS.replace(",","")
    STATS =STATS.replace("'","")
    ITEMS =STATS.replace("(","");STATS =STATS.replace(")","")
    #print(ITEMS)
    item =ITEMS.split(" ")
    print(item[1],item[2],item[3],item[5],item[10],item[14])

var = 1.217670286278381
A=2471*var
print(int(A))
B=A*var
print(int(B))
C=B*var
print(int(C))
D=C*var
print (int(D))
print("----------------")
print(2732.3)
print(3087.7)
print(3443.2)

A=43847*1.317676
print(int(A))
B=A*1.3
print(int(B))
C=B*1.3
print(int(C))
D=C*1.3
print (int(D))

942 Confirmed_Cases 13677 
1209 Confirmed_Cases 19100
1581 Confirmed_Cases 25489
2026 Confirmed_Cases 3327678
2467 

import numpy as np

# the given sequence
data =[
[0, 706.0],
[1, 942.0],
[2, 1209.0],
[3, 1581.0],
[4, 2026.0],
[5, 2467.0],
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
#alpha = 0.01 # learning rate
#iters = 2000 # iterations
alpha = 0.004 # learning rate
iters = 18000 # iterations

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

43847/33276

33276*1.317676403413872

A=43847*1.317676
print(int(A))
B=A*1.3
print(int(B))
C=B*1.3
print(int(C))
D=C*1.3
print (int(D))

span = 6
num=len(cases)
print(num)
end=num-span
print(end)
for x in range(span,end):
    d=x+span
    mort = int(deaths[d])/int(cases[x])
    print(x,"  Mortality",round(mort,3),"   Deaths:",deaths[d],"    Confirmed_Cases",cases[x])
print("\n---------------------------------------------\n")
mortt = mort
for y in range(x+1,num):
    mortt=mortt-.002
    print(cases[y]," * ",int(int(cases[y])*mort),int(int(cases[y])*mortt))

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(y=counts))
fig.add_trace(go.Bar(y=counts))
fig.update_layout(title = 'USA CONDID-19 Cases')
fig.show()

LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
DataIn = open(LASTFILE).readlines()
SEARCH = input("SEARCH: ")
search = str(SEARCH)
for line in DataIn:
    line=line.replace("\n","")
    line = line.split(",")
    if search in line:
        print(" ".join(line))

import plotly.graph_objects as go

fig = go.Figure(go.Scattergeo())
fig.update_geos(
    visible=False, resolution=110, scope="usa",
    showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="Blue"
)
fig.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

import plotly.express as px
df = px.data.gapminder().query("year == 2007")
fig = px.scatter_geo(df, locations="iso_alpha",
                     size="pop", # size of markers, "pop" is one of the columns of gapminder
                     )
fig.show()

!ls csse_covid_19_data/csse_covid_19_time_series/

!ls csse_covid_19_data/csse_covid_19_time_series/

LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
DataIn = open(LASTFILE).readlines()
for line in DataIn:
    print(line)

import os
from pathlib import Path
count=0
bigList=[]
for x in range(1,10):
    X=str(x)
    if len(X)<2:X="0"+X 
    dirpath= "csse_covid_19_data/csse_covid_19_daily_reports/03-"+X+"-2020.csv"
    DataIn = open(dirpath).readlines()
    cnt = 0
    for line in DataIn:
        line=line.replace("\"","")
        line=line.replace("\n","")
        if line[0:1] ==",":
             bigList.append(line[1:]) 
        if line[0:1] !=",":
             if len(line[0:1])<5:
                bigList.append(line)
        
                                    
for line in bigList:
    if "US" in line and "U.S." not in line:
        line = line.split(",")
        line[1]=line[1].lstrip(" ")
        print (line[1],line[2],line[3],line[4],line[5],line[6])

                #print(WORDS)                                                      
#bigList.append(WORDS+"\n")
#print(len(bigList)) 

import time
from shutil import copyfile
filename = "DATA/"+(time.strftime('%a_%d_%b_%Y_%I_%M_%S_%p_%Z_', time.gmtime())+"covid192.db.db")
copyfile("DATA/covid192.db",filename)


!ls DATA/*.db

from shutil import copyfile

!ls csse_covid_19_data/csse_covid_19_daily_reports/

for x in range(10,31):
    X=str(x)
    if len(X)<2:X="0"+X 
    dirpath= "csse_covid_19_data/csse_covid_19_daily_reports/03-"+X+"-2020.csv"

!ls 

import sqlite3
import os
from pathlib import Path
import time
import shutil
import sqlite3


conn=sqlite3.connect("DATA/covid19.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS covid19(data TEXT UNIQUE)")
conn.commit()
conn.close()
#DataBack = "DATA/"+(time.strftime('%a_%d_%b_%Y_%I_%M_%S_%p_%Z_', time.gmtime())+"covid192.db")
#shutil.move("DATA/covid192.db",DataBack)

def GetEpoch(TIMe):
    pattern = '%Y-%m-%dT%H:%M:%S'
    epochs = int(time.mktime(time.strptime(TIMe, pattern)))
    return epochs


count=0
BigList=[]
for x in range(10,31):
    X=str(x)
    if len(X)<2:X="0"+X 
    dirpath= "csse_covid_19_data/csse_covid_19_daily_reports/03-"+X+"-2020.csv"
    DataIn = open(dirpath).readlines()
    cnt = 0
    for line in DataIn:
        line=line.replace("\"","")
        line=line.replace("\n","")
        if line[0:1] ==",":
             BigList.append(line[1:]+"\n") 
        if line[0:1] !=",":    
             BigList.append(line+"\n")
cnt=0
total=0

conn=sqlite3.connect("DATA/covid192.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS covid19(data TEXT UNIQUE)")
conn.commit()


for line in BigList:
    line = line.replace("\n","")
    if "US" in line and "U.S." not in line:
        cnt = cnt+1
        if len(line)>5:
            TXT = line.split(",")
            TIME = (TXT[2])
            if len(TIME)==19:
                cnt=cnt+1
                TIMe = TIME
                epoc=GetEpoch(TIMe)
                if cnt<5:print(TIMe,epoc)
                ENTRY = line+","+str(epoc)
                c.execute("INSERT OR IGNORE into covid19 values (?)",(ENTRY,)) 
print (cnt)        
conn.commit()
conn.close()     

import sqlite3
conn=sqlite3.connect("DATA/covid192.db")
c= conn.cursor()
for row in c.execute('SELECT rowid,* from covid19'):
     print(row[0],row[1])
conn.close()   

!ls -t csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv

LASTFILE="csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
DataIn = open(LASTFILE).readlines()
cnt=0
for Sample in DataIn:
    cnt=cnt+1
    if cnt<5:
        print(Sample.lstrip(","))
cnt = 0
LIST=[]
for line in DataIn:
    line=line.replace("\"","")
    line=line.replace("\n","")
    if line[0:1] ==",":
         LIST.append(line[1:]+"\n") 
    if line[0:1] !=",":    
         LIST.append(line+"\n")
cnt=0
total=0

cnt=0
for line in LIST:
    if cnt==0:
        print (line)
        cnt=cnt+1
    if "US" in line:
        print (line)

import sqlite3
from datetime import datetime
from time import gmtime, strftime
import time
import os
import requests
import glob

!git clone https://github.com/CSSEGISandData/COVID-19

!git pull

!ls csse_covid_19_data/csse_covid_19_daily_reports

conn=sqlite3.connect("DATA/COVID19.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS CORONA(date TEXT, data TEXT UNIQUE)")
# INSERT OR IGNORE into CORONA values (?)",(data,))    
conn.commit()
conn.close()

#['Province/State','Country/Region','Last Update','Confirmed','Deaths','Recovered', 'Latitude', 'Longitude']
import csv
cnt = 0
LIST =[]
LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/03-24-2024.csv"
#LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv"
with open(LASTFILE, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
         LIST.append(lines[0]+","+lines[1]+","+lines[3]+","+lines[4])
         #print (lines)

cases=0
deaths=0
CASES = []
DEATHS = []
count=0
for line in LIST:
    if count==0:print ('{:<2} {:<23} {} {:<6} {} {}'.format(line[1],line[0],"Cases:",line[2],"Deaths:",line[3]))
    if "US" in line and "Virgin Islands" not in line and "Diamond Princess" not in line and 'US,US' not in line:
        line = line.lstrip(" ")
        line = line.split(",")
        count=count+1
        
    
        print ('{:<1} {:<23} {} {:<6} {} {}'.format(line[1],line[0],"Cases:",line[2],"Deaths:",line[3]))
        ENTRY = '{:<1} {:<23} {} {:<6} {} {}'.format(line[1],line[0],"Cases:",line[2],"Deaths:",line[3])
        #print ("ENTRY:",ENTRY)
        cases  = cases  + int(line[2])
        deaths = deaths + int(line[3])
        CASES.append(line[2])
        DEATHS.append(line[3])
        
        
print ("Cases:",  cases)
print ("Deaths:", deaths)

#['Province/State','Country/Region','Last Update','Confirmed','Deaths','Recovered', 'Latitude', 'Longitude']
import csv
cnt = 0
All =[]
LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/03-24-2020.csv"
with open(LASTFILE, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
         All.append(lines[0]+","+lines[1]+","+lines[2]+","+lines[3]+","+\
                    lines[4]+","+lines[5]+","+lines[6]+","+lines[7])

cases=0
deaths=0
CASES = []
DEATHS = []

for line in LIST:
    if "US" in line and "Virgin Islands" not in line and "Diamond Princess" not in line and 'US,US' not in line:
        line = line.lstrip(" ")
        line = line.split(",")
    
        #print ('{:<2} {:<23} {} {:<6} {} {}'.format(line[1],line[0],"Cases:",line[2],"Deaths:",line[3]))
    
        print ('{:<1} {:<23} {} {:<6} {} {}'.format(line[1],line[0],"Cases:",line[2],"Deaths:",line[3]))
        cases  = cases  + int(line[2])
        deaths = deaths + int(line[3])
        CASES.append(line[2])
        DEATHS.append(line[3])
print ("Cases:",  cases)
print ("Deaths:", deaths)


for line in All:
    print (line.lstrip(","))

#['Province/State','Country/Region','Last Update','Confirmed','Deaths','Recovered', 'Latitude', 'Longitude']
import csv
cnt = 0
LIST =[]
LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/03-20-2020.csv"
with open(LASTFILE, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
         LIST.append(lines[0]+","+lines[1]+",   "+lines[3]+",  "+lines[4])
         #print (lines)
for line in LIST:
    print (line.lstrip(","))        

LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/03-20-2020.csv"
DataIn = open(LASTFILE).readlines()
cnt = 0
LIST=[]
for line in DataIn:
    line=line.replace("\"","")
    line=line.replace("\n","")
    cnt=cnt+1
    if cnt <5:
        #if line[0:1] ==",":line.replace(line[0:1],"")
        if line[0:1] ==",":
            LIST.append(line[1:]+"\n") 
        if line[0:1] !=",":    
            LIST.append(line+"\n")
for item in LIST:
    item = item.replace("\n","")
    print (item)

cnt=0
total=0
Total=0
for line in LIST:

    line = line.replace("\n","")
    if "US" in line:
        cnt=cnt+1
        line = line.split(",")
        print (cnt,":",line[0],line[1],"---",line[3],line[4])
        total=total+int(line[4])
        Total=Total+int(line[3])
print ("Confirmed:",Total) 
print ("Deaths:",total)        

!ls -t csse_covid_19_data/csse_covid_19_daily_reports/

files.sort(key=os.path.getctime)

import os
from pathlib import Path
count=0
BigList=[]
for x in range(10,21):
    X=str(x)
    if len(X)<2:X="0"+X 
    dirpath= "csse_covid_19_data/csse_covid_19_daily_reports/03-"+X+"-2020.csv"
    DataIn = open(dirpath).readlines()
    cnt = 0
    for line in DataIn:
        line=line.replace("\"","")
        line=line.replace("\n","")
        if line[0:1] ==",":
             BigList.append(line[1:]+"\n") 
        if line[0:1] !=",":    
             BigList.append(line+"\n")
print(len(BigList)) 

#total=0
#for line in BigList:
#    line = line.replace("\n","")
#    if "US" in line:
#        count = count+1
        #print (count,": ",line)
cnt=0
total=0
for line in BigList:
    line = line.replace("\n","")
    if "US" in line and "U.S." not in line:
        cnt=cnt+1
        line = line.split(",")        
        print ('{:<2} {:<23} {} {:<6} {} {}'.format(line[1],line[0],"Cases:",line[3],"Deaths:",line[4]))
        #ENTRY = '{:<2} {:<23} {} {:<6} {} {}'.format(line[1],line[0],"Cases:",line[3],"Deaths:",line[4])
print ("====================================================================")        
        #total = total + int(line[3])
#print ("Total Cases: ",total)
#print ("Total Cases Minus Cruise Ships: ",total-67)   

import os
from pathlib import Path
for x in range(1,21):
    X=str(x)
    if len(X)<2:X="0"+X 
    dirpath= "csse_covid_19_data/csse_covid_19_daily_reports/03-"+X+"-2020.csv"
    print (dirpath)

LASTFILE

LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/03-19-2020.csv"
DataIn = open(LASTFILE).readlines()
cnt = 0
LIST=[]
for line in DataIn:
    line=line.replace("\"","")
    line=line.replace("\n","")
    if line[0:1] ==",":
         LIST.append(line[1:]+"\n") 
    if line[0:1] !=",":    
         LIST.append(line+"\n")

LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/03-19-2020.csv"
DataIn = open(LASTFILE).readlines()
for Sample in DataIn:
     s=1 
print (Sample.lstrip(","))
cnt = 0
LIST=[]
for line in DataIn:
    line=line.replace("\"","")
    line=line.replace("\n","")
    if line[0:1] ==",":
         LIST.append(line[1:]+"\n") 
    if line[0:1] !=",":    
         LIST.append(line+"\n")
cnt=0
total=0
for line in LIST:
    line = line.replace("\n","")
    if "US" in line:
        cnt = cnt+1
        print (line)            

print (len(LIST))
print (LIST)

import time
def GetEpoch(line):
    TXT = line.split(",")
    text = (TXT[2])
    pattern = '%Y-%m-%dT%H:%M:%S'
    epochs = int(time.mktime(time.strptime(text, pattern)))
    return epochs

line = "New York,US,2020-03-17T22:53:03,1706,13,0,42.1657,-74.9481"
GetEpoch(line)

import time
FullData = []
def GetEpoch(line):
    TXT = line.split(",")
    text = (TXT[2])
    pattern = '%Y-%m-%dT%H:%M:%S'
    epochs = int(time.mktime(time.strptime(text, pattern)))
    return epochs

cnt=0
total=0
for line in LIST:
    line = line.replace("\n","")
    if "US" in line:
        cnt = cnt+1
        #print (cnt,": ",line)
        TXT = line.split(",")
        text = (TXT[2])
        #print (text)
        epoc=GetEpoch(line)
        pattern = '%Y-%m-%dT%H:%M:%S'
        #print (epoc)
        epochs = line+","+str(epoc)
        FullData.append(epochs)
        print (epochs)

# 3,13,2020,03:45,GMT,1747,41
text =arrangedDdata.split("\n")
text= text[1:-1]
EPOCHa=[]
for line in text:
    #print(line)
    #line=str(LINE)
    line = line.split("-")
    #print (str(line[1]+'/'+line[0]+'/'+line[2][:-3]))
    dt = time.strftime((str(line[1]+'/'+line[0]+'/'+line[2][:-3])))
    #print (dt+":00")

    dt_ti = dt+":00"
    #print (dt_ti)
    #03-16-2020 02:48,3777
    pattern = '%d/%m/%Y %H:%M:%S'
    #pattern = '%m/%d/%Y %H:%M:%S'
    epochs = int(time.mktime(time.strptime(dt_ti, pattern)))
    print (dt_ti, epochs)
    EPOCHa.append(int(epochs))    

import os
from pathlib import Path
count=0
BigList=[]
TOTAL = []
for x in range(10,20):
    X=str(x)
    if len(X)<2:X="0"+X 
    dirpath= "csse_covid_19_data/csse_covid_19_daily_reports/03-"+X+"-2020.csv"
    DataIn = open(dirpath).readlines()
    cnt = 0
    for line in DataIn:
        line=line.replace("\"","")
        line=line.replace("\n","")
        if line[0:1] ==",":
             BigList.append(line[1:]+"\n") 
        if line[0:1] !=",":    
             BigList.append(line+"\n")
print(len(BigList)) 

#total=0
#for line in BigList:
#    line = line.replace("\n","")
#    if "US" in line:
#        count = count+1
        #print (count,": ",line)
cnt=0
total=0
for line in BigList:
    Subtotal = 0
    line = line.replace("\n","")
    if "US" in line and "U.S." not in line:
        cnt=cnt+1
        line = line.split(",")
        print ('{:<2} {:<23} {} {:<6} {} {}'.format(line[1],line[0],"Cases:",line[3],"Deaths:",line[4]))
        ENTRY = '{:<2} {:<23} {} {:<6} {} {}'.format(line[1],line[0],"Cases:",line[3],"Deaths:",line[4])
        TOTAL.append(ENTRY)

def Sort(Item): 
    l = len(Item) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (Item[j][1] > Item[j + 1][1]): 
                tempo = Item[j] 
                Item[j]= Item[j + 1] 
                Item[j + 1]= tempo 
    return Item 

#Sort(TOTAL).reverse()    
for item in Sort(TOTAL):
    print (item)
    
  

for num in TOTAL.sort():
    print (num)

COUNTS=[]
cnt=0
total=0
Total=0
for line in BigList:

    line = line.replace("\n","")
    if "US" in line:
        cnt=cnt+1
        line = line.split(",")
        print (cnt,":",line[0],line[1],"---",line[3],line[4])
        if cnt>525 and "Virgin Islands" not in line:
            entry = str(line[3])+"  "+str(line[4])
            COUNTS.append(entry)
            total=total+int(line[4])
            Total=Total+int(line[3])
print ("Confirmed:",Total) 
print ("Deaths:",total)        

cnt=0
total=0
for line in LIST:
    line = line.replace("\n","")
    if "US" in line:
        line=line.split(",")
        cnt = cnt+1
        print (cnt,"; ",line[0],line[1],"   Cases:",line[3],"   Deaths:",line[4])

cnt=0
total=0
for line in LIST:
    line = line.replace("\n","")
    if "US" in line:
        line=line.split(",")
        cnt = cnt+1
        print (cnt,": ",line[0],line[1],"   Cases:",line[3],"   Deaths:",line[4])

#['Province/State','Country/Region','Last Update','Confirmed','Deaths','Recovered', 'Latitude', 'Longitude']
import csv

LIST =[]
#LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/03-29-2020.csv"
with open(LASTFILE, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
        LIST.append(lines[0]+","+lines[1]+","+lines[3]+","+lines[4]+","+lines[5]+","+lines[6]+","+lines[7]+","+lines[8])
    cnt=cnt+1
    print(lines[8])
    if cnt>1 and int(lines[8]) >0:print (line.lstrip(","))
    if cnt==2:print(lines)    
    #if int(line[8]) >0:print (line)
    #if int(line[8]) >0:print (line)
#for line in LIST:
#    print (line)

#['Province/State','Country/Region','Last Update','Confirmed','Deaths','Recovered', 'Latitude', 'Longitude']
import csv
cnt = 0
LIST =[]
#LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv"
with open(LASTFILE, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
         LIST.append(lines[0]+","+lines[1]+","+lines[3]+","+lines[4])
         #print (lines)
cnt=0
total=0
US = []
for line in LIST:
    line = line.replace("\n","")
    if "US" in line and "U.S." not in line:
        cnt=cnt+1
        if len(line)>5:
            print (cnt,line)
            US.append(line)
print ("\n-----------------------------------\n")            
cnt=0
for line in LIST:
    line = line.replace("\n","")
print(line)
print ("\n-----------------------------------\n")  
for line in US:
    line = line.replace("\n","")
    if "US" in line and "U.S." not in line:
        print (line)
        cnt=cnt+1
        if len(line)>5:
            Line = line.split(",") 
            #print ("Line: ",Line)
            #print (Line[0],Line[1],Line[2],Line[3])
            print ('{:<2} {:<23} {} {:<6} {} {}'.format(Line[1],Line[0],"Cases:",Line[2],"Deaths:",Line[3]))
            total = total + int(Line[2])
print ("Total Cases: ",total)
print ("Total Cases Minus Cruise Ships: ",total-67)

import os
from pathlib import Path
count=0
BigList=[]
for x in range(10,20):
    X=str(x)
    if len(X)<2:X="0"+X 
    dirpath= "csse_covid_19_data/csse_covid_19_daily_reports/03-"+X+"-2020.csv"
    DataIn = open(dirpath).readlines()
    cnt = 0
    for line in DataIn:
        line=line.replace("\"","")
        line=line.replace("\n","")
        if line[0:1] ==",":
             BigList.append(line[1:]+"\n") 
        if line[0:1] !=",":    
             BigList.append(line+"\n")
print(len(BigList)) 

#total=0
#for line in BigList:
#    line = line.replace("\n","")
#    if "US" in line:
#        count = count+1
        #print (count,": ",line)
cnt=0
total=0
for line in BigList:
    line = line.replace("\n","")
    if "US" in line and "U.S." not in line:
        cnt=cnt+1
        line = line.split(",")        
        print ('{:<2} {:<23} {} {:<6} {} {}'.format(line[1],line[0],"Cases:",line[3],"Deaths:",line[4]))
        ENTRY = '{:<2} {:<23} {} {:<6} {} {}'.format(line[1],line[0],"Cases:",line[3],"Deaths:",line[4])
print ("====================================================================")        
        #total = total + int(line[3])
#print ("Total Cases: ",total)
#print ("Total Cases Minus Cruise Ships: ",total-67)   

cnt=0
total=0
for line in LIST:
    line = line.replace("\n","")
    if "US" in line:
        cnt=cnt+1
        line = line.split(",")
        print (cnt,":",line[0],line[1],"---",line[2],line[3])
        total=total+ int(line[2])
print ("Total Confirmed: ",total)

cnt=0
total=0
Total=0
for line in LIST:

    line = line.replace("\n","")
    if "US" in line:
        cnt=cnt+1
        line = line.split(",")
        print (cnt,":",line[0],line[1],"---",line[2],line[3])
        total=total+int(line[2])
        Total=Total+int(line[3])
print ("Confirmed:",Total) 
print ("Deaths:",total)        

!ls csse_covid_19_data/csse_covid_19_daily_reports/

DataIn = open("csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv").readlines()
cnt = 0
LIST=[]
for line in DataIn:
    line=line.replace("\"","")
    line=line.replace("\n","")
    cnt=cnt+1
    if cnt <20:
        #if line[0:1] ==",":line.replace(line[0:1],"")
        if line[0:1] ==",":
            print(line[1:]) 
        if line[0:1] !=",":    
            print (line)

print (TEXT)

Taa = TEXT
Ta = LAST

import sqlite3
TEXT = ""
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
for row in c.execute('SELECT rowid,* from CORONA'):
    print (DATAout(row[1]))
    TEXT=TEXT+DATAout(row[1]+"\n")

import datetime
import calendar
cnt =0
text =TEXT.split("\n")
for line in TEXT:
    cnt=cnt+1
    print (cnt,":",line)

import datetime
import calendar
# "28/12/2015 "
text =TEXT.split("\n")
EPOCH=[]
for line in text:
    #print(line)
    #line=str(LINE)
    line = line.split(",")
    dt = time.strftime((str(line[1]+'/'+line[0]+'/'+line[2]+" ")))
    ti = str(line[3]+":00")
    dt_ti = dt + ti
    #print (dt_ti)
    pattern = '%d/%m/%Y %H:%M:%S'
    epoch = int(time.mktime(time.strptime(dt_ti, pattern)))
    print (epoch)
    EPOCH.append(epoch)
print (EPOCH)    

import datetime
import calendar
dt = time.strftime("08/03/2020 ")
ti = "23:30:00"
dt_ti = dt + ti
pattern = '%d/%m/%Y %H:%M:%S'

epoch = int(time.mktime(time.strptime(dt_ti, pattern)))
print (epoch)
# 1450224000

utc_epoch = int(calendar.timegm(time.strptime(dt_ti, pattern)))
print (utc_epoch)

from datetime import datetime

timestamp = 1583681400
dt_object = datetime.fromtimestamp(timestamp)

print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))

import datetime
import calendar
import time
import datetime
import calendar
import time
import sqlite3
from M2D import Month2Num
arrangedDdata = ''
arrangedDdata=arrangedDdata+"date_time,cases\n"
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
for row in c.execute('SELECT rowid,* from CORONA'):
    MISC=row[1]
    Str = MISC.split(" ")
    month = Str[0][0:5]
    OUT = Month2Num(month)+","+MISC[5:15]+" "+MISC[18:24]+":00"
    OUT = OUT.replace(", ","-")
    OUT = OUT.replace("c","")
    #OUT = OUT.replace(",","-")
    OUT = OUT.replace(" ",",");OUT = OUT.replace(",,"," ")
    OUT = OUT.rstrip(",");OUT = OUT.replace(",","") 
    print (OUT) 
    arrangedDdata = arrangedDdata+OUT+"\n"
conn.close() 
#3-15-2020 19:00,3329
# 3,13,2020,03:45,GMT,1747,41
text =arrangedDdata.split("\n")
text= text[1:-1]
EPOCH=[]
for line in text:
    #print(line)
    #line=str(LINE)
    line = line.split("-")
    #print (str(line[1]+'/'+line[0]+'/'+line[2][:-3]))
    dt = time.strftime((str(line[1]+'/'+line[0]+'/'+line[2][:-3])))
    #print (dt+":00")

    dt_ti = dt+":00"
    #print (dt_ti)
    #03-16-2020 02:48,3777
    pattern = '%d/%m/%Y %H:%M:%S'
    #pattern = '%m/%d/%Y %H:%M:%S'
    epochs = int(time.mktime(time.strptime(dt_ti, pattern)))
    print (dt_ti, epochs)
    EPOCH.append(int(epochs))
    

# 3,13,2020,03:45,GMT,1747,41
text =arrangedDdata.split("\n")
text= text[1:-1]
EPOCHa=[]
for line in text:
    #print(line)
    #line=str(LINE)
    line = line.split("-")
    #print (str(line[1]+'/'+line[0]+'/'+line[2][:-3]))
    dt = time.strftime((str(line[1]+'/'+line[0]+'/'+line[2][:-3])))
    #print (dt+":00")

    dt_ti = dt+":00"
    #print (dt_ti)
    #03-16-2020 02:48,3777
    pattern = '%d/%m/%Y %H:%M:%S'
    #pattern = '%m/%d/%Y %H:%M:%S'
    epochs = int(time.mktime(time.strptime(dt_ti, pattern)))
    print (dt_ti, epochs)
    EPOCHa.append(int(epochs))    

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.interpolate import CubicSpline
LAST.reverse()
t = np.array(EPOCH)
#t = np.delete(t, 0)
#t = np.delete(t, 0)
print ('EPOCH',len(t))
#T = np.array(LAST[:-1])
T = np.array(LAST)
#T = np.delete(T,1)
print ('LAST',len(T))
# nearest neighbor
nn_fun = interp1d(t, T, kind='nearest')
# linear
lin_fun = interp1d(t, T, kind='linear')
# cubic spline (uses not-a-knot conditions)
cs_fun = interp1d(t, T, kind='cubic')
# cubic spline (defaults to not-a-knot conditions)
cs_fun2 = CubicSpline(t, T)

tmodel = np.linspace(t.min(), t.max(), 1000)
#fig, ax = plt.subplots(figsize=(10, 6))
fig = plt.figure(figsize=(10, 6),num=1, clear=True)
ax = fig.add_subplot(1,1,1)
ax.plot(t, T, 'ko', label='Data')
ax.plot(tmodel, nn_fun(tmodel), 'r.', label='Nearest', ms=1)
ax.plot(tmodel, lin_fun(tmodel), 'b-', label='Linear')
ax.plot(tmodel, cs_fun(tmodel), 'm-', label='Cubic Spline (nak)')
ax.plot(tmodel, cs_fun2(tmodel), 'y--', label='Cubic Spline* (nak)')
ax.legend()
ax.set(title = 'Generally Using interp1')
fig.savefig('interps1.png')

# cubic spline (defaults to not-a-knot conditions)
cs_fun2_nak = CubicSpline(t, T)
# cubic spline (clamped end conditions: first and last f'=0)
cs_fun2_cla = CubicSpline(t, T, bc_type='clamped')
# cubic spline (clamps first f' to -5 and last f' to 5)
cs_fun2_cla5 = CubicSpline(t, T, bc_type=((1, -5), (1, 5)))
# cubic spline (natural end conditions)
cs_fun2_nat = CubicSpline(t, T, bc_type='natural')
# cubic spline (sets first f'' to -5 and last f'' to 5)
cs_fun2_nat5 = CubicSpline(t, T, bc_type=((2, -5), (2, 5)))
fig = plt.figure(num=2, clear=True)
ax = fig.add_subplot(1,1,1)
ax.plot(t, T, 'ko', label='Data')
ax.plot(tmodel, cs_fun2_nak(tmodel), 'y--', label='Not-a-Knot', ms=1)
ax.plot(tmodel, cs_fun2_cla(tmodel), 'b-', label='Clamped at 0')
ax.plot(tmodel, cs_fun2_cla5(tmodel), 'g--', label='Clamped at $\mp$ 5')
ax.plot(tmodel, cs_fun2_nat(tmodel), 'c--', label='Natural at 0')
ax.plot(tmodel, cs_fun2_nat5(tmodel), 'k--', label='2nd Derivatives at $\mp$ 5')
ax.legend()
ax.set(title = 'Generally Using CubicSpline')
fig.savefig('interps2.png')

%%writefile M2D.py
def Month2Num(month):
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

from M2D import Month2Num
month = 'June'
Month2Num(month)

https://github.com/CSSEGISandData/COVID-19.git

import datetime
import calendar
import time
import datetime
import calendar
import time
import sqlite3
from M2D import Month2Num
arrangedDdata = ''
arrangedDdata=arrangedDdata+"date_time,cases\n"
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
print ('\nThis is frome the current database history. These are the dates of data entry.')
for row in c.execute('SELECT rowid,* from CORONA'):
    MISC=row[1]
    Str = MISC.split(" ")
    month = Str[0][0:5]
    OUT = Month2Num(month)+","+MISC[5:15]+" "+MISC[18:24]+":00"
    OUT = OUT.replace(", ","-")
    OUT = OUT.replace("c","")
    #OUT = OUT.replace(",","-")
    OUT = OUT.replace(" ",",");OUT = OUT.replace(",,"," ")
    OUT = OUT.rstrip(",");OUT = OUT.replace(",","") 
    print (OUT) 
    arrangedDdata = arrangedDdata+OUT+"\n"
conn.close() 
#3-15-2020 19:00,3329
# 3,13,2020,03:45,GMT,1747,41
text =arrangedDdata.split("\n")
text= text[1:-1]
print ("\nThe date is converted to an Epoch / timestamp.")
print("A timestamp is easy to put in sequential order.\n")
EPOCH=[]
for line in text:
    #print(line)
    #line=str(LINE)
    line = line.split("-")
    #print (str(line[1]+'/'+line[0]+'/'+line[2][:-3]))
    dt = time.strftime((str(line[1]+'/'+line[0]+'/'+line[2][:-3])))
    #print (dt+":00")

    dt_ti = dt+":00"
    #print (dt_ti)
    #03-16-2020 02:48,3777
    pattern = '%d/%m/%Y %H:%M:%S'
    #pattern = '%m/%d/%Y %H:%M:%S'
    epochs = int(time.mktime(time.strptime(dt_ti, pattern)))
    print (dt_ti, epochs)
    EPOCH.append(int(epochs))
    

# 3,13,2020,03:45,GMT,1747,41
text =arrangedDdata.split("\n")
text= text[1:-1]
EPOCHa=[]
for line in text:
    #print(line)
    #line=str(LINE)
    line = line.split("-")
    #print (str(line[1]+'/'+line[0]+'/'+line[2][:-3]))
    dt = time.strftime((str(line[1]+'/'+line[0]+'/'+line[2][:-3])))
    #print (dt+":00")

    dt_ti = dt+":00"
    #print (dt_ti)
    #03-16-2020 02:48,3777
    pattern = '%d/%m/%Y %H:%M:%S'
    #pattern = '%m/%d/%Y %H:%M:%S'
    epochs = int(time.mktime(time.strptime(dt_ti, pattern)))
    print (dt_ti, epochs)
    EPOCHa.append(int(epochs))    

import sqlite3
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
for row in c.execute('SELECT rowid,* from CORONA'):
     print (row[0],row[1])
conn.close()        

%%writefile M2D.py
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


from M2D import Month2Num

def DATAout(DATAin):
    data = DATAin.replace(",","")
    data = data.split(" ")
    OutPut = Month2Num(data[0]),data[1],data[2],data[4],data[5],data[9],data[13]
    Output =  ','.join(OutPut)
    return Output
    
    
DATAin ="March 14, 2020 at 16:45 GMT, there have been 2499 confirmed cases and 51 deaths due to coronavirus COVID-19 in the United States."
    
DATAout(DATAin)

import sqlite3
from M2D import Month2Num

def DATAout(DATAin):
    data = DATAin.replace(",","")
    data = data.split(" ")
    OutPut = Month2Num(data[0]),data[1],data[2],data[4],data[5],data[9],data[13]
    Output =  ','.join(OutPut)
    return Output
TEXT = ""
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
for row in c.execute('SELECT rowid,* from CORONA'):
    if len(row[1])>3:
        print (DATAout(row[1]))
        TEXT=TEXT+DATAout(row[1]+"\n")        
conn.close() 

#print (TEXT)

import sqlite3
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
for row in c.execute('SELECT rowid,* from CORONA'):
    #if len(row[1])>5:
    print (row[0],row[1])
    #print (row[1])   
conn.close()        

!ls DATA

!ls -t DATA/*.html

import glob
import os
files = glob.glob('DATA/*.html')
File = max(files, key=os.path.getctime)

print (File)

from time import gmtime, strftime
import time
import os
import glob
files = glob.glob('DATA/*.html') # * means format then *.html
File = max(files, key=os.path.getctime)
print ("Opening: ",File)
print("\n")
DataO = open(File, "r").read()
ndata = DataO.split("<p>")
par = ndata[1]
par=par.replace("<strong>", "")
par=par.replace("</strong>", "")
par=par.replace("</p>", "")
print (par)


#   DATA/Sun_15_Mar_2020_04_47_07_AM_GMT.html

dataout = DataO
dataout = str(dataout)
dataout = dataout.replace("March","\n\n\nXXXXXXXXMarch")
dataout = dataout.replace("<strong>","")
dataout = dataout.replace("</strong>","")
dataout = dataout.replace(">","")
dataout= dataout.split("XXXXXXXX")
data = (dataout[1][0:129])
print (data)

MISC = "March 16, 2020 at 02:48 GMT, there have been 3777 confirmed cases and 69 deaths due to coronavirus COVID-19 in the United States."
print (MISC)
print ("-----------------------")
Str = MISC.split(",")
print (Str)
print ("-----------------------")
print (Str[0][0:5])
print ("-----------------------")

#module to change word-month to number-month   March to 03  April to 04 etc. 
from M2D import Month2Num
month = Str[0][0:5]
OUT = Month2Num(month)+","+MISC[5:15]+MISC[18:24]+MISC[45:50]
OUT = OUT.replace(", ",",")
print (OUT)

conn=sqlite3.connect("DATA/CoronaData.db")
c= conn.cursor()
for row in c.execute('SELECT rowid,* from CORONA'):
    print (row[0],row[1],row[2])
    print (row[3])
    print("----------------------")


import sqlite3
from M2D import Month2Num
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
for row in c.execute('SELECT rowid,* from CORONA'):
    MISC=row[1]
    Str = MISC.split(" ")
    month = Str[0][0:5]
    OUT = Month2Num(month)+","+MISC[5:15]+MISC[18:24]+MISC[45:50]
    OUT = OUT.replace(", ",",")
    OUT = OUT.replace("c","")
    print (OUT) 
conn.close()       

dataout = DataO
dataout = dataout.replace("<p>","XXXX<p>")
dataout =dataout.replace("</p>","</p>XXXX")
paragraph = dataout.split("XXXX")
for line in paragraph:
    if "<p>" in line:
        print (line)
        print ("--------------------")






# c.execute("CREATE TABLE IF NOT EXISTS CORONA(Id integer primary key autoincrement, data TEXT UNIQUE)")

data2="""March 08, 2020 at 23:30 GMT, there have been 537 confirmed cases and 21 deaths due to coronavirus COVID-19 in the United States.
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
March 14, 2020 at 16:15 GMT, there have been 2329 confirmed cases and 50 deaths due to coronavirus COVID-19 in the United States.
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
March 17, 2020 at 21:55 GMT, there have been 6211 confirmed cases and 102 deaths due to coronavirus COVID-19 in the United States
"""

!cp DATA/CoronaData2.db DATA/CoronaData2-bak.db

import sqlite3
data2= ""
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
for row in c.execute('SELECT rowid,* from CORONA'):
    #print (row[0],row[1])
    print (row[1]) 
    data2=data2+row[1]
conn.close()        

data = data2.split(".")
for line in data:
    print (line)

print (1715/1639)
print (1639/1336)
print (1336/1327)
print (1327/1301)

from M2D import Month2Num

def DATAout(DATAin):
    data = DATAin.replace(",","")
    data = data.split(" ")
    OutPut = Month2Num(data[0]),data[1],data[2],data[4],data[5],data[9],data[13]
    Output =  ','.join(OutPut)
    return Output
    
    
experiment ="March 14, 2020 at 16:45 GMT, there have been 2499 confirmed cases and 51 deaths due to coronavirus COVID-19 in the United States."
    
DATAout(experiment)

from M2D import Month2Num

def DATAexperiment(DATAin):
    data = DATAin.replace(",","")
    data = data.split(" ")
    OutPut = Month2Num(data[0])+"/"+data[1]+"/"+data[2]+" "+data[4]+" Cases: "+data[9]+" Deaths: "+data[13]
    #OutPut = Month2Num(data[0])+"/"+data[1]+"/"+data[2]+" "+data[4]+" Cases: "+data[9]
    Output =  ''.join(OutPut)
    return Output
    
    
EXP ="March 14, 2020 at 16:45 GMT, there have been 2499 confirmed cases and 51 deaths due to coronavirus COVID-19 in the United States."
    
DATAexperiment(EXP)

TEXT="""3,08,2020,23:30,GMT,537,21
3,09,2020,04:30,GMT,589,22
3,10,2020,05:30,GMT,708,27
3,10,2020,23:35,GMT,975,30
3,11,2020,04:25,GMT,1010,31
3,15,2020,19:00 GMT,3329,63"""

import sqlite3
from M2D import Month2Num
arrangedDdata = ''
arrangedDdata=arrangedDdata+"date_time,cases\n"
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
for row in c.execute('SELECT rowid,* from CORONA'):
    MISC=row[1]
print ("\n------ MISC=row[1]  results ----------------\n")
print (MISC)
print ("\n----------------------\n")
for row in c.execute('SELECT rowid,* from CORONA'):
    MISC=row[1]
    Str = MISC.split(" ")
    month = Str[0][0:5]
    OUT = Month2Num(month)+","+MISC[5:15]+" "+MISC[18:24]+MISC[45:50]
    OUT = OUT.replace(", ",",")
    OUT = OUT.replace("c","")
    OUT = OUT.replace(",","-")
    OUT = OUT.replace(" ",",");OUT = OUT.replace(",,"," ")
    OUT = OUT.rstrip(",") 
    print (OUT) 
    arrangedDdata = arrangedDdata+OUT+"\n"
conn.close() 
#3-15-2020 19:00,3329

import re
TEST="M^54{-[098(0<uy>{dsjdyh}COVID-19 United States."

name= re.sub('[(),[^{}2<>-]', '', TEST)
print(name)

ndata= TEXT.replace(",","-")
ndata= ndata.replace(" ","-")
Ndata= ndata.split("\n")
arrangedDdata =''

cnt=0
for line in Ndata:
    cnt=cnt+1
    if cnt ==1:arrangedDdata=arrangedDdata+"date_time,cases\n"
    line=line.split("-")
    arrangedDdata=arrangedDdata+str(line[0])+"-"+str(line[1])+"-"+str(line[2])+" "+str(line[3])+","+str(line[5])+"\n"
print (arrangedDdata)

from io import StringIO
import numpy as np
import pandas as pd
from scipy import interpolate
import matplotlib.pyplot as plt
from time import gmtime, strftime
import time
csv = StringIO(arrangedDdata)

print("\nGMT: "+time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()))
df = pd.read_csv(csv, parse_dates=['date_time'], index_col=0)

s = .9
x = df.index.values
y = df.cases.values
xnew = np.arange(x[0], x[-1], np.timedelta64(5, 'm'))
fig, ax = plt.subplots(figsize=(12, 8))
#tck = interpolate.splrep(x, y, k=3, s=s)
tck = interpolate.splrep(x, y, k=4, s=s)
ynew = interpolate.splev(xnew.view(int), tck)

df.cases.plot(marker='o', ls='', label='data')
plt.plot(xnew, ynew, label=f'scipy cubic spline (s={s})')
(df.cases.resample('5min')
               .interpolate(method='spline', order=2, s=s)
               .plot(label=f'pandas cubic spline (s={s})'))
plt.legend();

TXT="""
03-17-2020 10:31,4743
03-17-2020 14:38,4752
03-17-2020 18:41,5723
03-17-2020 21:55,6211
03-17-2020 22:40,6349
03-18-2020 02:20,6499
03-18-2020 06:05,6522
03-18-2020 10:10,6524
03-18-2020 14:15,7301
03-18-2020 18:16,7708
03-18-2020 22:10,8998
03-19-2020 02:17,9371
03-19-2020 10:16,9464
03-19-2020 14:15,9486
03-19-2020 15:15,10692
03-19-2020 18:17,11355
03-19-2020 22:45,13737
03-20-2020 00:48,13865
03-20-2020 02:40,14316
03-20-2020 06:35,14366
03-20-2020 08:10,14366
03-20-2020 10:11,14366
03-20-2020 12:11,14366
03-20-2020 14:10,14373
03-20-2020 16:11,16067
03-20-2020 18:12,16545
03-20-2020 20:12,18121
03-20-2020 22:12,18876
03-21-2020 00:06,19393
03-21-2020 00:25,19429
03-21-2020 02:07,19643
03-21-2020 04:08,19652
03-21-2020 06:05,19774
03-21-2020 08:10,19774
03-21-2020 10:12,19774
"""

from io import StringIO
import numpy as np
import pandas as pd
from scipy import interpolate
import matplotlib.pyplot as plt
from time import gmtime, strftime
import time
csv = StringIO("""
date_time,cases
03-08-2020 23:30,537
03-09-2020 04:30,589
03-10-2020 05:30,708
03-10-2020 23:35,975
03-11-2020 04:25,1010
03-11-2020 15:17,1016
03-11-2020 23:35,1301
03-12-2020 03:25,1327
03-12-2020 11:37,1336
03-12-2020 22:00,1639
03-13-2020 00:05,1715
03-13-2020 01:35,1725
03-13-2020 03:45,1747
03-13-2020 06:00,1762
03-13-2020 15:25,1832
03-13-2020 22:25,2269
03-14-2020 02:40,2291
03-14-2020 16:15,2329
03-14-2020 16:45,2499
03-14-2020 23:03,2836
03-15-2020 05:00,2982
03-15-2020 05:40,2995
03-15-2020 07:05,3043
03-15-2020 19:00,3329
03-15-2020 20:05,3400
03-15-2020 21:15,3621
03-15-2020 22:15,3502
03-16-2020 00:35,3714
03-16-2020 02:48,3777
03-16-2020 05:36,3782
03-16-2020 08:29,3802
03-16-2020 18:40,4186
03-16-2020 22:40,4597
03-17-2020 10:31,4743
03-17-2020 14:38,4752
03-17-2020 18:41,5723
03-17-2020 21:55,6211
03-17-2020 22:40,6349
03-18-2020 02:20,6499
03-18-2020 06:05,6522
03-18-2020 10:10,6524
03-18-2020 14:15,7301
03-18-2020 18:16,7708
03-18-2020 22:10,8998
03-19-2020 02:17,9371
03-19-2020 10:16,9464
03-19-2020 14:15,9486
03-19-2020 15:15,10692
03-19-2020 18:17,11355
03-19-2020 22:45,13737
03-20-2020 00:48,13865
03-20-2020 02:40,14316
03-20-2020 06:35,14366
03-20-2020 08:10,14366
03-20-2020 10:11,14366
03-20-2020 12:11,14366
03-20-2020 14:10,14373
03-20-2020 16:11,16067
03-20-2020 18:12,16545
03-20-2020 20:12,18121
03-20-2020 22:12,18876
03-21-2020 00:06,19393
03-21-2020 00:25,19429
03-21-2020 02:07,19643
03-21-2020 04:08,19652
03-21-2020 06:05,19774
03-21-2020 08:10,19774
03-21-2020 10:12,19774
""")

print("\nGMT: "+time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()))
df = pd.read_csv(csv, parse_dates=['date_time'], index_col=0)

s = 1.2
x = df.index.values
y = df.cases.values
xnew = np.arange(x[0], x[-1], np.timedelta64(5, 'm'))
fig, ax = plt.subplots(figsize=(12, 8))
tck = interpolate.splrep(x, y, k=3, s=s)
ynew = interpolate.splev(xnew.view(int), tck)

df.cases.plot(marker='o', ls='', label='data')
plt.plot(xnew, ynew, label=f'scipy cubic spline (s={s})')
(df.cases.resample('5min')
               .interpolate(method='spline', order=2, s=s)
               .plot(label=f'pandas cubic spline (s={s})'))
plt.legend();

EpochData=""
text =arrangedDdata.split("\n")
text= text[1:-1]
for line in text:
    line = line.split(",")
    print(line[0])
    EpochData=EpochData+line[0]+"\n"

print (EpochData)

import sqlite3
from M2D import Month2Num
arrangedDdata = ''
# The next line will add a header to the data:  date_time,cases
# arrangedDdata=arrangedDdata+"date_time,cases\n"
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
for row in c.execute('SELECT rowid,* from CORONA'):
    MISC=row[1]
    Str = MISC.split(" ")
    month = Str[0][0:5]
    OUT = Month2Num(month)+","+MISC[5:15]+" "+MISC[18:24]+MISC[45:50]
    OUT = OUT.replace(", ","-")
    OUT = OUT.replace("c","")
    #OUT = OUT.replace(",","-")
    OUT = OUT.replace(" ",",");OUT = OUT.replace(",,"," ")
    OUT = OUT.rstrip(",") 
    print (OUT) 
    arrangedDdata = arrangedDdata+OUT+"\n"
conn.close() 
#3-15-2020 19:00,3329

import sqlite3
from M2D import Month2Num
arrangedDdata = ''
arrangedDdata=arrangedDdata+"date_time,cases\n"
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
for row in c.execute('SELECT rowid,* from CORONA'):
    MISC=row[1]
    Str = MISC.split(" ")
    month = Str[0][0:5]
    OUT = Month2Num(month)+","+MISC[5:15]+" "+MISC[18:24]+MISC[45:50]
    OUT = OUT.replace(", ","-")
    OUT = OUT.replace("c","")
    #OUT = OUT.replace(",","-")
    OUT = OUT.replace(" ",",");OUT = OUT.replace(",,"," ")
    OUT = OUT.rstrip(",") 
    print (OUT) 
    arrangedDdata = arrangedDdata+OUT+"\n"
conn.close() 
#3-15-2020 19:00,3329

import sqlite3
from M2D import Month2Num
arrangedDdata = ''
LAST = []
arrangedDdata=arrangedDdata+"date_time,cases\n"
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
for rows in c.execute('SELECT ROWID,* from CORONA'):
    rows=str(rows)
    print (rows)
    row = rows.split(" ")
    #print (row[10])
    LAST.append(row[10])
conn.close() 
#3-15-2020 19:00,3329

import sqlite3
from M2D import Month2Num
arrangedDdata = ''
arrangedDdata=arrangedDdata+"date_time,cases\n"
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
for row in c.execute('SELECT rowid,* from CORONA'):
    MISC=row[1]
    Str = MISC.split(" ")
    month = Str[0][0:5]
    OUT = Month2Num(month)+","+MISC[5:15]+" "+MISC[18:24]+":00"
    OUT = OUT.replace(", ","-")
    OUT = OUT.replace("c","")
    #OUT = OUT.replace(",","-")
    OUT = OUT.replace(" ",",");OUT = OUT.replace(",,"," ")
    OUT = OUT.rstrip(",");OUT = OUT.replace(",","") 
    print (OUT) 
    arrangedDdata = arrangedDdata+OUT+"\n"
conn.close() 
#3-15-2020 19:00,3329

print (OUT)

print (text)

import datetime
import calendar
import time
# 3,13,2020,03:45,GMT,1747,41
text =arrangedDdata.split("\n")
text= text[1:-1]
EPOCHa=[]
for line in text:
    #print(line)
    #line=str(LINE)
    line = line.split("-")
    #print (str(line[1]+'/'+line[0]+'/'+line[2][:-3]))
    dt = time.strftime((str(line[1]+'/'+line[0]+'/'+line[2][:-3])))
    #print (dt+":00")

    dt_ti = dt+":00"
    #print (dt_ti)
    #03-16-2020 02:48,3777
    pattern = '%d/%m/%Y %H:%M:%S'
    #pattern = '%m/%d/%Y %H:%M:%S'
    epochs = int(time.mktime(time.strptime(dt_ti, pattern)))
    print (dt_ti, epochs)
    EPOCHa.append(int(epochs))

print (EPOCHa)
EPOCH= EPOCHa

print (len(EPOCH))
epoch = EPOCH
print (epoch)

print(round(32.671, 2))
print(round(32.676, 2))
print(round(32.678, 2))

print ((1583681400-1583699400)/3600)
print ((1583699400-1583789400)/3600)
print ((1583789400-1583854500)/3600)
number =((1583789400-1583854500)/3600)
print (str(round(number, 2)))
print ((1583854500-1583871900)/3600)
print ((1583871900-1583911020)/3600)
print ((1583911020-1583940900)/3600)
print ((1584398100-1584412260)/3600)
print ((1584412260-1584427080)/3600)
print ((1584427080-1584441660)/3600)
print ((1584441660-1584453300)/3600)
print ((1584453300-1584456000)/3600)



import sqlite3
TEXt = []
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
for row in c.execute('SELECT rowid,* from CORONA'):
    #print (DATAout(row[1]))
    TEXt.append(DATAout(row[1]))      
TExt =str(TEXt)
TX=TExt.split("\n")
for lines in TX:
    print (lines[0:])
print ("\n----------------------------------------")
print (TEXt)    
conn.close()     

import sqlite3
TEXT = ""
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
for row in c.execute('SELECT rowid,* from CORONA'):
    #print (DATAout(row[1]))
    TEXT=TEXT+DATAout(row[1]+"\n")        
conn.close() 
TEXT=TEXT.split("\n")
for lines in TEXT:
    print (lines)

Text =  ' '.join(TEXT)
lines=Text.split("\n")
print (lines)

import sqlite3
TEXT = ""
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
for row in c.execute('SELECT rowid,* from CORONA'):
    print (DATAout(row[1]))
    TEXT=TEXT+DATAout(row[1])

from M2D import Month2Num
import sqlite3
minus=0
out2 =0
DIFF = []

CHANGE = ""
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
for row in c.execute('SELECT rowid,* from CORONA'):
    rows = DATAout(row[1]).split(",")
    out = int(rows[5])-minus
    print ("rowid:",row[0],"      ",out2,"=>",int(rows[5]),"Increase",int(rows[5])-out2)
    DIFF.append(int(rows[5])-out2)
    INT=int(rows[5])-out2
    STR=str(INT)
    CHANGE = CHANGE+STR+"\n"
    out2=out+minus
    

DIFF.reverse()
diff = DIFF

import time
import os
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
#%matplotlib inline 
import numpy as np 

print (DIFF)
#del DIFF[0]
#del DIFF[0]
print (DIFF)
diff = DIFF
#del diff[1]
epoch = EPOCH
#del epoch[1]
#num = [(number/150000)-10500 for number in epoch]
num = epoch
E=len(num)
print ("Epoch Quantity",E)
Time = np.array(num)

E=len(diff)
dif = np.array(diff)
#print (Time[3:], end=" ")
e = len(diff)
print ("DIFF Quantity",e)
ss = range(0,e)
aa = np.array(diff)
Ta = np.array(diff,dtype=np.int)
print(Ta)
s= np.array(num)
figure(num=None, figsize=(10,10), dpi=150, facecolor='salmon')
#fig, ax = plt.subplots(dpi=150)

plt.subplot(2, 1, 1)
plt.plot(Time, Ta, 'blue')
plt.title('Top: Time Relative Plot / Bottom: Relative to number of Samples')
plt.ylabel('Number of Cases')

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from scipy.interpolate import UnivariateSpline
NUM = len(diff)
print(NUM)
x = np.linspace(-3, 3, NUM)
y = np.array(diff,dtype=np.int)
#y = np.exp(-x**2) + 0.1 * np.array(diff,dtype=np.int)
figure(num=None, figsize=(8,5), dpi=100, facecolor='lightblue')
plt.plot(x, y, 'ro', ms=5)

#Use the default value for the smoothing parameter:
spl = UnivariateSpline(x, y)
#xs = np.linspace(-3, 3, 1000)
xs = np.linspace(-3, 3, NUM*2)
plt.plot(xs, spl(xs), 'g', lw=3)

#Manually change the amount of smoothing:
spl.set_smoothing_factor(0.5)
plt.plot(xs, spl(xs), 'b', lw=3)
plt.show()



#from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import scipy.interpolate
#from scipy import interpolate
from scipy import integrate
from scipy import ndimage

y=diff
SM = (len(diff))
print ("len_SM",len(diff))
x = np.linspace(1 ,20,len(y))

# convert both to arrays
x_sm = np.array(x)
print ("x_sm",len(x_sm))
y_sm = np.array(y)
print ("y_sm",len(y_sm))
# resample to lots more points - needed for the smoothed curves
x_smooth = np.linspace(x_sm.min(), x_sm.max(), SM)

# spline - always goes through all the data points x/y
y_spline = interpolate.SmoothBivariateSpline(x, y, x_smooth)

spl = interpolate.UnivariateSpline(x, y)

sigma = 2
x_g1d = ndimage.gaussian_filter1d(x_sm, sigma)
y_g1d = ndimage.gaussian_filter1d(y_sm, sigma)
figure(num=None, figsize=(8,5), dpi=100, facecolor='lightblue')
#fig, ax = plt.subplots(figsize=(10, 6))
#ax.legend(loc='center left', bbox_to_anchor=(1.05, 0.5), frameon=False)

plt.plot(x_sm, y_sm, 'green', linewidth=1)
plt.plot(x_smooth+.2, spl(x_smooth)-15, 'blue', linewidth=1)
plt.plot(x_g1d,y_g1d, 'magenta', linewidth=1)

plt.show()

for line in LAST:
    print (line, end=" ")
LAST.reverse() 
print ("\n-----------------------------------")
for line in LAST:
    print (line, end=" ")
    
LAST.reverse()     

import numpy as np 
epoch = EPOCH
num = [(number/150000)-1050 for number in epoch]
E=len(num)
print (E)
Time = np.array(num)
for num in Time:
    print (num, end=" ")

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
epoch = EPOCH
num = [(number/150000)-10500 for number in epoch]
E=len(num)
print ("len(num)",E)
Time = np.array(num)
e = len(LAST)
print ("len(LAST)",e)
print (Time[3:], end=" ")

ss = range(0,e)
aa = np.array(LAST)
#del LAST[0]
Ta = np.array(LAST,dtype=np.int)
print("Ta",Ta)
s= np.array(LAST)
figure(num=None, figsize=(10,10), dpi=80, facecolor='salmon')
#fig, ax = plt.subplots(dpi=150)


plt.subplot(2, 1, 1)
plt.plot(Time, Ta, 'blue')
plt.title('Top: Time Relative Plot / Bottom: Relative to number of Samples')
plt.ylabel('Number of Cases')


plt.subplot(2, 1, 2)
plt.plot(s, Ta, 'red')
plt.xlabel('time (s)')
plt.ylabel('Number of Samples')

plt.show()



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
EPOCH2 = [number/1500 for number in EPOCH]
#EPOCH = [number*.002 for number in EPOCH]
E=len(EPOCH2)
print (E)
Time = np.array(EPOCH2)
print (Time[3:], end=" ")
e = len(LAST)
print (e)
ss = range(0,e)
aa = np.array(LAST)
Ta = np.array(LAST,dtype=np.int)
print(Ta)
s= np.array(LAST)
figure(num=None, figsize=(10,10), dpi=80, facecolor='salmon')
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

E=len(EPOCH)
print (E)
Time = np.array(EPOCH)
print (Time[3:], end=" ")
e = len(LAST)
print (e)
ss = range(0,e)
aa = np.array(LAST)
Ta = np.array(LAST,dtype=np.int)
print(Ta)
s= np.array(LAST)
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
E=len(EPOCH)
print (E)
Time = np.array(EPOCH)
print (Time[3:], end=" ")
e = len(LAST)
print (e)
ss = range(0,e)
aa = np.array(LAST)
Ta = np.array(LAST,dtype=np.int)
print(Ta)
s= np.array(LAST)
fig, ax = plt.subplots(dpi=100, facecolor='salmon')
#figure(num=None, figsize=(10,8), dpi=80, facecolor='salmon')
#ax.plot(s, Ta)
#ax.plot(Time-15800000, Ta)
ax.plot(Time, Ta)
DT = time.strftime("%Y-%m-%d:%H")
ax.set(xlabel='DATE: '+DT)
ax.grid()
tm = time.strftime("%Y-%m%d%H%M%S")
Filename = tm+".png"
print (Filename)
fig.savefig(Filename)
plt.show()


import sqlite3
from M2D import Month2Num
arrangedDdata = ''
LAST = []
arrangedDdata=arrangedDdata+"date_time,cases\n"
conn=sqlite3.connect("DATA/CoronaData2.db")
c= conn.cursor()
for rows in c.execute('SELECT * from CORONA'):
    rows=str(rows)
    row = rows.split(" ")
    print (row[9])
    LAST.append(row[9])
conn.close() 
#3-15-2020 19:00,3329

from __future__ import division
import sys
import glob
import time
import os
import matplotlib
import matplotlib.pyplot as plt
#%matplotlib inline 
import numpy as np 
CHANGEca = LAST
#del EPOCH[0]
Time = np.array(EPOCH)
#del CHANGEca[0]

#CHANGEca.reverse()
T = len(Time)
print ("len(Time)",T,"\n")


e = len(CHANGEca)
print ("len(CHANGEca)",e)
ss = range(0,e)
TaX = np.array(CHANGEca,dtype=np.float)
print("len(TaX)",len(TaX),"\n")
print(TaX)

sX= np.array(CHANGEca)
fig, ax = plt.subplots(dpi=100)
ax.plot(Time, TaX)
DT = time.strftime("%Y-%m-%d:%H")
ax.set(xlabel='DATE: '+DT)
ax.grid()
tm = time.strftime("%Y-%m%d%H%M%S")
Filename = tm+".png"
print (Filename)
fig.savefig(Filename)
plt.show()




from __future__ import division
import sys
import glob
import time
import os
import matplotlib
import matplotlib.pyplot as plt
#%matplotlib inline 
import numpy as np 
LAST.reverse()
e = len(LAST)
print (e)
ss = range(0,e)
Taa = np.array(LAST,dtype=np.int)
print(Taa)
fig, ax = plt.subplots(dpi=100)
ax.plot(ss, Taa)
DT = time.strftime("%Y-%m-%d:%H")
ax.set(xlabel='DATE: '+DT)
ax.grid()
tm = time.strftime("%Y-%m%d%H%M%S")
Filename = tm+"_.png"
print (Filename)
fig.savefig(Filename)
plt.show()


!chmod +x TestCorona

# %load TestCorona
#!/home/jack/miniconda3/bin/python
def some_job():
    import requests
    from time import gmtime, strftime
    import time
    print ("TEMPDATA/"+strftime("%d-%m-%Y_%H:%M:%S",gmtime())+".html")
    filename = "TEMPDATA/"+strftime("%d-%m-%Y_%H:%M:%S",gmtime())+".html"
    DataIn = open(filename,"w")
    listTEXT = []
    stringTEXT = ""
    response = requests.get('https://www.worldometers.info/coronavirus/country/us/')
    DATA = str(response.content)
    listTEXT.append(DATA)
    stringTEXT = stringTEXT+DATA
    DataIn.write(str(listTEXT))
    DataIn.close()
    print(filename)
some_job()   


import matplotlib
import numpy as np
import mpld3
import matplotlib.pyplot as plt
from PIL import Image
from mpld3 import plugins
%matplotlib inline
fig, ax = plt.subplots()
im = np.array(Image.open('mouse-sizing-n-cropping-files/soil600.jpg'))
# Default shows the image upside down [::-1] flips the image
#im = im[::-1]
plt.imshow(im)
plugins.connect(fig, plugins.MousePosition(fontsize=14))


mpld3.display()

from matplotlib import pyplot as plt
import numpy as np
import mpld3
from mpld3 import plugins
%matplotlib inline
LA = LAT[:-8]
LO = LONG[:-8]

print(len(LA))
print(len(LO))

LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)
print (max(LT))
print (min(LT))
print (max(LG))
print (min(LG))

fig = plt.figure(num=None, figsize=(12,10), dpi=80, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#8eda8b'))

S=1
Size=[]
for x in cases:
    S=1+(float(x)*.01)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

plt.axis([-130,-65,20,55])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="black")
plt.grid(True)

plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
plt.show()
#plugins.connect(fig, plugins.MousePosition(fontsize=14))


#mpld3.display()



from DTE import Date2Epoch
Date = "31 March 2020 02:48"
Date2Epoch(Date,last=1583621400)

!pwd

#LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/04-02-2020.csv"
#LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/04-13-2020.csv"
DataIn = open(LASTFILE).readlines()
LAT=[]
LONG=[]
CITY=[]
cases=[]
TEXT=[]
cnt = -1
Total=0
for line in DataIn:
    cnt=cnt+1
    line=line.replace("\n","")
    line = line.lstrip(",")
    line = line.split(",")
    End=len(line)-1
    #print(line[2])
    if len(line)>5 and "Florida" in line[6] and "Out of FL" not in line:
        print(line[5],line[6],line[8],line[9], line[End] )
        Total=Total+int(line[End])
        CITY.append(line[5])
        LAT.append(line[8])
        LONG.append(line[9])
        cases.append(line[End])        
        text = str(line[2]+' '+line[1]+' '+line[3]+' '+line[4]+' '+line[5]+' '+line[6]+' '+line[7]+' '+line[8]+' '+line[9]+' '+line[10])
        TEXT.append(text)
            
print("Number of Cities: ",len(CITY)) 
print("Total Deaths: ",Total)

from matplotlib import pyplot as plt
import numpy as np
import mpld3
from mpld3 import plugins
%matplotlib inline

#LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/04-13-2020.csv"
LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
#LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"
DataIn = open(LASTFILE).readlines()
LAT=[]
LONG=[]
CITY=[]
cases=[]
TEXT=[]
cnt = -1
Total=0
for line in DataIn:
    if len(line)>10 and 'US' in line and "Recovered" not in line and "Unassigned" not in line:
        cnt=cnt+1
        line=line.replace("\n","")
        line = line.lstrip(",")
        line = line.split(",")
        End=len(line)-1
        if len(line)>5 and "Florida" in line[6] and "Out of FL" not in line:
            if cnt==1:print(line[5],line[6],line[8],line[9], line[End] )
            Total=Total+int(line[End])
            CITY.append(line[5])
            LAT.append(line[8])
            LONG.append(line[9])
            cases.append(line[End])        
            text = str(line[2]+' '+line[1]+' '+line[3]+' '+line[4]+' '+line[5]+' '+line[6]+' '+line[7]+' '+line[8]+' '+line[9]+' '+line[10])
            TEXT.append(text)
            
print("Number of Cities: ",len(CITY)) 
print("Total Deaths: ",Total)

LA = LAT
LO = LONG

print(len(LA))
print(len(LO))

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

S=5
Size=[]
for x in cases:
    S=2+(float(x)*.2)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

#plt.axis([-130,-65,20,55])
plt.axis([A,B,C,D])

ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="black")
plt.grid(True)

plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
plt.show()
#plugins.connect(fig, plugins.MousePosition(fontsize=14))


#mpld3.display()

from matplotlib import pyplot as plt
import numpy as np
import mpld3
from mpld3 import plugins
%matplotlib inline

#LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/04-13-2020.csv"
#LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"
DataIn = open(LASTFILE).readlines()
LAT=[]
LONG=[]
CITY=[]
deaths=[]
TEXT=[]
cnt = -1
Total=0
for line in DataIn:
    if len(line)>10 and 'US' in line and "Recovered" not in line and "Unassigned" not in line:
        cnt=cnt+1
        line=line.replace("\n","")
        line = line.lstrip(",")
        line = line.split(",")
        End=len(line)-1
        if len(line)>5 and "Florida" in line[6] and "Out of FL" not in line:
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
    Sd=2+(float(xd)*3)
    Sized.append(int(Sd))
    #print(int(S))
sd = np.array(Sized)

S=1
Size=[]
for x in cases:
    S=2+(float(x)*3)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

#plt.axis([-130,-65,20,55])
plt.axis([A,B,C,D])

ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="black")
plt.scatter(LG, LT, s=sd, color="red")
plt.grid(True)

plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from:\n https://github.com/CSSEGISandData/COVID-19\n Black is Confirmed Cases and the Red are Deaths', fontsize=18)
plt.ylabel('Number of Cases')
plt.show()
#plugins.connect(fig, plugins.MousePosition(fontsize=14))


#mpld3.display()

from matplotlib import pyplot as plt
import numpy as np
import mpld3
from mpld3 import plugins
%matplotlib inline

















LA = LAT
LO = LONG

print(len(LA))
print(len(LO))

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

S=5
Size=[]
for x in cases:
    S=2+(float(x)*2)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

#plt.axis([-130,-65,20,55])
plt.axis([A,B,C,D])

ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="black")
plt.grid(True)

plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
plt.show()


from matplotlib import pyplot as plt
from matplotlib.pyplot import text
import numpy as np

LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/04-13-2020.csv"


DataIn = open(LASTFILE).readlines()
cnt=-1
LAT =[]
LON =[]
cases = []
#STate = input("What State? ")
STate = 'Florida'
for lines in DataIn:
    lines = lines.replace("\n","")

    line = lines.split(",")
    if STate in line[2] and len(line[5])>8 and len(line[6])>4:
        cnt=cnt+1
        if cnt<5:print(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
        LAT.append(line[5]) 
        LON.append(line[6])
        cases.append(int(line[7]))
LA = LAT
LO = LON

print("len(LA)",len(LA))
print("len(LO)",len(LO))
LT = np.array(LAT,dtype=np.float)
LG = np.array(LON,dtype=np.float)
print ("max(LT)",max(LT))
print ("min(LT)",min(LT))
print ('max(LG)',max(LG))
print ('min(LG)',min(LG))
print('len(LT)',len(LT))
print('len(LG)',len(LG))

fig = plt.figure(num=None, figsize=(12,12), dpi=80, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

#ax.set_facecolor('xkcd:green')
ax.set_facecolor(('#c2efc1'))

S=1
Size=[]
for x in cases:
    S=1+(float(x)*.1)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

print (min(LG))
print (max(LG))
print (min(LT))
print (max(LT))


A= (min(LG))-1
B = (max(LG))+1
C = (min(LT))-1
D = (max(LT))+1

ax = fig.gca()
T= 'Miami-Dade'
text(0.68, 0.29, T, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

#if float(line[6])<=-87 and float(line[6])>=-89:
#                if float(line[5])>42 and float(line[5])<44:
#font="/home/jack/fonts/DancingScript-Bold.ttf"
#-90 and float(line[6])>-92 and float(line[5])<40 and float(line[5])<42
#plt.axis([-100,-70,30,45])
plt.axis([A,B,C,D])
#plt.axis([-80,-90,40,45])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.scatter(LG, LT, s=s, color="black")
plt.grid(True)
#plt.text(2, 0.65, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
#text(20, 40, r'$\cos(2 \pi t) \exp(-t)$')
plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
plt.show()

LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
DataIn = open(LASTFILE).readlines()
cases=[]
for line in DataIn:
    if len(line)>10 and 'US' in line and "Recovered" not in line and "Unassigned" not in line:
        line=line.replace("\n","")
        line = line.lstrip(",")
        line = line.split(",")
        End=len(line)-1
        if len(line)>5 and "Florida" in line[6] and "Out of FL" not in line:
            cases.append(line[End])        

from matplotlib.pyplot import text
from matplotlib import pyplot as plt
import numpy as np
import mpld3
from mpld3 import plugins
import time
%matplotlib inline
LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
DataIn = open(LASTFILE).readlines()
cases=[]
for line in DataIn:
    if len(line)>10 and 'US' in line and "Recovered" not in line and "Unassigned" not in line:
        line=line.replace("\n","")
        line = line.lstrip(",")
        line = line.split(",")
        End=len(line)-1
        if len(line)>5 and "Florida" in line[6] and "Out of FL" not in line:
            cases.append(line[End])        

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
plt.scatter(LG, LT, s=s, color="black")
plt.scatter(LG, LT, s=sd, color="red")
plt.grid(True)

plt.xlabel('- Longitude -\nFirst Data Record : January 21, 2020', fontsize=18)
plt.title('Using Latitude and Longitude from:\n https://github.com/CSSEGISandData/COVID-19\n Black is Confirmed Cases and the Red are Deaths', fontsize=18)
plt.ylabel('- Latitude -', fontsize=18, color="white")
filename = "images/"+SEARCH+"_"+(time.strftime('%a_%d_%b_%Y_%I_%M_%S_%p_%Z', time.gmtime())+".png")
fig.savefig(filename, facecolor=fig.get_facecolor(), edgecolor='black')
print(filename)
plt.show()

from PIL import Image
IM = Image.open(filename)
print(IM.size)
IM












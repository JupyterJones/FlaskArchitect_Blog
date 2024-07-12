import requests as req
import time
# Create an empty list to store the URL
deaths_UScsv=[]
# Get a string based on current time to 'time' identify your saved file
DATE = time.strftime("%m-%d-%H_")
URL ="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"

# Use requests to get the URL
response = req.get(URL)
#save the response.text
content = response.text
#append the entire content to the emty list "deaths_UScsv"
deaths_UScsv.append(content)
# At this point the entire contents of the online file is in "memory" list called 'deaths_UScsv'

# The list 'deaths_UScsv' can be printed line by line:
for line in deaths_UScsv:
    print(line)

ALLin=[]
DataIn = str(deaths_UScsv)
DataIn = DataIn.replace(",,",",NaN,")
DataIn = DataIn.replace("\"","")
DATAIn = DataIn.split("\\n")
for line in DATAIn:
    entry = line.split(",")
    ALLin.append(entry)

print(len(ALLin))



cnt=0
for line in ALLin:
    cnt=cnt+1
    if cnt<5:
        print(line)
        print("")

for i in range(6,16):
    print(ALLin[i][5],ALLin[i][6])

for i in range(26,56):
    print(ALLin[i][-2],ALLin[i][-1], end = " - ")

for i in range(26,56):
    print(int(ALLin[i][-1])-int(ALLin[i][-2]), end = " - ")

THRESHhold=50
increase=0
print('The death rates in the following locations have increase by over',THRESHhold,'\n')
for i in range(1,len(ALLin)-1):
    Threshhold = int(ALLin[i][-1])-int(ALLin[i][-2])
    increase=increase+int(ALLin[i][-1])-int(ALLin[i][-2])
    if Threshhold>THRESHhold:
        print('Yesterday',ALLin[i][5],ALLin[i][6]+' had',int(ALLin[i][-1]),'deaths. The day before yesterday was',ALLin[i][-2]+'. So that is an increase of',int(ALLin[i][-1])-int(ALLin[i][-2]))
        
print('\nYesterday the total increases across the USA was about',str(increase)+'.')

for args in (('apple', '$1.09', '80'), ('truffle', '$58.01', '2')):
    print ('{0:<10} {1:>8} {2:>8}'.format(*args))


Threshhold =60
ALL=ALLin
cnt=0
CNT=0
STATE = "Florida"
for i in range(0,len(ALL)-1):
    cnt=cnt+1
    if ALL[i][6]==STATE:
        CNT=CNT+1
        if CNT==1:print(ALL[i])
        if ALL[i][8]:
            print(ALL[i][5],ALL[i][6],ALL[i][8],ALL[i][9])     

        
        #print(ALL[i][5],ALL[i][6],ALL[i][-3],ALL[i][-2],ALL[i][-1],)
        #print('{0:<12} {1:>10} {1:>20}'.format(ALL[i][5],ALL[i][6],ALL[i][10]))
        #print('{0:<12}'.format(ALL[i][5],ALL[i][6])) 

Threshhold =60
ALL=ALLin
cnt=0
CNT=0
for i in range(0,len(ALL)):
    cnt=cnt+1
    L=int(len(ALL[i]))
    if cnt>L:
        print("END")
        break
    try:
        if cnt>1 and len(ALL[i])>20:
            All=ALL[i]
            print(ALL[-3]),(ALL[-4])
            if int(ALL[-1])-int(ALL[-2])>Threshhold:
                CNT=CNT+1
                print(meta[5],meta[6],"\n",data)
    except ValueError as err:
        print("OS error: {0}".format(err))
        print(data)
print(CNT)        

ALL=ALLin
TOTAL=0
DATA = []
STATE=[]
L=len(ALL)
print(L)
cnt=0
for i in range(0,len(ALL)):
    L=int(len(ALL[i]))
    if cnt>L:
        print("END")
        break
    if ALL[i][6] == 'Florida':
        cnt=cnt+1
        #if cnt==1:print((ALL[i]))
        #if cnt==1:print(ALL[i][5],(ALL[i][6],float(ALL[i][8]),float(ALL[i][9]),int(ALL[i][-2]),int(ALL[i][-1])))
        
        Daily= "'0', '0'"+str(ALL[i]).split("', '0', '0'",1)[-1]
        Daily=Daily.replace('\'','')
        Daily=Daily.replace(']','')
        Daily=Daily.replace(' ','')
        daily = map(int,Daily.split(","))
        daily =(list(daily))
        STATE.append(daily)
        inc= int(ALL[i][-1])-int(ALL[i][-2])
        #print(i,ALL[i][5],ALL[i][6],ALL[i][-2],ALL[i][-1],inc)
        TOTAL=TOTAL+int(ALL[i][-1])
        DATA.append([ALL[i][5],ALL[i][6],float(ALL[i][8]),float(ALL[i][9]),daily,int(ALL[i][-2]),int(ALL[i][-1]),inc])
print(cnt,TOTAL) 

import requests as req
import time
DATE = time.strftime("%m-%d-%H_")
URL ="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"

resp = req.get(URL)
content = resp.text

#create a date oriented filename and print it
filename=str(DATE)+"_"+URL[-21:]
print(filename)
content=content.replace(",,",",Ex,")
content=content.replace("(","")
content=content.replace(")","")
content=content.replace("\"","")
#print(content)
# Open a file using the new filename and write the content of the 'gitfile' to it.
# Update one time daily
TEMP = open(filename,"w")
TEMP.write(content)
TEMP.close()

LASTFILE="05-02-06__covid19_deaths_US.csv"
DataIn = open(LASTFILE).readlines()
ALL=[]
for line in DataIn:
    line=line.replace('"','')
    #line=line.replace(',,',',XX,')
    line=line.replace("\n","")
    line = line.lstrip(",")
    
    line = line.split(",")
    if "US" == line[7]:# and line[6] == "New York":
         ALL.append(line)

TOTAL=0
DATA = []
STATE=[]
L=len(ALL)
cnt=0
for i in range(0,len(ALL)):
    L=int(len(ALL[i]))
    if ALL[i][6] == 'Florida':
        cnt=cnt+1
        #if cnt==1:print((ALL[i]))
        #if cnt==1:print(ALL[i][5],(ALL[i][6],float(ALL[i][8]),float(ALL[i][9]),int(ALL[i][-2]),int(ALL[i][-1])))
        
        Daily= "'0', '0'"+str(ALL[i]).split("', '0', '0'",1)[-1]
        Daily=Daily.replace('\'','')
        Daily=Daily.replace(']','')
        Daily=Daily.replace(' ','')
        daily = map(int,Daily.split(","))
        daily =(list(daily))
        STATE.append(daily)
        inc= int(ALL[i][-1])-int(ALL[i][-2])
        #print(i,ALL[i][5],ALL[i][6],ALL[i][-2],ALL[i][-1],inc)
        TOTAL=TOTAL+int(ALL[i][-1])
        DATA.append([ALL[i][5],ALL[i][6],float(ALL[i][8]),float(ALL[i][9]),daily,int(ALL[i][-2]),int(ALL[i][-1]),inc])
print(cnt,TOTAL)        

TOTAL=0
DATA = []
L=len(ALL)
DAILY=[]
cnt=0
for i in range(0,len(ALL)):
    L=int(len(ALL[i]))
    cnt=cnt+1
    #if cnt==1:print((ALL[i]))
    #if cnt==1:print(ALL[i][5],(ALL[i][6],float(ALL[i][8]),float(ALL[i][9]),int(ALL[i][-2]),int(ALL[i][-1])))
    Daily= "'0', '0', '0'"+str(ALL[i]).split("', '0', '0', '0'",1)[-1]
    Daily=Daily.replace('\'','')
    Daily=Daily.replace(']','')
    Daily=Daily.replace(' ','')
    Daily=Daily.replace('"','')
    Dail=Daily.replace(',,',',X,')
    daily = map(int,Daily.split(","))
    daily =(list(daily))
    DAILY.append(daily)
    inc= daily[-1]-daily[-2]
    #print(i,[ALL[i][5],ALL[i][6],float(ALL[i][8]),float(ALL[i][9]),daily,daily[-2],daily[-1],inc])
    TOTAL=TOTAL+int(ALL[i][L-1])
    DATA.append([ALL[i][5],ALL[i][6],float(ALL[i][8]),float(ALL[i][9]),daily,daily[-2],daily[-1],inc])
print(cnt,TOTAL)        

print(STATE)

res=[sum(x) for x in zip(*STATE)]
print(res)

import plotly.graph_objects as go
import pandas as pd

import plotly.graph_objects as go
import numpy as np
last=0
inc=[]
for num in res:
    dat=num-last
    inc.append(dat)
    last=num
N = 100    
data=inc
time=range(0,len(data))
x = np.asarray(time)
y = np.asarray(data)
colors = np.asarray(100)
sz = 5

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y
    )
)

fig.show()


import plotly.graph_objects as go
import pandas as pd

import plotly.graph_objects as go
import numpy as np
last=0
inc=[]
for num in DATA[209][4]:
    dat=num-last
    inc.append(dat)
    last=num
N = 100    
data=inc
time=range(0,len(data))
x = np.asarray(time)
y = np.asarray(data)
colors = np.asarray(100)
sz = 5

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y
    )
)

fig.show()


print(DATA[209][4])

print([range(0,len(DATA[209][4]))])

last=0
inc=[]
for num in DATA[209][4]:
    dat=num-last
    inc.append(dat)
    last=num

import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import numpy as np
last=0
inc=[]
for num in DATA[209][4]:
    dat=num-last
    inc.append(dat)
    last=num
    
data=inc
time=range(0,len(data))
x = np.asarray(time)
y = np.asarray(data)
print(x)
print(y)
plt.bar(x, y, color='#2040D0', width=6, linewidth=0)
plt.bar(x, y, linewidth=6, color='r', zorder=10,  alpha=0.6)
plt.scatter(x, y, s=30, color='yellow', zorder=15,  alpha=0.6)

import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import numpy as np
data=DATA[209][4]
time=range(0,len(data))
x = np.asarray(time)
y = np.asarray(data)
print(x)
print(y)
plt.scatter(x, y, s=4, color='r', zorder=10,  alpha=0.6)

%matplotlib inline 
#%pprint           
import plotly
import plotly.graph_objs as go
import numpy as np   # So we can use random numbers in examples
# Must enable in order to use plotly off-line (vs. in the cloud... hate cloud)
plotly.offline.init_notebook_mode()
data=DATA[209][4]
time=range(0,len(data))
x = np.asarray(time)
y = np.asarray(data)

trace_b = go.Bar(x=data,
                y=time,
                name='Citizen',
                marker=dict(color='#FFCDD2'))

data3 = go.Data([data, range(0,len(data))])









# Create a trace
trace = go.bar(x,y)

data0 = [trace]

# Plot and embed in ipython notebook!
plotly.offline.iplot(data3, filename='basic-scatter')

!ls 04-30-16__covid19_deaths_US.csv



print(ALL[13])

TOTAL=0
DATA = []
L=len(ALL)
cnt=0
for i in range(0,len(ALL)):
    L=int(len(ALL[i]))
    if ALL[i][6] == 'Alabama':
        cnt=cnt+1
        #if cnt==1:print((ALL[i]))
        #if cnt==1:print(ALL[i][5],(ALL[i][6],float(ALL[i][8]),float(ALL[i][9]),int(ALL[i][-2]),int(ALL[i][-1])))
        
        Daily= "'0', '0'"+str(ALL[i]).split("', '0', '0'",1)[-1]
        Daily=Daily.replace('\'','')
        Daily=Daily.replace(']','')
        Daily=Daily.replace(' ','')
        daily = map(int,Daily.split(","))
        daily =(list(daily))
        inc= int(ALL[i][-1])-int(ALL[i][-2])
        #print(i,ALL[i][5],ALL[i][6],ALL[i][-2],ALL[i][-1],inc)
        TOTAL=TOTAL+int(ALL[i][-1])
        DATA.append([ALL[i][5],ALL[i][6],float(ALL[i][8]),float(ALL[i][9]),daily,int(ALL[i][-2]),int(ALL[i][-1]),inc])
print(cnt,TOTAL)        



print(daily[-1])

print(DATA[209][4])

print (len(DATA))
INC=0
for i in range(0,len(DATA)-1):
    city = DATA[i][0]
    state = DATA[i][1]
    latitude = DATA[i][2]
    longitude = DATA[i][3]
    data = DATA[i][4]
    yesterday = DATA[i][5]
    today = DATA[i][6]
    increase = DATA[i][7]
    if increase>40:
        INC=INC+1
        #print(data)
        print("\n",INC,city,state,yesterday,today,"  New Deaths:",increase)
        if increase>50:
            print(i,"   One Week Record: ",data[-7],data[-6],data[-5],data[-4],data[-3],data[-2],data[-1],"\n   One week increase",(data[-1]-data[-7]))
print("\n",INC,"Locations with increase of over 40 deaths.")

print (len(DATA))
INC=0
for i in range(0,len(DATA)):
    if len(DATA[i])==8:
        INC=INC+1
        city = DATA[i][0]
        state = DATA[i][1]
        latitude = DATA[i][2]
        longitude = DATA[i][3]
        data = DATA[i][4]
        yesterday = DATA[i][5]
        today = DATA[i][6]
        Len=len(DATA[i])
        print(i,INC,Len,city,state,yesterday,today,increase)


import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import numpy as np
from PIL import Image,ImageFont,ImageDraw,ImageFilter,ImageChops
from random import randint
from mpl_toolkits.basemap import Basemap
fig = plt.figure(num=None, figsize=(12, 8) ) 
m = Basemap(width=6000000,height=4500000,resolution='c',projection='aea',lat_1=35.,lat_2=45,lon_0=-100,lat_0=40)
m.drawcoastlines(linewidth=0.5)
m.fillcontinents(color='tan',lake_color='lightblue')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,15.),labels=[True,True,False,False],dashes=[2,2])
m.drawmeridians(np.arange(-180.,181.,15.),labels=[False,False,False,True],dashes=[2,2])
m.drawmapboundary(fill_color='lightblue')
m.drawcountries(linewidth=2, linestyle='solid', color='k' ) 
m.drawstates(linewidth=0.5, linestyle='solid', color='k')
m.drawrivers(linewidth=0.5, linestyle='solid', color='blue')
cities =[]
LAT=[]
LONG=[]
LATd=[]
LONGd=[]
STATES=[]
ALL=[]
cases=[]
deaths =[]
yesterday=0
today=0
longitude = ""
cnt=0
CNT=0
Dcnt=0
LASTFILE="04-30-10__covid19_deaths_US.csv"
DataIn = open(LASTFILE).readlines()
for line in DataIn:
    line=line.replace('"','')
    #if cnt==0:print (line)
    cnt=cnt+1
    line=line.replace("\n","")
    line = line.lstrip(",")
    line = line.split(",")
    #if cnt<10 and line[5] !="":print (line[6])
    if "US" == line[7]:# and line[6] == "New York":
        #if CNT==7:print(line)
        #if CNT==8:print(line)    
        #if CNT<5 and line[5] !="":print line
        CNT=CNT+1
        ALL.append(line)
        LAT.append(line[5])
        LONG.append(line[6])
        L=len(line)
        deaths.append(line[L-1])
        #print(L)
        #print(line[L-1],line[L-2])
        if int(line[L-2])+50<int(line[L-1]):
            #print ("if ",int(line[L-2]),'+10',int(line[L-1]))
            #print (text,int(line[L-2]),int(line[L-1]))
            if len(line[8])>3:            
                text=line
                STATES.append(text)
                yesterday=yesterday+int(line[-2])
                today= today+int(line[-1])
                Dcnt=Dcnt+1
                #print(line[8],line[9])
                cities.append([line[5],line[6],line[8],line[9],line[L-1],int(line[L-1])-int(line[L-2])])
                LATd.append(line[8])
                LONGd.append(line[9])
                
                
LTd = np.array(LATd,dtype=np.float)
LGd = np.array(LONGd,dtype=np.float)
Str = np.array(cities,dtype=np.str)

S=1
Size=[]
for x in cases:
    S=1+(float(x)*.01)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

Sd=1
Sized=[]
for xd in deaths:
    Sd=0+(float(xd)*.07)
    Sized.append(int(Sd))
    #print(int(S))
sd = np.array(Sized)
#print(Sized)
plt.title("Finding-Hot-Spots.ipynb - https://github.com/JupyterJones/COVID-19-Jupyter-Notebooks")
#plt.text(max(LG-1.2),max(LT), search, color='white', fontsize=24)
#x, y = m(lons, lats)  # transform coordinates
x, y = m(LGd, LTd)
#xx,yy = m(LG, LT)
plt.xlabel('Longitude',color="white", fontsize=24)
plt.ylabel('Latitute',color="white", fontsize=24)

for i in (range(0,len(cities))):
    C=cities[i][0]
    S=cities[i][1]
    t=float(cities[i][2])
    l=float(cities[i][3])
    d=cities[i][4]
    inc=cities[i][5]
    print(C,S,l,t,d,inc)
    plt.annotate(C, m(l,t),color='black',fontsize=10,zorder=15)   
    
m.scatter(x, y, s=sd, color='r', zorder=10,  alpha=0.6)
filename = "BaseMap/april30_Hotspots__.png"
plt.savefig(filename, dpi=120, facecolor='salmon', edgecolor='b',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches="tight", pad_inches=0.2,
        frameon=None, metadata=None)


LS=[]
LISTS="""0,0,0,0,1,1,1,2,2,3,4,6,9,9,11,17,19,20,0,0,0,0,0,0,0
0,0,0,0,1,1,1,2,2,3,4,6,9,9,11,17,19,20,0,0,0,0,0,0,0
0,0,0,0,1,1,1,2,2,3,4,6,9,9,11,17,19,20,0,0,0,0,0,0,0
0,0,0,0,1,1,1,2,2,3,4,6,9,9,11,17,19,20,0,0,0,0,0,0,0
0,0,0,0,1,1,1,2,2,3,4,6,9,9,11,17,19,20,0,0,0,0,0,0,0"""
LISTS=LISTS.split("\n")
for line in LISTS:
    line=line.replace('\'','')
    line=line.lstrip("'")
    lline=line.rstrip("'")
    LS.append([lline])


print(LS)


LS=[]
LISTS=[[0,0,0,0,1,1,1,2,2,3,4,6,9,9,11,17,19,20,0,0,0,0,0,0,0],[1,1,1,2,2,3,4,6,9,9,11,17,19,20,0,0,0,0,0,0,0,0,0,0,0],[4,6,9,9,11,17,19,20,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,3],
[11,17,19,20,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,3,4,6,9,9],[19,20,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,3,4,6,9,9,11,17]]

res=[sum(x) for x in zip(*LISTS)]
print(res)

[0,   0,  0,  0,  1,  1,  1,  2, 2, 3,  4,  6,  9,  9, 11, 17, 19, 20,0,0, 0, 0, 0, 0, 0],
[1,   1,  1,  2,  2,  3,  4,  6, 9, 9, 11, 17, 19, 20,  0,  0,  0,  0,0,0, 0, 0, 0, 0, 0],
[4,   6,  9,  9, 11, 17, 19, 20, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,0,1, 1, 1, 2, 2, 3],
[11, 17, 19, 20,  0,  0,  0,  0, 0, 0,  0,  0,  0,  0,  0,  1,  1,  1,2,2, 3, 4, 6, 9, 9],
[19, 20,  0,  0,  0,  0,  0,  0, 0, 0,  0,  0,  0,  1,  1,  1,  2,  2,3,4, 6, 9, 9,11,17]

 35, 44, 29, 31, 14, 21, 24, 28, 11,12, 15,23, 28, 30, 12, 19, 22, 23,5,7,10,14,17,22,29

integers = [1, 2, 3]


strings = [str(integer) for integer in integers]

a_string = "".join(strings)

an_integer = int(a_string)


print(an_integer)

# Using graph_objects
import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv('05-01-13__covid19_deaths_US.csv')

fig = go.Figure([go.Scatter(x=df['lat'], y=df['long_'])])
fig.show()



https://en.wikipedia.org/wiki/List_of_United_States_counties_and_county_equivalents
states the USA and territories has 3,243 counties

# Use data from the resource above
import requests as req
import time
# Create an empty list to store the URL
CountyStats=[]
# Get a string based on current time to 'time' identify your saved file
DATE = time.strftime("%m-%d-%H_")
URL ="https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/totals/co-est2019-alldata.csv"
resp = req.get(URL)
content = resp.text

#create a date oriented filename and print it
filename=str(DATE)+"_"+URL[-22:]
print(filename)
#print(content)
# Open a file using the new filename and write the content of the 'gitfile' to it.
# Update one time daily
TEMP = open(filename,"w")
TEMP.write(content)
CountyStats.append(content)
TEMP.close()

LASTFILE="05-02-08__co-est2019-alldata.csv"
DataIn = open(LASTFILE).readlines()
cnt=0
for lineZ in DataIn:
    cnt=cnt+1
    line=lineZ.split(",")
    if cnt<8:
        if cnt==1:print(line)
        if cnt==2:print("----------------------------------------------------------------")
        #print(line)
        print("----------------------------------------------------------------")
        print(line[1],line[2])

count=0
cnt=0
dec=0
State = "Alabama"
with open("05-02-08__co-est2019-alldata.csv") as txt_file:
    for line in txt_file:
        count=count+1
        if count==1:print(line)
        line = line.split(",")
        if line[5]==State:
            cnt=cnt+1
            print(line[3],line[4],line[5],line[6],line[18],line[28])
            if int(line[28])<0:dec=dec+1
        pass
print("\nlines in File: ",count)
print(State," has ", cnt," counties.")
print("In 2019 ",dec," counties decreased in population.")

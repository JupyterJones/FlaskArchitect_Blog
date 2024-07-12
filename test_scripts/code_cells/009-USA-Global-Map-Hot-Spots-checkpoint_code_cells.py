import time
#DATE = time.strftime("%Y-%m%d%H%M%S")
DATE = time.strftime("%m-%d-%H_")
DATE 


import requests as req
import time
DATE = time.strftime("%m-%d-%H_")
URL ="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/04-29-2020.csv"

resp = req.get(URL)
content = resp.text

#create a date oriented filename and print it
filename=URL[-14:]
print(filename)
content=content.replace(",,",",Ex,")
content=content.replace("(","")
content=content.replace(")","")
content=content.replace("\"","")
print(content)
# Open a file using the new filename and write the content of the 'gitfile' to it.
# Update one time daily
TEMP = open(filename,"w")
TEMP.write(content)
TEMP.close()

LASTFILE="05-01-10__04-29-2020.csv"
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

weirdstuff="45001,Abbeville,South Carolina,US,2020-04-30 02:32:27,34.22333378,-82.46170658,29,0,0,29,Abbeville, South Carolina, US"
text=weirdstuff.split(",")
print(text[1])

LASTFILE="05-01-10__04-29-2020.csv"
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

!ls 04-30-14__covid19_deaths_US.csv

filename=str(DATE)+"_"+URL[-21:]
print(filename)

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

# Using graph_objects
import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = go.Figure([go.Scatter(x=df['Date'], y=df['AAPL.High'])])
fig.show()


print (ALL[9])

for i in range(0,len(ALL)):
    if int(ALL[i][-2])+50<int(ALL[i][-1]):
        print('   ',ALL[i][5],ALL[i][6],ALL[i][-2],ALL[i][-1])
        print(ALL[i][5]+',',ALL[i][6],'Has',int(ALL[i][-1])-int(ALL[i][-2]),'more deaths than yesterday.')


from PIL import Image
IM=Image.open('BaseMap/april30_Hotspots__.png')
IM

for i in (range(0,len(cities))):
    C=cities[i][0]
    S=cities[i][1]
    t=cities[i][2]
    l=cities[i][3]
    n=cities[i][4]
    print(city,l,t,ca,n)

for i in (range(0,len(cities))):
    city=cities[i][0]
    state=cities[i][1]
    l=float(cities[i][2])
    t=float(cities[i][3])
    n=cities[i][4]
    TX=ca+","+str(n)
    plt.text(l, t, TX, color='white', fontsize=24)
    
    

filename = "BaseMap/text30_Hotspots__.png"
plt.savefig(filename, dpi=120, facecolor='salmon', edgecolor='b',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches="tight", pad_inches=0.2,
        frameon=None, metadata=None)


import matplotlib.pyplot as plt
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

for i in (range(0,len(cities))):
    C=cities[i][0]
    S=cities[i][1]
    t=float(cities[i][2])
    l=float(cities[i][3])
    n=cities[i][4]
    print(C,l,t)
    plt.annotate(C, m(l,t),color='white',fontsize=10,zorder=15)
#plt.annotate(cities[4][0], m(-118.228241,34.308283),color='white',fontsize=24,zorder=18)    
#plt.annotate("TEST", m(-118.228241,34.308283),color='green',fontsize=24,zorder=15)

#plt.annotate('Jul-24-2012', xy=(40.88320119, -72.8012172), xycoords='axes fraction')
plt.show()

ax.annotate("blablabla", m1(121.597366,25.105497),color='green')

for i in (range(0,len(cities))):
    C=cities[i][0]
    S=cities[i][1]
    t=cities[i][2]
    l=cities[i][3]
    n=cities[i][4]
    print(C,S,l,t,n)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

num = 79
lat = 5 * np.random.random(num) + 33
lon = 10 * np.random.random(num) - 104

fig, ax = plt.subplots()
m = Basemap(projection='stere',lon_0=-95,lat_0=35.,lat_ts=40,
            llcrnrlat=33,urcrnrlat=38,
            llcrnrlon=-103.8,urcrnrlon=-94,
            resolution='h', ax=ax)

X,Y = m(lon,lat)
m.drawcoastlines()
m.drawstates()
m.drawcountries()
m.drawmapboundary(fill_color='lightblue')
m.drawparallels(np.arange(0.,40.,2.),color='gray',dashes=[1,3],labels=[1,0,0,0])
m.drawmeridians(np.arange(0.,360.,2.),color='gray',dashes=[1,3],labels=[0,0,0,1])

ax.scatter(X,Y)

for i, (x, y) in enumerate(zip(X, Y), start=1):
    ax.annotate(str(i), (x,y), xytext=(5, 5), textcoords='offset points')

plt.show()



from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(projection='ortho', 
              lat_0=0, lon_0=0)
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

x, y = map(2, 41)
x2, y2 = (-90, 10)

plt.annotate('Barcelona', xy=(x, y),  xycoords='data',
                xytext=(x2, y2), textcoords='offset points',
                color='r',
                arrowprops=dict(arrowstyle="fancy", color='g')
                )

x2, y2 = map(0, 0)
plt.annotate('Barcelona', xy=(x, y),  xycoords='data',
                xytext=(x2, y2), textcoords='data',
                arrowprops=dict(arrowstyle="->")
                )
plt.show()


x, y = m(0,0)
ax.annotate('0', xy=(x, y), xycoords='data', xytext=(x, y), textcoords='data')

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


#data points
ra = [25,20,21]
dec = [25,20,21]

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])

# Get the hammer projection map
m = Basemap(projection='hammer',lon_0 = 0, rsphere = 1.0)
m.drawparallels(np.arange(-90.,90.,30.),labels=[1,0,0,0]) # draw parallels
m.drawmeridians(np.arange(-180.,180.,60.)) # draw meridians

m.plot(ra,dec,marker='o',linestyle='None',markersize=1,latlon=True)
ax.annotate('0', xy=(0, 0), xycoords='data',xytext = (0,0),textcoords='data')

plt.show()

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


#data points
ra = [25,20,21]
dec = [25,20,21]

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])

# Get the hammer projection map
m = Basemap(projection='hammer',lon_0 = 0, rsphere = 1.0)
m.drawparallels(np.arange(-90.,90.,30.),labels=[1,0,0,0]) # draw parallels
m.drawmeridians(np.arange(-180.,180.,60.)) # draw meridians

m.plot(ra,dec,marker='o',linestyle='None',markersize=1,latlon=True)
# Convert from latitude/longitude to x,y
x, y = m(0,0)
ax.annotate('0', xy=(x, y), xycoords='data', xytext=(x, y), textcoords='data')

plt.show()




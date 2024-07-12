!find /home/jack/miniconda3 -name gshhs_h.dat

!sudo updatedb

!locate gshhs_h.dat 

!conda install basemap-data-hires

!locate share/proj

!mkdir BaseMap

import sys
sys.path.append("/home/jack/miniconda3/envs/deep/lib/python3.7/site-packages/") # go to parent dir
#from customFunctions import *

import os
import sys
os.environ['PROJ_LIB'] = '/home/jack/miniconda3/envs/deep/share/proj'
sys.path.append("/home/jack/miniconda3/envs/deep/lib/python3.7/site-packages/") # go to parent dir

!wget https://anaconda.org/conda-forge/basemap-data-hires/1.2.1/download/linux-64/basemap-data-hires-1.2.1-0.tar.bz2

!conda install --offline ./basemap-data-hires-1.2.2-0.tar.bz2

!wget https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv

datafile = open("time_series_covid19_deaths_US.csv", "r")
count = 0
for data in datafile:
    count=count+1
    if "Ohio" in data:
        print ("XXXXX",count,data)

import os
os.environ['PROJ_LIB'] = '/home/jack/miniconda3/envs/deep/share/proj'
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import numpy as np
from PIL import Image,ImageFont,ImageDraw,ImageFilter,ImageChops
from random import randint
from mpl_toolkits.basemap import Basemap
import requests as req
import time
DATE = time.strftime("%m-%d-%H_")

# Create an empty list
ALLdata=[]

URL ="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"
#https://raw.githubusercontent.com/CSSEGISandData/COVID-19/
#master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv
resp = req.get(URL)
content = resp.text

#clean the content, then break the content into lines 
content=content.replace(",,",",Ex,")
content=content.replace("(","")
content=content.replace(")","")
content=content.replace("\"","")
lines= content.splitlines()
print (len(lines))
# loop the lines one line at a time
# split each line at the delimiter ` , ` 
# then append the empty list 'ALLdata' with the line (which is now a list):  [line]  
for line in lines:
    #convert the splitlines to strings
    line= str(line).split(",")
    ALLdata.append(line)
    
"""
Finding counties with a "threshhold" increase in deaths
Take the last four entries of data to see if the number of deaths has increased for the last three days:
To make it easy to understand lets use dates instead of data.
May10 May11 May12 May13
subract May10 from May11 check if the result is above the 'Threshhold'
subract May11 from May12 check if the result is above the 'Threshhold'
subract May12 from May13 check if the result is above the 'Threshhold'
if all three conditions are met, print the location and information.
"""    
    
Threshhold = 10
count = 0
STATE =[]
COUNTY =[]
Points =[]
lat=[]
long=[]
# Check each line of data, county by county.
for i in range(1,len(ALLdata)):
    # Increase a counter for every line -  this will allow further investigation into the data
    # as demonstarted in the next four cells.
    count=count+1
    # subtract the last four days of data to see if it has increased by the minimum of the Threshhold each day
    if int(ALLdata[i][-3])-int(ALLdata[i][-4]) >Threshhold and int(ALLdata[i][-2])-int(ALLdata[i][-3]) >Threshhold and int(ALLdata[i][-1])-int(ALLdata[i][-2]) >Threshhold:
        # if they do increase as specified, define the line as a variable called history
        history=[int(ALLdata[i][-3])-int(ALLdata[i][-4]),int(ALLdata[i][-2])-int(ALLdata[i][-3]),int(ALLdata[i][-1])-int(ALLdata[i][-2])]
        # The total amount of deaths in the specific county
        deaths = int(ALLdata[i][-1])
        # The county's name
        county = ALLdata[i][5]
        # The State the county is located in
        state = ALLdata[i][6]
        STATE.append(state)
        COUNTY.append(county)
        # The longitude and latitude of the county
        longitude = ALLdata[i][9]
        latitude = ALLdata[i][8]
        long.append(float(longitude))
        lat.append(float(latitude))
        Points.append([float(longitude),float(latitude)])
        #print the data line by line
        print ("i="+str(count),deaths,county,state,longitude,latitude,history)
"""
Plot the data on a basemape with annotations of the County namea
""" 

fig = plt.figure(num=None, figsize=(12, 8), dpi=120 ) 
m = Basemap(width=6000000,height=4500000,resolution='h',projection='aea',lat_1=35.,lat_2=45,lon_0=-100,lat_0=40)
m.drawcoastlines(linewidth=0.5)
m.fillcontinents(color='tan',lake_color='lightblue')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,10.),labels=[True,True,False,False],dashes=[2,2])
m.drawmeridians(np.arange(-180.,181.,10.),labels=[False,False,False,True],dashes=[2,2])
m.drawmapboundary(fill_color='lightblue')
m.drawcountries(linewidth=2, linestyle='solid', color='k' ) 
m.drawstates(linewidth=0.5, linestyle='solid', color='k')
m.drawrivers(linewidth=0.5, linestyle='solid', color='blue')

#-- Place the text in the upper left hand corner of the axes
# The basemap instance doesn't have an annotate method, so we'll use the pyplot
# interface instead.  (This is one of the many reasons to use cartopy instead.)
#plt.annotate('Jul-24-2012', xy=(0, 1), xycoords='axes fraction')
text0 = COUNTY
text = STATE
for i in range(len(Points)):
    x = Points[i][0]
    y = Points[i][1]
    tx = str(text0[i])+", "+str(text[i])
    xx, yy = m(x,y)
    print(xx, yy)
    #plt.plot(xx, yy, 'bo')
    plt.scatter(xx, yy, s=20, color='red', zorder=5, alpha=0.6)
    plt.text(xx, yy, tx, fontsize=16, color="white")

filename = "BaseMap/Hotspots__.png"
plt.savefig(filename, dpi=120, facecolor='salmon', edgecolor='b',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches="tight", pad_inches=0.2,
        frameon=None, metadata=None)
    
plt.show()

from PIL import Image
IM = Image.open(filename)
print (IM.size)
IM

text0 = COUNTY
text = STATE
for i in range(len(Points)):
    x = Points[i][0]
    y = Points[i][1]
    tx = text0[i]+", "+text[i]
    xx, yy = m(x,y)
    print(xx, yy)
    #plt.plot(xx, yy, 'bo')
    plt.scatter(xx, yy, s=20, color='red', zorder=5, alpha=0.6)
    plt.text(xx, yy, tx, fontsize=16, color="white")


inc= len(COUNTY)
colors = ['yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan','yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan']

color = colors[-inc:]
print (color)

print(Points)

text0 = COUNTY
text = STATE
for i in range(len(Points)):
    x = Points[i][0]
    y = Points[i][1]
    tx = text0[i]+", "+text[i]
    colorz =color[i]
    xx, yy = m(x,y)
    print(xx, yy)
    #plt.plot(xx, yy, 'bo')
    plt.scatter(xx, yy, s=20, color=colorz, zorder=5, alpha=0.6)
    plt.text(xx, yy, tx, fontsize=16, color="white")


import matplotlib.pyplot as plt
import numpy as np

c = np.char.array(COUNTY)
S = np.char.array(STATE)
y = np.array(long)
x =np.array(lat)

inc= len(COUNTY)
colorZ = ['yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan','yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan','navy']
colors = colorZ[-inc:]


plt.scatter(x,y, s=40, color=colors)

labels = ['{0}, {1}'.format(i,j) for i,j in zip(c, S)]



sortlegend0 = [colors[0], labels[0],]
sortlegend1 = [colors[1], labels[1],]
print (sortlegend)
plt.legend([(sortlegend0,sortlegend1)], loc='left center', bbox_to_anchor=(-0.1, 1.),
           fontsize=8)

"""
plt.legend(handles=sortlegend, loc='left center', bbox_to_anchor=(-0.1, 1.),
           fontsize=8)
"""
plt.savefig('piechart.png', bbox_inches='tight')


#plt.legend(handles=[line_up, line_down])

import matplotlib.pyplot as plt
import numpy as np

c = np.char.array(COUNTY)
S = np.char.array(STATE)
y = np.array(long)
x =np.array(lat)

inc= len(COUNTY)
colorZ = ['yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan','yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan','navy']
colors = colorZ[-inc:]


plt.scatter(x,y, s=40, color=colors)

labels = ['{0}, {1}'.format(i,j) for i,j in zip(c, S)]



sortlegend0 = [colors[0], labels[0],]
sortlegend1 = [colors[1], labels[1],]
print (sortlegend)
plt.legend([(sortlegend0,sortlegend1)], loc='left center', bbox_to_anchor=(-0.1, 1.),
           fontsize=8)

"""
plt.legend(handles=sortlegend, loc='left center', bbox_to_anchor=(-0.1, 1.),
           fontsize=8)
"""
plt.savefig('piechart.png', bbox_inches='tight')


#plt.legend(handles=[line_up, line_down])

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

red_patch = mpatches.Patch(color=colors, label=labels)
plt.legend(handles=[red_patch])

plt.show()

A,B = [colors, labels]
print(A)

import matplotlib.pyplot as plt
import numpy as np
#Legend, = color, label =  [colors, labels]
A,B = [colors, labels]

Legend= [A, B]
plt.legend(handles=Legend, loc='left center', bbox_to_anchor=(-0.1, 1.),fontsize=8)

sort_legend = True
if sort_legend:
    colors, labels =  zip(*colors, labels,
                                          key=lambda x: x[1],
                                          reverse=True)
print(colors, labels)

import matplotlib.pyplot as plt
import numpy as np

c = np.char.array(COUNTY)
S = np.char.array(STATE)
y = np.array(long)
x =np.array(lat)

inc= len(COUNTY)
colors = ['yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan','yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan']
colorz = colors[-inc:]
#Cc = np.char.array(colors)

plt.scatter(x,y, s=40, color=colorz)


labels = ['{0}, {1}'.format(i,j) for i,j in zip(c, S)]

sort_legend = True
if sort_legend:
    colors, labels =  zip(*sorted(zip(colorz, labels),
                                          key=lambda x: x[1],
                                          reverse=True))
    print(colorz, labels)
plt.legend(colors, labels, loc='left center', bbox_to_anchor=(-0.1, 1.),
           fontsize=8)

plt.savefig('piechart.png', bbox_inches='tight')

import matplotlib.pyplot as plt
import numpy as np

x = np.char.array(COUNTRY)
y = np.array([234, 64, 54,10, 0, 1, 0, 9, 2, 1, 7, 7])
colors = ['yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan']
porcent = 100.*y/y.sum()

patches, texts = plt.pie(y, colors=colors, startangle=90, radius=1.2)
labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, porcent)]

sort_legend = True
if sort_legend:
    patches, labels, dummy =  zip(*sorted(zip(patches, labels, y),
                                          key=lambda x: x[2],
                                          reverse=True))

plt.legend(patches, labels, loc='left center', bbox_to_anchor=(-0.1, 1.),
           fontsize=8)

plt.savefig('piechart.png', bbox_inches='tight')

import matplotlib.pyplot as plt
import numpy as np

x = np.char.array(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct', 'Nov','Dec'])
y = np.array([234, 64, 54,10, 0, 1, 0, 9, 2, 1, 7, 7])
colors = ['yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan']
porcent = 100.*y/y.sum()

patches, texts = plt.pie(y, colors=colors, startangle=90, radius=1.2)
labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, porcent)]

sort_legend = True
if sort_legend:
    patches, labels, dummy =  zip(*sorted(zip(patches, labels, y),
                                          key=lambda x: x[2],
                                          reverse=True))

plt.legend(patches, labels, loc='left center', bbox_to_anchor=(-0.1, 1.),
           fontsize=8)

plt.savefig('piechart.png', bbox_inches='tight')

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
m = Basemap(width=120000,height=90000,projection='aeqd',
            resolution=None,lat_0=30.,lon_0=80.)
lats=[30.0,30.1,30.2,30.0,30.1,30.2]
lons=[80.0,80.1,80.2,80.3,80.4,80.5]
m.bluemarble()
x, y = m(lons,lats)
labels=['Point1','Point2','Point3','Point4','Point5','Point6']
m.scatter(x,y,10,marker='o',color='k')
for label, xpt, ypt in zip(labels, x, y):
    plt.text(xpt + 10, ypt + 10, label, size=20)
plt.show()

import requests as req
import time
DATE = time.strftime("%m-%d-%H_")

# Create an empty list
ALLdata=[]

URL ="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"

resp = req.get(URL)
content = resp.text

#clean the content, then break the content into lines 
content=content.replace(",,",",Ex,")
content=content.replace("(","")
content=content.replace(")","")
content=content.replace("\"","")
lines= content.splitlines()
print (len(lines))
# loop the lines one line at a time
# split each line at the delimiter ` , ` 
# then append the empty list 'ALLdata' with the line (which is now a list):  [line]  
for line in lines:
    #convert the splitlines to strings
    line= str(line).split(",")
    ALLdata.append(line)
    
    

Threshhold = 15
count = 0
STATE =[]
Points =[]
# Check each line of data, county by county.
for i in range(1,len(ALLdata)):
    # Increase a counter for every line -  this will allow further investigation into the data
    # as demonstarted in the next four cells.
    count=count+1
    # subtract the last four days of data to see if it has increased by the minimum of the Threshhold each day
    if int(ALLdata[i][-3])-int(ALLdata[i][-4]) >Threshhold and int(ALLdata[i][-2])-int(ALLdata[i][-3]) >Threshhold and int(ALLdata[i][-1])-int(ALLdata[i][-2]) >Threshhold:
        # if they do increase as specified, define the line as a variable called history
        history=[int(ALLdata[i][-3])-int(ALLdata[i][-4]),int(ALLdata[i][-2])-int(ALLdata[i][-3]),int(ALLdata[i][-1])-int(ALLdata[i][-2])]
        # The total amount of deaths in the specific county
        deaths = int(ALLdata[i][-1])
        # The county's name
        county = ALLdata[i][5]
        # The State the county is located in
        state = ALLdata[i][6]
        STATE.append(state)
        # The longitude and latitude of the county
        longitude = ALLdata[i][9]
        latitude = ALLdata[i][8]
        Points.append([float(longitude),float(latitude)])
        #print the data line by line
        print ("i="+str(count),deaths,county,state,longitude,latitude,history)
        

print (Points)
#points = [[-118.22824109999999,34.30828379],[-87.81658794,41.84144849],[-72.8012172,40.88320119]]
print (STATE)

print(Points[0][1])

import matplotlib.pyplot as plt


#text = [['Los Angeles'],['Cook'],['Suffolk']]
text = STATE
for i in range(len(Points)):
    x = Points[i][0]
    y = Points[i][1]
    xx = text[i]
    plt.plot(x, y, 'bo')
    plt.text(x , y , xx, fontsize=12)

plt.xlim((-120, -50))
plt.ylim((30, 50))
plt.show()

MAX=[max(points[0]),max(points[1]),max(points[2])]
MIN=[min(points[0]),min(points[1]),min(points[2])]

print(min(MIN),max(MIN))
print(min(MAX),max(MAX))

import matplotlib.pyplot as plt

points = [[-118.22824109999999,34.30828379],[-87.81658794,41.84144849],[-72.8012172,40.88320119]]
text = ['Los Angeles','Cook','Suffolk']
for i in range(len(points)):
    x = points[i][0]
    y = points[i][1]
    xx = text[i]
    plt.plot(x, y, 'bo')
    plt.text(x , y , xx, fontsize=12)

#plt.xlim((-120, -50))
#plt.ylim((30, 50))
plt.xlim(min(MIN),max(MIN))
plt.ylim(min(MAX),max(MAX))

plt.show()

import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import numpy as np
from PIL import Image,ImageFont,ImageDraw,ImageFilter,ImageChops
from random import randint
from mpl_toolkits.basemap import Basemap
fig = plt.figure(num=None, figsize=(12, 8), dpi=300 ) 
m = Basemap(width=6000000,height=4500000,resolution='h',projection='aea',lat_1=35.,lat_2=45,lon_0=-100,lat_0=40)
m.drawcoastlines(linewidth=0.5)
m.fillcontinents(color='tan',lake_color='lightblue')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,10.),labels=[True,True,False,False],dashes=[2,2])
m.drawmeridians(np.arange(-180.,181.,10.),labels=[False,False,False,True],dashes=[2,2])
m.drawmapboundary(fill_color='lightblue')
m.drawcountries(linewidth=2, linestyle='solid', color='k' ) 
m.drawstates(linewidth=0.5, linestyle='solid', color='k')
m.drawrivers(linewidth=0.5, linestyle='solid', color='blue')

#-- Place the text in the upper left hand corner of the axes
# The basemap instance doesn't have an annotate method, so we'll use the pyplot
# interface instead.  (This is one of the many reasons to use cartopy instead.)
#plt.annotate('Jul-24-2012', xy=(0, 1), xycoords='axes fraction')
text = STATE
for i in range(len(Points)):
    x = Points[i][0]
    y = Points[i][1]
    tx = text[i]
    xx, yy = m(x,y)
    print(xx, yy)
    #plt.plot(xx, yy, 'bo')
    plt.scatter(xx, yy, s=20, color='red', zorder=5, alpha=0.6)
    plt.text(xx, yy, tx, fontsize=12)


plt.savefig("BaseMap/Hotspots__.png", dpi=300, facecolor='salmon', edgecolor='b',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches="tight", pad_inches=0.2,
        frameon=None, metadata=None)
    
plt.show()

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
m = Basemap(width=6000000,height=4500000,resolution='h',projection='aea',lat_1=35.,lat_2=45,lon_0=-100,lat_0=40)
m.drawcoastlines(linewidth=0.5)
m.fillcontinents(color='tan',lake_color='lightblue')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,10.),labels=[True,True,False,False],dashes=[2,2])
m.drawmeridians(np.arange(-180.,181.,10.),labels=[False,False,False,True],dashes=[2,2])
m.drawmapboundary(fill_color='lightblue')
m.drawcountries(linewidth=2, linestyle='solid', color='k' ) 
m.drawstates(linewidth=0.5, linestyle='solid', color='k')
m.drawrivers(linewidth=0.5, linestyle='solid', color='blue')
def RndState():
    TX=["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    x=randint(1,49)
    return TX[x]

search = RndState()
LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/05-12-2020.csv"
#LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/03-30-2020.csv"
DataIn = open(LASTFILE).readlines()
LAT=[]
LONG=[]
LATd=[]
LONGd=[]
STATES=[]
cases=[]
deaths =[]
longitude = ""
search = RndState()
for line in DataIn:
    line=line.replace("\n","")
    line = line.lstrip(",")
    line = line.split(",")
    #if search in line[2] and "-" in (line[6]):
    if len(line[2])>0 and "-" in (line[6]):    
        text=line[2],line[1],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10]
        STATES.append(text)
        LAT.append(line[5])
        LONG.append(line[6])
        if int(line[8])>0:
            LATd.append(line[5])
            LONGd.append(line[6])        
        cases.append(line[7])
        deaths.append(line[8])
        longitude = longitude+line[6]+","
print(len(STATES))        
LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)
LTd = np.array(LATd,dtype=np.float)
LGd = np.array(LONGd,dtype=np.float)

S=1
Size=[]
for x in cases:
    S=1+(float(x)*.05)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

Sd=0
Sized=[]
for xd in deaths:
    Sd=0+(float(xd)+.05)
    Sized.append(int(Sd))
    #print(int(S))
sd = np.array(Sized)
#print(Sized)
plt.title("COVID-19:\n Cases: (black)\n Deaths(red) \n Location:\n "+search+"\n", fontsize=15, loc='right')
#plt.text(max(LG-1.2),max(LT), search, color='white', fontsize=24)
#x, y = m(lons, lats)  # transform coordinates
x, y = m(LGd, LTd)
xx,yy = m(LG, LT)
plt.xlabel('Longitude',color="white", fontsize=24)
plt.ylabel('Latitute',color="white", fontsize=24)

m.scatter(xx, yy, s=s, color='black', zorder=5, alpha=0.6)
m.scatter(x, y, s=sd, color='r', zorder=10,  alpha=0.6)

plt.savefig("BaseMap/"+search+"Hotspots1__.png", dpi=120, facecolor='salmon', edgecolor='b',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches="tight", pad_inches=0.2,
        frameon=None, metadata=None)




from matplotlib.pyplot import text
from matplotlib import pyplot as plt
import numpy as np
import mpld3
from mpld3 import plugins
import time
%matplotlib inline
#LASTFILE="DATA/Download.csv"
#DataIn = open(LASTFILE).readlines()
cases=[]
#cnt=cnt+1
#for line in DataIn:
#    line = line.split(",")
#    if cnt==0:print(line)

LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"
DataIn = open(LASTFILE).readlines()
LAT=[]
LONG=[]
CITY=[]
deaths=[]
TEXT=[]
cnt = -1
Total=0
SEARCH = "Mississippi"
for line in DataIn:
    if len(line)>10 and 'US' in line and "Recovered" not in line and "Unassigned" not in line:
        cnt=cnt+1
        line=line.replace("\n","")
        line = line.lstrip(",")
        line = line.split(",")
        End=len(line)-1
        if len(line)>5 and SEARCH in line[6] and "0.0" not in line:
            
            if cnt>=1 and cnt<=5:print(line[5],line[6],line[8],line[9], line[End] )
            Total=Total+int(line[End])
            CITY.append(line[5])
            LAT.append(line[8])
            LONG.append(line[9])
            cases.append(line[9])
            deaths.append(line[End])        
            TText = str(line[2]+' '+line[1]+' '+line[3]+' '+line[4]+' '+line[5]+' '+line[6]+' '+line[7]+' '+line[8]+' '+line[9]+' '+line[10])
            if cnt==10:print("TTEXT: ",TText)
            TEXT.append(TText)
            
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

print(deaths[-1])


A = (min(LG))-1
B = (max(LG))+1
C = (min(LT))-1
D = (max(LT))+1

fig = plt.figure(num=None, figsize=(12,12), dpi=80, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()
ax.set_facecolor(('#8eda8b'))

Sd=5
Sized=[]
for xd in deaths:
    Sd=2+(float(xd)*1)
    Sized.append(int(Sd))
    #print(int(S))
sd = np.array(Sized)

S=5
Size=[]
for x in cases:
    S=2+(float(x)*2)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

plt.text(A+.5, D-.5, SEARCH, fontsize=26)
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




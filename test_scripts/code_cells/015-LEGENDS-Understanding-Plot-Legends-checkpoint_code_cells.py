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
HISTORY=[]
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
        HISTORY.append(history)
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

import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D, HandlerTuple


for i in range(0,len(lat)):
    #p1, = plt.scatter(long,lat, s=1, color='blue')
    p2, = plt.plot(long[i],lat[i], s=20, color='red')

l = plt.legend([(p1, p2)], ['Two keys'], numpoints=1,
               handler_map={tuple: HandlerTuple(ndivide=None)})

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
print (sortlegend0,sortlegend1)
plt.legend([(sortlegend0,sortlegend1)], loc='left center', bbox_to_anchor=(-0.1, 1.),
           fontsize=8)

"""
plt.legend(handles=sortlegend, loc='left center', bbox_to_anchor=(-0.1, 1.),
           fontsize=8)
"""
plt.savefig('piechart.png', bbox_inches='tight')


#plt.legend(handles=[line_up, line_down])

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




import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np

x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()
plt.plot(x, np.sin(x), '-b', label='Sine')
plt.plot(x, np.cos(x), '--r', label='Cosine')
plt.axis('equal')
leg = plt.legend();


import requests as req
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
Finding counties with a "threshhold" increase in deaths for the last three consecutive days.
How to inspect last four entries of data to see if the number of deaths has increased:
To make it easy to understand lets use the following three dates instead of data.
May10 May11 May12 May13
Subract May10 from May11 check if the result is above the 'Threshhold'
Subract May11 from May12 check if the result is above the 'Threshhold'
Subract May12 from May13 check if the result is above the 'Threshhold'
If all three conditions are met, print the location and information.
"""    
    
Threshhold = 25
count = 0
STATE =[]
COUNTY =[]
Points =[]
HISTORY=[]
SUM =[]
SORTED =[]
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
        Sum=(int(ALLdata[i][-3])-int(ALLdata[i][-4]))+(int(ALLdata[i][-2])-int(ALLdata[i][-3]))+(int(ALLdata[i][-1])-int(ALLdata[i][-2]))
        SUM.append(Sum)
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
        print ("i="+str(count),deaths,county,state,longitude,latitude,history,Sum)
        SORTED.append([Sum,"i="+str(count),deaths,county,state,longitude,latitude,history])

i=315
print(ALLdata[i][5:7])
DataAsString = ALLdata[i][14:]
print (DataAsString)
DataAsInteger = list(map(int, DataAsString))
x = str(ALLdata[i][5:7]).replace(",","").replace("'","")
filename = ''.join(filter(str.isalnum, x))+".png"
print(filename)
print(". . . .")
print(DataAsInteger)

i=314
print(ALLdata[i][5:7])
DataAsString = ALLdata[i][14:]
print (DataAsString)
DataAsInteger = list(map(int, DataAsString))
x = str(ALLdata[i][5:7]).replace(",","").replace("'","")
filename = ''.join(filter(str.isalnum, x))+".png"
print(filename)
print(". . . .")
print(DataAsInteger)

print(ALLdata[i][5:7])

import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
import time
data = DataAsInteger
variation=[]
previous=0
for i in range(1,len(data)):
    print(data[i]-data[i-1], end = " ")
    variation.append(data[i]-data[i-1])
    
Xv=np.asarray(variation)
Yv = np.asarray(range(0,len(Xv)))

XX = np.asarray(DataAsInteger)
Y = np.asarray(range(0,len(XX)))
fig = plt.figure(num=None, figsize=(5,5), dpi=80, facecolor='salmon')
fig, ax = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
ax[0].grid(color='lightgray', linestyle='-', linewidth=1)
plt.grid(True)
ax[0].plot(Yv,Xv,  '-b', label='Day by Day Variation in Deaths')
ax[1].grid(color='lightgray', linestyle='-', linewidth=1)
plt.grid(True)
ax[1].plot(Y,XX, '-r', label='Day by Day Variation in Deaths')
leg = ax[0].legend();
leg = ax[1].legend();
#filename = "images/2"+(time.strftime('%a_%d_%b_%Y_%I_%M_%S_%p.png'))
filename1 = "images/1"+filename+(time.strftime('%I_%M_%S_%p.png'))
fig.savefig(filename, facecolor=fig.get_facecolor(), edgecolor='black')
plt.rcParams['axes.facecolor']='yellow'
#plt.rcParams['savefig.facecolor']='red'
ax[0].set_facecolor((1,1,1,0))
ax[1].set_facecolor("grey")
fig.savefig(filename1, facecolor=(1,1,1,0))
print(filename)
print(filename1)

from PIL import Image
IM=Image.open("images/1HartfordConnecticut.png01_15_03_PM.png")
IM

from PIL import Image
IM=Image.open("FairfieldConnecticut.png")
IM

x = str(ALLdata[i][5:7]).replace(",","").replace("'","")
s = ''.join(filter(str.isalnum, x))
print(s)

x_values = Yv
y_values = Xv
plt.plot(x_values, y_values)
fig = plt.figure(1)
rect = fig.patch
rect.set_facecolor("salmon")

plt.savefig("figure_with_background.png", facecolor=fig.get_facecolor())

import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np


X = np.log10(DataAsInteger)
Y = np.asarray(range(0,len(X)))

XX = np.asarray(DataAsInteger)
YY = np.asarray(range(0,len(XX)))

fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].grid(color='lightgray', linestyle='-', linewidth=1)
plt.grid(True)
axs[0].plot(Y,X,  '-b', label='Day by Day Variation in Deaths')
axs[1].grid(color='lightgray', linestyle='-', linewidth=1)
plt.grid(True)
axs[1].plot(YY,XX, '-r', label='Day by Day Variation in Deaths')

leg = axs.legend();


def normalize(column):
    upper = column.max()
    lower = column.min()
    y = (column - lower)/(upper-lower)
    return y

data = DataAsInteger
variation=[]
previous=0
for i in range(1,len(data)):
    print(data[i]-data[i-1], end = " ")
    variation.append(data[i]-data[i-1])
Xv=np.asarray(variation)
Yv = np.asarray(range(0,len(Xv)))
fig = plt.figure(num=None, figsize=(5,5), dpi=80, facecolor='salmon')
fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].grid(color='lightgray', linestyle='-', linewidth=1)
plt.grid(True)
axs[0].plot(Yv,Xv,  '-b', label='Day by Day Variation in Deaths')
axs[1].grid(color='lightgray', linestyle='-', linewidth=1)
plt.grid(True)
axs[1].plot(Y,XX, '-r', label='Day by Day Variation in Deaths')

filename = "images/2"+(time.strftime('%a_%d_%b_%Y_%I_%M_%S_%p.png'))
fig.savefig(filename, facecolor=fig.get_facecolor(), edgecolor='black')
print(filename)

filename="images/2Fri_15_May_2020_05_22_44_PM.png"
from PIL import Image
IM=Image.open(filename)
print(IM.size)
IM

import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np

data = DataAsInteger
variation=[]
previous=0
for i in range(1,len(data)):
    print(data[i]-data[i-1], end = " ")
    variation.append(data[i]-data[i-1])
Xv=np.asarray(variation)


#new_list = [x+1 for x in variation]
#Xx=np.log(new_list)

#Y=np.asarray(range(0,len(variation)))
Y = np.linspace(0, 1000, len(X))
fig, ax = plt.subplots()
ax.plot(Y,X, '-b', label='Day by Day Variation in Deaths')
#ax.plot(X, np.cos(X), '--r', label='Cosine')
#ax.axis('equal')
leg = ax.legend();


import numpy as np
import matplotlib.pyplot as plt
import time
list_x = np.asarray(range(0,len(variation)))
list_y = np.asarray(variation)
inc = len(variation)/10
print(inc)

fig = plt.figure(num=None, figsize=(12,12), dpi=120, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

#plt.figure()
poly = np.polyfit(list_x,list_y,inc)
poly_y = np.poly1d(poly)(list_x)
plt.plot(list_x,poly_y)
plt.plot(list_x,list_y)

ax.grid(color='lightgray', linestyle='-', linewidth=1)

plt.grid(True)

def listToString(s):  
    # initialize an empty string 
    str1 = " " 
    # return string   
    return (str1.join(s)) 
i=315
print("i: ",i)        
TExt = listToString(ALLdata[i][5:7])
total = "Total Deaths to Date: "+str(ALLdata[i][-1])
plt.text(0,70, TExt, fontsize=30, color="red")
plt.text(0,65, total, fontsize=30, color="red")
plt.xlabel('- Time Span -\nFirst Data Record : January 21, 2020\nhttps://raw.githubusercontent.com/CSSEGISandData/COVID-19/master\n/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv', fontsize=18)
plt.title('Plotting Day by Day Death Variations from:\n https://github.com/JupyterJones/COVID-19-Jupyter-Notebooks\n Orange is actual, Blue is smoothed', fontsize=18)
plt.ylabel('- Variation -', fontsize=18, color="white")
filename = "images/"+(time.strftime('%a_%d_%b_%Y_%I_%M_%S_%p_%Z', time.gmtime())+".png")
fig.savefig(filename, facecolor=fig.get_facecolor(), edgecolor='black')
print(filename)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

list_x = np.asarray(range(0,len(variation)))
list_y = np.asarray(variation)
inc = len(variation)/10
print(inc)

fig = plt.figure(num=None, figsize=(12,12), dpi=80, facecolor='salmon')
#fig = plt.figure()
ax = fig.gca()

#plt.figure()
poly = np.polyfit(list_x,list_y,inc)
poly_y = np.poly1d(poly)(list_x)
plt.plot(list_x,poly_y)
plt.plot(list_x,list_y)
plt.show()

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

import matplotlib.pyplot as plt
import numpy as np

T = np.array([6, 7, 8, 9, 10, 11, 12])
power = np.array([1.53E+03, 5.92E+02, 2.04E+02, 7.24E+01, 2.72E+01, 1.10E+01, 4.70E+00])

plt.plot(T,power)
plt.show()

from scipy.interpolate import make_interp_spline, BSpline
import numpy as np

#list_x=variation
list_y = np.asarray(range(0,len(variation)))
list_x = np.asarray(variation)

list_x_new = np.linspace(min(list_x), max(list_x), 1000)
list_y_smooth = make_interp_spline(list_x, list_y, list_x_new)

plt.plot(list_x_new, list_y_smooth)
plt.show() 

from scipy.interpolate import make_interp_spline, BSpline

# 300 represents number of points to make between T.min and T.max
xnew = np.linspace(min(variation), max(variation), 300) 
#xnew=np.asarray(variation)
spl = make_interp_spline(variation, power, k=3)  # type: BSpline
power_smooth = spl(xnew)

plt.plot(xnew, power_smooth)
plt.show()

import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np

data = DataAsInteger
variation=[]
previous=0
for i in range(1,len(data)):
    print(data[i]-data[i-1], end = " ")
    variation.append(data[i]-data[i-1])
X=np.asarray(variation)
#Y=np.asarray(range(0,len(variation)))
Y = np.linspace(0, 1000, len(X))
fig, ax = plt.subplots()
ax.plot(Y,X, '-b', label='Day by Day Variation in Deaths')
#ax.plot(X, np.cos(X), '--r', label='Cosine')
ax.axis('equal')
leg = ax.legend();


print("SumLastThreeDays, ItemLine, TotalDeaths, Country, State, Long, Lat, IncreasePerDay(LastThreeDays)\n")
for line in sorted(SORTED, reverse=True):
    print (line)

# To view the header use ALLdata[0] that is the first line:
print ("This is the first line or `The header`.\n",ALLdata[0])

# Use the `i` value ( i=616 ) to view the entire line of data.
# Example:  To see i=616 enter:  616
i =input("Enter a value for `i`: ")
i = int(i)
print ("\nThe data at position ALLdata["+str(i)+"]\n----------\n",ALLdata[i])



for i in range(0,len(COUNTY)):
    #print(COUNTY[i],STATE[i])
    print('{:<12} {:>12}'.format(COUNTY[i],STATE[i]))
    
#Los Angeles  California        

data = DataAsInteger
variation=[]
previous=0
for i in range(1,len(data)):
    print(data[i]-data[i-1], end = " ")
    variation.append(data[i]-data[i-1])




import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D, HandlerTuple
import numpy as np
inc= len(Y)
colorZ = ['yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan','yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan','navy']
colors = colorZ[-inc:]

y=np.asarray(long)
x=np.asarray(lat)


#plt.scatter(y,x, s=40, color=colors)

for i in range(0,len(lat)-1):
    #p1, = plt.plot(float(long[i]),float(lat[i]), color=colors[i])
    plt.scatter(float(long[i]),float(lat[i]), color=colors[i])
    #p3, = plt.text(float(long[i]),float(lat[i]), COUNTY[i])
    #p3, = plt.scatter(float(long[i]),float(lat[i]), color=colors[i])
    print(long[i],lat[i])
    '''
    l = plt.legend([(p2)], ['Two keys'], numpoints=1,
               handler_map={tuple: HandlerTuple(ndivide=None)})
    '''

print(y[1])

colorZ = ['yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan','yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan','navy']

inc= len(y)

colors = colorZ[-inc:]
colorS = colorZ[0:inc]
print(colors)
print(len(colors))
print(colorS)
print(len(colorS))

print(len(y))

negative=plt.scatter(x,y,s=12, color=colors, label='negative')
positive= plt.scatter(y,x,s=6, color=colors,label = 'positive')
plt.legend(handles=[negative,positive])

negative=plt.plot(x,y,linestyle ='dashed', label='negative')
positive= plt.plot(y,x,label = 'positive')
plt.legend(handles=[negative[0],positive[0],])

negative=plt.plot(x,lat,linestyle ='dashed', label='negative')
positive= plt.plot(x,long,label = 'positive')
plt.legend(handles=[negative[0],positive[0]])

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
#plt.legend([(sortlegend0,sortlegend1)], loc='left center', bbox_to_anchor=(-0.1, 1.),
#           fontsize=8)


#l = plt.legend([(sortlegend0,sortlegend1)], ['Two keys'], numpoints=1,
#               handler_map={tuple: HandlerTuple(ndivide=None)})



"""
plt.legend(handles=sortlegend, loc='left center', bbox_to_anchor=(-0.1, 1.),
           fontsize=8)
"""
plt.savefig('piechart.png', bbox_inches='tight')


#plt.legend(handles=[line_up, line_down])

inc= len(Points)
colorZ = ['yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan','yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan','navy']
colors = colorZ[-inc:]


text0 = COUNTY
text = STATE
for i in range(len(Points)):
    x = Points[i][0]
    y = Points[i][1]
    tx = text0[i]+", "+text[i]
    #xx, yy = m(x,y)
    #print(xx, yy)
    print(x, y)
    print(colors[i])
    c=colors[i]
    #plt.plot(xx, yy, 'bo')
    #plt.scatter(xx, yy, s=20, color=c, zorder=5, alpha=0.6)
    #t = plt.text(xx, yy, tx, fontsize=16, color=c)
    plt.scatter(x, y, s=20, color=c, zorder=5, alpha=0.6)
    t = plt.text(x, y, tx, fontsize=16, color=c)

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
    plt.text(xx, yy, tx, fontsize=10, color="white")

filename = "BaseMap/Hotspots__.png"
plt.savefig(filename, dpi=120, facecolor='salmon', edgecolor='b',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches="tight", pad_inches=0.2,
        frameon=None, metadata=None)
    
plt.show()




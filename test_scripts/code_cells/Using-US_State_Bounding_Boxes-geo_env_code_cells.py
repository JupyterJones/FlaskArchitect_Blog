!pwd

%%writefile US_State_Bounding_Boxes.py
"""
Usage with basemap: 
The plus and minus .5 adds about a 35 mile padding to the mapbox:
from US_State_Bounding_Boxes import GetCOOR
search="Ohio"
coor= GetCOOR(search)
urcrnrlat = coor[0]+.5
llcrnrlat = coor[1]-.5
urcrnrlon = coor[2]+.5
llcrnrlon = coor[3]-.5
m = Basemap(llcrnrlon,llcrnrlat,urcrnrlon,urcrnrlat,
             resolution='i', projection='tmerc', lat_0 = lat_0, lon_0 = lon_0)

state="Florida"
COOR(state)
>>> ('Florida', '-87.634938 24.523096 -80.031362 31.000888')
or:
state="Florida"
x=COOR(state)[0]
coor=COOR(state)[1]
print(x,coor)
>>> Florida -87.634938 24.523096 -80.031362 31.000888
st = COOR(state)
print (st[0])
>>> Florida
print (st[1])
>>> -87.634938 24.523096 -80.031362 31.000888
"""

DATA="""
NAME  xmin ymin xmax ymax
Alabama  -88.473227 30.223334 -84.88908 35.008028
Alaska  -179.148909 51.214183 179.77847 71.365162
American Samoa  -171.089874 -14.548699 -168.1433 -11.046934
Arizona  -114.81651 31.332177 -109.045223 37.00426
Arkansas  -94.617919 33.004106 -89.644395 36.4996
California  -124.409591 32.534156 -114.131211 42.009518
Colorado  -109.060253 36.992426 -102.041524 41.003444
Commonwealth of the Northern Mariana Islands  144.886331 14.110472 146.064818 20.553802
Connecticut  -73.727775 40.980144 -71.786994 42.050587
Delaware  -75.788658 38.451013 -75.048939 39.839007
District of Columbia  -77.119759 38.791645 -76.909395 38.99511
Florida  -87.634938 24.523096 -80.031362 31.000888
Georgia  -85.605165 30.357851 -80.839729 35.000659
Guam  144.618068 13.234189 144.956712 13.654383
Hawaii  -178.334698 18.910361 -154.806773 28.402123
Idaho  -117.243027 41.988057 -111.043564 49.001146
Illinois  -91.513079 36.970298 -87.494756 42.508481
Indiana  -88.09776 37.771742 -84.784579 41.760592
Iowa  -96.639704 40.375501 -90.140061 43.501196
Kansas  -102.051744 36.993016 -94.588413 40.003162
Kentucky  -89.571509 36.497129 -81.964971 39.147458
Louisiana  -94.043147 28.928609 -88.817017 33.019457
Maine  -71.083924 42.977764 -66.949895 47.459686
Maryland  -79.487651 37.911717 -75.048939 39.723043
Massachusetts  -73.508142 41.237964 -69.928393 42.886589
Michigan  -90.418136 41.696118 -82.413474 48.2388
Minnesota  -97.239209 43.499356 -89.491739 49.384358
Mississippi  -91.655009 30.173943 -88.097888 34.996052
Missouri  -95.774704 35.995683 -89.098843 40.61364
Montana  -116.050003 44.358221 -104.039138 49.00139
Nebraska  -104.053514 39.999998 -95.30829 43.001708
Nevada  -120.005746 35.001857 -114.039648 42.002207
New Hampshire  -72.557247 42.69699 -70.610621 45.305476
New Jersey  -75.559614 38.928519 -73.893979 41.357423
New Mexico  -109.050173 31.332301 -103.001964 37.000232
New York  -79.762152 40.496103 -71.856214 45.01585
North Carolina  -84.321869 33.842316 -75.460621 36.588117
North Dakota  -104.0489 45.935054 -96.554507 49.000574
Ohio  -84.820159 38.403202 -80.518693 41.977523
Oklahoma  -103.002565 33.615833 -94.430662 37.002206
Oregon  -124.566244 41.991794 -116.463504 46.292035
Pennsylvania  -80.519891 39.7198 -74.689516 42.26986
Puerto Rico  -67.945404 17.88328 -65.220703 18.515683
Rhode Island  -71.862772 41.146339 -71.12057 42.018798
South Carolina  -83.35391 32.0346 -78.54203 35.215402
South Dakota  -104.057698 42.479635 -96.436589 45.94545
Tennessee  -90.310298 34.982972 -81.6469 36.678118
Texas  -106.645646 25.837377 -93.508292 36.500704
United States Virgin Islands  -65.085452 17.673976 -64.564907 18.412655
Utah  -114.052962 36.997968 -109.041058 42.001567
Vermont  -73.43774 42.726853 -71.464555 45.016659
Virginia  -83.675395 36.540738 -75.242266 39.466012
Washington  -124.763068 45.543541 -116.915989 49.002494
West Virginia  -82.644739 37.201483 -77.719519 40.638801
Wisconsin  -92.888114 42.491983 -86.805415 47.080621
Wyoming  -111.056888 40.994746 -104.05216 45.005904
"""
def GetCOOR(state):
    STATElist=DATA.split("\n")
    for States in STATElist:
        if state in States:
            Statez = States.split("  ")
            StateS = Statez[1].split(" ")
            urcrnrlat = float(StateS[3])
            llcrnrlat = float(StateS[1])
            urcrnrlon = float(StateS[2])
            llcrnrlon = float(StateS[0])
            return urcrnrlat,llcrnrlat,urcrnrlon,llcrnrlon

def COOR(state):
    STATElist=DATA.split("\n")
    for States in STATElist:
        if state in States:
            COOR=States.split("  ")
            state = COOR[0]
            coor =COOR[1]
            return state,coor

from US_State_Bounding_Boxes import *
state="New York"        
GetCOOR(state)        

from US_State_Bounding_Boxes import *
state="New York"
print(GetCOOR(state))


%%writefile GetShape.py
#!/usr/bin/env python
# zipfile37 is for python 3.7 zipfile36 for python 36 etc
# Creates a directory 'ShapeFiles' then downloads and extracts shapefiles there.
import requests
import os
from zipfile37 import ZipFile
def Getshape():
    if not os.path.exists('ShapeFiles'):
        os.makedirs('ShapeFiles')
    url = 'http://pubs.usgs.gov/of/2005/1071/data/background/us_bnds/state_bounds.zip'
    r = requests.get(url, allow_redirects=True)
    open('ShapeFiles/state_bounds.zip', 'wb').write(r.content)
    # Create a ZipFile Object and load sample.zip in it
    with ZipFile('ShapeFiles/state_bounds.zip', 'r') as zipObj:
        # Extract all the contents of zip file in current directory
        zipObj.extractall("ShapeFiles")

if __name__=="__main__":
    if not os.path.exists('ShapeFiles/state_bounds.shp'):
        Getshape()
    else:
        entries = os.listdir('ShapeFiles/')
        for entry in entries:
            print(entry)

!ls COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/04-2*

!wget --no-check-certificate http://pubs.usgs.gov/of/2005/1071/data/background/us_bnds/state_bounds.zip

!ls /home/jack/miniconda3/envs/geo_env/share

!ls /home/jack/miniconda3/envs/geo_env/lib/python3.9

import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import xarray as xy
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import os

import os
import sys
os.environ['PROJ_LIB'] = '/home/jack/miniconda3/envs/geo_env/share/proj'
sys.path.append("/home/jack/miniconda3/envs/geo_env/lib/python3.9/site-packages/") # go to parent dir
from mpl_toolkits.basemap import Basemap


#%matplotlib notebook
from mpl_toolkits.basemap import Basemap
%matplotlib inline
from US_State_Bounding_Boxes import GetCOOR # get coordinates for state(box)
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
search="Ohio"
fig = plt.figure(num=None, figsize=(12,10), dpi=80, facecolor='salmon')
coor= GetCOOR(search)
urcrnrlat = coor[0]+.5
llcrnrlat = coor[1]-.5
urcrnrlon = coor[2]+.5
llcrnrlon = coor[3]-.5

lat_0 = (urcrnrlat+llcrnrlat)/2
lon_0 =(urcrnrlon+llcrnrlon)/2
print(lat_0/lon_0)

#fig = plt.gcf()
#fig.set_size_inches(8, 6.5)


m = Basemap(llcrnrlon,llcrnrlat,urcrnrlon,urcrnrlat,
             resolution='i', projection='tmerc', lat_0 = lat_0, lon_0 = lon_0)
# Shapefile resource:
# http://pubs.usgs.gov/of/2005/1071/data/background/us_bnds/state_bounds.zip

#FILE="stateboundaries/state_boundaries.shp"
#StateBounds/state_bounds.shp
#r = shapefile.Reader(filepath, encoding = "utf-8")

m.readshapefile(r'./StateBounds/state_bounds', 'Neighborhoods')
#m.readshapefile(r'ShapeFiles/state_bounds', 'Neighborhoods')
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='#ddaa66',lake_color='aqua')
m.drawcoastlines()
m.drawrivers(linewidth=1.0,color='navy',zorder=8)
m.drawcounties(linewidth=1.0, linestyle='solid', color='gray', antialiased=1, facecolor='lightgreen', ax=None, zorder=2, drawbounds=True)
m.drawstates(linewidth=1.5, linestyle='solid', color='black', antialiased=1,zorder=2, )
plt.text(urcrnrlon,urcrnrlat, search, color='black', fontsize=24.5, zorder=6,bbox=dict(facecolor='salmon'))
plt.savefig("BaseMap/"+search+"Counties__.png", dpi=120, facecolor='salmon', edgecolor='b', bbox_inches="tight", pad_inches=0.2)
plt.show()

from PIL import Image
IM= Image.open("BaseMap/"+search+"Counties__.png")
print(IM.size)
IM

from PIL import Image
IM= Image.open("BaseMap/"+search+"Counties__.png")
print(IM.size)
IM

import warnings
warnings.filterwarnings("ignore")
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.pyplot import text
from zipfile37 import ZipFile
import requests
import numpy as np
from matplotlib.font_manager import FontProperties
from US_State_Bounding_Boxes import GetCOOR # get coordinates for state(box)
import os
import ipywidgets as wdg  #ipython notebook widgets

!pip install zipfile37

from zipfile37 import ZipFile

from zipfile37 import ZipFile
import requests

url = 'http://pubs.usgs.gov/of/2005/1071/data/background/us_bnds/state_bounds.zip'
r = requests.get(url, allow_redirects=True)
open('state_bounds.zip', 'wb').write(r.content)
# Create a ZipFile Object and load sample.zip in it
with ZipFile('state_bounds.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()

!mkdir ShapeFiles

!mv state* ShapeFiles

%matplotlib notebook
#%matplotlib inline
import warnings
warnings.filterwarnings("ignore")
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.pyplot import text
from zipfile37 import ZipFile
import requests
import numpy as np
from matplotlib.font_manager import FontProperties
from US_State_Bounding_Boxes import GetCOOR # get coordinates for state(box)
import os
import ipywidgets as wdg  #ipython notebook widgets
"""
When I tried to draw counties, I got error: basemap 'utf-8' codec can't decode byte 0xf1 in position
Answered on https://stackoverflow.com/questions/45660904/matplotlib-basemap-drawcounties-having-issues

Budi said, for me, i change return v.decode(encoding, encodingErrors) to return v.decode('latin-1') and it's works,, – Budi Mulyo May 27 '19 at 8:12

My file looked different than you described: so I opened /miniconda3/lib/python3.7/site-packages/shapefile.py and replaced all instances of 'utf-8' with 'latin-1' Itt works fine now. 
Thank you very much. – JackNorthrup 3 mins ago

"""
def Getshape():
    if not os.path.exists('ShapeFiles'):
        os.makedirs('ShapeFiles')
    url = 'http://pubs.usgs.gov/of/2005/1071/data/background/us_bnds/state_bounds.zip'
    r = requests.get(url, allow_redirects=True)
    open('ShapeFiles/state_bounds.zip', 'wb').write(r.content)
    # Create a ZipFile Object and load sample.zip in it
    with ZipFile('ShapeFiles/state_bounds.zip', 'r') as zipObj:
       # Extract all the contents of zip file in current directory
       zipObj.extractall("ShapeFiles")

if not os.path.exists('ShapeFiles/state_bounds.shp'):
    Getshape
    
LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/04-25-2020.csv"
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
search = "Ohio"
for line in DataIn:
    line=line.replace("\n","")
    line = line.lstrip(",")
    line = line.split(",")
    if search in line[2] and "-" in (line[6]):
        #print(line[2],line[1],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10])
        STATES.append(text)
        LAT.append(line[5])
        LONG.append(line[6])
        cases.append(line[7])
        deaths.append(line[8])
        if int(line[8])>0:
            LATd.append(line[5])
            LONGd.append(line[6])            
        longitude = longitude+line[6]+","

LT = np.array(LAT,dtype=np.float)
LG = np.array(LONG,dtype=np.float)
LTd = np.array(LATd,dtype=np.float)
LGd = np.array(LONGd,dtype=np.float)
fig = plt.figure(num=None, figsize=(12,10), dpi=80, facecolor='salmon')


coor= GetCOOR(search)
urcrnrlat = coor[0]+.5
llcrnrlat = coor[1]-.5
urcrnrlon = coor[2]+.5
llcrnrlon = coor[3]-.5

lat_0 = (urcrnrlat+llcrnrlat)/2
lon_0 =(urcrnrlon+llcrnrlon)/2

lats = LT
lons = LG

latsd = LTd
lonsd = LGd

fig = plt.gcf()
fig.set_size_inches(8, 6.5)


m = Basemap(llcrnrlon,llcrnrlat,urcrnrlon,urcrnrlat,
             resolution='i', projection='tmerc', lat_0 = lat_0, lon_0 = lon_0)
# Shapefile resource:
# http://pubs.usgs.gov/of/2005/1071/data/background/us_bnds/state_bounds.zip
m.readshapefile(r'ShapeFiles/state_bounds', 'Neighborhoods')
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='#ddaa66',lake_color='aqua')
m.drawcoastlines()
m.drawrivers()
#m.drawcounties(linewidth=0.1, linestyle='solid', color='k', antialiased=1, facecolor='none', ax=None, zorder=None, drawbounds=False)
m.drawcounties(zorder=20)
S=1
Size=[]
for x in cases:
    S=1+(float(x)*.5)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

Sd=0
Sized=[]
for xd in deaths:
    Sd=0+(float(xd)*1)
    Sized.append(int(Sd))
    #print(int(S))
sd = np.array(Sized)
print(len(deaths),deaths)
'''
# Create and display textarea widget
txt = wdg.Textarea(
    value='',
    placeholder='',
    description='event:',
    disabled=False
)
display(txt)

# Define a callback function that will update the textarea
def onclick(event):
    txt.value = str(event)  # Dynamically update the text box above

'''



plt.text(urcrnrlon,urcrnrlat, search, color='white', fontsize=24, zorder=10,bbox=dict(facecolor='salmon'))
plt.text(lon_0,lat_0, search, color='black', fontsize=24.75)
x, y = m(lons, lats)  # transform coordinates
xx, yy = m(lonsd, latsd)  # transform coordinates 
plt.scatter(x, y,  s=s, color="black", zorder=3, alpha=.5)


# Create and display textarea widget
txt = wdg.Textarea(
    value='',
    placeholder='',
    description='event:',
    disabled=False
)
display(txt)

# Define a callback function that will update the textarea
def onclick(event):
    txt.value = str(event)  # Dynamically update the text box above






plt.scatter(xx, yy,  s=sd, color="red", zorder=6)

plt.savefig("BaseMap/"+search+"Counties__.png", dpi=200, facecolor='salmon', edgecolor='b',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches="tight", pad_inches=0.2,
        frameon=None, metadata=None)
plt.show()

TD=0
for num in deaths:
    TD=TD+int(num)
print(TD)    



from PIL import Image
IM = Image.open("BaseMap/"+search+"Counties__.png")
IM

LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/04-25-2020.csv"
#LASTFILE="csse_covid_19_data/csse_covid_19_daily_reports/03-30-2020.csv"
DataIn = open(LASTFILE).readlines()
LAT=[]
LONG=[]
STATES=[]
cases=[]
deaths =[]
longitude = ""
search = "Wyoming"
cnt=0
for line in DataIn:
    if cnt==0:print(line)
    cnt=cnt+1
    line=line.replace("\n","")
    line = line.lstrip(",")
    line = line.split(",")
    if search in line[2] and "-" in (line[6]) and int(line[8]) >0:
    
        print(line[5],line[6],line[7],line[8])

%%writefile RandomState.py
from random import randint
def RndState():
    TX=["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    x=randint(0,49)
    return TX[x]

import RandomState
state = RandomState.RndState()
print (state)

import geopandas as gdp
import urllib
import zipfile
urllib.request.urlretrieve("https://s3.amazonaws.com/nyc-tlc/misc/taxi_zones.zip", "taxi_zones.zip")
with zipfile.ZipFile("taxi_zones.zip","r") as zip_ref:
    zip_ref.extractall("./shape")

sf = gpd.read_file(r"../shape/taxi_zones.shp")




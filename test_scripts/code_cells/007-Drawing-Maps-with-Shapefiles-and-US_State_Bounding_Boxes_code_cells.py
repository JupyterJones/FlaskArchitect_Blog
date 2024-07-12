!pwd

import sqlite3
from datetime import datetime
from time import gmtime, strftime
import glob
import time
import os
import requests
stringTEXT = ""
if not os.path.exists('state-data/DATA'):
    os.makedirs('state-data/DATA')
print (time.strftime('%a_%d_%b_%Y_%I_%M_%S_%p_%Z', time.gmtime())+".html")
filename = "state-data/DATA/US_State_Bounding_Boxes.csv"
DataIn = open(filename,"w")

BoundingBoxes = ""
response = requests.get('https://gist.githubusercontent.com/a8dx/2340f9527af64f8ef8439366de981168/raw/81d876daea10eab5c2675811c39bcd18a79a9212/US_State_Bounding_Boxes.csv')
filename = "state-data/DATA/US_State_Bounding_Boxes.csv"
with open(filename, mode='wb') as localfile:
    localfile.write(response.content)


!ls state-data/DATA

filename = "state-data/DATA/US_State_Bounding_Boxes.csv"
output = open(filename,"r").readlines()
for line in output:
    line=line.replace("\n","")
    print(line)

EX="01,AL,Alabama,-88.473227,30.223334,-84.88908,35.008028"
print(EX[6:])

File = b"/home/jack/Desktop/state-data/DATA/US_State_Bounding_Boxes.csv"
BOXES = []
DataOut = open(File, "r").readlines()
cnt= 0

for items in DataOut:
    cnt=cnt+1
    items=items.replace('\n','')
    clean=items.replace('"','')
    clean = clean.split(',')
    print(" ".join(clean[3:]))
    entry=" ".join(clean[3:])
    BOXES.append(entry)

%%writefile US_State_Bounding_Boxes.py
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
            States = States.replace("  "," ")
            States = States.split(" ")
            urcrnrlat = float(States[4])
            llcrnrlat = float(States[2])
            urcrnrlon = float(States[3])
            llcrnrlon = float(States[1])
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
coor= GetCOOR("Michigan")
print(coor[0],coor[1],coor[2],coor[3])

from US_State_Bounding_Boxes import GetCOOR
coor= GetCOOR("Michigan")
urcrnrlat = coor[0]
llcrnrlat = coor[1]
urcrnrlon = coor[2]
llcrnrlon = coor[3]

%matplotlib inline
import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", palette="pastel", color_codes=True)
sns.mpl.rc("figure", figsize=(10,6))



!cp -a /mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/home/jack/Desktop/state-data/* state-data

!cp /home/jack/Desktop/state-data/tl_2010_us_state10.sh state-data/DATA/

shp_path = "state-data/tl_2010_us_state10.sh"
sf = shp.Reader(shp_path)

len(sf.shapes())

# How many elements in the record ?
len(sf.records()[1])

sf.records()[1]

sf.records()[1][5]

import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid", palette="pastel", color_codes=True)
sns.mpl.rc("figure", figsize=(10,6))
%matplotlib inline
shp_path = "state-data/tl_2010_us_state10.sh"
sf = shp.Reader(shp_path)

print(len(sf.shapes()))
print(sf.records()[1])
#comuna = 'Pennsylvania'
#com_id = df[df.NOM_COMUNA == comuna].index.get_values()[0]
#plot_shape(com_id, comuna)

def read_shapefile(sf):
    """
    Read a shapefile into a Pandas dataframe with a 'coords' 
    column holding the geometry information. This uses the pyshp
    package
    """
    fields = [x[0] for x in sf.fields][1:]
    records = sf.records()
    shps = [s.points for s in sf.shapes()]
    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)
    return df

df = read_shapefile(sf)
df.shape

df.sample(5)

df[df.NAME10 == 'Pennsylvania']

df['NAME10']

def plot_shape(id, s=None):
    """ PLOTS A SINGLE SHAPE """
    plt.figure()
    ax = plt.axes()
    ax.set_aspect('equal')
    shape_ex = sf.shape(id)
    x_lon = np.zeros((len(shape_ex.points),1))
    y_lat = np.zeros((len(shape_ex.points),1))
    for ip in range(len(shape_ex.points)):
        x_lon[ip] = shape_ex.points[ip][0]
        y_lat[ip] = shape_ex.points[ip][1]
        plt.plot(x_lon,y_lat) 
    x0 = np.mean(x_lon)
    y0 = np.mean(y_lat)
    plt.text(x0, y0, s, fontsize=10)
    # use bbox (bounding box) to set plot limits
    plt.xlim(shape_ex.bbox[0],shape_ex.bbox[2])
    return x0, y0

plot_shape(12, s=None)

def plot_map(sf, x_lim = None, y_lim = None, figsize = (11,9)):
    '''
    Plot map with lim coordinates
    '''
    plt.figure(figsize = figsize)
    id=0
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        plt.plot(x, y, 'k')
        
        if (x_lim == None) & (y_lim == None):
            x0 = np.mean(x)
            y0 = np.mean(y)
            plt.text(x0, y0, id, fontsize=10)
        id = id+1
    
    if (x_lim != None) & (y_lim != None):     
        plt.xlim(x_lim)
        plt.ylim(y_lim)

plot_map(sf,1)

import US_State_Bounding_Boxes
help(US_State_Bounding_Boxes)

from US_State_Bounding_Boxes import *
state="Ohio"
GetCOOR(state)

from US_State_Bounding_Boxes import *
state="Ohio"
a,b,c,d = GetCOOR(state)
c,b
d,a

%%writefile US_State_Bounding_Boxes.py
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
            States = States.split("  ")[-1]
            States = States.split(" ")
            urcrnrlat = float(States[3])
            llcrnrlat = float(States[1])
            urcrnrlon = float(States[2])
            llcrnrlon = float(States[0])
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
state="Ohio"
COOR(state)

from US_State_Bounding_Boxes import *
state="New York"
GetCOOR(state)

from US_State_Bounding_Boxes import *
#state="Ohio"
#state="Maine"
state="Florida"
#state="Michigan"
a,b,c,d = GetCOOR(state)
#c,b
#d,a
#y_lim = (38.403202,41.977523) # latitude 
#x_lim = (-84.820159, -80.518693) # longitude

padding = .5
y_lim = (b-padding,a+padding) # latitude 
x_lim = (d-padding,c+padding) # longitude
plot_map(sf, x_lim, y_lim)

y_lim = (38.403202,41.977523) # latitude 
x_lim = (-84.820159, -80.518693) # longitude
plot_map(sf, x_lim, y_lim)

y_lim = (37.5,42.5) # latitude 
x_lim = (-86, -80) # longitude
plot_map(sf, x_lim, y_lim)




fig=plt.figure()

%matplotlib notebook
import mplcursors
from matplotlib.pyplot import text
import numpy as np
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import matplotlib.pyplot as plt
import numpy as np
import mpld3
from mpld3 import plugins
from PIL import Image

LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/04-14-2020.csv"


DataIn = open(LASTFILE).readlines()
cnt=-1
LAT =[]
LON =[]
cases = []
STate = 'Florida'
for lines in DataIn:
    lines = lines.replace("\n","")
    line = lines.split(",")
    if STate in line[2] and len(line[5])>8 and len(line[6])>4:
        cnt=cnt+1
        if cnt<5:
            print(" ")
            #print(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
        LAT.append(line[5]) 
        LON.append(line[6])
        cases.append(int(line[7]))
LA = LAT
LO = LON
LT = np.array(LAT,dtype=np.float)
LG = np.array(LON,dtype=np.float)

#fig = plt.figure(num=None, figsize=(8,8), dpi=80, facecolor='salmon')
ax = fig.gca()
ax.set_facecolor(('#c2efc1'))

S=1
Size=[]
for x in cases:
    S=1+(float(x)*.1)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

A =(min(LG))-3
B =(max(LG))+3
C =(min(LT))-3
D =(max(LT))+3
fig = plt.figure(num=None, figsize=(8,8), dpi=80, facecolor='salmon')



longLeft= (min(LG))-3
longRight = (max(LG))+3
lat1 = (min(LT))-3
lat2 = (max(LT))+3

ax = fig.gca()
T= 'Miami-Dade'
text(0.62, 0.29, T, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

plt.axis([longLeft,longRight,lat1,lat2])

ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.grid(True)
plt.scatter(LG, LT, s=s, color="black")


plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
mplcursors.cursor(hover=True)

plt.show()

%matplotlib notebook
import mplcursors
from matplotlib.pyplot import text
import numpy as np
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import matplotlib.pyplot as plt
import numpy as np
import mpld3
from mpld3 import plugins
from PIL import Image

LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/04-02-2020.csv"

DataIn = open(LASTFILE).readlines()
cnt=-1
LAT =[]
LON =[]
cases = []
STate = 'Florida'
for lines in DataIn:
    lines = lines.replace("\n","")
    line = lines.split(",")
    if STate in line[2] and len(line[5])>8 and len(line[6])>4:
        cnt=cnt+1
        if cnt<5:
            print(" ")
            #print(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
        LAT.append(line[5]) 
        LON.append(line[6])
        cases.append(int(line[7]))
LA = LAT
LO = LON
LT = np.array(LAT,dtype=np.float)
LG = np.array(LON,dtype=np.float)

fig = plt.figure(num=None, figsize=(8,8), dpi=80, facecolor='salmon')
ax = fig.gca()
ax.set_facecolor(('#c2efc1'))

S=1
Size=[]
for x in cases:
    S=1+(float(x)*.1)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

A =(min(LG))-3
B =(max(LG))+3
C =(min(LT))-3
D =(max(LT))+3

longLeft= (min(LG))-3
longRight = (max(LG))+3
lat1 = (min(LT))-3
lat2 = (max(LT))+3

ax = fig.gca()
T= 'Miami-Dade'
text(0.62, 0.29, T, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

plt.axis([longLeft,longRight,lat1,lat2])

ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.grid(True)
plt.scatter(LG, LT, s=s, color="black")

plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
mplcursors.cursor(hover=True)

plt.show()

%matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
import mplcursors


#fig, ax = plt.subplots()
fig = plt.figure(num=None, figsize=(8,8), dpi=80, facecolor='salmon')
plt.grid(True)
plt.scatter(LG, LT, s=s, color="black")



#ax.scatter(LG, LT)
#ax.set_title("Mouse over a point")

mplcursors.cursor(hover=True)

plt.show()


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

from matplotlib.pyplot import text
import numpy as np
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import matplotlib.pyplot as plt
import numpy as np
import mpld3
%matplotlib inline  
from mpld3 import plugins
from PIL import Image
img=Image.open("mouse-sizing-n-cropping-files/soil600.jpg")

LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/04-02-2020.csv"
#im = np.array(Image.open('mouse-sizing-n-cropping-files/soil600.jpg'))

DataIn = open(LASTFILE).readlines()
cnt=-1
LAT =[]
LON =[]
cases = []
STate = 'Florida'
for lines in DataIn:
    lines = lines.replace("\n","")
    line = lines.split(",")
    if STate in line[2] and len(line[5])>8 and len(line[6])>4:
        cnt=cnt+1
        if cnt<5:
            print(" ")
            #print(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
        LAT.append(line[5]) 
        LON.append(line[6])
        cases.append(int(line[7]))
LA = LAT
LO = LON
LT = np.array(LAT,dtype=np.float)
LG = np.array(LON,dtype=np.float)

#fig = plt.figure(num=None, figsize=(8,8), dpi=80, facecolor='salmon')
ax = fig.gca()
ax.set_facecolor(('#c2efc1'))

S=1
Size=[]
for x in cases:
    S=1+(float(x)*.1)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

A =(min(LG))-3
B =(max(LG))+3
C =(min(LT))-3
D =(max(LT))+3
#fig = plt.figure(num=None, figsize=(8,8), dpi=80, facecolor='salmon')
#fig, ax = plt.subplots(figsize=(8,8), dpi=80, facecolor='salmon')
#im = ax.imshow(img, extent=(A, B, C, D),
#               origin='upper', zorder=0, interpolation='nearest')
#plugins.connect(fig, plugins.MousePosition(fontsize=14))
#mpld3.display()

ax = fig.gca()
T= 'Miami-Dade'
text(0.62, 0.29, T, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

plt.axis([A, B, C, D])
#plugins.connect(ax, plugins.MousePosition(fontsize=14))

ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.grid(True)
plt.scatter(LG, LT, s=s, color="black")
fig, ax = plt.subplots(figsize=(8,8), dpi=80, facecolor='salmon')
plugins.connect(fig, plugins.MousePosition(fontsize=14))
im = ax.imshow(img, extent=(A, B, C, D),
               origin='upper', zorder=0, interpolation='nearest')

mpld3.display()

plt.show()
#from PIL import Image
#im = np.array(Image.open('mouse-sizing-n-cropping-files/soil600.jpg'))
#plugins.connect(fig, plugins.MousePosition(fontsize=14))

mpld3.display()



from matplotlib.pyplot import text
import numpy as np
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import matplotlib.pyplot as plt
import numpy as np
import mpld3
%matplotlib inline  
from mpld3 import plugins
from PIL import Image
img=Image.open("mouse-sizing-n-cropping-files/soil600.jpg")

LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/04-02-2020.csv"
#im = np.array(Image.open('mouse-sizing-n-cropping-files/soil600.jpg'))

DataIn = open(LASTFILE).readlines()
cnt=-1
LAT =[]
LON =[]
cases = []
STate = 'Florida'
for lines in DataIn:
    lines = lines.replace("\n","")
    line = lines.split(",")
    if STate in line[2] and len(line[5])>8 and len(line[6])>4:
        cnt=cnt+1
        if cnt<5:
            print(" ")
            #print(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
        LAT.append(line[5]) 
        LON.append(line[6])
        cases.append(int(line[7]))
LA = LAT
LO = LON
LT = np.array(LAT,dtype=np.float)
LG = np.array(LON,dtype=np.float)

#fig = plt.figure(num=None, figsize=(8,8), dpi=80, facecolor='salmon')
ax = fig.gca()
ax.set_facecolor(('#c2efc1'))

S=1
Size=[]
for x in cases:
    S=1+(float(x)*.1)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

A =(min(LG))-3
B =(max(LG))+3
C =(min(LT))-3
D =(max(LT))+3
#fig = plt.figure(num=None, figsize=(8,8), dpi=80, facecolor='salmon')
fig, ax = plt.subplots(figsize=(8,8), dpi=80, facecolor='salmon')
im = ax.imshow(img, extent=(A, B, C, D),
               origin='upper', zorder=0, interpolation='nearest')
plugins.connect(fig, plugins.MousePosition(fontsize=14))

longLeft= (min(LG))-3
longRight = (max(LG))+3
lat1 = (min(LT))-3
lat2 = (max(LT))+3

ax = fig.gca()
T= 'Miami-Dade'
text(0.62, 0.29, T, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

plt.axis([longLeft,longRight,lat1,lat2])

ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.grid(True)
plt.scatter(LG, LT, s=s, color="black")

#im = ax.imshow(img, extent=(A, B, C, D),
#               origin='lower', zorder=1, interpolation='nearest')

plt.xlabel('First data sample was: 09/03/2020 04:30:00')
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
plt.show()

plugins.connect(fig, plugins.MousePosition(fontsize=14))

mpld3.display()



from matplotlib.pyplot import text
import numpy as np
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import matplotlib.pyplot as plt
import numpy as np
import mpld3
%matplotlib inline  
from mpld3 import plugins
from PIL import Image
img=Image.open("mouse-sizing-n-cropping-files/soil600.jpg")

LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/04-02-2020.csv"
#im = np.array(Image.open('mouse-sizing-n-cropping-files/soil600.jpg'))

DataIn = open(LASTFILE).readlines()
cnt=-1
LAT =[]
LON =[]
cases = []
STate = 'Florida'
for lines in DataIn:
    lines = lines.replace("\n","")
    line = lines.split(",")
    if STate in line[2] and len(line[5])>8 and len(line[6])>4:
        cnt=cnt+1
        if cnt<5:
            print(" ")
            #print(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
        LAT.append(line[5]) 
        LON.append(line[6])
        cases.append(int(line[7]))
LA = LAT
LO = LON
LT = np.array(LAT,dtype=np.float)
LG = np.array(LON,dtype=np.float)

#fig = plt.figure(num=None, figsize=(8,8), dpi=80, facecolor='salmon')
ax = fig.gca()
ax.set_facecolor(('#c2efc1'))

S=1
Size=[]
for x in cases:
    S=1+(float(x)*.1)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

A =(min(LG))-3
B =(max(LG))+3
C =(min(LT))-3
D =(max(LT))+3
#fig = plt.figure(num=None, figsize=(8,8), dpi=80, facecolor='salmon')
fig, ax = plt.subplots(figsize=(8,8), dpi=80, facecolor='salmon')
im = ax.imshow(img, extent=(A, B, C, D),
               origin='upper', zorder=0, interpolation='nearest')
plugins.connect(fig, plugins.MousePosition(fontsize=14))
mpld3.display()

ax = fig.gca()
T= 'Miami-Dade'
text(0.62, 0.29, T, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

plt.axis([A, B, C, D])

ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.grid(True)
plt.scatter(LG, LT, s=s, color="black")

#im = ax.imshow(img, extent=(A, B, C, D),
#               origin='lower', zorder=1, interpolation='nearest')

#plt.xlabel('First data sample was: 09/03/2020 04:30:00')
#plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
#plt.ylabel('Number of Cases')
plt.show()
from PIL import Image
im = np.array(Image.open('mouse-sizing-n-cropping-files/soil600.jpg'))
plugins.connect(fig, plugins.MousePosition(fontsize=14))

mpld3.display()



from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import matplotlib.pyplot as plt
import numpy as np
import mpld3
%matplotlib inline  
from mpld3 import plugins
from PIL import Image
img=Image.open("mouse-sizing-n-cropping-files/soil600.jpg")
 

fig, ax = plt.subplots()
im = ax.imshow(img, extent=(10, 20, 10, 20),
               origin='upper', zorder=1, interpolation='nearest')

plugins.connect(fig, plugins.MousePosition(fontsize=14))
mpld3.display()
from PIL import Image
im = np.array(Image.open('mouse-sizing-n-cropping-files/soil600.jpg'))
plt.show()
plugins.connect(fig, plugins.MousePosition(fontsize=14))

mpld3.display()


%matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
import mplcursors
np.random.seed(42)

fig, ax = plt.subplots()
ax.scatter(*np.random.random((2, 26)))
ax.set_title("Mouse over a point")

mplcursors.cursor(hover=True)

plt.show()


%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt

company=['google','amazon','msft','fb']
revenue=[80,68,54,27]

fig=plt.figure()
ax=plt.subplot()

xpos=np.arange(len(company))

bars = plt.bar(xpos,revenue)


annot = ax.annotate("", xy=(0,0), xytext=(-20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="black", ec="b", lw=2),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(bar):
    x = bar.get_x()+bar.get_width()/2.
    y = bar.get_y()+bar.get_height()
    annot.xy = (x,y)
    text = "({:.2g},{:.2g})".format( x,y )
    annot.set_text(text)
    annot.get_bbox_patch().set_alpha(0.4)


def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        for bar in bars:
            cont, ind = bar.contains(event)
            if cont:
                update_annot(bar)
                annot.set_visible(True)
                fig.canvas.draw_idle()
                return
    if vis:
        annot.set_visible(False)
        fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show()

import mplcursors
help(mplcursors)

%matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np


def plot_unit_circle():
    angs = np.linspace(0, 2 * np.pi, 10**6)
    rs = np.zeros_like(angs) + 1
    xs = rs * np.cos(angs)
    ys = rs * np.sin(angs)
    plt.plot(xs, ys)


def mouse_move(event):
    x, y = event.xdata, event.ydata
    print(x, y)


plt.connect('motion_notify_event', mouse_move)
plot_unit_circle()
plt.axis('equal')
plt.show()

%matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as wdg  # Using the ipython notebook widgets

# Create a random image
a = np.random.poisson(size=(12,15))
fig = plt.figure()
plt.imshow(a)

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

# Create an hard reference to the callback not to be cleared by the garbage collector
ka = fig.canvas.mpl_connect('button_press_event', onclick)




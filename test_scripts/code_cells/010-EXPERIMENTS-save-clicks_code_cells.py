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

collector = []
def onclick(event):
    global i, collector
    collector.append((event.xdata, event.ydata))
    # Open the annotations file to continue to write
    target = open('annotation.txt', 'a')
    # Write picture and coordinates
    target.write(line)
    target.write("\n")
    i += 1
    event.canvas.figure.clear()
    event.canvas.figure.gca().imshow(images[i])

fig = plt.figure(figsize=(5,5))
fig.canvas.mpl_connect('button_press_event', onclick)

plt.imshow(images[0])
plt.show()

%matplotlib notebook
from matplotlib import pyplot as plt
import mplcursors
from pandas import DataFrame
collector = []
def onclick(event):
    global i, collector
    collector.append((event.xdata, event.ydata))
    # Open the annotations file to continue to write
    target = open('annotation.txt', 'a')
    # Write picture and coordinates
    target.write(line)
    target.write("\n")
    i += 1
    event.canvas.figure.clear()
    event.canvas.figure.gca().imshow(images[i])






#fig = plt.figure(figsize=(5,5))
#fig.canvas.mpl_connect('button_press_event', onclick)

df = DataFrame(
    [("Alice", 163, 54),
     ("Bob", 174, 67),
     ("Charlie", 177, 73),
     ("Diane", 168, 57)],
    columns=["name", "height", "weight"])
scatter1 = df.plot.scatter("height", "weight")
mplcursors.cursor(scatter1, hover=True).connect("add",
    lambda sel: sel.annotation.set_text(
        f'{df["name"][sel.target.index]}\nHeight: {df["height"][sel.target.index] / 100} m\nWeight: {df["weight"][sel.target.index]} kg'))


plt.show()

print(collector)

from matplotlib import pyplot as plt
import mplcursors
from pandas import DataFrame
collector = []
df = DataFrame(
    [("Alice", 163, 54),
     ("Bob", 174, 67),
     ("Charlie", 177, 73),
     ("Diane", 168, 57)],
    columns=["name", "height", "weight"])
scatter1 = df.plot.scatter("height", "weight")
mplcursors.cursor(scatter1, hover=True).connect("add",
    lambda sel: sel.annotation.set_text(
        f'{df["name"][sel.target.index]}\nHeight: {df["height"][sel.target.index] / 100} m\nWeight: {df["weight"][sel.target.index]} kg'))
plt.show()

import ipywidgets as widgets
import numpy as np
import pandas as pd

vartest = 0

Button = widgets.Button(description='Search', disabled=False, button_style='info', tooltip='Search')
display(Button)

def whenclick2(b):
    global df

    if vartest==0:
        df = pd.DataFrame(np.arange(5))


        class displayDF(object):
            def _create_widgets(self):
                self.button = Button
                self.button.on_click(self._on_button_clicked) # define which function to run when cliked

            def _on_button_clicked(self, change):
                self.out.clear_output() # clean previous outptu (I think ). Not working
                with self.out:# using self.out (the output widget) do the display
                    display(df) #aqui es donde digo que haga display del dataframe que es la variable self.file1

            def display_widgets(self):
                self._create_widgets() # calls the creation of the widgets
                self.out = widgets.Output()  # this is the output widget in which the df is displayed
                display(widgets.VBox([self.out])) # controls layout of widget position  

            def get_df_objects(self):
                return self.df_objects

    # Run class and store output in something
    something = displayDF()
    # output the display
    something.display_widgets()

    #return df    

Button.on_click(whenclick2)



%matplotlib notebook
sav=[]
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(np.random.rand(10))
text=ax.text(0,0, "", va="bottom", ha="left")

def onclick(event):
    tx = 'button=%d, x=%d, y=%d, xdata=%f, ydata=%f' % (event.button, event.x, event.y, event.xdata, event.ydata)
    text.set_text(tx)
    sav.append(tx)

cid = fig.canvas.mpl_connect('button_press_event', onclick)

print(sav)

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
import ipywidgets as wdg 
LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/05-08-2020.csv"

DataIn = open(LASTFILE).readlines()
cnt=-1
LAT =[]
LON =[]
LOCATION =[]
cases = []
COORD=[]
STate = input("Which State? ")
STate = "Ohio"
for lines in DataIn:
    lines = lines.replace("\n","")
    line = lines.split(",")
    if STate in line[2] and len(line[5])>8 and len(line[6])>4:
        if cnt ==2:print(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
        cnt=cnt+1
        if cnt<5:
            print(" ")
            #print(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
        LAT.append(line[5]) 
        LON.append(line[6])
        cases.append(int(line[7]))
        LOCATION.append([line[7],line[5],line[6],line[8]])
LA = LAT
LO = LON
X = np.array(LAT,dtype=np.float)
Y = np.array(LON,dtype=np.float)
LT = np.array(LAT,dtype=np.float)
LG = np.array(LON,dtype=np.float)

fig = plt.figure(num=None, figsize=(12,12), dpi=80, facecolor='salmon')
ax = fig.gca()
ax.set_facecolor(('#c2efc1'))

S=1
Size=[]
for x in cases:
    S=1+(float(x)*.1)
    Size.append(int(S))
    #print(int(S))
s = np.array(Size)

A =(min(LG))-1
B =(max(LG))+1
C =(min(LT))-1
D =(max(LT))+1


longLeft= (min(LG))-3
longRight = (max(LG))+3
lat1 = (min(LT))-3
lat2 = (max(LT))+3

ax = fig.gca()
T= STate
text(0.62, 0.29, T, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=20)

# Create and display textarea widget
txt = wdg.Textarea(
    value='',
    placeholder='',
    description='event:',
    disabled=False
)
display(txt)

#COORD.append(txt)
# Define a callback function that will update the textarea
def onclick(event):
    # Uncomment for only one one click at a time
    #COORD=[]

    txt.value = str(event)  # Dynamically update the text box above
    COORD.append(txt.value)

# Create an hard reference to the callback not to be cleared by the garbage collector
ka = fig.canvas.mpl_connect('button_press_event', onclick)

plt.axis([longLeft,longRight,lat1,lat2])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.grid(True)
plt.scatter(Y, X, s=s, color="black")


plt.xlabel('First data sample was taken: 01/20/2020', fontsize=24)
plt.title('Using Latitude and Longitude from https://github.com/CSSEGISandData/COVID-19')
plt.ylabel('Number of Cases')
mplcursors.cursor(hover=True)

plt.show()

LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/05-08-2020.csv"

DataIn = open(LASTFILE).readlines()
cnt=-1
LAT =[]
LON =[]
LOCATION =[]
cases = []
COORD=[]
CITY =[]
#STate = input("Which State? ")
Threshhold = 40
STate = "Ohio"
for lines in DataIn:
    lines = lines.replace("\n","")
    line = lines.split(",")
    if STate in line[2] and len(line[5])>8 and len(line[6])>4:
        if int(line[8])>Threshhold:
            print(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
            cnt=cnt+1
            LAT.append(line[5]) 
            LON.append(line[6])
            cases.append(int(line[7]))
            LOCATION.append([line[1],line[6],line[5],line[8]])
            CITY.append(line[1])

for i in range(0,len(LOCATION)):
    location = LOCATION[i][1:-1]
    print(location[0],location[1])

location = LOCATION[3][1:-1]

import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import numpy as np
from PIL import Image,ImageFont,ImageDraw,ImageFilter,ImageChops
from random import randint
from mpl_toolkits.basemap import Basemap

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
LASTFILE="csv/_deaths_US.csv"
DataIn = open(LASTFILE).readlines()
for line in DataIn:
    line=line.replace('"','')
    if cnt==0:print (line)
    cnt=cnt+1
    line=line.replace("\n","")
    line = line.lstrip(",")
    line = line.split(",")
    if cnt<10 and line[5] !="":print (line[7])
    if "Ohio" in line[2]:# and line[6] == "New York":
        #if CNT==7:print(line)
        #if CNT==8:print(line)    
        if CNT<5 and line[5] !="":print(line)
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
    plt.annotate(C, m(l,t),color='red',fontsize=20,zorder=15)   
    
m.scatter(x, y, s=sd, color='r', zorder=10,  alpha=0.6)
filename = "BaseMap/april30_Hotspots__.png"
plt.savefig(filename, dpi=120, facecolor='salmon', edgecolor='b',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches="tight", pad_inches=0.2,
        frameon=None, metadata=None)

import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import numpy as np
from PIL import Image,ImageFont,ImageDraw,ImageFilter,ImageChops
from random import randint
from mpl_toolkits.basemap import Basemap
#prevents a warning from using Python3 instaead of Python2
import warnings
warnings.filterwarnings("ignore")
import sys
sys.path.insert(1, "/home/jack/hidden")
import Key
import twython
from twython import Twython

def RndState():
    TX=["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    x=randint(1,50)
    return TX[x]


LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/04-27-2020.csv"
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
    if search in line[2] and "-" in (line[6]):
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

# Make the figure
fig = plt.figure(num=None, figsize=(10,8), dpi=80, facecolor='salmon')

urcrnrlat=max(LT)+.5
llcrnrlat=min(LT)-.5
urcrnrlon=max(LG)+.8
llcrnrlon=min(LG)-.5
lat_0 = (urcrnrlat+llcrnrlat)/2
lon_0 =(urcrnrlon+llcrnrlon)/2

# Easiest way to make a basemap is to use the cylidrical projection and 
# define the bottom left lat/lon and top right lat/lon corners
# create the map object, m
m = Basemap(resolution='h', projection='cyl', \
    llcrnrlon=llcrnrlon, llcrnrlat=llcrnrlat, urcrnrlon=urcrnrlon, urcrnrlat=urcrnrlat)

# Note:
# You can define the resolution of the map you just created. Higher - resolutions take longer to create.
#    'c' - crude
#    'l' - low
#    'i' - intermediate
#    'h' - high
#    'f' - full

# Draw some map elements on the map
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='#ddaa66',lake_color='aqua')
m.drawcoastlines()
m.drawrivers(linewidth=1.0,color='navy',zorder=8)
m.drawcounties(linewidth=1.0, linestyle='solid', color='gray', antialiased=1, facecolor='lightgreen', ax=None, zorder=2, drawbounds=True)
m.drawstates(linewidth=1.5, linestyle='solid', color='black', antialiased=1,zorder=2, )
plt.text(llcrnrlon,llcrnrlat+.5, search, color='black', fontsize=24.5, zorder=6,bbox=dict(facecolor='salmon'))

# Drawing ArcGIS Basemap (only works with cylc projections??)
# Examples of what each map looks like can be found here:
# http://kbkb-wx-python.blogspot.com/2016/04/python-basemap-background-image-from.html
maps = ['ESRI_Imagery_World_2D',    # 0
        'ESRI_StreetMap_World_2D',  # 1
        'NatGeo_World_Map',         # 2
        'NGS_Topo_US_2D',           # 3
        'Ocean_Basemap',            # 4
        'USA_Topo_Maps',            # 5
        'World_Imagery',            # 6
        'World_Physical_Map',       # 7
        'World_Shaded_Relief',      # 8
        'World_Street_Map',         # 9
        'World_Terrain_Base',       # 10
        'World_Topo_Map'            # 11
        ]
MapStyle = 2
print ("Drawing MapStyle",MapStyle," image from arcGIS server..."),

m.arcgisimage(service=maps[MapStyle], xpixels=2000, verbose=False)
print ("...finished")

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
    Sd=0+(float(xd))
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

plt.savefig("BaseMap/"+search+"arcGIS__.png", dpi=120, facecolor='salmon', edgecolor='b',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches="tight", pad_inches=0.2,
        frameon=None, metadata=None)

# Add plot title and other plot elements the normal way
filename0 = "BaseMap/"+search+"arcGIS__.png"

def draw_blurred_back(img, position, text, font, col, halo_col):
    halo = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(position, text, font = font, fill = halo_col)
    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(position, text, font = font, fill = col)
    return Image.composite(img, blurred_halo, ImageChops.invert(blurred_halo))

if __name__ == '__main__':
    
    basewidth = 720
    inp = Image.open(filename0)
    wpercent = (basewidth / float(inp.size[0]))
    hsize = int((float(inp.size[1]) * float(wpercent)))
    inp = inp.resize((basewidth, hsize), Image.ANTIALIAS)
    #img.save(resized_image.jpg')
    
    #inp = inp.resize((640,640), Image.ANTIALIAS)
    font = ImageFont.truetype("/home/jack/fonts/Exo-Black.ttf", 30)
    text_title = (255, 255,230) # bright green
    blur_title = (0, 0, 0)   # black

    i2 = draw_blurred_back(inp, (15, 30), "Plotting COVID-19 Data", font, text_title, blur_title)
    font0 = ImageFont.truetype("/home/jack/fonts/Exo-Black.ttf", 20)
    font1 = ImageFont.truetype("/home/jack/fonts/Exo-Black.ttf", 14)
    font2 = ImageFont.truetype("/home/jack/fonts/PatrickHand-Regular.ttf", 16)
    #i2 = draw_blurred_back(i2, (15, 65), "Plot Using ArcGIS Basemap - "+search, font0, text_title, blur_title)
    
    i2 = draw_blurred_back(i2, (15, 65), "Drawing MapStyle "+str(MapStyle)+" image from arcGIS server..."+search, font0, text_title, blur_title)
    
    TXT="https://github.com/JupyterJones/COVID-19-Jupyter-Notebooks"
    draw = ImageDraw.Draw(i2) 
    draw.text((15, 5), TXT, font = font2, align ="left",fill="black")
    #i2 = draw(i2, (15, 65),TXT, font1)    
    
    #txt = Image.new('RGBA', i.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("/home/jack/fonts/Exo-Black.ttf", 20)
    # get a drawing context
    signature_ = "@jacklnorthrup" 
    #get length in pixel of signature_
    sizeS,ln = fnt.getsize(signature_)
    #add 15 pixels to right border
    pt = sizeS+25
    width, height = inp.size
    #marginx starting point of signature_
    marginx = pt
    #bottom margin
    marginy = 30
    x = width - marginx
    y = height - marginy
    

    text_sig = (255, 255,230) # bright green
    blur_sig = (0, 0, 0)   # black
    txt=draw_blurred_back(i2,(x,y), signature_, fnt, text_sig, blur_sig)
    out = Image.alpha_composite(i2, txt)
    out.save("images/TEMP_POST.png")

CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

STR = "#"+search+"  #arcGIS server #Basemap #COVID-19 - #Python  Plot data using "+TXT+" #JupyterJones" 

PATH = "images/TEMP_POST.png"
photo = open(PATH,'rb')
#response = twitter.upload_media(media=photo)
#twitter.update_status(status=STR, media_ids=[response['media_id']])

import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import numpy as np
from PIL import Image,ImageFont,ImageDraw,ImageFilter,ImageChops
from random import randint
from mpl_toolkits.basemap import Basemap
#prevents a warning from using Python3 instaead of Python2
import warnings
warnings.filterwarnings("ignore")
import sys
sys.path.insert(1, "/home/jack/hidden")
import Key
import twython
from twython import Twython

def RndState():
    TX=["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    x=randint(1,50)
    return TX[x]


LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/04-27-2020.csv"
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
    if search in line[2] and "-" in (line[6]):
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

# Make the figure
fig = plt.figure(num=None, figsize=(10,8), dpi=80, facecolor='salmon')

urcrnrlat=max(LT)+.5
llcrnrlat=min(LT)-.5
urcrnrlon=max(LG)+.8
llcrnrlon=min(LG)-.5
lat_0 = (urcrnrlat+llcrnrlat)/2
lon_0 =(urcrnrlon+llcrnrlon)/2

# Easiest way to make a basemap is to use the cylidrical projection and 
# define the bottom left lat/lon and top right lat/lon corners
# create the map object, m
m = Basemap(resolution='h', projection='cyl', \
    llcrnrlon=llcrnrlon, llcrnrlat=llcrnrlat, urcrnrlon=urcrnrlon, urcrnrlat=urcrnrlat)
print("llcrnrlon=",llcrnrlon, "llcrnrlat=",llcrnrlat,"urcrnrlon=",urcrnrlon,"urcrnrlat=",urcrnrlat)
# Note:
# You can define the resolution of the map you just created. Higher - resolutions take longer to create.
#    'c' - crude
#    'l' - low
#    'i' - intermediate
#    'h' - high
#    'f' - full

# Draw some map elements on the map
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='#ddaa66',lake_color='aqua')
m.drawcoastlines()
m.drawrivers(linewidth=1.0,color='navy',zorder=8)
m.drawcounties(linewidth=1.0, linestyle='solid', color='gray', antialiased=1, facecolor='lightgreen', ax=None, zorder=2, drawbounds=True)
m.drawstates(linewidth=1.5, linestyle='solid', color='black', antialiased=1,zorder=2, )
plt.text(llcrnrlon,llcrnrlat+.5, search, color='black', fontsize=24.5, zorder=6,bbox=dict(facecolor='salmon'))

# Drawing ArcGIS Basemap (only works with cylc projections??)
# Examples of what each map looks like can be found here:
# http://kbkb-wx-python.blogspot.com/2016/04/python-basemap-background-image-from.html
maps = ['ESRI_Imagery_World_2D',    # 0
        'ESRI_StreetMap_World_2D',  # 1
        'NatGeo_World_Map',         # 2
        'NGS_Topo_US_2D',           # 3
        'Ocean_Basemap',            # 4
        'USA_Topo_Maps',            # 5
        'World_Imagery',            # 6
        'World_Physical_Map',       # 7
        'World_Shaded_Relief',      # 8
        'World_Street_Map',         # 9
        'World_Terrain_Base',       # 10
        'World_Topo_Map'            # 11
        ]
MapStyle = 2
print ("Drawing MapStyle",MapStyle," image from arcGIS server..."),

m.arcgisimage(service=maps[MapStyle], xpixels=2000, verbose=False)
print ("...finished")

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
    Sd=0+(float(xd))
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

plt.savefig("BaseMap/"+search+"arcGIS__.png", dpi=120, facecolor='salmon', edgecolor='b',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches="tight", pad_inches=0.2,
        frameon=None, metadata=None)

# Add plot title and other plot elements the normal way
filename0 = "BaseMap/"+search+"arcGIS__.png"

def draw_blurred_back(img, position, text, font, col, halo_col):
    halo = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(position, text, font = font, fill = halo_col)
    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(position, text, font = font, fill = col)
    return Image.composite(img, blurred_halo, ImageChops.invert(blurred_halo))

if __name__ == '__main__':
    
    basewidth = 720
    inp = Image.open(filename0)
    wpercent = (basewidth / float(inp.size[0]))
    hsize = int((float(inp.size[1]) * float(wpercent)))
    inp = inp.resize((basewidth, hsize), Image.ANTIALIAS)
    #img.save(resized_image.jpg')
    
    #inp = inp.resize((640,640), Image.ANTIALIAS)
    font = ImageFont.truetype("/home/jack/fonts/Exo-Black.ttf", 30)
    text_title = (255, 255,230) # bright green
    blur_title = (0, 0, 0)   # black

    i2 = draw_blurred_back(inp, (15, 30), "Plotting COVID-19 Data", font, text_title, blur_title)
    font0 = ImageFont.truetype("/home/jack/fonts/Exo-Black.ttf", 20)
    font1 = ImageFont.truetype("/home/jack/fonts/Exo-Black.ttf", 14)
    font2 = ImageFont.truetype("/home/jack/fonts/PatrickHand-Regular.ttf", 16)
    #i2 = draw_blurred_back(i2, (15, 65), "Plot Using ArcGIS Basemap - "+search, font0, text_title, blur_title)
    
    i2 = draw_blurred_back(i2, (15, 65), "Drawing MapStyle "+str(MapStyle)+" image from arcGIS server..."+search, font0, text_title, blur_title)
    
    TXT="https://github.com/JupyterJones/COVID-19-Jupyter-Notebooks"
    draw = ImageDraw.Draw(i2) 
    draw.text((15, 5), TXT, font = font2, align ="left",fill="black")
    #i2 = draw(i2, (15, 65),TXT, font1)    
    
    #txt = Image.new('RGBA', i.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("/home/jack/fonts/Exo-Black.ttf", 20)
    # get a drawing context
    signature_ = "@jacklnorthrup" 
    #get length in pixel of signature_
    sizeS,ln = fnt.getsize(signature_)
    #add 15 pixels to right border
    pt = sizeS+25
    width, height = inp.size
    #marginx starting point of signature_
    marginx = pt
    #bottom margin
    marginy = 30
    x = width - marginx
    y = height - marginy
    

    text_sig = (255, 255,230) # bright green
    blur_sig = (0, 0, 0)   # black
    txt=draw_blurred_back(i2,(x,y), signature_, fnt, text_sig, blur_sig)
    out = Image.alpha_composite(i2, txt)
    out.save("images/TEMP_POST.png")

CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

STR = "#"+search+"  #arcGIS server #Basemap #COVID-19 - #Python  Plot data using "+TXT+" #JupyterJones" 

PATH = "images/TEMP_POST.png"
photo = open(PATH,'rb')
#response = twitter.upload_media(media=photo)
#twitter.update_status(status=STR, media_ids=[response['media_id']])

from PIL import Image
IM = Image.open(PATH)
IM




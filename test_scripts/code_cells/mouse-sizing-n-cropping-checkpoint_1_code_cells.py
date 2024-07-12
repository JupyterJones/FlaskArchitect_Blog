from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

!wget -O mouse-sizing-n-cropping-files/postoid.jpg https://jacknorthrup.com/postoids/postoid%20%2810%29.jpg

from PIL import Image
im=Image.open('mouse-sizing-n-cropping-files/postoid.jpg')
im.size # (width,height) tuple

import PIL
from PIL import Image

basewidth = 400
img = Image.open("mouse-sizing-n-cropping-files/postoid.jpg")
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save("mouse-sizing-n-cropping-files/postoid400.jpg")
img

http://stackoverflow.com/questions/6136588/image-cropping-using-python
http://2017.compciv.org/guide/topics/python-nonstandard-libraries/pillow.html

!wget -O mouse-sizing-n-cropping-files/soil.jpg https://static.pexels.com/photos/60013/desert-drought-dehydrated-clay-soil-60013.jpeg

from PIL import Image
im=Image.open('mouse-sizing-n-cropping-files/soil.jpg')
im.size # (width,height) tuple

import PIL
from PIL import Image

basewidth = 600
img = Image.open("mouse-sizing-n-cropping-files/soil.jpg")
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save("mouse-sizing-n-cropping-files/soil600.jpg")

from PIL import Image
im=Image.open("mouse-sizing-n-cropping-files/soil600.jpg")
im.size # (width,height) tuple

from PIL import Image
im=Image.open("mouse-sizing-n-cropping-files/soil600.jpg")
im # (display image)

def add_cursor(fig, ax):
    plt.close(fig)

    vline = ax.axvline(1, color='k')
    hline = ax.axhline(0.5, color='k')

    def set_cursor(x, y):
        vline.set_xdata((x, x))
        hline.set_ydata((y, y))
        display(fig)

    interact(set_cursor, x=ax.get_xlim(), y=ax.get_ylim())

#import ipympl
from math import sin
import matplotlib.pyplot as plt
%matplotlib inline 
x = (sin(6))
plt.plot([0, 1, 2, x, 5, 8,0,-4, -2, -6])
plt.show()


import matplotlib.pyplot as plt
%matplotlib inline 
plt.rcParams['figure.figsize'] = (20.0, 10.0)
import matplotlib.image as mpimg
import numpy as np
img=mpimg.imread('mouse-sizing-n-cropping-files/soil600.jpg')
imgplot = plt.imshow(img)


from PIL import Image
img = Image.open('mouse-sizing-n-cropping-files/soil600.jpg')
crop_specs = (145, 50, img.width - 40, img.height - 135)
crop_img = img.crop(crop_specs)
crop_img.save('mouse-sizing-n-cropping-files/soil-cropped.png')   

img=mpimg.imread('mouse-sizing-n-cropping-files/soil-cropped.png')
imgplot = plt.imshow(img)

from PIL import Image
im=Image.open('mouse-sizing-n-cropping-files/soil-cropped.png')
im.size # (width,height) tuple

from PIL import Image
im=Image.open('mouse-sizing-n-cropping-files/soil-cropped.png')
im

http://mpld3.github.io/

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.path as mpath
import matplotlib.patches as mpatches

import mpld3
from mpld3 import plugins, utils


class LinkedDragPlugin(plugins.PluginBase):
    JAVASCRIPT = r"""
    mpld3.register_plugin("drag", DragPlugin);
    DragPlugin.prototype = Object.create(mpld3.Plugin.prototype);
    DragPlugin.prototype.constructor = DragPlugin;
    DragPlugin.prototype.requiredProps = ["idpts", "idline", "idpatch"];
    DragPlugin.prototype.defaultProps = {}
    function DragPlugin(fig, props){
        mpld3.Plugin.call(this, fig, props);
    };

    DragPlugin.prototype.draw = function(){
        var patchobj = mpld3.get_element(this.props.idpatch, this.fig);
        var ptsobj = mpld3.get_element(this.props.idpts, this.fig);
        var lineobj = mpld3.get_element(this.props.idline, this.fig);

        var drag = d3.behavior.drag()
            .origin(function(d) { return {x:ptsobj.ax.x(d[0]),
                                          y:ptsobj.ax.y(d[1])}; })
            .on("dragstart", dragstarted)
            .on("drag", dragged)
            .on("dragend", dragended);

        lineobj.path.attr("d", lineobj.datafunc(ptsobj.offsets));
        patchobj.path.attr("d", patchobj.datafunc(ptsobj.offsets,
                                                  patchobj.pathcodes));
        lineobj.data = ptsobj.offsets;
        patchobj.data = ptsobj.offsets;

        ptsobj.elements()
           .data(ptsobj.offsets)
           .style("cursor", "default")
           .call(drag);

        function dragstarted(d) {
          d3.event.sourceEvent.stopPropagation();
          d3.select(this).classed("dragging", true);
        }

        function dragged(d, i) {
          d[0] = ptsobj.ax.x.invert(d3.event.x);
          d[1] = ptsobj.ax.y.invert(d3.event.y);
          d3.select(this)
            .attr("transform", "translate(" + [d3.event.x,d3.event.y] + ")");
          lineobj.path.attr("d", lineobj.datafunc(ptsobj.offsets));
          patchobj.path.attr("d", patchobj.datafunc(ptsobj.offsets,
                                                    patchobj.pathcodes));
        }

        function dragended(d, i) {
          d3.select(this).classed("dragging", false);
        }
    }

    mpld3.register_plugin("drag", DragPlugin);
    """

    def __init__(self, points, line, patch):
        if isinstance(points, mpl.lines.Line2D):
            suffix = "pts"
        else:
            suffix = None

        self.dict_ = {"type": "drag",
                      "idpts": utils.get_id(points, suffix),
                      "idline": utils.get_id(line),
                      "idpatch": utils.get_id(patch)}


fig, ax = plt.subplots()

Path = mpath.Path
path_data = [
    (Path.MOVETO, (1.58, -2.57)),
    (Path.CURVE4, (0.35, -1.1)),
    (Path.CURVE4, (-1.75, 2.0)),
    (Path.CURVE4, (0.375, 2.0)),
    (Path.LINETO, (0.85, 1.15)),
    (Path.CURVE4, (2.2, 3.2)),
    (Path.CURVE4, (3, 0.05)),
    (Path.CURVE4, (2.0, -0.5)),
    (Path.CLOSEPOLY, (1.58, -2.57)),
    ]
codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
ax.add_patch(patch)

# plot control points and connecting lines
x, y = zip(*path.vertices[:-1])
points = ax.plot(x, y, 'go', ms=10)
line = ax.plot(x, y, '-k')

ax.grid(True, color='gray', alpha=0.5)
ax.axis('equal')
ax.set_title("Drag Points to Change Path", fontsize=18)

plugins.connect(fig, LinkedDragPlugin(points[0], line[0], patch))

mpld3.display()

import matplotlib.pyplot as plt
import numpy as np
import mpld3
from mpld3 import plugins

fig, ax = plt.subplots()

x = np.linspace(-2, 2, 20)
y = x[:, None]
X = np.zeros((20, 20, 4))

X[:, :, 0] = np.exp(- (x - 1) ** 2 - (y) ** 2)
X[:, :, 1] = np.exp(- (x + 0.71) ** 2 - (y - 0.71) ** 2)
X[:, :, 2] = np.exp(- (x + 0.71) ** 2 - (y + 0.71) ** 2)
X[:, :, 3] = np.exp(-0.25 * (x ** 2 + y ** 2))

im = ax.imshow(X, extent=(10, 20, 10, 20),
               origin='lower', zorder=1, interpolation='nearest')
fig.colorbar(im, ax=ax)

ax.set_title('An Image', size=20)

plugins.connect(fig, plugins.MousePosition(fontsize=14))

mpld3.display()


class ImageFile(object):
    """Class for storing an image location."""
    def __init__(self, fpath):
        self.fpath = fpath
    def _repr_png_(self):
        return open(self.fpath, 'r').read()
ImageFile('mouse-sizing-n-cropping-files/soil600.jpg')

from IPython.display import Image
image = Image('mouse-sizing-n-cropping-files/soil600.jpg')
image


!pwd

class ImageFile(object):
    """Class for storing an image location."""

    def __init__(self, fpath):
        self.fpath = fpath
        self.format = fpath.split('.')[-1]

    def _repr_png_(self):
        if self.format == 'png':
            return open(self.fpath, 'r').read()

    def _repr_jpeg_(self):
        if self.format == 'jpeg' or self.format == 'jpg':
            return open(self.fpath, 'r').read()

    def _repr_svg_(self):
        if self.format == 'svg':
            return open(self.fpath, 'r').read()



import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
%matplotlib inline

im = np.array(Image.open('mouse-sizing-n-cropping-files/soil600.jpg'))
plt.imshow(im)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import mpld3
%matplotlib inline  
from mpld3 import plugins
from PIL import Image
img=Image.open("mouse-sizing-n-cropping-files/soil600.jpg")
 

fig, ax = plt.subplots()
im = ax.imshow(img, extent=(10, 20, 10, 20),
               origin='lower', zorder=1, interpolation='nearest')

plugins.connect(fig, plugins.MousePosition(fontsize=14))
mpld3.display()
from PIL import Image


im = np.array(Image.open('mouse-sizing-n-cropping-files/soil600.jpg'))



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
im = im[::-1]
plt.imshow(im)
plugins.connect(fig, plugins.MousePosition(fontsize=14))

mpld3.display()

!sudo locate manilyn.jpg

from PIL import Image
img = Image.open('mouse-sizing-n-cropping-files/soil600.jpg')
crop_specs = (200, 0, img.width - 150, img.height - 0)
crop_img = img.crop(crop_specs)
crop_img.save('mouse-sizing-n-cropping-files/cropsoil600.jpg')   

import matplotlib
import numpy as np
import mpld3
import matplotlib.pyplot as plt
from PIL import Image
from mpld3 import plugins
%matplotlib inline
fig, ax = plt.subplots()
im = np.array(Image.open('mouse-sizing-n-cropping-files/cropsoil600.jpg'))
# Default shows the image upside down [::-1] flips the image
im = im[::-1]
plt.imshow(im)
plugins.connect(fig, plugins.MousePosition(fontsize=14))

mpld3.display()

im = Image.open('mouse-sizing-n-cropping-files/soil600.jpg')
im

#Python 2.7 - Linux
from PIL import Image
# open an image file (.jpg or.png)
im1 = Image.open('mouse-sizing-n-cropping-files/soil600.jpg')
# multiply each pixel by a variable - less than 1 is darker greater than 1 is lighter
# works best with .jpg and .png images
im2 = im1.point(lambda p: p * 1.8) # lighter
im3 = im1.point(lambda p: p * .5)  # Darker

# This pops up your defaultimage viewer
im1.show()
im2.show()
im3.show()
# save modified image 
im2.save("mouse-sizing-n-cropping-files/soil-light.jpg")
im3.save("mouse-sizing-n-cropping-files/soil-dark.jpg")


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
im = im[::-1]
plt.imshow(im)
plugins.connect(fig, plugins.MousePosition(fontsize=14))


mpld3.display()

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('mouse-sizing-n-cropping-files/soil600.jpg')
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (425,107,686,454)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import mpld3
#%matplotlib inline  
from mpld3 import plugins
from PIL import Image
fig, ax = plt.subplots()

plugins.connect(fig, plugins.MousePosition(fontsize=14))
mpld3.display()

!wget -O mouse-sizing-n-cropping-files/jungle.jpg https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Brooklyn_Museum_-_In_the_Jungle%2C_Florida_-_Winslow_Homer_-_overall.jpg/800px-Brooklyn_Museum_-_In_the_Jungle%2C_Florida_-_Winslow_Homer_-_overall.jpg

import PIL
from PIL import Image
im1 = Image.open("mouse-sizing-n-cropping-files/jungle.jpg")
#longer_side = max(im1.size)
basewidth = 700
hsize = 500
img = im1.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save("mouse-sizing-n-cropping-files/jungle700.jpg")
im = Image.open("mouse-sizing-n-cropping-files/jungle700.jpg")
im

import tkinter as Tkinter
from PIL import Image, ImageTk
from sys import argv

window = Tkinter.Tk(className="bla")

image = Image.open("mouse-sizing-n-cropping-files/jungle700.jpg")
canvas = Tkinter.Canvas(window, width=image.size[0], height=image.size[1])
canvas.pack()
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(image.size[0]//2, image.size[1]//2, image=image_tk)

def callback(event):
    #print "[",event.x,"],["+event.y,"]"
    print ("[",event.x,",",event.y,"],",)
 
canvas.bind("<Button-1>", callback)
Tkinter.mainloop()

%matplotlib inline
#The line above is necesary to show Matplotlib's plots inside a Jupyter Notebook

import cv2
from matplotlib import pyplot as plt

#Import image
image = cv2.imread("input_path")

#Show the image with matplotlib



%matplotlib inline
#The line above is necesary to show Matplotlib's plots inside a Jupyter Notebook

import cv2
from matplotlib import pyplot as plt  # function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):

    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:

        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                str(y), (x,y), font,
                1, (255, 0, 0), 2)
        cv2.imshow('image', img)

    # checking for right mouse clicks	
    if event==cv2.EVENT_RBUTTONDOWN:

        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', img)

# reading the image
img = cv2.imread("mouse-sizing-n-cropping-files/jungle700.jpg", 1)

# displaying the image
plt.imshow(image)
plt.show()

# setting mouse handler for the image
# and calling the click_event() function
cv2.setMouseCallback('image', click_event)




from tkinter import *
from PIL import Image, ImageTk
from sys import argv
from logger_settings import api_logger
#api_logger.info('hello world')
#window = Tkinter.Tk(className="bla")
window = Tk(className="Clickable")
image = Image.open("mouse-sizing-n-cropping-files/jungle700.jpg")
canvas = Canvas(window, width=image.size[0], height=image.size[1])
canvas.pack()
image_tk = ImageTk.PhotoImage(image)
api_logger.info(image_tk)
canvas.create_image(image.size[0]//2, image.size[1]//2, image=image_tk)

def callback(event):
    #print "[",event.x,"],["+event.y,"]"
    print ("[",event.x,",",event.y,"],",)

canvas.bind("<Button-1>", callback)
tkinter.mainloop()

# importing the module
import cv2

# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):

	# checking for left mouse clicks
	if event == cv2.EVENT_LBUTTONDOWN:

		# displaying the coordinates
		# on the Shell
		print(x, ' ', y)

		# displaying the coordinates
		# on the image window
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img, str(x) + ',' +
					str(y), (x,y), font,
					1, (255, 0, 0), 2)
		cv2.imshow('image', img)

	# checking for right mouse clicks	
	if event==cv2.EVENT_RBUTTONDOWN:

		# displaying the coordinates
		# on the Shell
		print(x, ' ', y)

		# displaying the coordinates
		# on the image window
		font = cv2.FONT_HERSHEY_SIMPLEX
		b = img[y, x, 0]
		g = img[y, x, 1]
		r = img[y, x, 2]
		cv2.putText(img, str(b) + ',' +
					str(g) + ',' + str(r),
					(x,y), font, 1,
					(255, 255, 0), 2)
		cv2.imshow('image', img)

# driver function
if __name__=="__main__":

	# reading the image
	img = cv2.imread("mouse-sizing-n-cropping-files/jungle700.jpg", 1)

	# displaying the image
	cv2.imshow('image', img)

	# setting mouse handler for the image
	# and calling the click_event() function
	cv2.setMouseCallback('image', click_event)

	# wait for a key to be pressed to exit
	cv2.waitKey(0)

	# close the window
	cv2.destroyAllWindows()


poly = np.array([ [ 320 , 123 ], [ 437 , 121 ], [ 451 , 267 ], [ 356 , 277 ],[ 321 , 125 ] ], np.int32)
print poly

import cv2
import numpy as np 

import cv2
import numpy as np 

# Read images
dst = cv2.imread("mouse-sizing-n-cropping-files/soil600.jpg")

src = cv2.imread("mouse-sizing-n-cropping-files/jungle700.jpg")
src_mask = np.zeros(src.shape, src.dtype)

src_mask = np.zeros(src.shape, src.dtype)

poly = np.array([ [ 269 , 24 ], [ 273 , 117 ], [ 301 , 145 ], [ 345 , 199 ], 
[ 398 , 273 ], [ 428 , 317 ], [ 447 , 278 ], [ 440 , 231 ], [ 487 , 220 ], [ 491 , 202 ],
[ 437 , 209 ], [ 415 , 162 ], [ 433 , 126 ], [ 410 , 113 ], [ 360 , 115 ], [ 363 , 73 ], [ 317 , 25 ] ], np.int32)



cv2.fillPoly(src_mask, [poly], (255, 255, 255))

# This is where the CENTER of the airplane will be placed
center = (550,275)

# Clone seamlessly.
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)

# Write result
cv2.imwrite("mouse-sizing-n-cropping-files/soil-jungle.jpg", output);


import cv2
import numpy as np 

# Read images
#dst = cv2.imread("01-ajungle2.jpg")
#dst = cv2.imread("/notebooks/edge-preserving-normalized-convolution-filter.jpg")
#src = cv2.imread("/notebooks/learnopencv/SeamlessCloning/images/airplane.jpg")
#src = cv2.imread("desert-drought.jpg")
dst = cv2.imread("mouse-sizing-n-cropping-files/soil600.jpg")
src = cv2.imread("mouse-sizing-n-cropping-files/jungle700.jpg")
#src = cv2.imread("mouse-sizing-n-cropping-files/soil600.jpg")
#dst = cv2.imread("mouse-sizing-n-cropping-files/jungle700.jpg")
# Create a rough mask around the airplane.
src_mask = np.zeros(src.shape, src.dtype)
#poly = np.array([ [4,80], [30,54], [151,63], [254,37], [298,90], [272,134], [43,122] ], np.int32)
poly = np.array([ [ 320 , 123 ], [ 437 , 121 ], [ 451 , 267 ], [ 356 , 277 ],[ 321 , 125 ] ], np.int32)
#poly = np.array([ [1,100], [1,50], [151,63], [254,37], [298,90], [272,134], [43,122] ], np.int32)
#poly = np.array([ [736, 113],[768, 97],[784, 93],[788, 157],[789, 197],[788, 225],[777, 265],[768, 301],[778, 318],\
#[794, 332],[767, 386],[743, 348],[707, 314],[693, 304],[666, 299],[668, 275],[705, 273],[729, 272],\
#[716, 223],[706, 236],[689, 207],[687, 217],[687, 231],[667, 217],[647, 226],[629, 208],[614, 207],\
#[615, 198],[602, 183],[607, 174],[609, 159],[636, 162],[640, 146],[634, 137],[597, 153],[594, 137],\
#[601, 122],[583, 115],[611, 83],[626, 78],[622, 72],[589, 73],[583, 51],[591, 13],[605, 10],[631, 28],\
#[650, 17],[666, 39],[681, 18],[699, 4],[728, 6],[751, 7],[743, 39],[794, 13],[797, 42],[764, 66],\
#[735, 101],[736, 113] ], np.int32)




cv2.fillPoly(src_mask, [poly], (255, 255, 255))

# This is where the CENTER of the airplane will be placed
center = (250,275)

# Clone seamlessly.
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)

# Write result
cv2.imwrite("01-cloning-example3.jpg", output);


im = Image.open("01-cloning-example3.jpg")
im

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import mpld3

mpld3.enable_notebook()
from mpld3 import plugins

fig, ax = plt.subplots(subplot_kw=dict(axisbg='#EEEEEE'))
ax.grid(color='white', linestyle='solid')

N = 50
scatter = ax.scatter(np.random.normal(size=N),
                     np.random.normal(size=N),
                     c=np.random.random(size=N),
                     s = 1000 * np.random.random(size=N),
                     alpha=0.3,
                     cmap=plt.cm.jet)

ax.set_title("D3 Scatter Plot (with tooltips!)", size=20)

labels = ['point {0}'.format(i + 1) for i in range(N)]
fig.plugins = [plugins.PointLabelTooltip(scatter, labels)]

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import mpld3

mpld3.enable_notebook()




fig, ax = plt.subplots(subplot_kw=dict(axisbg='#EEEEEE'))
ax.grid(color='white', linestyle='solid')

N = 50
scatter = ax.scatter(np.random.normal(size=N),
                     np.random.normal(size=N),
                     c=np.random.random(size=N),
                     s = 1000 * np.random.random(size=N),
                     alpha=0.3,
                     cmap=plt.cm.jet)

ax.set_title("D3 Scatter Plot", size=18);

import matplotlib
import numpy as np
from math import sin
import matplotlib.pyplot as plt
%matplotlib inline  

x = np.linspace(0, 3*np.pi, 500)
plt.plot(x, np.sin(x**2))
plt.title('A simple chirp')
plt.show()




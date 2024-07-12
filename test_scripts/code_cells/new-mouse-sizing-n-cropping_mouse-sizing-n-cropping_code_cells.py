from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

!ls mouse-sizing-n-cropping-files/jungle700.jpg

#!ls mouse-sizing-n-cropping-files/soil600.jpg
!ls mouse-sizing-n-cropping-files/jungle700.jpg

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

from PIL import Image, ImageTk
import PIL
from sys import argv
import sys
import tkinter as Tkinter
import cv2
import numpy as np 
from logger_settings import api_logger

window = Tk(className="Clickable")
data = []
image = PIL.Image.open("mouse-sizing-n-cropping-files/jungle700.jpg")
canvas = Canvas(window, width=image.size[0], height=image.size[1])
canvas.pack()
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(image.size[0]//2, image.size[1]//2, image=image_tk)

def callback(event):
    #print "[",event.x,"],["+event.y,"]"
    #Data= ("[",event.x,",",event.y,"],",)
    Data= [event.x,event.y]
    data.append(Data)
    print ("[",event.x,",",event.y,"],",)

canvas.bind("<Button-1>", callback)
#data = str(callback)
#api_logger.info(data)
#mainloop()

poly = np.array(data, np.int32)

# Read images
dst = cv2.imread("mouse-sizing-n-cropping-files/soil600.jpg")
src = cv2.imread("mouse-sizing-n-cropping-files/jungle700.jpg")
src_mask = np.zeros(src.shape, src.dtype)
#poly = np.array([ [1,100], [1,50], [151,63], [254,37], [298,90], [272,134], [43,122] ], np.int32)
cv2.fillPoly(src_mask, [poly], (255, 255, 255))
# This is where the CENTER where thr 'poly' will be placed
center = (250,275)
# Clone seamlessly.
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)
# Write result
cv2.imwrite("01-cloning-xxz1.jpg", output);
im = PIL.Image.open("01-cloning-xxz1.jpg")
im

ctypes.addressof(p_block.contents).

object = callback
id(object)

import ctypes
>>>a = 5
>>>address = id(a)
>>>address
493382800
>>>ctypes.cast(address, ctypes.py_object).value
5

!cat logs/api.log

!ls /home/jack/Desktop/TWITTER/JupyterNotebook-Graphics-master/mouse-sizing-n-cropping-files

!cp -a /home/jack/Desktop/TWITTER/JupyterNotebook-Graphics-master/mouse-sizing-n-cropping-files .

!ls mouse-sizing-n-cropping-files

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


!ls mouse-sizing-n-cropping-files

class ImageFile(object):
    """Class for storing an image location."""
    def __init__(self, fpath):
        self.fpath = fpath
    def _repr_png_(self):
        return open(self.fpath, 'rb').read()
ImageFile('mouse-sizing-n-cropping-files/soil.jpg')#,encoding= 'unicode_escape')

with open(path, 'rb') as f:
  contents = f.read()

from IPython.display import Image
image = Image('mouse-sizing-n-cropping-files/soil600.jpg')
image


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
 

#fig, ax = plt.subplots()
fig, ax = plt.subplots(figsize=(9.,9.))
im = ax.imshow(img, extent=(10, 20, 10, 20),
               origin='lower', zorder=1, interpolation='nearest')

plugins.connect(fig, plugins.MousePosition(fontsize=14))
mpld3.display()

#im = np.array(Image.open('mouse-sizing-n-cropping-files/soil600.jpg'))
#im

import matplotlib
import numpy as np
import mpld3
import matplotlib.pyplot as plt
from PIL import Image
from mpld3 import plugins
%matplotlib inline
#fig, ax = plt.subplots()
fig, ax = plt.subplots(figsize=(9.,9.))
im = np.array(Image.open('mouse-sizing-n-cropping-files/soil600.jpg'))
# Default shows the image upside down [::-1] flips the image
im = im[::-1]
plt.imshow(im)
plugins.connect(fig, plugins.MousePosition(fontsize=14))

mpld3.display()

!locate manilyn.jpg

from PIL import Image
img = Image.open('mouse-sizing-n-cropping-files/soil600.jpg')
crop_specs = (200, 0, img.width - 150, img.height - 0)
crop_img = img.crop(crop_specs)
crop_img.save('mouse-sizing-n-cropping-files/cropsoil600.jpg')   

import matplotlib.pyplot as plt
import matplotlib.image as mimage
import matplotlib.cbook as cbook
datafile = cbook.get_sample_data('logo2.png', asfileobj=False)
im = mimage.imread(datafile)
fig, ax = plt.subplots(figsize=(5.,5.))
myaximage = ax.imshow(im,
                      aspect='auto',
                      extent=(20, 80, 20, 80),
                      alpha=0.5)
ax.plot(range(100))
plt.show()

import matplotlib
import numpy as np
import mpld3
import matplotlib.pyplot as plt
from PIL import Image
from mpld3 import plugins
%matplotlib inline
#fig, ax = plt.subplots()
fig, ax = plt.subplots(figsize=(9.,9.))
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
#im1.show()
im2.show()
#im3.show()
# save modified image 
im2.save("mouse-sizing-n-cropping-files/soil-light.jpg")
im3.save("mouse-sizing-n-cropping-files/soil-dark.jpg")


im2

im3

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

import matplotlib
import numpy as np
import mpld3
import matplotlib.pyplot as plt
from PIL import Image
from mpld3 import plugins
%matplotlib inline
#fig, ax = plt.subplots()
fig, ax = plt.subplots(figsize=(5.,5.))
im = np.array(Image.open('mouse-sizing-n-cropping-files/test.jpg'))
# Default shows the image upside down [::-1] flips the image
#im = im[::-1]
plt.imshow(im)
plugins.connect(fig, plugins.MousePosition(fontsize=14))

mpld3.display()

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('mouse-sizing-n-cropping-files/test.jpg')
mask = np.zeros(img.shape[:2],np.uint8)
print(img.shape[:2])
print(mask.shape[:2])
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
print(bgdModel.shape[:2])
print(fgdModel.shape[:2])
#rect = (425,107,686,454)
#rect = (topleft,topright,107,686,454)
#rect = (325,207,386,454)
#rect = (150,100,403,150)
rect = (196,167,340,224)


cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()

!pwd

# Python program to illustrate
# foreground extraction using
# GrabCut algorithm

# organize imports
import numpy as np
import cv2
from matplotlib import pyplot as plt

# path to input image specified and
# image is loaded with imread command
image = cv2.imread('mouse-sizing-n-cropping-files/soil600.jpg')

# create a simple mask image similar
# to the loaded image, with the
# shape and return type
mask = np.zeros(image.shape[:2], np.uint8)

# specify the background and foreground model
# using numpy the array is constructed of 1 row
# and 65 columns, and all array elements are 0
# Data type for the array is np.float64 (default)
backgroundModel = np.zeros((1, 65), np.float64)
foregroundModel = np.zeros((1, 65), np.float64)

# define the Region of Interest (ROI)
# as the coordinates of the rectangle
# where the values are entered as
# (startingPoint_x, startingPoint_y, width, height)
# these coordinates are according to the input image
# it may vary for different images
rectangle = (20, 100, 150, 150)

# apply the grabcut algorithm with appropriate
# values as parameters, number of iterations = 3
# cv2.GC_INIT_WITH_RECT is used because
# of the rectangle mode is used
cv2.grabCut(image, mask, rectangle,
			backgroundModel, foregroundModel,
			3, cv2.GC_INIT_WITH_RECT)

# In the new mask image, pixels will
# be marked with four flags
# four flags denote the background / foreground
# mask is changed, all the 0 and 2 pixels
# are converted to the background
# mask is changed, all the 1 and 3 pixels
# are now the part of the foreground
# the return type is also mentioned,
# this gives us the final mask
mask2 = np.where((mask == 2)|(mask == 0), 0, 1).astype('uint8')

# The final mask is multiplied with
# the input image to give the segmented image.
image = image * mask2[:, :, np.newaxis]

# output segmented image with colorbar
plt.imshow(image)
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

import tkinter
dir(tkinter)

from PIL import Image, ImageTk
import PIL
from sys import argv
import sys
from tkinter import *
window = Tk(className="Clickable")
data = []
image = PIL.Image.open("mouse-sizing-n-cropping-files/jungle700.jpg")
canvas = Canvas(window, width=image.size[0], height=image.size[1])
canvas.pack()
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(image.size[0]//2, image.size[1]//2, image=image_tk)

def callback(event):
    #print "[",event.x,"],["+event.y,"]"
    #Data= ("[",event.x,",",event.y,"],",)
    Data= [event.x,event.y]
    data.append(Data)
    print ("[",event.x,",",event.y,"],",)

canvas.bind("<Button-1>", callback)
mainloop()

poly = np.array(data, np.int32)

import cv2
import numpy as np 
# Read images
dst = cv2.imread("mouse-sizing-n-cropping-files/soil600.jpg")
src = cv2.imread("mouse-sizing-n-cropping-files/jungle700.jpg")
src_mask = np.zeros(src.shape, src.dtype)
#poly = np.array([ [1,100], [1,50], [151,63], [254,37], [298,90], [272,134], [43,122] ], np.int32)
cv2.fillPoly(src_mask, [poly], (255, 255, 255))
# This is where the CENTER where thr 'poly' will be placed
center = (250,275)
# Clone seamlessly.
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)
# Write result
cv2.imwrite("01-cloning-10.jpg", output);
im = PIL.Image.open("01-cloning-10.jpg")
im

print (data)

poly = np.array(data, np.int32)
print(poly)

poly = np.array([ [ 320 , 123 ], [ 437 , 121 ], [ 451 , 267 ], [ 356 , 277 ],[ 321 , 125 ] ], np.int32)
print(poly)

# This is used in the cell
poly = np.array([ [1,100], [1,50], [151,63], [254,37], [298,90], [272,134], [43,122] ], np.int32)
print (poly)

import cv2
import numpy as np 
# Read images
dst = cv2.imread("mouse-sizing-n-cropping-files/soil600.jpg")
src = cv2.imread("mouse-sizing-n-cropping-files/jungle700.jpg")
src_mask = np.zeros(src.shape, src.dtype)
#poly = np.array([ [1,100], [1,50], [151,63], [254,37], [298,90], [272,134], [43,122] ], np.int32)
cv2.fillPoly(src_mask, [poly], (255, 255, 255))
# This is where the CENTER where thr 'poly' will be placed
center = (250,275)
# Clone seamlessly.
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)
# Write result
cv2.imwrite("01-cloning-example6.jpg", output);
im = PIL.Image.open("01-cloning-example6.jpg")
im

im = PIL.Image.open("01-cloning-example6.jpg")
im





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
poly = [[poly], np.int32]


cv2.fillPoly(src_mask, [poly], (255, 255, 255))

# This is where the CENTER of the airplane will be placed
center = (550,275)

# Clone seamlessly.
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)

# Write result
cv2.imwrite("mouse-sizing-n-cropping-files/soil-jungle.jpg", output);


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
dst = cv2.imread("mouse-sizing-n-cropping-files/soil600.jpg")

src = cv2.imread("mouse-sizing-n-cropping-files/jungle700.jpg")
src_mask = np.zeros(src.shape, src.dtype)

src_mask = np.zeros(src.shape, src.dtype)

poly = np.array([ [ 269 , 24 ], [ 273 , 117 ], [ 301 , 145 ], [ 345 , 199 ], 
[ 398 , 273 ], [ 428 , 317 ], [ 447 , 278 ], [ 440 , 231 ], [ 487 , 220 ], [ 491 , 202 ],
[ 437 , 209 ], [ 415 , 162 ], [ 433 , 126 ], [ 410 , 113 ], [ 360 , 115 ], [ 363 , 73 ], [ 317 , 25 ] ], np.int32)
poly = [[poly], np.int32]


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
dst = cv2.imread("mouse-sizing-n-cropping-files/soil600.jpg")
src = cv2.imread("mouse-sizing-n-cropping-files/jungle700.jpg")
src_mask = np.zeros(src.shape, src.dtype)
poly = np.array([ [1,100], [1,50], [151,63], [254,37], [298,90], [272,134], [43,122] ], np.int32)
cv2.fillPoly(src_mask, [poly], (255, 255, 255))
# This is where the CENTER where thr 'poly' will be placed
center = (250,275)
# Clone seamlessly.
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)
# Write result
cv2.imwrite("01-cloning-example5.jpg", output);

im = PIL.Image.open("01-cloning-example5.jpg")
im

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import mpld3

mpld3.enable_notebook()
from mpld3 import plugins



fig, ax = plt.subplots(figsize=(9.,9.),facecolor='#ADD8E6')
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

# Loading necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Plotting pretty figures and avoid blurry images
%config InlineBackend.figure_format = 'retina'  
# No need to include %matplotlib inline magic command. These things come built-in now.

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

# Enable multiple cell outputs
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'
#plt.subplots()
#fig, ax = plt.subplots(subplot_kw=dict(

ax = plt.axes(facecolor='#E6E6E6')
ax.grid(color='white', linestyle='solid')


N = 50
scatter = ax.scatter(np.random.normal(size=N),
                     np.random.normal(size=N),
                     c=np.random.random(size=N),
                     s = 1000 * np.random.random(size=N),
                     alpha=0.3,
                     cmap=plt.cm.jet)

ax.set_title("D3 Scatter Plot", size=18);


%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import mpld3

mpld3.enable_notebook()


fig, ax = plt.subplots(subplot_kw=dict(ax = plt.axes(facecolor='#E6E6E6')))
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

import cv2
import numpy as np 
# Read images
dst = cv2.imread("mouse-sizing-n-cropping-files/soil600.jpg")
src = cv2.imread("mouse-sizing-n-cropping-files/jungle700.jpg")
src_mask = np.zeros(src.shape, src.dtype)
#poly = np.array([ [1,100], [1,50], [151,63], [254,37], [298,90], [272,134], [43,122] ], np.int32)
cv2.fillPoly(src_mask, [poly], (255, 255, 255))
# This is where the CENTER where thr 'poly' will be placed
center = (250,275)
# Clone seamlessly.
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)
# Write result
cv2.imwrite("01-cloning-example6.jpg", output);
im = PIL.Image.open("01-cloning-example6.jpg")
im



import cv2
import numpy as np 
# Read images
dst = cv2.imread("mouse-sizing-n-cropping-files/soil600.jpg")
src = cv2.imread("mouse-sizing-n-cropping-files/jungle700.jpg")
src_mask = np.zeros(src.shape, src.dtype)
poly = np.array([ [1,100], [1,50], [151,63], [254,37], [298,90], [272,134], [43,122] ], np.int32)
cv2.fillPoly(src_mask, [poly], (255, 255, 255))
# This is where the CENTER where thr 'poly' will be placed
center = (250,275)
# Clone seamlessly.
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)
# Write result
cv2.imwrite("01-cloning-example5.jpg", output);




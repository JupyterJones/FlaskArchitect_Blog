!mkdir images

!wget -O images/face.jpg https://upload.wikimedia.org/wikipedia/commons/3/33/Arnold_Schwarzenegger_edit%28ws%29.jpg

# Notice the mpld3 module - it will allow youtoload animage and use to mouse to see pixel locations
# handy tool to find points for a fast crop
import matplotlib
import numpy as np
import mpld3
import matplotlib.pyplot as plt
from PIL import Image
from mpld3 import plugins
%matplotlib inline
fig, ax = plt.subplots()
im = np.array(Image.open('images/face.jpg'))
# Default shows the image upside down [::-1] flips the image
im = im[::-1]
plt.imshow(im)
plugins.connect(fig, plugins.MousePosition(fontsize=14))

mpld3.display()

# This is tool to mark the points and record them. The display is formated specially to useina cut and paste
# where the image arrays points are required.
import Tkinter
from PIL import Image, ImageTk
from sys import argv

window = Tkinter.Tk(className="Array Points")

image = Image.open("images/face.jpg")
canvas = Tkinter.Canvas(window, width=image.size[0], height=image.size[1])
canvas.pack()
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(image.size[0]//2, image.size[1]//2, image=image_tk)

def callback(event):
    #This is formated so the array results below may be cut and pasted.
    #Don'tforget toremove the final trailing comma the pasted area should start and end with [ ]
    print "[",event.x,",",event.y,"],"
 
canvas.bind("<Button-1>", callback)
Tkinter.mainloop()

from PIL import Image
im = Image.open("images/face.jpg")

image0 = im.crop((270,350, 400, 500))
image0.save("images/nose.jpg")

!showme images/nose.jpg

# this will will provide a finer tune ' croping array ' for seamless cloning
import Tkinter
from PIL import Image, ImageTk
from sys import argv

window = Tkinter.Tk(className="Array Points")

image = Image.open("images/nose.jpg")
canvas = Tkinter.Canvas(window, width=image.size[0], height=image.size[1])
canvas.pack()
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(image.size[0]//2, image.size[1]//2, image=image_tk)

def callback(event):
    #print "[",event.x,"],["+event.y,"]"
    print "[",event.x,",",event.y,"],",
 
canvas.bind("<Button-1>", callback)
Tkinter.mainloop()

# Saving multiple arrays in an npz file example:
# Create two arrays
x = np.arange(10)
y = np.sin(x)

#Using savez with *args, the arrays are saved with default names " ['arr_1', 'arr_0'] "
np.savez("numpy-filters/temp1", x, y)

!cp -R /home/conda/Desktop/NoteBooks/GRAPHICS/numpy-array-filters/numpy-filters .

npz = np.load("numpy-filters/temp1.npz")
npz.files

# Retrieve the first array for use
npz['arr_0']

# Retrieve the second array for use
npz['arr_1']
# Assigning a variable to the array
sin = npz['arr_1']
print sin

oranges = np.arange(10)
apples = np.sin(x)
np.savez("numpy-filters/example2", oranges=oranges, apples=apples)

npzfile = np.load("numpy-filters/example2.npz")
npzfile.files

npzfile['apples'] , npzfile['oranges'] 

import cv2
import numpy as np 

# Read face image ( dst destination of the nose src )
dst = cv2.imread("images/face.jpg")
# Read nose image ( src of the seamlesClone image )
src = cv2.imread("images/nose.jpg")


# Create a rough mask around the nose
src_mask = np.zeros(src.shape, src.dtype)

# notice the array above is cut and pasted here
poly = np.array([[ 33 , 21 ],
[ 3 , 111 ],
[ 11 , 135 ],
[ 69 , 144 ],
[ 122 , 137 ],
[ 129 , 92 ],
[ 75 , 14 ],
[ 65 , 12 ]], np.int32)

# This will save BOTH the nose image and the poly array in a single file src-mask001.npz
# notice below,  I am using src=src, poly=poly . 
#That will give me arrays npz['src'] and npz['poly']

np.savez('numpy-filters/nose_001', src=src, poly=poly) 

#place the nose image poly array in the 'rough' source mask
cv2.fillPoly(src_mask, [poly], (255, 255, 255))

# This is where the CENTER of the airplane will be placed
center = (340,255)

# Clone seamlessly.
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)

# Write result
cv2.imwrite("images/face_clone.jpg", output);
!showme images/face_clone.jpg

from PIL import Image
im = Image.open("images/face_clone.jpg")
im

# Get an image from public domain wiki
!wget -O images/woman.jpg https://upload.wikimedia.org/wikipedia/commons/1/1b/Young_Woman_Thinking.jpg

#get points for cropping image
import Tkinter
from PIL import Image, ImageTk
from sys import argv

window = Tkinter.Tk(className="Array Points")

image = Image.open("images/woman.jpg")
canvas = Tkinter.Canvas(window, width=image.size[0], height=image.size[1])
canvas.pack()
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(image.size[0]//2, image.size[1]//2, image=image_tk)

def callback(event):
    #print "[",event.x,"],["+event.y,"]"
    print "[",event.x,",",event.y,"],"
 
canvas.bind("<Button-1>", callback)
Tkinter.mainloop()

# Crop the Downloaded, images/woman.jpg, image.
from PIL import Image
img = Image.open("images/woman.jpg")

image0 = img.crop((350,70, 950, 600))
image0.save("images/Crop_woman.jpg")

img = Image.open("images/Crop_woman.jpg")
img

# View the files/arrays in the " nose_001.npz "
npz = np.load("numpy-filters/nose_001.npz")
npz.files

import cv2
import numpy as np 

# Read woman image
dst = cv2.imread("images/Crop_woman.jpg")

#load the nose image AND the numpy array around it
npz = np.load("numpy-filters/nose_001.npz")


# The src_mask requires shape from the original nose image
# be sure define this variable before creating the src_mask 
src=npz['src']

# cv2.fillPoly requires placing the poly array in the src_mask
poly=npz['poly']

#rough shape a mask
src_mask = np.zeros(src.shape, src.dtype)

#fill that rough mask with the poly array of the select areas of the nose image
# nose_001a.npz contains the nose image and the poly array
cv2.fillPoly(src_mask, [poly], (255, 255, 255))

# This is where the CENTER where the nose image will be placed
center = (265,210)

# Clone seamlessly.
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)

# Write result
cv2.imshow('dst', dst)
cv2.imwrite("images/face_clonez.jpg", output);
cv2.imshow('output', output)
cv2.imshow('src_mask', src_mask)
cv2.imshow('src', src)
cv2.waitKey(0)
cv2.destroyAllWindows()

Im = Image.open("images/face_clonez.jpg")

npz = np.load("numpy-filters/nose_001.npz")
src=npz['src']
poly=npz['poly']
print "POLY: ",poly , "\n \n SRC: ",src

from PIL import Image
im = Image.open("images/face.jpg")

# This variable allows manipulation on the open im without effecting it
temp = im.copy()

image0 = temp.crop((200,300, 450, 550))
image0.save("images/temp-nose.jpg")
#the original ' im '  is unaltered and may be used later inthe script



#if an image needs to be rotated, do it before final cropping and picking array points
import cv2
import numpy as np 
import scipy
from scipy import ndimage
# Read nose image

new = cv2.imread("images/temp-nose.jpg")

new1 = ndimage.interpolation.rotate(new, -5, axes=(1, 0), \
                                   reshape=True, output=None, \
                                   order=3,mode='constant', cval=0.0, prefilter=True)

cv2.imwrite("images/nose-rotate.jpg", new1);
cv2.imshow('new1', new1)
cv2.waitKey(0)
cv2.destroyAllWindows()

import time
timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "images/"+timestr+".png"
print filename

!mkdir images/seq

import cv2
import numpy as np 
import scipy
from scipy import ndimage
import time
from datetime import datetime



# Read woman image
dst = cv2.imread("images/nose.jpg")
count = 0
while (count < 360):
    timestr = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    junk = ndimage.interpolation.rotate(dst, count, axes=(1, 0), \
                                       reshape=True, output=None, \
                                       order=3,mode='constant', cval=0.0, prefilter=True)
    filename = "images/seq/"+timestr+".png"
    cv2.imwrite(filename, junk);
    #prevent the same filename on time based filenames
    time.sleep(1) 
    count = count +1
    #cv2.imshow('junk', junk)

    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

import cv2
import numpy as np 
import scipy
from scipy import ndimage
# Read woman image
dst = cv2.imread("images/nose.jpg")



junk = ndimage.interpolation.rotate(dst, 0, axes=(1, 0), \
                                   reshape=True, output=None, \
                                   order=3,mode='constant', cval=0.0, prefilter=True)

junk = junk + 100

cv2.imwrite("images/junk.jpg", junk);
cv2.imshow('junk', junk)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np 
import scipy
from scipy import ndimage
# Read woman image
dst = cv2.imread("images/Crop_woman.jpg")
#load the nose image AND the numpy array around it
npz = np.load("numpy-filters/nose_001.npz")
# The src_mask requires shape from the original nose image
# be sure define this variable before creating the src_mask 
src=npz['src']
# cv2.fillPoly requires placing the poly array in the src_mask
poly=npz['poly']

#rough shape a mask

src_mask = np.zeros(src.shape, src.dtype)

#fill that rough mask with the poly array of the select areas of the nose image
# nose_001a.npz contains the nose image and the poly array
cv2.fillPoly(src_mask, [poly], (255, 255, 255))

# This is where the CENTER where the nose image will be placed
center = (265,210)

# Clone seamlessly.
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)

# Write result
cv2.imwrite("images/face_clone-roll.jpg", output);
cv2.imshow('output', output)
cv2.imshow('src', src)
cv2.waitKey(0)
cv2.destroyAllWindows()

!showme images/nose-rotate.jpg

import cv2
import numpy as np 
import scipy
from scipy import ndimage
# Read woman image
dst = cv2.imread("images/Crop_woman.jpg")

#load the nose image AND the numpy array around it
#npz = np.load("numpy-filters/nose_001.npz")
#cv2.imwrite("test.png", npz)
npz = np.load("numpy-filters/nose_001.npz")
# The src_mask requires shape from the original nose image
# be sure define this variable before creating the src_mask 
src=npz['src']
cv2.imwrite("images/test1.png", src)
# cv2.fillPoly requires placing the poly array in the src_mask
poly=npz['poly']

src_mask = np.zeros(src.shape, src.dtype)

#fill that rough mask with the poly array of the select areas of the nose image
# nose_001a.npz contains the nose image and the poly array
test2 = cv2.fillPoly(src_mask, [poly], (255, 255, 255))
cv2.imwrite("images/test2.png", test2)
cv2.imshow('images/test2', test2)
cv2.waitKey(0)
cv2.destroyAllWindows()

!showme test2.png

import cv2
import numpy as np 
import scipy
from scipy import ndimage
# Read woman image
dst = cv2.imread("images/Crop_woman.jpg")

#load the nose image AND the numpy array around it
npz = np.load("numpy-filters/nose_001.npz")


# The src_mask requires shape from the original nose image
# be sure define this variable before creating the src_mask 
src=npz['src']

# cv2.fillPoly requires placing the poly array in the src_mask
poly=npz['poly']


newim = ndimage.interpolation.rotate(src, 23.5, axes=(1, 0), reshape=True, output=None, order=3,mode='constant', cval=0.0, prefilter=True)
cv2.imwrite("images/newim.png", newim)
cv2.imshow('src', newim)
cv2.waitKey(0)
cv2.destroyAllWindows()

export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig


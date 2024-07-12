-

### import os
import sys
from PIL import Image
import shutil
import time
import random
filename0= '/home/jack/Desktop/3DFRACT/Mandelbulb3Dv199/MutaGen5B93367881C0506~.png'
filename1='/home/jack/Desktop/3DFRACT/Mandelbulb3Dv199/sea3.jpg'
shutil.copy2(filename0, 'instagram/')
shutil.copy2(filename1, 'instagram/')
aa = Image.open(filename0).convert("RGB")
bb = Image.open(filename1).convert("RGB")
xx=aa.resize((640,640), Image.NEAREST)
yy=bb.resize((640,640), Image.NEAREST)
xx.save("junk/aa.png")
yy.save("junk/bb.png")
src = Image.open('junk/aa.png').convert('RGB')
dst = Image.open('junk/bb.png').convert('RGB')
src.save("junk/aa.png")
dst.save("junk/bb.png")
n = 5 #number of partitions per channel.
src_handle = Image.open("junk/bb.png")
dst_handle = Image.open("junk/aa.png")
src = src_handle.load()
dst = dst_handle.load()
assert src_handle.size[0]*src_handle.size[1] == dst_handle.size[0]*dst_handle.size[1],"images must be same size"
def makePixelList(img):
    l = []
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            l.append((x,y))
    return l
lsrc = makePixelList(src_handle)
ldst = makePixelList(dst_handle)
def sortAndDivide(coordlist,pixelimage,channel): #core
    global src,dst,n
    retlist = []
    #sort
    coordlist.sort(key=lambda t: pixelimage[t][channel])
    #divide
    partitionLength = int(len(coordlist)/n)
    if partitionLength <= 0:
        partitionLength = 1
    if channel < 2:
        for i in range(0,len(coordlist),partitionLength):
            retlist += sortAndDivide(coordlist[i:i+partitionLength],pixelimage,channel+1)
    else:
        retlist += coordlist
    return retlist

print(src[lsrc[0]])
lsrc = sortAndDivide(lsrc,src,0)
ldst = sortAndDivide(ldst,dst,0)
for i in range(len(ldst)):
    dst[ldst[i]] = src[lsrc[i]]
#filename = time.strftime("junk/post-color2560.png")
filename = time.strftime("/home/jack/Desktop/3DFRACT/Mandelbulb3Dv199/MutaGen0005.jpg")
dst_handle.save(filename)
shutil.copy2(filename, "instagram/")
print filename

!showme home/jack/Desktop/text-stuff/junk/post-color5.png

%reset -f

!ls

!locate Immanip

from Immanip import SwapPalettes
filename0 = '/home/jack/Desktop/text_stuff/instagram/PalletteTemp.png'
filename1 = '/home/jack/Desktop/text_stuff/instagram/sea1.jpg'
filename = 'pallet_test.jpg'
SwapPalettes.swappalettes(filename0,filename1,filename)

!rm /home/jack/anaconda2/lib/python2.7/site-packages/Immanip/SwapPalettes.pyc

%%writefile /home/jack/anaconda2/lib/python2.7/site-packages/Immanip/SwapPalettes.py
import os, errno
import sys
from PIL import Image
import shutil
import time
import random

def swappalettes(filename0,filename1,filename):
    try:
        os.makedirs('copies')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise    
    try:
        os.makedirs('tempS')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise    
    
    shutil.copy2(filename0, 'copies/')
    shutil.copy2(filename1, 'copies/')
    aa = Image.open(filename0).convert("RGB")
    bb = Image.open(filename1).convert("RGB")
    xx=aa.resize((640,640), Image.NEAREST)
    yy=bb.resize((640,640), Image.NEAREST)
    xx.save("tempS/aa.png")
    yy.save("tempS/bb.png")
    src = Image.open('tempS/aa.png').convert('RGB')
    dst = Image.open('tempS/bb.png').convert('RGB')
    src.save("tempS/aa.png")
    dst.save("tempS/bb.png")
    n = 5 #number of partitions per channel.
    src_handle = Image.open("tempS/bb.png")
    dst_handle = Image.open("tempS/aa.png")
    src = src_handle.load()
    dst = dst_handle.load()
    assert src_handle.size[0]*src_handle.size[1] == dst_handle.size[0]*dst_handle.size[1],"images must be same size"
    def makePixelList(img):
        l = []
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                l.append((x,y))
        return l
    lsrc = makePixelList(src_handle)
    ldst = makePixelList(dst_handle)
    def sortAndDivide(coordlist,pixelimage,channel): #core
        global src,dst,n
        retlist = []
        #sort
        coordlist.sort(key=lambda t: pixelimage[t][channel])
        #divide
        partitionLength = int(len(coordlist)/5)
        if partitionLength <= 0:
            partitionLength = 1
        if channel < 2:
            for i in range(0,len(coordlist),partitionLength):
                retlist += sortAndDivide(coordlist[i:i+partitionLength],pixelimage,channel+1)
        else:
            retlist += coordlist
        return retlist

    print(src[lsrc[0]])
    lsrc = sortAndDivide(lsrc,src,0)
    ldst = sortAndDivide(ldst,dst,0)
    for i in range(len(ldst)):
        dst[ldst[i]] = src[lsrc[i]]
    dst_handle.save(filename)
    shutil.copy2(filename, "copies/")
    print filename

%%writefile /home/jack/anaconda2/lib/python2.7/site-packages/Immanip/paletts.py
import os
import sys
from PIL import Image
import shutil
import time
import random
filename0= sys.argv[1]
filename1= sys.argv[2]
filename= sys.argv[3]
shutil.copy2(filename0, 'instagram/')
shutil.copy2(filename1, 'instagram/')
aa = Image.open(filename0).convert("RGB")
bb = Image.open(filename1).convert("RGB")
xx=aa.resize((640,640), Image.NEAREST)
yy=bb.resize((640,640), Image.NEAREST)
xx.save("junk/aa.png")
yy.save("junk/bb.png")
src = Image.open('junk/aa.png').convert('RGB')
dst = Image.open('junk/bb.png').convert('RGB')
src.save("junk/aa.png")
dst.save("junk/bb.png")
n = 5 #number of partitions per channel.
src_handle = Image.open("junk/bb.png")
dst_handle = Image.open("junk/aa.png")
src = src_handle.load()
dst = dst_handle.load()
assert src_handle.size[0]*src_handle.size[1] == dst_handle.size[0]*dst_handle.size[1],"images must be same size"
def makePixelList(img):
    l = []
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            l.append((x,y))
    return l
lsrc = makePixelList(src_handle)
ldst = makePixelList(dst_handle)
def sortAndDivide(coordlist,pixelimage,channel): #core
    global src,dst,n
    retlist = []
    #sort
    coordlist.sort(key=lambda t: pixelimage[t][channel])
    #divide
    partitionLength = int(len(coordlist)/n)
    if partitionLength <= 0:
        partitionLength = 1
    if channel < 2:
        for i in range(0,len(coordlist),partitionLength):
            retlist += sortAndDivide(coordlist[i:i+partitionLength],pixelimage,channel+1)
    else:
        retlist += coordlist
    return retlist

print(src[lsrc[0]])
lsrc = sortAndDivide(lsrc,src,0)
ldst = sortAndDivide(ldst,dst,0)
for i in range(len(ldst)):
    dst[ldst[i]] = src[lsrc[i]]
dst_handle.save(filename)
shutil.copy2(filename, "instagram/")
print filename

!python paletts.py junk/aa.png instagram/bb.png junk/skyPallette.png

from PIL import Image
im = Image.open("junk/Pallette.png")
im

%%writefile resize640.py
#!/home/jack/anaconda2/bin
from PIL import Image
import sys
sys.argv
def resize640(image, output):
    Bp=Image.open(image)
    width, height = Bp.size
    w1=int((width-height)/2)
    w2 = int(width-w1)
    h1=height-height
    h2=height
    Cc=Bp.crop((w1,h1,w2,h2))
    result = Cc.resize((640,640), Image.NEAREST)
    result.save(output)
if __name__ == '__main__':
    image = sys.arg[1:]
    output = sys.arg[2:]
    resize640(image, output)        

sys.argv

if __name__ == '__main__':
    dst = sys.arg[1:]
    src = sys.arg[2:]
    resize640(image, output) 

from PIL import Image, ImageOps
im = Image.open("junk/aa.png").convert('LA').convert('RGB')
im.save('junk/aaout.jpg')
im = Image.open("junk/aaout.jpg").convert('L')
#im.load() # make sure it's loaded into memory
assert im.mode == "L"
# create a lookup table (r, g, b, r, g, b, r, g, b, ...)
lut = []
for i in range(256):
    lut.extend([255-i, i/2, i])
im.putpalette(lut)
assert im.mode == "P" # now has a palette
im.save("junk/out.gif")
im

original_path = 'junk/posterize_gogh.jpg'
original = Image.open(original_path)
original

from PIL import Image, ImageFilter
import os
import cv2
import random
import time
path = r"AUGposT/"
#path = r"crawler4/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
    ])
filename0=(path+base_image)
im = Image.open(filename0)
imP = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=6)
imP.putpalette([
     243,164,10,
     157,17,17,
     66,99,166,
     70,155,53,
     0,0,0,
     70,70,140,
     ])


im2 = Image.open(filename0)
mask0 = im2.convert('L') # need a greyscale image to create a mask
mask = Image.eval(mask0, lambda a: 255 if a == 0 else 0)
mask = mask.filter(ImageFilter.MinFilter(3))
imP.paste(2, mask) # Paste the color of index 2 using image2 as a mask
filename = time.strftime("junk/PILStuff%Y%m%d%H%M%S.png")
imP.save(filename)

print filename
imP

from PIL import Image, ImageFilter
import os
import cv2
import random
import time
path = r"AUGposT/"
#path = r"crawler4/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
    ])
filename0=(path+base_image)
im = Image.open(filename0)
imP = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=6)
#imP.putpalette([
#     243,164,10,
#     157,17,17,
#     66,99,166,
#     70,155,53,
#     0,0,0,
#     70,70,140,
#     ])

list1 =  """ [0,0,0, 255,0,0, 0,255,0, 0,0,255, 125,125,125, 255,255,255,]
"""
imP.putpalette('%s' % (list1))




im2 = Image.open(filename0)
mask0 = im2.convert('L') # need a greyscale image to create a mask
mask = Image.eval(mask0, lambda a: 255 if a == 0 else 0)
mask = mask.filter(ImageFilter.MinFilter(3))
imP.paste(2, mask) # Paste the color of index 2 using image2 as a mask
filename = time.strftime("junk/PILStuff%Y%m%d%H%M%S.png")
imP.save(filename)

print filename
imP

# appears to be NON RGB
from PIL import Image, ImageMath
im1 = Image.open("junk/PILStuff20170826124220.png").convert("L")
im2 = Image.open("junk/YTUG.png").convert("L")
#out = ImageMath.eval("convert(min(a, b), 'RGB')", a=im1, b=im2)
out = ImageMath.eval("convert(min(a, b), 'L')", a=im1, b=im2)
out.save("junk/newResult2.jpg")
out

import numpy as np
from PIL import Image

def palette(img):
    """
    Return palette in descending order of frequency
    """
    arr = np.asarray(img)
    palette, index = np.unique(asvoid(arr).ravel(), return_inverse=True)
    palette = palette.view(arr.dtype).reshape(-1, arr.shape[-1])
    count = np.bincount(index)
    order = np.argsort(count)
    return palette[order[::-1]]

def asvoid(arr):
    """View the array as dtype np.void (bytes)
    This collapses ND-arrays to 1D-arrays, so you can perform 1D operations on them.
    http://stackoverflow.com/a/16216866/190597 (Jaime)
    http://stackoverflow.com/a/16840350/190597 (Jaime)
    Warning:
    >>> asvoid([-0.]) == asvoid([0.])
    array([False], dtype=bool)
    """
    arr = np.ascontiguousarray(arr)
    return arr.view(np.dtype((np.void, arr.dtype.itemsize * arr.shape[-1])))


img = Image.open('junk/PILStuff20170826142340.png', 'r').convert('RGB')
print(palette(img))

from PIL import Image
import time
def makePixelList(img):
    l = []
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            l.append((x,y))
    return l

lsrc = makePixelList(src_handle)
ldst = makePixelList(dst_handle)

def sortAndDivide(coordlist,pixelimage,channel): #core
    global src,dst,n
    retlist = []
    #sort
    coordlist.sort(key=lambda t: pixelimage[t][channel])
    #divide
    partitionLength = int(len(coordlist)/n)
    if partitionLength <= 0:
        partitionLength = 1
    if channel < 2:
        for i in range(0,len(coordlist),partitionLength):
            retlist += sortAndDivide(coordlist[i:i+partitionLength],pixelimage,channel+1)
    else:
        retlist += coordlist
    return retlist

print(src[lsrc[0]])

lsrc = sortAndDivide(lsrc,src,0)
ldst = sortAndDivide(ldst,dst,0)

for i in range(len(ldst)):
    dst[ldst[i]] = src[lsrc[i]]

#dst_handle.save("exchange"+str(src_index)+str(dst_index)+".png")
filename = time.strftime("junk/exchange%Y%m%d%H%M%S.png")
dst_handle.save(filename)
print filename


from colorthief import ColorThief
import string
import re
color_thief = ColorThief('junk/exchange20170826173902.png')
# build a color palette
palette = color_thief.get_palette(color_count=6)
name = " ".join(str(x) for x in palette)
table = string.maketrans( '', '' )
print name.translate(table,"(){}<>")

from PIL import Image, ImageFilter
import os
import cv2
import random
import time
path = r"AUGposT/"
#path = r"crawler4/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
    ])
filename0=(path+base_image)
im = Image.open(filename0)
imP = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=6)

list1 =  """ [0,0,0, 255,0,0, 0,255,0, 0,0,255, 125,125,125, 255,255,255,]
"""
imP.putpalette('%s' % (list1))


im2 = Image.open(filename0)
mask0 = im2.convert('L') # need a greyscale image to create a mask
mask = Image.eval(mask0, lambda a: 255 if a == 0 else 0)
mask = mask.filter(ImageFilter.MinFilter(3))
imP.paste(2, mask) # Paste the color of index 2 using image2 as a mask
filename = time.strftime("junk/PILStuff%Y%m%d%H%M%S.png")
imP.save(filename)

print filename
imP

from PIL import Image, ImageFilter
import os
import cv2
import random
import time
"""
path = r"AUGposT/"
#path = r"crawler4/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
    ])
filename0=(path+base_image)
im = Image.open(filename0)
"""
im= Image.open('crawler1/0032myth.jpg')
imP = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=6)

list1 =  """ [244,164,12,68,87,154,68,156,52,156,20,20,4,4,4,204,168,84,]
"""
imP.putpalette('%s' % (list1))

#name = 'marcog'
#number = 42
#print '%s %d' % (name, number)

#imP.putpalette(
#[244,164,12,68,87,154,68,156,52,156,20,20,4,4,4,204,168,84,]   
#)
# print "pasting at: (%s, %s)" % (paste_left, paste_top)
im2 = Image.open(filename0)
mask0 = im2.convert('L') # need a greyscale image to create a mask
mask = Image.eval(mask0, lambda a: 255 if a == 0 else 0)
mask = mask.filter(ImageFilter.MinFilter(3))
imP.paste(2, mask) # Paste the color of index 2 using image2 as a mask
filename = time.strftime("junk/PILStuff%Y%m%d%H%M%S.png")
imP.save(filename)

print filename
imP

from colorthief import ColorThief
import string
import re
color_thief = ColorThief('junk/PILStuff20170826124220.png')
# build a color palette
palette = color_thief.get_palette(color_count=6)
name = " ".join(str(x) for x in palette)
table = string.maketrans( '', '' )
newT = name.translate(table,",(){}<>")
palette = newT.replace(" ", ",")
print palette

# Works Fine
import PIL
from PIL import Image
file="junk/newResult2.jpg"
im = Image.open(file)
im_web = im.convert("P")
im_256 = im.convert("P", palette=PIL.Image.ADAPTIVE, colors=256)
im_16 = im.convert("P", palette=PIL.Image.ADAPTIVE, colors=16)
im_16

# ImageOps.
def _border(border):

def _color(color, mode):

def _lut(image, lut):

def autocontrast(image, cutoff=0, ignore=None):

def colorize(image, black, white):

def crop(image, border=0):

def deform(image, deformer, resample=Image.BILINEAR):

def equalize(image, mask=None):

def expand(image, border=0, fill=0):

def fit(image, size, method=Image.NEAREST, bleed=0.0, centering=(0.5, 0.5)):

def flip(image):

def grayscale(image):

def invert(image):

def mirror(image):

def posterize(image, bits):

def solarize(image, threshold=128):

def gaussian_blur(im, radius=None):

def unsharp_mask(im, radius=None, percent=None, threshold=None):


from PIL import Image,ImageOps
im = Image.open("crawler1/0010van_gogh.jpg")
solar=ImageOps.solarize(im, threshold=12)
solar

from PIL import Image
im = Image.open("crawler1/0010van_gogh.jpg").convert('LA').convert('RGB')
im.load() # make sure it's loaded into memory
im

from PIL import ImagePalette

ImagePalette(object)

%%writefile test002.py
#!/usr/bin/python
__author__ = 'Jack Northrup'
import sys, getopt
from PIL import Image 
image=''
output=''
 
###############################
# o == option
# a == argument passed to the o
###############################
# Cache an error with try..except 
# Note: options is the string of option letters that the script wants to recognize, with 
# options that require an argument followed by a colon (':') i.e. -i fileName
#
try:
    myopts, args = getopt.getopt(sys.argv[1:],"i:o:")
except getopt.GetoptError as e:
    print (str(e))
    print("Usage: %s -i input -o output" % sys.argv[0])
    sys.exit(2)
 
for o, a in myopts:
    if o == '-i':
        image=a
    elif o == '-o':
        output=a
 
# Display input and output file name passed as the args
print ("Input file : %s and output file: %s" % (image,output) )

!ls instagram

from PIL import Image
import scipy
import scipy.cluster
from pprint import pprint
image = Image.open('instagram/640fish.jpg')
NUM_CLUSTERS = 5

# Convert image into array of values for each point.
ar = scipy.misc.fromimage(image)
shape = ar.shape

# Reshape array of values to merge color bands.
if len(shape) > 2:
       ar = ar.reshape(scipy.product(shape[:2]), shape[2])

# Get NUM_CLUSTERS worth of centroids.
codes, _ = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)

# Pare centroids, removing blacks and whites and shades of really dark and really light.
original_codes = codes
for low, hi in [(60, 200), (35, 230), (10, 250)]:
        codes = scipy.array([code for code in codes 
        if not ((code[0] < low and code[1] < low and code[2] < low) or
              (code[0] > hi and code[1] > hi and code[2] > hi))])
        if not len(codes): codes = original_codes
        else: break

# Assign codes (vector quantization). Each vector is compared to the centroids
# and assigned the nearest one.
vecs, _ = scipy.cluster.vq.vq(ar, codes)

# Count occurences of each clustered vector.
counts, bins = scipy.histogram(vecs, len(codes))

# Show colors for each code in its hex value.
colors = [''.join(chr(c) for c in code).encode('hex') for code in codes]
total = scipy.sum(counts)
color_dist = dict(zip(colors, [count/float(total) for count in counts]))
pprint(color_dist)

# Find the most frequent color, based on the counts.
index_max = scipy.argmax(counts)
peak = codes[index_max]
color = ''.join(chr(c) for c in peak).encode('hex')

import struct
from PIL import Image
import scipy
import scipy.misc
import scipy.cluster

NUM_CLUSTERS = 5

print 'reading image'
im = Image.open('instagram/640fish.jpg')
im = im.resize((640, 640))      # optional, to reduce time
ar = scipy.misc.fromimage(im)
shape = ar.shape
ar = ar.reshape(scipy.product(shape[:2]), shape[2])

#print 'finding clusters'
codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
#print 'cluster centres:\n', codes

#vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
#counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

#index_max = scipy.argmax(counts)                    # find most frequent
#peak = codes[index_max]
#colour = ''.join(chr(c) for c in peak).encode('hex')
#print 'most frequent is %s (#%s)' % (peak, colour)

https://hhsprings.bitbucket.io/docs/programming/examples/python/PIL/Image__class_Image.html

import os
import requests
from StringIO import StringIO
import lxml.html as html
from PIL import Image
import scipy
import scipy.misc
import scipy.cluster
import numpy as np

NUM_CLUSTERS = 5

def detect_color(imgurl):
    im = Image.open(imgurl)
    im = im.resize((250, 250))      # optional, to reduce time
    ar = scipy.misc.fromimage(im)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2])
    ar = ar.astype(float)

    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)

    vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
    counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

    index_max = np.argmax(counts)                    # find most frequent
    peak = codes[index_max]
    colour = ''.join(chr(int(round(c))) for c in peak).encode('hex')
    if colour == "ffffff":
        value_second_max = np.sort(counts)[-2]
        index_second_max = np.where(counts==value_second_max)
        index_max = index_second_max[0][0]
        peak = codes[index_max]
        colour = ''.join(chr(int(round(c))) for c in peak).encode('hex')
    return colour
detect_color('instagram/640fish.jpg')

def hex2rgb(hexcode):
    rgb = tuple(map(ord,hexcode[1:].decode('hex')))
    return rgb
hexcode = raw_input("Enter a hex value: ")
rgbvalue = hex2rgb(hexcode)
print(rgbvalue)

# from pure python list data
from PIL import Image
img = Image.new("RGB", (640, 640),(29, 117, 100))  # multiple bands
img.save("hex.jpg")

from PIL import Image
im = Image.open("hex.jpg")
im

def rgb2hex(r,g,b):
    hex = "#{:02x}{:02x}{:02x}".format(r,g,b)
    return hex
def hex2rgb(hexcode):
    rgb = tuple(map(ord,hexcode[1:].decode('hex')))
    return rgb

r = int(input("Enter r: "))
g = int(input("Enter g: "))
b = int(input("Enter b: "))
rgb = (r,g,b)
hexvalue = rgb2hex(rgb[0],rgb[1],rgb[2])
print(hexvalue)

hexcode = raw_input("Enter a hex value: ")
rgbvalue = hex2rgb(hexcode)
print(rgbvalue)


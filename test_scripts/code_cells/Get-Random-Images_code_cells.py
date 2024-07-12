imagedir = open("jpg3.list", "r")
IMAGES =[]
for images in imagedir:
    if "docker" not in images:
        images = images.replace("\n","")
        IMAGES.append(images)


print(len(IMAGES))

from PIL import Image
import numpy
import cv2
from random import randint
import time

def binarize_image(img_path, target_path, threshold):
    """Binarize an image."""
    image_file = Image.open(img_path)
    image_file = image_file.resize((720,480)) 
    image = image_file.convert('L')  # convert image to monochrome
    image = numpy.array(image)
    image = binarize_array(image, threshold)
    cv2.imwrite(target_path, image)

def binarize_array(numpy_array, threshold=200):
    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
    return numpy_array

    
    
for i in range(350):    
    
    threshold = 100
    rnd = randint(0, len(IMAGES))
    img_path = IMAGES[rnd]
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "binary_images/"+timestr+"_"+str(i)+".png"
    target_path = filename
    print(".", end="|")
    binarize_image(img_path, target_path, threshold)    

!find . -iname '*.jpg' > jpg3.list

from random import randint
rnd = randint(0, len(IMAGES))
print(IMAGES[rnd])

print ( len(IMAGES))

!mkdir image_resources

import PIL
from time import sleep
for i in range(1,1000):
    sleep(1.5)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "image_resources/"+timestr+str(i)+"_.png"
    print (filename)

from PIL import Image
import time
imagedir = open("jpg.list", "r")
IMAGES =[]
for images in imagedir:
    if "docker" not in images:
        images = images.replace("\n","")
        IMAGES.append(images)

for i in range(0,1300):
    while True:
        try:
            # do stuff
            time.sleep(.5)
            rnd = randint(0, len(IMAGES))
            im = Image.open(IMAGES[rnd])
            newsize = (720, 480)
            im1 = im.resize(newsize)
            timestr = time.strftime("%Y%m%d-%H%M%S")
            filename = "image_resources/"+timestr+str(i)+"_.png"
            im1.save(filename)
            print(i,end=".")           
        except Exception:
            pass

        break


from PIL import Image
import time
from random import randint
cnt = 0
for i in range(130):
    time.sleep(.5)
    cnt =cnt+1
    rnd = randint(0, len(IMAGES))
    im = Image.open(IMAGES[rnd])
    newsize = (720, 480)
    im1 = im.resize(newsize)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "image_resources/"+timestr+str(i)+"_.png"
    im1.save(filename)
    print(i,end=".")

!mkdir blacknwhite_resources

import cv2
cnt = 0
import time
for i in range(30):
    cnt = cnt +1
    rnd = randint(0, len(IMAGES))
    im = Image.open(IMAGES[rnd])
    im.resize(720,480, "Image.NEAREST")
    originalImage = cv2.imread(IMAGES[rnd])
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "blacknwhite_resources/"+timestr+str(i)+"_.png"
    cv2.imwrite(filename, img)

  


import cv2

!mkdir binary_images

!ls

import numpy as np
import mahotas
from pylab import imshow, show
# importing required libraries
import mahotas as mh
from pylab import imshow, show
import cv2 
  
# loading image
img = cv2.imread('binary_images/20220921-104704_27.png')
  
# filtering the image
img = img[:, :, 0]
    
print("Image with filter")
# showing the image
imshow(img)
show()
  
# getting mean value
mean = img.mean()
  
# printing mean value
print("Mean Value for 0 channel : " + str(mean))

 
# getting nuclear image
nuclear = mh.demos.nuclear_image()
 
 
# filtering the image
nuclear = nuclear[:, :, 0]
 
print("Image with filter")
# showing the image
imshow(nuclear)
show()
 
# getting mean value
mean = nuclear.mean()
 
# printing mean value
print("Mean Value for 0 channel : " + str(mean))


# import using ``mh`` abbreviation which is common:
import mahotas as mh

# Load one of the demo images
im = mh.demos.load('nuclear')

# Automatically compute a threshold
T_otsu = mh.thresholding.otsu(im)

# Label the thresholded image (thresholding is done with numpy operations
seeds,nr_regions = mh.label(im > T_otsu)

# Call seeded watershed to expand the threshold
labeled = mh.cwatershed(im.max() - im, seeds)


import imread
dir (imread)

!ls

import os
from pylab import imshow, show
import cv2
for filename in os.listdir("junk/"):
    print (filename)


#mean()

IPYNB = []
f = open("ipynb.list","r").readlines()
for line in f:
    if "docker" not in line:
        line=line.replace("\n", "")
        IPYNB.append(line)

for notebook in IPYNB:
    if "dream" in notebook:
        print(notebook)

!cp /home/jack/Desktop/NOTEBOOKS/JupyterMaster/jupnote-master/Creating-C++-Image-blender.ipynb .

!cp /media/jack/HDD5003/Downloads/JupyterNotebook-Graphics-master/*.ipynb .

import shutil
src ="/home/jack/Desktop/TWITTER/JupyterNotebook-Graphics-master/GenIm.pynotebook150517524319150517524319.ipynb"
shutil.copyfile(src, "GenIm.pynotebook.ipynb")

rnd = randint(0, len(IMAGES))
image_path = IMAGES[rnd]
print(image_path)

API Key

APIkey()[0]

API Key Secret

APIkey()[1]


Access Token
APIkey()[2]

Access Token
APIkey()[3]


#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Binarize (make it black and white) an image with Python."""

from PIL import Image
from scipy.misc import imsave
import numpy


def binarize_image(img_path, target_path, threshold):
    """Binarize an image."""
    image_file = Image.open(img_path)
    image = image_file.convert('L')  # convert image to monochrome
    image = numpy.array(image)
    image = binarize_array(image, threshold)
    imsave(target_path, image)


def binarize_array(numpy_array, threshold=200):
    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
    return numpy_array


def get_parser():
    """Get parser object for script xy.py."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input",
                        dest="input",
                        help="read this file",
                        metavar="FILE",
                        required=True)
    parser.add_argument("-o", "--output",
                        dest="output",
                        help="write binarized file hre",
                        metavar="FILE",
                        required=True)
    parser.add_argument("--threshold",
                        dest="threshold",
                        default=200,
                        type=int,
                        help="Threshold when to show white")
    return parser


if __name__ == "__main__":
    args = get_parser().parse_args()
    binarize_image(args.input, args.output, args.threshold)


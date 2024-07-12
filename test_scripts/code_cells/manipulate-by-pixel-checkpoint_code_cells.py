import caffe

!sudo locate caffe/_caffe

sys.path.insert(0, "/usr/local/caffe/python/python/caffe")
import _caffe

import sys
sys.path.insert(0, "/usr/local/")
sys.path.insert(0, "/usr/local/caffe/python/python/caffe")
import caffe

from PIL import Image, ImageOps
import cv2
from cv2 import *

picture = Image.new( 'RGB', (5,5), "black")
# Get the size of the image
x, y = picture.size
h = x*-1
v = y*-1
while (h<x):
    while (v <y):
        
        
        v=v+1
    else:    
        h=h+1
        v=0
        


x=0
y=0

while (x<10):
    while (y <10):
        print x,y
        y=y+1
    else:    
        x=x+1
        y=0
        print x,y


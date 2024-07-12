

!mkdir 


timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "test/"+timestr+"_.png"
bg.save(filename)
im =Image.open('result.png')
im

dim = (720, 480)
 
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)





#nap=randint(10,400)
#time.sleep(nap)
path2 = r"binary_images/"
base_image = random.choice([
    x for x in os.listdir(path2)
    if os.path.isfile(os.path.join(path2, x))
])
file3=(path+base_image)

import cv2
import numpy as np
import time
import random
import os
from random import randint
from PIL import Image


dim = (720, 480)
path = r"publish/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
file1=(path+base_image)
print("file1 :",file1)
# read image 1
img1 = cv2.imread(file1)
im1 = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)



path1 = r"publish/"
base_image = random.choice([
    x for x in os.listdir(path1)
    if os.path.isfile(os.path.join(path1, x))
])
file2=(path1+base_image)
print("file2 :",file2)
# read image 2 and resize to same size as img1
img2 = cv2.imread(file2)
im2 = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)


path2 = r"binary_images/"
base_image = random.choice([
    x for x in os.listdir(path2)
    if os.path.isfile(os.path.join(path2, x))
])
file3=(path2+base_image)
#file3 ="/home/jack/Desktop/dockercommands/binary_images/20220921-164122_.png"
#file3 ="/home/jack/Desktop/dockercommands/binary_images/20220923-143435_0.png"
print("file3 :",file3)

# read saliency mask as grayscale and resize to same size as img1
mask = cv2.imread(file3)
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
mask = cv2.resize(mask, dim, interpolation = cv2.INTER_AREA)

# add img1 and img2
img12 = cv2.add(img1, img2)

# get mean of mask and shift mean to mid-gray
# desirable for hard light compositing
# add bias as needed
mean = np.mean(mask)
bias = -32
shift = 128 - mean + bias
mask = cv2.add(mask, shift)
mask = cv2.merge([mask,mask,mask])

# threshold mask at mid gray and convert to 3 channels
# (needed to use as src < 0.5 "if" condition in hard light)
thresh = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)[1]

# do hard light composite of img12 and mask
# see CSS specs at https://www.w3.org/TR/compositing-1/#blendinghardlight
img12f = img12.astype(np.uint8)/255
maskf =  mask.astype(np.uint8)/255
threshf =  thresh.astype(np.uint8)/255
threshf_inv = 1 - threshf
low = 2.0 * img12f * maskf
high = 1 - 2.0 * (1-img12f) * (1-maskf)
result = ( 255 * (low * threshf_inv + high * threshf) ).clip(0, 255).astype(np.uint8)

# save results
timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "test/"+timestr+"_.png"
cv2.imwrite(filename, result)
from PIL import Image
im = Image.open(filename)
im


from PIL import Image
im = Image.open("img12_hardlight.png")
im

!ls img12_hardlight.png

import cv2 as cv
import os
from time import sleep
def blenem(x):
    dim = (720, 480)
 
    #path1 = r"marblepaper/"
    path1 = r"image_resources/"
    base_image = random.choice([
    x for x in os.listdir(path1)
    if os.path.isfile(os.path.join(path1, x))])
    file1=(path1+base_image)
    print(file1)
    image = cv.imread(file1, cv.IMREAD_COLOR)
    # resize image
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    path = r"binary_images/"
    base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))])
    file2=(path+base_image)
    print(file2)
    
    od = cv.imread(file2, cv.IMREAD_GRAYSCALE)
    # resize image
    od = cv2.resize(od, dim, interpolation = cv2.INTER_AREA)
    other = cv.bitwise_not(od)
    res =  cv.bitwise_and(image, image, mask=other)
    path2 = r"binary_images/"
    base_image = random.choice([
    x for x in os.listdir(path2)
    if os.path.isfile(os.path.join(path2, x))])
    file3=(path2+base_image) 
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "test/XXX"+timestr+"_"+str(x)+".png"
    print(filename,end="-")
    cv.imwrite(filename, res)

    
    
try:    
    for x in range(0,500):    
        blenem(x)
        sleep(2)
except:
    pass       

import random
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageChops 
import os
import sys
import time
count = 0
PATHS=["art%20nouveau/","vintage%20magazine%20covers/","posterize/","antique%20book%20covers/",\
       "ancient%20manuscript%20art/","vintage%20advertisments/","ManRay/","polarized/"]
while count < 350:
    #path = r"art%20nouveau/"
    #path = r"vintage%20magazine%20covers/"
    #path = r"vintage%20clothing%20patterns/"
    #path = r"posterize/"
    path = r"output/"
    base_image = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    filename0=(path+base_image)
    print(filename0)

    #path0 = r"antique%20book%20covers/"
    #path0 = r"vintage%20advertisments/"
    #path0 = r"ancient%20manuscript%20art/"
    path0 = r"ManRay/"
    base_image0 = random.choice([
        x0 for x0 in os.listdir(path0)
        if os.path.isfile(os.path.join(path0, x0))
    ])
    filename00=(path0+base_image0)
    print(filename00)
    
    path1 = r"binary_images/"
    base_image1 = random.choice([
        x1 for x1 in os.listdir(path1)
        if os.path.isfile(os.path.join(path1, x1))
    ])
    mask0=(path1+base_image1)
    print(mask0)



    im0 = Image.open(filename0)
    im1 = im0.resize((720,480), Image.NEAREST)

    im01 = Image.open(filename00)
    im2 = im01.resize((720,480), Image.NEAREST)
    
    im03 = Image.open(mask0)
    im03 = im03.resize((720,480), Image.NEAREST)
    
    
    result1 = ImageChops.composite(im1, im2, im03) 
    
    filename = time.strftime("publish/"+str(count)+"_%Y%m%d%H%M%S.jpg")
    result1.save(filename)
    time.sleep(3)
    count= count +1

from PIL import Image
im = Image.open('test/20220924-041859_.png')
im

!ls test




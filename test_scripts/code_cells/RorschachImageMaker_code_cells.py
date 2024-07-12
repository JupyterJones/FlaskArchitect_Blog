%%writefile goodfrombad.py
#This one tries to to tell good blots from bad by particle_count`ing
# over twenty goes to one directory under twenty goes to another
from PIL import Image, ImageFilter, ImageOps
import numpy as np
import random
from random import randint
import sys
import time
import cv2
import pylab
from scipy import ndimage
count = 0
while count < 200:
    imgsize = 640, 640
    color = (0, 0, 0)
    img = Image.new("RGB", imgsize, "white")
    max_range = randint(100,700)
    for j in range(0,max_range):
        start = (random.randrange(0, imgsize[0]/2), random.randrange(0, imgsize[1]))
        point = start
        img.putpixel(point, color)
        """
        point_list = [p for p in 
                      [(point[0], point[1]+1), (point[0], point[1]-1), 
                       #(point[0]+1, point[1]+1), (point[0]-1, point[1]-1), 
                       #(point[0]-1, point[1]+1), (point[0]+1, point[1]-1), 
                       (point[0]+1, point[1]), (point[0]-1, point[1])]
                      if 0 < p[0] and 0 < p[1] < imgsize[1] and p not in avoid_points]
        """

        blotsize = random.randrange(0, 640)
        for i in range(blotsize):
            directions = [(point[0], point[1]+1), (point[0], point[1]-1),
                         (point[0]+1, point[1]+1), (point[0]-1, point[1]-1), 
                         (point[0]-1, point[1]+1), (point[0]+1, point[1]-1),                       
                         (point[0]+1, point[1]), (point[0]-1, point[1])]
            toremove = []
            for direction in directions:
                if direction[0]>=(imgsize[0]/2) or direction[1]>=imgsize[1] or direction[0]<0 or direction[1]<0:
                    toremove.append(direction)
            for d in toremove:
                directions.remove(d)
            point = random.choice(directions)
            img.putpixel(point, color)


    cropped = img.crop((0, 0, imgsize[0]//2, imgsize[1]))
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img.paste(cropped, (0, 0, imgsize[0]//2, imgsize[1]))
    rad = randint(5,30)
    img = img.filter(ImageFilter.GaussianBlur(radius=rad))
    img.save("images/blot.png")


    def binarize_array(numpy_array, threshold=200):
        """Binarize a numpy array."""
        for i in range(len(numpy_array)):
            for j in range(len(numpy_array[0])):
                if numpy_array[i][j] > threshold:
                    numpy_array[i][j] = 255
                else:
                    numpy_array[i][j] = 0
        return numpy_array

    filename0=('images/blot.png')

    im = Image.open(filename0)
    im_grey = im.convert('LA') # convert to grayscale
    width,height = im.size

    total=0
    for i in range(0,width):
        for j in range(0,height):
            total += im_grey.getpixel((i,j))[0]

    mean = total / (width * height)

    image_file = Image.open(filename0)
    imagex = image_file.convert('L')  # convert image to monochrome
    imagey = np.array(imagex)
    #imagez = binarize_array(imagey, threshold)
    imagez = binarize_array(imagey, mean)
    time.sleep(2)
    filename = time.strftime("TEMP/tmpp.png")
    cv2.imwrite(filename, imagez)

    im = cv2.imread('TEMP/tmpp.png')
    pylab.figure(0)
    pylab.imshow(im)

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)
    maxValue = 255
    adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C#cv2.ADAPTIVE_THRESH_MEAN_C #cv2.ADAPTIVE_THRESH_GAUSSIAN_C
    thresholdType = cv2.THRESH_BINARY#cv2.THRESH_BINARY #cv2.THRESH_BINARY_INV
    blockSize = 5 #odd number like 3,5,7,9,11
    C = -3 # constant to be subtracted
    im_thresholded = cv2.adaptiveThreshold(gray, maxValue, adaptiveMethod, thresholdType, blockSize, C) 
    labelarray, particle_count = ndimage.measurements.label(im_thresholded)
    
    if particle_count < 20:
        print"JUST RIGHT : ",particle_count
        filename = time.strftime("TEMP/good%Y%m%d%H%M%S.png")
        ImageOps.expand(Image.open('TEMP/tmpp.png').convert("RGB"),border=30,fill='red').save(filename)
        #cv2.imwrite(filename, imagez)
    else:
        print "TOO MUCH : ",particle_count
        filename = time.strftime("junk/toomany%Y%m%d%H%M%S.png")
        ImageOps.expand(Image.open('TEMP/tmpp.png').convert("RGB"),border=30,fill='red').save(filename)
        #cv2.imwrite(filename, imagez)
    print count    
    count = count+1




%%writefile GOODblot.py
import random
from PIL import Image, ImageFilter, ImageOps
import time
import cv2
from random import randint
import numpy as np
import os
#imgsize = (2000, 1000)
#seed_count = 10
#seed_max_size = 18000
count= 0
while count < 20:
    imgsize = (640, 640)
    seed_count = randint(6, 10)
    seed_max_size = randint(5000,16000)

    margin_h = 60
    margin_v = 60
    degradation = 10
    max_white = 100

    color = (0, 0, 0)
    img = Image.new("RGB", imgsize, "white")


    def next_points(point, avoid_points=[], shuffle=True):
        point_list = [p for p in 
                      [(point[0], point[1]+1), (point[0], point[1]-1), 
                       #(point[0]+1, point[1]+1), (point[0]-1, point[1]-1), 
                       #(point[0]-1, point[1]+1), (point[0]+1, point[1]-1), 
                       (point[0]+1, point[1]), (point[0]-1, point[1])]
                      if 0 < p[0] and 0 < p[1] < imgsize[1] and p not in avoid_points]

        for idx in range(len(point_list)):
            if point_list[idx][0] > imgsize[0]//2:
                point_list[idx] = (point[0], 
                                   point_list[idx][1] if point_list[idx][1] != point[1] else random.choice([point[1]+1,
                                                                                                            point[1]-1]))

        point_list = [p for p in point_list                  
                      if 0 < p[0] and 0 < p[1] < imgsize[1] and p not in avoid_points]

        if shuffle:
            random.shuffle(point_list)

        return point_list

    def degrade_color(color):
        return (color[0] + degradation, 
                color[1] + degradation,
                color[2] + degradation)

    def upgrade_color(color):
        return (color[0] - degradation//2, 
                color[1] - degradation//2,
                color[2] - degradation//2)

    def spread(img, point, color):
        if color[0] <= max_white and img.getpixel(point)[0] > color[0]:
            img.putpixel(point, color)
            points = next_points(point, shuffle=False)
            color = degrade_color(color)
            for point in points:
                spread(img, point, color)

    old_points = []
    posible_root_points = []
    for seed in range(0, seed_count):
        #print("Seed: %d" % seed)
        point = None
        while not point or point in old_points:
            point = (random.randrange(0 + margin_h, imgsize[0]//2), 
                     random.randrange(0 + margin_v, imgsize[1] - margin_v))
        old_points.append(point)
        posible_root_points.append(point)
        img.putpixel(point, color)

        seedsize = random.randrange(0, seed_max_size)
        #print("Seed size: %d" % seedsize)
        flow = 0
        for progress in range(0, seedsize):
            flow += 1
            points = next_points(point, old_points)
            try:
                point = points.pop()
            except IndexError:
                posible_root_points.remove(point)
                #print("Looking for old points... Seed: %d Seed Size: %d "
                      "Progress: %d Flow: %d Statistic: %d" % (seed,
                                                               seedsize,
                                                               progress,
                                                               flow, 
                                                               len(posible_root_points)))
                for idx in reversed(range(0, len(posible_root_points))):
                    points = next_points(posible_root_points[idx], old_points)
                    try:
                        point = points.pop()
                        #print("Using old point...")
                        flow = 0
                        break;
                    except IndexError:
                        posible_root_points.pop()
                if not point:
                    #print("No way!")
                    break

            old_points.append(point)
            posible_root_points.append(point)
            img.putpixel(point, color)

            for surr_point in points:
                spread(img, surr_point, degrade_color(color))

    print ("Cropping...")
    cropped = img.crop((0, 0, imgsize[0]//2, imgsize[1]))
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img.paste(cropped, (0, 0, imgsize[0]//2, imgsize[1]))
    img = img.filter(ImageFilter.GaussianBlur(radius=10))
    img.save("images/blot.png")


    def binarize_array(numpy_array, threshold=200):
        """Binarize a numpy array."""
        for i in range(len(numpy_array)):
            for j in range(len(numpy_array[0])):
                if numpy_array[i][j] > threshold:
                    numpy_array[i][j] = 255
                else:
                    numpy_array[i][j] = 0
        return numpy_array

    filename0=('images/blot.png')

    im = Image.open(filename0)
    im_grey = im.convert('LA') # convert to grayscale
    width,height = im.size

    total=0
    for i in range(0,width):
        for j in range(0,height):
            total += im_grey.getpixel((i,j))[0]

    mean = total / (width * height)

    image_file = Image.open(filename0)
    imagex = image_file.convert('L')  # convert image to monochrome
    imagey = np.array(imagex)
    #imagez = binarize_array(imagey, threshold)
    imagez = binarize_array(imagey, mean)
    time.sleep(2)
    filename = time.strftime("blot/tmmmp.png")
    cv2.imwrite(filename, imagez)
    filename = time.strftime("blot/GOODblots%Y%m%d%H%M%S.png")
    ImageOps.expand(Image.open('blot/tmmmp.png').convert("RGB"),border=30,fill='red').save(filename)
    print "GoodBlot : ",count
    count=count+1    

!mkdir blot

from PIL import Image, ImageFilter, ImageOps
import numpy as np
import random
from random import randint
import sys
import time
import cv2
count = 0
while count<20:
    imgsize = 640, 640
    color = (0, 0, 0)
    img = Image.new("RGB", imgsize, "white")
    max_range = randint(100,700)
    for j in range(0,max_range):
        start = (random.randrange(0, imgsize[0]/2), random.randrange(0, imgsize[1]))
        point = start
        img.putpixel(point, color)
        """
        point_list = [p for p in 
                      [(point[0], point[1]+1), (point[0], point[1]-1), 
                       #(point[0]+1, point[1]+1), (point[0]-1, point[1]-1), 
                       #(point[0]-1, point[1]+1), (point[0]+1, point[1]-1), 
                       (point[0]+1, point[1]), (point[0]-1, point[1])]
                      if 0 < p[0] and 0 < p[1] < imgsize[1] and p not in avoid_points]
        """

        #blotsize = random.randrange(0, 640)
        blotsize = random.randrange(0, max_range)
        for i in range(blotsize):
            directions = [(point[0], point[1]+1), (point[0], point[1]-1),
                         (point[0]+1, point[1]+1), (point[0]-1, point[1]-1), 
                         (point[0]-1, point[1]+1), (point[0]+1, point[1]-1),                       
                         (point[0]+1, point[1]), (point[0]-1, point[1])]
            toremove = []
            for direction in directions:
                if direction[0]>=(imgsize[0]/2) or direction[1]>=imgsize[1] or direction[0]<0 or direction[1]<0:
                    toremove.append(direction)
            for d in toremove:
                directions.remove(d)
            point = random.choice(directions)
            img.putpixel(point, color)


    cropped = img.crop((0, 0, imgsize[0]//2, imgsize[1]))
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img.paste(cropped, (0, 0, imgsize[0]//2, imgsize[1]))
    rad = randint(5,30)
    img = img.filter(ImageFilter.GaussianBlur(radius=rad))
    img.save("blots/blot.png")


    def binarize_array(numpy_array, threshold=200):
        """Binarize a numpy array."""
        for i in range(len(numpy_array)):
            for j in range(len(numpy_array[0])):
                if numpy_array[i][j] > threshold:
                    numpy_array[i][j] = 255
                else:
                    numpy_array[i][j] = 0
        return numpy_array

    filename0=('blots/blot.png')

    im = Image.open(filename0)
    im_grey = im.convert('LA') # convert to grayscale
    width,height = im.size

    total=0
    for i in range(0,width):
        for j in range(0,height):
            total += im_grey.getpixel((i,j))[0]

    mean = total / (width * height)

    image_file = Image.open(filename0)
    imagex = image_file.convert('L')  # convert image to monochrome
    imagey = np.array(imagex)
    #imagez = binarize_array(imagey, threshold)
    imagez = binarize_array(imagey, mean)
    time.sleep(2)
    filename = time.strftime("blots/tmpp.png")
    cv2.imwrite(filename, imagez)

    filename = time.strftime("blots/blot%Y%m%d%H%M%S.png")
    ImageOps.expand(Image.open('blots/tmpp.png').convert("RGB"),border=30,fill='red').save(filename)

    print count    
    count = count+1



*python GOODblot.py

from PIL import Image, ImageChops
import time
import os
import random
count = 0    
while count <3:    
    path = r"blots/"
    base_image = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
        ])
    filename0=(path+base_image)

    path0 = r"junk/"
    base_image0 = random.choice([
        x0 for x0 in os.listdir(path0)
        if os.path.isfile(os.path.join(path0, x0))
        ])
    filename00=(path0+base_image0)

    path1 = r"blots/"
    base_image1 = random.choice([
        x1 for x1 in os.listdir(path1)
        if os.path.isfile(os.path.join(path1, x1))
        ])
    mask0=(path1+base_image1)

    im0 = Image.open(filename0)
    im1 = im0.resize((700,700), Image.NEAREST)

    im01 = Image.open(filename00)
    im2 = im01.resize((700,700), Image.NEAREST)

    im03 = Image.open(mask0).convert("RGBA")
    
    result1 = ImageChops.composite(im1, im2, im03)
    #result = result1.resize((640,640), Image.NEAREST)
    #filename = time.strftime("tmp/blotstuff.jpg")
    
    
    filename = time.strftime("blots/fixedblot%Y%m%d%H%M%S.png")
    result1.save(filename)
    
    
    #ImageOps.expand(Image.open('tmp/blotstuff.jpg').convert("RGB"),border=30,fill='red').save(filename)
    time.sleep(4)
    count = count +1
   

# Good stuff
# Makes a mask from any image
# It takes the mean of a image and uses it as a threshold
from PIL import Image
import time
import random
from random import randint 
import cv2
import numpy as np
import os

def binarize_array(numpy_array, threshold=150):
    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
    return numpy_array

filename0=('fix/bot.png')
im = Image.open(filename0)
im = im.convert('LA')
img = im.filter(ImageFilter.GaussianBlur(radius=5))
cropped = img.crop((0, 0, imgsize[0]//2, imgsize[1]))
img = img.transpose(Image.FLIP_LEFT_RIGHT)
img.paste(cropped, (0, 0, imgsize[0]//2, imgsize[1]))


img.save("junk/blot.png")

    
image_file = Image.open("junk/blot.png")

width,height = image_file.size
total=0
for i in range(0,width):
    for j in range(0,height):
        total += im_grey.getpixel((i,j))[0]
mean = total / (width * height)

imagex = image_file.convert('L')  # convert image to monochrome
imagey = np.array(imagex)
#imagez = binarize_array(imagey, threshold)
imagez = binarize_array(imagey, mean)
time.sleep(2)
cv2.imwrite("tmp/fixtmpp.png", imagez)
filename = time.strftime("fix/Manual%Y%m%d%H%M%S.png")
ImageOps.expand(Image.open('tmp/fixtmpp.png').convert("RGB"),border=30,fill='red').save(filename)

print filename

# Good stuff
# Makes a mask from any image
# It takes the mean of a image and uses it as a threshold
from PIL import Image, ImageOps
import time
import random
from random import randint 
import cv2
import numpy as np
import os

def binarize_array(numpy_array, threshold=100):
    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
    return numpy_array

path = r"crawler1/"
base_image = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
        ])
filename0=(path+base_image)

im = Image.open(filename0)
im = im.convert('LA')

img = im.filter(ImageFilter.GaussianBlur(radius=5))
cropped = img.crop((0, 0, imgsize[0]//2, imgsize[1]))
img = img.transpose(Image.FLIP_LEFT_RIGHT)
img.paste(cropped, (0, 0, imgsize[0]//2, imgsize[1]))



img.save("junk/blot.png")

    
image_file = Image.open("junk/blot.png").convert("RGB")
img = ImageOps.invert(image_file)



width,height = image_file.size
total=0
for i in range(0,width):
    for j in range(0,height):
        total += im_grey.getpixel((i,j))[0]
mean = total / (width * height)

imagex = image_file.convert('L')  # convert image to monochrome
imagey = np.array(imagex)
#imagez = binarize_array(imagey, threshold)
imagez = binarize_array(imagey, mean)
time.sleep(2)
cv2.imwrite("tmp/fixtmpp.png", imagez)
filename = time.strftime("fix/Manual%Y%m%d%H%M%S.png")
ImageOps.expand(Image.open('tmp/fixtmpp.png').convert("RGB"),border=30,fill='red').save(filename)

print filename


# Good stuff
# Makes a mask from any image
# It takes the mean of a image and uses it as a threshold
from PIL import Image, ImageOps
import time
import random
from random import randint 
import cv2
import numpy as np
import os
count=0
while count<600:
    def binarize_array(numpy_array, threshold=100):
        """Binarize a numpy array."""
        for i in range(len(numpy_array)):
            for j in range(len(numpy_array[0])):
                if numpy_array[i][j] > threshold:
                    numpy_array[i][j] = 255
                else:
                    numpy_array[i][j] = 0
        return numpy_array
    #path = r"crawler1/"
    path = r"newstuff2/"
    base_image = random.choice([
            x for x in os.listdir(path)
            if os.path.isfile(os.path.join(path, x))
            ])
    filename0=(path+base_image)

    im = Image.open(filename0)
    im = im.convert('LA')

    img = im.filter(ImageFilter.GaussianBlur(radius=5))
    cropped = img.crop((0, 0, imgsize[0]//2, imgsize[1]))
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img.paste(cropped, (0, 0, imgsize[0]//2, imgsize[1]))
    img.save("junk/blot.png")
    image_file = Image.open("junk/blot.png").convert("RGB")
    img = ImageOps.invert(image_file)
    width,height = image_file.size
    total=0
    for i in range(0,width):
        for j in range(0,height):
            total += im_grey.getpixel((i,j))[0]
    mean = total / (width * height)
    imagex = image_file.convert('L')  # convert image to monochrome
    imagey = np.array(imagex)
    #imagez = binarize_array(imagey, threshold)
    imagez = binarize_array(imagey, mean)
    time.sleep(2)
    cv2.imwrite("tmp/fixtmpp.png", imagez)
    filename = time.strftime("fix/Manual%Y%m%d%H%M%S.png")
    ImageOps.expand(Image.open('tmp/fixtmpp.png').convert("RGB"),border=30,fill='red').save(filename)
    count=count+1


!showme fix/Manual20170903160308.png


!mkdir fix

import random
from PIL import Image, ImageFilter
import time
import cv2
import numpy as np
import os
#imgsize = (2000, 1000)
#seed_count = 10
#seed_max_size = 18000
imgsize = (640, 640)
seed_count = 8
seed_max_size = 9000
margin_h = 20
margin_v = 20
degradation = 10
max_white = 100
color = (0, 0, 0)
img = Image.new("RGB", imgsize, "white")
def next_points(point, avoid_points=[], shuffle=True):
    point_list = [p for p in 
                  [(point[0], point[1]+1), (point[0], point[1]-1), 
                   #(point[0]+1, point[1]+1), (point[0]-1, point[1]-1), 
                   #(point[0]-1, point[1]+1), (point[0]+1, point[1]-1), 
                   (point[0]+1, point[1]), (point[0]-1, point[1])]
                  if 0 < p[0] and 0 < p[1] < imgsize[1] and p not in avoid_points]
                   
    for idx in range(len(point_list)):
        if point_list[idx][0] > imgsize[0]//2:
            point_list[idx] = (point[0], 
                               point_list[idx][1] if point_list[idx][1] != point[1] else random.choice([point[1]+1,
                                                                                                        point[1]-1]))
                                                                                                        
    point_list = [p for p in point_list                  
                  if 0 < p[0] and 0 < p[1] < imgsize[1] and p not in avoid_points]
        
    if shuffle:
        random.shuffle(point_list)
                 
    return point_list

def degrade_color(color):
    return (color[0] + degradation, 
            color[1] + degradation,
            color[2] + degradation)
            
def upgrade_color(color):
    return (color[0] - degradation//2, 
            color[1] - degradation//2,
            color[2] - degradation//2)
            
def spread(img, point, color):
    if color[0] <= max_white and img.getpixel(point)[0] > color[0]:
        img.putpixel(point, color)
        points = next_points(point, shuffle=False)
        color = degrade_color(color)
        for point in points:
            spread(img, point, color)
            
old_points = []
posible_root_points = []
for seed in range(0, seed_count):
    print("Seed: %d" % seed)
    point = None
    while not point or point in old_points:
        point = (random.randrange(0 + margin_h, imgsize[0]//2), 
                 random.randrange(0 + margin_v, imgsize[1] - margin_v))
    old_points.append(point)
    posible_root_points.append(point)
    img.putpixel(point, color)

    seedsize = random.randrange(0, seed_max_size)
    print("Seed size: %d" % seedsize)
    flow = 0
    for progress in range(0, seedsize):
        flow += 1
        points = next_points(point, old_points)
        try:
            point = points.pop()
        except IndexError:
            posible_root_points.remove(point)
            print("Looking for old points... Seed: %d Seed Size: %d "
                  "Progress: %d Flow: %d Statistic: %d" % (seed,
                                                           seedsize,
                                                           progress,
                                                           flow, 
                                                           len(posible_root_points)))
            for idx in reversed(range(0, len(posible_root_points))):
                points = next_points(posible_root_points[idx], old_points)
                try:
                    point = points.pop()
                    print("Using old point...")
                    flow = 0
                    break;
                except IndexError:
                    posible_root_points.pop()
            if not point:
                print("No way!")
                break
            
        old_points.append(point)
        posible_root_points.append(point)
        img.putpixel(point, color)
        
        for surr_point in points:
            spread(img, surr_point, degrade_color(color))

print ("Cropping...")
cropped = img.crop((0, 0, imgsize[0]//2, imgsize[1]))
img = img.transpose(Image.FLIP_LEFT_RIGHT)
img.paste(cropped, (0, 0, imgsize[0]//2, imgsize[1]))
img = img.filter(ImageFilter.GaussianBlur(radius=10))
img.save("images/blot.png")

def binarize_array(numpy_array, threshold=200):
    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
    return numpy_array

filename0=('images/blot.png')
    
im = Image.open(filename0)
im_grey = im.convert('LA') # convert to grayscale
width,height = im.size

total=0
for i in range(0,width):
    for j in range(0,height):
        total += im_grey.getpixel((i,j))[0]

mean = total / (width * height)
    
image_file = Image.open(filename0)
imagex = image_file.convert('L')  # convert image to monochrome
imagey = np.array(imagex)
#imagez = binarize_array(imagey, threshold)
imagez = binarize_array(imagey, mean)
time.sleep(2)
filename = time.strftime("images/%Y%m%d%H%M%S.png")
cv2.imwrite(filename, imagez)
print filename




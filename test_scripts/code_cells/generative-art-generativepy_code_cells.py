https://github.com/JakobGlock/Generative-Art

https://pythoninformer.com/generative-art/fractals/kings-dream/
    You can try different values of the constants. A and B need to be in the range -3 tp +3,
    while C and D need to be in the range -1.5 to +1.5, otherwise the values wil fly off to 
    infinity rather than creating a pattern.

!locate generativepy

%%writefile saveunique.py
import time
def saveunique():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filen = "/tmp/"+timestr+".dat"
    return filen

from saveunique import saveunique
filename = saveunique()
print (filename)

from generativepy.bitmap import Scaler
from generativepy.nparray import make_nparray_data, save_nparray, load_nparray, make_npcolormap, apply_npcolormap, save_nparray_image
from generativepy.color import Color
import math
import numpy as np
from saveunique import saveunique

MAX_COUNT = 1000000
A = 2.379879
B = -0.7765145
C = -0.866918
D =  0.544728

#MAX_COUNT = 10000000
#A = 2.879879
#B = -0.765145
#C = -0.966918
#D = 0.744728

def paint(image, pixel_width, pixel_height, frame_no, frame_count):
    scaler = Scaler(pixel_width, pixel_height, width=4, startx=-2, starty=-2)

    x = 1.22
    y = 1.2
    for i in range(MAX_COUNT):
        x, y = math.sin(A*x)+B*math.sin(A*y), math.sin(C*x)+D*math.sin(C*y)
        px, py = scaler.user_to_device(x, y)
        image[py, px] += 1


def colorise(counts):
    counts = np.reshape(counts, (counts.shape[0], counts.shape[1]))
    power_counts = np.power(counts, 0.25)
    maxcount = np.max(power_counts)
    normalised_counts = (power_counts * 1023 / max(maxcount, 1)).astype(np.uint32)

    colormap = make_npcolormap(1024, [Color('black'), Color('blue'), Color('orange'), Color('yellow'), Color('white')])

    outarray = np.zeros((counts.shape[0], counts.shape[1], 3), dtype=np.uint8)
    apply_npcolormap(outarray, normalised_counts, colormap)
    return outarray


data = make_nparray_data(paint, 900, 900, channels=1)
Fname=saveunique() 
save_nparray(Fname, data)
save_nparray("tmp/temp.dat", data)
data = load_nparray("tmp/temp.dat")

frame = colorise(data)

save_nparray_image('temp/kings-dream.png', frame)

from PIL import Image
im = Image.open('temp/kings-dream.png')
im

from generativepy.bitmap import Scaler
from generativepy.nparray import make_nparray_data, save_nparray, load_nparray, make_npcolormap, apply_npcolormap, save_nparray_image
from generativepy.color import Color
import math
import numpy as np

MAX_COUNT = 10000000
A = 2.675869
B = -0.985145
C = -0.9136918
D = 0.784728


def paint(image, pixel_width, pixel_height, frame_no, frame_count):
    scaler = Scaler(pixel_width, pixel_height, width=4, startx=-2, starty=-2)

    x = 2
    y = 2
    for i in range(MAX_COUNT):
        x, y = math.sin(A*x)+B*math.sin(A*y), math.sin(C*x)+D*math.sin(C*y)
        px, py = scaler.user_to_device(x, y)
        image[py, px] += 1


def colorise(counts):
    counts = np.reshape(counts, (counts.shape[0], counts.shape[1]))
    power_counts = np.power(counts, 0.25)
    maxcount = np.max(power_counts)
    normalised_counts = (power_counts * 1023 / max(maxcount, 1)).astype(np.uint32)

    colormap = make_npcolormap(1024, [Color('rgb(255,45,120)'), Color('red'), Color('orange'), Color('yellow'), Color('white')])

    outarray = np.zeros((counts.shape[0], counts.shape[1], 3), dtype=np.uint8)
    apply_npcolormap(outarray, normalised_counts, colormap)
    return outarray


data = make_nparray_data(paint, 600, 600, channels=1)
Fname=saveunique() 
save_nparray(Fname, data)
save_nparray("tmp/temp.dat", data)
data = load_nparray("tmp/temp.dat")

frame = colorise(data)

save_nparray_image('tmp/kings-dream5.png', frame)

MAX_COUNT = 100000000
""""A = 0.9
B = -0.6013
C = 2.0
D = 0.5
"""
A = 0.943
B = -0.5013
C = 2.134
D = 0.5154
def paint(image, pixel_width, pixel_height, frame_no, frame_count):
    scaler = Scaler(pixel_width, pixel_height, width=3, startx=-2, starty=-2)

    x = 0.01
    y = -0.01
    for i in range(MAX_COUNT):
        x, y = x*x - y*y + A*x + B*y, 2*x*y + C*x + D*y
        px, py = scaler.user_to_device(x, y)
        image[py, px] += 1

#filename = temp_file('tinkerbell.dat')
Fname=saveunique() 
save_nparray(Fname, data)
filename = 'tmp/tinkerbell2.dat'
data = make_nparray_data(paint, 1000, 1000, channels=1)
save_nparray(filename, data)

def colorise(counts):
    counts = np.reshape(counts, (counts.shape[0], counts.shape[1]))
    power_counts = np.power(counts, 0.25)
    maxcount = np.max(power_counts)
    normalised_counts = (power_counts * 1023 / max(maxcount, 1)).astype(np.uint32)

    colormap = make_npcolormap(1024, [Color('black'), Color('red'), Color('orange'), Color('yellow'), Color('white')])

    outarray = np.zeros((counts.shape[0], counts.shape[1], 3), dtype=np.uint8)
    apply_npcolormap(outarray, normalised_counts, colormap)
    return outarray

data = load_nparray(filename)
frame = colorise(data)
save_nparray_image('tmp/tinkerbell3.png', frame)

from PIL import Image
im = Image.open('tmp/tinkerbell3.png')
im

!ls tmp

data = load_nparray("tmp/tinkerbell.dat")

frame = colorise(data)

save_nparray_image('tmp/tinkerbell.png', frame)

!cp /tmp/temp.dat /tmp/001.dat

import generativepy
dir(generativepy)

import generativepy
help(generativepy)

from generativepy import *

from generativepy import graph
help(graph)


!pip install easy_vector

!pip3 install pycairo==1.11.1

#https://martinmcbride.org/generative-art/fractals/tinkerbell-colour/
from generativepy.bitmap import Scaler
from generativepy.nparray import (make_nparray_data, make_npcolormap, save_nparray,
                                  load_nparray, save_nparray_image, apply_npcolormap)
from generativepy.color import Color
from generativepy.utils import temp_file
import numpy as np

MAX_COUNT = 256

def calc(c1, c2):
    x = y = 0
    for i in range(MAX_COUNT):
        x, y = x*x - y*y + c1, abs(2*x*y) + c2
        if x*x + y*y > 4:
            return i + 1
    return 0


def paint(image, pixel_width, pixel_height, frame_no, frame_count):
    scaler = Scaler(pixel_width, pixel_height, width=3.2, startx=-2, starty=-1.8)

    for px in range(pixel_width):
        for py in range(pixel_height):
            x, y = scaler.device_to_user(px, py)
            count = calc(x, y)
            image[py, px] = count


def colorise(counts):
    counts = np.reshape(counts, (counts.shape[0], counts.shape[1]))

    colormap = make_npcolormap(MAX_COUNT+1,
                               [Color('black'), Color('red'), Color('orange'), Color('yellow'), Color('white')],
                               [16, 8, 32, 128])

    outarray = np.zeros((counts.shape[0], counts.shape[1], 3), dtype=np.uint8)
    apply_npcolormap(outarray, counts, colormap)
    return outarray


data = make_nparray_data(paint, 800, 600, channels=1)

filename = temp_file('burning-ship.dat')
save_nparray(filename, data)
data = load_nparray(filename)

frame = colorise(data)

save_nparray_image('burning-ship.png', frame)



from PIL import Image
im = Image.open("burning-ship.png")
im

from generativepy.bitmap import Scaler
from generativepy.nparray import make_nparray_data, save_nparray, load_nparray, make_npcolormap, apply_npcolormap, save_nparray_image
from generativepy.color import Color
from generativepy.utils import temp_file
from generativepy.analytics import print_stats, print_histogram
import numpy as np
import math

MAX_COUNT = 10000000
A = -55
B = -1
C = 42

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

def colorise(counts):
    counts = np.reshape(counts, (counts.shape[0], counts.shape[1]))
    power_counts = np.power(counts, 0.25)
    maxcount = np.max(power_counts)
    normalised_counts = (power_counts * 1023 / max(maxcount, 1)).astype(np.uint32)

    colormap = make_npcolormap(1024, [Color('black'), Color('green'), Color('yellow'), Color('red')])

    outarray = np.zeros((counts.shape[0], counts.shape[1], 3), dtype=np.uint8)
    apply_npcolormap(outarray, normalised_counts, colormap)
    return outarray

def paint(image, pixel_width, pixel_height, frame_no, frame_count):
    scaler = Scaler(pixel_width, pixel_height, width=1000, startx=-500, starty=-500)

    x = -1
    y = 0
    for i in range(MAX_COUNT):
        inc = i*.00001
        x, y = y-math.sqrt(abs(B*x-C))*sign(x), A-x
        px, py = scaler.user_to_device(x, y)
        if 0 <= px < pixel_width and 0 <= py < pixel_height:
            image[py, px] += 1


filename = 'tmp/hopalong1.dat'

data = make_nparray_data(paint, 600, 600, channels=1)
save_nparray(filename, data)
data = load_nparray(filename)

frame = colorise(data)

save_nparray_image('tmp/hopalong1.png', frame)

from PIL import Image
im = Image.open("tmp/hopalong1.png")
im

from math import cos

from generativepy.bitmap import Scaler
from generativepy.nparray import make_nparray_data, save_nparray, load_nparray, make_npcolormap, apply_npcolormap, save_nparray_image
from generativepy.color import Color
from generativepy.utils import temp_file
from generativepy.analytics import print_stats, print_histogram
import numpy as np
import math
from math import *
MAX_COUNT = 1000000000
A = -55
B = -1
C = 42

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

def colorise(counts):
    counts = np.reshape(counts, (counts.shape[0], counts.shape[1]))
    power_counts = np.power(counts, 0.25)
    maxcount = np.max(power_counts)
    normalised_counts = (power_counts * 1023 / max(maxcount, 1)).astype(np.uint32)

    colormap = make_npcolormap(1024, [Color('black'), Color('green'), Color('yellow'), Color('red')])

    outarray = np.zeros((counts.shape[0], counts.shape[1], 3), dtype=np.uint8)
    apply_npcolormap(outarray, normalised_counts, colormap)
    return outarray

def paint(image, pixel_width, pixel_height, frame_no, frame_count):
    scaler = Scaler(pixel_width, pixel_height, width=1000, startx=-500, starty=-500)

    x = -2
    y = 2
    for i in range(0,MAX_COUNT):

      
        
        x, y = y-math.sqrt(abs(B*x-C))*cos(x), A-x
        px, py = scaler.user_to_device(x, y)
        if 0 <= px < pixel_width and 0 <= py < pixel_height:
            image[py, px] += 1


filename = 'tmp/hopalong5.dat'

data = make_nparray_data(paint, 720, 480, channels=1)
save_nparray(filename, data)
data = load_nparray(filename)

frame = colorise(data)

save_nparray_image('tmp/hopalong5.png', frame)

from PIL import Image
im = Image.open("tmp/hopalong5.png")
im

from generativepy.bitmap import Scaler
from generativepy.nparray import make_nparray_data, save_nparray, load_nparray, make_npcolormap, apply_npcolormap, save_nparray_image
from generativepy.color import Color
from generativepy.utils import temp_file
from generativepy.analytics import print_stats, print_histogram
import numpy as np
import math
from math import *
MAX_COUNT = 100000000
A = -55
B = -1
C = 42

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

def colorise(counts):
    counts = np.reshape(counts, (counts.shape[0], counts.shape[1]))
    power_counts = np.power(counts, 0.25)
    maxcount = np.max(power_counts)
    normalised_counts = (power_counts * 1023 / max(maxcount, 1)).astype(np.uint32)

    colormap = make_npcolormap(1024, [Color('black'), Color('green'), Color('yellow'), Color('red')])

    outarray = np.zeros((counts.shape[0], counts.shape[1], 3), dtype=np.uint8)
    apply_npcolormap(outarray, normalised_counts, colormap)
    return outarray

def paint(image, pixel_width, pixel_height, frame_no, frame_count):
    scaler = Scaler(pixel_width, pixel_height, width=500, startx=-50, starty=-50)

    x = -4
    y = 5
    a= .1
    b= .1
    for i in range(0,MAX_COUNT):

        x,y = sin(x*y)*y+cos(a*x-y),x+sin(y)
        if i % 1000000==0:print(i,end="-")
        
        #x, y = y-math.sqrt(abs(B*x-C))*cos(x), A-x
        px, py = scaler.user_to_device(x, y)
        if 0 <= px < pixel_width and 0 <= py < pixel_height:
            image[py, px] += 100


filename = 'tmp/hopalong8.dat'

data = make_nparray_data(paint, 1000, 1000, channels=1)
save_nparray(filename, data)
data = load_nparray(filename)
Fname=saveunique() 
save_nparray(Fname, data)

frame = colorise(data)

save_nparray_image('tmp/hopalong9.png', frame)

from PIL import Image
im = Image.open("tmp/hopalong9.png")
im

filename = 'tmp/hopalong8.dat'

data = make_nparray_data(paint, 100, 100, channels=1)
save_nparray(filename, data)
data = load_nparray(filename)
Fname=saveunique() 
save_nparray(Fname, data)

frame = colorise(data)

save_nparray_image('tmp/hopalong20.png', frame)

x and y both start at 1.0

x = sin(x*y/b)*y+cos(a*x-y)
y = x+sin(y)/b


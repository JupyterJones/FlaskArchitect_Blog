#!/home/jack/miniconda3/envs/cloned_base/bin/python

"""
@author: The Absolute Tinkerer
"""

import os
import math
import numpy as np
from time import sleep
from PyQt5.QtGui import QColor


def QColor_HSV(h, s, v, a=255):
    """
    Hue        : > -1 [wraps between 0-360]
    Saturation : 0-255
    Value      : 0-255
    Alpha      : 0-255
    """
    color = QColor()
    color.setHsv(*[int(e) for e in [h, s, v, a]])
    return color


def save(p, fname='image', folder='Images', extension='jpg', quality=100, overwrite=True):
    if not os.path.exists(folder):
        os.mkdir(folder)

    # The image name
    imageFile = f'{folder}/{fname}.{extension}'

    # Do not overwrite the image if it exists already
    if os.path.exists(imageFile):
        assert overwrite, 'File exists and overwrite is set to False!'

    # fileName, format, quality [0 through 100]
    p.saveImage(imageFile, imageFile[-3:], quality)


def Perlin2D(width, height, n_x, n_y, clampHorizontal=False, clampVertical=False):
    """
    Constructor

    Optimizations were gained from studying:
    https://github.com/pvigier/perlin-numpy/blob/master/perlin_numpy/perlin2d.py

    Parameters:
    -----------
    width : int
        The width of the canvas
    height : int
        The height of the canvas
    n_x : int
        The number of x tiles; must correspond to an integer x-edge length
    n_y : int
        The number of y tiles; must correspond to an integer y-edge length
    clampHorizontal : boolean
        Imagine the Perlin Noise on a sheet of paper - form a cylinder with
        the horizontal edges. If True, cylinder will be continuous noise
    clampVertical : boolean
        Imagine the Perlin Noise on a sheet of paper - form a cylinder with
        the vertical edges. If True, cylinder will be continuous noise

    Returns:
    --------
    <value> : numpy array
        noise values for array[width, height] between -1 and 1
    """
    # First ensure even number of n_x and n_y divide into the width and height,
    # respectively
    msg = 'n_x and n_y must evenly divide into width and height, respectively'
    assert width % n_x == 0 and height % n_y == 0, msg

    # We start off by defining our interpolation function
    def fade(t):
        return t * t * t * (t * (t * 6 - 15) + 10)

    # Next, we generate the gradients that we are using for each corner point
    # of the grid
    angles = 2 * np.pi * np.random.rand(n_x + 1, n_y + 1)
    r = math.sqrt(2)  # The radius of the unit circle
    gradients = np.dstack((r * np.cos(angles), r * np.sin(angles)))

    # Now, if the user has chosen to clamp at all, set the first and last row/
    # column equal to one another
    if clampHorizontal:
        gradients[-1, :] = gradients[0, :]
    if clampVertical:
        gradients[:, -1] = gradients[:, 0]

    # Now that gradient vectors are complete, we need to create the normalized
    # distance from each point to its starting grid point. In other words, this
    # is the normalized distance from the grid tile's origin based upon the
    # grid tile's width and height
    delta = (n_x / width, n_y / height)
    grid = np.mgrid[0:n_x:delta[0], 0:n_y:delta[1]].transpose(1, 2, 0) % 1

    # At this point, we need to compute the dot products for each corner of the
    # grid. To do this, we first need proper-dimensioned gradient vectors - do
    # this now. A computation for number of points per tile is needed as well
    px, py = int(width / n_x), int(height / n_y)
    gradients = gradients.repeat(px, 0).repeat(py, 1)
    g00 = gradients[:-px, :-py]
    g10 = gradients[px:, :-py]
    g01 = gradients[:-px, py:]
    g11 = gradients[px:, py:]

    # Compute dot products for each corner
    d00 = np.sum(g00 * grid, 2)
    d10 = np.sum(g10 * np.dstack((grid[:, :, 0] - 1, grid[:, :, 1])), 2)
    d01 = np.sum(g01 * np.dstack((grid[:, :, 0], grid[:, :, 1] - 1)), 2)
    d11 = np.sum(g11 * np.dstack((grid[:, :, 0] - 1, grid[:, :, 1] - 1)), 2)

    # We're doing improved perlin noise, so we use a fade function to compute
    # the x and y fractions used in the linear interpolation computation
    # t is the faded grid
    # u is the faded dot product between the top corners
    # v is the faded dot product between the bottom corners
    # _x and _y are the fractional (0-1) location of x, y in the tile
    t = fade(grid)
    u = d00 + t[:, :, 0] * (d10 - d00)
    v = d01 + t[:, :, 0] * (d11 - d01)

    # Now perform the second dimension's linear interpolation to return value
    return u + t[:, :, 1] * (v - u)

"""
@author: The Absolute Tinkerer
"""

import os
import math
import time
import random

import numpy as np

from PIL import Image

from PyQt5.QtGui import QColor, QPen, QPixmap
from PyQt5.QtCore import QPointF, QRect

import Painter
from utils import QColor_HSV, save, Perlin2D
def is_even(i):
    return i % 4000 == 0

def draw_white_noise(width, height, fname):
    assert not os.path.exists(fname), 'File already exists!'

    # Create a matrix of random values between zero and one
    pixels = np.random.random(size=(height, width))

    # Now modify the random values to be 0-255 (pixel color range)
    pixels = 255*pixels

    # The function to write the array of pixels to an image requires integers, not float values
    pixels = pixels.astype(np.uint8)

    # We choose to make random values grayscale, so each RGB element is identical. This code adds the third dimension
    # to our pixels array
    pixels = pixels[:, :, np.newaxis]

    # We need to repeat each value to finalize the pixels arrays in the grayscale space
    pixels = np.repeat(pixels, 3, axis=2)

    # Now create the image from an array of pixels
    im = Image.fromarray(pixels)

    # Save the image to file
    im.save(fname)


def draw_perlin(nx, ny, width, height, fname):
    assert not os.path.exists(fname), 'File already exists'

    # Initialize Perlin Noise
    noise = (Perlin2D(width, height, nx, ny) + 1)/2

    # Convert to pixels
    pixels = 255 * noise
    pixels = pixels.astype(np.uint8)
    pixels = pixels[:, :, np.newaxis]
    pixels = np.repeat(pixels, 3, axis=2)

    # Create and save the image from pixels
    im = Image.fromarray(pixels)
    im.save(fname)

    return noise


def draw_vectors(nx, ny, width, height, seed=random.randint(0, 100000000), flow_length=100, n_vectors=50):
    p_path = f'{seed}_1_perlin_noise.jpg'
    v_path = f'{seed}_2_vectors'
    f_path = f'{seed}_3_flow_field'

    # Ensure we don't overwrite paths
    assert not os.path.exists(p_path), 'Perlin Noise image already exists!'
    assert not os.path.exists(v_path), 'Vectors image already exists!'
    assert not os.path.exists(f_path), 'Flow field image already exists!'

    # Set the random seed for repeatability
    np.random.seed(seed)

    # Create the Perlin Noise image
    noise = draw_perlin(nx, ny, width, height, p_path)

    # Initialize the Painter object for drawing
    p = Painter.Painter(width, height)
    p.setRenderHint(p.Antialiasing)  # allow smooth drawing

    def draw_arrow(p, x_i, y_i, length=100, angle=0):
        # Compute the second points and draw the arrow body
        x_f = x_i + length*math.cos(math.radians(angle))
        y_f = y_i - length*math.sin(math.radians(angle))
        p.drawLine(x_i, y_i, x_f, y_f)

        # Compute the arrow head second points
        a_angle1, a_angle2 = math.radians(angle-30), math.radians(angle+30)
        x1 = x_f - (length/10)*math.cos(a_angle1)
        y1 = y_f + (length/10)*math.sin(a_angle1)
        x2 = x_f - (length/10)*math.cos(a_angle2)
        y2 = y_f + (length/10)*math.sin(a_angle2)
        p.drawLine(x_f, y_f, x1, y1)
        p.drawLine(x_f, y_f, x2, y2)

    # Load the Perlin Noise image and draw it with the Painter
    p.drawPixmap(QRect(0, 0, width, height), QPixmap(p_path))

    # Now we're drawing red arrows for vectors, so set the pen color to red
    p.setPen(QColor(255, 0, 0))

    # We need arrow locations, so create a grid of n_vectors x n_vectors, excluding the image border
    _nx, _ny = n_vectors, n_vectors
    dx, dy = width / (_nx + 1), height / (_ny + 1)
    x_points = [dx + i*dx for i in range(_nx)]
    y_points = [dy + i*dy for i in range(_ny)]

    # Draw the arrows
    for x in x_points:
        for y in y_points:
            angle = 360*noise[int(x), int(y)]
            draw_arrow(p, x, y, length=min(dx, dy), angle=angle)

    # Save the vector image
    save(p, fname=v_path, folder='.')

    # Now draw the flow field. Start by initializing a new Painter
    p = Painter.Painter(width, height)
    p.setRenderHint(p.Antialiasing)  # allow smooth drawing
    p.setPen(QColor(0, 0, 0))  # pen color set to black

    # Step size between points
    STEP_SIZE = 0.001 * max(width, height)

    # Draw the flow field
    for x in x_points:
        for y in y_points:
            # The starting position
            x_s, y_s = x, y
            # The current line length tracking variable
            c_len = 0
            while c_len < flow_length:
                # angle between 0 and 2*pi
                angle = 2 * noise[int(x_s), int(y_s)] * math.pi

                # Compute the new point
                x_f = x_s + STEP_SIZE * math.cos(angle)
                y_f = y_s - STEP_SIZE * math.sin(angle)

                # Draw the line
                p.drawLine(QPointF(x_s, y_s), QPointF(x_f, y_f))

                # Update the line length
                c_len += math.sqrt((x_f - x_s) ** 2 + (y_f - y_s) ** 2)

                # Break from the loop if the new point is outside our image bounds
                # or if we've exceeded the line length; otherwise update the point
                if x_f < 0 or x_f >= width or y_f < 0 or y_f >= height or c_len > flow_length:
                    break
                else:
                    x_s, y_s = x_f, y_f
    save(p, fname=f_path, folder='.')


def draw_flow_field(width, height, seed=random.randint(0, 100000000)):
    # Set the random seed for repeatability
    np.random.seed(seed)

    # These are color hues
    colors = [200, 140, 70, 340, 280]
    for i, mod in enumerate(colors):
        print('Starting Image %s/%s' % (i + 1, len(colors)))
        p = Painter.Painter(width, height)

        # Allow smooth drawing
        p.setRenderHint(p.Antialiasing)

        # Draw the background color
        p.fillRect(0, 0, width, height, QColor(0, 0, 0))

        # Set the pen color
        p.setPen(QPen(QColor(150, 150, 225, 5), 2))

        num = 1
        for j in range(num):
            print('Creating Noise... (%s/%s)' % (j + 1, num))
            p_noise = Perlin2D(width, height, 2, 2)
            print('Noise Generated! (%s/%s)' % (j + 1, num))

            MAX_LENGTH = 2 * width
            STEP_SIZE = 0.001 * max(width, height)
            NUM = int(width * height / 1000)
            POINTS = [(random.randint(0, width - 1), random.randint(0, height - 1)) for i in range(NUM)]

            for k, (x_s, y_s) in enumerate(POINTS):
                print(f'{100 * (k + 1) / len(POINTS):.1f}'.rjust(5) + '% Complete', end='\r')

                # The current line length tracking variable
                c_len = 0

                # Actually draw the flow field
                while c_len < MAX_LENGTH:
                    # Set the pen color for this segment
                    sat = 200 * (MAX_LENGTH - c_len) / MAX_LENGTH
                    hue = (mod + 130 * (height - y_s) / height) % 360
                    p.setPen(QPen(QColor_HSV(hue, sat, 255, 20), 2))

                    # angle between -pi and pi
                    angle = p_noise[int(x_s), int(y_s)] * math.pi

                    # Compute the new point
                    x_f = x_s + STEP_SIZE * math.cos(angle)
                    y_f = y_s + STEP_SIZE * math.sin(angle)

                    # Draw the line
                    p.drawLine(QPointF(x_s, y_s), QPointF(x_f, y_f))

                    # Update the line length
                    c_len += math.sqrt((x_f - x_s) ** 2 + (y_f - y_s) ** 2)

                    # Break from the loop if the new point is outside our image bounds
                    # or if we've exceeded the line length; otherwise update the point
                    if x_f < 0 or x_f >= width or y_f < 0 or y_f >= height or c_len > MAX_LENGTH:
                        break
                    else:
                        x_s, y_s = x_f, y_f

            save(p, fname=f'image_{mod}_{num}_{seed}', folder='.', overwrite=True)


def draw_perlin_rounding(width, height, fname, seed=random.randint(0, 100000000)):
    # Ensure we don't overwrite paths
    cnts = 0
    assert not os.path.exists(fname), 'Image already exists!'

    # Set the random seed for repeatability
    np.random.seed(seed)
    cnt=0
    # Initialize a new Painter
    p = Painter.Painter(width, height)
    p.setRenderHint(p.Antialiasing)

    # Draw the background color
    p.fillRect(0, 0, width, height, QColor(0, 0, 0))
    #p.fillRect(0, 0, width, height, QColor(100,100, 0))
    #p.setPen(QColor(255, 0, 0, 127))
    p.setPen(QPen(QColor(150, 150, 225, 5), 2))
    # Set the pen color
    #pc = 250 - cnt
    #if pc <10:pc=250
    #p.setPen(QColor(200, 200, pc))

    print('Creating Noise...', end='', flush=True)
    noise = Perlin2D(width, height, 1, 1)
    print('Done!')

    # The maximum line length and step size
    MAX_LENGTH = 1000
    STEP_SIZE = 0.001 * max(width, height)

    # Compute a grid 200x200 points, centered in the screen
    dx, dy = width / (200 + 1), height / (200 + 1)
    POINTS = [[(i+1)*dx, (j+1)*dy] for i in range(200) for j in range(200)]

    for i, (x_s, y_s) in enumerate(POINTS):
        print(f'{100 * (i + 1) / len(POINTS):.1f}'.rjust(5) + '% Complete', end='\r')

        # The current line length tracking variable
        c_len = 0
        while c_len < MAX_LENGTH:
            # angle between -pi and pi
            angle = math.pi*noise[int(x_s), int(y_s)]

            # Round the angle to pi/4 increments
            angle = round(angle / (math.pi / 4)) * (math.pi / 4)

            # Compute the new point
            x_f = x_s + STEP_SIZE * math.cos(angle)
            y_f = y_s + STEP_SIZE * math.sin(angle)

            # Draw the line
            p.drawLine(x_s, y_s, x_f, y_f)
            '''pc = 200 - cnts
            if pc <10:pc=200
                
            pa = 200 - cnts
            if pa <10:pa=200 
            
            
            pb = 0 + cnts
            if pb >200:pb=0 
            cnts=cnts+1 
            pc = 200 - cnts
            if pc <10:pc=200
                
            pa = 200 - cnts
            if pa <10:pa=200 
            
            
            pb = 0 + cnts
            if pb >200:pb=0 
            cnts=cnts+1 '''
            pa=100
            pb=100
            pc=0
            print(pa, pb, pc)    
            p.setPen(QColor(pa, pb, pc))
 
            if is_even(cnt):
                    scnt = str(cnt)
                    #save(p, fname=f'{fname}_{scnt}_{seed}', folder='.')
                    save(p, fname=f'{fname}{scnt}', folder='.')
                    print(i,":",end=" ")
                    #sleep(1)
            
            #scnt = str(cnt)
            #save(p, fname=f'{fname}_{scnt}_{seed}', folder='.')
            #print(f'{fname}_{scnt}_{seed}')
            cnt = cnt+1   
            # Update the line length
            c_len += math.sqrt((x_f - x_s) ** 2 + (y_f - y_s) ** 2)

            # Break from the loop if the new point is outside our image bounds
            # or if we've exceeded the line length; otherwise update the point
            if (x_f < 0 or x_f >= width or y_f < 0 or y_f >= height or
                    c_len > MAX_LENGTH):
                break
            else:
                x_s, y_s = x_f, y_f
                


class Body:
    def __init__(self, x, y, vx, vy):
        self._position = np.array([x, y], dtype=np.float64)
        self._velocity = np.array([vx, vy], dtype=np.float64)

    @property
    def position(self):
        return self._position

    @property
    def velocity(self):
        return self._velocity

    def update(self, dt):
        # update the body position
        self._position = self._position + dt*self._velocity


class ExpandingCircleRandom:
    def __init__(self, radius, num_bodies, center=(0, 0), v_limits=(-2, 2)):
        self._bodies = [Body(center[0] + radius*math.cos(i*2*math.pi/num_bodies),
                             center[1] + radius*math.sin(i*2*math.pi/num_bodies),
                             v_limits[0]+(v_limits[1]-v_limits[0])*random.random(),
                             v_limits[0]+(v_limits[1]-v_limits[0])*random.random()) for i in range(num_bodies)]

    def draw(self, dt, Painter):
        # Connect the dots between each body
        for i in range(len(self._bodies)):
            # Handle the wrapping case
            if i == len(self._bodies) - 1:
                p1 = QPointF(*self._bodies[i].position)
                p2 = QPointF(*self._bodies[0].position)
            else:
                p1 = QPointF(*self._bodies[i].position)
                p2 = QPointF(*self._bodies[i+1].position)
            Painter.drawLine(p1, p2)

        # Update the position of each body
        for i in range(len(self._bodies)):
            self._bodies[i].update(dt)


class ExpandingCircleNoise:
    def __init__(self, radius, num_bodies, noise, center=(0, 0), v_max=2):
        self._bodies = [Body(center[0] + radius*math.cos(i*2*math.pi/num_bodies),
                             center[1] + radius*math.sin(i*2*math.pi/num_bodies),
                             0, 0) for i in range(num_bodies)]
        self._v_max = v_max
        self._noise = noise

    def draw(self, dt, Painter):
        # Connect the dots between each body
        for i in range(len(self._bodies)):
            # Handle the wrapping case
            if i == len(self._bodies) - 1:
                p1 = QPointF(*self._bodies[i].position)
                p2 = QPointF(*self._bodies[0].position)
            else:
                p1 = QPointF(*self._bodies[i].position)
                p2 = QPointF(*self._bodies[i + 1].position)
            Painter.drawLine(p1, p2)

            # Try to update the velocity for each body. If we can't its because the point is beyond the noise
            # field we've created, so at that point, just maintain velocity.
            try:
                a = math.pi*self._noise[int(p1.x()), int(p1.y())]
                v = np.array([self._v_max*math.cos(a), self._v_max*math.sin(a)])
                self._bodies[i]._velocity = v
            except IndexError:
                pass

        # Update the position of each body
        for i in range(len(self._bodies)):
            self._bodies[i].update(dt)


def draw_delta_body(width, height, seed=random.randint(0, 100000000), mode='noise'):
    assert mode in ['noise', 'random'], 'Mode must either be "noise" or "random"'

    # Set the random seed for repeatability
    np.random.seed(seed)
    random.seed(seed)

    # Initialize the Painter
    p = Painter.Painter(width, height)
    p.setRenderHint(p.Antialiasing)  # Allow smooth drawing

    # Draw the background color
    p.fillRect(0, 0, width, height, QColor(0, 0, 0))

    # Set the pen color
    p.setPen(QPen(QColor(220, 220, 220, 5), 1))

    # Initialize the expanding circle centered in the canvas
    if mode == 'random':
        circle = ExpandingCircleRandom(width/8, 100, center=(width/2, height/2), v_limits=(-2, 2))
    elif mode == 'noise':
        noise = Perlin2D(width, height, 5, 5)
        circle = ExpandingCircleNoise(width/6, 200, noise, center=(width/4, height/2), v_max=5)
    else:
        circle = None

    # Initialize the delta time we're applying to each update
    dt = 0.3

    iterations = 1000
    for i in range(iterations):
        circle.draw(dt, p)

    save(p, fname=f'delta_{mode}_{seed}', folder='.', overwrite=True)

    

width = 1000
height = 1000
fname = "XXXX/0"

draw_perlin_rounding(width, height, fname, seed=random.randint(0, 100000000))

!rm -r XXXX

!mkdir XXXX

from PIL import Image
im = Image.open("XXXX/test.png_14233798.jpg")
im

def is_even(i):
    return i % 100 == 0

for i in range(0,1000):
    if is_even(i):
        print(i)

p.drawLine(x_s, y_s, x_f, y_f)
pc = 200 - cnts
if pc <10:pc=200;pa = 200 - cnts
if pa <10:pa=200;pb = 0 + cnts
if pb >200:pb=0;cnts=cnts+1           
print(pa, pb, pc)    


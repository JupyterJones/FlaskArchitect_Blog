from PIL import Image, ImageTk
import PIL
from sys import argv
import sys
from tkinter import *
import cv2
import numpy as np 
from sys import argv
'''
This script is a combination of Python code using the Tkinter library for GUI interactions and OpenCV for image processing. The purpose of the script appears to be to allow the user to click on points of an image displayed in a Tkinter window, record those points, and then use those points to perform a seamless clone operation with OpenCV. Let's break down the script in detail:
Step-by-Step Breakdown:

    Imports and Initializations:

    python

from PIL import Image, ImageTk
import PIL
from sys import argv
import sys
from tkinter import *
import cv2
import numpy as np

    PIL (Pillow): Used for opening and displaying images.
    sys: Provides access to system-specific parameters and functions.
    tkinter: Used to create GUI elements.
    cv2 (OpenCV): Used for image processing.
    numpy: Used for handling arrays, particularly for the points clicked on the image.

Setting up Tkinter Window:

python

window = Tk(className="Clickable")
data = []
image = PIL.Image.open("/home/jack/Desktop/FlaskBlog/TRANSITIONS/images/images/00022.jpg")
canvas = Canvas(window, width=image.size[0], height=image.size[1])
canvas.pack()
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(image.size[0]//2, image.size[1]//2, image=image_tk)

    A Tkinter window named "Clickable" is created.
    An empty list data is initialized to store the points clicked by the user.
    An image is loaded using PIL and displayed on a Tkinter canvas.

Callback Function for Mouse Clicks:

python

def callback(event):
    Data = [event.x, event.y]
    data.append(Data)
    print("[", event.x, ",", event.y, "],")

canvas.bind("<Button-1>", callback)
mainloop()

    The callback function captures the coordinates of mouse clicks on the canvas.
    These coordinates are appended to the data list.
    The canvas is bound to the <Button-1> event (left mouse click), so that each click calls the callback function.
    mainloop() starts the Tkinter event loop, waiting for user actions.

Using Collected Points for Seamless Cloning:

python

poly = np.array(data, np.int32)

dst = cv2.imread("/home/jack/Desktop/FlaskBlog/TRANSITIONS/images/images/00021.jpg")
src = cv2.imread("/home/jack/Desktop/FlaskBlog/TRANSITIONS/images/images/00022.jpg")
src_mask = np.zeros(src.shape, src.dtype)
cv2.fillPoly(src_mask, [poly], (255, 255, 255))

center = (250, 275)
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)
cv2.imwrite("01-cloning-xxz1.jpg", output)
im = PIL.Image.open("01-cloning-xxz1.jpg")
im.show()

    The collected points are converted to a numpy array poly.
    Two images are read using OpenCV: dst (destination image) and src (source image, which was also displayed in Tkinter).
    A mask src_mask of the same size as the source image is created and filled with the polygon defined by poly.
    The cv2.seamlessClone function performs the seamless cloning operation, blending the source image into the destination image at the specified center position using the mask.
    The result is saved to a file and displayed using PIL.

Additional Tkinter Window (Unused):

python

    import tkinter as tk
    Name = "fds"
    window = tk.Tk(className=Name)

    def change_className():
        global Name
        Name = "dsfsd"
        window.title(Name)

        This part of the script creates another Tkinter window and a function to change its title. However, this part is not connected to the main flow of the script.

Summary:

    GUI Setup: A Tkinter window displays an image, allowing the user to click on it.
    Data Collection: Click coordinates are collected and stored in a list.
    Image Processing: These points are used to create a mask, which is then used for seamless cloning with OpenCV.
    Display Result: The result of the seamless cloning is saved and displayed.

This script allows users to interactively select points on an image and use those points to perform a seamless cloning operation on another image, effectively blending the selected area into a new image.

Note: This script is only suitable for seamless cloning operations that involve a single source image and destination image.
'''

window = Tk(className="Clickable")
data = []
image = PIL.Image.open(argv[4])
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

# Read images
dst = cv2.imread(argv[3])
src = cv2.imread(argv[4])
src_mask = np.zeros(src.shape, src.dtype)
#poly = np.array([ [1,100], [1,50], [151,63], [254,37], [298,90], [272,134], [43,122] ], np.int32)
cv2.fillPoly(src_mask, [poly], (255, 255, 255))
# This is where the CENTER where thr 'poly' will be placed
center = (int(argv[1]),int(argv[2]))
print("center: ",center)
# Clone seamlessly.
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)
# Write result
cv2.imwrite("01-cloning-xxz1.jpg", output);
im = PIL.Image.open("01-cloning-xxz1.jpg")
im.show()

import tkinter as tk
Name="fds"
window = tk.Tk(className = Name)
def change_className():
    global Name
    Name = "dsfsd"
    window.title(Name)

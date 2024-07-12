from PIL import Image, ImageTk
import PIL
from sys import argv
import sys
from tkinter import *
import cv2
import numpy as np 

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

# Read images
dst = cv2.imread("/home/jack/Desktop/FlaskBlog/TRANSITIONS/images/images/00002.jpg")
src = cv2.imread("/home/jack/Desktop/FlaskBlog/TRANSITIONS/images/images/00002.jpg")
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
im.show()

import tkinter as tk
Name="fds"
window = tk.Tk(className = Name)
def change_className():
    global Name
    Name = "dsfsd"
    window.title(Name)
'''
#bool=True
button=tk.Button(window,command=change_className)
button.pack()
window.mainloop()

import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("My Do-Nothing Application")
myapp.master.minsize(600, 400)
myapp.master.maxsize(1000, 800)

# start the program
myapp.mainloop()



from PIL import Image, ImageTk
from sys import argv
from tkinter import *
import tkinter
from PIL import Image
window = tkinter.Tk(className="bla")

image = Image.open("mouse-sizing-n-cropping-files/jungle700.jpg")
canvas = tkinter.Canvas(window, width=image.size[0], height=image.size[1])
canvas.pack()
image_tk = ImageTk.PhotoImage(image)

data = (image.size[0]//2, image.size[1]//2, image==image_tk)
print (data)
#canvas.create_image(image.size[0]//2, image.size[1]//2, image==image_tk)

from PIL import Image, ImageTk
from sys import argv
from tkinter import *
import tkinter
from PIL import Image
window = tkinter.Tk(className="bla")

image = Image.open("mouse-sizing-n-cropping-files/jungle700.jpg")
canvas = tkinter.Canvas(window, width=image.size[0], height=image.size[1])
canvas.pack()
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(image.size[0]//2, image.size[1]//2, image=image_tk)

def callback(event):
    #print "[",event.x,"],["+event.y,"]"
    print ("[",event.x,",",event.y,"],",)

canvas.bind("<Button-1>", callback)
tkinter.mainloop()


'''
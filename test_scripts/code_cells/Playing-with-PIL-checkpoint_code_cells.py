from PIL import Image
filename = "/home/jack/Pictures/A_full_sized_highly_detailed_cad_drawn_blueprint_of_a_Mechanical_Toad_artistic_style_of_H._R._Giger (2).png" 
im = Image.open(filename)
im

from OutlineImage import outlineP
filename1 = "/home/jack/Pictures/A_full_sized_highly_detailed_cad_drawn_blueprint_of_a_Mechanical_Toad_artistic_style_of_H._R._Giger (2).png" 
filename1 = "onevid/tempp.png"
outfile_png = "onevid/temppp.png" 
outlineP(filename1,outfile_png)

from PIL import Image
#filename = "/home/jack/Pictures/A_full_sized_highly_detailed_cad_drawn_blueprint_of_a_Mechanical_Toad_artistic_style_of_H._R._Giger (2).png" 
im = Image.open(outfile_png)
im

photo_image_path = "/home/jack/Pictures/A_full_sized_highly_detailed_cad_drawn_blueprint_of_a_Mechanical_Toad_artistic_style_of_H._R._Giger (2).png" 
watermark_image_path = "/home/jack/Desktop/dockercommands/frame-lite.png"
image = Image.open(photo_image_path).convert('RGBA')
w,h = image.size
watermark = Image.open(watermark_image_path).convert('RGBA')
watermark = watermark.resize((w,h),Image.NEAREST)
layer = Image.new('RGBA', image.size, (0, 0, 0, 0))
x=0
y=0
layer.paste(watermark, (x, y))

# Create a copy of the layer
layer2 = layer.copy()

# Put alpha on the copy
layer2.putalpha(65)

# merge layers with mask
layer.paste(layer2, layer)


result = Image.alpha_composite(image, layer)

result

from PIL import Image
from PIL.Image import Exif
from PIL.ExifTags import TAGS, GPSTAGS

def get_exif(file_name) -> Exif:
    image: Image.Image = Image.open(file_name)
    return image.getexif()


def get_labeled_exif(exif):
    return {
        TAGS.get(key, key): value
        for key, value in exif.items()
    }


def get_geo(labeled_exif):
    gps_info = labeled_exif.get("GPSInfo", {})
    return {
        GPSTAGS.get(key, key): value
        for key, value in gps_info.items()
    }

if __name__ == '__main__':
    exif = get_exif("/home/jack/Pictures/content_example_ibiza.jpg")
    labeled_exif = get_labeled_exif(exif)
    #geo = get_geo(labeled_exif)
    #print(geo)
    print(labeled_exif)

class Foo(object):
    def __init__(self, val=2):
        self.val = val
    def __getstate__(self):
        print("I'm being pickled")
        self.val *= 2
        return self.__dict__
    def __setstate__(self, d):
        print("I'm being unpickled with these values: " + repr(d))
        self.__dict__ = d
        self.val *= 3

import pickle
f = Foo()
f_data = pickle.dumps(f)
f_new = pickle.loads(f_data)


img = Image.open("/home/jack/Pictures/content_example_ibiza.jpg")
img


# importing Image module from PIL package
from PIL import Image

# creating image object
img = Image.open("/home/jack/Pictures/content_example_ibiza.jpg")

# using image transform method
img1 = img.transform((300, 300), Image.EXTENT,
	data =[200, 20, 100 + img.width // 2, img.height // 2 ])
img1.save("junk/SHIP.jpg")
img1


import sys
from PIL import Image

img = Image.open("junk/SHIP.jpg")
width, height = img.size
m = -0.5
xshift = abs(m) * width
new_width = width + int(round(xshift))
img = img.transform((new_width, height), Image.AFFINE,
        (1, m, -xshift if m > 0 else 0, 0, 1, 0), Image.BICUBIC)
img.save("junk/SHIP-T.jpg")
img

import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def find_coefs(original_coords, warped_coords):
        matrix = []
        for p1, p2 in zip(original_coords, warped_coords):
            matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
            matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])

        A = np.matrix(matrix, dtype=float)
        B = np.array(warped_coords).reshape(8)

        res = np.dot(np.linalg.inv(A.T * A) * A.T, B)
        return np.array(res).reshape(8)


coefs = find_coefs(
                  [(867,652), (1020,580), (1206,666), (1057,757)],
                  [(700,732), (869,754), (906,916), (712,906)]
                  )

coefs_inv = find_coefs(
                  [(700,732), (869,754), (906,916), (712,906)],
                  [(867,652), (1020,580), (1206,666), (1057,757)]
                  )
filename = "/home/jack/Pictures/content_example_ibiza.jpg"
image = Image.open(filename)

img = image.transform(((1500,800)),
                      method=Image.PERSPECTIVE,
                      data=coefs_inv)

a, b, c, d, e, f, g, h = coefs

old_p1 = [50, 100]
x,y = old_p1
new_x = (a * x + b * y + c) / (g * x + h * y + 1)
new_y = (d * x + e * y + f) / (g * x + h * y + 1)
new_p1 = (int(new_x),int(new_y))

old_p2 = [400, 500]
x,y = old_p2
new_x = (a * x + b * y + c) / (g * x + h * y + 1)
new_y = (d * x + e * y + f) / (g * x + h * y + 1)
new_p2 = (int(new_x),int(new_y))



plt.figure()
plt.imshow(image)
plt.scatter([old_p1[0], old_p2[0]],[old_p1[1], old_p2[1]]  , s=150, marker='.', c='b')
plt.show()


plt.figure()
plt.imshow(img)
plt.scatter([new_p1[0], new_p2[0]],[new_p1[1], new_p2[1]]  , s=150, marker='.', c='r')

plt.show()

I = np.asarray(Image.open("junk/SHIP.jpg"))
#Do some stuff to I, then, convert it back to an image:

from PIL import ImageFilter

# Open an already existing image


# Apply sharp filter
#sharpened1 = I.filter(ImageFilter.SHARPEN);
#I = sharpened1.filter(ImageFilter.SHARPEN);


im = Image.fromarray(np.uint8(I))
im

import numpy as np
from PIL import Image
import scipy.signal
from scipy.signal import convolve2d
filename = "/home/jack/Pictures/content_example_ibiza.jpg"
image = Image.open(filename)
img_array = np.array(image)


def RGB_convolve(image,kern):
    image2 = np.empty_like(image)
    for dim in range(image.shape[-1]):
        image2[:,:,dim]=convolve2d(image[:,:,dim],kern, 'same')
    return image2

KERNEL_sharpen = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
im_filtered = RGB_convolve(img_array,KERNEL_sharpen)

#output_image = Image.fromarray(im_filtered)
#display(output_image)
output_image = Image.fromarray(im_filtered.astype('uint8'))
display(output_image)

# Load image
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image as grayscale
filename = "/home/jack/Pictures/content_example_ibiza.jpg"
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
# Create kernel
kernel = np.array([[0, -1, 0], 
                   [-1, 5,-1], 
                   [0, -1, 0]])

# Sharpen image
image_sharp = cv2.filter2D(image, -1, kernel)
# Show image
plt.imshow(image_sharp, cmap='gray'), plt.axis("off")
plt.show()


import numpy as np

def create_perspective_transform_matrix(src, dst):
    """ Creates a perspective transformation matrix which transforms points
        in quadrilateral ``src`` to the corresponding points on quadrilateral
        ``dst``.

        Will raise a ``np.linalg.LinAlgError`` on invalid input.
        """
    # See:
    # * http://xenia.media.mit.edu/~cwren/interpolator/
    # * http://stackoverflow.com/a/14178717/71522
    in_matrix = []
    for (x, y), (X, Y) in zip(src, dst):
        in_matrix.extend([
            [x, y, 1, 0, 0, 0, -X * x, -X * y],
            [0, 0, 0, x, y, 1, -Y * x, -Y * y],
        ])

    A = np.matrix(in_matrix, dtype=np.float)
    B = np.array(dst).reshape(8)
    af = np.dot(np.linalg.inv(A.T * A) * A.T, B)
    return np.append(np.array(af).reshape(8), 1).reshape((3, 3))


def create_perspective_transform(src, dst, round=False, splat_args=False):
    """ Returns a function which will transform points in quadrilateral
        ``src`` to the corresponding points on quadrilateral ``dst``::

            >>> transform = create_perspective_transform(
            ...     [(0, 0), (10, 0), (10, 10), (0, 10)],
            ...     [(50, 50), (100, 50), (100, 100), (50, 100)],
            ... )
            >>> transform((5, 5))
            (74.99999999999639, 74.999999999999957)

        If ``round`` is ``True`` then points will be rounded to the nearest
        integer and integer values will be returned.

            >>> transform = create_perspective_transform(
            ...     [(0, 0), (10, 0), (10, 10), (0, 10)],
            ...     [(50, 50), (100, 50), (100, 100), (50, 100)],
            ...     round=True,
            ... )
            >>> transform((5, 5))
            (75, 75)

        If ``splat_args`` is ``True`` the function will accept two arguments
        instead of a tuple.

            >>> transform = create_perspective_transform(
            ...     [(0, 0), (10, 0), (10, 10), (0, 10)],
            ...     [(50, 50), (100, 50), (100, 100), (50, 100)],
            ...     splat_args=True,
            ... )
            >>> transform(5, 5)
            (74.99999999999639, 74.999999999999957)

        If the input values yield an invalid transformation matrix an identity
        function will be returned and the ``error`` attribute will be set to a
        description of the error::

            >>> tranform = create_perspective_transform(
            ...     np.zeros((4, 2)),
            ...     np.zeros((4, 2)),
            ... )
            >>> transform((5, 5))
            (5.0, 5.0)
            >>> transform.error
            'invalid input quads (...): Singular matrix
        """
    try:
        transform_matrix = create_perspective_transform_matrix(src, dst)
        error = None
    except np.linalg.LinAlgError as e:
        transform_matrix = np.identity(3, dtype=np.float)
        error = "invalid input quads (%s and %s): %s" %(src, dst, e)
        error = error.replace("\n", "")

    to_eval = "def perspective_transform(%s):\n" %(
        splat_args and "*pt" or "pt",
    )
    to_eval += "  res = np.dot(transform_matrix, ((pt[0], ), (pt[1], ), (1, )))\n"
    to_eval += "  res = res / res[2]\n"
    if round:
        to_eval += "  return (int(round(res[0][0])), int(round(res[1][0])))\n"
    else:
        to_eval += "  return (res[0][0], res[1][0])\n"
    locals = {
        "transform_matrix": transform_matrix,
    }
    locals.update(globals())
    exec to_eval in locals, locals
    res = locals["perspective_transform"]
    res.matrix = transform_matrix
    res.error = error
    return res


from PyDraw import pydraw
img = pydraw.Image().new(width=500,height=500)
img.drawbezier([(22,22),(88,88),(188,22),(333,88)], fillcolor=(222,0,0))
img.drawcircle(333,111,fillsize=55,outlinecolor=(222,222,0))
img.drawline(0,250,499,250, fillcolor=(222,222,222))
img.floodfill(444,444,fillcolor=(0,222,0))
img.floodfill(222,222,fillcolor=(0,0,222))
img.view()

from __future__ import absolute_import

from pyping.core import *
#from .core import *

import pydraw

https://pypi.org/project/pydraw/

from pydraw import *
from tkinter import Tk
import sys
screen = Screen(800, 600, 'My First Project!')

# Here we create a rectangle at x=50, y=50 that is 50 pixels wide and 50 pixels tall.
# It is top-left anchored. This means that the position is the location of the top left corner.
# It's important to know that pydraw's canvas has the origin in the top left, with
# positive-y at the bottom of the screen, and positive-x to the right of the screen.
box = Rectangle(screen, 50, 50, 50, 50) 
a = Tk()
fps = 30
running = True
while running:
    screen.update()
    screen.sleep(1 / fps)

#screen.sys.exit()
#screen.exit()

def shutdown_ttk_repeat():
    a.eval('::ttk::CancelRepeat')
    a.destroy()

a.protocol("WM_DELETE_WINDOW", shutdown_ttk_repeat)
a.mainloop()


winfo.distroy()

screen.close()
box.close()


I've encountered a similar problem recently. The error message is exactly the same. 
I solved that by adding a a.quit() in an Exit method. (before that there was only 
                                                       a.destroy() in this method) 
Maybe you have already solved this question. But schlenk's answer doesn't work well 
on me. So I hope my answer can give another clue to such question


del box
del screen

from tkinter import Tk,Label,Button
from tkinter import ttk
from tkinter.ttk import Combobox

def cbox_do(event):
    'Used for cbox.'
    clabel.config(text=cbox.get())

a = Tk()
cbox = Combobox(a, value=('Luke','Biggs','Wedge'), takefocus=0)
cbox.bind("<<ComboboxSelected>>", cbox_do)
cbox.pack()
clabel = Label(a)
clabel.pack()

def shutdown_ttk_repeat():
    a.eval('::ttk::CancelRepeat')
    a.destroy()

a.protocol("WM_DELETE_WINDOW", shutdown_ttk_repeat)
a.mainloop()




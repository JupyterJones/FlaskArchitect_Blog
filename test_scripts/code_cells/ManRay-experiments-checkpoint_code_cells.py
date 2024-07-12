!ls haarcascades/haarcascade_frontalface_alt.xml

https://www.graph.cool/pricing/

import sys
sys.path.insert(0, "/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import cv2

%%writefile testblend.py
# ________  EXPERIMENT

"""
This opens two random images from the associated directories. Both images are resized to 
640x640. This is done in order to use the blend function. To use blend, both images must 
be the same size. The first image has a randomly created transparent region, to add 
to the effects. The blend is also a random alpha so all images created do not have an 
identical blend. All files saved are 640x640 and saved by " date-filename.png "
The purpose of these files are to create images to be pasted on the base or back 
ground collage piece.
"""
def Blend():
    import PIL
    import time
    from PIL import Image
    import random, os
    from random import randint
    import random, os
    path = r"../../GRAPHICS/gmic/640x640/"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])

    img1 = path+"/"+random_filename
    im1=Image.open(img1)
    longer_side = max(im1.size)
    basewidth = longer_side
    img = Image.open(img1)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    half_the_width = img.size[0] / 2
    half_the_height = img.size[1] / 2
    img4 = img.crop(
        (
            half_the_width - 320,
            half_the_height - 320,
            half_the_width + 320,
            half_the_height + 320
        )
    )
    img4.save("STUFF/"+"TEMP-img5.png")
    from PIL import ImageDraw
    im = Image.open("STUFF/"+"TEMP-img5.png")

    x1=(randint(1, 150))
    x2=(randint(1, 150))
    y1=(randint(151,320))
    y2=(randint(151, 320))
    transparent_area = (x1,x2,300,500)

    mask=Image.new('L', im.size, color=255)
    draw=ImageDraw.Draw(mask) 
    draw.rectangle(transparent_area, fill=0)
    im.putalpha(mask)
    im.save("STUFF/"+"TEMP-img4.png")
    path2 = r"../../GRAPHICS/gmic/640x640/"
    #path2 = r"bugs/advertisements1800/"
    random_filename2 = random.choice([
        y for y in os.listdir(path2)
        if os.path.isfile(os.path.join(path2, y))
    ])

    img1a = path2+"/"+random_filename2
    im1a=Image.open(img1a)
    basewidth = 640
    imga = Image.open(img1a)
    wpercent = (basewidth / float(imga.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    imga = imga.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    half_the_width = imga.size[0] / 2
    half_the_height = imga.size[1] / 2
    img4a = imga.crop(
        (
            half_the_width - 320,
            half_the_height - 320,
            half_the_width + 320,
            half_the_height + 320
        )
    )
    img4a.save("STUFF/"+"TEMP-img4a.png")
    img1 = "STUFF/"+"TEMP-img4.png"
    img2 = "STUFF/"+"TEMP-img4a.png"

    from PIL import Image
    #im1=Image.open(img1)
    #im1.size # (width,height) tuple
    #im2=Image.open(img2)
    #im2.size # (width,height) tuple
    background = Image.open(img1)
    overlay = Image.open(img2)

    #background = Image.open(img2)
    background = background.convert("RGBA")
    #overlay = Image.open(img2)
    overlay = overlay.convert("RGBA")
    Alpha=(randint(1, 9))*0.1
    new_img = Image.blend(background, overlay, Alpha)

    timename = time.strftime("%Y%m%d-%H%M%S")
    #filename = timename+".png"
    filename = timename
    #new_img.save(filename,"PNG")
    saveas = "ManRay_temp/"+filename+".png"
    new_img.save(saveas,"PNG")
    return saveas

from testblend import Blend
from time import sleep
count =0
while count <50:
    Blend()
    count=count+1
    sleep(1.5)
    print count,

#1- GOOD RANDOM resize and crop
import PIL
import time
from PIL import Image
import random, os
import random, os
count = 0
while (count < 5):

    path = r"photos"

    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    img1 = path+"/"+random_filename
    im1=Image.open(img1)
    basewidth = 1040
    img = Image.open(img1)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    half_the_width = img.size[0] / 2
    half_the_height = img.size[1] / 2
    img4 = img.crop(
        (
            half_the_width - 520,
            half_the_height - 520,
            half_the_width + 520,
            half_the_height + 520
        )
    )
    img4.save("TEMP/img4.png")

    path2 = r"photos"
    #path2 = r"bugs/advertisements1800/"
    random_filename2 = random.choice([
        y for y in os.listdir(path2)
        if os.path.isfile(os.path.join(path2, y))
    ])

    img1a = path2+"/"+random_filename2
    im1a=Image.open(img1a)
    basewidth = 1040
    imga = Image.open(img1a)
    wpercent = (basewidth / float(imga.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    imga = imga.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    half_the_width = imga.size[0] / 2
    half_the_height = imga.size[1] / 2
    img4a = imga.crop(
        (
            half_the_width - 520,
            half_the_height - 520,
            half_the_width + 520,
            half_the_height + 520
        )
    )
    img4a.save("TEMP/img4a.png")
    img1 = "TEMP/img4.png"
    img2 = "TEMP/img4a.png"

    from PIL import Image
    #im1=Image.open(img1)
    #im1.size # (width,height) tuple
    #im2=Image.open(img2)
    #im2.size # (width,height) tuple
    background = Image.open(img1)
    overlay = Image.open(img2)

    #background = Image.open(img2)
    background = background.convert("RGBA")
    #overlay = Image.open(img2)
    overlay = overlay.convert("RGBA")

    new_img = Image.blend(background, overlay, 0.5)



    new_img = new_img.convert("RGBA")


    #new = PIL.Image.new("RGB", 1040, 1040, color=1)
    white = (255,255,255)
    img_base = Image.new("RGB", [1040,1040], white)



    offset = (0, 0)
    new_img2 = img_base.paste(new_img, offset)




    #new_img2 = Image.blend(new_img, base_img, 1)

    timename = time.strftime("%Y%m%d-%H%M%S")
    #filename = timename+".png"
    filename = timename
    #new_img.save(filename,"PNG")

    img_base.save("ManRay/"+filename+".png","PNG")

    count = count +1
    time.sleep(1.5)
    print count,

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

from IPython.display import display, Image

from glob import glob

import PIL
images = [ PIL.Image.open(f) for f in glob('ManRay/*') ]

def img2array(im):
    if im.mode != 'RGB':
        im = im.convert(mode='RGB')
    return np.fromstring(im.tobytes(), dtype='uint8').reshape((im.size[1], im.size[0], 3))

np_images = [ img2array(im) for im in images ]

for img in np_images:
    plt.figure()
    plt.imshow(img)

#1- GOOD RANDOM resize and crop
#This is fine makes a 1040x1040 background
import PIL
import time
from PIL import Image
import random, os
import random, os
#count = 0
#while (count < 30):

    path = r"bugs/lupe/"

    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    img1 = path+"/"+random_filename
    im1=Image.open(img1)
    basewidth = 1040
    img = Image.open(img1)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    half_the_width = img.size[0] / 2
    half_the_height = img.size[1] / 2
    img4 = img.crop(
        (
            half_the_width - 520,
            half_the_height - 520,
            half_the_width + 520,
            half_the_height + 520
        )
    )
    img4.save("TEMP-img4.png")


    path2 = r"cycle/"
    #path2 = r"bugs/advertisements1800/"
    random_filename2 = random.choice([
        y for y in os.listdir(path2)
        if os.path.isfile(os.path.join(path2, y))
    ])

    img1a = path2+"/"+random_filename2
    im1a=Image.open(img1a)
    basewidth = 1040
    imga = Image.open(img1a)
    wpercent = (basewidth / float(imga.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    imga = imga.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    half_the_width = imga.size[0] / 2
    half_the_height = imga.size[1] / 2
    img4a = imga.crop(
        (
            half_the_width - 520,
            half_the_height - 520,
            half_the_width + 520,
            half_the_height + 520
        )
    )
    img4a.save("TEMP-img4a.png")
    img1 = "TEMP-img4.png"
    img2 = "TEMP-img4a.png"

    from PIL import Image
    #im1=Image.open(img1)
    #im1.size # (width,height) tuple
    #im2=Image.open(img2)
    #im2.size # (width,height) tuple
    background = Image.open(img1)
    overlay = Image.open(img2)

    #background = Image.open(img2)
    background = background.convert("RGBA")
    #overlay = Image.open(img2)
    overlay = overlay.convert("RGBA")

    new_img = Image.blend(background, overlay, 0.5)



    new_img = new_img.convert("RGBA")


    #new = PIL.Image.new("RGB", 1040, 1040, color=1)
    white = (255,255,255)
    img_base = Image.new("RGB", [1040,1040], white)



    offset = (0, 0)
    new_img2 = img_base.paste(new_img, offset)




    #new_img2 = Image.blend(new_img, base_img, 1)

    timename = time.strftime("%Y%m%d-%H%M%S")
    #filename = timename+".png"
    filename = timename
    #new_img.save(filename,"PNG")

    img_base.save("cycle2/"+filename+".png","PNG")

    #count = count +1
    return img_base

# 2- GOOD RANDOM resize and crop  Sepia experiment
import PIL
from PIL import Image, ImageOps
import random, os
import time

import random, os

count = 0
while (count < 30):


    path = r"/home/jack/Desktop/deep-dream-generator/notebooks/test/"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])

    img1 = path+"/"+random_filename
    im1=Image.open(img1)
    basewidth = 1040
    img = Image.open(img1)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    half_the_width = img.size[0] / 2
    half_the_height = img.size[1] / 2
    im = img.crop(
        (
            half_the_width - 520,
            half_the_height - 520,
            half_the_width + 520,
            half_the_height + 520
        )
    )




    # GOOD WORKING TURNS IMAGE SEPIA


    def make_linear_ramp(white):
        # putpalette expects [r,g,b,r,g,b,...]
        ramp = []
        r, g, b = white
        for i in range(255):
            ramp.extend((r*i/255, g*i/255, b*i/255))
        return ramp
    # make sepia ramp (tweak color as necessary)
    sepia = make_linear_ramp((255, 240, 192))

    #imgo=Image.open("newimage.png", "r")
    #im = Image.open(img1S, 'r')
    #img_w, img_h = imgo.size
    #background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))

    # convert to grayscale
    if im.mode != "L":
        im = im.convert("L")

    # optional: apply contrast enhancement here, e.g.
    im = ImageOps.autocontrast(im)

    # apply sepia palette
    im.putpalette(sepia)

    # convert back to RGB so we can save it as JPEG
    # (alternatively, save it in PNG or similar)
    #im = im.convert("RGB")

    #im.save("file.jpg")
    timename = time.strftime("%Y%m%d-%H%M%S")
    #filename = timename+".png"
    filename = timename
    #new_img.save(filename,"PNG")

    #background.save("STUFF/"+filename+".png","PNG")
    im.save("TEMP-img4.png","PNG")


    #img4.save("TEMP-img4.png")


    path2 = r"/home/jack/Desktop/deep-dream-generator/notebooks/test/"
    #path2 = r"bugs/deco/"
    random_filename2 = random.choice([
        y for y in os.listdir(path2)
        if os.path.isfile(os.path.join(path2, y))
    ])

    img1a = path2+"/"+random_filename2
    im1a=Image.open(img1a)
    basewidth = 1200
    imga = Image.open(img1a)
    wpercent = (basewidth / float(imga.size[0]))
    #hsize = int((float(img.size[1]) * float(wpercent)))
    hsize = basewidth
    imga = imga.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    half_the_width = imga.size[0] / 2
    half_the_height = imga.size[1] / 2
    img4a = imga.crop(
        (
            half_the_width - 520,
            half_the_height - 520,
            half_the_width + 520,
            half_the_height + 520
        )
    )
    img4a.save("TEMP-img4a.png")
    img1 = "TEMP-img4.png"
    img2 = "TEMP-img4a.png"

    from PIL import Image
    #im1=Image.open(img1)
    #im1.size # (width,height) tuple
    #im2=Image.open(img2)
    #im2.size # (width,height) tuple
    background = Image.open(img1)
    overlay = Image.open(img2)

    #background = Image.open(img2)
    background = background.convert("RGBA")
    #overlay = Image.open(img2)
    overlay = overlay.convert("RGBA")

    new_img = Image.blend(background, overlay, 0.5)



    timename = time.strftime("%Y%m%d-%H%M%S")
    #filename = timename+".png"
    filename = timename
    #new_img.save(filename,"PNG")

    new_img.save("/home/jack/Desktop/deep-dream-generator/notebooks/ManRay_temp/"+filename+".png","PNG")
return new_image
count = count +1

# 4- GooD -EXPERIMENT
import PIL
from PIL import Image
from PIL import Image
import random, os
from PIL import Image
import time
import random, os
count = 0
while (count < 30):



    path = r"/home/jack/Desktop/deep-dream-generator/notebooks/test"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])

    img1 = path+"/"+random_filename
    im1=Image.open(img1)

    basewidth = 1040
    img = Image.open(img1)
    wpercent = (basewidth / float(img.size[0]))
    #hsize = int((float(img.size[1]) * float(wpercent)))
    hsize = basewidth
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    half_the_width = img.size[0] / 2
    half_the_height = img.size[1] / 2
    img4 = img.crop(
        (
            half_the_width - 520,
            half_the_height - 520,
            half_the_width + 520,
            half_the_height + 520
        )
    )
    #img4.save("TEMP-img4.png")



    path2 = "/home/jack/Desktop/deep-dream-generator/notebooks/test"
    random_filename2 = random.choice([
        y for y in os.listdir(path2)
        if os.path.isfile(os.path.join(path2, y))
    ])

    img1a = path2+"/"+random_filename2
    im1a=Image.open(img1a)
    basewidth = 1040
    imga = Image.open(img1a)
    wpercent = (basewidth / float(imga.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    imga = imga.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    #half_the_width = imga.size[0] / 2
    #half_the_height = imga.size[1] / 2
    from random import randint
    x1=(randint(1, 520-count))
    x2=(randint(1, 520-count))
    x3=(randint(x1, 1039-count))
    x4=(randint(x2, 1039-count))

    img4a = imga.crop(
        (
            x1,
            x2,
            x3,
            x4,
        )
    )
    img4a.save("TEMP-img4a.png")
    img1 = "TEMP-img4.png"
    img2 = "TEMP-img4a.png"

    from PIL import Image
    #im1=Image.open(img1)
    #im1.size # (width,height) tuple
    #im2=Image.open(img2)
    #im2.size # (width,height) tuple
    background = Image.open(img1)
    overlay = Image.open(img2)

    #background = Image.open(img2)
    background = background.convert("RGBA")
    #overlay = Image.open(img2)
    #overlay = overlay.convert("RGBA")
    overlay = overlay.convert("RGBA")

    bg_w, bg_h = background.size
    ctr1=random.randint(50, 700)
    ctr2=random.randint(50, 700)

    offset = (ctr1-200, ctr2-200)

    #image=Image.open("star_blue.png")
    #Alpha=(randint(4, 9))*0.1
    bands=list(overlay.split())
    if len(bands)==4:
        bands[3]=bands[3].point(lambda x:x*1)
        new_image=Image.merge(overlay.mode,bands)

    #new_img = Image.blend(background, overlay, 0.3)
    background.paste(new_image, offset)

    timename = time.strftime("%Y%m%d-%H%M%S")
    #filename = timename+".png"
    filename = timename
    #new_img.save(filename,"PNG")
    #background.save("STUFF/experiment/TEMP-img4a.png","PNG")
    background.save("/home/jack/Desktop/deep-dream-generator/notebooks/ManRay_temp/XXXexperiment.png","PNG")
    time.sleep(1.5)    #
count=count+1

# 4- GooD -EXPERIMENT
#KEE
import PIL
from PIL import Image
from PIL import Image
import random, os
from PIL import Image
import time
import random, os
count = 0
while (count < 30):



    path = r"bugs/spiders/"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])

    img1 = path+"/"+random_filename
    im1=Image.open(img1)

    basewidth = 1040
    img = Image.open(img1)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    hsize = basewidth
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    half_the_width = img.size[0] / 2
    half_the_height = img.size[1] / 2
    img4 = img.crop(
        (
            half_the_width - 520,
            half_the_height - 520,
            half_the_width + 520,
            half_the_height + 520
        )
    )
    img4.save("TEMP-img4.png")



    path2 = "bugs/vintage-labels/"
    random_filename2 = random.choice([
        y for y in os.listdir(path2)
        if os.path.isfile(os.path.join(path2, y))
    ])

    img1a = path2+"/"+random_filename2
    im1a=Image.open(img1a)
    
    inter= 500-(count*3)
    side=(randint(1, 70))
    sidea=(randint(1, inter))
    sideb= side+sidea
    img4a = im1a.resize((sidea,sideb), PIL.Image.ANTIALIAS)
    
    
    
    
    
    
    
    
  
    #basewidth = x1
    #imga = Image.open(img1a)
    #wpercent = (basewidth / float(imga.size[0]))
    #hsize = int((float(img.size[1]) * float(wpercent)))
    #img4a = imga.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    #half_the_width = imga.size[0] / 2
    #half_the_height = imga.size[1] / 2
    from random import randint
    x1=(randint(1, 520-count))
    
    img4a.save("TEMP-img4a.png")
    img1 = "TEMP-img4.png"
    img2 = "TEMP-img4a.png"

    from PIL import Image
    #im1=Image.open(img1)
    #im1.size # (width,height) tuple
    #im2=Image.open(img2)
    #im2.size # (width,height) tuple
    background = Image.open(img1)
    overlay = Image.open(img2)

    #background = Image.open(img2)
    background = background.convert("RGBA")
    #overlay = Image.open(img2)
    #overlay = overlay.convert("RGBA")
    overlay = overlay.convert("RGBA")

    bg_w, bg_h = background.size
    ctr1=random.randint(1, 900)
    ctr2=random.randint(1, 900)

    offset = (ctr1-200, ctr2-200)

    #image=Image.open("star_blue.png")
    #Alpha=(randint(4, 9))*0.1
    bands=list(overlay.split())
    if len(bands)==4:
        bands[3]=bands[3].point(lambda x:x*1)
        new_image=Image.merge(overlay.mode,bands)

    #new_img = Image.blend(background, overlay, 0.3)
    background.paste(new_image, offset)

    timename = time.strftime("%Y%m%d-%H%M%S")
    #filename = timename+".png"
    filename = timename
    #new_img.save(filename,"PNG")
    #background.save("STUFF/experiment/TEMP-img4a.png","PNG")
    background.save("/home/jack/Desktop/deep-dream-generator/notebooks/ManRay_temp/experiment9.png","PNG")
    time.sleep(1.5)    #
count=count+1

# 4- GooD -EXPERIMENT
import PIL
from PIL import Image
from PIL import Image
import random, os
from PIL import Image
import time
path = r"bugs/nouveau/"
import random, os
random_filename = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])

img1 = path+"/"+random_filename
im1=Image.open(img1)

basewidth = 1040
img = Image.open(img1)
wpercent = (basewidth / float(img.size[0]))
#hsize = int((float(img.size[1]) * float(wpercent)))
hsize = basewidth
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
half_the_width = img.size[0] / 2
half_the_height = img.size[1] / 2
img4 = img.crop(
    (
        half_the_width - 520,
        half_the_height - 520,
        half_the_width + 520,
        half_the_height + 520
    )
)
img4.save("TEMP-img4.png")



path2 = r"bugs/advertisements/"
random_filename2 = random.choice([
    y for y in os.listdir(path2)
    if os.path.isfile(os.path.join(path2, y))
])

img1a = path2+"/"+random_filename2
im1a=Image.open(img1a)
basewidth = 1040
imga = Image.open(img1a)
wpercent = (basewidth / float(imga.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
imga = imga.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
#half_the_width = imga.size[0] / 2
#half_the_height = imga.size[1] / 2
from random import randint
x1=(randint(22, 520))
x2=(randint(22, 520))
x3=(randint(x1+50, 1039))
x4=(randint(x2+50, 1039))

img4a = imga.crop(
    (
        x1,
        x2,
        x3,
        x4,
    )
)
img4a.save("TEMP-img4a.png")
img1 = "TEMP-img4.png"
img2 = "TEMP-img4a.png"

from PIL import Image
#im1=Image.open(img1)
#im1.size # (width,height) tuple
#im2=Image.open(img2)
#im2.size # (width,height) tuple
background = Image.open(img1)
overlay = Image.open(img2)

#background = Image.open(img2)
background = background.convert("RGBA")
#overlay = Image.open(img2)
#overlay = overlay.convert("RGBA")
overlay = overlay.convert("RGBA")

bg_w, bg_h = background.size
ctr1=random.randint(1, 800)
ctr2=random.randint(1, 800)






offset = (ctr1, ctr2)


#image=Image.open("star_blue.png")
Alpha=(randint(1, 9))*0.1
bands=list(overlay.split())
if len(bands)==4:
    bands[3]=bands[3].point(lambda x:x*Alpha)
    new_image=Image.merge(overlay.mode,bands)








#offset = ((bg_w - ctr1), (bg_h - ctr2))






#new_img = Image.blend(background, overlay, 0.3)
background.paste(new_image, offset)

timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")
#background.save("STUFF/experiment/TEMP-img4a.png","PNG")
background.save("STUFF/savers/"+filename+".png","PNG")

# emboss -EXPERIMENT
import PIL

from PIL import Image, ImageFilter
import random, os
from PIL import Image
import time
path = r"bugs/Bosch-Earthly Delights/"
random_filename = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])

img1 = path+"/"+random_filename
im1=Image.open(img1)
basewidth = 1024
img = Image.open(img1)
wpercent = (basewidth / float(img.size[0]))
hsize = basewidth
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
half_the_width = img.size[0] / 2
half_the_height = img.size[1] / 2
img4 = img.crop(
    (
        half_the_width - 520,
        half_the_height - 520,
        half_the_width + 520,
        half_the_height + 520
    )
)
img4.save("TEMP-img4.png")



path2 = r"STUFF/"
random_filename2 = random.choice([
    y for y in os.listdir(path2)
    if os.path.isfile(os.path.join(path2, y))
])

img1a = path2+"/"+random_filename2
im1a=Image.open(img1a)
basewidth = 1200
imga = Image.open(img1a)
wpercent = (basewidth / float(imga.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
imga = imga.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
half_the_width = imga.size[0] / 2
half_the_height = imga.size[1] / 2
from random import randint
x1=(randint(12, 356))
x2=(randint(12, 356))
x3=(randint(360, 600))
x4=(randint(360, 600))

img4a = imga.crop(
    (
        half_the_width - 520+x1,
        half_the_height - 520+x2,
        half_the_width + 520+x3,
        half_the_height + 520+x4
    )
)


#img4a.save("TEMP-img4a.png")
#image = Image.open('img4aS-001.png')
img4 = img4a.filter(ImageFilter.BLUR)
img4.save('TEMP-img4a.png') 





img1 = "TEMP-img4.png"
img2 = "TEMP-img4a.png"

from PIL import Image
#im1=Image.open(img1)
#im1.size # (width,height) tuple
#im2=Image.open(img2)
#im2.size # (width,height) tuple
background = Image.open(img1)
overlay = Image.open(img2)

#background = Image.open(img2)
background = background.convert("RGBA")
#overlay = Image.open(img2)
overlay = overlay.convert("RGBA")
bg_w, bg_h = background.size
ctr1=random.randint(1, 611)-100
ctr2=random.randint(1, 611)-100

#offset = ((bg_w - ctr1), (bg_h - ctr2))

offset = (ctr1, ctr2)

#new_img = Image.blend(background, overlay, 0.3)
background.paste(overlay, offset)

timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")

background.save("STUFF/"+filename+".png","PNG")

# 3 -GOOD RANDOM resize and crop
import PIL
from PIL import Image
from PIL import Image
import random, os
from PIL import Image
import time
path = r"bugs/manuscript/"
import random, os
random_filename = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])

img1 = path+"/"+random_filename
im1=Image.open(img1)
longer_side = max(im1.size)
basewidth = longer_side
img = Image.open(img1)
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
half_the_width = img.size[0] / 2
half_the_height = img.size[1] / 2
img4 = img.crop(
    (
        half_the_width - 320,
        half_the_height - 320,
        half_the_width + 320,
        half_the_height + 320
    )
)
img4.save("TEMP-img4.png")



path2 = r"bugs/nouveau/"
random_filename2 = random.choice([
    y for y in os.listdir(path2)
    if os.path.isfile(os.path.join(path2, y))
])

img1a = path2+"/"+random_filename2
im1a=Image.open(img1a)
basewidth = 1200
imga = Image.open(img1a)
wpercent = (basewidth / float(imga.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
imga = imga.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
half_the_width = imga.size[0] / 2
half_the_height = imga.size[1] / 2
img4a = imga.crop(
    (
        half_the_width - 320,
        half_the_height - 320,
        half_the_width + 320,
        half_the_height + 320
    )
)
img4a.save("TEMP-img4a.png")
img1 = "TEMP-img4.png"
img2 = "TEMP-img4a.png"

from PIL import Image
#im1=Image.open(img1)
#im1.size # (width,height) tuple
#im2=Image.open(img2)
#im2.size # (width,height) tuple
background = Image.open(img1)
overlay = Image.open(img2)

#background = Image.open(img2)
background = background.convert("RGBA")
#overlay = Image.open(img2)
overlay = overlay.convert("RGBA")
Alpha=(randint(1, 9))*0.1
new_img = Image.blend(background, overlay, Alpha)



timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")

new_img.save("STUFF/"+filename+".png","PNG")

# 5 - do not touch working fine
#from PIL import Image
#img = Image.open('800px-Tioman_Rainforest_.jpg', 'r')
import PIL.Image
import time
pathS = r"bugs/nouveau/"
import random, os
random_filenameS = random.choice([
    x for x in os.listdir(pathS)
    if os.path.isfile(os.path.join(pathS, x))
])
img1S = pathS+"/"+random_filenameS
#imgo=Image.open("newimage.png", "r")
imgo = Image.open(img1S, 'r')
img_w, img_h = imgo.size
#background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))

from PIL import Image

path2S = r"STUFF/"
random_filename2S = random.choice([
    yS for yS in os.listdir(path2S)
    if os.path.isfile(os.path.join(path2S, yS))
])

img1aS = path2S+"/"+random_filename2S
im1aS=Image.open(img1aS)
basewidthS = 1200
imgaS = Image.open(img1aS)
wpercent = (basewidthS / float(imgaS.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
imgaS = imgaS.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
half_the_width = imgaS.size[0] / 2
half_the_height = imgaS.size[1] / 2
from random import randint
x1=(randint(+120, +360))
x2=(randint(+120, +360))
x3=(randint(+120, +360))
x4=(randint(+120, +360))
img4aS = imgaS.crop(
    (
        half_the_width - x1,
        half_the_height - x2,
        half_the_width + x3,
        half_the_height + x4
    )
)
img4aS.save('img4aS-001.png')

#background = Image.open(img4aS)
background = Image.open("img4aS-001.png")
ctr1=(randint(1, img_w))
ctr2=(randint(1, img_h))
bg_w, bg_h = background.size
offset = ((bg_w - ctr1), (bg_h - ctr2))



#offset = ((bg_w - img_w) /2, (bg_h - img_h) / 2)
background.paste(imgo, offset)
#background.save('overlay001.png')
#do not touch working fine


timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")

#background.save("STUFF/"+filename+".png","PNG")
background.save("STUFF/new7/"+filename+".png","PNG")

# 6 - do not touch working fine
#from PIL import Image
#img = Image.open('800px-Tioman_Rainforest_.jpg', 'r')
import PIL.Image
import time
pathS = r"bugs/manuscript/"
import random, os
random_filenameS = random.choice([
    x for x in os.listdir(pathS)
    if os.path.isfile(os.path.join(pathS, x))
])
img1S = pathS+"/"+random_filenameS
#imgo=Image.open("newimage.png", "r")
imgo = Image.open(img1S, 'r')
img_w, img_h = imgo.size
#background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))

from PIL import Image

path2S = r"STUFF/"
random_filename2S = random.choice([
    yS for yS in os.listdir(path2S)
    if os.path.isfile(os.path.join(path2S, yS))
])

img1aS = path2S+"/"+random_filename2S
im1aS=Image.open(img1aS)
basewidthS = 1200
imgaS = Image.open(img1aS)
wpercent = (basewidthS / float(imgaS.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
imgaS = imgaS.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
half_the_width = imgaS.size[0] / 2
half_the_height = imgaS.size[1] / 2
from random import randint
x1=(randint(+120, +360))
x2=(randint(+120, +360))
x3=(randint(+120, +360))
x4=(randint(+120, +360))
img4aS = imgaS.crop(
    (
        half_the_width - x1,
        half_the_height - x2,
        half_the_width + x3,
        half_the_height + x4
    )
)
img4aS.save('img4aS-001.png')

#background = Image.open(img4aS)
background = Image.open("img4aS-001.png")
ctr1=(randint(1, img_w))
ctr2=(randint(1, img_h))
bg_w, bg_h = background.size
offset = ((bg_w - ctr1), (bg_h - ctr2))



#offset = ((bg_w - img_w) /2, (bg_h - img_h) / 2)
background.paste(imgo, offset)
#background.save('overlay001.png')
#do not touch working fine


timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")

#background.save("STUFF/"+filename+".png","PNG")
background.save("STUFF/new7/"+filename+".png","PNG")

# 7 do not touch working fine
#from PIL import Image
#img = Image.open('800px-Tioman_Rainforest_.jpg', 'r')
import PIL.Image
import time
pathS = r"bugs/manuscript/"
import random, os
random_filenameS = random.choice([
    x for x in os.listdir(pathS)
    if os.path.isfile(os.path.join(pathS, x))
])
img1S = pathS+"/"+random_filenameS
#imgo=Image.open("newimage.png", "r")
imgo = Image.open(img1S, 'r')
img_w, img_h = imgo.size
#background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))

from PIL import Image

path2S = r"STUFF/new/"
random_filename2S = random.choice([
    yS for yS in os.listdir(path2S)
    if os.path.isfile(os.path.join(path2S, yS))
])

img1aS = path2S+"/"+random_filename2S
im1aS=Image.open(img1aS)
basewidthS = 1200
imgaS = Image.open(img1aS)
wpercent = (basewidthS / float(imgaS.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
imgaS = imgaS.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
half_the_width = imgaS.size[0] / 2
half_the_height = imgaS.size[1] / 2
from random import randint
x1=(randint(+120, +360))
x2=(randint(+120, +360))
x3=(randint(+120, +360))
x4=(randint(+120, +360))
img4aS = imgaS.crop(
    (
        half_the_width - x1,
        half_the_height - x2,
        half_the_width + x3,
        half_the_height + x4
    )
)
img4aS.save('img4aS-001.png')

#background = Image.open(img4aS)
background = Image.open("img4aS-001.png")
ctr1=(randint(1, img_w))
ctr2=(randint(1, img_h))
bg_w, bg_h = background.size
offset = ((bg_w - ctr1), (bg_h - ctr2))



#offset = ((bg_w - img_w) /2, (bg_h - img_h) / 2)
background.paste(imgo, offset)
#background.save('overlay001.png')
#do not touch working fine


timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")

#background.save("STUFF/"+filename+".png","PNG")
background.save("STUFF/new7/"+filename+".png","PNG")

# 8 do not touch working fine
#from PIL import Image
#img = Image.open('800px-Tioman_Rainforest_.jpg', 'r')
import PIL.Image
import time
pathS = r"bugs/bookdecade1880/"
import random, os
random_filenameS = random.choice([
    x for x in os.listdir(pathS)
    if os.path.isfile(os.path.join(pathS, x))
])
img1S = pathS+"/"+random_filenameS
#imgo=Image.open("newimage.png", "r")
imgo = Image.open(img1S, 'r')
img_w, img_h = imgo.size
#background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))

from PIL import Image

path2S = r"bugs/fairytales"
random_filename2S = random.choice([
    yS for yS in os.listdir(path2S)
    if os.path.isfile(os.path.join(path2S, yS))
])

img1aS = path2S+"/"+random_filename2S
im1aS=Image.open(img1aS)
basewidthS = 1200
imgaS = Image.open(img1aS)
wpercent = (basewidthS / float(imgaS.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
imgaS = imgaS.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
half_the_width = imgaS.size[0] / 2
half_the_height = imgaS.size[1] / 2
from random import randint
x1=(randint(+120, +360))
x2=(randint(+120, +360))
x3=(randint(+120, +360))
x4=(randint(+120, +360))
img4aS = imgaS.crop(
    (
        half_the_width - x1,
        half_the_height - x2,
        half_the_width + x3,
        half_the_height + x4
    )
)

#half_the_width - 320,
#half_the_height - 320,
#half_the_width + 320,
#half_the_height + 320




img4aS.save('img4aS-001.png')

#background = Image.open(img4aS)
background = Image.open("img4aS-001.png")
ctr1=(randint(1, img_w))
ctr2=(randint(1, img_h))
bg_w, bg_h = background.size
offset = ((bg_w - ctr1), (bg_h - ctr2))



#offset = ((bg_w - img_w) /2, (bg_h - img_h) / 2)
background.paste(imgo, offset)
#background.save('overlay001.png')
#do not touch working fine


timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")

#background.save("STUFF/"+filename+".png","PNG")
background.save("STUFF/new7/"+filename+".png","PNG")

# 9 do not touch working fine

#work on this 


#from PIL import Image
#img = Image.open('800px-Tioman_Rainforest_.jpg', 'r')
import PIL.Image
import time
pathS = r"bugs/bookdecade1880/"
import random, os
random_filenameS = random.choice([
    x for x in os.listdir(pathS)
    if os.path.isfile(os.path.join(pathS, x))
])
img1S = pathS+"/"+random_filenameS
#imgo=Image.open("newimage.png", "r")
imgo = Image.open(img1S, 'r')
img_w, img_h = imgo.size
#background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))

from PIL import Image

path2S = r"bugs/bookdecade1880"
random_filename2S = random.choice([
    yS for yS in os.listdir(path2S)
    if os.path.isfile(os.path.join(path2S, yS))
])

img1aS = path2S+"/"+random_filename2S
im1aS=Image.open(img1aS)
basewidthS = 1200
imgaS = Image.open(img1aS)
wpercent = (basewidthS / float(imgaS.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
imgaS = imgaS.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
half_the_width = imgaS.size[0] / 2
half_the_height = imgaS.size[1] / 2
from random import randint
x1=(randint(+120, +360))
x2=(randint(+120, +360))
x3=(randint(+120, +360))
x4=(randint(+120, +360))
img4aS = imgaS.crop(
    (
        half_the_width - x1,
        half_the_height - x2,
        half_the_width + x3,
        half_the_height + x4
    )
)

#half_the_width - 320,
#half_the_height - 320,
#half_the_width + 320,
#half_the_height + 320




img4aS.save('img4aS-001.png')

#background = Image.open(img4aS)
background = Image.open("img4aS-001.png")
ctr1=(randint(1, img_w))
ctr2=(randint(1, img_h))
bg_w, bg_h = background.size
offset = ((bg_w - ctr1), (bg_h - ctr2))



#offset = ((bg_w - img_w) /2, (bg_h - img_h) / 2)
background.paste(imgo, offset)
#background.save('overlay001.png')
#do not touch working fine


timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")

#background.save("STUFF/"+filename+".png","PNG")
background.save("STUFF/"+filename+".png","PNG")

#do not touch working fine
#from PIL import Image
#img = Image.open('800px-Tioman_Rainforest_.jpg', 'r')
import PIL.Image
import time
pathS = r"STUFF/"
import random, os
random_filenameS = random.choice([
    x for x in os.listdir(pathS)
    if os.path.isfile(os.path.join(pathS, x))
])
img1S = pathS+"/"+random_filenameS
#imgo=Image.open("newimage.png", "r")
imgo = Image.open(img1S, 'r')
img_w, img_h = imgo.size
#background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))

from PIL import Image

path2S = r"bugs/butterflies/"
random_filename2S = random.choice([
    yS for yS in os.listdir(path2S)
    if os.path.isfile(os.path.join(path2S, yS))
])

img1aS = path2S+"/"+random_filename2S
im1aS=Image.open(img1aS)
basewidthS = 1024
imgaS = Image.open(img1aS)
wpercent = (basewidthS / float(imgaS.size[0]))
#hsize = int((float(img.size[1]) * float(wpercent)))
hsize = basewidth
imgaS = imgaS.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
half_the_width = imgaS.size[0] / 2
half_the_height = imgaS.size[1] / 2
from random import randint
x1=(randint(+120, +360))
x2=(randint(+120, +360))
x3=(randint(+120, +360))
x4=(randint(+120, +360))
img4aS = imgaS.crop(
    (
        half_the_width - x1,
        half_the_height - x2,
        half_the_width + x3,
        half_the_height + x4
    )
)

#half_the_width - 320,
#half_the_height - 320,
#half_the_width + 320,
#half_the_height + 320




img4aS.save('img4aS-001.png')

#background = Image.open(img4aS)
background = Image.open("img4aS-001.png")
ctr1=(randint(1, img_w))
ctr2=(randint(1, img_h))
bg_w, bg_h = background.size
offset = ((bg_w - ctr1), (bg_h - ctr2))




#offset = ((bg_w - img_w) /2, (bg_h - img_h) / 2)
background.paste(imgo, offset)
#background.save('overlay001.png')
#do not touch working fine


timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")

#background.save("STUFF/"+filename+".png","PNG")
background.save("STUFF/new7/"+filename+".png","PNG")

# GOOD WORKING TURNS IMAGE SEPIA

from PIL import Image, ImageOps
def make_linear_ramp(white):
    # putpalette expects [r,g,b,r,g,b,...]
    ramp = []
    r, g, b = white
    for i in range(255):
        ramp.extend((r*i/255, g*i/255, b*i/255))
    return ramp
# make sepia ramp (tweak color as necessary)
sepia = make_linear_ramp((255, 240, 192))
pathS = r"bugs/deco/"
import random, os
random_filenameS = random.choice([
    x for x in os.listdir(pathS)
    if os.path.isfile(os.path.join(pathS, x))
])
img1S = pathS+"/"+random_filenameS
#imgo=Image.open("newimage.png", "r")
im = Image.open(img1S, 'r')
img_w, img_h = imgo.size
#background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))

# convert to grayscale
if im.mode != "L":
    im = im.convert("L")

# optional: apply contrast enhancement here, e.g.
im = ImageOps.autocontrast(im)

# apply sepia palette
im.putpalette(sepia)

# convert back to RGB so we can save it as JPEG
# (alternatively, save it in PNG or similar)
#im = im.convert("RGB")

#im.save("file.jpg")
timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")

#background.save("STUFF/"+filename+".png","PNG")
im.save("STUFF/sepia"+filename+".png","PNG")

from PIL import Image, ImageFilter
import random, os
path2S = r"STUFF"
random_filename2S = random.choice([
    yS for yS in os.listdir(path2S)
    if os.path.isfile(os.path.join(path2S, yS))
])
img1aS = path2S+"/"+random_filename2S
image=Image.open(img1aS)
#image = Image.open('img4aS-001.png')
image = image.filter(ImageFilter.CONTOUR)
#image.save('filters/CONTOUR.png') 
#im.save("file.jpg")
timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")
#background.save("STUFF/"+filename+".png","PNG")
image.save("STUFF/contour"+filename+".png","PNG")

from PIL import Image, ImageFilter
import random, os
path2S = r"bugs/fairytales/"
random_filename2S = random.choice([
    yS for yS in os.listdir(path2S)
    if os.path.isfile(os.path.join(path2S, yS))
])
img1aS = path2S+"/"+random_filename2S
image=Image.open(img1aS)
#image = Image.open('img4aS-001.png')
image = image.filter(ImageFilter.EDGE_ENHANCE)
#image.save('filters/CONTOUR.png') 
#im.save("file.jpg")
timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")
#background.save("STUFF/"+filename+".png","PNG")
image.save("STUFF/EDGE_ENHANCE"+filename+".png","PNG")

from PIL import Image, ImageFilter
import random, os
path2S = r"STUFF"
random_filename2S = random.choice([
    yS for yS in os.listdir(path2S)
    if os.path.isfile(os.path.join(path2S, yS))
])

img1aS = path2S+"/"+random_filename2S
image=Image.open(img1aS)
#image = Image.open('img4aS-001.png')
image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
#image.save('filters/CONTOUR.png') 
#im.save("file.jpg")
timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")
#background.save("STUFF/"+filename+".png","PNG")
saveas = "STUFF/EDGE_ENHANCE_MORE"+filename+".png
image.save(saveas,"PNG")
print saveas

from PIL import Image, ImageFilter
import random, os
path2S = r"STUFF"
random_filename2S = random.choice([
    yS for yS in os.listdir(path2S)
    if os.path.isfile(os.path.join(path2S, yS))
])

img1aS = path2S+"/"+random_filename2S
image=Image.open(img1aS)
#image = Image.open('img4aS-001.png')
image = image.filter(ImageFilter.DETAIL)
#image.save('filters/CONTOUR.png') 
#im.save("file.jpg")
timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")
#background.save("STUFF/"+filename+".png","PNG")
image.save("STUFF/DETAIL"+filename+".png","PNG")

from PIL import Image, ImageFilter
import random, os
path2S = r"STUFF"
random_filename2S = random.choice([
    yS for yS in os.listdir(path2S)
    if os.path.isfile(os.path.join(path2S, yS))
])

img1aS = path2S+"/"+random_filename2S
image=Image.open(img1aS)
#image = Image.open('img4aS-001.png')
image = image.filter(ImageFilter.FIND_EDGES)
#image.save('filters/CONTOUR.png') 
#im.save("file.jpg")
timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")
#background.save("STUFF/"+filename+".png","PNG")
image.save("STUFF/FIND_EDGES"+filename+".png","PNG")

from PIL import Image, ImageFilter
import random, os
path2S = r"STUFF"
random_filename2S = random.choice([
    yS for yS in os.listdir(path2S)
    if os.path.isfile(os.path.join(path2S, yS))
])

img1aS = path2S+"/"+random_filename2S
image=Image.open(img1aS)
#image = Image.open('img4aS-001.png')
image = image.filter(ImageFilter.EMBOSS)
#image.save('filters/CONTOUR.png') 
#im.save("file.jpg")
timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")
#background.save("STUFF/"+filename+".png","PNG")
image.save("STUFF/EMBOSS"+filename+".png","PNG")

from PIL import Image, ImageFilter
import random, os
path2S = r"STUFF"
random_filename2S = random.choice([
    yS for yS in os.listdir(path2S)
    if os.path.isfile(os.path.join(path2S, yS))
])

img1aS = path2S+"/"+random_filename2S
image=Image.open(img1aS)
#image = Image.open('img4aS-001.png')
image = image.filter(ImageFilter.SHARPEN)
#image.save('filters/CONTOUR.png') 
#im.save("file.jpg")
timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")
#background.save("STUFF/"+filename+".png","PNG")
image.save("STUFF/SHARPEN"+filename+".png","PNG")

from PIL import Image, ImageFilter
import random, os
path2S = r"bugs/spiders/"
random_filename2S = random.choice([
    yS for yS in os.listdir(path2S)
    if os.path.isfile(os.path.join(path2S, yS))
])

img1aS = path2S+"/"+random_filename2S
image=Image.open(img1aS)
#image = Image.open('img4aS-001.png')
image = image.filter(ImageFilter.SMOOTH)
#image.save('filters/CONTOUR.png') 
#im.save("file.jpg")
timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")
#background.save("STUFF/"+filename+".png","PNG")
image.save("STUFF/SMOOTH"+filename+".png","PNG")

import time
import random, os
from PIL import Image, ImageFilter
path2S = r"STUFF"
random_filename2S = random.choice([
    yS for yS in os.listdir(path2S)
    if os.path.isfile(os.path.join(path2S, yS))
])

img1aS = path2S+"/"+random_filename2S
image=Image.open(img1aS)
#image = Image.open('img4aS-001.png')
image = image.filter(ImageFilter.SMOOTH_MORE)
#image.save('filters/CONTOUR.png') 
#im.save("file.jpg")
timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")
#background.save("STUFF/"+filename+".png","PNG")
image.save("STUFF/SMOOTH_MORE"+filename+".png","PNG")

import sys
sys.path.insert(0, "/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import cv2
import time
import numpy as np
from matplotlib import pyplot as plt
import random, os
from PIL import Image, ImageFilter
path2S = r"STUFF"
random_filename2S = random.choice([
    yS for yS in os.listdir(path2S)
    if os.path.isfile(os.path.join(path2S, yS))
])
img1aS = path2S+"/"+random_filename2S
#image=Image.open(img1aS)
img = cv2.imread(img1aS,0)
edges = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")
saveas = "STUFF/"+filename+'-Canny.png'
plt.savefig(saveas, bbox_inches='tight')
print saveas

!showme STUFF/20180509-132245Canny.png

import numpy as np
from scipy.misc import imread, imsave
import pylab as plt

from PIL import Image, ImageFilter
path2S = r"bugs/fairytales/"
random_filename2S = random.choice([
    yS for yS in os.listdir(path2S)
    if os.path.isfile(os.path.join(path2S, yS))
])

img1aS = path2S+"/"+random_filename2S
#image=Image.open(img1aS)

image_data = imread(img1aS).astype(np.float32)

#image_data = imread('img4aS-001.png').astype(np.float32)
scaled_image_data = image_data / 255.

print 'Size: ', image_data.size
print 'Shape: ', image_data.shape
  
image_slice_red =  scaled_image_data[:,:,0]
image_slice_green =  scaled_image_data[:,:,1]
image_slice_blue =  scaled_image_data[:,:,2]

#print 'Size: ', image_slice_0.size
#print 'Shape: ', image_slice_0.shape

plt.subplot(221)
plt.imshow(image_slice_red, cmap=plt.cm.Reds_r)

plt.subplot(222)
plt.imshow(image_slice_green, cmap=plt.cm.Greens_r)

plt.subplot(223)
plt.imshow(image_slice_blue, cmap=plt.cm.Blues_r)  

plt.subplot(224)
plt.imshow(scaled_image_data)  

#plt.show()
timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")


plt.savefig("STUFF/"+filename+'FOUR.png', bbox_inches='tight')

import numpy as np
from matplotlib import pyplot as plt
from random import randint
%matplotlib inline

w=(randint(50, 640))
h=(randint(50, 640))



random_image = np.random.random([w, h])

plt.imshow(random_image, cmap='gray', interpolation='nearest');
#plt.show()
timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")


plt.savefig("STUFF/"+filename+'noise.png', bbox_inches='tight')

# import the necessary packages
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image, ImageFilter
%matplotlib inline

#import numpy as np
#from matplotlib import pyplot as plt

img = cv2.imread('img4aS-001.png',0)

import matplotlib.pyplot as plt
img = cv2.imread("img4aS-001.png")
plt.imshow(img)

from PIL import Image
from resizeimage import resizeimage
import time
fd_img = open('img4aS-001.png', 'r')
img = Image.open(fd_img)
img = resizeimage.resize_cover(img, [512, 512])

timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")
img.save('STUFF/'+filename+'image-cover.png', img.format)
fd_img.close()

# GOOD RANDOM resize and crop
import PIL
from PIL import Image
import time
import random, os
from PIL import Image
path = r"bugs/advertisements-1/"
import random, os
random_filename = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])

img1 = path+"/"+random_filename
im1=Image.open(img1)
basewidth = 1200
img = Image.open(img1)
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
half_the_width = img.size[0] / 2
half_the_height = img.size[1] / 2
img4 = img.crop(
    (
        half_the_width - 320,
        half_the_height - 320,
        half_the_width + 320,
        half_the_height + 320
    )
)
img4.save("aaaa_resized.jpg")



path2 = r"bugs/manuscript/"
random_filename2 = random.choice([
    y for y in os.listdir(path2)
    if os.path.isfile(os.path.join(path2, y))
])

img1a = path2+"/"+random_filename2
im1a=Image.open(img1a)
basewidth = 1200
imga = Image.open(img1a)
wpercent = (basewidth / float(imga.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
imga = imga.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
half_the_width = imga.size[0] / 2
half_the_height = imga.size[1] / 2
img4a = imga.crop(
    (
        half_the_width - 320,
        half_the_height - 320,
        half_the_width + 320,
        half_the_height + 320
    )
)
img4a.save("bbbb_resized.jpg")
img1 = "aaaa_resized.jpg"
img2 = "bbbb_resized.jpg"

from PIL import Image
#im1=Image.open(img1)
#im1.size # (width,height) tuple
#im2=Image.open(img2)
#im2.size # (width,height) tuple
background = Image.open(img1)
overlay = Image.open(img2)

#background = Image.open(img2)
background = background.convert("RGBA")
#overlay = Image.open(img2)
overlay = overlay.convert("RGBA")

new_img = Image.blend(background, overlay, 0.3)
#new_img.save("AA-BB-out.png","PNG")

timename = time.strftime("%Y%m%d-%H%M%S")
#filename = timename+".png"
filename = timename
#new_img.save(filename,"PNG")
new_img.save('STUFF/blend'+filename+'image-cover.png', img.format)

# encoding: utf-8
import operator
from PIL import Image
from PIL import ImageDraw
import time
import os, random

path = r"bugs/advertisements-1/"
random_filename = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])

img1 = path+"/"+random_filename
im1=Image.open(img1)

folder2=r"bugs/manuscript/"
b=random.choice(os.listdir(folder2))
img2 = folder2+b
base = Image.open(img1)
baseO = base.resize((512, 512))
overlay = Image.open(img2)
overlayO = overlay.resize((512, 512))
#blend with alpha=0.5
result = Image.blend(baseO, overlayO, alpha=0.4)
timename = time.strftime("%Y%m%d-%H%M%S")
filename = timename+".jpg"
result.save("STUFF/"+filename)
print filename

from PIL import Image
basewidth = 140
import time
import os, random
folder=r"bugs/fairytales/"
a=random.choice(os.listdir(folder))
img1 = folder+a

img = Image.open(img1)
#wpercent = (basewidth / float(img.size[0]))
#hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, basewidth), PIL.Image.ANTIALIAS)
#img.save('STUFF/140.jpg') 


timename = time.strftime("%Y%m%d-%H%M%S")
filename = timename+".jpg"
img.save("STUFF/140"+filename)
print filename

# encoding: utf-8
import operator
from PIL import Image
from PIL import ImageDraw
import time
import os, random

folder=r"bugs/advertisements-1/"
a=random.choice(os.listdir(folder))
img1 = folder+a
#os.open(folder+"/"+a, os.O_RDWR)
folder2=r"bugs/manuscript/"
b=random.choice(os.listdir(folder2))
img2 = folder+a

background = Image.open(img1)
overlay = Image.open(img2)

background = Image.open(img1)
background = background.convert("RGBA")
overlay = Image.open(img2)
overlay = overlay.convert("RGBA")
new_img = Image.blend(background, overlay, 0.5)
timename = time.strftime("%Y%m%d-%H%M%S")
filename = timename+".png"

new_img.save(filename,"PNG")
print filename

print filename
# GOOD BLOCK
from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image

%matplotlib inline
pil_im = Image.open(filename, 'r')
imshow(pil_im)

run collagemaker.py -w 8000 -i 800 -s

run collagemaker.py -w 6000 -i 1000 -s

run collagemaker.py -w 8000 -i 2000 -s

!mkdir collage

%%writefile collagemaker.py
# -*- coding: utf-8 -*-
"""
Collage maker - tool to create picture collages
Author: Delimitry
"""
import time
import argparse
import os
import random
from PIL import Image


def make_collage(images, filename, width, init_height):
    """
    Make a collage image with a width equal to `width` from `images` and save to `filename`.
    """
    if not images:
        print('No images for collage found!')
        return False

    margin_size = 2
    # run until a suitable arrangement of images is found
    while True:
        # copy images to images_list
        images_list = images[:]
        coefs_lines = []
        images_line = []
        x = 0
        while images_list:
            # get first image and resize to `init_height`
            img_path = images_list.pop(0)
            img = Image.open(img_path)
            img.thumbnail((width, init_height))
            # when `x` will go beyond the `width`, start the next line
            if x > width:
                coefs_lines.append((float(x) / width, images_line))
                images_line = []
                x = 0
            x += img.size[0] + margin_size
            images_line.append(img_path)
        # finally add the last line with images
        coefs_lines.append((float(x) / width, images_line))

        # compact the lines, by reducing the `init_height`, if any with one or less images
        if len(coefs_lines) <= 1:
            break
        if any(map(lambda c: len(c[1]) <= 1, coefs_lines)):
            # reduce `init_height`
            init_height -= 10
        else:
            break

    # get output height
    out_height = 0
    for coef, imgs_line in coefs_lines:
        if imgs_line:
            out_height += int(init_height / coef) + margin_size
    if not out_height:
        print('Height of collage could not be 0!')
        return False

    collage_image = Image.new('RGB', (width, int(out_height)), (35, 35, 35))
    # put images to the collage
    y = 0
    for coef, imgs_line in coefs_lines:
        if imgs_line:
            x = 0
            for img_path in imgs_line:
                img = Image.open(img_path)
                # if need to enlarge an image - use `resize`, otherwise use `thumbnail`, it's faster
                k = (init_height / coef) / img.size[1]
                if k > 1:
                    img = img.resize((int(img.size[0] * k), int(img.size[1] * k)), Image.ANTIALIAS)
                else:
                    img.thumbnail((int(width / coef), int(init_height / coef)), Image.ANTIALIAS)
                if collage_image:
                    collage_image.paste(img, (int(x), int(y)))
                x += img.size[0] + margin_size
            y += int(init_height / coef) + margin_size
    collage_image = collage_image.resize((1000,1000), Image.ANTIALIAS)        
    collage_image.save(filename)
    return True


def main():
    timename = time.strftime("%Y%m%d-%H%M%S")
    filename = "collage/collage"+timename+".png"
    #filename = timename
    #new_img.save(filename,"PNG")
    # prepare argument parser
    parse = argparse.ArgumentParser(description='Photo collage maker')
    parse.add_argument('-f', '--folder', dest='folder', help='folder with images (*.jpg, *.jpeg, *.png)',\
                       default='randomsized/')
    parse.add_argument('-o', '--output', dest='output', help='output collage image filename',\
                       default=filename)
    parse.add_argument('-w', '--width', dest='width', type=int, help='resulting collage image width')
    parse.add_argument('-i', '--init_height', dest='init_height', type=int, \
                       help='initial height for resize the images')
    parse.add_argument('-s', '--shuffle', action='store_true', dest='shuffle', help='enable images shuffle')

    args = parse.parse_args()
    if not args.width or not args.init_height:
        parse.print_help()
        exit(1)

    # get images
    files = [os.path.join(args.folder, fn) for fn in os.listdir(args.folder)]
    images = [fn for fn in files if os.path.splitext(fn)[1].lower() in ('.jpg', '.jpeg', '.png')]
    if not images:
        print('No images for making collage! Please select other directory with images!')
        exit(1)

    # shuffle images if needed
    if args.shuffle:
        random.shuffle(images)

    print('Making collage...')
    res = make_collage(images, args.output, args.width, args.init_height)
    if not res:
        print('Failed to create collage!')
        exit(1)
    print('Collage is ready!')


if __name__ == '__main__':
    main()

from PIL import Image
import os
from random import randint
import time
from datetime import datetime

dirZ = os.walk('.').next()[1]
for dirs in dirZ:
    files = [os.path.join(dirs, fn) for fn in os.listdir(dirs)]
    images = [fn for fn in files if os.path.splitext(fn)[1].lower() in ('.jpg', '.jpeg', '.png')]
    for imag in images:
        w = randint(120,200)
        var = randint(5,30)
        h = w+var
        try:
            IM = Image.open(imag)
            IM = IM.resize((w,h), Image.BICUBIC)
            filename = datetime.now().strftime("randomsized/%H:%M:%S.%f.png")
            time.sleep(.1)
            IM.save(filename)
            print filename
        except:
            pass
        
        

%%writefile collagemaker.py
# -*- coding: utf-8 -*-
"""
Collage maker - tool to create picture collages
Author: Delimitry
"""
import time
import argparse
import os
import random
from PIL import Image


def make_collage(images, filename, width, init_height):
    """
    Make a collage image with a width equal to `width` from `images` and save to `filename`.
    """
    if not images:
        print('No images for collage found!')
        return False

    margin_size = 2
    # run until a suitable arrangement of images is found
    while True:
        # copy images to images_list
        images_list = images[:]
        coefs_lines = []
        images_line = []
        x = 0
        while images_list:
            # get first image and resize to `init_height`
            img_path = images_list.pop(0)
            img = Image.open(img_path)
            img.thumbnail((width, init_height))
            # when `x` will go beyond the `width`, start the next line
            if x > width:
                coefs_lines.append((float(x) / width, images_line))
                images_line = []
                x = 0
            x += img.size[0] + margin_size
            images_line.append(img_path)
        # finally add the last line with images
        coefs_lines.append((float(x) / width, images_line))

        # compact the lines, by reducing the `init_height`, if any with one or less images
        if len(coefs_lines) <= 1:
            break
        if any(map(lambda c: len(c[1]) <= 1, coefs_lines)):
            # reduce `init_height`
            init_height -= 10
        else:
            break

    # get output height
    out_height = 0
    for coef, imgs_line in coefs_lines:
        if imgs_line:
            out_height += int(init_height / coef) + margin_size
    if not out_height:
        print('Height of collage could not be 0!')
        return False

    collage_image = Image.new('RGB', (width, int(out_height)), (35, 35, 35))
    # put images to the collage
    y = 0
    for coef, imgs_line in coefs_lines:
        if imgs_line:
            x = 0
            for img_path in imgs_line:
                img = Image.open(img_path)
                # if need to enlarge an image - use `resize`, otherwise use `thumbnail`, it's faster
                k = (init_height / coef) / img.size[1]
                if k > 1:
                    img = img.resize((int(img.size[0] * k), int(img.size[1] * k)), Image.ANTIALIAS)
                else:
                    img.thumbnail((int(width / coef), int(init_height / coef)), Image.ANTIALIAS)
                if collage_image:
                    collage_image.paste(img, (int(x), int(y)))
                x += img.size[0] + margin_size
            y += int(init_height / coef) + margin_size
    collage_image.save(filename)
    return True


def main():
    timename = time.strftime("%Y%m%d-%H%M%S")
    filename = "collage/collage"+timename+".png"
    #filename = timename
    #new_img.save(filename,"PNG")
    # prepare argument parser
    parse = argparse.ArgumentParser(description='Photo collage maker')
    parse.add_argument('-f', '--folder', dest='folder', help='folder with images (*.jpg, *.jpeg, *.png)',\
                       default='ManRay/')
    parse.add_argument('-o', '--output', dest='output', help='output collage image filename',\
                       default=filename)
    parse.add_argument('-w', '--width', dest='width', type=int, help='resulting collage image width')
    parse.add_argument('-i', '--init_height', dest='init_height', type=int, \
                       help='initial height for resize the images')
    parse.add_argument('-s', '--shuffle', action='store_true', dest='shuffle', help='enable images shuffle')

    args = parse.parse_args()
    if not args.width or not args.init_height:
        parse.print_help()
        exit(1)

    # get images
    files = [os.path.join(args.folder, fn) for fn in os.listdir(args.folder)]
    images = [fn for fn in files if os.path.splitext(fn)[1].lower() in ('.jpg', '.jpeg', '.png')]
    if not images:
        print('No images for making collage! Please select other directory with images!')
        exit(1)

    # shuffle images if needed
    if args.shuffle:
        random.shuffle(images)

    print('Making collage...')
    res = make_collage(images, args.output, args.width, args.init_height)
    if not res:
        print('Failed to create collage!')
        exit(1)
    print('Collage is ready!')


if __name__ == '__main__':
    main()



# watermark.py

from PIL import Image, ImageDraw

def main(image, output):
    # Open the original image
    im = Image.open(image)
    print im.size
    # Create a new image for the watermark with an alpha layer (RGBA)
    #  the same size as the original image
    watermark = Image.new("RGBA", im.size)
    print watermark.size
    # Get an ImageDraw object so we can draw on the image
    waterdraw = ImageDraw.ImageDraw(watermark, "RGBA")
    # Place the text at (10, 10) in the upper left corner. Text will be white.
    waterdraw.text((10, 10), "The Image Project")

    # Get the watermark image as grayscale and fade the image
    # See <http://www.pythonware.com/library/pil/handbook/image.htm#Image.point>
    #  for information on the point() function
    # Note that the second parameter we give to the min function determines
    #  how faded the image will be. That number is in the range [0, 256],
    #  where 0 is black and 256 is white. A good value for fading our white
    #  text is in the range [100, 200].
    watermask = watermark.convert("L").point(lambda x: min(x, 100))
    # Apply this mask to the watermark image, using the alpha filter to 
    #  make it transparent
    watermark = watermark.putalpha(watermask)

    # Paste the watermark (with alpha layer) onto the original image and save it
    new_img = Image.blend(im, watermark, 0.5)
    
    
    new_img.save(output)
    return new_img



# Watermarks

from PIL import ImageDraw, Image, ImageFont
def watermark(img, Watermark):
    base = Image.open(img).convert('RGBA')
    w,h = base.size
    txt = Image.new('RGBA', base.size, (255,255,255,0))
    # get a font
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 140)
    # get a drawing context
    d = ImageDraw.Draw(txt)
    d.text((20,200), Watermark, font=fnt, fill=(200,200,200, 100))
    out = Image.alpha_composite(base, txt)
    rgb_img = out.convert('RGB')
    rgb_img.save("TEMP/JUNK.jpg")
    return rgb_img
    
img ="ManRay/20180909-090738.png"
Watermark = "NO COPY"    
watermark(img, Watermark)


import PIL
import time
from PIL import Image
import random, os
from random import randint
import random, os
# Randomly choose two images. The default directories are images/. Theimages may be two 
# different directories.
def blendoverlay(Opath="images/", Bpath="images/"):
    #path = r"bugs/advertisements/"

    random_filename1 = random.choice([
        x for x in os.listdir(Opath)
        if os.path.isfile(os.path.join(Opath, x))
    ])

    img1 = Opath+random_filename1
    return img1
    print(img1)

import sys
sys.path.insert(0,"/home/jack/script")
from Immanip import blendoverlay
from Immanip import datename
new_img = blendoverlay.blend_overlay("photos/","TEMP/")
new_img.save("ManRay/"+datename.date_name())
print "ManRay/"+datename.date_name()

from PIL import Image
im = Image.open("ManRay/20180909-090220.png")
im

import os
from random import randint
PATH = "/home/jack/Desktop/JupyterNotebook-Graphics/"
for dirnames, filenames in os.listdir(PATH):
    print dirnames

!mkdir randomsized

filename = time.strftime("randomsized/%Y%m%d-%H%M%S%F.png")
print filename

dirZ = os.walk('.').next()[1]
for dirs in dirZ:
    img = os.listdir(dir)
    for im in img:
        print "images/"+im

dirs = os.walk('.').next()[1]
for dir in dirs:
    print dir

import os
from random import randint
PATH = "/home/jack/Desktop/JupyterNotebook-Graphics/"
for dirpath, dirnames, filenames in os.walk(PATH):
    print dirnames
    for filename in [f for f in filenames if f.endswith(".t7")]:
        if len(filename)>20:
            AZ = filename[-9:-3]
            samp.append(AZ)


import os
from random import randint
img = os.listdir("images/")
for im in img:
    print "images/"+im
    




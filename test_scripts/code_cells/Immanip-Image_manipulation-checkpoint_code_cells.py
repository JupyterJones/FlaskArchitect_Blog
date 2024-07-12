import cv2

!rm Immanip/*.pyc

!ls Immanip

!mkdir output

import sys
sys.path.insert(0,"/home/jack/script")
from Immanip import blendoverlay
from Immanip import datename
new_img = blendoverlay.blend_overlay("photos/","TEMP/")
PATH = "ManRay/"
new_img.save(PATH+datename.date_name())
print PATH+datename.date_name()
new_img

# %load Immanip/blendoverlay.py
#!/usr/bin/python
import PIL
import time
from PIL import Image
import random, os
from random import randint
import random, os
# Randomly choose two images. The default directories are images/. The images may be two 
# different directories.
def blend_overlay(Opath="images/", Bpath="images/"):
    #path = r"bugs/advertisements/"

    random_filename1 = random.choice([
        x for x in os.listdir(Opath)
        if os.path.isfile(os.path.join(Opath, x))
    ])
  
    img1 = Opath+random_filename1
    im1 = Image.open(img1)
    longer_side = max(im1.size)
    basewidth = 800
    img = Image.open(img1)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    half_the_width = img.size[0] / 2
    half_the_height = img.size[1] / 2
    im = img.crop(
        (
            half_the_width - 320,
            half_the_height - 320,
            half_the_width + 320,
            half_the_height + 320
        )
    ) 
    
    im.save("output/"+"TEMP-img4.png") 
    #path2 = r"bugs/butterflies/"
    #path2 = r"bugs/advertisements1800/"
    random_filename2 = random.choice([
        y for y in os.listdir(Bpath)
        if os.path.isfile(os.path.join(Bpath, y))
    ])

    img1a = Bpath+"/"+random_filename2
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
    img4a.save("output/"+"TEMP-img4a.png")

    
    background = Image.open("output/"+"TEMP-img4.png").convert("RGBA")
    overlay = Image.open("output/"+"TEMP-img4a.png").convert("RGBA")
 
    background = background.resize((640, 640), PIL.Image.ANTIALIAS)
    overlay = overlay.resize((640, 640), PIL.Image.ANTIALIAS)


    Alpha=(randint(1, 9))*0.1
    new_img = Image.blend(background, overlay, 0.4)

    
    return new_img

blend_overlay(Opath="images/", Bpath="images/")

# %load Immanip/randsize.py
#!/usr/bin/python
import PIL
import time
from PIL import Image
import random, os
from random import randint
# rand_size(imp_path='STUFF/new/', minS=150, maxS=300, output="STUFF/Temp.jpg")
# Picks a ranom image in a directory, and distorts it  
# Default path images/ default minimum width random(250-400), height random(250-400) intentionally\
# distorting the aspect.
def rand_size(imp_path='images/', minS=250, maxS=500, output="output/Temp.jpg"):
    path3 = imp_path
    random_filename3 = random.choice([
        x for x in os.listdir(path3)
        if os.path.isfile(os.path.join(path3, x))
    ])
    sidea=(randint(minS, maxS))
    
    sideb=(randint(minS, maxS))
    img1 = path3+"/"+random_filename3
    im1=Image.open(img1)
    img = im1.resize((sidea,sideb), PIL.Image.ANTIALIAS)
    img.save(output)
    return img 
 

rand_size(imp_path='images', minS=250, maxS=500, output="output/Temp.png")

# %load Immanip/rmblack.py
#!/usr/bin/python
def rm_black(image_in ="output/Temp.png", image_out = "XCXCXC.png"):
    import cv2    
    src = cv2.imread(image_in, 1)
    tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
    b, g, r = cv2.split(src)
    rgba = [b,g,r, alpha]
    dst = cv2.merge(rgba,4)
    cv2.imwrite(image_out, dst)
    return dst

rm_black(image_in ="output/Temp.png", image_out = "XCXCXC.png")

from PIL import Image
image_out = "XCXCXC.png"
im = Image.open(image_out)
im

# %load Immanip/randim.py
#!/usr/bin/python
# randim(inpath = "images/") Finds random images in a directory 
#Default directory is: images/
import PIL
import time
from PIL import Image
import random, os
from random import randint
def rand_im(inpath = "photos/"):
    random_filename2 = random.choice([
        x for x in os.listdir(inpath)
        if os.path.isfile(os.path.join(inpath, x))
    ])

    #img1 = inpath+"/"+random_filename2
    img1 = inpath+random_filename2
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
    return img4
if __name__ == '__main__':
    rand_im()

rand_im().save("photos/photos.png")



# %load Immanip/c_rmblack.py
#!/usr/bin/python
# Works Great makes black transparent
import cv2

image_in = "photos/photos.png"
image_out = "TEMP/NB-T-20170621-152227.png"

src = cv2.imread(image_in, 1)
tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
b, g, r = cv2.split(src)
rgba = [b, g, r, alpha]
dst = cv2.merge(rgba, 4)
cv2.imwrite(image_out, dst)


image_out = "TEMP/NB-T-20170621-152227.png"
view = Image.open(image_out)
view




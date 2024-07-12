http://www.karinkuhlmann.com/fractals-2-digital-art/fractals-2-digital-art.html

#Very Good COMPOSITE ___ _ do not change
from PIL import Image, ImageChops
import time
import random
import os
count = 0
while count<235: 
    
    path = r"/home/jack/Desktop/deep-dream-generator/notebooks/context-free/output/"
    base_image = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
        ])
    filename0=(path+base_image)

    path0 = r"/home/jack/Desktop/deep-dream-generator/notebooks/context-free/output/"
    #path0 = r"testmasks/"
    base_image0 = random.choice([
        x0 for x0 in os.listdir(path0)
        if os.path.isfile(os.path.join(path0, x0))
        ])
    filename00=(path0+base_image0)

    path1 = r"newmask/"
    base_image1 = random.choice([
        x1 for x1 in os.listdir(path1)
        if os.path.isfile(os.path.join(path1, x1))
        ])
    mask0=(path1+base_image1)

    #im = Image.open('%s' % os.path.join(os.getcwd(), s + '.png')).convert("RGB")
      
    
    im1a = Image.open(filename0).convert("RGB")
    im1a.save("tmp/01aa.jpg")
    im1b = Image.open("tmp/01aa.jpg")
    im1c = im1b.resize((640,640), Image.NEAREST)
    im1c.save("tmp/01ab.jpg")
    jpg_im1 = Image.open("tmp/01ab.jpg") 

    im02a = Image.open(filename00).convert("RGB")
    im02 = im02a.resize((640,640), Image.NEAREST)
    im02.save("tmp/01aaa.jpg")
    im02b = Image.open("tmp/01aaa.jpg").convert("RGB")
    im02b.save("tmp/01aab.jpg")
    jpg_im2 = Image.open("tmp/01aab.jpg") 
    
    im03 = Image.open(mask0)
    im03.save("tmp/01aaaa.jpg")
    jpg_im3 = Image.open("tmp/01aaaa.jpg")
    mask = jpg_im3.resize((640,640), Image.NEAREST)
    time.sleep(3)
    result1 = ImageChops.blend(jpg_im1, jpg_im2, .5)
    
    #result1 = ImageChops.composite(jpg_im1, jpg_im2, mask)
    filename = time.strftime("/home/jack/Desktop/deep-dream-generator/notebooks/context-free/output/blended%Y%m%d%H%M%S.jpg")
    result1.save(filename)
    count=count+1
   

#Very Good COMPOSITE ___ _ do not change
from PIL import Image, ImageChops
import time
import random
import os
count = 0
while count<35: 
    
    path = r"/home/jack/Desktop/deep-dream-generator/notebooks/context-free/output/"
    base_image = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
        ])
    filename0=(path+base_image)

    path0 = r"/home/jack/Desktop/deep-dream-generator/notebooks/context-free/output/"
    #path0 = r"testmasks/"
    base_image0 = random.choice([
        x0 for x0 in os.listdir(path0)
        if os.path.isfile(os.path.join(path0, x0))
        ])
    filename00=(path0+base_image0)

    path1 = r"newmask/"
    base_image1 = random.choice([
        x1 for x1 in os.listdir(path1)
        if os.path.isfile(os.path.join(path1, x1))
        ])
    mask0=(path1+base_image1)

    #im = Image.open('%s' % os.path.join(os.getcwd(), s + '.png')).convert("RGB")
      
    
    im1a = Image.open(filename0).convert("RGB")
    im1a.save("tmp/01aa.jpg")
    im1 = Image.open("tmp/01aa.jpg").convert("RGB")
    imi = im1.resize((640,640), Image.NEAREST)
    im1.save("tmp/01aa2.jpg")
    jpg_im1 = Image.open("tmp/01aa2.jpg") 

    im02a = Image.open(filename00).convert("RGB")
    im02a.save("tmp/01aaa.jpg")
    im02 = Image.open("tmp/01aaa.jpg").convert("RGB")
    im02 = im02.resize((640,640), Image.NEAREST)
    im02.save("tmp/01aaa2.jpg")
    jpg_im2 = Image.open("tmp/01aaa2.jpg") 

    im03 = Image.open(mask0)
    im03.save("tmp/01aaaa.jpg")
    jpg_im3 = Image.open("tmp/01aaaa.jpg")
    mask = jpg_im3.resize((640,640), Image.NEAREST)
    time.sleep(3)
    result1 = ImageChops.blend(jpg_im1, jpg_im2, .5)
    
    #result1 = ImageChops.composite(jpg_im1, jpg_im2, mask)
    filename = time.strftime("/home/jack/Desktop/deep-dream-generator/notebooks/context-free/output/blended%Y%m%d%H%M%S.jpg")
    result1.save(filename)
    count=count+1
   

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
from random import randint
from PIL import Image
from PIL import ImageChops


square_size = 10
offset_factor = 20
darken_factor = 0.1
path = r"crawler4/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
    ])
filename0=(path+base_image)

image = Image.open(filename0)
size = image.size

# Create image np array
im = np.array(image, dtype=np.uint8)

# Create figure and axes
fig,ax = plt.subplots(1)

# Display the image
ax.imshow(im)

# Add random offset to tuple based on offset_factor
def add_offet(t):
    t[0] = random.randint(t[0], (t[0] + offset_factor))
    t[1] = random.randint(t[1], (t[1] + offset_factor))

    return t


# Create a Rectangle patch
for w in xrange(0, size[0], square_size):
    for h in xrange(0, size[1], square_size):
        #print str(w) + ':' + str(h)
        square_size = randint(10,30)
        offset_factor = randint(10,30)
    
        # Get the average color of the section
        rect = im[h:h+square_size, w:w+square_size]
        mean = rect.mean(axis=(0,1))

        # Convert to hex value
        face_color = '#%02x%02x%02x' % (int(mean[0]), int(mean[1]), int(mean[2]))
        edge_color = '#%02x%02x%02x' % (int(mean[0] - (mean[0] * darken_factor)), int(mean[1]  - (mean[1] * darken_factor)), int(mean[2] - (mean[2] * darken_factor)))

        # Dont draw outline with the dominant color
        z_order = 2
        if '#e' in face_color or '#f' in face_color:
            line_width = 0.0
        else:
            line_width = 0.1
            z_order = 3

        points = [add_offet([w, h]), add_offet([w + square_size, h]), add_offet([w, h + square_size])]
        triangle1 = patches.Polygon(points, edgecolor=edge_color, linewidth=line_width, facecolor=face_color, zorder=z_order)

        # Second triangle
        points2 = [add_offet([w, h + square_size]), add_offet([w + square_size, h + square_size]), add_offet([w + square_size, h])]
        triangle2 = patches.Polygon(points2, edgecolor=edge_color, linewidth=line_width, facecolor=face_color, zorder=z_order)

        # Square in background
        rec = patches.Rectangle((w,h),square_size,square_size,linewidth=0.0, edgecolor=edge_color, facecolor=face_color, zorder=1)

        # Add the patch to the Axes
        ax.add_patch(triangle1)
        ax.add_patch(triangle2)
        ax.add_patch(rec)

plt.axis('off')
plt.savefig("images/Sranger-Tri-001a.jpg", bbox_inches='tight', dpi=200)
img = Image.open("images/Sranger-Tri-001a.jpg")
nonwhite_positions = [(x,y) for x in range(img.size[0]) for y in range(img.size[1]) if img.getdata()[x+y*img.size[0]] != (255,255,255)]
rect = (min([x for x,y in nonwhite_positions]), min([y for x,y in nonwhite_positions]), max([x for x,y in nonwhite_positions]), max([y for x,y in nonwhite_positions]))
img.crop(rect).save('images/Sranger-Tri-001-crop2a.jpg')
#Create a second image
square_size = 10
offset_factor = 20
darken_factor = 0.1
#image = Image.open("images/Sranger002.jpg")

size = image.size

# Create image np array
im = np.array(image, dtype=np.uint8)

# Create figure and axes
fig,ax = plt.subplots(1)

# Display the image
ax.imshow(im)

# Add random offset to tuple based on offset_factor
def add_offet(t):
    t[0] = random.randint(t[0], (t[0] + offset_factor))
    t[1] = random.randint(t[1], (t[1] + offset_factor))

    return t


# Create a Rectangle patch
for w in xrange(0, size[0], square_size):
    for h in xrange(0, size[1], square_size):
        #print str(w) + ':' + str(h)
        square_size = randint(15,30)
        offset_factor = randint(15,30)
    
        # Get the average color of the section
        rect = im[h:h+square_size, w:w+square_size]
        mean = rect.mean(axis=(0,1))

        # Convert to hex value
        face_color = '#%02x%02x%02x' % (int(mean[0]), int(mean[1]), int(mean[2]))
        edge_color = '#%02x%02x%02x' % (int(mean[0] - (mean[0] * darken_factor)), int(mean[1]  - (mean[1] * darken_factor)), int(mean[2] - (mean[2] * darken_factor)))

        # Dont draw outline with the dominant color
        z_order = 2
        if '#e' in face_color or '#f' in face_color:
            line_width = 0.0
        else:
            #line_width = 0.1
            z_order = 3

        points = [add_offet([w, h]), add_offet([w + square_size, h]), add_offet([w, h + square_size])]
        triangle1 = patches.Polygon(points, edgecolor=edge_color, linewidth=line_width, facecolor=face_color, zorder=z_order)

        # Second triangle
        points2 = [add_offet([w, h + square_size]), add_offet([w + square_size, h + square_size]), add_offet([w + square_size, h])]
        triangle2 = patches.Polygon(points2, edgecolor=edge_color, linewidth=line_width, facecolor=face_color, zorder=z_order)

        # Square in background
        rec = patches.Rectangle((w,h),square_size,square_size,linewidth=0.0, edgecolor=edge_color, facecolor=face_color, zorder=1)

        # Add the patch to the Axes
        ax.add_patch(triangle1)
        ax.add_patch(triangle2)
        ax.add_patch(rec)

plt.axis('off')
plt.savefig("images/Sranger-Tri-001a.jpg", bbox_inches='tight', dpi=200)
img = Image.open("images/Sranger-Tri-001a.jpg")
nonwhite_positions = [(x,y) for x in range(img.size[0]) for y in range(img.size[1]) if img.getdata()[x+y*img.size[0]] != (255,255,255)]
rect = (min([x for x,y in nonwhite_positions]), min([y for x,y in nonwhite_positions]), max([x for x,y in nonwhite_positions]), max([y for x,y in nonwhite_positions]))
img.crop(rect).save('images/Sranger-Tri-001-crop2b.jpg')


img0 = Image.open("images/Sranger-Tri-001-crop2a.jpg")
img1 = Image.open("images/Sranger-Tri-001-crop2b.jpg")
blen = ImageChops.blend(img0, img1, .5)
blen.save('images/Sranger-Tri-001-crop2b.jpg')
blen

#Very Good COMPOSITE ___ _ do not change
from PIL import Image, ImageChops
import time
import random
import os
count = 0
while count<550: 
    #path = r"build/"
    path = r"crawler/"
    base_image = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
        ])
    filename0=(path+base_image)

    path0 = r"crawler1/"
    #path0 = r"testmasks/"
    base_image0 = random.choice([
        x0 for x0 in os.listdir(path0)
        if os.path.isfile(os.path.join(path0, x0))
        ])
    filename00=(path0+base_image0)

    path1 = r"newmask/"
    base_image1 = random.choice([
        x1 for x1 in os.listdir(path1)
        if os.path.isfile(os.path.join(path1, x1))
        ])
    mask0=(path1+base_image1)

    im1 = Image.open(filename0).convert('RGB')
    im1 = im1.resize((640,640), Image.NEAREST)
    im1.save("tmp/01aa.jpg")
    jpg_im1 = Image.open("tmp/01aa.jpg") 

    im02 = Image.open(filename00).convert('RGB')
    im2 = im02.resize((640,640), Image.NEAREST)
    im2.save("tmp/01aaa.jpg")
    jpg_im2 = Image.open("tmp/01aaa.jpg") 

    im03 = Image.open(mask0)
    im03.save("tmp/01aaaa.jpg")
    jpg_im3 = Image.open("tmp/01aaaa.jpg") 
    im03 = jpg_im3.resize((640,640), Image.NEAREST)
    time.sleep(3)
    result1 = ImageChops.blend(jpg_im1, jpg_im2, .5)
    
    #result1 = ImageChops.composite(jpg_im1, jpg_im2, im03)
    filename = time.strftime("aug25/%Y%m%d%H%M%S.jpg")
    result1.save(filename)
    count=count+1
   

!mkdir aug25

result1.save(filename)

jpg_im1

jpg_im2

im03

from PIL import Image, ImageChops
jpg_im3 = Image.open("junk/03.jpg") 
jpg_im3

#Very Good COMPOSITE ___ _ do not change
from PIL import Image, ImageChops
import time
import random
import os
path = r"build/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
    ])
filename0=(path+base_image)

#path0 = r"blend/"
path0 = r"testmasks/"
base_image0 = random.choice([
    x0 for x0 in os.listdir(path0)
    if os.path.isfile(os.path.join(path0, x0))
    ])
filename00=(path0+base_image0)

path1 = r"testmasks/"
base_image1 = random.choice([
    x1 for x1 in os.listdir(path1)
    if os.path.isfile(os.path.join(path1, x1))
    ])
mask0=(path1+base_image1)

im1 = Image.open(filename0)
im1 = im1.resize((640,640), Image.NEAREST)
im1.save("junk/01.jpg")
jpg_im1 = Image.open("junk/01.jpg") 

im02 = Image.open(filename00)
im2 = im02.resize((640,640), Image.NEAREST)
im1.save("junk/02.jpg")
jpg_im2 = Image.open("junk/02.jpg") 

im03 = Image.open(mask0)
im03.save("junk/03.jpg")
jpg_im3 = Image.open("junk/03.jpg") 
im03 = jpg_im3.resize((640,640), Image.NEAREST)
  
result1 = ImageChops.composite(jpg_im1, jpg_im2, im03)
filename = time.strftime("junk/%Y%m%d%H%M%S.jpg")
#result1.save(filename)
result1

!ls ../deep-dream-generator/notebooks/STUFF/experiment

#Very Good COMPOSITE ___ _ do not change
from PIL import Image, ImageChops
import time
import random
import os

count=count+1
while count<300:
    path = r"/home/jack/Desktop/deep-dream-generator/notebooks/new/1/"
    #path = r"build/"
    base_image = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
        ])
    filename0=(path+base_image)

    #path0 = r"blend/"
    path0 = r"output/"
    base_image0 = random.choice([
        x0 for x0 in os.listdir(path0)
        if os.path.isfile(os.path.join(path0, x0))
        ])
    filename00=(path0+base_image0)

    path1 = r"newmask/"
    base_image1 = random.choice([
        x1 for x1 in os.listdir(path1)
        if os.path.isfile(os.path.join(path1, x1))
        ])
    mask0=(path1+base_image1)

    im1 = Image.open(filename0)
    im1 = im1.resize((640,640), Image.NEAREST)
    im1.save("junk/01.jpg")
    jpg_im1 = Image.open("junk/01.jpg") 

    im02 = Image.open(filename00)
    im2 = im02.resize((640,640), Image.NEAREST)
    im1.save("junk/02.jpg")
    jpg_im2 = Image.open("junk/02.jpg") 

    im03 = Image.open(mask0)
    im03.save("junk/03.jpg")
    jpg_im3 = Image.open("junk/03.jpg") 
    im03 = jpg_im3.resize((640,640), Image.NEAREST)
    time.sleep(3)
    result1 = ImageChops.blend(jpg_im1, jpg_im2, .03)
    filename = time.strftime("greedy/%Y%m%d%H%M%S.jpg")
    #result1.save(filename)
    result1
    count=count+1

#Very Good COMPOSITE ___ _ do not change
from PIL import Image, ImageChops
import time
import random
import os
count=0
while count <400:
    path = r"crawler4/"
    #path = r"build/"
    base_image = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
        ])
    filename0=(path+base_image)
    random.seed(5)
    time.sleep(5)
    #path0 = r"blend/"
    path0 = r"crawler4/"
    base_image0 = random.choice([
        x0 for x0 in os.listdir(path0)
        if os.path.isfile(os.path.join(path0, x0))
        ])
    filename00=(path0+base_image0)

    path1 = r"newmask/"
    base_image1 = random.choice([
        x1 for x1 in os.listdir(path1)
        if os.path.isfile(os.path.join(path1, x1))
        ])
    mask0=(path1+base_image1)

    im1 = Image.open(filename0)
    im1 = im1.resize((640,640), Image.NEAREST)
    im1.save("junk/01.png")
    jpg_im1 = Image.open("junk/01.png") 

    im02 = Image.open(filename00)
    im2 = im02.resize((640,640), Image.NEAREST)
    im1.save("junk/02.png")
    jpg_im2 = Image.open("junk/02.png") 

    im03 = Image.open(mask0)
    im03.save("junk/03.png")
    jpg_im3 = Image.open("junk/03.png") 
    im03 = jpg_im3.resize((640,640), Image.NEAREST)
  
    result1 = ImageChops.blend(jpg_im1, jpg_im2, .5)
    filename = time.strftime("crawler4/%Y%m%d%H%M%S.png")
    result1.save(filename)
    count=count+1

#Very Good COMPOSITE ___ _ do not change
from PIL import Image, ImageChops
import time
import random
import os
  

#Very Good COMPOSITE ___ _ do not change
from PIL import Image, ImageChops
import time
import random
import os
path = r"/home/jack/Desktop/deep-dream-generator/notebooks/new/1/"
#path = r"build/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
    ])
filename0=(path+base_image)

#path0 = r"blend/"
path0 = r"crawler4/"
base_image0 = random.choice([
    x0 for x0 in os.listdir(path0)
    if os.path.isfile(os.path.join(path0, x0))
    ])
filename00=(path0+base_image0)

path1 = r"newmask/"
base_image1 = random.choice([
    x1 for x1 in os.listdir(path1)
    if os.path.isfile(os.path.join(path1, x1))
    ])
mask0=(path1+base_image1)

im1 = Image.open(filename0)
im1 = im1.resize((640,640), Image.NEAREST)
im1.save("junk/01.png")
jpg_im1 = Image.open("junk/01.png") 

im02 = Image.open(filename00)
im2 = im02.resize((640,640), Image.NEAREST)
im1.save("junk/02.png")
jpg_im2 = Image.open("junk/02.png") 

im03 = Image.open(mask0)
im03.save("junk/03.png")
jpg_im3 = Image.open("junk/03.png") 
im03 = jpg_im3.resize((640,640), Image.NEAREST)
  
result1 = ImageChops.blend(jpg_im1, jpg_im2, .5)
filename = time.strftime("output/%Y%m%d%H%M%S.png")
result1.save(filename)
result1

result1.save(filename)

from PIL import Image, ImageChops
help(ImageChops)

#Very Good COMPOSITE ___ _ do not change
from PIL import Image, ImageChops
import time
import random
import os

path = r"build/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))])
filename=(path+base_image)
im1 = Image.open(filename)
im1 = im1.resize((640,640), Image.NEAREST)
im1.save("tmp/01.jpg")
jpg_im1 = Image.open("tmp/01.jpg") 




path0 = r"blend/"
#path0 = r"basic/"
base_image0 = random.choice([
    x0 for x0 in os.listdir(path0)
    if os.path.isfile(os.path.join(path0, x0))])
filename00=(path0+base_image0)
im02 = Image.open(filename00)
im2 = im02.resize((640,640), Image.NEAREST)
im1.save("tmp/02.jpg")
jpg_im2 = Image.open("tmp/02.jpg")


pathm = r"mask/"
#path0 = r"basic/"
mask01 = random.choice([
    x0 for x0 in os.listdir(pathm)
    if os.path.isfile(os.path.join(pathm, x0))])
filenameM=(pathm+mask01)
imM = Image.open(filenameM)
imMm = imM.resize((640,640), Image.NEAREST)
imMm.save("tmp/03.png")
jpg_M = Image.open("tmp/03.png") 



pathm = r"experiment/"
#path0 = r"basic/"
base_image01 = random.choice([
    x0 for x0 in os.listdir(pathm)
    if os.path.isfile(os.path.join(pathm, x0))])
filename001=(pathm+base_image01)
im03 = Image.open(filename001)
im3 = im03.resize((640,640), Image.NEAREST)
im3.save("tmp/03.jpg")
jpg_im3 = Image.open("tmp/03.jpg") 




result1 = ImageChops.lighter(jpg_im1, jpg_im2)  
result2 = ImageChops.blend(jpg_im1, result1, 0.5)
result4 = ImageChops.composite(jpg_im1, result2, jpg_M)
result3 = ImageChops.blend(jpg_im2, result2, 0.5)
#filename = time.strftime("darkimages/%Y%m%d%H%M%S.jpg")
#result1.save(filename)
result4

#Very Good COMPOSITE ___ _ do not change
from PIL import Image, ImageChops
import time
import random
import os

path = r"build/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))])
filename=(path+base_image)
im1 = Image.open(filename)
im1 = im1.resize((640,640), Image.NEAREST)
im1.save("tmp/01.jpg")
jpg_im1 = Image.open("tmp/01.jpg") 




path0 = r"blend/"
#path0 = r"basic/"
base_image0 = random.choice([
    x0 for x0 in os.listdir(path0)
    if os.path.isfile(os.path.join(path0, x0))])
filename00=(path0+base_image0)
im02 = Image.open(filename00)
im2 = im02.resize((640,640), Image.NEAREST)
im1.save("tmp/02.jpg")
jpg_im2 = Image.open("tmp/02.jpg")


pathm = r"testmasks/"
#path0 = r"basic/"
mask01 = random.choice([
    x0 for x0 in os.listdir(pathm)
    if os.path.isfile(os.path.join(pathm, x0))])
filenameM=(pathm+mask01)
imM = Image.open(filenameM)
imMm = imM.resize((640,640), Image.NEAREST)
imMm.save("tmp/03.png")
jpg_M = Image.open("tmp/03.png") 



pathm = r"experiment/"
#path0 = r"basic/"
base_image01 = random.choice([
    x0 for x0 in os.listdir(path01)
    if os.path.isfile(os.path.join(path01, x0))])
filename001=(path01+base_image01)
im03 = Image.open(filename001)
im3 = im03.resize((640,640), Image.NEAREST)
im3.save("tmp/03.jpg")
jpg_im3 = Image.open("tmp/03.jpg") 




result1 = ImageChops.lighter(jpg_im1, jpg_im2)  
result2 = ImageChops.blend(jpg_im1, result1, 0.5)
result4 = ImageChops.composite(jpg_im1, result2, jpg_im3)
result3 = ImageChops.blend(jpg_im2, result2, 0.5)
result5 = ImageChops.screen(result2, result3)
result6 = ImageChops.darker(result5, result5)
#filename = time.strftime("darkimages/%Y%m%d%H%M%S.jpg")
#result1.save(filename)
result6

filename = time.strftime("tmp/%Y%m%d%H%M%S.jpg")
result5.save(filename)

inv=ImageChops.invert(result5)
inv

xoffset = 5
newim= ImageChops.offset(inv, xoffset, yoffset=None)
newim

resultXX = ImageChops.blend(newim, result5, 0.5)

filename = time.strftime("tmp/%Y%m%d%H%M%S.jpg")
resultXX.save(filename)
resultXX

filename = time.strftime("tmp/%Y%m%d%H%M%S.jpg")
resultXX.save(filename)

from PIL import Image, ImageChops
import time
import random
import os
path01 = r"experiment/"
#path0 = r"basic/"
base_image01 = random.choice([
    x0 for x0 in os.listdir(path01)
    if os.path.isfile(os.path.join(path01, x0))])
print base_image01

from PIL import Image, ImageChops
import time
import random
import os
path01 = r"experiment/"
#path0 = r"basic/"
base_image01 = random.choice([
    x0 for x0 in os.listdir(path01)
    if os.path.isfile(os.path.join(path01, x0))])
filename001=(path01+base_image01)
im03 = Image.open(filename001)
im3 = im03.resize((640,640), Image.NEAREST)
im3.save("tmp/03.jpg")
jpg_im3 = Image.open("tmp/03.jpg") 
#filename = time.strftime("tmp/%Y%m%d%H%M%S.jpg")
#result5.save(filename)
inv=ImageChops.invert(jpg_im3)

xoffset = 5
newim= ImageChops.offset(inv, xoffset, yoffset=None)
newim

from PIL import Image, ImageChops
import time
import random
import os
path01 = r"experiment/"
#path0 = r"basic/"
base_image01 = random.choice([
    x0 for x0 in os.listdir(path01)
    if os.path.isfile(os.path.join(path01, x0))])
filename001=(path01+base_image01)

im03 = Image.open(filename001)
im03 = im03.convert('L') 



im3 = im03.resize((640,640), Image.NEAREST)
im3.save("tmp/03.jpg")
jpg_im3 = Image.open("tmp/03.jpg") 
#filename = time.strftime("tmp/%Y%m%d%H%M%S.jpg")
#result5.save(filename)
inv=ImageChops.invert(jpg_im3)
xoffset = 5
newim= ImageChops.offset(inv, xoffset, yoffset=None)

resultXX = ImageChops.blend(newim, inv, 0.5)
#filename = time.strftime("tmp/03.jp")

#resultXX.save(filename)

#jpg_new = resultXX.resize((640,640), Image.NEAREST)

#jpg_new
resultXX


# Working Fine 
from PIL import Image, ImageChops
import time
import random
import os
pathm = r"experiment/"
#path0 = r"basic/"
base_image01 = random.choice([
    x0 for x0 in os.listdir(path01)
    if os.path.isfile(os.path.join(path01, x0))])
filename001=(path01+base_image01)

im03 = Image.open(filename001)
im03 = im03.convert('L') 
im3 = im03.resize((640,640), Image.NEAREST)
im3.save("tmp/03.jpg")


jpg_im3 = Image.open("tmp/03.jpg") 
jpg_new = jpg_im3.resize((640,640), Image.NEAREST)

inv=ImageChops.invert(jpg_new)
xoffset = 5
newim= ImageChops.offset(inv, xoffset, yoffset=None)
result5 = newim.resize((640,640), Image.NEAREST)


resultXX = ImageChops.blend(newim, im03, 0.5)

resultXX 


# Gray scale Embossing --- Working Fine 
from PIL import Image, ImageChops
import time
import random
import os
import cv2
pathm = r"experiment/"
#path0 = r"basic/"
base_image01 = random.choice([
    x0 for x0 in os.listdir(path01)
    if os.path.isfile(os.path.join(path01, x0))])
filename001=(path01+base_image01)

im03 = Image.open(filename001)
im03 = im03.convert('L') 

im3 = im03.resize((640,640), Image.NEAREST)
im3.save("tmp/03.jpg")
im03 = cv2.imread("tmp/03.jpg")
blur = cv2.blur(im03,(2,2))
cv2.imwrite("tmp/03.jpg", blur)


jpg_im3 = Image.open("tmp/03.jpg") 
jpg_new = jpg_im3.resize((640,640), Image.NEAREST)

inv=ImageChops.invert(jpg_new)
xoffset = 5
newim= ImageChops.offset(inv, xoffset, yoffset=None)
result5 = newim.resize((640,640), Image.NEAREST)


resultXX = ImageChops.blend(newim, jpg_im3, 0.5)

resultXX 


from PIL import Image, ImageChops
import time
import random
import os
pathm = r"experiment/"
#path0 = r"basic/"
base_image01 = random.choice([
    x0 for x0 in os.listdir(path01)
    if os.path.isfile(os.path.join(path01, x0))])
filename001=(path01+base_image01)

im03 = Image.open(filename001)
im3 = im03.resize((640,640), Image.NEAREST)
im3.save("tmp/03.jpg")

jpg_im3 = Image.open("tmp/03.jpg") 
jpg_new = jpg_im3.resize((640,640), Image.NEAREST)


inv=ImageChops.invert(jpg_im3)
xoffset = 5
newim= ImageChops.offset(inv, xoffset, yoffset=None)

result5 = newim.resize((640,640), Image.NEAREST)

resultXX = ImageChops.blend(newim, result5, 0.5)

resultXX 


import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
from random import randint
from PIL import Image
from PIL import ImageChops
import os

square_size = 10
offset_factor = 20
darken_factor = 0.1
path = r"basic/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
    ])
filename0=(path+base_image)

image = Image.open(filename0)
size = image.size

# Create image np array
im = np.array(image, dtype=np.uint8)

# Create figure and axes
fig,ax = plt.subplots(1)

# Display the image
ax.imshow(im)

# Add random offset to tuple based on offset_factor
def add_offet(t):
    t[0] = random.randint(t[0], (t[0] + offset_factor))
    t[1] = random.randint(t[1], (t[1] + offset_factor))

    return t


# Create a Rectangle patch
for w in xrange(0, size[0], square_size):
    for h in xrange(0, size[1], square_size):
        #print str(w) + ':' + str(h)
        square_size = randint(10,30)
        offset_factor = randint(10,30)
    
        # Get the average color of the section
        rect = im[h:h+square_size, w:w+square_size]
        mean = rect.mean(axis=(0,1))

        # Convert to hex value
        face_color = '#%02x%02x%02x' % (int(mean[0]), int(mean[1]), int(mean[2]))
        edge_color = '#%02x%02x%02x' % (int(mean[0] - (mean[0] * darken_factor)), int(mean[1]  - (mean[1] * darken_factor)), int(mean[2] - (mean[2] * darken_factor)))

        # Dont draw outline with the dominant color
        z_order = 2
        if '#e' in face_color or '#f' in face_color:
            line_width = 0.0
        else:
            line_width = 0.1
            z_order = 3

        points = [add_offet([w, h]), add_offet([w + square_size, h]), add_offet([w, h + square_size])]
        triangle1 = patches.Polygon(points, edgecolor=edge_color, linewidth=line_width, facecolor=face_color, zorder=z_order)

        # Second triangle
        points2 = [add_offet([w, h + square_size]), add_offet([w + square_size, h + square_size]), add_offet([w + square_size, h])]
        triangle2 = patches.Polygon(points2, edgecolor=edge_color, linewidth=line_width, facecolor=face_color, zorder=z_order)

        # Square in background
        rec = patches.Rectangle((w,h),square_size,square_size,linewidth=0.0, edgecolor=edge_color, facecolor=face_color, zorder=1)

        # Add the patch to the Axes
        ax.add_patch(triangle1)
        ax.add_patch(triangle2)
        ax.add_patch(rec)

plt.axis('off')
plt.savefig("images/Sranger-Tri-001a.jpg", bbox_inches='tight', dpi=200)

path = r"basic/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
    ])
filename0=(path+base_image)


img = Image.open("images/Sranger-Tri-001a.jpg")
nonwhite_positions = [(x,y) for x in range(img.size[0]) for y in range(img.size[1]) if img.getdata()[x+y*img.size[0]] != (255,255,255)]
rect = (min([x for x,y in nonwhite_positions]), min([y for x,y in nonwhite_positions]), max([x for x,y in nonwhite_positions]), max([y for x,y in nonwhite_positions]))
img.crop(rect).save('images/Sranger-Tri-001-crop2a.jpg')
#Create a second image
square_size = 10
offset_factor = 20
darken_factor = 0.1
#image = Image.open("images/Sranger002.jpg")

size = image.size

# Create image np array
im = np.array(image, dtype=np.uint8)

# Create figure and axes
fig,ax = plt.subplots(1)

# Display the image
ax.imshow(im)

# Add random offset to tuple based on offset_factor
def add_offet(t):
    t[0] = random.randint(t[0], (t[0] + offset_factor))
    t[1] = random.randint(t[1], (t[1] + offset_factor))

    return t


 

img = Image.open("images/Sranger-Tri-001a.jpg")
nonwhite_positions = [(x,y) for x in range(img.size[0]) for y in range(img.size[1]) if img.getdata()[x+y*img.size[0]] != (255,255,255)]
rect = (min([x for x,y in nonwhite_positions]), min([y for x,y in nonwhite_positions]), max([x for x,y in nonwhite_positions]), max([y for x,y in nonwhite_positions]))
img.crop(rect).save('images/Sranger-Tri-001-crop2b.jpg')

path = r"basic/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
    ])
filename0=(path+base_image)





im0 = Image.open("images/Sranger-Tri-001-crop2b.jpg")
img0 = im0.resize((640,640,3), Image.NEAREST)

im1 = Image.open(filename0)
img1 = im1.resize((640,640,3), Image.NEAREST)



blen = ImageChops.blend(img0, img1, .5)
blen.save('junk/Sranger-Tri-001-crop2b.jpg')
blen

#So I managed to do it, using "palette" image type, but the resulting file is not as small as I expected... 
#Here's my code in case its useful for someone else, or if someone can improve on it.

from PIL import Image

im = Image.open("tmp/03b.png")
imP = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=5)
imP.putpalette([
    0, 0, 0, # index 0 is black background
    0, 0, 255, # index 1 is blue
    255, 0, 0, # index 2 is red 
    ])

im2 = Image.open("tmp/03b.png")
imP2L = im2.convert('L') # need a greyscale image to create a mask
mask = Image.eval(imP2L, lambda a: 255 if a == 0 else 0)
imP.paste(2, mask) # Paste the color of index 2 using image2 as a mask
imP.save('tmp/wow-out3a.png', transparency = 0, optimize = 1) # Save and set index 0 as transparent



-

!showme tmp/wow-out3a.png

im = Image.open('tmp/wow-out3a.png')
rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((1, 1))

print(r, g, b)


max_width = max(image.size[0] for image in images)
max_height = max(image.size[1] for image in images)

image_sheet = Image.new("RGBA", (max_width * len(images), max_height))

for (i, image) in enumerate(images):
    image_sheet.paste(image, (
        max_width * i + (max_width - image.size[0]) / 2,
        max_height * 0 + (max_height - image.size[1]) / 2
    ))

image_sheet.save("whatever.png")
image_sheet

from PIL import Image
img = Image.new('RGB', (240,240), (255, 255, 255))
img.save("tmp/image.png", "PNG")

from math import sin

#creates a grayscale 
from PIL import Image
from math import sin, cos
img = Image.new('RGB', (256,256), (255, 255, 255))
img.save("tmp/image.png", "PNG")
image = Image.open('tmp/image.png') #open image
image = image.convert("RGBA")  #convert to RGBA
h,w = image.size
hh=0
ww=0
hl = h-h/2
wl = w-w/2
zl = (hl+5)+(wl-5)
aa = 255
i=2
while hh < h:
    ww=0
    while ww < w:
        r,g,b,a = image.getpixel((hh, ww)) #Get the rgba value at coordinates x,y
        #sin(x*y)+sin(y*z)+sin(z*x)==0
        x=ww-126
        y=hh-126
        z=ww-130
        if int(abs((cos(x**2-cos(y)-x+y**2)))*200)>60:
            co = int(abs((cos(x**2-cos(y)-x+y**2)))*200)
            image.putpixel((hh, ww), (co,0,0,aa)) #put back the modified reba values at same pixel coordinates
        else:
            image.putpixel((hh, ww), (255,255,255,aa))
        image.save("tmp/image2.png", "PNG")   
        ww = ww + 1
    hh=hh+1


image




import Image, ImageDraw

im = Image.open("lena.pgm")

draw = ImageDraw.Draw(im)

# Fill=128 creates a grey line
draw.line((0, 0) + im.size, fill=128)   
draw.line((0, im.size[1], im.size[0], 0), fill=128)
del draw

# write to stdout
im.save(sys.stdout, "PNG")

from PIL import Image
image = Image.open('tmp/wow-out3a.png') #open image
image = image.convert("RGBA")  #convert to RGBA
r,g,b,a = image.getpixel((x, y)) #Get the rgba value at coordinates x,y
A = a/100
#r,g,b,a = int(r,g,b,(a / 2)) #or you could do rgb[3] = 50 maybe? #set alpha to half somehow
image.putpixel((x,y), (r,g,b,A)) #put back the modified reba values at same pixel coordinates
image




i = "i.png"
o = "o.png"

key = (0, 0, 0, 255)

from PIL import Image as I

_i = I.open(i)
_ii = _i.load()

_o = I.new("RGBA", _i.size)
_oo = _o.load()

for x in range(0, _i.size[0]): 
    for y in range(0, _i.size[1]): 
        col = list(_ii[x, y])
        if col[0:3] == my_key_color[0:3]:
            _oo[x,y] = col[0:3]+(0,) # keep RGB, set A to 0
        else:
            _oo[x,y] = col

_o.save(o)



from skimage import io
import numpy as np

image = io.imread('http://i.stack.imgur.com/Y8UeF.jpg')

print(np.mean(image))

You might want to convert all images to float to get a value betwenn 0 and 1:

from skimage import io, img_as_float
import numpy as np

image = io.imread('http://i.stack.imgur.com/Y8UeF.jpg')
image = img_as_float(image)
print(np.mean(image))

from PIL import Image

img = Image.open('tmp/03b.png')
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("tmp/img2.png", "PNG")
img

from PIL import Image, ImageChops

image_two = Image.open ("tmp/03b.png")
image_two = image_two.convert ("RGBA")

pixels = image_two.load()

for y in xrange (image_two.size[1]):
    for x in xrange (image_two.size[0]):
        if pixels[x, y][3] == 255:
            pixels[x, y] = (255, 0, 0, 255)
        else:
            pixels[x, y] = (255, 255, 255, 255)

image_two.save("tmp/image_two2.png")

from PIL import Image, ImageChops
import time
def remove_transparency(im, bg_colour=(255, 255, 255)):

    # Only process if image has transparency (http://stackoverflow.com/a/1963146)
    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):

        # Need to convert to RGBA if LA format due to a bug in PIL (http://stackoverflow.com/a/1963146)
        alpha = im.convert('RGBA').split()[-1]

        # Create a new background image of our matt color.
        # Must be RGBA because paste requires both images have the same format
        # (http://stackoverflow.com/a/8720632  and  http://stackoverflow.com/a/9459208)
        bg = Image.new("RGBA", im.size, bg_colour + (255,))
        bg.paste(im, mask=alpha)
        return bg

    else:
        return im
    
im3 = Image.open('tmp/03a.png')     
nim =remove_transparency(im3, bg_colour=(255, 255, 255))

nim.save('tmp/03b.png')
nim

# Gray scale Embossing --- Working Fine 
from PIL import Image, ImageChops
import time
import random
import os
import cv2
import numpy as np
pathm = r"experiment/"
#path0 = r"basic/"
base_image01 = random.choice([
    x0 for x0 in os.listdir(path01)
    if os.path.isfile(os.path.join(path01, x0))])
filename001=(path01+base_image01)

im03 = Image.open(filename001)
im03 = im03.convert('L') 

im3 = im03.resize((640,640), Image.NEAREST)
im3.save("tmp/03.jpg")
im03 = cv2.imread("tmp/03.jpg")
blur = cv2.blur(im03,(2,2))
cv2.imwrite("tmp/03.jpg", blur)


jpg_im3 = Image.open("tmp/03.jpg") 
jpg_new = jpg_im3.resize((640,640), Image.NEAREST)

inv=ImageChops.invert(jpg_new)
xoffset = 5
newim= ImageChops.offset(inv, xoffset, yoffset=None)
result5 = newim.resize((640,640), Image.NEAREST)


resultXX = ImageChops.blend(newim, jpg_im3, 0.5)

pix = np.array(resultXX)
blurfin = cv2.blur(pix,(4,4))
cv2.imwrite("tmp/05a.jpg", blurfin)




!showme tmp/05a.jpg

# Gray scale Embossing --- Working Fine 
from PIL import Image, ImageChops
import time
import random
import os
import cv2
pathm = r"experiment/"
#path0 = r"basic/"
base_image01 = random.choice([
    x0 for x0 in os.listdir(path01)
    if os.path.isfile(os.path.join(path01, x0))])
filename001=(path01+base_image01)

im03 = Image.open(filename001)
im03 = im03.convert('L') 

im3 = im03.resize((640,640), Image.NEAREST)
im3.save("tmp/03.jpg")
im03 = cv2.imread("tmp/03.jpg")
blur = cv2.blur(im03,(2,2))
cv2.imwrite("tmp/03.jpg", blur)


jpg_im3 = Image.open("tmp/03.jpg") 
jpg_new = jpg_im3.resize((640,640), Image.NEAREST)

inv=ImageChops.invert(jpg_new)
xoffset = 5
newim= ImageChops.offset(inv, xoffset, yoffset=None)
result5 = newim.resize((640,640), Image.NEAREST)


resultXX = ImageChops.blend(newim, jpg_im3, 0.5)

resultXX 


# Working Fine 
from PIL import Image, ImageChops
import time
import random
import os
pathm = r"experiment/"
#path0 = r"basic/"
base_image01 = random.choice([
    x0 for x0 in os.listdir(path01)
    if os.path.isfile(os.path.join(path01, x0))])
filename001=(path01+base_image01)

im03 = Image.open(filename001)
im03 = im03.convert('L') 
im3 = im03.resize((640,640), Image.NEAREST)
im3.save("tmp/03.jpg")


jpg_im3 = Image.open("tmp/03.jpg") 
jpg_new = jpg_im3.resize((640,640), Image.NEAREST)

inv=ImageChops.invert(jpg_new)
xoffset = 5
newim= ImageChops.offset(inv, xoffset, yoffset=None)
result5 = newim.resize((640,640), Image.NEAREST)


resultXX = ImageChops.blend(newim, im03, 0.5)

resultXX 


from PIL import Image, ImageFont, ImageDraw, ImageEnhance

source_img = Image.open("tmp/tmp.jpg").convert("RGBA")


font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 15)
text = "TwitterBot Project"
# get text size
text_size = font.getsize(text)
# set button size + 10px margins
button_size = (text_size[0]+8, text_size[1]+8)
# create image with correct size and black background
button_img = Image.new('RGBA', button_size, "black")
# put text on button with 10px margins
button_draw = ImageDraw.Draw(button_img)
button_draw.text((4, 4), text, font=font)




# put button on source image in position (0, 0)
source_img.paste(button_img, (15,15))
# save in new file
source_img.save("junk/output.jpg", "JPEG")
source_img

image=Image.open("star_blue.png")
opacity=0.5
bands=list(self.image.split())
if len(bands)==4:
    bands[3]=bands[3].point(lambda x:x*opacity)
    new_image=Image.merge(image.mode,bands)


from PIL import Image, ImageFont, ImageDraw, ImageEnhance

source_img = Image.open("tmp/tmp.jpg").convert("RGBA")


font2 = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 15)
text = "TwitterBot Project"
# get text size
text_size = font.getsize(text)
# set button size + 10px margins
button_size = (text_size[0]+8, text_size[1]+8)
# create image with correct size and black background
button_img = Image.new('RGBA', button_size, "black")
# put text on button with 10px margins
button_draw = ImageDraw.Draw(button_img)
button_draw.text((4, 4), text, font=font2)
opacity=0.5
bands=list(button_img.split())
if len(bands)==4:
    bands[3]=bands[3].point(lambda x:x*opacity)
    new_image=Image.merge(button_img.mode,bands)
# put button on source image in position (0, 0)
source_img.paste(new_image, (15,15))
# save in new file
source_img.save("junk/output.jpg", "JPEG")
source_img





import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

width = 854
height = 480
black = (0,0,0)
text = "copyright"
white = (255,255,255)
font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 35)
img = Image.new("RGBA", (width,height),white)
draw = ImageDraw.Draw(img)
w, h = draw.textsize(text, font)
draw.text(((width-w)/2,(height-h)/2),text,black,font=font)
draw = ImageDraw.Draw(img)
#img.putalpha
img.save("junk/result2.png")
img

!showme junk/output.jpg

from PIL import Image
bg = Image.open("1.jpg")
fg = Image.open("2.jpg")
# set alpha to .7
Image.blend(bg, fg, .7).save("out.png")



image=Image.open("star_blue.png")
opacity=0.5
bands=list(self.image.split())
if len(bands)==4:
    bands[3]=bands[3].point(lambda x:x*opacity)
    new_image=Image.merge(image.mode,bands)


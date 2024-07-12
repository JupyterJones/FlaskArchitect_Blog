https://note.nkmk.me/en/python-pillow-paste/

!locate data/src/rocket.jpg

from PIL import Image, ImageDraw, ImageFilter

im1 = Image.open('data/src/lena.jpg')
im2 = Image.open('data/src/rocket.jpg').resize(im1.size)
mask = Image.new("L", im1.size, 128)
im = Image.composite(im1, im2, mask)
# im = Image.blend(im1, im2, 0.5)
mask = Image.new("L", im1.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((140, 50, 260, 170), fill=255)
im = Image.composite(im1, im2, mask)
mask = Image.open('data/src/horse.png').convert('L').resize(im1.size)
im = Image.composite(im1, im2, mask)


from random import randint
import random
import os
CHOOSE =[]
Paths = open("directory.list","r")
for path in Paths:
    path = str(path).replace("\n","")
    CHOOSE.append(path)
def usefile():
    ID = randint(0, len(CHOOSE)-1)
    DIR = CHOOSE[ID]
    return DIR

print(usefile())

path = usefile()
base_image = random.choice([
x for x in os.listdir(path)
if os.path.isfile(os.path.join(path, x))
        ])
filename0=(path+base_image)
print(filename0)

from PIL import Image, ImageDraw, ImageFilter
from random import randint
import random
import os
CHOOSE =[]
Paths = open("directory.list","r")
for path in Paths:
    path = str(path).replace("\n","")
    CHOOSE.append(path)
def usefile():
    ID = randint(0, len(CHOOSE)-1)
    DIR = CHOOSE[ID]
    return DIR

path = usefile()
base_image = random.choice([
x for x in os.listdir(path)
if os.path.isfile(os.path.join(path, x))
        ])
filename0=(path+base_image)
print(filename0)

im1 = Image.open(filename0)

path0 = usefile()
base_image = random.choice([
x for x in os.listdir(path0)
if os.path.isfile(os.path.join(path, x))
        ])
filename00=(path0+base_image)
print(filename00)
im2 = Image.open(filename00)


im1.paste(im2)
#im1.save('data/dst/rocket_pillow_paste.jpg', quality=95)
im1

im1 = Image.open(filename00)
im2 = Image.open(filename0)

back_im = im1.copy()
back_im.paste(im2)
#back_im.save('data/dst/rocket_pillow_paste.jpg', quality=95)
back_im

#Specify the position to paste

#The position to paste is specified by a tuple (x coordinate in upper left, y coordinate in upper left) 
#in the second parameter box.

back_im = im1.copy()
back_im.paste(im2, (100, 50))
#back_im.save('data/dst/rocket_pillow_paste_pos.jpg', quality=95)
back_im

#If the pasted image extends outside the region of the base image, the area that extends is ignored.

back_im = im1.copy()
back_im.paste(im2, (400, 100))
#back_im.save('data/dst/rocket_pillow_paste_out.jpg', quality=95)
back_im

from PIL import Image
mask_im = Image.new("L", im2.size, 0)
draw = ImageDraw.Draw(mask_im)
draw.ellipse((140, 50, 260, 170), fill=255)
#mask_im.save('junk/mask_circle.jpg', quality=95)
mask_im


back_im = im1.copy()
back_im.paste(im2, (0, 0), mask_im)
back_im.save('junk/mask_circle.jpg', quality=95)
back_im

mask_im_blur = mask_im.filter(ImageFilter.GaussianBlur(10))
mask_im_blur.save('junk/mask_circle_blur.jpg', quality=95)

mask_im_blur

back_im = im1.copy()
back_im.paste(im2, (0, 0), mask_im_blur)
back_im.save('junk/_mask_circle_blur.jpg', quality=95)
back_im

#After the image is read by open(), it is adjusted to the size of the pasted image by resize(),
#and the mode is converted to 'L' (grayscale) by convert().

mask_im = Image.open(filename00).resize(im2.size).convert('L')

back_im = im1.copy()
back_im.paste(im2, (100, 50), mask_im)
back_im.save('junk/_paste_mask_horse.jpg', quality=95)
back_im

from PIL import Image, ImageDraw

images = []

width = 200
center = width // 2
color_1 = (0, 0, 0)
color_2 = (255, 255, 255)
max_radius = int(center * 1.5)
step = 8

for i in range(0, max_radius, step):
    im = Image.new('RGB', (width, width), color_1)
    draw = ImageDraw.Draw(im)
    draw.ellipse((center - i, center - i, center + i, center + i), fill=color_2)
    images.append(im)

for i in range(0, max_radius, step):
    im = Image.new('RGB', (width, width), color_2)
    draw = ImageDraw.Draw(im)
    draw.ellipse((center - i, center - i, center + i, center + i), fill=color_1)
    images.append(im)

images[0].save('junk/pillow_imagedraw.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)


im = Image.new('RGB', (500, 250), (128, 128, 128))
draw = ImageDraw.Draw(im)

draw.line(((30, 200), (130, 100), (80, 50)), fill=(255, 255, 0))
draw.line(((80, 200), (180, 100), (130, 50)), fill=(255, 255, 0), width=10)
draw.polygon(((200, 200), (800, 100), (250, 50)), fill=(255, 255, 0), outline=(0, 0, 0))
draw.point(((350, 200), (450, 100), (400, 50)), fill=(255, 255, 0))
im

im = Image.new('RGB', (600, 250), (128, 128, 128))
draw = ImageDraw.Draw(im)

draw.arc((25, 50, 175, 200), start=30, end=270, fill=(255, 255, 0))
draw.chord((225, 50, 375, 200), start=30, end=270, fill=(255, 255, 0), outline=(0, 0, 0))
draw.pieslice((425, 50, 575, 200), start=30, end=270, fill=(255, 255, 0), outline=(0, 0, 0))


im = Image.open(filename00)
draw = ImageDraw.Draw(im)

draw.pieslice((15, 50, 140, 175), start=30, end=330, fill=(255, 255, 0))
im

from PIL import Image, ImageDraw, ImageFilter

im_rgb = Image.open(filename0)
im_rgba = im_rgb.copy()
im_rgba.putalpha(128)
im_rgba.save('junk/pillow_putalpha_solid.png')
im_rgba

im_a = Image.new("L", im_rgb.size, 0)
draw = ImageDraw.Draw(im_a)
draw.ellipse((140, 50, 260, 170), fill=255)
im_a

im_rgba = im_rgb.copy()
im_rgba.putalpha(im_a)
im_rgba_crop = im_rgba.crop((140, 50, 260, 170))
im_rgba_crop.save('junk/pillow_putalpha_circle.png')

im_rgba_crop

m_rgba = im_rgb.copy()
im_rgba.putalpha(im_a_blur)
im_rgba_crop = im_rgba.crop((135, 45, 265, 175))
im_rgba_crop.save('junk/pillow_putalpha_circle_blur.png')

im_rgba_crop






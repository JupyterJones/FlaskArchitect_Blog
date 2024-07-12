from PIL import ImageFont, ImageDraw, Image
import time
import os
import random
from random import randint

!mkdir base
!mkdir images

!wget -O images/0003xxx.jpg https://jacknorthrup.com/INSTAGRAM/0003xxx.jpg
!wget -O images/0195insta.jpg https://jacknorthrup.com/INSTAGRAM/0195insta.jpg

!mv Philippine-Specialty-Paper.jpg.1 images/background.jpg
!mv postoid\ \(10\).jpg.1 images/postoid.jpg

from PIL import Image
#IM = Image.open('images/background.jpg')
IM = Image.open('images/0195insta.jpg')
im=IM.resize((1280,720), Image.NEAREST)
im

from PIL import Image
#IM = Image.open('images/postoid.jpg')
IM = Image.open('images/0003xxx.jpg')
IM

from PIL import ImageFont, ImageDraw, Image
import time
import os
import random
from random import randint
        
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
#IMAGE1 = 'images/background.jpg'
IMAGE1 = '/home/jack/Documents/QmaBzt5dcMaGm4mQ7doCEZZsQs3m5HGf27pbkKDnFUcyKt.png'
image = Image.open(IMAGE1)
image = image.resize((1280,720), Image.NEAREST)
W,H = image.size
draw = ImageDraw.Draw(image)
txt = "Linux VPS  @LBRY_vps"
fontsize = 6 # starting font size
W, H = image.size
# portion of image width you want text width to be
base = Image.new('RGB',(W, H))

font = ImageFont.truetype(FONT, fontsize)
#print image.size

W,H = base.size
nSize = base.resize((W-100, H-30,), Image.NEAREST)
#print blank.size
while (font.getsize(txt)[0] < nSize.size[0]) and (font.getsize(txt)[1] < nSize.size[1]):
    # iterate until the text size is just larger than the criteria
    fontsize += 1
    font = ImageFont.truetype(FONT, fontsize)

# optionally de-increment to be sure it is less than criteria
fontsize -= 1
font = ImageFont.truetype(FONT, fontsize)

w, h = draw.textsize(txt, font=font)
#print 'final font size',fontsize, FONT
draw.text((15,605), txt, font=font, fill="black") # put the text on the image
draw.text((20,600), txt, font=font, fill="white") # put the text on the image
DT = time.strftime("base/%Y-%m-%d-%H-%M-%S.png")
image.save(DT) # save it
print (DT)

from PIL import Image
IM = Image.open(DT)
IM

from PIL import ImageFilter, ImageDraw, ImageFont, Image
import time
import shutil
import os
import random
from PIL import Image
from random import randint
font_file='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
#file_path ="base/2020-02-21-08-54-23.png"
file_path ="base/2022-11-11-18-02-30.png"
IMG = Image.open(file_path)
im =IMG.resize((1280,720), Image.NEAREST)

file_path0='/home/jack/Documents/QmaRW2BgnB7foncFM8aZcHUeA8BTamQxxrgycQfNR2CAAV.png'
IMG0 = Image.open(file_path0)
IMG0 =IMG0.resize((570,570), Image.NEAREST)
IMG0 = IMG0.convert('RGBA')
w,h = IMG0.size

#the shadow for the overlay
foreground = Image.new('RGBA', (w,h), (0, 0, 0, 240))
im.paste(foreground, (625, 35), foreground)
im = im.filter(ImageFilter.MinFilter(3))
background = im.filter(ImageFilter.BLUR)
# Almost transparent white
foreground1 = Image.new('RGBA', (1280,720), (255, 255, 255, 100))
background.paste(foreground1, (0, 0), foreground1)
background.paste(IMG0, (640, 20), IMG0)

text0 = "CREATED by"
text1 = "LBRY-Toolbox"
text2 = "ImageBot"
x= randint(1,4)
r=randint(125,200)
g=randint(125,200)
b=randint(125,200)
colour = (r, g, b)
colours = (0,0,0)
font_size = 70
font = ImageFont.truetype(font_file, font_size)
w, h = font.getsize(text1)
draw = ImageDraw.Draw(background)
H=x*8
draw.text((20+H, 170+H),text0, colours, font=font)
draw.text((20+H, 270+H),text1, colours, font=font)
draw.text((20+H, 370+H),text2, colours, font=font)
draw.text((20+H-5, 170+H+5),text0, colour, font=font)
draw.text((20+H-5, 270+H+5),text1, colour, font=font)
draw.text((20+H-5, 370+H+5),text2, colour, font=font)
#DT = time.strftime("images/%Y-%m-%d-%H-%M.png")
DT = "images/TEMP01.png"
background.save(DT)
print (DT)

IMG = Image.open(DT)
IMG

from PIL import ImageFilter, ImageDraw, ImageFont, Image, ImageEnhance
import time
import shutil
import os
import random
from PIL import Image
from random import randint
font_file='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
file_path ="base/2020-02-21-08-54-23.png"
IMG = Image.open(file_path)
im =IMG.resize((1280,720), Image.NEAREST)

file_path0='images/0003xxx.jpg'
IMG0 = Image.open(file_path0)
IMG0 =IMG0.resize((570,570), Image.NEAREST)
IMG0 = IMG0.convert('RGBA')

sharp = ImageEnhance.Sharpness(IMG0)
sharpness = 5.0
sharpened = sharp.enhance(sharpness)
w,h = sharpened.size

#the shadow for the overlay
foreground = Image.new('RGBA', (w,h), (0, 0, 0, 240))
im.paste(foreground, (625, 35), foreground)
im = im.filter(ImageFilter.MinFilter(3))
background = im.filter(ImageFilter.BLUR)
# Almost transparent white
foreground1 = Image.new('RGBA', (1280,720), (255, 255, 255, 100))
background.paste(foreground1, (0, 0), foreground1)
background.paste(sharpened, (640, 20), sharpened)

text0 = "CREATED by"
text1 = "LBRY-Toolbox"
text2 = "ImageBot"
x= randint(1,4)
r=randint(125,200)
g=randint(125,200)
b=randint(125,200)
colour = (r, g, b)
colours = (0,0,0)
font_size = 70
font = ImageFont.truetype(font_file, font_size)
w, h = font.getsize(text1)
draw = ImageDraw.Draw(background)
H=x*8
draw.text((20+H, 170+H),text0, colours, font=font)
draw.text((20+H, 270+H),text1, colours, font=font)
draw.text((20+H, 370+H),text2, colours, font=font)
draw.text((20+H-5, 170+H+5),text0, colour, font=font)
draw.text((20+H-5, 270+H+5),text1, colour, font=font)
draw.text((20+H-5, 370+H+5),text2, colour, font=font)
DT = time.strftime("images/%Y-%m-%d-%H-%M.png")
#DT = "images/TEMP01.png"
background.save(DT)
print (DT)

IMG = Image.open(DT)
IMG

!ls images/*.jpg

import requests

TEXT ="""
The postoid below has a funny story. Notice it is the leaning tower of FRANCE   ????? 
I had some mail art rubbber art stamps made. The set was in fact the same as the white postoid / mail art paper in our mail art specialty paper set. As soon as they came in I started stamping and playing with ideas. I made postoids until about 2:30am. That is when I made this four corner stamp. It wasn't until I had finished I realized I put the leaning tower of Pisa in my france stamp.
My faux stamp misprint
"""    
    

requests.post("http://localhost:5279", json={"method": "channel_create", "params": {"name": "@LBRY-vps", "bid": "1.0", "tags": "vps"}}).json()

#!/usr/bin/python2
import time
import urllib
import simplejson as json
import requests
data = requests.post("http://localhost:5279", json={"method": "channel_create", "params": {"name": "@lbry-vps", "bid": "2.0", "tags": "vps"}}).json()
LINES = (json.dumps(data, indent=2 * ' '))
Lin =str(LINES)
L = Lin.split("\n")
for lines in L:
        print (lines)


!ls *.mp4

#!/usr/bin/python2
import time
import urllib
import simplejson as json
import requests
name = "Posting-From-my-VPS" #no Spaces or Special Characters
title = "Javascript KdenliveFfmpeg Generated Video"
file_Path = "/home/jack/Desktop/LBRY-toolbox/Computer-Graphics-Javascript-Kdenlive-Open-Source-Software.mp4"
thumbnail = "https://lbry-toolbox.com/images/2020-02-21-04-59-24.png"
Text="""
In 1984 I was a heavy equipment mechanic. I knew I couldn't continue this type of work 
my entire life. One day, I was in my pickup truck on my way home from an extraordinarily 
difficult project and noticed a gaudy looking changeable letter sign. 
That sign read, "FREE - Adult Education: Introduction to computers”. I wrote the phone 
number in the dust of my pickup truck. Little did I know that phone number, in the dust 
on my dashboard, would change my life. I went to that course for about a week. I loved 
the concept of computers, but It was so crowded there was very little computer time. 
However, I loved the fact if you communicated properly and it always listened and did 
as you wish. I bought my first computer, my first of well over a hundred in all. 
I actually started building and selling computers just to keep up with the changing systems.
I retired from a career as a self-taught electrical engineer specializing in computer automation.
I am nearing seventy-two and still love the computer. I am a devoted Linux man and am thoroughly
devoted to LBRY. I am using the LBRY platform to learn several computer languages. Life is good!
Follow me here and on lbry.tv. Read the description for more details.
Music from https://filmmusic.io "Sovereign" by Kevin MacLeod (https://incompetech.com)
License: CC BY (http://creativecommons.org/licenses/by/4.0/)
"""
data = requests.post("http://localhost:5279", json={"method": "publish", "params": {"name": name, "bid": "0.01", "title": title, "file_path": file_Path, "tags": "VPS","description":Text, "thumbnail_url": thumbnail,"channel_id": "c133f925c7b68affa500c9b5492c1e16089aa17e"}}).json()
LINES = (json.dumps(data, indent=2 * ' '))
Lin =str(LINES)
L = Lin.split("\n")
for lines in L:
        print (lines)


!ffmpeg -i Computer-Graphics-Javascript-Kdenlive-Open-Source-Software.mp4 -vframes 1 -an -s 1280x720 -ss 26 -y OutputFile.jpg

from PIL import Image
IM= Image.open("OutputFile.jpg")
IM

!ffmpeg -i Computer-Graphics-Javascript-Kdenlive-Open-Source-Software.mp4

#!/usr/bin/python2
import time
import urllib
import simplejson as json
import requests
name = "First-Post-of-Wallet-Plot" #no Spaces or Special Characters
title = "This will be fun to look back at"
image = "/home/jack/Desktop/LBRY-toolbox/Computer-Graphics-Javascript-Kdenlive-Open-Source-Software.mp4"
thumbnail = "/home/jack/Desktop/VPS_resources/202002201016-final.png"
Text="""
I got a plot of the first two tips. WOW !
"""
data = requests.post("http://localhost:5279", json={"method": "publish", "params": {"name": name, "bid": "0.01", "title": title, "file_path": image, "tags": "LBC Plot","description":Text, "thumbnail_url": image, "channel_id": "0dba0712be1bf830f8c2c11872399d5f61704dbf" }}).json()
LINES = (json.dumps(data, indent=2 * ' '))
Lin =str(LINES)
L = Lin.split("\n")
for lines in L:
      print (lines)


0dba0712be1bf830f8c2c11872399d5f61704dbf

!ls Computer-Graphics-Javascript-Kdenlive-Open-Source-Software.mp4







!locate *.ttf

!ls /usr/share/fonts/truetype/

!ls /mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/All-images/

print(FONT[2])

FONT =[]
def randomfont(pathf):
    imgf = random.choice(os.listdir(pathf))
    file_path =pathf+imgf+".ttf"
    file_path0 =path0+img0
    return file_path
for i in range(20):
    pathf = '/usr/share/fonts/truetype/'
    print (randomfont(pathf))
    FONT.append(randomfont(pathf))

from PIL import ImageFilter, ImageDraw, ImageFont
import time
import shutil
import os
import random
from PIL import Image
from random import randint
path = '/home/jack/Documents/'
img = random.choice(os.listdir(path))
path0 = '/home/jack/Documents/'
img0 = random.choice(os.listdir(path0))
file_path =path+img
file_path0 =path0+img0
IMG = Image.open(file_path)
IMG0 = Image.open(file_path0)
IMG0 =IMG0.resize((640,640), Image.NEAREST)
w,h = IMG0.size
IMG1 = IMG0.convert('RGBA')
im =IMG.resize((1280,720), Image.NEAREST)
foreground = Image.new('RGBA', (w+5,h+5), (0, 0, 0, 150))
im.paste(foreground, (580, 60), foreground)
im1 = im.filter(ImageFilter.MinFilter(7))
background = im1.filter(ImageFilter.BLUR)
foreground1 = Image.new('RGBA', (1280,720), (255, 255, 255, 100))
background.paste(foreground1, (0, 0), foreground1)
background.paste(IMG1, (600, 50), IMG1)
background
text0 = "CREATED by"
text1 = "LBRY-Toolbox"
text2 = "ImageBot"
x= randint(1,4)
r=randint(125,200)
g=randint(125,200)
b=randint(125,200)
colour = (r, g, b)
colours = (0,0,0)

path0 = '/home/jack/Documents/'
img0 = random.choice(os.listdir(path0))
file_path =path+img
file_path0 =path0+img0

font_file = FONT[2]
font_file = FONT[2]
font_file = FONT[2]
font_file = FONT[2]
print(font_file)
font_size = 70
font = ImageFont.truetype(font_file, font_size)
w, h = font.getsize(text)
draw = ImageDraw.Draw(background)
H=x*8
draw.text((30+H, 170+H),text0, colours, font=font)
draw.text((30+H, 270+H),text1, colours, font=font)
draw.text((30+H, 370+H),text2, colours, font=font)
draw.text((30+H-5, 170+H+5),text0, colour, font=font)
draw.text((30+H-5, 270+H+5),text1, colour, font=font)
draw.text((30+H-5, 370+H+5),text2, colour, font=font)
DT = time.strftime("images/%Y-%m-%d-%H-%M.png")
background.save(DT)

from PIL import Image
file_path = DT
IMG = Image.open(file_path)
IMG

from PIL import ImageFont, ImageDraw, Image
import time
import os
import random
from random import randint
def pick(font_path):    
        
        font=random.choice([x for x in os.listdir(font_path) if os.path.isfile(os.path.join(font_path, x))])
        return font_path+font
def mkimage(path1):
    
    img = random.choice(os.listdir(path1))
    file_path =path1+img 
    return file_path

def mkbatch(mkimage,pick):
    image = Image.open(mkimage)
    image = image.resize((1280,720), Image.NEAREST)
    W,H = image.size
    draw = ImageDraw.Draw(image)
    txt = "Python Generated /Processed Images"
    fontsize = 6 # starting font size

    W, H = image.size

    # portion of image width you want text width to be
    blank = Image.new('RGB',(W, H))

    FONT = pick
    font = ImageFont.truetype(FONT, fontsize)
    #print image.size

    W,H = blank.size
    blank = blank.resize((W-100, H-30,), Image.NEAREST)
    #print blank.size
    while (font.getsize(txt)[0] < blank.size[0]) and (font.getsize(txt)[1] < blank.size[1]):
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype(FONT, fontsize)

    # optionally de-increment to be sure it is less than criteria
    fontsize -= 1
    font = ImageFont.truetype(FONT, fontsize)

    w, h = draw.textsize(txt, font=font)

    #print 'final font size',fontsize, FONT
    draw.text((15,625), txt, font=font, fill="black") # put the text on the image
    draw.text((20,620), txt, font=font, fill="white") # put the text on the image
    DT = time.strftime("base/%Y-%m-%d-%H-%M-%S.png")
    image.save(DT) # save it
    #image
for i in range(1,500):
    path1 = '/mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/All-images/'
    font_path = '/home/jack/fonts/'
    mkbatch(mkimage(path1),pick(font_path))
    time.sleep(3)
    print ".",

!locate STIXGeneralBol.ttf

!locate *.ttf

from PIL import ImageFont, ImageDraw, Image
import time
image = Image.open("/home/jack/Documents/use-to-seed003.jpg")
image = image.resize((1280,720), Image.NEAREST)
W,H = image.size
draw = ImageDraw.Draw(image)
txt = "Python Generated Processed Images"
fontsize = 6 # starting font size

W, H = image.size

# portion of image width you want text width to be
blank = Image.new('RGB',(W, H))

FONT = "/home/jack/miniconda3/pkgs/matplotlib-base-3.5.2-py310hf590b9c_0/lib/python3.10/site-packages/matplotlib/mpl-data/fonts/ttf/STIXGeneralBol.ttf"
font = ImageFont.truetype(FONT, fontsize)
print (image.size)

W,H = blank.size
blank = blank.resize((W-100, H-30,), Image.NEAREST)
#print blank.size
while (font.getsize(txt)[0] < blank.size[0]) and (font.getsize(txt)[1] < blank.size[1]):
    # iterate until the text size is just larger than the criteria
    fontsize += 1
    font = ImageFont.truetype(FONT, fontsize)

# optionally de-increment to be sure it is less than criteria
fontsize -= 1
font = ImageFont.truetype(FONT, fontsize)

w, h = draw.textsize(txt, font=font)

print ('final font size',fontsize, FONT)
draw.text((15,625), txt, font=font, fill="black") # put the text on the image
draw.text((20,620), txt, font=font, fill="white") # put the text on the image
DT = time.strftime("base/%Y-%m-%d-%H-%M-%S.png")
print (DT)
image.save(DT) # save it
image

from PIL import ImageFont, ImageDraw, Image
def pick():    
        font_path = '/home/jack/miniconda3/pkgs/matplotlib-base-3.5.2-py310hf590b9c_0/lib/python3.10/site-packages/matplotlib/mpl-data/fonts/ttf/'
        font=random.choice([x for x in os.listdir(font_path) if os.path.isfile(os.path.join(font_path, x))])
        return font_path+font
def mkimage():
    path = '/home/jack/Documents/jpg/720/'
    img = random.choice(os.listdir(path))
    file_path =path+img 
    return file_path

image = Image.open(mkimage())
image = image.resize((1280,720), Image.NEAREST)
W,H = image.size
draw = ImageDraw.Draw(image)
txt = "Python Generated Processed Images"
fontsize = 6 # starting font size

W, H = image.size

# portion of image width you want text width to be
blank = Image.new('RGB',(W, H))

FONT = pick()
font = ImageFont.truetype(FONT, fontsize)
print (image.size)

W,H = blank.size
blank = blank.resize((W-100, H-30,), Image.NEAREST)
print (blank.size)
while (font.getsize(txt)[0] < blank.size[0]) and (font.getsize(txt)[1] < blank.size[1]):
    # iterate until the text size is just larger than the criteria
    fontsize += 1
    font = ImageFont.truetype(FONT, fontsize)

# optionally de-increment to be sure it is less than criteria
fontsize -= 1
font = ImageFont.truetype(FONT, fontsize)

w, h = draw.textsize(txt, font=font)

print ('final font size',fontsize, FONT)
draw.text((15,625), txt, font=font, fill="black") # put the text on the image
draw.text((20,620), txt, font=font, fill="white") # put the text on the image
DT = time.strftime("base/%Y-%m-%d-%H-%M-%S.png")
image.save(DT) # save it
image

/home/jack/fonts/Quatl.ttf
/home/jack/fonts/Exo-Black.ttf
/home/jack/fonts/Rafika.ttf
/home/jack/fonts/georgiab.ttf
/home/jack/fonts/Biryani-Light.ttf
/home/jack/fonts/Regulators.ttf
/home/jack/fonts/Quatl.ttf
/home/jack/fonts/DancingScript-VariableFont_wght.ttf
/home/jack/fonts/Tafelschrift.ttf     (nice script)
/home/jack/fonts/VeraSe.ttf

IMG=Image.open("sample-out.png")
IMG



from PIL import ImageFilter, ImageDraw, ImageFont
import time
import shutil
import os
import random
from PIL import Image
from random import randint
path = '/mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/All-images/'
img = random.choice(os.listdir(path))
path0 = '/mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/All-images/'
img0 = random.choice(os.listdir(path0))
file_path =path+img
file_path0 =path0+img0
IMG = Image.open(file_path)
IMG0 = Image.open(file_path0)
IMG0 =IMG0.resize((640,640), Image.NEAREST)
w,h = IMG0.size
IMG1 = IMG0.convert('RGBA')
im =IMG.resize((1280,720), Image.NEAREST)
foreground = Image.new('RGBA', (w+5,h+5), (0, 0, 0, 150))
im.paste(foreground, (580, 60), foreground)
im1 = im.filter(ImageFilter.MinFilter(7))
background = im1.filter(ImageFilter.BLUR)
foreground1 = Image.new('RGBA', (1280,720), (255, 255, 255, 100))
background.paste(foreground1, (0, 0), foreground1)
background.paste(IMG1, (600, 50), IMG1)
background
text0 = "CREATED by"
text1 = "LBRY-Toolbox"
text2 = "ImageBot"
x= randint(1,4)
r=randint(125,200)
g=randint(125,200)
b=randint(125,200)
colour = (r, g, b)
colours = (0,0,0)

if x==1:font_file = '/usr/share/fonts/truetype/freefont/FreeSansBold.ttf'
if x==2:font_file ="/home/jack/fonts/Biryani-Black.ttf"
if x==3:font_file ="/home/jack/fonts/ChangaOne-Regular.ttf"
if x==4:font_file ="/home/jack/fonts/Exo-Black.ttf"
font_size = 70
font = ImageFont.truetype(font_file, font_size)
w, h = font.getsize(text)
draw = ImageDraw.Draw(background)
H=x*8
draw.text((30+H, 170+H),text0, colours, font=font)
draw.text((30+H, 270+H),text1, colours, font=font)
draw.text((30+H, 370+H),text2, colours, font=font)
draw.text((30+H-5, 170+H+5),text0, colour, font=font)
draw.text((30+H-5, 270+H+5),text1, colour, font=font)
draw.text((30+H-5, 370+H+5),text2, colour, font=font)
DT = time.strftime("images/%Y-%m-%d-%H-%M.png")
background.save(DT)

from PIL import Image
file_path = DT
IMG = Image.open(file_path)
IMG

from PIL import ImageFilter, ImageDraw, ImageFont
import time
import shutil
import os
import random
from PIL import Image
from random import randint
def pick():    
        font_path = '/home/jack/fonts/'
        font=random.choice([x for x in os.listdir(font_path) if os.path.isfile(os.path.join(font_path, x))])
        return font_path+font
def mkimage():
    path = '/mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/All-images/'
    img = random.choice(os.listdir(path))
    file_path =path+img 
    path0 = '/mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/All-images/'
    img0 = random.choice(os.listdir(path0))
    file_path0 =path0+img0
    IMG = Image.open(file_path)
    IMG0 = Image.open(file_path0)
    IMG0 =IMG0.resize((640,640), Image.NEAREST)
    w,h = IMG0.size
    IMG1 = IMG0.convert('RGBA')
    im =IMG.resize((1280,720), Image.NEAREST)
    foreground = Image.new('RGBA', (w+5,h+5), (0, 0, 0, 150))
    im.paste(foreground, (580, 60), foreground)
    im1 = im.filter(ImageFilter.MinFilter(7))
    background = im1.filter(ImageFilter.BLUR)
    foreground1 = Image.new('RGBA', (1280,720), (255, 255, 255, 100))
    background.paste(foreground1, (0, 0), foreground1)
    background.paste(IMG1, (600, 50), IMG1)
    background
    text0 = "CREATED by"
    text1 = "LBRY-Toolbox"
    text2 = "ImageBot"
    x= randint(1,4)
    r=randint(125,200)
    g=randint(125,200)
    b=randint(125,200)
    colour = (r, g, b)
    colours = (0,0,0)
    font_file = pick()
    #font_file = random.choice([x for x in os.listdir(font_path) if os.path.isfile(os.path.join(font_path, x))])
    #if x==1:font_file = '/usr/share/fonts/truetype/freefont/FreeSansBold.ttf'
    #if x==2:font_file ="/home/jack/fonts/Biryani-Black.ttf"
    #if x==3:font_file ="/home/jack/fonts/ChangaOne-Regular.ttf"
    #if x==4:font_file ="/home/jack/fonts/Exo-Black.ttf"
    font_size = 70
    font = ImageFont.truetype(font_file, font_size)
    w, h = font.getsize(text)
    draw = ImageDraw.Draw(background)
    H=x*8
    draw.text((30+H, 170+H),text0, colours, font=font)
    draw.text((30+H, 270+H),text1, colours, font=font)
    draw.text((30+H, 370+H),text2, colours, font=font)
    draw.text((30+H-5, 170+H+5),text0, colour, font=font)
    draw.text((30+H-5, 270+H+5),text1, colour, font=font)
    draw.text((30+H-5, 370+H+5),text2, colour, font=font)
    DT = time.strftime("manybot/%Y-%m-%d-%H-%M-%S.png")
    background.save(DT)

for i in range(1,500):
    time.sleep(3)
    print ".",
    mkimage()

from PIL import ImageFilter, ImageDraw, ImageFont
import time
import shutil
import os
import random
from PIL import Image
from random import randint
path = '/mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/GOOD-Blends/'
img = random.choice(os.listdir(path))
path0 = '/mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/GOOD-Blends/'
img0 = random.choice(os.listdir(path0))
file_path =path+img
file_path0 =path0+img0
IMG = Image.open(file_path)
IMG0 = Image.open(file_path0)
IMG0 =IMG0.resize((640,640), Image.NEAREST)
w,h = IMG0.size
IMG1 = IMG0.convert('RGBA')
im =IMG.resize((1280,720), Image.NEAREST)
foreground = Image.new('RGBA', (w+5,h+5), (0, 0, 0, 150))
im.paste(foreground, (580, 60), foreground)
im1 = im.filter(ImageFilter.MinFilter(7))
background = im1.filter(ImageFilter.BLUR)
foreground1 = Image.new('RGBA', (1280,720), (255, 255, 255, 100))
background.paste(foreground1, (0, 0), foreground1)
background.paste(IMG1, (600, 50), IMG1)
background
text0 = "CREATED by"
text1 = "LBRY-Toolbox"
text2 = "ImageBot"
x= randint(1,4)
r=randint(125,200)
g=randint(125,200)
b=randint(125,200)
colour = (r, g, b)
colours = (0,0,0)

if x==1:font_file = '/usr/share/fonts/truetype/freefont/FreeSansBold.ttf'
if x==2:font_file ="/home/jack/fonts/Biryani-Black.ttf"
if x==3:font_file ="/home/jack/fonts/ChangaOne-Regular.ttf"
if x==4:font_file ="/home/jack/fonts/Exo-Black.ttf"
font_size = 70
font = ImageFont.truetype(font_file, font_size)
w, h = font.getsize(text)
draw = ImageDraw.Draw(background)
H=x*8
draw.text((30+H, 170+H),text0, colours, font=font)
draw.text((30+H, 270+H),text1, colours, font=font)
draw.text((30+H, 370+H),text2, colours, font=font)
draw.text((30+H-5, 170+H+5),text0, colour, font=font)
draw.text((30+H-5, 270+H+5),text1, colour, font=font)
draw.text((30+H-5, 370+H+5),text2, colour, font=font)
DT = time.strftime("images/%Y-%m-%d-%H-%M.png")
background.save(DT)

from PIL import Image
file_path = DT
IMG = Image.open(file_path)
IMG

for x in range(1,40):
    y= randint(1,4)
    print y,

from PIL import ImageFilter, ImageDraw, ImageFont
import time
import shutil
import os
import random
from PIL import Image
from random import randint
path = '/mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/forvids/images/'
img = random.choice(os.listdir(path))
file_path =path+img
file_path0 =path+img
IMG = Image.open(file_path)
IMG0 = Image.open(file_path0)
IMG0 =IMG0.resize((640,640), Image.NEAREST)
w,h = IMG0.size
IMG1 = IMG0.convert('RGBA')
im =IMG.resize((1280,720), Image.NEAREST)
foreground = Image.new('RGBA', (w+5,h+5), (0, 0, 0, 150))
im.paste(foreground, (580, 60), foreground)
im1 = im.filter(ImageFilter.MinFilter(7))
background = im1.filter(ImageFilter.BLUR)
foreground1 = Image.new('RGBA', (1280,720), (255, 255, 255, 100))
background.paste(foreground1, (0, 0), foreground1)
background.paste(IMG1, (600, 50), IMG1)
background
text0 = "CREATED by"
text1 = "LBRY-Toolbox"
text2 = "ImageBot"
x= randint(1,4)
r=randint(125,200)
g=randint(125,200)
b=randint(125,200)
colour = (r, g, b)
colours = (0,0,0)

if x==1:font_file = '/usr/share/fonts/truetype/freefont/FreeSansBold.ttf'
if x==2:font_file ="/home/jack/fonts/Biryani-Black.ttf"
if x==3:font_file ="/home/jack/fonts/ChangaOne-Regular.ttf"
if x==4:font_file ="/home/jack/fonts/Exo-Black.ttf"
font_size = 70
font = ImageFont.truetype(font_file, font_size)
w, h = font.getsize(text)
draw = ImageDraw.Draw(background)
H=x*8
draw.text((30+H, 170+H),text0, colours, font=font)
draw.text((30+H, 270+H),text1, colours, font=font)
draw.text((30+H, 370+H),text2, colours, font=font)
draw.text((30+H-5, 170+H+5),text0, colour, font=font)
draw.text((30+H-5, 270+H+5),text1, colour, font=font)
draw.text((30+H-5, 370+H+5),text2, colour, font=font)
DT = time.strftime("images/%Y-%m-%d-%H-%M.png")
background.save(DT)

from PIL import Image
file_path = DT
IMG = Image.open(file_path)
IMG


#image = Image.open(path+img)
print path+img
#shutil.copy(image,"images/image1.jpg")
#shutil.copy(image,"images/image2.jpg")

import shutil
import os
import random
from PIL import Image
path = '/mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/forvids/images/'
img = random.choice(os.listdir(path))
img = Image.open(path+img)
def getAverageRGB(img):
  """
  Given PIL Image, return average value of color as (r, g, b)
  """
  # no. of pixels in image
  npixels = image.size[0]*image.size[1]
  # get colors as [(cnt1, (r1, g1, b1)), ...]
  cols = image.getcolors(npixels)
  # get [(c1*r1, c1*g1, c1*g2),...]
  sumRGB = [(x[0]*x[1][0], x[0]*x[1][1], x[0]*x[1][2]) for x in cols] 
  # calculate (sum(ci*ri)/np, sum(ci*gi)/np, sum(ci*bi)/np)
  # the zip gives us [(c1*r1, c2*r2, ..), (c1*g1, c1*g2,...)...]
  avg = tuple([sum(x)/npixels for x in zip(*sumRGB)])
  return avg
print getAverageRGB(img)

!mv  Retrieve-Twitter-Tweets-Images.html /var/www/lbry-toolbox.com/public/notebooks

!ls *.jpg

!wget https://jacknorthrup.com/jupyter-notebooks/retrieve-firefox-passwords-enter-sqlite-database.html

!wget https://jacknorthrup.com/image2/v2.jpg

from PIL import Image
file_path = DT
IMG = Image.open(file_path)
IMG

path = '/home/jack/Desktop/JupyterNotebooks-languages/manybot/'
img = random.choice(os.listdir(path))
file_Path =path+img

IM=Imageopen(file_Path)
IM

from PIL import ImageFont, ImageDraw, Image
import time
import os
import random
from random import randint
def pick(font_path):    
        
        font=random.choice([x for x in os.listdir(font_path) if os.path.isfile(os.path.join(font_path, x))])
        return font_path+font
def mkimage(path1):
    
    img = random.choice(os.listdir(path1))
    file_path =path1+img 
    return file_path

def mkbatch(mkimage,pick):
    image = Image.open(mkimage)
    image = image.resize((1280,720), Image.NEAREST)
    W,H = image.size
    draw = ImageDraw.Draw(image)
    txt = "Python Generated /Processed Images"
    fontsize = 6 # starting font size

    W, H = image.size

    # portion of image width you want text width to be
    blank = Image.new('RGB',(W, H))

    FONT = pick
    font = ImageFont.truetype(FONT, fontsize)
    #print image.size

    W,H = blank.size
    blank = blank.resize((W-100, H-30,), Image.NEAREST)
    #print blank.size
    while (font.getsize(txt)[0] < blank.size[0]) and (font.getsize(txt)[1] < blank.size[1]):
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype(FONT, fontsize)

    # optionally de-increment to be sure it is less than criteria
    fontsize -= 1
    font = ImageFont.truetype(FONT, fontsize)

    w, h = draw.textsize(txt, font=font)

    #print 'final font size',fontsize, FONT
    draw.text((15,625), txt, font=font, fill="black") # put the text on the image
    draw.text((20,620), txt, font=font, fill="white") # put the text on the image
    DT = time.strftime("base/%Y-%m-%d-%H-%M-%S.png")
    image.save(DT) # save it
    #image
for i in range(1,500):
    path1 = '/mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/All-images/'
    font_path = '/home/jack/fonts/'
    mkbatch(mkimage(path1),pick(font_path))
    time.sleep(3)
    print ".",

!pwd

scp /home/jack/Desktop/JupyterNotebooks-languages/images/BGI-056.jpg jack@192.243.108.78:/var/www/lbry-toolbox.com/public/images

!ls /home/jack/Desktop/JupyterNotebooks-languages/images/BGI-056.jpg

/mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/data/ancient art

https://lbry-toolbox.com/images/BGI-056.jpg

#!/usr/bin/python2
import os
from random import randint
from time import sleep
import time
import urllib
import simplejson as json
import requests
import sys
import subprocess
from Completedpy2 import track_download
import sqlite3
import watchVID
DT = time.strftime("%Y-%m-%d-%H:%M")
name = "Plot-Created-by-LBRYCron-Bot" #no Spaces or Special Characters
title = "LBRY LBC Wallet Balance Plot Generated by a Linux Cron Job"
file_path ="/home/jack/Desktop/JupyterNotebooks-languages/test1280.png"
data = requests.post("http://localhost:5279", json={"method": "publish", "params": {"name": name, "bid": "0.01", "title": title, "file_path": file_path, "tags": "python plot","description":"Wallet balance plot generated by a Linux cron job" , "channel_name": "@MyLinuxToyBox" }}).json()
LINES = (json.dumps(data, indent=2 * ' '))
Lin =str(LINES)
L = Lin.split("\n")
for lines in L:
        print lines


from PIL import Image
file_path ="/home/jack/Desktop/JupyterNotebooks-languages/test-full.png"
IMG = Image.open(file_path)
IM =IMG.resize((1280,720), Image.NEAREST)
im = IM.size
IM.save("/home/jack/Desktop/JupyterNotebooks-languages/test1280.png")
IM

!lbrynet address list --address=bDyZqrP3KoUVjotbdiRsPgkXpqHvASLPrT --page_size=50 --page=1

!lbrynet address list 


!ls test.jpg



publish

Create or replace a stream claim at a given name (use 'stream create/update' for more control).
Arguments

name    str    name of the content (can only consist of a-z A-Z 0-9 and -(dash))
bid    optionaldecimal    amount to back the claim
file_path    optionalstr    path to file to be associated with name.
fee_currency    optionalstring    specify fee currency
fee_amount    optionaldecimal    content download fee
fee_address   optionalstr    address where to send fee payments, gefaut value from --claim_address if not provided
title    optionalstr    title of the publication
description    optionalstr    description of the publication
author    optionalstr    author of the publication. The usage for this field is not the same as for channels.
The author field is used to credit an author who is not the publisher and is not represented by the
channel. For example, a pdf file of 'The Odyssey' has an author of 'Homer' but may by published to a
channel such as '@classics', or to no channel at all
tags    optionallist    add content tags
languages    optionallist    languages used by the channel, using RFC 5646 format, eg: for English 
    `--languages=en` for Spanish (Spain) `--languages=es-ES` for Spanish (Mexican) `--languages=es-MX`
    for Chinese (Simplified) `--languages=zh-Hans` for Chinese (Traditional) `--languages=zh-Hant`
locations    optionallist    locations relevant to the stream, consisting of 2 letter `country` 
code and a `state`, `city` and a postal `code` along with a `latitude` and `longitude`. for JSON RPC:
    pass a dictionary with aforementioned attributes as keys,
eg: ... "locations": [{'country': 'US', 'state': 'NH'}] ... for command line: pass a colon delimited 
list with values in the following order: "COUNTRY:STATE:CITY:CODE:LATITUDE:LONGITUDE" making
sure to include colon for blank values, for example to provide only the 
city: ... --locations="::Manchester" with all values set: ...
--locations="US:NH:Manchester:03101:42.990605:-71.460989" optionally, you can just pass 
the "LATITUDE:LONGITUDE": ... --locations="42.990605:-71.460989" finally, you can also pass 
JSON string of dictionary on the command line as you would via JSON RPC ...
 --locations="{'country': 'US', 'state': 'NH'}"
    license
    optionalstr
    publication license
    license_url
    optionalstr
    publication license url
    thumbnail_url
    optionalstr
    thumbnail url
    release_time
    optionalint
    original public release of content, seconds since UNIX epoch
    width
    optionalint
    image/video width, automatically calculated from media file
    height
    optionalint
    image/video height, automatically calculated from media file
    duration
    optionalint
    audio/video duration in seconds, automatically calculated
    channel_id
    optionalstr
    claim id of the publisher channel
    channel_name
    optionalstr
    name of publisher channel
    channel_account_id
    optionalstr
    one or more account ids for accounts to look in for channel certificates, defaults to all accounts.
    account_id
    optionalstr
    account to use for holding the transaction
    wallet_id
    optionalstr
    restrict operation to specific wallet
    funding_account_ids
    optionallist
    ids of accounts to fund this transaction
    claim_address
    optionalstr
    address where the claim is sent to, if not specified it will be determined automatically from the account
    preview
    optionalbool
    do not broadcast the transaction
    blocking
    optionalbool
    wait until transaction is in mempool


def pick():    
        font_path = '/home/jack/fonts/'
        font=random.choice([x for x in os.listdir(font_path) if os.path.isfile(os.path.join(font_path, x))])
        return font_path+font
for i in range(1,100):
    print pick()    



def getAverageRGB(img):
  """
  Given PIL Image, return average value of color as (r, g, b)
  """
  # no. of pixels in image
  npixels = image.size[0]*image.size[1]
  # get colors as [(cnt1, (r1, g1, b1)), ...]
  cols = image.getcolors(npixels)
  # get [(c1*r1, c1*g1, c1*g2),...]
  sumRGB = [(x[0]*x[1][0], x[0]*x[1][1], x[0]*x[1][2]) for x in cols] 
  # calculate (sum(ci*ri)/np, sum(ci*gi)/np, sum(ci*bi)/np)
  # the zip gives us [(c1*r1, c2*r2, ..), (c1*g1, c1*g2,...)...]
  avg = tuple([sum(x)/npixels for x in zip(*sumRGB)])
  return avg
print getAverageRGB(img)

#https://stackoverflow.com/questions/24021579/how-to-set-appropriate-line-width-for-drawing-text-in-python-pil
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import textwrap
def pick():    
        font_path = '/home/jack/fonts/'
        font=random.choice([x for x in os.listdir(font_path) if os.path.isfile(os.path.join(font_path, x))])
        return font_path+font
    
size_x = 600 #This value can arbitrarily change
size_y = 700 #This value can arbitrarily change
font_size = 18 #This value can be adjusted to fit parameters of image if necessary

my_text = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam scelerisque sapien convallis nisl facilisis, sed facilisis odio accumsan. Maecenas vel leo eu turpis porta dictum at vel neque. Donec sagittis felis non tellus lacinia facilisis. Vivamus vel nisi ullamcorper, feugiat lorem sagittis, pellentesque dolor. Curabitur est magna, feugiat ut nibh quis, blandit vestibulum nisl. Sed pulvinar condimentum purus et rutrum. Proin magna arcu, scelerisque at gravida ut, convallis quis orci. Mauris ipsum tortor, laoreet et leo ac, lacinia euismod tellus. Curabitur volutpat nisi a metus faucibus, vel iaculis nisl fermentum. Curabitur et orci id sapien porttitor dignissim at ac dolor. Donec nec mattis nisi. ']

tx = Image.new('RGB', (size_x, size_y),color=(255,255,255))
draw = ImageDraw.Draw(tx)
randomfont=pick()
my_font = ImageFont.truetype(randomfont,size=font_size)
lines = textwrap.wrap(my_text[0], width = 130) #This width value needs to be set automatically
y_text = 0
for line in lines:
    width, height = my_font.getsize(line)
    draw.text((0, y_text), line, font = my_font, fill = (0,0,0))
    y_text += height

tx.show()

!ls /home/jack/Desktop/post

from PIL import Image
image = Image.open("/home/jack/Desktop/post/pil_text.png")
image

!ls -rant /home/jack/Desktop/VPS_resources

from PIL import Image
image = Image.open("/home/jack/Desktop/VPS_resources/202002201016-final.png")
image

from PIL import Image
image = Image.open("/home/jack/Desktop/post/202002200046-POST.png")
image

!cp base/2020-02-21-04-59-24.png /var/www/lbry-toolbox.com/public/images

https://lbry-toolbox.com/images/2020-02-21-04-59-24.png

from IPython.core.display import HTML
HTML("""
<style>
#notebook-container {
    padding: 15px;
    background-color: #E3F6FF;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.3);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.3);
}
.notebook_app {
    background-color: lightblue;
}
#header{
background-color: #ffebcd;
}
#notebook_name.filename{
color:DarkRed;
font-size:200%;
}
body #header{
background-color:#F9E1DF;
}
</style>
""")





!ls -d */

!mkdir publish

import random
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageChops 
import os
import sys
import time
count = 0
while count < 350:
    #path = r"art%20nouveau/"
    #path = r"vintage%20magazine%20covers/"
    path = r"vintage%20clothing%20patterns/"
    base_image = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    filename0=(path+base_image)
    print(filename0)

    #path0 = r"antique%20book%20covers/"
    #path0 = r"vintage%20advertisments/"
    path0 = r"ancient%20manuscript%20art/"
    base_image0 = random.choice([
        x0 for x0 in os.listdir(path0)
        if os.path.isfile(os.path.join(path0, x0))
    ])
    filename00=(path0+base_image0)
    print(filename00)
    
    path1 = r"binary_images/"
    base_image1 = random.choice([
        x1 for x1 in os.listdir(path1)
        if os.path.isfile(os.path.join(path1, x1))
    ])
    mask0=(path1+base_image1)
    print(mask0)



    im0 = Image.open(filename0)
    im1 = im0.resize((720,480), Image.NEAREST)

    im01 = Image.open(filename00)
    im2 = im01.resize((720,480), Image.NEAREST)
    
    im03 = Image.open(mask0)
    im03 = im03.resize((720,480), Image.NEAREST)
    
    
    result1 = ImageChops.composite(im1, im2, im03) 
    
    filename = time.strftime("publish/"+str(count)+"_%Y%m%d%H%M%S.jpg")
    result1.save(filename)
    time.sleep(3)
    count= count +1

# %load finddb.py
#!/home/jack/anaconda2/envs/py35/bin/python
# get the size of a list of files
#getting a list is easy  locate *.db >>sqlitedatabases.txt
import os
f = open('sqlitedatabases.txt', 'r').readlines()
f0 = open('sqlitedatabases-size.txt', 'w')
for line in f:
    line = line.replace('\n','')
    sz = os.path.getsize(line)
    sz=str(sz)
    f0.write(line+', '+sz+'\n')
f0.close() 


# get the size of a list of files
#getting a list is easy  locate *.db >>sqlitedatabases.txt
#print there list
f0 = open('sqlitedatabases-size.txt', 'r').readlines()
for line in f0:
    line = line.replace('\n','')
    line = line.split(', ')
    if int(line[1]) > int(1004135424):
        print line[0]
        print line[1]
#SNIPPETS 450.5kb = 405504      4 398 080   pointillist.db 1004135424

#/home/conda/Desktop/NoteBooks/ssl/SQLite-8a4e1988/test/fuzzdata1.db
!ls /home/conda/Desktop/NoteBooks/ssl/SQLite-8a4e1988/test

from math import sin, cos
x=140
y=240
z=236
i=2
#print sin(x*y)+sin(y*z)+sin(z*x)
print int(abs((cos(x**2-cos(y)-x+y**2)))*200)

from math import sin
x=-240
y=-240
z=-236
i=2
#print sin(x*y)+sin(y*z)+sin(z*x)
print int(abs((cos(x**2-cos(y)-x+y**2)))*200)

from math import sin
x=20
y=20
z=26
i=2
#print sin(x*y)+sin(y*z)+sin(z*x)
int(abs((cos(x**2-cos(y)-x+y**2)))*200)

1.02476410846
2.24526658171

#%%writefile ImageEffectsBot.py
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageChops 
import os
import sys
import markovify
sys.path.insert(0,"/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
import time
nap=randint(10,400)
time.sleep(nap)
path = r"publish/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)


def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]
        #textin = (generate_the_word("wordcloud.txt"))


base = Image.open(filename0).convert('RGBA')
 

txt = Image.new('RGBA', base.size, (255,255,255,0))
def generate_the_word(infile):
    with open(infile) as f:
            contents_of_file = f.read()
    lines = contents_of_file.splitlines()
    line_number = random.randrange(0, len(lines))
    return lines[line_number]
    

#base = Image.open('images/NewFolder/lightning01.jpg').convert('RGBA')
#8 5 4 6 3 2
# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
# get a drawing context
d = ImageDraw.Draw(txt)

width, height = base.size
# calculate the x,y coordinates of the text
#marginx = 325
#marginy = 75
marginx = 225
marginy = 50
x = width - marginx
y = height - marginy
signature_ = "The TwitterBot Project" 
d.text((x,y), signature_, font=fnt, fill=(0,0,0,256))

out = Image.alpha_composite(base, txt)
out.save("tmp/tmp.jpg", "JPEG")
# save the image then reopen to put a title
base = Image.open('tmp/tmp.jpg').convert('RGBA')
#8 5 4 6 3 2
# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 50)
# get a drawing context
d = ImageDraw.Draw(txt)

width, height = base.size
# calculate the x,y coordinates of the text
#marginx = 325
#marginy = 75
x = 90
y = 10
#generate a title
title = (generate_the_word("titles.txt"))
d.text((x,y), "Python Stuff" , font=fnt, fill=(0,0,0,250))
out2 = Image.alpha_composite(base, txt)
out2.save("tmp/TM_POST.jpg", "JPEG")

filenameP = time.strftime("posted/%Y%m%d%H%M%S.jpg")
out2.save(filenameP, "JPEG")
#removed keys for privacy reasons
CONSUMER_KEY = 'YazCRIfWX4VICiRCOiph08jDL'
CONSUMER_SECRET = 'QOkLHou6NMwkghSHjMFXMdffQKJlDzttKtP6uBCcZ4VlQtvJyc'
ACCESS_KEY = '296906916-AWggjhqpEWIS7EzXXhc2pOPBeCVJczpOm11cQGIf'
ACCESS_SECRET = 'zFrCiyaPt8gCBVVs1bLCmdCSyQQ3DKxT5wHJq2tOu2AMj'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#path = 'images/NewFolder'
f = open("art.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
#http://paulbourke.net/fractals/
STR = (text_model.make_short_sentence(140))
#STR = ("#All_in_One - #WordCloud #Create - Added ability to randomly choose an image background  #Automated")
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "tmp/TM_POST.jpg"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])


import random
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageChops 
import os
import sys
import time
count = 0
while count < 180:
    path = r"/home/jack/Desktop/pycode/vpython2/TrigonometryBot/images/"
    base_image = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    filename0=(path+base_image)

    path0 = r"/home/jack/Desktop/pycode/vpython2/TrigonometryBot/images/"
    base_image0 = random.choice([
        x0 for x0 in os.listdir(path0)
        if os.path.isfile(os.path.join(path0, x0))
    ])
    filename00=(path0+base_image0)



    im0 = Image.open(filename0)
    im1 = im0.resize((640,640), Image.NEAREST)

    im01 = Image.open(filename00)
    im2 = im01.resize((640,640), Image.NEAREST)
    result1 = ImageChops.lighter(im1, im2) 
    filename = time.strftime("build/%Y%m%d%H%M%S.jpg")
    result1.save(filename)
    time.sleep(3)
    count= count +1

import random
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageChops 
import os
import sys
import time
count = 0
while count < 124:
    path = r"/home/jack/Desktop/pycode/vpython2/TrigonometryBot/-images/"
    base_image = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    filename0=(path+base_image)

    path0 = r"/home/jack/Desktop/pycode/vpython2/TrigonometryBot/-images/"
    base_image0 = random.choice([
        x0 for x0 in os.listdir(path0)
        if os.path.isfile(os.path.join(path0, x0))
    ])
    filename00=(path0+base_image0)



    im0 = Image.open(filename0)
    im1 = im0.resize((640,640), Image.NEAREST)

    im01 = Image.open(filename00)
    im2 = im01.resize((640,640), Image.NEAREST)
    
    result1 = ImageChops.screen(im1, im2) 
    
    filename = time.strftime("experiment/%Y%m%d%H%M%S.jpg")
    result1.save(filename)
    time.sleep(3)
    count= count +1

import random
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageChops 
import os
import sys
import time
count = 0
while count < 154:
    path = r"/home/jack/Desktop/pycode/vpython2/TrigonometryBot/-images/"
    base_image = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    filename0=(path+base_image)

    path0 = r"/home/jack/Desktop/pycode/vpython2/TrigonometryBot/-images/"
    base_image0 = random.choice([
        x0 for x0 in os.listdir(path0)
        if os.path.isfile(os.path.join(path0, x0))
    ])
    filename00=(path0+base_image0)



    im0 = Image.open(filename0)
    im1 = im0.resize((640,640), Image.NEAREST)

    im01 = Image.open(filename00)
    im2 = im01.resize((640,640), Image.NEAREST)
    
    result1 = ImageChops.blend(im1, im2, .5) 
    
    filename = time.strftime("blend/%Y%m%d%H%M%S.jpg")
    result1.save(filename)
    time.sleep(3)
    count= count +1

import random
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageChops 
import os
import sys
import time
count = 0
while count < 24:
    path = r"/home/jack/Desktop/pycode/vpython2/TrigonometryBot/images/"
    base_image = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    filename0=(path+base_image)

    path0 = r"/home/jack/Desktop/pycode/vpython2/TrigonometryBot/images/"
    base_image0 = random.choice([
        x0 for x0 in os.listdir(path0)
        if os.path.isfile(os.path.join(path0, x0))
    ])
    filename00=(path0+base_image0)



    im0 = Image.open(filename0)
    im1 = im0.resize((640,640), Image.NEAREST)

    im01 = Image.open(filename00)
    im2 = im01.resize((640,640), Image.NEAREST)
    
    result1 = ImageChops.blend(im1, im2, .5) 
    
    filename = time.strftime("blend/%Y%m%d%H%M%S.jpg")
    result1.save(filename)
    time.sleep(3)
    count= count +1

!locate TrigonometryBot

!rm /home/jack/Desktop/pycode/vpython2/TrigonometryBot/-images/image_68704131938.png

from PIL import Image, ImageDraw, ImageFont, ImageChops 
help(ImageChops)

import random
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageChops 
import os
import sys



path = r"/home/jack/Desktop/pycode/vpython2/TrigonometryBot/images/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)

path0 = r"/home/jack/Desktop/pycode/vpython2/TrigonometryBot/images/"
base_image0 = random.choice([
    x0 for x0 in os.listdir(path0)
    if os.path.isfile(os.path.join(path0, x0))
])
filename00=(path0+base_image0)








print filename0,filename00

!mkdir publish


print filename

import random
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageChops 
import os
import sys
import time
path = r"/home/jack/Desktop/pycode/vpython2/TrigonometryBot/images/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)

path0 = r"/home/jack/Desktop/pycode/vpython2/TrigonometryBot/images/"
base_image0 = random.choice([
    x0 for x0 in os.listdir(path0)
    if os.path.isfile(os.path.join(path0, x0))
])
filename00=(path0+base_image0)



im0 = Image.open(filename0)
im1 = im0.resize((640,640), Image.NEAREST)

im01 = Image.open(filename00)
im2 = im01.resize((640,640), Image.NEAREST)
result1 = ImageChops.lighter(im1, im2) 
filename = time.strftime("build/%Y%m%d%H%M%S.jpg")
result1.save(filename)


!ls build

%%writefile ImageEffectsBot
#!/bin/bash

while true; do
    python ImageEffectsBot.py
    echo "posted :"
    date
    sleep 1800s
done

#!/anaconda2/bin/python
import os
import random
import sys
import markovify
sys.path.insert(0, '/home/jack/Desktop/pycode/vpython2')
import twython
from twython import Twython
import random
import time
SLEEP_INTERVAL = random.randint(90,200)
time.sleep(SLEEP_INTERVAL)
#removed keys for privacy reasons
CONSUMER_KEY = 'YazCRIfWX4VICiRCOiph08jDL'
CONSUMER_SECRET = 'QOkLHou6NMwkghSHjMFXMdffQKJlDzttKtP6uBCcZ4VlQtvJyc'
ACCESS_KEY = '296906916-AWggjhqpEWIS7EzXXhc2pOPBeCVJczpOm11cQGIf'
ACCESS_SECRET = 'zFrCiyaPt8gCBVVs1bLCmdCSyQQ3DKxT5wHJq2tOu2AMj'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
path = '/home/jack/Desktop/deep-dream-generator/notebooks/test'
count = 0
file_list = []
for filename in os.listdir(path):
        count = count+1
        file_list.append(filename)

rnd = random.randint(0,count)
with open("art.txt") as f:
    text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters

STR = (text_model.make_short_sentence(140))

#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')
photo = open('post/'+file_list[rnd],'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])

#%%writefile ImageEffectsBot.py
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageChops 
import os
import sys
import markovify
sys.path.insert(0,"/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
import time
#nap=randint(10,400)
#time.sleep(nap)
path = r"publish/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)


def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]
        #textin = (generate_the_word("wordcloud.txt"))


base = Image.open(filename0).convert('RGBA')
 

txt = Image.new('RGBA', base.size, (255,255,255,0))
def generate_the_word(infile):
    with open(infile) as f:
            contents_of_file = f.read()
    lines = contents_of_file.splitlines()
    line_number = random.randrange(0, len(lines))
    return lines[line_number]
    

#base = Image.open('images/NewFolder/lightning01.jpg').convert('RGBA')
#8 5 4 6 3 2
# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
# get a drawing context
d = ImageDraw.Draw(txt)

width, height = base.size
# calculate the x,y coordinates of the text
#marginx = 325
#marginy = 75
marginx = 225
marginy = 50
x = width - marginx
y = height - marginy
signature_ = "The TwitterBot Project" 
d.text((x,y), signature_, font=fnt, fill=(0,0,0,256))

out = Image.alpha_composite(base, txt)
out.save("tmp/tmp.jpg", "JPEG")
# save the image then reopen to put a title
base = Image.open('tmp/tmp.jpg').convert('RGBA')
#8 5 4 6 3 2
# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 50)
# get a drawing context
d = ImageDraw.Draw(txt)

width, height = base.size
# calculate the x,y coordinates of the text
#marginx = 325
#marginy = 75
x = 90
y = 10
#generate a title
title = (generate_the_word("titles.txt"))
d.text((x,y), title , font=fnt, fill=(0,0,0,250))
out2 = Image.alpha_composite(base, txt)
out2.save("tmp/TM_POST.jpg", "JPEG")

filenameP = time.strftime("posted/%Y%m%d%H%M%S.jpg")
out2.save(filenameP, "JPEG")
#removed keys for privacy reasons
CONSUMER_KEY = 'YazCRIfWX4VICiRCOiph08jDL'
CONSUMER_SECRET = 'QOkLHou6NMwkghSHjMFXMdffQKJlDzttKtP6uBCcZ4VlQtvJyc'
ACCESS_KEY = '296906916-AWggjhqpEWIS7EzXXhc2pOPBeCVJczpOm11cQGIf'
ACCESS_SECRET = 'zFrCiyaPt8gCBVVs1bLCmdCSyQQ3DKxT5wHJq2tOu2AMj'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#path = 'images/NewFolder'
f = open("art.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
#http://paulbourke.net/fractals/
STR = (text_model.make_short_sentence(140))
#STR = ("#All_in_One - #WordCloud #Create - Added ability to randomly choose an image background  #Automated")
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "tmp/TM_POST.jpg"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

#photo = open(PATH,'rb')
#response = twitter.upload_media(media=photo)
#twitter.update_status(status=STR, media_ids=[response['media_id']])
out2

#%%writefile ImageEffectsBot.py
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
from random import randint
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
import os
import sys
import markovify
sys.path.insert(0,"/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
import time
#nap=randint(10,400)
#time.sleep(nap)
path = r"publish/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)


def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]
        #textin = (generate_the_word("wordcloud.txt"))


base = Image.open(filename0).convert('RGBA')
 

txt = Image.new('RGBA', base.size, (255,255,255,0))
def generate_the_word(infile):
    with open(infile) as f:
            contents_of_file = f.read()
    lines = contents_of_file.splitlines()
    line_number = random.randrange(0, len(lines))
    return lines[line_number]







def draw_text_with_halo(img, position, text, font, col, halo_col):
    halo = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(position, text, font = font, fill = halo_col)
    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(position, text, font = font, fill = col)
    return Image.composite(img, blurred_halo, ImageChops.invert(blurred_halo))











#base = Image.open('images/NewFolder/lightning01.jpg').convert('RGBA')
#8 5 4 6 3 2
# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
# get a drawing context
#d = ImageDraw.Draw(txt)




width, height = base.size
# calculate the x,y coordinates of the text
#marginx = 325
#marginy = 75
marginx = 225
marginy = 50
x = width - marginx
y = height - marginy
signature_ = "The TwitterBot Project" 
d.text((x,y), signature_, font=fnt, fill=(0,0,0,256))

out = Image.alpha_composite(base, txt)
out.save("tmp/tmp.jpg", "JPEG")
# save the image then reopen to put a title
#base = Image.open('tmp/tmp.jpg').convert('RGBA')


if __name__ == '__main__':
    img0 = Image.open('tmp/tmp.jpg').convert('RGBA')
    font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 50)
    txt = 'The TwitterBot Project'
    text_col = (0, 0,0) # bright green
    halo_col = (255,255,255)   # black
    i2 = draw_text_with_halo(img0, (90, 10), txt, font, text_col, halo_col)



#8 5 4 6 3 2
# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 30)
# get a drawing context
#d = ImageDraw.Draw(txt)
d= draw_text_with_halo(img0, (90, 10), txt, font, text_col, halo_col)
width, height = base.size
# calculate the x,y coordinates of the text
#marginx = 325
#marginy = 75
x = 90
y = 10
#generate a title
title = (generate_the_word("titles.txt"))
d.text((x,y), title , font=fnt, fill=(0,0,0,250))
out2 = Image.alpha_composite(base, i2)
out2.save("tmp/TM_POST.jpg", "JPEG")

filenameP = time.strftime("posted/%Y%m%d%H%M%S.jpg")
out2.save(filenameP, "JPEG")
#removed keys for privacy reasons
CONSUMER_KEY = 'YazCRIfWX4VICiRCOiph08jDL'
CONSUMER_SECRET = 'QOkLHou6NMwkghSHjMFXMdffQKJlDzttKtP6uBCcZ4VlQtvJyc'
ACCESS_KEY = '296906916-AWggjhqpEWIS7EzXXhc2pOPBeCVJczpOm11cQGIf'
ACCESS_SECRET = 'zFrCiyaPt8gCBVVs1bLCmdCSyQQ3DKxT5wHJq2tOu2AMj'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#path = 'images/NewFolder'
f = open("art.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
#http://paulbourke.net/fractals/
STR = (text_model.make_short_sentence(140))
#STR = ("#All_in_One - #WordCloud #Create - Added ability to randomly choose an image background  #Automated")
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "tmp/TM_POST.jpg"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

#photo = open(PATH,'rb')
#response = twitter.upload_media(media=photo)
#twitter.update_status(status=STR, media_ids=[response['media_id']])
out2

import sys
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
path = r"publish/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)
def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]

def draw_text_with_halo(img, position, text, font, col, halo_col):
    halo = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(position, text, font = font, fill = halo_col)
    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(position, text, font = font, fill = col)
    return Image.composite(img, blurred_halo, ImageChops.invert(blurred_halo))

if __name__ == '__main__':
    i = Image.open(filename0)
    font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 50)
    text_col = (255, 255,230) # bright green
    halo_col = (0, 0, 0)   # black
    textin = (generate_the_word("wordcloud.txt"))
    i2 = draw_text_with_halo(i, (20, 20), textin, font, text_col, halo_col)
    
    txt = Image.new('RGBA', base.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 30)
    # get a drawing context
    d = ImageDraw.Draw(txt)
    
    width, height = i.size
    marginx = 325
    marginy = 50
    x = width - marginx
    y = height - marginy
    signature_ = "The TwitterBot Project" 
    d.text((x,y), signature_, font=fnt, fill=(0,0,0,256))

    out = Image.alpha_composite(i2, txt)

    filename = time.strftime("tmp/%Y%m%d%H%M%S.jpg")


out

out.save(filename)

%%writefile titlenpost.py
#!/home/jack/anaconda2/python
import random
from random import randint
import time
import markovify
import os
import sys
sys.path.insert(1, "/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
nap = randint(10,35)
time.sleep(nap)
path = r"publish/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)
def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]

def draw_text_with_halo(img, position, text, font, col, halo_col):
    halo = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(position, text, font = font, fill = halo_col)
    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(position, text, font = font, fill = col)
    return Image.composite(img, blurred_halo, ImageChops.invert(blurred_halo))

if __name__ == '__main__':
    inp = Image.open(filename0)
    font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 40)
    text_col = (255, 255,230) # bright green
    halo_col = (0, 0, 0)   # black
    textin = (generate_the_word("wordcloud.txt"))
    i2 = draw_text_with_halo(inp, (15, 8), textin, font, text_col, halo_col)
    
    #txt = Image.new('RGBA', i.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
    # get a drawing context
    width, height = inp.size
    marginx = 225
    marginy = 35
    x = width - marginx
    y = height - marginy
    signature_ = "The TwitterBot Project" 
    #text_col2 = (150, 255, 150) # bright green
    #halo_col2 = (0, 0, 0)   # black
    text_col2 = (255, 255,230) # bright green
    halo_col2 = (0, 0, 0)   # black
    txt=draw_text_with_halo(i2,(x,y), signature_, fnt, text_col2, halo_col2)
    out = Image.alpha_composite(i2, txt)
    out.save("tmp/TM_POST.jpg")

#removed keys for privacy reasons
CONSUMER_KEY = 'YazCRIfWX4VICiRCOiph08jDL'
CONSUMER_SECRET = 'QOkLHou6NMwkghSHjMFXMdffQKJlDzttKtP6uBCcZ4VlQtvJyc'
ACCESS_KEY = '296906916-AWggjhqpEWIS7EzXXhc2pOPBeCVJczpOm11cQGIf'
ACCESS_SECRET = 'zFrCiyaPt8gCBVVs1bLCmdCSyQQ3DKxT5wHJq2tOu2AMj'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#path = 'images/NewFolder'
f = open("art.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
#http://paulbourke.net/fractals/
STR = (text_model.make_short_sentence(140))
#STR = ("#All_in_One - #WordCloud #Create - Added ability to randomly choose an image background  #Automated")
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "tmp/TM_POST.jpg"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])

#%%writefile titlenpost2.py
#!/home/jack/anaconda2/python
import sys
import random
from random import randint
import time
import markovify
import os
import sys
sys.path.insert(1, "/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
nap = randint(10,35)
time.sleep(nap)
path = r"publish/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)
def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]

def draw_text_with_halo(img, position, text, font, col, halo_col):
    halo = Image.new('RGBA', tit.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(position, text, font = font, fill = halo_col)
    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(position, text, font = font, fill = col)
    return Image.composite(img, blurred_halo, ImageChops.invert(blurred_halo))

if __name__ == '__main__':
    tit = Image.open(filename0)
    font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 50)
    #textin = 'Python Generated'
    text_col = (255, 255,230) # bright green
    halo_col = (0, 0, 0)   # black
    textin = (generate_the_word("wordcloud.txt"))
    i2 = draw_text_with_halo(tit, (20, 10), textin, font, text_col, halo_col)
    txt = Image.new('RGBA', tit.size, (255,255,255,0))
    # get a font
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 30)
    # get a drawing context
    d = ImageDraw.Draw(txt)
    
    width, height = tit.size
    marginx = 325
    marginy = 50
    x = width - marginx
    y = height - marginy
    out = Image.alpha_composite(i2, txt)
    out.save("tmp/TM_XXX.jpg", "JPEG")
    
    signature_ = "The TwitterBot Project"
    #i3 = draw_text_with_halo( out, (x,y), signature_, font, text_col, halo_col)
    #out = Image.alpha_composite(i3, out)
    

filenameP = time.strftime("posted/%Y%m%d%H%M%S.jpg")
out.save(filenameP, "JPEG")
#removed keys for privacy reasons
CONSUMER_KEY = 'YazCRIfWX4VICiRCOiph08jDL'
CONSUMER_SECRET = 'QOkLHou6NMwkghSHjMFXMdffQKJlDzttKtP6uBCcZ4VlQtvJyc'
ACCESS_KEY = '296906916-AWggjhqpEWIS7EzXXhc2pOPBeCVJczpOm11cQGIf'
ACCESS_SECRET = 'zFrCiyaPt8gCBVVs1bLCmdCSyQQ3DKxT5wHJq2tOu2AMj'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#path = 'images/NewFolder'
f = open("art.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
#http://paulbourke.net/fractals/
STR = (text_model.make_short_sentence(140))
#STR = ("#All_in_One - #WordCloud #Create - Added ability to randomly choose an image background  #Automated")
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "tmp/TM_POST.jpg"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

#photo = open(PATH,'rb')
#response = twitter.upload_media(media=photo)
#twitter.update_status(status=STR, media_ids=[response['media_id']])
out



!ls

%%writefile titles.txt
Python Fun
Python Graphics
Generator
Word Cloud
Graphics
Fun w/Python
Python Stuff
PYTHON !!!
Love`en Python
Creative Python
Graphic Fun
ImageBot
Programming

%%writefile wordcloud.txt
Python
Programming
ImageBot
Enjoy
Just for You
Good Stuff
Computer Graphics
Python Fun
Python Graphics
Generator
Word Cloud
Graphics
Fun w/Python
Python Stuff
PYTHON !!!
Love`en Python
Creative Python
Graphic Fun
ImageBot
Programming

%%writefile titlenpost
#!/bin/bash

while true; do
  python titlenpost.py
  echo "posted :"
  date
  sleep 1800s
done



import sys
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
path = r"publish/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)
def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]

def draw_text_with_halo(img, position, text, font, col, halo_col):
    halo = Image.new('RGBA', i.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(position, text, font = font, fill = halo_col)
    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(position, text, font = font, fill = col)
    return Image.composite(img, blurred_halo, ImageChops.invert(blurred_halo))

if __name__ == '__main__':
    i = Image.open(filename0)
    font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 50)
    text_col = (255, 255,230) # bright green
    halo_col = (0, 0, 0)   # black
    textin = (generate_the_word("wordcloud.txt"))
    i2 = draw_text_with_halo(i, (20, 20), textin, font, text_col, halo_col)
    
    txt = Image.new('RGBA', i.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 30)
    # get a drawing context
    d = ImageDraw.Draw(txt)
    
    width, height = i.size
    marginx = 325
    marginy = 50
    x = width - marginx
    y = height - marginy
    signature_ = "The TwitterBot Project" 
    d.text((x,y), signature_, font=fnt, fill=(0,0,0,256))

    out = Image.alpha_composite(i2, txt)

    #filename = time.strftime("tmp/%Y%m%d%H%M%S.jpg")
    
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
    button_draw.text((x,y), text, font=font2)
    opacity=0.5
    bands=list(button_img.split())
    if len(bands)==4:
        bands[3]=bands[3].point(lambda x:x*opacity)
        new_image=Image.merge(button_img.mode,bands)
    # put button on source image in position (0, 0)
    out.paste(new_image, (15,15))
    # save in new file
    #source_img.save("junk/output.jpg", "JPEG")
    #source_img    

    
        
    
    
    
    
    
    
    


out

#Great title n signature

#Great signature
import sys
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
path = r"publish/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)
def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]

def draw_text_with_halo(img, position, text, font, col, halo_col):
    halo = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(position, text, font = font, fill = halo_col)
    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(position, text, font = font, fill = col)
    return Image.composite(img, blurred_halo, ImageChops.invert(blurred_halo))

if __name__ == '__main__':
    inp = Image.open(filename0)
    font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 40)
    text_col = (255, 255,230) # bright green
    halo_col = (0, 0, 0)   # black
    textin = (generate_the_word("wordcloud.txt"))
    i2 = draw_text_with_halo(inp, (15, 8), textin, font, text_col, halo_col)
    
    #txt = Image.new('RGBA', i.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
    # get a drawing context
    d = ImageDraw.Draw(txt)
    width, height = inp.size
    marginx = 225
    marginy = 35
    x = width - marginx
    y = height - marginy
    signature_ = "The TwitterBot Project" 
    #text_col2 = (150, 255, 150) # bright green
    #halo_col2 = (0, 0, 0)   # black
    text_col2 = (255, 255,230) # bright green
    halo_col2 = (0, 0, 0)   # black
    txt=draw_text_with_halo(i2,(x,y), signature_, fnt, text_col2, halo_col2)
    out = Image.alpha_composite(i2, txt)
    filename = time.strftime("tmp/%Y%m%d%H%M%S.jpg")


out



#%%writefile titlenpost.py
#!/home/jack/anaconda2/python
import random
from random import randint
import time
import markovify
import os
import sys
sys.path.insert(1, "/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
nap = randint(10,35)
time.sleep(nap)
path = r"publish/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)
def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]

def draw_text_with_halo(img, position, text, font, col, halo_col):
    halo = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(position, text, font = font, fill = halo_col)
    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(position, text, font = font, fill = col)
    return Image.composite(img, blurred_halo, ImageChops.invert(blurred_halo))

if __name__ == '__main__':
    inp = Image.open(filename0)
    font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 40)
    text_col = (255, 255,230) # bright green
    halo_col = (0, 0, 0)   # black
    textin = (generate_the_word("wordcloud.txt"))
    i2 = draw_text_with_halo(inp, (15, 8), textin, font, text_col, halo_col)
    
    #txt = Image.new('RGBA', i.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
    # get a drawing context
    width, height = inp.size
    marginx = 225
    marginy = 35
    x = width - marginx
    y = height - marginy
    signature_ = "The TwitterBot Project" 
    #text_col2 = (150, 255, 150) # bright green
    #halo_col2 = (0, 0, 0)   # black
    text_col2 = (255, 255,230) # bright green
    halo_col2 = (0, 0, 0)   # black
    txt=draw_text_with_halo(i2,(x,y), signature_, fnt, text_col2, halo_col2)
    out = Image.alpha_composite(i2, txt)
    out.save("tmp/TM_POST.jpg")

#removed keys for privacy reasons
CONSUMER_KEY = 'YazCRIfWX4VICiRCOiph08jDL'
CONSUMER_SECRET = 'QOkLHou6NMwkghSHjMFXMdffQKJlDzttKtP6uBCcZ4VlQtvJyc'
ACCESS_KEY = '296906916-AWggjhqpEWIS7EzXXhc2pOPBeCVJczpOm11cQGIf'
ACCESS_SECRET = 'zFrCiyaPt8gCBVVs1bLCmdCSyQQ3DKxT5wHJq2tOu2AMj'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#path = 'images/NewFolder'
f = open("art.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
#http://paulbourke.net/fractals/
STR = (text_model.make_short_sentence(140))
#STR = ("#All_in_One - #WordCloud #Create - Added ability to randomly choose an image background  #Automated")
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "tmp/TM_POST.jpg"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

#photo = open(PATH,'rb')
#response = twitter.upload_media(media=photo)
#twitter.update_status(status=STR, media_ids=[response['media_id']])
out

%%writefile titlenpost.py
#!/home/jack/anaconda2/python
import random
from random import randint
import time
import markovify
import os
import sys
sys.path.insert(1, "/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
nap = randint(10,35)
time.sleep(nap)
path = r"publish/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)
def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]

def draw_text_with_halo(img, position, text, font, col, halo_col):
    halo = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(position, text, font = font, fill = halo_col)
    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(position, text, font = font, fill = col)
    return Image.composite(img, blurred_halo, ImageChops.invert(blurred_halo))

if __name__ == '__main__':
    inp = Image.open(filename0)
    font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 40)
    text_col = (255, 255,230) # bright green
    halo_col = (0, 0, 0)   # black
    textin = (generate_the_word("wordcloud.txt"))
    i2 = draw_text_with_halo(inp, (15, 8), textin, font, text_col, halo_col)
    
    #txt = Image.new('RGBA', i.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
    # get a drawing context
    width, height = inp.size
    marginx = 225
    marginy = 35
    x = width - marginx
    y = height - marginy
    signature_ = "The TwitterBot Project" 
    #text_col2 = (150, 255, 150) # bright green
    #halo_col2 = (0, 0, 0)   # black
    text_col2 = (255, 255,230) # bright green
    halo_col2 = (0, 0, 0)   # black
    txt=draw_text_with_halo(i2,(x,y), signature_, fnt, text_col2, halo_col2)
    out = Image.alpha_composite(i2, txt)
    out.save("tmp/TM_POST.jpg")

#removed keys for privacy reasons
CONSUMER_KEY = 'YazCRIfWX4VICiRCOiph08jDL'
CONSUMER_SECRET = 'QOkLHou6NMwkghSHjMFXMdffQKJlDzttKtP6uBCcZ4VlQtvJyc'
ACCESS_KEY = '296906916-AWggjhqpEWIS7EzXXhc2pOPBeCVJczpOm11cQGIf'
ACCESS_SECRET = 'zFrCiyaPt8gCBVVs1bLCmdCSyQQ3DKxT5wHJq2tOu2AMj'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#path = 'images/NewFolder'
f = open("art.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
#http://paulbourke.net/fractals/
STR = (text_model.make_short_sentence(140))
#STR = ("#All_in_One - #WordCloud #Create - Added ability to randomly choose an image background  #Automated")
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "tmp/TM_POST.jpg"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])


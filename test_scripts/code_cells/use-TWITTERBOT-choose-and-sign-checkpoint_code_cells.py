%%writefile use-TWITTERBOT-choose-and-sign.py
#!/home/jack/miniconda3/envs/cloned_base/bin/python
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageFilter 
import os
import sys
import markovify
import twython
from twython import Twython
import time
import shutil
# Open background image and work out centre

path = r"publish/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)


bg = Image.open(filename0).convert('RGB')
x = bg.width//2
y = bg.height//2

# The text we want to add
text = "NFT TwitterBot Project"

# Create font
font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 40)

# Create piece of canvas to draw text on and blur
blurred = Image.new('RGBA', bg.size)
draw = ImageDraw.Draw(blurred)
draw.text(xy=(x,y+190), text=text, fill='black', font=font, anchor='mm')
blurred = blurred.filter(ImageFilter.BoxBlur(7))
src_path = filename0
dst_path = "Processed-Images/"
shutil.move(src_path, dst_path)
# Paste soft text onto background
bg.paste(blurred,blurred)

# Draw on sharp text
draw = ImageDraw.Draw(bg)
draw.text(xy=(x,y+190), text=text, fill='white', font=font, anchor='mm')
#xx=0
#yy=0
#bg.paste("peferations.png", (xx,yy)) 
# paste an onerlay image
#perferations.png
#mask=Image.open("perferations.png").convert('RGBA') 
#bg.paste(mask, (x,y), mask=mask)
#bg.paste("peferations.png", box=(0, 0) + original.size) 
bg.save('result.png')
timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "records/"+timestr+"_.png"
bg.save(filename)
im =Image.open('result.png')
im



#nap=randint(10,400)
#time.sleep(nap)
path = r"publish/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename1=(path+base_image)

bg = Image.open(filename1).convert('RGB')
x = bg.width//2
y = bg.height//2
src_path = filename1
dst_path = "Processed-Images/"
shutil.move(src_path, dst_path)
# The text we want to add
text = "NFT TwitterBot Project"


# Create font
font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 40)

# Create piece of canvas to draw text on and blur
blurred = Image.new('RGBA', bg.size)
draw = ImageDraw.Draw(blurred)
draw.text(xy=(x,y+190), text=text, fill='black', font=font, anchor='mm')
blurred = blurred.filter(ImageFilter.BoxBlur(7))

# Paste soft text onto background
bg.paste(blurred,blurred)

# Draw on sharp text
draw = ImageDraw.Draw(bg)
draw.text(xy=(x,y+190), text=text, fill='white', font=font, anchor='mm')
postage = ["perferations.png","perferations+.png","usa-perferations.png","usar-perferations.png","usal-perferations.png"]
Num = randint( 0, len(postage)-1)
BOARDER = postage[Num]
mask=Image.open(BOARDER).convert('RGBA') 
bg.paste(mask, (0,0), mask=mask)
bg.save('result.png')
#removed keys for privacy reasons
CONSUMER_KEY = 'APIkey()[0]'
CONSUMER_SECRET = 'APIkey()[1]'
ACCESS_KEY = 'APIkey()[2]'
ACCESS_SECRET = 'APIkey()[3]'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#path = 'images/NewFolder'
with open("sart.txt") as f:
    data = f.read()
data_model = markovify.Text(data)
STR = data_model.make_sentence()
#STR = ("#All_in_One - #WordCloud #Create - Added ability to randomly choose an image background  #Automated")
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
#PATH = "images/TM_POST.png"
PATH = "result.png"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])


import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageChops 
import os
import sys
import markovify
import twython
from twython import Twython
import time

%%writefile ImageBot
#!/bin/bash

while true; do
    python ImageBot.py
    echo "posted :"
    date
    sleep 1800s
done

from IPython.display import Image as showme
from PIL import Image
im = Image.open("result.png")
im




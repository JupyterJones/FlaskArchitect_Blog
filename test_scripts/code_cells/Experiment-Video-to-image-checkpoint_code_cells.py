import cv2
import numpy as np
import time
import random
import os
from random import randint
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from skimage import io
from randtext import randTXT
STR = randTXT()
#print (STR)
import cv2
from PIL import Image
import time
import random
randomframes = []
def vid2img(filename, count):
    vidcap = cv2.VideoCapture(filename)
    # get total number of frames
    totalFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)

    randomFrameNumber=random.randint(0, totalFrames)
    randomframes.append(randomFrameNumber)
    # set frame position
    vidcap.set(cv2.CAP_PROP_POS_FRAMES,randomFrameNumber)
    success, image = vidcap.read()
    if success:
        print(".",end="|")
        cv2.imwrite("junk/archived-images.jpg", image)
    IM = Image.open("junk/archived-images.jpg")
    im = IM.resize((720,480))
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "onevid/"+str(count)+".jpg"

    im.save(filename)
    nim = Image.open(filename)
    #print(nim.size)
    return nim

filename ="/home/jack/Desktop/dockercommands/complete-videos/24sept-output-slow-3per-sec-jpgs.mp4"
for count in range(0,3):
    vid2img(filename, count)
    
print(randomframes)    

def creatmased(count):
    dim = (720, 480)
    
    img1 = cv2.imread("onevid/0.jpg")
    im1 = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)

    img2 = cv2.imread(images[1])
    im2 = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)
    # read saliency mask as grayscale and resize to same size as img1
    
    mask = io.imread("onevid/1.jpg")
    #conn = cv2.imread(images[2])
    #cv2.imwrite("onevid/3.jpg", conn)
    mask = io.imread(images[2])
    mask = cv2.imread("onevid/2.jpg")
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    mask = cv2.resize(mask, dim, interpolation = cv2.INTER_AREA)

    # add img1 and img2
    img12 = cv2.add(img1, img2)

    # get mean of mask and shift mean to mid-gray
    # desirable for hard light compositing
    # add bias as needed
    mean = np.mean(mask)
    bias = -32
    shift = 128 - mean + bias
    mask = cv2.add(mask, shift)
    mask = cv2.merge([mask,mask,mask])

    # threshold mask at mid gray and convert to 3 channels
    # (needed to use as src < 0.5 "if" condition in hard light)
    thresh = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)[1]

    # do hard light composite of img12 and mask
    # see CSS specs at https://www.w3.org/TR/compositing-1/#blendinghardlight
    img12f = img12.astype(np.uint8)/255
    maskf =  mask.astype(np.uint8)/255
    threshf =  thresh.astype(np.uint8)/255
    threshf_inv = 1 - threshf
    low = 2.0 * img12f * maskf
    high = 1 - 2.0 * (1-img12f) * (1-maskf)
    result = ( 255 * (low * threshf_inv + high * threshf) ).clip(0, 255).astype(np.uint8)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    file = "onevid/"+timestr+"_"+str(count)+".png"
    cv2.imwrite(file, result)
    cv2.imwrite("onevid/temp.png", result)
    text = "NFT TwitterBot Project"
    text = STR
    # Create font
    font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/\
    truetype/dejavu/DejaVuSans-Bold.ttf', 15)
    # Create piece of canvas to draw text on and blur
    imgsize = Image.open("onevid/temp.png")
    
    ##overlay ="/home/jack/Desktop/dockercommands/toplayer/3020220925140724.png"
    #mask=Image.open(overlay)#.convert('RGBA')
    #imgsize.paste(mask, (0,0), mask=mask)  
    #overlay ="/home/jack/Desktop/dockercommands/toplayer/14320220925140747.png"
    #overlay ="/home/jack/Desktop/dockercommands/toplayer/23620220925140804.png"
    #mask=Image.open(overlay).convert('RGBA')
    #imgsize.paste(mask, (0,0), mask=mask)      
    
    
    
    
    x = imgsize.width//2
    y = imgsize.height//2
    blurred = Image.new('RGBA', imgsize.size)
    draw = ImageDraw.Draw(blurred)
    draw.text(xy=(x,y+130), text=text, fill='white', font=font, anchor='mm')
    blurred = blurred.filter(ImageFilter.BoxBlur(7))
    # Paste soft text onto background
    imgsize.paste(blurred,blurred)
    # Draw on sharp text
    draw = ImageDraw.Draw(imgsize)
    draw.text(xy=(x,y+130), text=text, fill='black', font=font, anchor='mm') 
    postage = ["perferations.png","perferations+.png","usa-perferations.png","usar-perferations.png","usal-perferations.png"]
    Num = randint( 0, len(postage)-1)
    BOARDER = postage[Num]
    
    
    #overlay ="/home/jack/Desktop/dockercommands/toplayer/4020220925140726.png"
    #mask=Image.open(overlay).convert('RGBA')
    #imgsize.paste(mask, (0,0), mask=mask)  
    
    
    
    mask=Image.open(BOARDER).convert('RGBA') 
    imgsize.paste(mask, (0,0), mask=mask)
    # save results
    timestr = time.strftime("%Y%m%d-%H%M%S")
    file = "onevid/"+timestr+"_"+str(count+1)+".png"
    imgsize.save(file)
    imgsize.save("onevid/temp.png")
    #im = Image.open(filename)
    #im
#for count in range(0,1500):
count = 1
creatmased(count)
print(count,end=".")

from PIL import Image
im = Image.open("onevid/temp.png")
im

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
from randtext import randTXT
STR2 = randTXT()

STR2 = "#Python #100DaysOfCode #PythonBots \n"+STR
print(STR2)
# Open background image and work out centre
#removed keys for privacy reasons
CONSUMER_KEY = 'APIkey()[0]'
CONSUMER_SECRET = 'APIkey()[1]'
ACCESS_KEY = 'APIkey()[2]'
ACCESS_SECRET = 'APIkey()[3]'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
PATH = "onevid/temp.png"
#PATH = "Screenshot_2022-09-29_23-06-02.png"
photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])








import cv2
import numpy as np
import time
import random
import os
from random import randint
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from skimage import io
from randtext import randTXT
STR = randTXT()
#print (STR)
import cv2
from PIL import Image
import time
import random
randomframes = []
def vid2img(filename, count):
    vidcap = cv2.VideoCapture(filename)
    # get total number of frames
    totalFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)

    randomFrameNumber=random.randint(0, totalFrames)
    randomframes.append(randomFrameNumber)
    # set frame position
    vidcap.set(cv2.CAP_PROP_POS_FRAMES,randomFrameNumber)
    success, image = vidcap.read()
    if success:
        print(".",end="|")
        cv2.imwrite("junk/archived-images.jpg", image)
    IM = Image.open("junk/archived-images.jpg")
    im = IM.resize((720,480))
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "onevid/"+str(count)+".jpg"

    im.save(filename)
    nim = Image.open(filename)
    #print(nim.size)
    return nim

filename ="/home/jack/Desktop/dockercommands/complete-videos/24sept-output-slow-3per-sec-jpgs.mp4"
for count in range(0,3):
    vid2img(filename, count)
    
print(randomframes)    

def creatmased(count):
    dim = (720, 480)
    
    img1 = cv2.imread("onevid/0.jpg")
    im1 = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)

    img2 = cv2.imread(images[1])
    im2 = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)
    # read saliency mask as grayscale and resize to same size as img1
    
    mask = io.imread("onevid/1.jpg")
    #conn = cv2.imread(images[2])
    #cv2.imwrite("onevid/3.jpg", conn)
    mask = io.imread(images[2])
    mask = cv2.imread("onevid/2.jpg")
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    mask = cv2.resize(mask, dim, interpolation = cv2.INTER_AREA)

    # add img1 and img2
    img12 = cv2.add(img1, img2)

    # get mean of mask and shift mean to mid-gray
    # desirable for hard light compositing
    # add bias as needed
    mean = np.mean(mask)
    bias = -32
    shift = 128 - mean + bias
    mask = cv2.add(mask, shift)
    mask = cv2.merge([mask,mask,mask])

    # threshold mask at mid gray and convert to 3 channels
    # (needed to use as src < 0.5 "if" condition in hard light)
    thresh = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)[1]

    # do hard light composite of img12 and mask
    # see CSS specs at https://www.w3.org/TR/compositing-1/#blendinghardlight
    img12f = img12.astype(np.uint8)/255
    maskf =  mask.astype(np.uint8)/255
    threshf =  thresh.astype(np.uint8)/255
    threshf_inv = 1 - threshf
    low = 2.0 * img12f * maskf
    high = 1 - 2.0 * (1-img12f) * (1-maskf)
    result = ( 255 * (low * threshf_inv + high * threshf) ).clip(0, 255).astype(np.uint8)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    file = "onevid/"+timestr+"_"+str(count)+".png"
    cv2.imwrite(file, result)
    cv2.imwrite("onevid/temp.png", result)
    text = "NFT TwitterBot Project"
    text = STR
    # Create font
    font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/\
    truetype/dejavu/DejaVuSans-Bold.ttf', 15)
    # Create piece of canvas to draw text on and blur
    imgsize = Image.open("onevid/temp.png")
    x = imgsize.width//2
    y = imgsize.height//2
    blurred = Image.new('RGBA', imgsize.size)
    draw = ImageDraw.Draw(blurred)
    draw.text(xy=(x,y+130), text=text, fill='white', font=font, anchor='mm')
    blurred = blurred.filter(ImageFilter.BoxBlur(7))
    # Paste soft text onto background
    imgsize.paste(blurred,blurred)
    # Draw on sharp text
    draw = ImageDraw.Draw(imgsize)
    draw.text(xy=(x,y+130), text=text, fill='black', font=font, anchor='mm') 
    postage = ["perferations.png","perferations+.png","usa-perferations.png","usar-perferations.png","usal-perferations.png"]
    Num = randint( 0, len(postage)-1)
    BOARDER = postage[Num]
    overlay ="/home/jack/Desktop/dockercommands/toplayer/3020220925140724.png"
    mask=Image.open(overlay).convert('RGBA')
    imgsize.paste(mask, (0,0), mask=mask)  
    
    
    mask=Image.open(BOARDER).convert('RGBA') 
    imgsize.paste(mask, (0,0), mask=mask)
    

    
    
    # save results
    timestr = time.strftime("%Y%m%d-%H%M%S")
    file = "onevid/"+timestr+"_"+str(count+1)+".png"
    imgsize.save(file)
    imgsize.save("onevid/temp.png")
    #im = Image.open(filename)
    #im
#for count in range(0,1500):
count = 1
creatmased(count)
print(count,end=".")

from PIL import Image
im = Image.open("onevid/temp.png")
im

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
from randtext import randTXT
STR2 = randTXT()

STR2 = "#Python #100DaysOfCode #PythonBots \n"+STR
print(STR2)
# Open background image and work out centre
#removed keys for privacy reasons
CONSUMER_KEY = 'APIkey()[0]'
CONSUMER_SECRET = 'APIkey()[1]'
ACCESS_KEY = 'APIkey()[2]'
ACCESS_SECRET = 'APIkey()[3]'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
PATH = "onevid/temp.png"
photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])


https://towardsdatascience.com/making-plots-in-jupyter-notebook-beautiful-more-meaningful-23c8a35c0d5d
https://www.geeksforgeeks.org/python-working-with-png-images-using-matplotlib/
https://swcarpentry.github.io/python-novice-gapminder/09-plotting/index.html

!mkdir onevid

import random
for i in range(5):
    # Any number can be used in place of '0'.
    random.seed(0) 
    # Generated random number will be between 1 to 1000.
    print(random.randint(1, 1000)) 

jpg

import cv2
from PIL import Image
import time
import random
randomframes = []
def vid2img(filename, count):
    vidcap = cv2.VideoCapture(filename)
    # get total number of frames
    totalFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)

    randomFrameNumber=random.randint(0, totalFrames)
    randomframes.append(randomFrameNumber)
    # set frame position
    vidcap.set(cv2.CAP_PROP_POS_FRAMES,randomFrameNumber)
    success, image = vidcap.read()
    if success:
        print(".",end="|")
        cv2.imwrite("junk/archived-images.jpg", image)
    IM = Image.open("junk/archived-images.jpg")
    im = IM.resize((720,480))
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "onevid/"+str(count)+".jpg"

    im.save(filename)
    nim = Image.open(filename)
    #print(nim.size)
    return nim

filename ="/home/jack/Desktop/dockercommands/complete-videos/24sept-output-slow-3per-sec-jpgs.mp4"
for count in range(0,3):
    vid2img(filename, count)
    
print(randomframes)    

from PIL import Image
im = Image.open((images[0]))
im

from PIL import Image
im = Image.open((images[1]))
im

from PIL import Image
im = Image.open(images[2])
im

from randtext import randTXT
STR = randTXT()
print (STR)

!ls onevid/

!ls onevid



from VID2img import vid2img
vid2img()

!ls *.py

!ls onevid

import glob

%load_ext autoreload
%autoreload 2
%reload_ext autoreload
import ipyplot
import glob
datasets_dir ="onevid"
images = glob.glob(datasets_dir +'/*.*')
images = [image.replace('\\', '/') for image in images]
print(images)

ipyplot.plot_images(images, max_images=20, img_width=150)
#plot_images.cla() 

datasets_dir ="onevid"
images = glob.glob(datasets_dir +'/*.*')
images = [image.replace('\\', '/') for image in images]



import cv2
import numpy as np
import time
import random
import os
from random import randint
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from skimage import io
from randtext import randTXT
STR = randTXT()
#print (STR)
import cv2
from PIL import Image
import time
import random
randomframes = []
count = 1
def vid2img(filename, count=0):
    vidcap = cv2.VideoCapture(filename)
    # get total number of frames
    totalFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)

    randomFrameNumber=random.randint(0, totalFrames)
    randomframes.append(randomFrameNumber)
    # set frame position
    vidcap.set(cv2.CAP_PROP_POS_FRAMES,randomFrameNumber)
    success, image = vidcap.read()
    if success:
        print(".",end="|")
        cv2.imwrite("junk/archived-images.jpg", image)
    IM = Image.open("junk/archived-images.jpg")
    im = IM.resize((720,480))
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "onevid/"+str(count)+".jpg"

    im.save(filename)
    nim = Image.open(filename)
    #print(nim.size)
    return nim

filename ="/home/jack/Desktop/dockercommands/complete-videos/24sept-output-slow-3per-sec-jpgs.mp4"
vid2img(filename,count=0)
    
dim = (720, 480)
    
img1 = cv2.imread("onevid/0.jpg")
im1 = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
img2 = cv2.imread(images[1])
im2 = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)
# read saliency mask as grayscale and resize to same size as img1
mask = io.imread("onevid/1.jpg")
#conn = cv2.imread(images[2])
#cv2.imwrite("onevid/3.jpg", conn)
mask = io.imread(images[2])
mask = cv2.imread("onevid/2.jpg")
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
mask = cv2.resize(mask, dim, interpolation = cv2.INTER_AREA)
# add img1 and img2
img12 = cv2.add(img1, img2)
# get mean of mask and shift mean to mid-gray
# desirable for hard light compositing
# add bias as needed
mean = np.mean(mask)
bias = -32
shift = 128 - mean + bias
mask = cv2.add(mask, shift)
mask = cv2.merge([mask,mask,mask])
# threshold mask at mid gray and convert to 3 channels
# (needed to use as src < 0.5 "if" condition in hard light)
thresh = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)[1]
# do hard light composite of img12 and mask
# see CSS specs at https://www.w3.org/TR/compositing-1/#blendinghardlight
img12f = img12.astype(np.uint8)/255
maskf =  mask.astype(np.uint8)/255
threshf =  thresh.astype(np.uint8)/255
threshf_inv = 1 - threshf
low = 2.0 * img12f * maskf
high = 1 - 2.0 * (1-img12f) * (1-maskf)
result = ( 255 * (low * threshf_inv + high * threshf) ).clip(0, 255).astype(np.uint8)
#
"""STR='''STR=\"timestr = time.strftime("%Y%m%d-%H%M%S")
file = "onevid/"+timestr+"_"+str(count)+".png"
cv2.imwrite(file, result)
cv2.imwrite("onevid/temp.png", result)
text = "NFT TwitterBot Project"
text = STR\"'''
"""
#
timestr = time.strftime("%Y%m%d-%H%M%S")
file = "onevid/"+timestr+"_"+str(count)+".png"
cv2.imwrite(file, result)
cv2.imwrite("onevid/temp.png", result)
text = "NFT TwitterBot Project"
text = STR
STR=STR.replace("  ","")
# Create font
font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/\
truetype/dejavu/DejaVuSans-Bold.ttf', 15)
# Create piece of canvas to draw text on and blur
imgsize = Image.open("onevid/temp.png")
##overlay ="/home/jack/Desktop/dockercommands/toplayer/3020220925140724.png"
#mask=Image.open(overlay)#.convert('RGBA')
#imgsize.paste(mask, (0,0), mask=mask)  
#overlay ="/home/jack/Desktop/dockercommands/toplayer/14320220925140747.png"
#overlay ="/home/jack/Desktop/dockercommands/toplayer/23620220925140804.png"
#mask=Image.open(overlay).convert('RGBA')
#imgsize.paste(mask, (0,0), mask=mask)      
x = imgsize.width//2
y = imgsize.height//2
blurred = Image.new('RGBA', imgsize.size)
draw = ImageDraw.Draw(blurred)
CH = randint(0,1)
if CH == 0:COLor = ["black","white"]
elif CH == 1:COLor = ["white","black"]
    
draw.text(xy=(x-20,y+130), text=text, fill=COLor[0], font=font, anchor='mm')
blurred = blurred.filter(ImageFilter.BoxBlur(7))
# Paste soft text onto background
imgsize.paste(blurred,blurred)
# Draw on sharp text
draw = ImageDraw.Draw(imgsize)
draw.text(xy=(x-20,y+130), text=text, fill=COLor[1], font=font, anchor='mm') 
postage = ["perferations.png","perferations+.png","usa-perferations.png","usar-perferations.png","usal-perferations.png"]
Num = randint( 0, len(postage)-1)
BOARDER = postage[Num]
#overlay ="/home/jack/Desktop/dockercommands/toplayer/4020220925140726.png"
#mask=Image.open(overlay).convert('RGBA')
#imgsize.paste(mask, (0,0), mask=mask)  
  
mask=Image.open(BOARDER).convert('RGBA') 
imgsize.paste(mask, (0,0), mask=mask)
# save results
timestr = time.strftime("%Y%m%d-%H%M%S")
file = "onevid/"+timestr+"_"+str(count+1)+".png"
imgsize.save(file)
imgsize.save("onevid/temp.png")
#im = Image.open(filename)
#im
#for count in range(0,1500):
#removed keys for privacy reasons
CONSUMER_KEY = 'APIkey()[0]'
CONSUMER_SECRET = 'APIkey()[1]'
ACCESS_KEY = 'APIkey()[2]'
ACCESS_SECRET = 'APIkey()[3]'
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#path = 'images/NewFolder'
PATH = "onevid/temp.png"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')
#photo = open(PATH,'rb')
#response = twitter.upload_media(media=photo)
#twitter.update_status(status=STR, media_ids=[response['media_id']])


from PIL import Image
im = Image.open("onevid/temp.png")
im





import cv2
import numpy as np
import time
import random
import os
from random import randint
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from skimage import io
from randtext import randTXT
STR = randTXT()
#print (STR)
import cv2
from PIL import Image
import time
import random
randomframes = []
def vid2img(filename, count):
    vidcap = cv2.VideoCapture(filename)
    # get total number of frames
    totalFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)

    randomFrameNumber=random.randint(0, totalFrames)
    randomframes.append(randomFrameNumber)
    # set frame position
    vidcap.set(cv2.CAP_PROP_POS_FRAMES,randomFrameNumber)
    success, image = vidcap.read()
    if success:
        print(".",end="|")
        cv2.imwrite("junk/archived-images.jpg", image)
    IM = Image.open("junk/archived-images.jpg")
    im = IM.resize((720,480))
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "onevid/"+str(count)+".jpg"

    im.save(filename)
    nim = Image.open(filename)
    #print(nim.size)
    return nim

filename ="/home/jack/Desktop/dockercommands/complete-videos/24sept-output-slow-3per-sec-jpgs.mp4"
for count in range(0,3):
    vid2img(filename, count)
    
print(randomframes)    

def creatmased(count):
    dim = (720, 480)
    
    img1 = cv2.imread("onevid/0.jpg")
    im1 = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)

    img2 = cv2.imread(images[1])
    im2 = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)
    # read saliency mask as grayscale and resize to same size as img1
    
    mask = io.imread("onevid/1.jpg")
    #conn = cv2.imread(images[2])
    #cv2.imwrite("onevid/3.jpg", conn)
    mask = io.imread(images[2])
    mask = cv2.imread("onevid/2.jpg")
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    mask = cv2.resize(mask, dim, interpolation = cv2.INTER_AREA)

    # add img1 and img2
    img12 = cv2.add(img1, img2)

    # get mean of mask and shift mean to mid-gray
    # desirable for hard light compositing
    # add bias as needed
    mean = np.mean(mask)
    bias = -32
    shift = 128 - mean + bias
    mask = cv2.add(mask, shift)
    mask = cv2.merge([mask,mask,mask])

    # threshold mask at mid gray and convert to 3 channels
    # (needed to use as src < 0.5 "if" condition in hard light)
    thresh = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)[1]

    # do hard light composite of img12 and mask
    # see CSS specs at https://www.w3.org/TR/compositing-1/#blendinghardlight
    img12f = img12.astype(np.uint8)/255
    maskf =  mask.astype(np.uint8)/255
    threshf =  thresh.astype(np.uint8)/255
    threshf_inv = 1 - threshf
    low = 2.0 * img12f * maskf
    high = 1 - 2.0 * (1-img12f) * (1-maskf)
    result = ( 255 * (low * threshf_inv + high * threshf) ).clip(0, 255).astype(np.uint8)
    #
    """STR='''STR=\"timestr = time.strftime("%Y%m%d-%H%M%S")
    file = "onevid/"+timestr+"_"+str(count)+".png"
    cv2.imwrite(file, result)
    cv2.imwrite("onevid/temp.png", result)
    text = "NFT TwitterBot Project"
    text = STR\"'''
    """
    
    
    
    
    #
    timestr = time.strftime("%Y%m%d-%H%M%S")
    file = "onevid/"+timestr+"_"+str(count)+".png"
    cv2.imwrite(file, result)
    cv2.imwrite("onevid/temp.png", result)
    text = "NFT TwitterBot Project"
    text = STR
    # Create font
    font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/\
    truetype/dejavu/DejaVuSans-Bold.ttf', 15)
    # Create piece of canvas to draw text on and blur
    imgsize = Image.open("onevid/temp.png")
    
    ##overlay ="/home/jack/Desktop/dockercommands/toplayer/3020220925140724.png"
    #mask=Image.open(overlay)#.convert('RGBA')
    #imgsize.paste(mask, (0,0), mask=mask)  
    #overlay ="/home/jack/Desktop/dockercommands/toplayer/14320220925140747.png"
    #overlay ="/home/jack/Desktop/dockercommands/toplayer/23620220925140804.png"
    #mask=Image.open(overlay).convert('RGBA')
    #imgsize.paste(mask, (0,0), mask=mask)      
    
    x = imgsize.width//2
    y = imgsize.height//2
    blurred = Image.new('RGBA', imgsize.size)
    draw = ImageDraw.Draw(blurred)
    CH = randint(0,1)
    if CH == 0:COLor = ["black","white"]
    elif CH == 1:COLor = ["white","black"]
    
    draw.text(xy=(x-20,y+130), text=text, fill=COLor[0], font=font, anchor='mm')
    blurred = blurred.filter(ImageFilter.BoxBlur(7))
    # Paste soft text onto background
    imgsize.paste(blurred,blurred)
    # Draw on sharp text
    draw = ImageDraw.Draw(imgsize)
    draw.text(xy=(x-20,y+130), text=text, fill=COLor[1], font=font, anchor='mm') 
    postage = ["perferations.png","perferations+.png","usa-perferations.png","usar-perferations.png","usal-perferations.png"]
    Num = randint( 0, len(postage)-1)
    BOARDER = postage[Num]
    
    
    #overlay ="/home/jack/Desktop/dockercommands/toplayer/4020220925140726.png"
    #mask=Image.open(overlay).convert('RGBA')
    #imgsize.paste(mask, (0,0), mask=mask)  
    
    
    
    mask=Image.open(BOARDER).convert('RGBA') 
    imgsize.paste(mask, (0,0), mask=mask)
    # save results
    timestr = time.strftime("%Y%m%d-%H%M%S")
    file = "onevid/"+timestr+"_"+str(count+1)+".png"
    imgsize.save(file)
    imgsize.save("onevid/temp.png")
    #im = Image.open(filename)
    #im
#for count in range(0,1500):
count = 1
creatmased(count)
print(count,end=".")



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
from randtext import randTXT
STR2 = randTXT()

STR2 = "#Python #100DaysOfCode #PythonBots \n"+STR
print(STR2)
# Open background image and work out centre
#removed keys for privacy reasons
CONSUMER_KEY = 'APIkey()[0]'
CONSUMER_SECRET = 'APIkey()[1]'
ACCESS_KEY = 'APIkey()[2]'
ACCESS_SECRET = 'APIkey()[3]'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
PATH = "onevid/temp.png"
#PATH = "Screenshot_2022-09-29_23-06-02.png"
photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])


CH = randint(0,1)
if CH == 0:COLor = ["black","white"]
elif CH == 1:COLor = ["white","black"]
#print(COLor[1],COLor[0])




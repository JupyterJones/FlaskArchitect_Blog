path = "."
files = (file for file in os.listdir(path) 
         if os.path.isfile(os.path.join(path, file)))
for file in files:
    if "." not in file:
        print(file)

import os 
for file in os.listdir("."):
    if "." not in file:
        print(file)

!ls *.py

filename = "mkimag.py"
f= open(filename, "r").readlines()
for line in f:
    line = line.replace("\n","")
    print (line)

filenam = "Tweetme2"
fn= open(filenam, "r").readlines()
for linen in fn:
    linen = linen.replace("\n","")
    print (linen)

#%%writefile Tweetme2
import cv2
import numpy as np
import time
import random
import twython
from twython import Twython
import shutil
import os
from random import randint
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from skimage import io
from randtext import randTXT
STR = randTXT()
#print (STR)
import cv2
from PIL import Image
randomframes = []
images=[]
count = 0
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
    images.append(filename)
    im.save(filename)
    nim = Image.open(filename)
    print(filename)
    return nim
#/home/jack/Desktop/dockercommands/complete-videos/24sept-output-slow-3per-sec-jpgs.mp4
#filename ="/home/jack/Desktop/dockercommands/complete-videos/24sept-output-slow-3per-sec-jpgs.mp4"
#filename ="/media/jack/HDD500/LinuxtoyboxVideos/test001.mp4"
filename ="/media/jack/HDD500/LinuxtoyboxVideos/Man_Ray_Style_Art_Video_Bot_Generated_Images_Us.mp4"
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
    cv2.imwrite("onevid/temp.png", img1)
    text = "NFT TwitterBot Project"
    
    # Create font
    font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/\
    truetype/dejavu/DejaVuSans-Bold.ttf', 18)
    # Create piece of canvas to draw text on and blur
    imgsize = Image.open("onevid/temp.png")
    imgsize=imgsize.resize((720,480), Image.NEAREST)
    bg= imgsize
    ##overlay ="/home/jack/Desktop/dockercommands/toplayer/3020220925140724.png"
    #mask=Image.open(overlay)#.convert('RGBA')
    #imgsize.paste(mask, (0,0), mask=mask)  
    #overlay ="/home/jack/Desktop/dockercommands/toplayer/14320220925140747.png"
    #overlay ="/home/jack/Desktop/dockercommands/toplayer/23620220925140804.png"
    #mask=Image.open(overlay).convert('RGBA')
    #imgsize.paste(mask, (0,0), mask=mask)      
    #STR = randTXT()
    Hash = ["#AIart #Tensorflow #twitme #100DaysOfCode\n",
            "#styletransfer #PythonGraphics #PIL\n",
            "#NFTartist #NFTProject #NEARnft #nearNFTs\n",
            "#NFT #NFTs #NFTCommunity #NFTdrop #nftart\n",
            "#CreativeCoding #AI #genart","#p5js #Generative\n",
            "#codefor30days #Python #100DaysOfCode\n",
            "#Python #100DaysOfCode #PythonBots #twitme\n"]
    hashnum = randint(0,len(Hash)-1)
    hashs =Hash[hashnum] 
    # add the hash to STR generated with randTXT()

    # Open background image and work out centre
    x = 720//2
    y = 480//2

    # The text we want to add
    #text = "NFT TwitterBot Project"
    text = hashs
    
    
    
    x = imgsize.width//2
    y = imgsize.height//2
    blurred = Image.new('RGBA', imgsize.size)
    draw = ImageDraw.Draw(blurred)
    """
    draw.text(xy=(x,y+230), text=text, fill='white', font=font, anchor='mm')
    draw.text(xy=(x,y+231), text=text, fill='white', font=font, anchor='mm')
    draw.text(xy=(x,y+232), text=text, fill='white', font=font, anchor='mm')
    draw.text(xy=(x,y+230), text=text, fill='white', font=font, anchor='mm')
    draw.text(xy=(x,y+231), text=text, fill='white', font=font, anchor='mm')
    draw.text(xy=(x,y+232), text=text, fill='white', font=font, anchor='mm')
    blurred = blurred.filter(ImageFilter.BoxBlur(2))
    # Paste soft text onto background
    imgsize.paste(blurred,blurred)
    # Draw on sharp text
    draw = ImageDraw.Draw(imgsize)
    draw.text(xy=(x,y+231), text=text, fill='black', font=font, anchor='mm') 
    """
    CH = randint(0,1)
    if CH == 0:COLor = ["white","black"]
    elif CH == 1:COLor = ["black","white"]  
    draw.text(xy=(x+20,y+230), text=text, fill=COLor[0], font=font, anchor='mm')
    draw.text(xy=(x+21,y+231), text=text, fill=COLor[0], font=font, anchor='mm')
    draw.text(xy=(x+22,y+229), text=text, fill=COLor[0], font=font, anchor='mm')
    draw.text(xy=(x+20,y+228), text=text, fill=COLor[0], font=font, anchor='mm')
    blurred = blurred.filter(ImageFilter.BoxBlur(2))
    # Paste soft text onto background
    bg.paste(blurred,blurred)
    # Draw on sharp text
    draw = ImageDraw.Draw(bg)
    draw.text(xy=(x+20,y+230), text=text, fill=COLor[1], font=font, anchor='mm')

    
    
    
    #postage = ["perferations.png","perferations+.png","usa-perferations.png","usar-perferations.png","usal-perferations.png"]
    #Num = randint( 0, len(postage)-1)
    #BOARDER = postage[Num]
    frames =["wood-blur-frame.png","frames.png","lined-frame.png","black-blur-frame.png", "white-blur-frame.png","beige-blur-frame.png","frame-lite.png"]
    Num = randint( 0, len(frames)-1)
    BOARDER = frames[Num]

    
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
    STR = randTXT()
    STR = hashs+STR
    STR= STR[:240]
    print(STR)
    return (STR)
#for count in range(0,1500):
count = 1
creatmased(count)
print(count,end=".")

from OutlineImage import outlineP
filename1 = "onevid/temp.png" 
outfile_png = "onevid/temp.png" 
outlineP(filename1,outfile_png)


CONSUMER_KEY = 'APIkey()[0]'
CONSUMER_SECRET = 'APIkey()[1]'
ACCESS_KEY = 'APIkey()[2]'
ACCESS_SECRET = 'APIkey()[3]'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
PATH = "onevid/temp.png"
#PATH = "Screenshot_2022-09-29_23-06-02.png"
photo = open(PATH,'rb')

Hash = ["#AIart #Tensorflow #twitme #100DaysOfCode\n",     
        "#styletransfer #PythonGraphics #PIL\n",
        "#NFTartist #NFTProject #NEARnft #nearNFTs\n",
        "#NFT #NFTs #NFTCommunity #NFTdrop #nftart\n",
        "#CreativeCoding #AI #genart","#p5js #Generative\n",
        "#codefor30days #Python #100DaysOfCode\n",
        "#Python #100DaysOfCode #PythonBots #twitme\n"]
hashnum = randint(0,len(Hash)-1)
hashs =Hash[hashnum] 
STR = randTXT()
STR = hashs+STR
STR= STR[:240]
print("STR: ",STR)
#response = twitter.upload_media(media=photo)
#twitter.update_status(status=STR, media_ids=[response['media_id']])


PATH = "onevid/temp.png"
from PIL import Image
im = Image.open(PATH)
im

response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])

%%writefile mkimag.py
#import Image and ImageEnhance modules
from PIL import Image, ImageEnhance, ImageChops
from random import randint
import random
import os
import time
import shutil
import cv2   
def mkimag(videofile):
    vidcap = cv2.VideoCapture(videofile)
    # get total number of frames
    cnt = 0
    totalFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    randomFrameNumber=random.randint(0, totalFrames)
    # set frame position
    vidcap.set(cv2.CAP_PROP_POS_FRAMES,randomFrameNumber)
    success, image = vidcap.read()
    if success:
           cv2.imwrite("junk/archived-images.jpg", image)
    IM = Image.open("junk/archived-images.jpg")
    im = IM.resize((720,480))
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "onevid/temp.jpg"
    im.save(filename)
    im = Image.open(filename)
    print(filename)
    im = im.resize((960,960), Image.ANTIALIAS)
    #print(im.size)
    Brighten = ImageEnhance.Brightness(im) # Create a Brightness class
    brightimage = Brighten.enhance(1.1)
    brightimage.save("junk/temp-brightened.jpg") # Save results
    im = Image.open("junk/temp-brightened.jpg") # Open the Image
    sharpened = ImageEnhance.Sharpness(im) # Create an object using Sharpness
    sharpenedimage = sharpened.enhance(1.1)
    sharpenedimage.save("junk/temp-sharpenedimage.jpg") # Save results
    im = Image.open('junk/temp-sharpenedimage.jpg') # Open the Image
    contrast = ImageEnhance.Contrast(im) # Create an object using Sharpness
    contrastedimage = contrast.enhance(1.1)
    contrastedimage.save('junk/temp-contrastedimage.jpg') # Save results
    im = Image.open("junk/temp-contrastedimage.jpg")
    width, height = im.size   # Get dimensions
    #im = im.resize((2*width,2*height), "Image.NEAREST" (0))
    #im = im.resize((2*width,2*height), Image.ANTIALIAS)
    Choose = ["insta-usa-perferations.png", "insta-philippines-perferations.png","insta-perferations.png"]
    num = randint(0,2)
    border = (Choose[num])
    mask=Image.open(border).convert('RGBA') 
    im.paste(mask, (0,0), mask=mask)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "junk/insta"+timestr+"_.jpg"
    im.save(filename)
    im.save('junk/temp1.jpg')
    return im
   


!ls /media/jack/HDD500/LinuxtoyboxVideos/

"/media/jack/HDD500/LinuxtoyboxVideos/Man_Ray_Style_Art_Video_Bot_Generated_Images_Us.mp4"

from mkimag import mkimag
videofile ="/media/jack/HDD500/LinuxtoyboxVideos/JACK.mp4"
im = mkimag(videofile)
im

!mkdir insta-posted

%%writefile videoimage.py
import cv2
from PIL import Image, ImageEnhance, ImageChops
from random import randint
import random
import os
import time
import shutil
def vid4img(filename):
    vidcap = cv2.VideoCapture(filename)
    # get total number of frames
    totalFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    randomFrameNumber=random.randint(0, totalFrames)
    # set frame position
    vidcap.set(cv2.CAP_PROP_POS_FRAMES,randomFrameNumber)
    success, image = vidcap.read()
    if success:
           cv2.imwrite("junk/archived-images.jpg", image)
    IM = Image.open("junk/archived-images.jpg")
    im = IM.resize((720,480))
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "onevid/"+str(count)+".jpg"
    im.save(filename)
    im = Image.open(filename)
    print(filename)
    return im

  

from videoimage import vid4img
filename ="/media/jack/HDD500/LinuxtoyboxVideos/Man_Ray_Style_Art_Video_Bot_Generated_Images_Us.mp4"
count = 1
file = vid4img(filename)
print (file)  

from PIL import Image
im = Image.open("onevid/1.jpg")
im

# %load InstaBot
#!/bin/bash

while true; do
  ./use-post-to-instagram.py
  echo "posted to instagram:"
  date
  sleep 3600s
done


from mkimag import mkimag
im = mkimag()


# %load use-post-to-instagram.py
#!/home/jack/miniconda3/envs/cloned_base/bin/python
from instabot import Bot
import os
import shutil
import markovify
from PIL import Image, ImageEnhance, ImageChops
from mkimag import mkimag
from randtext import randTXT
from time import sleep
from random import randint
STR = randTXT()
print(STR)
im = mkimag()


with open("sart.txt") as f:
    data = f.read()
data_model = markovify.Text(data)
#STR = data_model.make_sentence()



def clean_up(i):
    dir = "config"
    remove_me = "imgs\{}.REMOVE_ME".format(i)
    # checking whether config folder exists or not
    if os.path.exists(dir):
        try:
            # removing it so we can upload new image
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    if os.path.exists(remove_me):
        src = os.path.realpath("junk/{}".format(i))
        os.rename(remove_me, src)


def upload_post(i):
    bot = Bot()

    bot.login(username="jacklnorthrup", password="Pxyackjs22")
    bot.upload_photo("junk/{}".format(i), caption=STR)


#if __name__ == '__main__':
# enter name of your image bellow
image_name = "temp1.jpg"
clean_up(image_name)
upload_post(image_name)
tm = randint(1200,3800)
sleep(tm)
print("sleeping: ",tm, " seconds")
print(image_name)






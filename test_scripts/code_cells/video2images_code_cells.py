import os
os.chdir("/home/jack/Desktop/dockercommands")

#!/home/jack/miniconda3/envs/cloned_base/bin/python
import cv2
import numpy as np
import time
import random
import twython
from twython import Twython
import time
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
import time
import random
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
#filename ="/media/jack/HDD500/LinuxtoyboxVideos/Man_Ray_Style_Art_Video_Bot_Generated_Images_Us.mp4"
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

from PIL import Image
File = "onevid/temp.png"
viewim = Image.open(File)
viewim






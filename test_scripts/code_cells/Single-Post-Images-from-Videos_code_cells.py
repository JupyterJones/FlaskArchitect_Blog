import os
os.chdir('/home/jack/Desktop/dockercommands')
os.getcwd()



MOVIES=["/home/jack/Videos/vokoscreenNG-2022-09-29_21-50-38.mkv",
"/home/jack/Videos/Ogre_FULL_MOVIE_Monster_Movies_John_Schneider_The_Midnight_Screening.mp4",
"/home/jack/Videos/Alizée-EnConcertDVD-2004.mp4",
"/home/jack/Videos/FilipinaGirls.mp4",
"/home/jack/Videos/Britney_Spears-ALL_Pepsi_Commercials-Behind_the_Scenes-.mp4",
"/home/jack/Videos/USE.mp4",
"/media/jack/HDD500/complete-videos/Three-hours-of-Instagram-and-Twitter-Images-Generated-by-Bots.mp4",
"/media/jack/HDD500/complete-videos/2760-images-publish-archive.mp4",
"/media/jack/HDD500/complete-videos/24sept-output-slow-3per-sec-jpgs.mp4",
"/media/jack/HDD500/complete-videos/sep24-records-slow-3per-sec-pngs.mp4",
"/media/jack/HDD500/complete-videos/slow-3per-sec.mp4",
"/home/jack/Videos/new-vid-from-images.mp4",
"/media/jack/HDD500/complete-videos/output_2m-28sec.mp4"]        
        

from random import randint
vidid = randint(0,len(MOVIES)-1)
print(vidid)
print (MOVIES[vidid])

Hash = ["#Tensorflow #twitme #100DaysOfCode\n",
            "#styletransfer #PythonGraphics #PIL\n",
            "#NFTartist #NFTProject #twitme #nearNFTs\n",
            "#NFTs #NFTCommunity #NFTdrop #nftart\n",
            "#CreativeCoding #AI #p5js #Generative\n",
            "#codefor30days #Python #100DaysOfCode\n",
            "#AIart #genart #NFT #NEARnft\n",
            "#Python #100DaysOfCode #PythonBots\n",
            "#twitme #NFTProject #NFT\n"]
hashnum = randint(0,len(Hash)-1)
hashs = Hash[hashnum] 
print (hashs)

#!/home/jack/miniconda3/envs/cloned_base/bin/python
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
#import gettext
#STR = gettext.gettext()
#print (STR)
import cv2
from PIL import Image
from KEYS import TwitterKey

MOVIES=["/home/jack/Videos/vokoscreenNG-2022-09-29_21-50-38.mkv",
"/home/jack/Videos/Ogre_FULL_MOVIE_Monster_Movies_John_Schneider_The_Midnight_Screening.mp4",
"/home/jack/Videos/Alizée-EnConcertDVD-2004.mp4",
"/home/jack/Videos/FilipinaGirls.mp4",
"/home/jack/Videos/Britney_Spears-ALL_Pepsi_Commercials-Behind_the_Scenes-.mp4",
"/home/jack/Videos/USE.mp4",
"/media/jack/HDD500/complete-videos/Three-hours-of-Instagram-and-Twitter-Images-Generated-by-Bots.mp4",
"/media/jack/HDD500/complete-videos/2760-images-publish-archive.mp4",
"/media/jack/HDD500/complete-videos/24sept-output-slow-3per-sec-jpgs.mp4",
"/media/jack/HDD500/complete-videos/sep24-records-slow-3per-sec-pngs.mp4",
"/media/jack/HDD500/complete-videos/slow-3per-sec.mp4",
"/home/jack/Videos/new-vid-from-images.mp4",
"/media/jack/HDD500/complete-videos/output_2m-28sec.mp4"]        
        
        
reframe = []        
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
mvid=randint(0,len(MOVIES))-1
#/home/jack/Desktop/dockercommands/complete-videos/24sept-output-slow-3per-sec-jpgs.mp4
#filename ="/home/jack/Desktop/dockercommands/complete-videos/24sept-output-slow-3per-sec-jpgs.mp4"
filename = MOVIES[mvid]
filename="/media/jack/HDD500/complete-videos/vid-from-images2.mp4"
print("-------------------")
print ("Images Taken From Video: ",filename)
print("-------------------")
#filename ="/media/jack/HDD500/LinuxtoyboxVideos/Man_Ray_Style_Art_Video_Bot_Generated_Images_Us.mp4"
#filename ="/home/jack/Videos/fish-in-love.mp4"
for count in range(0,3):
    vid2img(filename, count)
print("\n-------------------")    
print("Image: onevid/0.jpg","randomframe number : ",randomframes[0])    
print("Image: onevid/1.jpg","randomframe number : ",randomframes[1])
print("Image: onevid/2.jpg","randomframe number : ",randomframes[2])
print("-------------------\n")
def creatmased(count):
    dim = (720, 480)
    
    img1 = cv2.imread("onevid/0.jpg")
    im1 = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)

    img2 = cv2.imread(images[1])
    im2 = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)
    # read saliency mask as grayscale and resize to same size as img1
    
    #mask = io.imread("onevid/1.jpg")
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
    timestr = time.strftime("%Y%m%d-%H%M%S")
    files = "onevid/mask"+timestr+"_"+str(count)+".png"
    cv2.imwrite(files, mask)
    # threshold mask at mid gray and convert to 3 channels
    # (needed to use as src < 0.5 "if" condition in hard light)
    thresh = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)[1]
    timestr = time.strftime("%Y%m%d-%H%M%S")
    files = "onevid/thresh"+timestr+"_"+str(count)+".png"
    cv2.imwrite(files, thresh)
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
    #cv2.imwrite("onevid/temp.png", img1)
    cv2.imwrite("onevid/temp.png", result)
    text = "NFT TwitterBot Project"
    
    # Create font
    font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/\
    truetype/dejavu/DejaVuSans-Bold.ttf', 18)
    # Create piece of canvas to draw text on and blur
    imgsize = Image.open("onevid/temp.png")
    imgsize=imgsize.resize((720,480), Image.NEAREST)
    
    ##overlay ="/home/jack/Desktop/dockercommands/toplayer/3020220925140724.png"
    #mask=Image.open(overlay)#.convert('RGBA')
    imgsize.paste(result, (0,0), mask=mask)  
    #overlay ="/home/jack/Desktop/dockercommands/toplayer/14320220925140747.png"
    #overlay ="/home/jack/Desktop/dockercommands/toplayer/23620220925140804.png"
    #mask=Image.open(overlay).convert('RGBA')
    #imgsize.paste(mask, (0,0), mask=mask)      
    #STR = randTXT()
    bg= imgsize
    Hash = ["#Tensorflow #twitme #100DaysOfCode\n",
            "#styletransfer #PythonGraphics #PIL\n",
            "#NFTartist #NFTProject #twitme #nearNFTs\n",
            "#NFTs #NFTCommunity #NFTdrop #nftart\n",
            "#CreativeCoding #AI #p5js #Generative\n",
            "#codefor30days #Python #100DaysOfCode\n",
            "#AIart #genart #NFT #NEARnft\n",
            "#Python #100DaysOfCode #PythonBots\n",
            "#twitme #NFTProject #NFT\n"]
    hashnum = randint(0,len(Hash)-1)
    hashs =Hash[hashnum] 
    # add the hash to STR generated with randTXT()

    # Open background image and work out centre
    x = 720//2
    y = 480//2

    # The text we want to add
    #text = "NFT TwitterBot Project"
    text = hashs
    print("Video Hash Overlay : ",text)
    
    
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
    draw.text(xy=(x+20,y+235), text=text, fill=COLor[0], font=font, anchor='mm')
    draw.text(xy=(x+21,y+236), text=text, fill=COLor[0], font=font, anchor='mm')
    draw.text(xy=(x+22,y+233), text=text, fill=COLor[0], font=font, anchor='mm')
    draw.text(xy=(x+20,y+234), text=text, fill=COLor[0], font=font, anchor='mm')
    blurred = blurred.filter(ImageFilter.BoxBlur(2))
    # Paste soft text onto background
    bg.paste(blurred,blurred)
    # Draw on sharp text
    draw = ImageDraw.Draw(bg)
    draw.text(xy=(x+20,y+234), text=text, fill=COLor[1], font=font, anchor='mm')

    
    
    
    #postage = ["perferations.png","perferations+.png","usa-perferations.png","usar-perferations.png","usal-perferations.png"]
    #Num = randint( 0, len(postage)-1)
    #BOARDER = postage[Num]
    frames =["frames/09-print.png","frames/08-print.png","frames/07-print.png","frames/06-print.png",\
              "frames/05-print.png","frames/04-print.png","frames/03-print.png","frames/02-print.png",\
              "frames/01-print.png","frames/rocks-print.png","frames/abstract-print.png",\
              "frames/leopard-print.png","frames/black-blur-frame.png","frames/golden-frame.png",\
              "frames/wood-blur-frame.png","frames/white-blur-frame.png","frames/frame-lite.png",\
              "frames/frames.png","frames/beige-blur-frame.png","frames/lined-frame.png",\
              "frames/usal-perferations.png","frames/usar-perferations.png",\
              "frames/usa-perferations.png","frames/perferations.png","frames/perferations+.png"]
    Num = randint( 0, len(frames)-1)
    BOARDER = frames[Num]
    print("BOARDER: ",BOARDER)
    
    #overlay ="/home/jack/Desktop/dockercommands/toplayer/4020220925140726.png"
    #mask=Image.open(overlay).convert('RGBA')
    #imgsize.paste(mask, (0,0), mask=mask)  
    
    
    
    mask=Image.open(BOARDER).convert('RGBA') 
    imgsize.paste(mask, (0,0), mask=mask)
    # save results
    timestr = time.strftime("%Y%m%d-%H%M%S")
    file = "onevid/"+timestr+"_"+str(count+1)+".png"
    reframe.append(file)
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


from OutlineImage import outlineP
filename1 = "onevid/temp.png" 
outfile_png = "onevid/temp.png" 
outlineP(filename1,outfile_png)

CONSUMER_KEY = TwitterKey()[0]
CONSUMER_SECRET = TwitterKey()[1]
ACCESS_KEY = TwitterKey()[2]
ACCESS_SECRET = TwitterKey()[3]

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
PATH = "onevid/temp.png"
#PATH = "/home/jack/Desktop/dockercommands/onevid/20221108-002618_2.png"
photo = open(PATH,'rb')

Hash = ["#Tensorflow #twitme #100DaysOfCode\n",
       "#styletransfer #PythonGraphics #PIL\n",
       "#NFTartist #NFTProject #twitme #nearNFTs\n",
       "#NFTs #NFTCommunity #NFTdrop #nftart\n",
       "#CreativeCoding #AI #p5js #Generative\n",
       "#codefor30days #Python #100DaysOfCode\n",
       "#AIart #genart #NFT #NEARnft\n",
       "#Python #100DaysOfCode #PythonBots\n",
       "#twitme #NFTProject #NFT\n"]
hashnum = randint(0,len(Hash)-1)
hashs =Hash[hashnum] 
STR = randTXT()
STR = hashs+STR
STR= STR[:240]
print("Status : ",STR)
im=Image.open(PATH)
im

#!/home/jack/miniconda3/envs/cloned_base/bin/python
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
#import gettext
#STR = gettext.gettext()
#print (STR)
import cv2
from PIL import Image
from KEYS import TwitterKey

MOVIES=["/home/jack/Videos/vokoscreenNG-2022-09-29_21-50-38.mkv",
"/home/jack/Videos/Ogre_FULL_MOVIE_Monster_Movies_John_Schneider_The_Midnight_Screening.mp4",
"/home/jack/Videos/Alizée-EnConcertDVD-2004.mp4",
"/home/jack/Videos/FilipinaGirls.mp4",
"/home/jack/Videos/Britney_Spears-ALL_Pepsi_Commercials-Behind_the_Scenes-.mp4",
"/home/jack/Videos/USE.mp4",
"/media/jack/HDD500/complete-videos/Three-hours-of-Instagram-and-Twitter-Images-Generated-by-Bots.mp4",
"/media/jack/HDD500/complete-videos/2760-images-publish-archive.mp4",
"/media/jack/HDD500/complete-videos/24sept-output-slow-3per-sec-jpgs.mp4",
"/media/jack/HDD500/complete-videos/sep24-records-slow-3per-sec-pngs.mp4",
"/media/jack/HDD500/complete-videos/slow-3per-sec.mp4",
"/home/jack/Videos/new-vid-from-images.mp4",
"/media/jack/HDD500/complete-videos/output_2m-28sec.mp4"]        
        
        
reframe = []        
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
mvid=randint(0,len(MOVIES))-1
#/home/jack/Desktop/dockercommands/complete-videos/24sept-output-slow-3per-sec-jpgs.mp4
#filename ="/home/jack/Desktop/dockercommands/complete-videos/24sept-output-slow-3per-sec-jpgs.mp4"
filename = MOVIES[mvid]
filename="/media/jack/HDD500/complete-videos/vid-from-images2.mp4"
print("-------------------")
print ("Images Taken From Video: ",filename)
print("-------------------")
#filename ="/media/jack/HDD500/LinuxtoyboxVideos/Man_Ray_Style_Art_Video_Bot_Generated_Images_Us.mp4"
#filename ="/home/jack/Videos/fish-in-love.mp4"
for count in range(0,3):
    vid2img(filename, count)
print("\n-------------------")    
print("Image: onevid/0.jpg","randomframe number : ",randomframes[0])    
print("Image: onevid/1.jpg","randomframe number : ",randomframes[1])
print("Image: onevid/2.jpg","randomframe number : ",randomframes[2])
print("-------------------\n")
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
    timestr = time.strftime("%Y%m%d-%H%M%S")
    files = "onevid/mask"+timestr+"_"+str(count)+".png"
    cv2.imwrite(files, mask)
    # threshold mask at mid gray and convert to 3 channels
    # (needed to use as src < 0.5 "if" condition in hard light)
    thresh = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)[1]
    timestr = time.strftime("%Y%m%d-%H%M%S")
    files = "onevid/thresh"+timestr+"_"+str(count)+".png"
    cv2.imwrite(files, thresh)
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
    #cv2.imwrite("onevid/temp.png", img1)
    cv2.imwrite("onevid/temp.png", result)
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
    Hash = ["#Tensorflow #twitme #100DaysOfCode\n",
            "#styletransfer #PythonGraphics #PIL\n",
            "#NFTartist #NFTProject #twitme #nearNFTs\n",
            "#NFTs #NFTCommunity #NFTdrop #nftart\n",
            "#CreativeCoding #AI #p5js #Generative\n",
            "#codefor30days #Python #100DaysOfCode\n",
            "#AIart #genart #NFT #NEARnft\n",
            "#Python #100DaysOfCode #PythonBots\n",
            "#twitme #NFTProject #NFT\n"]
    hashnum = randint(0,len(Hash)-1)
    hashs =Hash[hashnum] 
    # add the hash to STR generated with randTXT()

    # Open background image and work out centre
    x = 720//2
    y = 480//2

    # The text we want to add
    #text = "NFT TwitterBot Project"
    text = hashs
    print("Video Hash Overlay : ",text)
    
    
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
    draw.text(xy=(x+20,y+235), text=text, fill=COLor[0], font=font, anchor='mm')
    draw.text(xy=(x+21,y+236), text=text, fill=COLor[0], font=font, anchor='mm')
    draw.text(xy=(x+22,y+233), text=text, fill=COLor[0], font=font, anchor='mm')
    draw.text(xy=(x+20,y+234), text=text, fill=COLor[0], font=font, anchor='mm')
    blurred = blurred.filter(ImageFilter.BoxBlur(2))
    # Paste soft text onto background
    bg.paste(blurred,blurred)
    # Draw on sharp text
    draw = ImageDraw.Draw(bg)
    draw.text(xy=(x+20,y+234), text=text, fill=COLor[1], font=font, anchor='mm')

    
    
    
    #postage = ["perferations.png","perferations+.png","usa-perferations.png","usar-perferations.png","usal-perferations.png"]
    #Num = randint( 0, len(postage)-1)
    #BOARDER = postage[Num]
    frames =["frames/09-print.png","frames/08-print.png","frames/07-print.png","frames/06-print.png",\
              "frames/05-print.png","frames/04-print.png","frames/03-print.png","frames/02-print.png",\
              "frames/01-print.png","frames/rocks-print.png","frames/abstract-print.png",\
              "frames/leopard-print.png","frames/black-blur-frame.png","frames/golden-frame.png",\
              "frames/wood-blur-frame.png","frames/white-blur-frame.png","frames/frame-lite.png",\
              "frames/frames.png","frames/beige-blur-frame.png","frames/lined-frame.png",\
              "frames/usal-perferations.png","frames/usar-perferations.png",\
              "frames/usa-perferations.png","frames/perferations.png","frames/perferations+.png"]
    Num = randint( 0, len(frames)-1)
    BOARDER = frames[Num]
    print("BOARDER: ",BOARDER)
    
    #overlay ="/home/jack/Desktop/dockercommands/toplayer/4020220925140726.png"
    #mask=Image.open(overlay).convert('RGBA')
    #imgsize.paste(mask, (0,0), mask=mask)  
    
    
    
    mask=Image.open(BOARDER).convert('RGBA') 
    imgsize.paste(mask, (0,0), mask=mask)
    # save results
    timestr = time.strftime("%Y%m%d-%H%M%S")
    file = "onevid/"+timestr+"_"+str(count+1)+".png"
    reframe.append(file)
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


from OutlineImage import outlineP
filename1 = "onevid/temp.png" 
outfile_png = "onevid/temp.png" 
outlineP(filename1,outfile_png)

CONSUMER_KEY = TwitterKey()[0]
CONSUMER_SECRET = TwitterKey()[1]
ACCESS_KEY = TwitterKey()[2]
ACCESS_SECRET = TwitterKey()[3]

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
PATH = "onevid/temp.png"
#PATH = "/home/jack/Desktop/dockercommands/onevid/20221108-002618_2.png"
photo = open(PATH,'rb')

Hash = ["#Tensorflow #twitme #100DaysOfCode\n",
       "#styletransfer #PythonGraphics #PIL\n",
       "#NFTartist #NFTProject #twitme #nearNFTs\n",
       "#NFTs #NFTCommunity #NFTdrop #nftart\n",
       "#CreativeCoding #AI #p5js #Generative\n",
       "#codefor30days #Python #100DaysOfCode\n",
       "#AIart #genart #NFT #NEARnft\n",
       "#Python #100DaysOfCode #PythonBots\n",
       "#twitme #NFTProject #NFT\n"]
hashnum = randint(0,len(Hash)-1)
hashs =Hash[hashnum] 
STR = randTXT()
STR = hashs+STR
STR= STR[:240]
print("Status : ",STR)
im=Image.open(PATH)
im

response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])


!ls ~/hidden

from KEYS import TwitterKey
CONSUMER_KEY = TwitterKey()[0]
CONSUMER_SECRET = TwitterKey()[1]
ACCESS_KEY = TwitterKey()[2]
ACCESS_SECRET = TwitterKey()[3]




TXT="""/home/jack/Desktop/dockercommands/frames/09-print.png
/home/jack/Desktop/dockercommands/frames/08-print.png
/home/jack/Desktop/dockercommands/frames/07-print.png
/home/jack/Desktop/dockercommands/frames/06-print.png
/home/jack/Desktop/dockercommands/frames/05-print.png
/home/jack/Desktop/dockercommands/frames/04-print.png
/home/jack/Desktop/dockercommands/frames/03-print.png
/home/jack/Desktop/dockercommands/frames/02-print.png
/home/jack/Desktop/dockercommands/frames/01-print.png
/home/jack/Desktop/dockercommands/frames/rocks-print.png
/home/jack/Desktop/dockercommands/frames/abstract-print.png
/home/jack/Desktop/dockercommands/frames/leopard-print.png
/home/jack/Desktop/dockercommands/frames/black-blur-frame.png
/home/jack/Desktop/dockercommands/frames/golden-frame.png
/home/jack/Desktop/dockercommands/frames/wood-blur-frame.png
/home/jack/Desktop/dockercommands/frames/white-blur-frame.png
/home/jack/Desktop/dockercommands/frames/frame-lite.png
/home/jack/Desktop/dockercommands/frames/frames.png
/home/jack/Desktop/dockercommands/frames/beige-blur-frame.png
/home/jack/Desktop/dockercommands/frames/lined-frame.png
/home/jack/Desktop/dockercommands/frames/usal-perferations.png
/home/jack/Desktop/dockercommands/frames/usar-perferations.png
/home/jack/Desktop/dockercommands/frames/usa-perferations.png
/home/jack/Desktop/dockercommands/frames/perferations.png
/home/jack/Desktop/dockercommands/frames/perferations+.png
"""
for line in TXT.split("\n"):
    line=line.replace("/home/jack/Desktop/dockercommands/","")
    print("\""+line+"\"",end="," )

%%writefile reframepost.py
"""
Usage:
reframethis =reframe[0]
reframeit(reframethis)
"""
from random import randint
from PIL import Image
import PIL
import time
from KEYS import TwitterKey
import twython
from twython import Twython
from randtext import randTXT
STR = randTXT()
def reframeit(reframethis):
    print(reframethis)
    frames =["frames/09-print.png","frames/08-print.png","frames/07-print.png","frames/06-print.png","frames/05-print.png","frames/04-print.png","frames/03-print.png","frames/02-print.png","frames/01-print.png","frames/rocks-print.png","frames/abstract-print.png","frames/leopard-print.png","frames/black-blur-frame.png","frames/golden-frame.png","frames/wood-blur-frame.png","frames/white-blur-frame.png","frames/frame-lite.png","frames/frames.png","frames/beige-blur-frame.png","frames/lined-frame.png","frames/usal-perferations.png","frames/usar-perferations.png","frames/usa-perferations.png","frames/perferations.png","frames/perferations+.png"]
    Num = randint( 0, len(frames)-1)
    BOARDER = frames[Num]
    print("BOARDER: ",BOARDER)
           

    Hash = ["#Tensorflow #twitme #100DaysOfCode\n",
           "#styletransfer #PythonGraphics #PIL\n",
           "#NFTartist #NFTProject #twitme #nearNFTs\n",
           "#NFTs #NFTCommunity #NFTdrop #nftart\n",
           "#CreativeCoding #AI #p5js #Generative\n",
           "#codefor30days #Python #100DaysOfCode\n",
           "#AIart #genart #NFT #NEARnft\n",
           "#Python #100DaysOfCode #PythonBots\n",
           "#twitme #NFTProject #NFT\n"]
    hashnum = randint(0,len(Hash)-1)
    hashs =Hash[hashnum] 
           
           
    imgsize = PIL.Image.open(reframethis) 
    mask=Image.open(BOARDER).convert('RGBA') 
    imgsize.paste(mask, (0,0), mask=mask)
    # save results
    timestr = "onevid/"+time.strftime("%Y%m%d-%H%M%S")+".png"
    file = timestr
    imgsize.save(file)
    imgsize.save("onevid/temp.png")
    #im = Image.open(filename)
    #im
    STR = randTXT()
    STR = hashs+STR
    STR= STR[:240]
    print(STR)
    #for count in range(0,1500):
    count = 1
    creatmased(count)
    print(count,end=".")
    from OutlineImage import outlineP
    filename1 = "onevid/temp.png" 
    outfile_png = "onevid/temp.png" 
    outlineP(filename1,outfile_png)


    CONSUMER_KEY = TwitterKey()[0]
    CONSUMER_SECRET = TwitterKey()[1]
    ACCESS_KEY = TwitterKey()[2]
    ACCESS_SECRET = TwitterKey()[3]

    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
    PATH = "onevid/temp.png"
    #PATH = "/home/jack/Desktop/dockercommands/onevid/20221108-002618_2.png"
    photo = open(PATH,'rb')
    STR = randTXT()
    STR = hashs+STR
    STR= STR[:240]
    print("STR: ",STR)
    im=Image.open(PATH)
    return im    

!rm ~/miniconda3/envs/cloned_base/reframepost.py

from reframepost import reframeit
reframethis  = "onevid/20221108-101626_2.png"
reframeit(reframethis)

frames =["frames/golden-frame.png","frames/wood-blur-frame.png","frames/frames.png",\
         "frames/lined-frame.png","frames/black-blur-frame.png", \
         "frames/white-blur-frame.png","frames/beige-blur-frame.png","frames/frame-lite.png"]
Num = randint( 0, len(frames)-1)
BOARDER = frames[Num]
print("BOARDER: ",BOARDER)

from reframepost import reframeit
reframethis  = "onevid/20221108-101626_2.png"
reframeit(reframethis)

print(reframe[0])
frames =["frames/golden-frame.png","frames/wood-blur-frame.png","frames/frames.png","frames/lined-frame.png","frames/black-blur-frame.png", "frames/white-blur-frame.png","frames/beige-blur-frame.png","frames/frame-lite.png"]
Num = randint( 0, len(frames)-1)
BOARDER = frames[Num]
print("BOARDER: ",BOARDER)
    
#overlay ="/home/jack/Desktop/dockercommands/toplayer/4020220925140726.png"
#mask=Image.open(overlay).convert('RGBA')
#imgsize.paste(mask, (0,0), mask=mask)  
    
    
imgsize = Image.open(reframe[0]) 
mask=Image.open(BOARDER).convert('RGBA') 
imgsize.paste(mask, (0,0), mask=mask)
# save results
timestr = time.strftime("%Y%m%d-%H%M%S")
file = reframe[0]
imgsize.save(file)
imgsize.save("onevid/temp.png")
#im = Image.open(filename)
#im
STR = randTXT()
STR = hashs+STR
STR= STR[:240]
print(STR)
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
#PATH = "/home/jack/Desktop/dockercommands/onevid/20221108-002618_2.png"
photo = open(PATH,'rb')

Hash = ["#Tensorflow #twitme #100DaysOfCode\n",
       "#styletransfer #PythonGraphics #PIL\n",
       "#NFTartist #NFTProject #twitme #nearNFTs\n",
       "#NFTs #NFTCommunity #NFTdrop #nftart\n",
       "#CreativeCoding #AI #p5js #Generative\n",
       "#codefor30days #Python #100DaysOfCode\n",
       "#AIart #genart #NFT #NEARnft\n",
       "#Python #100DaysOfCode #PythonBots\n",
       "#twitme #NFTProject #NFT\n"]
hashnum = randint(0,len(Hash)-1)
hashs =Hash[hashnum] 
STR = randTXT()
STR = hashs+STR
STR= STR[:240]
print("STR: ",STR)
im=Image.open(PATH)
im    

!cp /home/jack/Desktop/dockercommands/onevid/20221107-181254_2.png /home/jack/Desktop/dockercommands/onevid/temp.png

import matplotlib.pyplot as plt
#from pysheds.grid import Grid
import pyproj
import numpy as np
import cv2
from skimage.util import view_as_blocks
from pathlib import Path
import georasters as gr
from geopandas.io import file
import cv2
from skimage.morphology import skeletonize

import tensorflow

no locator available for file '/pysheds-0.3.3-py3.9.egg/pysheds/_sgrid.py'


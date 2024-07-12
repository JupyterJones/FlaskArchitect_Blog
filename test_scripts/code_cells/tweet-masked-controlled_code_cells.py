import os 
os.chdir("/home/jack/Desktop/dockercommands")

from PIL import Image
import random
from random import randint
import time
import cv2
from PIL import ImageChops
dim = (720, 480)
def binarize(filein, fileout):
    # read the image file
    img = cv2.imread(filein, 2)
    ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # converting to its binary form
    bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(fileout, bw_img)
    output = fileout
    return output

path = r"/home/jack/Desktop/TENSORFLOW/images/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
    ])
file1=(path+base_image)
original = Image.open(file1).convert('RGB')
original = original.resize(dim, Image.NEAREST)
print("original.size",original.size)
print("------------------------")
path1 = r"/home/jack/Documents/jpg/720/"
base_image1 = random.choice([
    x for x in os.listdir(path1)
    if os.path.isfile(os.path.join(path1, x))
    ])
file2=(path1+base_image1)

background = Image.open(file2).convert('RGB')
background  = background.resize(dim, Image.NEAREST)
print("background.size",background.size)
print("------------------------")
path2 = r"/home/jack/Documents/jpg/720/"
base_image3 = random.choice([
   x for x in os.listdir(path2)
   if os.path.isfile(os.path.join(path2, x))
   ])
  
file3=(path2+base_image3)

path3 = r"/home/jack/Documents/jpg/720/"
base_image3 = random.choice([
   x for x in os.listdir(path3)
   if os.path.isfile(os.path.join(path3, x))
   ])
file4=(path3+base_image3)
   
filein=file1
filein=file2
filein=file3
#filein=file4
print("file1",file1)
print("file2",file2)
print("file3",file3)
print("file4",file4)
fileout = "junk/mask.png"
timestr = time.strftime("%Y%m%d-%H%M%S")
binarize(filein, fileout)
im = Image.open("junk/mask.png")
im.save("/home/jack/Desktop/TENSORFLOW/images/BINARY_"+timestr+"_.png")

#binarize(filein, fileout)
img = Image.open("junk/mask.png").convert('L')
img = ImageChops.invert(img)
dim = (720, 480)
mask =img.resize(dim, Image.NEAREST)


print("mask.size",mask.size)
result = Image.composite(original, background, mask)
result.save('resultmasked.png')
result.save('resultunlined.png')
timestr = time.strftime("%Y%m%d-%H%M%S")
filen = "onevid/"+timestr+"unlined.png"
result.save(filen)
from OutlineImage import outlineP
filename1 = "resultmasked.png" 
outfile_png = "resultmasked-outlined.png"
timestr = time.strftime("%Y%m%d-%H%M%S")
#outfile_png = "/home/jack/Desktop/TENSORFLOW/images/BINARY2"+timestr+"_.png"
outfile_png = "onevid/resultmasked-outlined.png"
outlineP(filename1,outfile_png)
result.save('onevid/resultunmasked.png')
result

outfile_png = "onevid/resultmasked-outlined.png"
im =Image.open(outfile_png)
im

from PIL import Image
import random
from random import randint
import time
import cv2
from PIL import ImageChops
dim = (720, 480)
def binarize(filein, fileout):
    # read the image file
    img = cv2.imread(filein, 2)
    ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # converting to its binary form
    bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(fileout, bw_img)
    output = fileout
    return output

path = r"/home/jack/Desktop/TENSORFLOW/images/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
    ])
file1=(path+base_image)
original = Image.open(file1).convert('RGB')
original = original.resize(dim, Image.NEAREST)
print("original.size",original.size)
print("------------------------")
path1 = r"/home/jack/Documents/jpg/720/"
base_image1 = random.choice([
    x for x in os.listdir(path1)
    if os.path.isfile(os.path.join(path1, x))
    ])
file2=(path1+base_image1)

background = Image.open(file2).convert('RGB')
background  = background.resize(dim, Image.NEAREST)
print("background.size",background.size)
print("------------------------")
path2 = r"/home/jack/Documents/jpg/720/"
base_image3 = random.choice([
   x for x in os.listdir(path2)
   if os.path.isfile(os.path.join(path2, x))
   ])
  
file3=(path2+base_image3)

path3 = r"/home/jack/Documents/jpg/720/"
base_image3 = random.choice([
   x for x in os.listdir(path3)
   if os.path.isfile(os.path.join(path3, x))
   ])
file4=(path3+base_image3)
   
filein=file1
filein=file2
filein=file3
#filein=file4
print("file1",file1)
print("file2",file2)
print("file3",file3)
print("file4",file4)
fileout = "junk/mask.png"
timestr = time.strftime("%Y%m%d-%H%M%S")
binarize(filein, fileout)
im = Image.open("junk/mask.png")
im.save("/home/jack/Desktop/TENSORFLOW/images/BINARY_"+timestr+"_.png")

#binarize(filein, fileout)
img = Image.open("junk/mask.png").convert('L')
img = ImageChops.invert(img)
dim = (720, 480)
mask =img.resize(dim, Image.NEAREST)


print("mask.size",mask.size)
result = Image.composite(original, background, mask)
result.save('resultmasked.png')
from OutlineImage import outlineP
filename1 = "resultmasked.png" 
outfile_png = "resultmasked-outlined.png"
timestr = time.strftime("%Y%m%d-%H%M%S")
#outfile_png = "/home/jack/Desktop/TENSORFLOW/images/BINARY2"+timestr+"_.png"
outfile_png = "onevid/resultmasked-outlined.png"
outlineP(filename1,outfile_png)


def creatmasked():   # Create font
    font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/\
    truetype/dejavu/DejaVuSans-Bold.ttf', 18)
    # Create piece of canvas to draw text on and blur
    imgsize = Image.open("/home/jack/Desktop/dockercommands/resultmasked.png")
    imgsize=imgsize.resize((720,480), Image.NEAREST)
    bg= imgsize
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
    bg.save("MAIN.png")
    
    filename1 = "onevid/temp.png" 

    
    #postage = ["perferations.png","perferations+.png","usa-perferations.png","usar-perferations.png","usal-perferations.png"]
    #Num = randint( 0, len(postage)-1)
    #BOARDER = postage[Num]
    frames =["frames/01-print.png","frames/abstract-print.png","frames/09-print.png",\
"frames/02-print.png","frames/beige-blur-frame.png","frames/rocks-print.png",\
"frames/03-print.png","frames/black-blur-frame.png","frames/lined-frame.png",\
"frames/04-print.png","frames/frame-lite.png","frames/08-print.png",\
"frames/05-print.png","frames/frames.png","frames/wood-blur-frame.png",\
"frames/06-print.png","frames/golden-frame.png","frames/white-blur-frame.png",\
"frames/07-print.png","frames/leopard-print.png"]
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

creatmasked()


from OutlineImage import outlineP
#filename1 = "onevid/temp.png" 
outfile_png = "onevid/temp.png" 
#outlineP(filename1,outfile_png)


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
im = Image.open(PATH)
im

def creatmasked():   # Create font
    font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/\
    truetype/dejavu/DejaVuSans-Bold.ttf', 18)
    # Create piece of canvas to draw text on and blur
    imgsize = Image.open("/home/jack/Desktop/dockercommands/resultmasked.png")
    imgsize=imgsize.resize((720,480), Image.NEAREST)
    bg= imgsize
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
    bg.save("MAIN.png")
    
    filename1 = "onevid/temp.png" 

    
    #postage = ["perferations.png","perferations+.png","usa-perferations.png","usar-perferations.png","usal-perferations.png"]
    #Num = randint( 0, len(postage)-1)
    #BOARDER = postage[Num]
    frames =["frames/01-print.png","frames/abstract-print.png","frames/09-print.png",\
"frames/02-print.png","frames/beige-blur-frame.png","frames/rocks-print.png",\
"frames/03-print.png","frames/black-blur-frame.png","frames/lined-frame.png",\
"frames/04-print.png","frames/frame-lite.png","frames/08-print.png",\
"frames/05-print.png","frames/frames.png","frames/wood-blur-frame.png",\
"frames/06-print.png","frames/golden-frame.png","frames/white-blur-frame.png",\
"frames/07-print.png","frames/leopard-print.png"]
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

creatmasked()


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
im = Image.open(PATH)
im

def creatmasked():   # Create font
    font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/\
    truetype/dejavu/DejaVuSans-Bold.ttf', 18)
    # Create piece of canvas to draw text on and blur
    imgsize = Image.open("/home/jack/Desktop/dockercommands/resultmasked.png")
    imgsize=imgsize.resize((720,480), Image.NEAREST)
    bg= imgsize
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
    bg.save("MAIN.png")
    
 
    from OutlineImage import outlineP
    filename1 = "MAIN.png" 
    outfile_png = "onevid/temp2.png"
    outlineP(filename1,outfile_png)
    
    #postage = ["perferations.png","perferations+.png","usa-perferations.png","usar-perferations.png","usal-perferations.png"]
    #Num = randint( 0, len(postage)-1)
    #BOARDER = postage[Num]
    frames =["frames/01-print.png","frames/abstract-print.png","frames/09-print.png",\
"frames/02-print.png","frames/beige-blur-frame.png","frames/rocks-print.png",\
"frames/03-print.png","frames/black-blur-frame.png","frames/lined-frame.png",\
"frames/04-print.png","frames/frame-lite.png","frames/08-print.png",\
"frames/05-print.png","frames/frames.png","frames/wood-blur-frame.png",\
"frames/06-print.png","frames/golden-frame.png","frames/white-blur-frame.png",\
"frames/07-print.png","frames/leopard-print.png"]
    Num = randint( 0, len(frames)-1)
    BOARDER = frames[Num]


    
    #overlay ="/home/jack/Desktop/dockercommands/toplayer/4020220925140726.png"
    #mask=Image.open(overlay).convert('RGBA')
    #imgsize.paste(mask, (0,0), mask=mask)  
    
    imgsize=Image.open("/home/jack/Desktop/dockercommands/onevid/temp2.png")
    
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

creatmasked()


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
im = Image.open(PATH)
im

response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])

from random import randint
Hash = ["#AIart #Tensorflow #twitme #100DaysOfCode\n",
       "#styletransfer #PythonGraphics #PIL\n",
       "#NFTartist #NFTProject #NEARnft #nearNFTs\n",
       "#NFT #NFTs #NFTCommunity #NFTdrop #nftart\n",
       "#CreativeCoding #AI #genart","#p5js #Generative\n",
       "#codefor30days #Python #100DaysOfCode\n",
       "#Python #100DaysOfCode #PythonBots #twitme\n"]
hashnum = randint(0,len(Hash)-1)
hashs =Hash[hashnum] 
hashs

from randtext import randTXT
STR = randTXT()
print (STR[:240])

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





from PIL import ImageDraw
frames =["frames/01-print.png","frames/abstract-print.png","frames/perferations.png",\
"frames/02-print.png","frames/beige-blur-frame.png","frames/rocks-print.png",\
"frames/03-print.png","frames/black-blur-frame.png","frames/usal-perferations.png",\
"frames/04-print.png","frames/frame-lite.png","frames/usa-perferations.png",\
"frames/05-print.png","frames/frames.png","frames/usar-perferations.png",\
"frames/06-print.png","frames/golden-frame.png","frames/white-blur-frame.png",\
"frames/07-print.png","frames/frames/leopard-print.png","frames/wood-blur-frame.png",\
"frames/08-print.png","lined-frame.png","frames/09-print.png","frames/perferations+.png"]
Num = randint( 0, len(frames)-1)
BOARDER = frames[Num]
imagebackground = Image.open(outfile_png)
border=Image.open(BOARDER)#.convert('p') 
imagebackground.paste(border, (0,0), mask=mask)
imagebackground

Hash = ["#AIart #Tensorflow #twitme #100DaysOfCode\n",
            "#styletransfer #PythonGraphics #PIL\n",
            "#NFTartist #NFTProject #NEARnft #nearNFTs\n",
            "#NFT #NFTs #NFTCommunity #NFTdrop #nftart\n",
            "#CreativeCoding #AI #genart","#p5js #Generative\n",
            "#codefor30days #Python #100DaysOfCode\n",
            "#Python #100DaysOfCode #PythonBots #twitme\n"]
# Create font
font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/\
truetype/dejavu/DejaVuSans-Bold.ttf', 16)
hashnum = randint(0,len(Hash)-1)
hashs =Hash[hashnum] 
x = 720//2
y = 480//2
text = hashs
x = imagebackground.width//2
y = imagebackground.height//2
blurred = Image.new('RGBA', imagebackground.size)
draw = ImageDraw.Draw(blurred)
CH = randint(0,1)
if CH == 0:COLor = ["white","black"]
elif CH == 1:COLor = ["black","white"]  
draw.text(xy=(x+20,y+230), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x+21,y+231), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x+22,y+229), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x+20,y+228), text=text, fill=COLor[0], font=font, anchor='mm')
blurred = blurred.filter(ImageFilter.BoxBlur(2))
# Paste soft text onto background
imagebackground.paste(blurred,blurred)
# Draw on sharp text
draw = ImageDraw.Draw(imagebackground)
draw.text(xy=(x+20,y+230), text=text, fill=COLor[1], font=font, anchor='mm')
imagebackground.save("onevid/temp.png")
imagebackground

from randtext import randTXT

"""
#for count in range(0,1500):
count = 1
creatmased(count)
print(count,end=".")

from OutlineImage import outlineP
filename1 = "onevid/temp.png" 
outfile_png = "onevid/temp.png" 
outlineP(filename1,outfile_png)
"""

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
im = Image.open(PATH)
im

!pwd

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
PATH = "/home/jack/Desktop/dockercommands/onevid/resultmasked-outlined0.png"
photo = open(PATH,'rb')
im = Image.open(PATH)
im

response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])




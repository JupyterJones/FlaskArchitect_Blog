import os 
os.chdir("/home/jack/Desktop/dockercommands")

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
outfile_png = "/home/jack/Desktop/TENSORFLOW/images/BINARY2"+timestr+"_.png"
outlineP(filename1,outfile_png)


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
border=Image.open(BOARDER).convert('RGBA') 
imagebackground.paste(border, (0,0), mask=mask)
imagebackground

Hash = ["#AIart #Tensorflow #twitme #100DaysOfCode\n",
            "#styletransfer #PythonGraphics #PIL\n",
            "#NFTartist #NFTProject #NEARnft #nearNFTs\n",
            "#NFT #NFTs #NFTCommunity #NFTdrop #nftart\n",
            "#CreativeCoding #AI #genart","#p5js #Generative\n",
            "#codefor30days #Python #100DaysOfCode\n",
            "#Python #100DaysOfCode #PythonBots #twitme\n"]

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
bg.paste(blurred,blurred)
# Draw on sharp text
draw = ImageDraw.Draw(bg)
draw.text(xy=(x+20,y+230), text=text, fill=COLor[1], font=font, anchor='mm')





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

from PIL import Image
import random
from random import randint
import time
dim = (720, 480)
path = r"/home/jack/Desktop/TENSORFLOW/images/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
    ])
file1=(path+base_image)
print("file1",file1)
#file2 = "/home/jack/Desktop/TENSORFLOW/otoro-neural-network/00003.png"
#file1 = "/home/jack/Desktop/TENSORFLOW/images/mining-machineol.png"
original = Image.open(file1).convert('RGB')
original = original.resize(dim, Image.NEAREST)
print("original.size",original.size)
print("------------------------")
path1 = r"/home/jack/Documents/jpg/720/"
base_image = random.choice([
    x for x in os.listdir(path1)
    if os.path.isfile(os.path.join(path1, x))
    ])
file2=(path1+base_image)
print (file2)
background = Image.open(file2).convert('RGB')
background  = background.resize(dim, Image.NEAREST)
print("background.size",background.size)
print("------------------------")
path2 = r"//home/jack/Documents/jpg/720/"
base_image = random.choice([
   x for x in os.listdir(path2)
   if os.path.isfile(os.path.join(path2, x))
   ])
  
file3=(path2+base_image)
print(file2) 

path2 = r"/home/jack/Documents/jpg/720/"
base_image = random.choice([
   x for x in os.listdir(path2)
   if os.path.isfile(os.path.join(path2, x))
   ])
   
file3=(path2+base_image)
print("file3",file3) 
img = Image.open(file3).convert('L')
dim = (720, 480)
mask =img.resize(dim, Image.NEAREST)


print("mask.size",mask.size)
result = Image.composite(original, background, mask)
result.save('resultmasked.png')
from OutlineImage import outlineP
filename1 = "resultmasked.png" 
outfile_png = "resultmasked-outlined.png"
timestr = time.strftime("%Y%m%d-%H%M%S")
outfile_png = "/home/jack/Desktop/TENSORFLOW/images/XX"+timestr+"_.png"
outlineP(filename1,outfile_png)


from PIL import Image
import random
from random import randint
import time
dim = (720, 480)
path = r"/home/jack/Desktop/TENSORFLOW/images/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
    ])
file1=(path+base_image)
print("file1",file1)
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
print ("file2: ",file2)
background = Image.open(file2).convert('RGB')
background  = background.resize(dim, Image.NEAREST)
print("background.size",background.size)
print("------------------------")

"""
path2 = r"/home/jack/Documents/jpg/720/"
base_image2 = random.choice([
   x for x in os.listdir(path2)
   if os.path.isfile(os.path.join(path2, x))
   ])
file3=(path2+base_image2)
file3 = "/home/jack/Desktop/TENSORFLOW/images/warrior-20.png"
print("file3: ",file3) 
print("------------------------")
path3 = r"/home/jack/Documents/jpg/720/"
base_image = random.choice([
   x for x in os.listdir(path3)
   if os.path.isfile(os.path.join(path3, x))
   ])
"""   
file4=(path3+base_image2)
file4=(path2+base_image1)
file4=(path1+base_image)
#file4=(path+base_image)
print("file4: ",file2) 
img = Image.open(file2).convert('L')
dim = (720, 480)
mask =img.resize(dim, Image.NEAREST)
timestr = time.strftime("%Y%m%d-%H%M%S")
png = "/home/jack/Desktop/TENSORFLOW/images/MASK"+timestr+"_.png"
mask.save(png)
print("mask.size",mask.size)
result = Image.composite(original, background, mask)
result.save('resultmasked.png')
from OutlineImage import outlineP
filename1 = "resultmasked.png" 
outfile_png = "resultmasked-outlined.png"
timestr = time.strftime("%Y%m%d-%H%M%S")
outfile_png = "/home/jack/Desktop/TENSORFLOW/images/XX"+timestr+"_.png"
outlineP(filename1,outfile_png)


from OutlineImage import outlineP
filename1 = "resultmasked.png" 
outfile_png = "resultmasked-outlined.png" 
outlineP(filename1,outfile_png)





from PIL import Image
dim = (720, 480)
path = r"/home/jack/Desktop/TENSORFLOW/images/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
    ])
file1=(path+base_image)
file2 = "/home/jack/Desktop/TENSORFLOW/otoro-neural-network/00003.png"
#file1 = "/home/jack/Desktop/TENSORFLOW/images/mining-machineol.png"
original = Image.open(file1).convert('RGB')
original = original.resize(dim, Image.NEAREST)
print(original.size)
path1 = r"/home/jack/Desktop/TENSORFLOW/images/"
base_image = random.choice([
    x for x in os.listdir(path1)
    if os.path.isfile(os.path.join(path1, x))
    ])
file2=(path1+base_image)
print (file2)





background = Image.open(file2).convert('RGB')

background  = background.resize(dim, Image.NEAREST)

print(background.size)
path2 = r"/home/jack/Desktop/Imagedata/2-binary_images/"
base_image = random.choice([
   x for x in os.listdir(path2)
   if os.path.isfile(os.path.join(path2, x))
   ])
   
file3=(path2+base_image)
#file3="/home/jack/Desktop/Imagedata/2-binary_images/binar_44_20220925161510.jpg"
print(file3) 



img = Image.open(file3).convert('L')
dim = (720, 480)
mask =img.resize(dim, Image.NEAREST)


print(mask.size)
result = Image.composite(original, background, mask)
result.save('resultmasked.png')
result

#file1 = "/home/jack/Desktop/TENSORFLOW/otoro-neural-network/00003.png"
#file2 = "/home/jack/Desktop/TENSORFLOW/images/mining-machineol.png"
room = cv2.imread(file2)
logo = cv2.imread(file1)
path2 = r"/home/jack/Desktop/Imagedata/2-binary_images/"
base_image = random.choice([
   x for x in os.listdir(path2)
   if os.path.isfile(os.path.join(path2, x))
   ])
    
file3=(path2+base_image)
#--- Resizing the logo to the shape of room image ---
logo = cv2.imread(file3)
logo = cv2.resize(logo, (room.shape[1], room.shape[0]))

#--- Apply Otsu threshold to blue channel of the logo image ---
ret, logo_mask = cv2.threshold(logo[:,:,0], 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
#cv2.imshow('logo_mask', logo_mask)

room2 = room.copy() 

#--- Copy pixel values of logo image to room image wherever the mask is white ---
room2[np.where(logo_mask == 255)] = logo[np.where(logo_mask == 255)]
timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "/home/jack/Desktop/TENSORFLOW/junk/XX"+timestr+"_"+str(count)+".png"
cv2.imwrite(filename, room2)



import cv2
  
def binarize(filein, fileout):
    # read the image file
    img = cv2.imread(filein, 2)
    ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # converting to its binary form
    bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(fileout, bw_img)
    output = fileout
    return output
    
filein = '/home/jack/Desktop/TENSORFLOW/images/MASK20221109-224545_.png'
fileout = "/home/jack/Desktop/TENSORFLOW/images/binary2.png"
binarize(filein, fileout)

original = Image.open(fileout).convert('RGB')
original

original = Image.open(filename).convert('RGB')
original

import mathsvg
image = mathsvg.SvgImage(pixel_density = 10, view_window = (( -1, -1 ), ( 1, 1 )))
image.draw_circle([0, 0], 1.1)
image.save("simple-example.svg")



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
print (STR)
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
im = Image.open(PATH)
im

In this 5th part of the image processing series, we discuss more on the Arithmetic and bitwise operations, and masking of images in Python.

It is recommended that the previous articles be run through, before starting off on your masked learning adventure here.
Setting up the environment

The following lines of code are used in all of the applications given below. We’ll include those here instead so you don’t have to read through a huge block of code.

Helps reduce clutter :)

# importing numpy to work with pixels
import numpy as np

# importing argument parsers
import argparse

# importing the OpenCV module
import cv2


# initializing an argument parser object
ap = argparse.ArgumentParser()

# adding the argument, providing the user an option
# to input the path of the image
ap.add_argument("-i", "--image", required=True, help="Path to the image")

# parsing the argument
args = vars(ap.parse_args())

# reading the image location through args
# and reading the image using cv2.imread
image = cv2.imread(args["image"])

Arithmetic Operations on Images using Python

Arithmetic Operations allow us to enhance a lot of aspects of an image.

We can work with lighting, shadows, the red, blue, and green color enhancement.

A lot of image filters on applications use the same method to alter and beautify photographs as well.

So, let’s get started with all of the code!

First, in order to understand whether the limit can go over 255 or 0, we can conduct a simple test, which provides us with 255 and 0.

# printing out details of image min, max and the wrap around
print("max of 255 :", str(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 0 :", str(cv2.subtract(np.uint8([50]), np.uint8([100]))))

print("wrap around :", str(np.uint8([200]) + np.uint8([100])))
print("wrap around :", str(np.uint8([50]) - np.uint8([100])))

In this example, we are increasing the intensity of all the pixels in the image by 100.

# adding pixels of value 255 (white) to the image
M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)
cv2.waitKey(0)

This is done by constructing a matrix with the same size as our images using the NumPy module, and adding it with our image.

In case we wish to darken an image, we subtract from the pixel values of the image, as shown below,

# adding pixels of value 0 (black) to the image
M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)

This should provide you with two different variations of the original image, one lighter, and the other darker.
Bitwise Operations

We use Bitwise operations a lot of the times while attempting to mask images.

This feature of OpenCV allows us to filter out the part of the image that is relevant to us.
Setting up

To work on Bitwise operations, we’ll first need two variables or images that we can conduct the operations on.

So, let’s create a bitwise square and a bitwise circle through which we can use the bitwise operations.

Note that bitwise operations require the images to be black and white.

# creating a square of zeros using a variable
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle : ", rectangle)

# creating a circle of zeros using a variable
circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle : ", circle)

The output images that you receive should look like this,
Image 4
Bit Square
Combine with the AND operation

Bitwise addition refers to the addition of two different images, and decide which is to be displayed using an AND operation on each pixel of the images.

# the bitwise_and function executes the AND operation
# on both the images
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

Bitwise addition of both the circle and the square gives us an output which should look like this,
Image 6
AND Bit Square
Given a choice with the OR operation

Bitwise OR provides us with a product of the two images with an OR operation performed on each pixel of the images.

# the bitwise_or function executes the OR operation
# on both the images
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

Upon performing the operation Bitwise OR, you should receive something like this,
Image 7
OR Bit Square
Exclusivity with the XOR operation

Another operation that is provided by the cv2 module is the XOR operation, which we can use through the bitwise_xor function.

# the bitwise_xor function executes the XOR operation
# on both the images
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

Image 8
XOR Bit Square
Negation using the NOT operation

Lastly, we have the negation operation, which is performed using the bitwise_not function.

The NOT operation only requires a single image as we’re not adding or subtracting anything here.

We still use it on both here however, that’s also an option.

# the bitwise_not function executes the NOT operation
# on both the images
bitwiseNot = cv2.bitwise_not(rectangle, circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)

The circle is inside the square in this case, and as such is not visible,
Image 9
Not Bit Square
Masking of images using Python OpenCV

Masking is used in Image Processing to output the Region of Interest, or simply the part of the image that we are interested in.

We tend to use bitwise operations for masking as it allows us to discard the parts of the image that we do not need.

So, let’s get started with masking!

The process of masking images

We have three steps in masking.

    Creating a black canvas with the same dimensions as the image, and naming it as mask.
    Changing the values of the mask by drawing any figure in the image and providing it with a white color.
    Performing the bitwise ADD operation on the image with the mask.

Following the same process, let’s create a few masks and use them on our image.

First, let’s work with a rectangle mask.

# creating a mask of that has the same dimensions of the image
# where each pixel is valued at 0
mask = np.zeros(image.shape[:2], dtype="uint8")

# creating a rectangle on the mask
# where the pixels are valued at 255
cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)
cv2.imshow("Mask", mask)

# performing a bitwise_and with the image and the mask
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask applied to Image", masked)
cv2.waitKey(0)

Now, let’s try it out with a circle mask.

# creating a mask of that has the same dimensions of the image
# where each pixel is valued at 0
mask = np.zeros(image.shape[:2], dtype="uint8")

# creating a rectangle on the mask
# where the pixels are valued at 255
cv2.circle(mask, (145, 200), 100, 255, -1)
cv2.imshow("Mask", mask)

# performing a bitwise_and with the image and the mask
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask applied to Image", masked)
cv2.waitKey(0)

If everything works out just fine, we should receive outputs which look something like this,
Image 10
Rectangular Mask
Conclusion

We’re finally getting started with the core of Image Processing, and understanding bitwise operations and masking in it is important.

It helps us to block out parts or only take in parts of the image that we are interested in, so, quite a useful concept.


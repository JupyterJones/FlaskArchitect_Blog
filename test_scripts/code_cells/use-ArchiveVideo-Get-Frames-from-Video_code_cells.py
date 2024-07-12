import os
os.chdir("/home/jack/Desktop/dockercommands/")
#!ls -d /*

!ls . -d */

!rm mp4.list

!find /home/ -iname '*.mp4' > mp4.list

MP4S =[]
files = open("mp4.list").readlines()
for file in files:
    if "xvid" not in file:
        file= file.replace("\n","")
        MP4S.append(file)

print(len(MP4S))

!mkdir videoframes

from random import randint
num = randint(0,len(MP4S)-1)


!mkdir archived-images

import cv2
from random import randint
from PIL import Image
import time
import random

def vid2img(filename, count):
    vidcap = cv2.VideoCapture(filename)
    # get total number of frames
    totalFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    randomFrameNumber=random.randint(0, totalFrames)
    # set frame position
    vidcap.set(cv2.CAP_PROP_POS_FRAMES,randomFrameNumber)
    success, image = vidcap.read()
    if success:
        print(".",end="|")
        cv2.imwrite("junk/archived-images.png", image)
    IM = Image.open("junk/archived-images.png")
    im = IM.resize((720,480))
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "archived-images/Wed"+str(count)+"_"+timestr+"_.png"

    im.save(filename)
    nim = Image.open(filename)
    #print(nim.size)
    return nim

filename ="/home/jack/Desktop/dockercommands/complete-videos/2196-archived-art-images.mp4"
for count in range(0,10):
    from random import randint
    num = randint(0,len(MP4S)-1)
    filename = MP4S[num]
    vid2img(filename, count)
    print (filename)
    

!ls archived-images

%%writefile VIDEOZ.py
def videoz():
    VIDEOS=["/home/jack/Desktop/dockercommands/complete-videos/2760-images-publish-archive.mp4",
    "/home/jack/Desktop/dockercommands/complete-videos/2196-archived-art-images.mp4",
    "/home/jack/Desktop/dockercommands/complete-videos/24sept-output-slow-3per-sec-jpgs.mp4",
    "/home/jack/Desktop/dockercommands/complete-videos/sep24-records-slow-3per-sec-pngs.mp4",
    "/home/jack/Desktop/dockercommands/complete-videos/slow-3per-sec.mp4",
    "/home/jack/Desktop/dockercommands/complete-videos/output_2m-28sec.mp4"]
    return VIDEOS

from VIDEOZ import videoz
MP4 = videoz()[3]
print(MP4)

!ls /home/jack/Desktop/dockercommands/image_resources/archive/archived-images.mp4

%%writefile VID2img.py
import cv2
from random import randint
from PIL import Image
import time
import random
#num = randint(0,len(MP4S))

def vid2img(count,outputpath):
    filename ="/home/jack/Desktop/dockercommands/complete-videos/24sept-output-slow-3per-sec-jpgs.mp4"
    vidcap = cv2.VideoCapture(filename)
    # get total number of frames
    totalFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    randomFrameNumber=random.randint(0, totalFrames)
    # set frame position
    vidcap.set(cv2.CAP_PROP_POS_FRAMES,randomFrameNumber)
    success, image = vidcap.read()
    print(image)
    if success:
        print(".",end="|")
        cv2.imwrite("junk/archived-images.png", image)
    IM = Image.open("junk/archived-images.png")
    im = IM.resize((720,480))
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = outputpath+"/Sunday"+str(count)+"_"+timestr+"_.png"
    im.save(filename)
    nim = Image.open(filename)
    if count==1:print(filename)
    return nim

count =1
outputpath = "Experiment"
im = vid2img(count,outputpath)
im

from VID2img import *
count =1
outputpath = "Experiment"
im = vid2img(count,outputpath)
im

!ls junk

!ls junk

from VID2img import *
for count in range(0,10):
    outputpath = "junk/"
    vid2img(count,outputpath)
    

!mkdir /home/jack/Desktop/dockercommands/archived-images/

import cv2
from random import randint
from PIL import Image
import time
import random

num = randint(0,len(MP4S)-1)
filename = MP4S[num]
vidcap = cv2.VideoCapture(filename)
# get total number of frames
totalFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
randomFrameNumber=random.randint(0, totalFrames)
# set frame position
vidcap.set(cv2.CAP_PROP_POS_FRAMES,randomFrameNumber)
success, image = vidcap.read()
if success:
    print("retrieved")
    cv2.imwrite("/home/jack/Desktop/dockercommands/archived-images/archived-images.png", image)
IM = Image.open("/home/jack/Desktop/dockercommands/archived-images/archived-images.png")
im = IM.resize((720,480))
timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "/home/jack/Desktop/dockercommands/archived-images/"+timestr+"_.png"

im.save(filename)
nim = Image.open(filename)
print(nim.size)
nim

import cv2
from random import randint
from PIL import Image
import time
import random
num = randint(0,len(MP4S))
vidcap = cv2.VideoCapture(MP4S[num])
# get total number of frames
totalFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
randomFrameNumber=random.randint(0, totalFrames)
# set frame position
vidcap.set(cv2.CAP_PROP_POS_FRAMES,randomFrameNumber)
success, image = vidcap.read()
if success:
    cv2.imwrite("videoframes/random_frame.jpg", image)
IM = Image.open("videoframes/random_frame.jpg")
im = IM.resize((720,480))
timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "videoframes/"+timestr+"_.jpg"

im.save(filename)
nim = Image.open(filename)
print(nim.size)
nim

!ls videoframes

import cv2
from random import randint
from PIL import Image
import time
from time import sleep
for i in range(200):
    try:
        num = randint(0,len(MP4S))
        vidcap = cv2.VideoCapture(MP4S[num])
        # get total number of frames
        totalFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
        randomFrameNumber=random.randint(0, totalFrames)
        # set frame position
        vidcap.set(cv2.CAP_PROP_POS_FRAMES,randomFrameNumber)
        success, image = vidcap.read()
        if success:
            cv2.imwrite("videoframes/random_frame.jpg", image)
        IM = Image.open("videoframes/random_frame.jpg")
        im = IM.resize((720,480))
        timestr = time.strftime("%Y%m%d-%H%M%S")
        filename = "videoframes/"+timestr+"_.jpg"
        im.save(filename)
        nim = Image.open(filename)
        print("-",end=".")
    except:
        pass

!ls new.db

import glob
import os.path
FILES = []
dir = '.'
files = glob.glob(os.path.join(dir, '*.ipynb'))
for file in files:
    print (file)
    FILES.append(file)

def insert(data):
    import sqlite3
    conn = sqlite3.connect("new.db")
    conn.text_factory = str
    c = conn.cursor()
    c.execute("CREATE VIRTUAL TABLE IF NOT EXISTS PROJECT using FTS4 (input)")
    c.execute("INSERT into PROJECT values (?)", (data,))
    for row in c.execute("SELECT ROWID,* FROM PROJECT ORDER BY ROWID DESC LIMIT 1"):
        print ("\nPOST VERIFIED:\n",row[0],row[1])
    conn.commit()
    conn.close()
    return
# this works data = "this is a test"
# insert(data)
ALL =[]
# string to search in a directory of files
word = 'mask'
# uncomment below to use an imput term
#word = input("Searchterm: ")

def WORDin(word):
    for filename in FILES:
        with open(filename, 'r') as fp:
            # read all lines in a list
            lines = fp.readlines()
            for line in lines:
                # check if string present on a current line
                if line.find(word) != -1:
                    if len(line)<100:
                        #print('The term '+word+' exists in '+filename+' .\nLineNumber:', lines.index(line),line.replace("\\n",""))
                        data ='The term '+word+' exists in '+filename+' .\nLineNumber:', lines.index(line),line.replace("\\n","")
                        ALL.append(data)
                        #convert the data to a string
                        dataout = str(data).replace("\\n",'')
                        insert(dataout)
word = 'mask'
WORDin(word)
for line in ALL:
    print(line)





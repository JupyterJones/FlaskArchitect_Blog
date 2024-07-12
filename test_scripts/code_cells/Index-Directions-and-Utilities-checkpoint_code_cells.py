GetRandDir.py

%%writefile GetRandDir.py
import os
from random import randint
def GetRandDir():
    DIRS =[]
    directories = next(os.walk('.'))[1]
    for directory in directories:
        # Exclude Directories: ".", "chromedrive" and "AutoImageCrawler"
        if "." not in directory and "_" not in directory and "chromedrive" not in directory and "AutoImageCrawler" not in directory:
            if "-images"in directory:
                DIRS.append(directory)
    Num = len(DIRS)-1
    ID = randint(0,Num) 

    DIRectory = (DIRS[ID])
    return DIRectory

from GetRandDir import GetRandDir
DIR = GetRandDir()
DIR

%%writefile getdirfromlist.py
from random import randint
def getdirfromlist(dirLIST):
    num= len(dirLIST)-1
    DirId = randint(0,num)
    Imdir = dirLIST[DirId]
    return Imdir

from getdirfromlist import *
dirLIST = ["antique%20art/","art%20nouveau/","ancient%20manuscript%20art/","antique%20book%20covers/"]
use = getdirfromlist(dirLIST)  
use

!ls . -d a*/

%%writefile FileName.py
import time
def FilenameByTime(directory):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = directory+"/"+timestr+"_.jpg"
    return filename    

from FileName import *
directory = "tmp"
filename = FilenameByTime(directory)
print(filename)

from PIL import Image
import random
import os
from GetRandDir import GetRandDir

DN = GetRandDir() 
def GetRandomImage(path):
    base_image = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
        ])
    filename0=(path+base_image)
    image = Image.open(filename0)
    return image

path = DN+"/"
im = GetRandomImage(path)
im

%%writefile GetRandDir.py
import os
from random import randint
def GetRandDir():
    DIRS =[]
    directories = next(os.walk('.'))[1]
    for directory in directories:
        if "." not in directory and "_" not in directory and "chromedrive" not in directory and "AutoImageCrawler" not in directory:
            DIRS.append(directory)
        Num = len(DIRS)-1
    ID = randint(0,Num) 

    DIRectory = (DIRS[ID])
    return DIRectory

from GetRandDir import GetRandDir
DN = GetRandDir() 
print(DN)

import os
from random import randint
DIRS =[]
directories = next(os.walk('.'))[1]
for directory in directories:
    if "." not in directory and "_" not in directory and "chromedrive" not in directory and "AutoImageCrawler" not in directory:
        DIRS.append(directory)
        print(directory)

Num = len(DIRS)-1
ID = randint(0,Num) 

DIRectory = (DIRS[ID])
print (DIRectory)

import os
from random import randint
DIRS =[]
directories = next(os.walk('.'))[1]
for directory in directories:
    dlst=["_","chromedrive","AutoImageCrawler"]
    if dlst[0] not in directory and dlst[1] not in directory and dlst[2] not in directory:
        DIRS.append(directory)
        print(directory)
    
Num = len(DIRS)-1
ID = randint(0,Num) 


# debug
dlst=["_","chromedrive","AutoImageCrawler"]
print (dlst[0], dlst[1], dlst[2])




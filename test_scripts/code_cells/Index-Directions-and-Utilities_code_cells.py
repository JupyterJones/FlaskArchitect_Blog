%%writefile GetRandDir.py
import os
from random import randint
def GetRandDir():
    DIRS =[]
    directories = next(os.walk('.'))[1]
    for directory in directories:
        # Exclude Directories: ".", "chromedrive" and "AutoImageCrawler"
        if "." not in directory and "_" not in directory:
            if "-images"in directory:
                DIRS.append(directory)
    Num = len(DIRS)-1
    ID = randint(0,Num) 
    print(Num,ID)
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
dirLIST = ["vintage-bottle-labels","vintage-advertisments","vintage-clothing-patterns"]
use = getdirfromlist(dirLIST)  
use

!ls . -d v*/

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

%%writefile GetRandomImage.py
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

def getone():
    path = DN+"/"
    from GetRandDir import GetRandDir
    DIR = GetRandDir()+"/"
    im = GetRandomImage(DIR)
    return im

from GetRandomImage import *
im = getone()
im

# Remember The "/" thay follows the directory name
from GetRandomImage import GetRandomImage
path = "vintage-clothing-patterns/"
IM= GetRandomImage(path)
IM

!ls *.py




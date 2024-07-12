count = 0
while True:
    filein = LST[count]
    print count,filein
    count = count +1
    if count==114:break

import os
import random
path0 = r"640x640/"
random_filename0 = random.choice([
y for y in os.listdir(path0)
if os.path.isfile(os.path.join(path0, y)) ])
RandIm = path0+random_filename0
!gmic -i 640x640/P_20180411_062100.jpg \
-v 0 -cartoon 1,124.771,20,0.5,1.5,8,0 \
-o cartoon0022A.jpg
!showme cartoon0022A.jpg


import os
import random
path0 = r"640x640/"
random_filename0 = random.choice([
y for y in os.listdir(path0)
if os.path.isfile(os.path.join(path0, y)) ])
RandIm = path0+random_filename0
!gmic -i 640x640/P_20180411_062100.jpg \
-v 0 -cartoon 1,124.771,20,0.5,1.5,8,0 \
-o cartoon0022A.jpg
!showme cartoon0022A.jpg


f = open("640x640.list").readlines()
LST = []
for lines in f:
    line = lines.replace("\n","")
    PATH = "640x640/"+line
    LST.append(PATH)

!ls 640x640/P_20180416_164243.jpg

!ls cartoon

# WORKS GOOD cartoon
# 114 images in 640x640.list
import subprocess
count = 0
filein = LST[0]
filein = filein.replace("\n","")
count = count +1
print count,line
filename = time.strftime("cartoon/%Y%m%d%H%M%S.jpg")
com ="gmic -input "+filein+ "-resize2dx[-1] 1024 lh='{h}' --blur[-1] 0.35% \
-quantize[-1] 10  -output "+filename+", shell=True"
subprocess.call(com)

import subprocess
import os
filein = LST[0]
filein = filein.replace("\n","")
count = count +1
print count,line
filename = time.strftime("cartoon/%Y%m%d%H%M%S.jpg")

com ="gmic -input "+filein+ " -resize2dx[-1] 1024 lh='{h}' --blur[-1] 0.35% \
-quantize[-1] 10  -output "+filename+", shell=True"
subprocess.call(com)

!ls 640x640/P_20180416_164243.jpg



import subprocess
import os
import time
filein = LST[0]
filein = filein.replace("\n","")
count = count +1
print count,line
filename = time.strftime("cartoon/%Y%m%d%H%M%S.jpg")

com =["gmic -input 640x640/P_20180416_164243.jpg -resize2dx[-1] 1024 lh='{h}' --blur[-1] 0.35% \
-quantize[-1] 10  -output TESTING.jpg"]
subprocess.call(com)

# cartoon Images
!gmic -i /home/jack/Desktop/GRAPHICS/gmic/640x640/P_20180416_163956_BF.jpg \
-v 0 -cartoon 1,124.771,20,0.5,1.5,8,0 \
-normalize[-0] 60,255 \
-o cartoon0022A.jpg
!showme cartoon0022A.jpg

# cartoon Images
!gmic -i /home/jack/Desktop/GRAPHICS/gmic/640x640/P_20180416_163956_BF.jpg \
-v 0 -cartoon 1,124.771,20,0.5,1.5,8,0 \
-normalize[-0] 60,255 \
-o cartoon0022A.jpg
!showme cartoon0022A.jpg

!gmic -i 640x640/P_20180416_164243.jpg \
-normalize[-0] 60,255 \
-o junk/LIGHTER_P_20180416_164243.jpg
!showme junk/LIGHTER_P_20180416_164243.jpg


# 114 images in 640x640.list
import subprocess
count = 35
filein = LST[count]
count = count +1
print count,line
filename = time.strftime("junk/cartoon_%Y%m%d%H%M%S.jpg")
subprocess.call("gmic -input "+line+" -v 0 -cartoon 1,124.771,20,0.5,1.5,8,0  -normalize[-0] 60,255 -output "+filename, shell=True) 




!gmic -v 99 -i 640x640/181.jpg -hotchocolate.gmic -o chocolate-test.jpg


# 114 images in 640x640.list
import subprocess
count = 0
filein = LST[count]
count = count +1
print count,line
filename = time.strftime("junk/%Y%m%d%H%M%S.jpg")
subprocess.call("gmic -input "+line+" -resize2dx[-1] 1024 lh='{h}' --blur[-1] 0.35% \
-quantize[-1] 8  -output "+filename, shell=True) 


!ls junk

!gmic v + sp tiger v

!ls /home/jack/.config/gmic/

!showme /home/jack/.config/gmic/sample_tiger.png

# %load /home/jack/.config/gmic/hotchocolate.gmic
#@gimp <span color="red">&#x2764; <b>One-click chocolate !</b></span> : gimp_hotchocolate, gimp_hotchocolate_preview
#@gimp : note = note{"Want to send a <b>free hot chocolate</b> to the <b>hard-working</b> developers who provide G'MIC <b>for free</b> ?\n
#@gimp : Just follow the link below (or copy/paste into your browser) and click <b>on the sponsored link</b> that is shown. It's as simple as that and
#@gimp : we'll drink to you :)"}
#@gimp : link = link{"Send a free hot chocolate to the G'MIC developers","http://gmic.eu/freechocolate.shtml"}
#@gimp : link = link{"http://gmic.eu/freechocolate.shtml"}
#@gimp : sep = separator()
#@gimp : note = note{"If you'd like to send <b>more</b> than a single hot chocolate for our efforts, please visit the following page where you can contribute
#@gimp : extra to help keep us motivated (via <b>Paypal</b>):"}
#@gimp : link = link{"Offer even more hot chocolate to the G'MIC developers","http://gmic.eu/morechocolate.shtml"}
#@gimp : link = link{"http://gmic.eu/morechocolate.shtml"}
#@gimp : sep = separator()
#@gimp : note = note{"<small><b>Note:</b> This filter won't appear anymore after you re-run the plug-in. So, don't miss the occasion!</small>"}
#@gimp : sep = separator(), note = note("<small>Author: <i>David Tschumperl&#233;</i>.      Latest update: <i>11/30/2015</i>.</small>")
gimp_hotchocolate : (10) -o. raw:/home/jack/.config/gmic/hotchocolate.gmic,uchar -rm. 
gimp_hotchocolate_preview : -gimp_hotchocolate -gimp_friends

!gmic -i 640x640/171.jpg

!gmic -v 6 -i 640x640/171.jpg

f = open("GMIC-documents.txt", "r").readlines()
count = 0
start = raw_input("Start: ")
for line in f:
    line = line.replace("\n", "")
    count = count +1
    start = int(start)
    end = start +150
    if count>start:
        print line

text = "gmic -i 640x640/153.jpg blur 3,0 sharpen 10 resize 200%,200% -o junk/.jpg"
name = "".join(text.split())
print name

!gmic -i 640x640/153.jpg resize 75%,75% -o junk/blur-sharpen-resize.jpg
!showme junk/blur-sharpen-resize.jpg

from random import randint
sm =randint(0,5)
sh =randint(50,250)
thres = randint(5,50)
thk = randint(1,5)*.1
col = randint(1,4)*.1
quant = randint(3,10)
print sm, sh, thres, thk, col, quant

Apply cartoon effect on selected images.
Default values: 
smoothness=3 sharpening=150 threshold=20 thickness=0.25 color=1.5 quantization=8

import os
import sys
sys.path.insert(0, "GRAPHICS/gmic")
from SEARCHdocs import searchdocs
searchdocs("GRAPHICS/gmic/GMIC-documents.txt")

from SEARCHdocs import searchdocs
searchdocs("/home/jack/.config/gmic/update222.gmic")

!gmic -v 99 -i posterize0022B.jpg old_photo -display


!gmic -v 99 -i posterize0022B.jpg sepia -display


v - noise 20 bilateral 30,60 b 2 sharpen 100 frame_fuzzy 8%,8%,6,3 to_rgb shadow_patch 0.75 n 0,255 sepia v +

from SEARCHdocs import searchdocs
searchdocs("GMIC-documents.txt")

f = open("GMIC-documents.txt", "r").readlines()
count = 0
search = raw_input("Search: ")
for line in f:
    line = line.replace("\n", "")
    count = count +1
    start = int(start)
    end = start +150
    if count>start:
        print line

!gmic -i 640x640/171.jpg -status

# create a list in memory of a directory
from time import sleep
import os
LST = []
PATH = "640x640/"
for files in sorted(os.listdir(PATH)):
    LST.append(PATH+files)
    
    
Then it may be used with:
    
    
for line in LST:
    print line    

for line in LST:
    print line

import subprocess
import os
count = 0
while True:
    count = count+1
    filein = LST[count]
    filein = filein.replace("\n","")
    count = count +1
    print count,line
    filename = time.strftime("cartoon/%Y%m%d%H%M%S.jpg")
    #com ="gmic -input "+filein+ " -v 0 -cartoon 1,124.771,20,0.5,1.5,8,0 \
    #-normalize[-0] 60,255 -output "+filename+", shell=True"
    #subprocess.call(com)
    subprocess.call("gmic -input "+filein+" -v 0 -cartoon 1,124.771,20,0.5,1.5,8,0 \
    -normalize[-0] 60,255 -output "+filename, shell=True) 


import subprocess
import os
count = 0
while True:
    count = count+1
    filein = LST[count]
    filein = filein.replace("\n","")
    count = count +1
    print count,line
    filename = time.strftime("cartoon/RANDOM_%Y%m%d%H%M%S.jpg")

    subprocess.call("gmic -input "+filein+" -v 0 -cartoon 1,124.771,20,0.5,1.5,8,0 \
    -normalize[-0] 60,255 -output "+filename, shell=True) 


print (randint(1,4)*1.1)-1



import subprocess
import os
count = 0
while True:
    count = count+1
    filein = LST[count]
    filein = filein.replace("\n","")
    count = count +1
    print count,line
    filename = time.strftime("cartoon/RANDOM_%Y%m%d%H%M%S.jpg")

    subprocess.call("gmic -input "+filein+" -v 0 -cartoon 1,124.771,20,0.5,1.5,8,0 \
    -normalize[-0] 60,255 -output "+filename, shell=True) 


!mkdir

import subprocess
import os
import time
directory = "cartoon"
if not os.path.exists(directory):
    os.makedirs(directory)
count = 0
while True:
    count = count +1
    if count==114:break
    filename = time.strftime(directory+"/TOON_%Y%m%d%H%M%S.jpg")
    filein = LST[count]
    
    
    print count,filein
    
    

#VERY GOOD 
import subprocess
import os
from random import randint
from time import sleep
count = 0
while True:
    count = count+1
    filein = LST[count]
    filein = filein.replace("\n","")
    count = count +1
    print count,line
    sm =randint(0,5)
    sh =randint(50,250)
    thres = randint(5,50)
    thk = randint(1,5)*.1
    col = (randint(1,10)*1.1)-1
    quant = randint(3,10)
    sm = str(sm)
    quant = str(quant)
    col = str(col)
    thres = str(thres)
    thk = str(thk)
    sh = str(sh)
    filename = time.strftime("cartoon/RANDOM-sm"+sm+"-sh"+sh+"-thres"+thres+"-thk"+thk+"-col"+col+"-quant"+quant+"%Y%m%d%H%M%S.jpg")
-v -99 -fx_posterize 150,30,1,12,0,0,0,0
    subprocess.call("gmic -input "+filein+" -v 0 -cartoon 1,"+sh+","+thres+","+thk+","+col+","+quant+",0 \
    -normalize[-0] 60,255 -output "+filename, shell=True)
    sleep(1)

import os
import random
path0 = r"640x640/"
random_filename0 = random.choice([
y for y in os.listdir(path0)
if os.path.isfile(os.path.join(path0, y)) ])
RandIm = path0+random_filename0
print RandIm

-v 0 -fx_halftone -15.3846,-35.5769,-26.9231,2.88462,12,11,57,5,2.76923,0

# 'density=50', 'thickness=10', 'max_angle=75', 'opacity=0.7' and 'smoothness=0'
!gmic -v 5 -i 640x640/101.jpg -cubism  50, 10, 75, 0.7,0 -display

# 'density=50', 'thickness=10', 'max_angle=75', 'opacity=0.7' and 'smoothness=0'
!gmic -i 640x640/P_20180415_164415.jpg \
-v 0 -cubism  50, 10, 75, 0.7,0 \
-o cubism22A.jpg
!showme cubism22A.jpg    

import os
import random
path0 = r"640x640/"
random_filename0 = random.choice([
y for y in os.listdir(path0)
if os.path.isfile(os.path.join(path0, y)) ])
RandIm = path0+random_filename0
#posterize0022A.jpg -v -99 -fx_posterize 150,30,1,12,0,0,0,0
#posterize0022c.jpg -v -99 -fx_posterize_preview 0,0,1.54472,12,8,17.0732,1,0
#posterize0022D.jpg -v -99 -fx_posterize 150,20,1.54472,12,8,15,1,0
#halftone0022E.jpg -v -99 -fx_halftone 0,0,0,0,8,6,10,5,0.5,0
#halftone0022f.jpg -v -99 -fx_halftone 0,0,0,0,5,8,8,5,0.1,0

!gmic -i 640x640/P_20180411_062100.jpg \
-v -99 -fx_halftone 0,0,0,0,5,8,8,5,0.1,0 \
-normalize[-0] 60,255 \
-o halftone0022f.jpg
!showme halftone0022f.jpg


!mkdir halftone

#Default values: 'strength=100', 'radius_min=70' and 'radius_max=90'.

!gmic -i 640x640/013.jpg \
-v -99 -fx_vignette 150.0,37.0,88.0,206,0,0,0  -display

# Good
!gmic -i /home/jack/Desktop/GRAPHICS/gmic/640x640/013.jpg -v -99 \
-fx_lightglow_preview 20.0,0.6,8,0.80,0,0 \
-v -99 -fx_vignette 150.0,37.0,88.0,206,0,0,0  -display

!gmic linear.png -input_gpl palette.gpl -x_colorize[0] 1,1024,1,[-1] -k[0] -s c,{3-s} -o[1] \
-display

!gmic -i /home/jack/Desktop/GRAPHICS/gmic/640x640/013.jpg -v -99 \
-to_rgba -replace_color 0,0,255,0,0,255,128,128,128,0 -display \
-o colorize.png


!gmic -i /home/jack/Desktop/GRAPHICS/gmic/640x640/013.jpg -v -99 \
-x_colorize 1,1024,1 -s c,{3-s} -o[-1] -display -o colorize.png

!showme colorize.png

!gmic -i /home/jack/Desktop/GRAPHICS/gmic/640x640/013.jpg -v -99 \
-fx_lightglow_preview 20.4819,0.610442,8,0.795181,0,0 -display

-v -99 -fx_vignette 43.4884,67.4419,88.3721,206,118,118,255

-v -99 -fx_lightglow_preview 20.4819,0.610442,8,0.795181,0,0

gmic lineart.png -x_colorize 1,1024,1 -s c,{3-s} -o[-1] colors.png
Here is another variant if you save also in this folder a palette.gpl file to get an additional palette dialog.  
gmic linear.png -input_gpl palette.gpl -x_colorize[0] 1,1024,1,[-1] -k[0] -s c,{3-s} -o[1] colors.png


# texturize_canvas
!gmic -input /home/jack/Desktop/GRAPHICS/gmic/640x640/P_20180412_173934.jpg \
 -v 99 old_photo \
-normalize[-1] 50,255 \
-output old-photo.jpg
!showme old-photo.jpg

randint(2000, 4000)*.01

!mkdir old_photo

#Thin Edges VERY GOOD 
import subprocess
import os
from random import randint
from time import sleep
import time
"""
old_photo
"""
# create a list in memory of a directory
LST = []
PATH = "MaskedResults/"
for files in sorted(os.listdir(PATH)):
    LST.append(PATH+files)
    
count = 0
while True:
    count = count+1
    filein = LST[count]
    filein = filein.replace("\n","")
    count = count +1
    print count

    threshhold = randint(20, 60)
    threshhold = str(threshhold)
    thresh = randint(150, 255)
    thresh = str(thresh)

    
    filename = time.strftime("old_photo/old_photo_%Y%m%d%H%M%S.jpg")
    #subprocess.call("gmic -input "+filein+" -v 0 -cartoon 1,124.771,20,0.5,1.5,8,0 \
    #subprocess.call("gmic -input "+filein+" -v 0 -cartoon" +sm+" "+sh+" "+thres+" "+thk+" "+col+" "+quant+\
    subprocess.call("gmic -input "+filein+"  -v 99 old_photo -normalize[-1] "+threshhold+","+thresh+" -output "+filename, shell=True)
    #  -v 0 -texturize_canvas 32.3794,3,0.6 \
    sleep(5)
    print filename

!gmic -update

#Thin Edges VERY GOOD 
import subprocess
import os
from random import randint
from time import sleep
"""
-v 0 -texturize_canvas 27.65,5,0.6
Add canvas texture to image [0], with amplitude 27.65, \
fibrousness 5 and emboss level 0.6.

-v 0 -texturize_canvas 32.3794,3,0.6
-v 0 -texturize_canvas 32.3794,3,0.6
"""
# create a list in memory of a directory
LST = []
PATH = "640x640/"
for files in sorted(os.listdir(PATH)):
    LST.append(PATH+files)
    
count = 0
while True:
    count = count+1
    filein = LST[count]
    filein = filein.replace("\n","")
    count = count +1
    print count,line
    #-v 0 -texturize_canvas 32.3794,3,0.6 \
    smoothness = randint(2000, 5000)*.01 
    threshhold = randint(2, 10)
    thresh = randint(1, 12)*.1
    smoothness = str(smoothness)
    thresh = str(thresh)
    threshhold = str(threshhold)
    
    filename = time.strftime("texture/RANDOM-smoothness"+smoothness+"-threshhold"+threshhold+"_%Y%m%d%H%M%S.jpg")
    #subprocess.call("gmic -input "+filein+" -v 0 -cartoon 1,124.771,20,0.5,1.5,8,0 \
    #subprocess.call("gmic -input "+filein+" -v 0 -cartoon" +sm+" "+sh+" "+thres+" "+thk+" "+col+" "+quant+\
    subprocess.call("gmic -input "+filein+" -v 0 -texturize_canvas "+smoothness+","+threshhold+",,"+thresh+" -output "+filename, shell=True)
    #  -v 0 -texturize_canvas 32.3794,3,0.6 \
    sleep(5)
    print filename

#Thin Edges VERY GOOD 
import subprocess
import os
from random import randint
from time import sleep
"""
Thin Edges
smoothness 0 4 
threshhold .2 10


-v -99 -fx_thin_edges 0.64257,7.83133,0,0
-v -99 -fx_thin_edges 1.16466,6.62651,0,0
"""
# create a list in memory of a directory
LST = []
PATH = "640x640/"
for files in sorted(os.listdir(PATH)):
    LST.append(PATH+files)
    
count = 0
while True:
    count = count+1
    filein = LST[count]
    filein = filein.replace("\n","")
    count = count +1
    print count,line
    
    smoothness = randint(1, 400)*.01 
    threshhold = randint(20, 600)*.01
    smoothness = str(smoothness)
    threshhold = str(threshhold)
    
    filename = time.strftime("thinedges/RANDOM-smoothness"+smoothness+"-threshhold"+threshhold+"_%Y%m%d%H%M%S.jpg")
    #subprocess.call("gmic -input "+filein+" -v 0 -cartoon 1,124.771,20,0.5,1.5,8,0 \
    #subprocess.call("gmic -input "+filein+" -v 0 -cartoon" +sm+" "+sh+" "+thres+" "+thk+" "+col+" "+quant+\
    subprocess.call("gmic -input "+filein+" -v 0 -fx_thin_edges "+smoothness+","+threshhold+"0,0 -output "+filename, shell=True)
    # -v -99 -fx_thin_edges 1.16466,6.62651,0,0
    sleep(5)
    print filename

#Halftone VERY GOOD 
import subprocess
import os
from random import randint
from time import sleep
"""
Halftone Parameters
brightness float -100 - 100
contrast float t -100 - 100
gama float -100 - 100
smoothness float 1 - 10

number 2 - 32 
size dark 2 - 256
size light 2 - 256
shape { 0=square | 1=diamond | 2=circle | 3=inv-square | 4=inv-diamond | 5=inv-circle }
smooth float 0 -32

-v -99 -fx_halftone 0,0,0,0,8,6,10,5,0.5,0
-v -99 -fx_halftone 0,0,0,0,5,8,8,5,0.1,0
"""
# create a list in memory of a directory
LST = []
PATH = "640x640/"
for files in sorted(os.listdir(PATH)):
    LST.append(PATH+files)
    
count = 0
while True:
    count = count+1
    filein = LST[count]
    filein = filein.replace("\n","")
    count = count +1
    print count,line
    
    brit = randint(-50,50)
    cont = randint(-50,50)
    gama = randint(-50,100)*.1
    smoothness = randint(1,80)*.1
    
    #number = randint(2, 32)
    number = randint(2, 10) 
    #sizedark = randint(2, 256)
    #sizelight = randint(2, 256)
    sizedark = randint(2, 15)
    sizelight = randint(2, 15)    
    shape = randint(0,5)
    smooth = randint(1, 20)*.1    
 
    brit = str(brit)
    cont = str(cont)
    gama = str(gama)
    smoothness = str(smoothness)
    number = str(number)
    sizedark =str(sizedark)
    sizelight = str(sizelight)
    shape = str(shape)
    smooth = str(smooth)
    
    filename = time.strftime("halftone/RANDOM-brit"+brit+"-cont"+cont+"-gama"+gama+"-smoothness"+smoothness+"-number"+number+"-sizedark"+sizedark+"-sizelight"+sizelight+"-shape"+shape+"-smooth"+smooth+"_%Y%m%d%H%M%S.jpg")
    #subprocess.call("gmic -input "+filein+" -v 0 -cartoon 1,124.771,20,0.5,1.5,8,0 \
    #subprocess.call("gmic -input "+filein+" -v 0 -cartoon" +sm+" "+sh+" "+thres+" "+thk+" "+col+" "+quant+\
    subprocess.call("gmic -input "+filein+" -v 0 -fx_halftone "+brit+","+cont+","+gama+","+smoothness+","+number+","+sizedark+","+sizelight+","+shape+","+smooth+" -normalize[-0] 0,255 -output "+filename, shell=True)
    # -v -99 -fx_halftone 0,0,0,0,8,6,10,5,0.5,0
    sleep(5)
    print filename

#Posturize VERY GOOD 
import subprocess
import os
from random import randint
from time import sleep
"""
Posturize Parameters
smoothness 150 - ( float  0 - 800 )
edges 30       - ( float  0 - 100 )
paint 1        - ( float  0 -  10 )
minimal area 9 - ( int    0 -  64 )
outline 0      - ( int    0 - 100)

-v -99 -fx_posterize 150,30,1,12,0,0,0,0
-v -99 -fx_posterize_preview 0,0,1.54472,12,8,17.0732,1,0

"""
# create a list in memory of a directory
LST = []
PATH = "640x640/"
for files in sorted(os.listdir(PATH)):
    LST.append(PATH+files)
    
count = 0
while True:
    count = count+1
    filein = LST[count]
    filein = filein.replace("\n","")
    count = count +1
    print count,line
    sm =randint(40,4000)*.1
    edge =randint(200,1000)*.1    
    paint = randint(10,100)*.1
    #paint = randint(2,10)
    #mini = randint(0,640)*.1
    mini = randint(0,96)
    minix = randint(0,100)
    outline = randint(0,20)
    linez = randint(0,80)
    sm = str(sm)
    edge = str(edge)
    paint = str(paint)
    mini = str(mini)
    minix = str(minix)
    outline =str(outline)
    linez = str(linez) 
    filename = time.strftime("posterize/RANDOM-sm"+sm+"-edge"+edge+"-paint"+paint+"-mini"+mini+"-minix"+minix+"-outline"+outline+"-linez"+linez+"_%Y%m%d%H%M%S.jpg")
    #subprocess.call("gmic -input "+filein+" -v 0 -cartoon 1,124.771,20,0.5,1.5,8,0 \
    #subprocess.call("gmic -input "+filein+" -v 0 -cartoon" +sm+" "+sh+" "+thres+" "+thk+" "+col+" "+quant+\
    subprocess.call("gmic -input "+filein+" -v 0 -fx_posterize "+sm+","+edge+","+paint+","+mini+","+minix+","+outline+","+linez+",0 \
    -normalize[-0] 0,255 -output "+filename, shell=True)
    #-v -99 -fx_posterize 150,20,1.54472,12,8,15,1,0
    sleep(5)
    print filename

#VERY GOOD 
import subprocess
import os
from random import randint
from time import sleep
count = 0
while True:
    count = count+1
    filein = LST[count]
    filein = filein.replace("\n","")
    count = count +1
    print count,line
    sm =randint(0,5)
    sh =randint(50,250)
    thres = randint(5,50)
    thk = randint(1,5)*.1
    col = (randint(1,10)*1.1)-1
    quant = randint(3,10)
    sm = str(sm)
    quant = str(quant)
    col = str(col)
    thres = str(thres)
    thk = str(thk)
    sh = str(sh)
    filename = time.strftime("cartoon/RANDOM-sm"+sm+"-sh"+sh+"-thres"+thres+"-thk"+thk+"-col"+col+"-quant"+quant+"%Y%m%d%H%M%S.jpg")
    #subprocess.call("gmic -input "+filein+" -v 0 -cartoon 1,124.771,20,0.5,1.5,8,0 \
    #subprocess.call("gmic -input "+filein+" -v 0 -cartoon" +sm+" "+sh+" "+thres+" "+thk+" "+col+" "+quant+\
    subprocess.call("gmic -input "+filein+" -v 0 -cartoon 1,"+sh+","+thres+","+thk+","+col+","+quant+",0 \
    -normalize[-0] 60,255 -output "+filename, shell=True)
    sleep(1)


import random
from random import randint
import time
import markovify
import os
import sys
sys.path.insert(1, "/home/jack/hidden")
import key
sys.path.insert(1, "/home/jack/Desktop/pycode/vpython2")
import twython
from twython import Twython
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
# %load mkplot.py
#!/usr/local/bin/python
from __future__ import division
import glob
import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline 
import numpy as np 


from PIL import Image
from PIL import ImageFont, ImageDraw, ImageFilter, ImageChops
import textwrap
til = Image.new("RGB",(640,640))
#image = "img = 'wiki/Training-Loss-Graph-forwiki_2018-0609062255.png'"
im = Image.open("Last-GRU-network-loss-1.1179-plot-for-Directory-uranbible_2018-0617131414.png") #600x400

til.paste(im,(20,35))
til2 = Image.new("RGB",(600,160),(250,250,250))
til.paste(til2,(20,450))
w,h = im.size
samp = []
cwd = os.getcwd()
directory = raw_input("USE Directory: ")
PATH = cwd+"/"+directory+"/"
files = glob.glob(PATH+"GRU*.t7")
files.sort(key=os.path.getmtime)
line = ("\n".join(files))
samp.append(line)
#fname = "Here shows the effect of changing the LearningRate"
fname = "Filename parsed for data:"
# read a text file as a list of lines
# find the last line, change to a file you have
filename = "/home/jack/Desktop/char-rnn/uranbible_.txt"
fileHandle = open (filename,"r" )
lineList = fileHandle.readlines()
fileHandle.close()
line = lineList[-1]
text0 = "This is the loss of the last model: ",line[-9:-3]
text1 = "This is the Epoch: ",line[-14:-10]
text2 = "Current learning_rate: ", line[-51:-38]
text3 = "rnn-size: ", line[-28:-25]

Text = str(line[-51:])
SPACE = "-----------------------------------------------"
text0 = str(text0)
text1 = str(text1)
text2 = str(text2)
text3 = str(text3)
text3 = str(text3)
draw = ImageDraw.Draw(til)
font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 18)
draw.text((70,450), fname, font=font, fill= "black")
font = ImageFont.truetype("/home/jack/.fonts/dontmix.ttf", 20)
#draw.text((320,450), fname0, font=font, fill= "black")
#font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 16)
#draw.text((70,474), text0, font=font, fill= "red")
font = ImageFont.truetype("/home/jack/.fonts/dontmix.ttf", 22)
draw.text((70,472), Text, font=font, fill= "navy")
draw.text((70,490), SPACE, font=font, fill= "black")
draw.text((70,510), text0, font=font, fill= "navy")  
draw.text((70,530), text1, font=font, fill= "navy")    
draw.text((70,550), text2, font=font, fill= "navy")    
draw.text((70,570), text3, font=font, fill= "navy")    
#draw.text((70,552), text4, font=font, fill= "navy")    
#draw.text((70,572), text5, font=font, fill= "navy")
filename = "testtiles.png"
til.save(filename)
filename0= filename
def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]

def draw_blurred_back(img, position, text, font, col, halo_col):
    halo = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(position, text, font = font, fill = halo_col)
    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(position, text, font = font, fill = col)
    return Image.composite(img, blurred_halo, ImageChops.invert(blurred_halo))

if __name__ == '__main__':
    inp = Image.open(filename0)
    inp = inp.resize((640,640), Image.ANTIALIAS)
    font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 35)
    text_title = (255, 30,30) # bright green
    blur_title = (0, 0, 0)   # black
    #textin = (generate_the_word("wordcloud.txt"))
    i2 = draw_blurred_back(inp, (320, 85), "PlotBot", font, text_title, blur_title)
    font0 = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 25)
    i2 = draw_blurred_back(i2, (320, 127), "Live Plot for this", font0, text_title, blur_title)    
    i2 = draw_blurred_back(i2, (320, 160), "Lua text generator.", font0, text_title, blur_title)    
    
    #txt = Image.new('RGBA', i.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
    # get a drawing context
    signature_ = "@Jacknorthrup Instagram and @jacklnorthrup TwitterBot Project" 
    #get length in pixel of signature_
    sizeS,ln = fnt.getsize(signature_)
    #add 15 pixels to right border
    pt = sizeS+25
    width, height = inp.size
    #marginx starting point of signature_
    marginx = pt
    #bottom margin
    marginy = 30
    x = width - marginx
    y = height - marginy
    

    text_sig = (255, 55,30) # bright green
    blur_sig = (0, 0, 0)   # black
    txt=draw_blurred_back(i2,(x,y), signature_, fnt, text_sig, blur_sig)
    out = Image.alpha_composite(i2, txt)
    out.save("TM_POST.png")

#removed keys for privacy reasons
CONSUMER_KEY = key.twiter()[0]
CONSUMER_SECRET = key.twiter()[1]
ACCESS_KEY = key.twiter()[2]
ACCESS_SECRET = key.twiter()[3]

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
f = open("MYTEXT.txt")
text = f.read()
text_model = markovify.Text(text)
STR = (text_model.make_short_sentence(200))
#STR = ("8conv3fc_DSN.caffemodel Layer pool4. Snow capped mouintains Yah right . Dream on !")
# USE BELOW for no signature
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "TM_POST.png"
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')
image = open(PATH,'rb')
#response = twitter.upload_media(media=image)
#twitter.update_status(status=STR, media_ids=[response['media_id']])

print STR
!showme TM_POST.png
out

#ONE TIME MANUAL POSTS
#!/home/jack/anaconda2/python
import random
from random import randint
import time
import markovify
import os
import sys
sys.path.insert(1, "/home/jack/hidden")
import key
sys.path.insert(1, "/home/jack/Desktop/pycode/vpython2")
import twython
from twython import Twython
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
# %load mkplot.py
#!/usr/local/bin/python
from __future__ import division
import sys
import glob
import time
import os
import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline 
import numpy as np 
#if len(sys.argv)==1: sys.exit("\n=========================\nThe directory of *.t7 files required. Example:\npython mktext-n-plot.py uranbible\n=========================\n")
#directory = sys.argv[1]
#directory ="wiki"
directory = raw_input("Use Directory: ")
#f0= open(title,"w");f.close()
cwd = os.getcwd()
PATH = cwd+"/"+directory
filename = PATH+"_.dat"
filenameD = directory+"_.dat"
# Function to get loss from the model filename in the list 'samp'  
def rateloss(iteR):
    for x in iteR:leng = len(x)
    for x in iteR:X= x[leng-9:leng-3]
    return X
def decrate(iteR):
    for x in iteR:leng = len(x)
    for x in iteR:Y = x[leng-51:leng-38]
    return Y
def epoch(iteR):
    for z in iteR:leng = len(z)
    for z in iteR:Z = z[leng-14:leng-10]
    return Z
try:
    os.remove(filenameD)
except:
    pass
# built is list ' samp ' of all models in a directory
samp = []
cwd = os.getcwd()
PATH = cwd+"/"+directory+"/"
files = glob.glob(PATH+"GRU*.t7")
files.sort(key=os.path.getmtime)
line = ("\n".join(files))
samp.append(line)
# clear the memory of any prior files that may have been created
# prevents the accidental printing of memory to the file 
try:
    del line
    del li
except:
    pass
fn = open(filenameD, "a")
count = 0
for line in samp:
    line = line.split()
    for li in line:
        count = count +1
        #if count>2:
        if len(li)>50:
            #print count-2,li
            li = li[-9:-3]
            #skips the first entry then print a comma before every ' li ' written
            # this avoids a tailing comma
            #if count>3:fn.write(", ")
            if count>1:fn.write(", ")
            fn.write(li)            
fn.close() 
"""
num = 0
for n in open(filenameD, "r").read().split(","):
    num = num+1
b = num    
a = 14
"""
f = open(filenameD).read()
f = str(f).split()
a = len(f)
A= str(a)
b = int(a)+1
print "---",A,a
c = a / b
c = 12
#np.arange(0.0, a, c)
#steps = 1
#c = range(b,steps)
iteR = samp    
LosR = rateloss(iteR) 
DecR = decrate(iteR)
E = epoch(iteR)
fname = filenameD
s = np.loadtxt(fname, dtype='float', comments='#', delimiter=",")
#s = (2.8920 , 2.2190 , 2.0573 , 1.9742 , 1.8616 , 1.8021 , 1.7422 , 1.7081 , 1.6884 , 1.6534 , 1.6351 , 1.6167 , 1.6084 , 1.5963 , 1.5953 , 1.5796 , 1.5654 , 1.5635 , 1.5472 , 1.5382 , 1.5329 , 1.5264 , 1.5266 , 1.5185 , 1.5118 , 1.5068 , 1.5075 , 1.5025 , 1.4998 , 1.4988 , 1.4974 , 1.4933 , 1.4945 , 1.4968 , 1.4859 , 1.4848 , 1.4840 , 1.4762 , 1.4718 , 1.4735 , 1.4684 , 1.4658 , 1.4609 , 1.4645 , 1.4587 , 1.4571 , 1.4533 , 1.4508 , 1.4483 , 1.4420 , 1.4363 , 1.4290 , 1.4219 , 1.4170 , 1.4013 , 1.3768 , 1.3657 , 1.3676 , 1.3694 , 1.3784 , 1.3823 , 1.3918 , 1.3867 , 1.3873 , 1.3894 , 1.3933 , 1.4013 , 1.3953 , 1.3955 , 1.3954 , 1.4042 , 1.3995 , 1.3992 , 1.3995 , 1.4001 , 1.3994 , 1.3983 , 1.3922 , 1.3970 )
#t = np.arange(0.0, a, c)
#t = np.arange(0.0, b, c)
e = len(s)
ss = range(0,e)
aa = np.array(ss)
#t = np.arange(0.0, aa, c)
# Note that using plt.subplots below is equivalent to using
# fig = plt.figure() and then ax = fig.add_subplot(111)
fig, ax = plt.subplots(dpi=100)
"""
print t
print"-------------"
print s
print"-------------"
print e
print"-------------"
print ss
"""
ax.plot(aa, s)
DT = time.strftime("%Y-%m-%d:%H")
ax.set(xlabel='DATE: '+DT+'      Samples(Scale = 1 per sample)', ylabel='Training Loss',
       title='Training Loss Plot from Last '+A+' Samples.   Epoch: '+E+' \n Last: ModelLoss: '+LosR+"    DecayRate: "+DecR )

ax.grid()
tm = time.strftime("%Y-%m%d%H%M%S")
Filename = "Last-GRU-network-loss-"+LosR+"-plot-for-Directory-"+directory+"_"+tm+".png"
#print Filename
fig.savefig(Filename)
#plt.show()
#custom = "Last-GRU-network-loss-1.1296-plot-for-Directory-uranbible_2018-0617100544.png"
filename0= Filename
def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]

def draw_blurred_back(img, position, text, font, col, halo_col):
    halo = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(position, text, font = font, fill = halo_col)
    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(position, text, font = font, fill = col)
    return Image.composite(img, blurred_halo, ImageChops.invert(blurred_halo))

if __name__ == '__main__':
    inp = Image.open(filename0)
    inp = inp.resize((640,640), Image.ANTIALIAS)
    font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 35)
    text_title = (255, 30,30) # bright green
    blur_title = (0, 0, 0)   # black
    #textin = (generate_the_word("wordcloud.txt"))
    i2 = draw_blurred_back(inp, (270, 100), "PlotBot", font, text_title, blur_title)
    font0 = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 25)
    i2 = draw_blurred_back(i2, (270, 142), "Live Plot for this", font0, text_title, blur_title)    
    i2 = draw_blurred_back(i2, (270, 175), "Lua text generator.", font0, text_title, blur_title)    
    
    #txt = Image.new('RGBA', i.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
    # get a drawing context
    signature_ = "@Jacknorthrup Instagram and @jacklnorthrup TwitterBot Project" 
    #get length in pixel of signature_
    sizeS,ln = fnt.getsize(signature_)
    #add 15 pixels to right border
    pt = sizeS+25
    width, height = inp.size
    #marginx starting point of signature_
    marginx = pt
    #bottom margin
    marginy = 30
    x = width - marginx
    y = height - marginy
    

    text_sig = (255, 55,30) # bright green
    blur_sig = (0, 0, 0)   # black
    txt=draw_blurred_back(i2,(x,y), signature_, fnt, text_sig, blur_sig)
    out = Image.alpha_composite(i2, txt)
    out.save("TM_POST.png")

#removed keys for privacy reasons
CONSUMER_KEY = key.twiter()[0]
CONSUMER_SECRET = key.twiter()[1]
ACCESS_KEY = key.twiter()[2]
ACCESS_SECRET = key.twiter()[3]

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
f = open("MYTEXT.txt")
text = f.read()
text_model = markovify.Text(text)
STR = (text_model.make_short_sentence(200))
#STR = ("8conv3fc_DSN.caffemodel Layer pool4. Snow capped mouintains Yah right . Dream on !")
# USE BELOW for no signature
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "TM_POST.png"
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')
image = open(PATH,'rb')
response = twitter.upload_media(media=image)
twitter.update_status(status=STR, media_ids=[response['media_id']])

print STR
!showme TM_POST.png
out

from PIL import Image
from PIL import ImageFont, ImageDraw
import random
import time
import textwrap
import glob
import os
try:
    del f0
    del line
except:
    pass
Samp = []
directory = raw_input("Use Directory: ")
#f0= open(title,"w");f.close()

cwd = os.getcwd()
PATH = cwd+"/"+directory
filename = PATH+"_.txt"
try:
    os.remove(filename)
except:
    pass
f0= open(filename,"w")
files = glob.glob(PATH+"/*.t7")
files.sort(key=os.path.getmtime)
line = ("\n".join(files))
if ".t7" in line:
    f0.write(line)
    Samp.append(line)
    print filename
f0.close()    















til = Image.new("RGB",(640,640))
im =  Image.new("RGB",(620,620),(150,150,150))
til.paste(im,(10,10))
til2 = Image.new("RGB",(600,160),(250,250,250))
til.paste(til2,(20,450))
w,h = im.size
text0 = "LUA Text Generator Using maching learning / AI"
def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]
infile = "MYTEXT.txt"    
Text = generate_the_word(infile)
#print text
draw = ImageDraw.Draw(til)
#font = ImageFont.truetype("/home/jack/.fonts/Daubmark.ttf", 30)
font = ImageFont.truetype("/home/jack/.fonts/dontmix.ttf", 20)
lines = textwrap.wrap(Text, width=75)
#print lines
y_text = h
#print "::",y_text
for line in lines:
    width, height = font.getsize(line)
    #print lines,w - width / 2, y_text
    W = (w - width) / 2
    H =  y_text-280
    print "++",W,H
    draw.text(((w - width) / 2, y_text-480), line, font=font, fill= "black")
    #draw.text((100, 100), line, font=font, fill= "black")
    
    y_text += height
    print y_text
    
    
font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 22)
draw.text((20,40), text0, font=font, fill= "red")    
    
tm = time.strftime("%Y-%m%d%H%M%S")

filename = tm+"testtiles.png"
print filename
til.save(filename)
til

# read a text file as a list of lines
# find the last line, change to a file you have
filename = "/home/jack/Desktop/char-rnn/uranbible_.txt"
fileHandle = open (filename,"r" )
lineList = fileHandle.readlines()
fileHandle.close()
line = lineList[-1]
print "This is the loss of the last model: ",line[-9:-3]
print "This is the Epoch: ",line[-14:-10]
print "Current learning_rate: ", line[-51:-38]
print "rnn-size: ", line[-28:-25]


til2 = Image.new("RGB",(600,160),(250,250,250))

# read a text file as a list of lines
# find the last line, change to a file you have
filename = "/home/jack/Desktop/char-rnn/uranbible_.txt"
fileHandle = open (filename,"r" )
lineList = fileHandle.readlines()
fileHandle.close()
line = lineList[-1]
text = "This is the loss of the last model: ",line[-9:-3]
text1 = "This is the Epoch: ",line[-14:-10]
text2 = "Current learning_rate: ", line[-51:-38]
text3 = "rnn-size: ", line[-28:-25]
font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 22)
draw.text((20,40), text0, font=font, fill= "red")
draw.text((20,40), text1, font=font, fill= "red")
draw.text((20,40), text2, font=font, fill= "red")
draw.text((20,40), text3, font=font, fill= "red")

f = open("/home/jack/Desktop/char-rnn/uranbible_.txt").read()
print f


f = open("MYTEXT.txt", "r").readlines()
count = 0
for line in f:
    line = line.replace("\n", "")
    count = count +1
    if count<45:
        print line

from PIL import Image
from PIL import ImageFont, ImageDraw
import textwrap
import time
til = Image.new("RGB",(640,640))
im = Image.new("RGB",(600,500),(210,210,230))
til.paste(im,(20,30))
til2 = Image.new("RGB",(600,160),(230,230,230))
til.paste(til2,(20,450))
w,h = im.size

text0 ="""
 The Most High was a world and an angel of God and the sins of the Father's life in the spiritual 
personality of the earth. The Paradise spirit of the Morning Spirit of God is a being of the spirit of 
God and in the divine different spirit of the Universal Father and the Deity Spirit. The Paradise Father 
is the superficial experience of the Father and the Son of Days and the spiritual father of God and 
provision universes to ask the Father's life in the well-half the ancient personality of the Deity 
Trinity of Deity and the Absolute is the first constellation of the experience of the Paradise Creator 
Son in the long experience of the Paradise Creator Son and the experience of God.
"""
draw = ImageDraw.Draw(til)
#font = ImageFont.truetype("/home/jack/.fonts/Daubmark.ttf", 30)
font = ImageFont.truetype("/home/jack/.fonts/dontmix.ttf", 24)
lines = textwrap.wrap(text0, width=60)
y_text = h
for line in lines:
    
    width, height = font.getsize(line)
    #print lines,w - width / 2, y_text
    draw.text(((w - width) / 2, y_text-450), line, font=font, fill= "black")
    y_text += height

text = """
wiki/GRU-0.002200000000-lm_lstm_epoch_0.39_1.3764.t7:   Iteration 11000 of 1420850
Loss is at 1.3764. _epoch_0.39 shows is is only 39% of a full Epoch.
"""
draw = ImageDraw.Draw(til)
#font = ImageFont.truetype("/home/jack/.fonts/Daubmark.ttf", 30)
font = ImageFont.truetype("/home/jack/.fonts/dontmix.ttf", 30)
lines = textwrap.wrap(text, width=40)
y_text = h
for line in lines:
    
    width, height = font.getsize(line)
    #print lines,w - width / 2, y_text
    draw.text(((w - width) / 2, y_text-30), line, font=font, fill= "black")
    y_text += height
    
tm = time.strftime("%Y-%m%d%H%M%S")

filename = tm+"test.png"
print filename
til.save(filename)
til

til2 = Image.new("RGB",(600,160),(250,250,250))

# read a text file as a list of lines
# find the last line, change to a file you have
filename = "/home/jack/Desktop/char-rnn/uranbible_.txt"
fileHandle = open (filename,"r" )
lineList = fileHandle.readlines()
fileHandle.close()
line = lineList[-1]
text = "This is the loss of the last model: ",line[-9:-3]
text1 = "This is the Epoch: ",line[-14:-10]
text2 = "Current learning_rate: ", line[-51:-38]
text3 = "rnn-size: ", line[-28:-25]
font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 22)
draw.text((20,40), text0, font=font, fill= "red")
draw.text((20,40), text1, font=font, fill= "red")
draw.text((20,40), text2, font=font, fill= "red")
draw.text((20,40), text3, font=font, fill= "red")

from PIL import Image
from PIL import ImageFont, ImageDraw
import textwrap
til = Image.new("RGB",(640,640))
#image = "img = 'wiki/Training-Loss-Graph-forwiki_2018-0609062255.png'"
im = Image.open("Last-GRU-network-loss-1.1179-plot-for-Directory-uranbible_2018-0617131414.png") #600x400

til.paste(im,(20,35))
til2 = Image.new("RGB",(600,160),(250,250,250))
til.paste(til2,(20,450))
w,h = im.size
#fname = "Here shows the effect of changing the LearningRate"
fname = "Filename parsed for data:"
# read a text file as a list of lines
# find the last line, change to a file you have
filename = "/home/jack/Desktop/char-rnn/uranbible_.txt"
fileHandle = open (filename,"r" )
lineList = fileHandle.readlines()
fileHandle.close()
line = lineList[-1]
text0 = "This is the loss of the last model: ",line[-9:-3]
text1 = "This is the Epoch: ",line[-14:-10]
text2 = "Current learning_rate: ", line[-51:-38]
text3 = "rnn-size: ", line[-28:-25]

text = str(line[-51:])
SPACE = "-----------------------------------------------"
text0 = str(text0)
text1 = str(text1)
text2 = str(text2)
text3 = str(text3)
text3 = str(text3)
draw = ImageDraw.Draw(til)
font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 18)
draw.text((70,450), fname, font=font, fill= "black")
font = ImageFont.truetype("/home/jack/.fonts/dontmix.ttf", 20)
#draw.text((320,450), fname0, font=font, fill= "black")
#font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 16)
#draw.text((70,474), text0, font=font, fill= "red")
font = ImageFont.truetype("/home/jack/.fonts/dontmix.ttf", 22)
draw.text((70,472), text, font=font, fill= "navy")
draw.text((70,490), SPACE, font=font, fill= "black")
draw.text((70,510), text0, font=font, fill= "navy")  
draw.text((70,530), text1, font=font, fill= "navy")    
draw.text((70,550), text2, font=font, fill= "navy")    
draw.text((70,570), text3, font=font, fill= "navy")    
#draw.text((70,552), text4, font=font, fill= "navy")    
#draw.text((70,572), text5, font=font, fill= "navy")




tm = time.strftime("%Y-%m%d%H%M%S")

filename = tm+"testtiles.png"
print filename
til.save(filename)

til




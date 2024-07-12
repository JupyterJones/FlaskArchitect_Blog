!ls images

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
PATH = "clouddream/backup/deepdream/images/"
im = Image.open(PATH+"8conv3fc_DSN-pool4-100-mountain.jpg")
im

!sudo locate twython/__init__.py

#ONE TIME MANUAL POSTS
#!/home/jack/anaconda2/python
import random
from random import randint
import time
import markovify
import os
import sys
import key
sys.path.insert(1, "/home/jack/Desktop/pycode/vpython2")
import twython
from twython import Twython
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter

#custom = "/home/jack/Desktop/post/ball009.png"
#custom = "/home/jack/Desktop/PROCESSING/color-wander/images/kk.png"
#custom = PAth+"gg.png"
custom = "junk2/PalletteTemp.jpg"

PATH = "clouddream/backup/deepdream/images/"
custom = PATH+"8conv3fc_DSN-pool4-100-mountain.jpg"

#custom = "/home/jack/Desktop/GRAPHICS/otoro-net/0001jav.png"
#custom = "/home/jack/Desktop/GRAPHICS/otoro-net/0002jav.png"

#custom = "/home/jack/Desktop/GRAPHICS/otoro-net/0003jav.png"
#custom = "/home/jack/Desktop/GRAPHICS/otoro-net/0004jav.png"
#custom = "junk/PalletteTemp.png"
filename0=(custom)
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
    font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 30)
    text_title = (255, 255,230) # bright green
    blur_title = (0, 0, 0)   # black
    #textin = (generate_the_word("wordcloud.txt"))
    i2 = draw_blurred_back(inp, (15, 4), "A Couple DeepDreams", font, text_title, blur_title)
    font0 = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
    i2 = draw_blurred_back(i2, (15, 40), "8conv3fc_DSN-CaffeModel", font0, text_title, blur_title)    
    i2 = draw_blurred_back(i2, (15, 60), "pool4", font0, text_title, blur_title)    
    
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
    

    text_sig = (255, 255,230) # bright green
    blur_sig = (0, 0, 0)   # black
    txt=draw_blurred_back(i2,(x,y), signature_, fnt, text_sig, blur_sig)
    out = Image.alpha_composite(i2, txt)
    out.save("copies/TM_POST.png")

#removed keys for privacy reasons
CONSUMER_KEY = key.twiter()[0]
CONSUMER_SECRET = key.twiter()[1]
ACCESS_KEY = key.twiter()[2]
ACCESS_SECRET = key.twiter()[3]

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
f = open("codetalk.txt")
text = f.read()
text_model = markovify.Text(text)
#STR = (text_model.make_short_sentence(140))
STR = ("8conv3fc_DSN.caffemodel Layer pool4. Snow capped mouintains Yah right . Dream on !")
# USE BELOW for no signature
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "copies/TM_POST.png"
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')
image = open(PATH,'rb')
response = twitter.upload_media(media=image)
twitter.update_status(status=STR, media_ids=[response['media_id']])

!showme copies/TM_POST.png

!ls Images

from PIL import Image
im = Image.open("Images/20171130-123049.jpg")
im.size

from PIL import Image
PATH = "/home/jack/Desktop/PROCESSING/color-wander/images/"
im = Image.open(PATH+"0007.png")
im

f = open("codetalk.txt")
text = f.read()
text_model = markovify.Text(text)
STR = (text_model.make_short_sentence(140))
print STR

!showme copies/TM_POST1.jpg

!mkdir copies

def pil_image():
    ''' A View that Returns a PNG Image generated using PIL'''

    from PIL import Image, ImageDraw 

    size = (100,50)             # size of the image to create
    im = Image.new('RGB', size) # create the image
    draw = ImageDraw.Draw(im)   # create a drawing object that is
                                # used to draw on the new image
    red = (255,0,0)    # color of our text
    text_pos = (10,10) # top-left position of our text
    text = "Hello World!" # text to draw
    # Now, we'll do the drawing: 
    draw.text(text_pos, text, fill=red)
    
    del draw # I'm done drawing so I don't need this anymore
    
    # We need an HttpResponse object with the correct mimetype
    response = HttpResponse(mimetype="image/png")
    # now, we tell the image to save as a PNG to the 
    # provided file-like object
    im.save("test.png", 'PNG')

    return im # and we're done!

pil_image()

def pil_image():
    ''' A View that Returns a PNG Image generated using PIL'''

    from PIL import Image, ImageDraw 

    size = (100,50)             # size of the image to create
    im = Image.new('RGB', size) # create the image
    draw = ImageDraw.Draw(im)   # create a drawing object that is
                                # used to draw on the new image
    red = (255,0,0)    # color of our text
    text_pos = (10,10) # top-left position of our text
    text = "Hello World!" # text to draw
    # Now, we'll do the drawing: 
    draw.text(text_pos, text, fill=red)
    
    del draw # I'm done drawing so I don't need this anymore
    
    # We need an HttpResponse object with the correct mimetype
    #response = HttpResponse(mimetype="image/png")
    # now, we tell the image to save as a PNG to the 
    # provided file-like object
    im.save("test.png", 'PNG')

    return im # and we're done!

pil_image()

%%writefile saltpost
#!/bin/bash

while true; do
  python saltpost.py
  echo "posted :"
  date
  sleep 800s
done

%%writefile saltpost
#!/bin/bash

while true; do
  python saltpost.py
  echo "posted :"
  date
  sleep 800s
done

#%%writefile saltpost.py
#ONE TIME MANUAL POSTS
#!/home/jack/anaconda2/python
import random
from random import randint
import time
import markovify
import os
import sys
sys.path.insert(1, "/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
import Key
def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]

def draw_text_with_halo(img, position, text, font, col, halo_col):
    halo = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(position, text, font = font, fill = halo_col)
    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(position, text, font = font, fill = col)
    return Image.composite(img, blurred_halo, ImageChops.invert(blurred_halo))

def rndcolor():
    r = randint(50,255)
    g = randint(50,255)
    b = randint(50,255)
    rndcolor = (r,g,b) 
    return rndcolor
def get_random_line(file_name):
    total_bytes = os.stat(file_name).st_size 
    random_point = random.randint(0, total_bytes)
    file = open(file_name)
    file.seek(random_point)
    file.readline() # skip this line to clear the partial line
    return file.readline()



if __name__ == '__main__':
    #nap = randint(500,1200)
    #time.sleep(nap)
    #isize = (640,640)     
    #inp = Image.new('RGB', isize)
    
    path2 = r"/home/jack/Desktop/pycode/vpython2/TrigonometryBot/images/"
    #path2 = r"bugs/advertisements1800/"
    random_filename2 = random.choice([
        y for y in os.listdir(path2)
        if os.path.isfile(os.path.join(path2, y))
    ])

    img1a = path2+"/"+random_filename2
    inp=Image.open(img1a)    
    inp = inp.resize((640,640), Image.NEAREST)
    
    
    font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 40)
    text_col = (255, 255,230) # bright green
    halo_col = (0, 0, 0)   # black
    textin = (generate_the_word("/home/jack/Desktop/imagebot/wordcloud.txt"))
    i2 = draw_text_with_halo(inp, (15, 8), "SaltMan", font, text_col, halo_col)
    
    #txt = Image.new('RGBA', i.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
    # get a drawing context
    width, height = inp.size
    marginx = 225
    marginy = 35
    x = width - marginx
    y = height - marginy
    signature_ = "The TwitterBot Project" 
    #text_col2 = (150, 255, 150) # bright green
    #halo_col2 = (0, 0, 0)   # black
    text_col2 = (255, 255,230) # bright green
    halo_col2 = (0, 0, 0)   # black
    #text_col2 = (0, 0, 0)  # bright green
    #halo_col2 = (255, 255,230)  # black    
    txt1=draw_text_with_halo(i2,(x,y), signature_, fnt, text_col2, halo_col2)
    
    
    
    # get a font
    fs=randint(15,24)
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", fs)
    # get a drawing context
    width, height = inp.size
    marginx = 225
    marginy = 35
    x = width - marginx
    y = height - marginy
    signature_ = "The TwitterBot Project" 
    #text_col2 = (150, 255, 150) # bright green
    #halo_col2 = (0, 0, 0)   # black
    #text_col2 = (255, 255,230) # bright green
    text_col2 = rndcolor()
    halo_col2 = (0, 0, 0)   # black
    #text_col2 = (0, 0, 0)  # bright green
    #halo_col2 = (255, 255,230)  # black 
    yy=randint(70,290)
    xx=randint(5,60)
    #iword = (text_model.make_short_sentence(50))
    file_name = '/home/jack/Desktop/imagebot/saltman.txt'
    iword = get_random_line(file_name)
    
    txt3=draw_text_with_halo(txt1,(xx,yy), iword, fnt, text_col2, halo_col2)
   
    vv=randint(320,530)
    vvv=randint(5,10)
    #iword = (text_model.make_short_sentence(50))
    file_name = '/home/jack/Desktop/imagebot/saltman.txt'
    lword = get_random_line(file_name)        
    text_col3 = rndcolor()
    fs2=randint(15,24)
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", fs2)
    txt=draw_text_with_halo(txt3,(vvv,vv), lword, fnt, text_col3, halo_col2)
     
    out = Image.alpha_composite(i2, txt)
    out.save("tmp/TM_POST.jpg")

#removed keys for privacy reasons
CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#path = 'images/NewFolder'
#f = open("Mine.txt")
#text = f.read()
# Build the model.
#text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
#http://paulbourke.net/fractals/
#STR = (text_model.make_short_sentence(140))
#random.choice(open('Mine.txt').readlines())



file_name = '/home/jack/Desktop/imagebot/Mine.txt'
STR = get_random_line(file_name)

#STR = ("Sometimes we have visitors at night. If lucky we don't wake up.")
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "tmp/TM_POST.jpg"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

photo = open(PATH,'rb')
#response = twitter.upload_media(media=photo)
#twitter.update_status(status=STR, media_ids=[response['media_id']])
print STR


!showme /home/jack/Desktop/imagebot/images/Sranger-Tri-001-crop2b.jpg

import random
from random import randint
import time
import markovify
import os
import sys
sys.path.insert(1, "/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
import Key
CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
file_name = '/home/jack/Desktop/imagebot/Mine.txt'
STR = get_random_line(file_name)
#STR = ("Sometimes we have visitors at night. If lucky we don't wake up.")
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "tmp/TM_POST1.jpg"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])
print STR


!showme tmp/TM_POST1.jpg

import genim
path="junk/"
genim.RanFile(path)

!showme tmp/TM_POST.jpg

#ONE TIME MANUAL POSTS
#!/home/jack/anaconda2/python
import random
from random import randint
import time
import markovify
import os
import Key
import sys
sys.path.insert(1, "/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
nap = randint(10,35)
time.sleep(nap)
path = r"publish/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)
def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]

def draw_text_with_halo(img, position, text, font, col, halo_col):
    halo = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(position, text, font = font, fill = halo_col)
    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(position, text, font = font, fill = col)
    return Image.composite(img, blurred_halo, ImageChops.invert(blurred_halo))

if __name__ == '__main__':
    inp = Image.open(filename0)
    font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 40)
    text_col = (255, 255,230) # bright green
    halo_col = (0, 0, 0)   # black
    textin = (generate_the_word("wordcloud.txt"))
    i2 = draw_text_with_halo(inp, (15, 8), "I_FollowBack", font, text_col, halo_col)
    
    #txt = Image.new('RGBA', i.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
    # get a drawing context
    width, height = inp.size
    marginx = 225
    marginy = 35
    x = width - marginx
    y = height - marginy
    signature_ = "The TwitterBot Project" 
    #text_col2 = (150, 255, 150) # bright green
    #halo_col2 = (0, 0, 0)   # black
    text_col2 = (255, 255,230) # bright green
    halo_col2 = (0, 0, 0)   # black
    txt=draw_text_with_halo(i2,(x,y), signature_, fnt, text_col2, halo_col2)
    out = Image.alpha_composite(i2, txt)
    out.save("tmp/TM_POST.jpg")

#removed keys for privacy reasons
#removed keys for privacy reasons
CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#path = 'images/NewFolder'
f = open("art.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
#http://paulbourke.net/fractals/
STR = (text_model.make_short_sentence(140))
#STR = ("#All_in_One - #WordCloud #Create - Added ability to randomly choose an image background  #Automated")
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "tmp/TM_POST.jpg"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

#photo = open(PATH,'rb')
#response = twitter.upload_media(media=photo)
#twitter.update_status(status=STR, media_ids=[response['media_id']])


Easy to customize with various title sizes, colors. and locations. 

%%writefile wordcloud.txt
Python
Programming
ImageBot
Enjoy
f4f always
Just for You
Good Stuff
Computer Graphics
Python Fun
Python Graphics
Generator
Followback
Word Cloud
Graphics
Fun w/Python
Python Stuff
PYTHON !!!
Follow4Follow
Love`en Python
Creative Python
Graphic Fun
ImageBot
Programming

%%writefile titlenpost
#!/bin/bash

while true; do
  python titlenpost.py
  echo "posted :"
  date
  sleep 1800s
done

%%writefile titlenpost
#!/bin/bash

while true; do
  python titlenpost.py
  echo "posted :"
  date
  sleep 1500s
done

!./titlenpost

#Great signature
import sys
import os
import time
import random
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
path = r"publish/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)
def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]

def draw_text_with_halo(img, position, text, font, col, halo_col):
    halo = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(position, text, font = font, fill = halo_col)
    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(position, text, font = font, fill = col)
    return Image.composite(img, blurred_halo, ImageChops.invert(blurred_halo))

if __name__ == '__main__':
    inp = Image.open(filename0)
    font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 40)
    text_col = (255, 255,230) # bright green
    halo_col = (0, 0, 0)   # black
    textin = (generate_the_word("wordcloud.txt"))
    i2 = draw_text_with_halo(inp, (15, 8), textin, font, text_col, halo_col)
    
    #txt = Image.new('RGBA', i.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
    
    width, height = inp.size
    marginx = 225
    marginy = 35
    x = width - marginx
    y = height - marginy
    signature_ = "The TwitterBot Project" 
    #text_col2 = (150, 255, 150) # bright green
    #halo_col2 = (0, 0, 0)   # black
    text_col2 = (255, 255,230) # bright green
    halo_col2 = (0, 0, 0)   # black
    txt=draw_text_with_halo(i2,(x,y), signature_, fnt, text_col2, halo_col2)
    # get a drawing context
    d = ImageDraw.Draw(txt)
    out = Image.alpha_composite(i2, txt)
    filename = time.strftime("tmp/%Y%m%d%H%M%S.jpg")


out

!cp key.py Key.py


!showme tmp/TM_POST1.jpg





#%%writefile titlenpost.py
#!/home/jack/anaconda2/python
import random
from random import randint
import time
import markovify
import os
import sys
import Key
sys.path.insert(1, "/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
#nap = randint(100,635)
#time.sleep(nap)
path = r"output/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)
def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]

def draw_text_with_halo(img, position, text, font, col, halo_col):
    halo = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(position, text, font = font, fill = halo_col)
    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(position, text, font = font, fill = col)
    return Image.composite(img, blurred_halo, ImageChops.invert(blurred_halo))

if __name__ == '__main__':
    inp = Image.open(filename0)
    font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 40)
    text_col = (255, 255,230) # bright green
    halo_col = (0, 0, 0)   # black
    textin = (generate_the_word("/home/jack/Desktop/imagebot/wordcloud.txt"))
    i2 = draw_text_with_halo(inp, (15, 8), textin, font, text_col, halo_col)
    
    #txt = Image.new('RGBA', i.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
    # get a drawing context
    width, height = inp.size
    marginx = 225
    marginy = 35
    x = width - marginx
    y = height - marginy
    signature_ = "" 
    #text_col2 = (150, 255, 150) # bright green
    #halo_col2 = (0, 0, 0)   # black
    text_col2 = (255, 255,230) # bright green
    halo_col2 = (0, 0, 0)   # black
    txt=draw_text_with_halo(i2,(x,y), signature_, fnt, text_col2, halo_col2)
    out = Image.alpha_composite(i2, txt)
    out.save("tmp/TM_POST1.jpg")


#removed keys for privacy reasons
CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#path = 'images/NewFolder'
f = open("/home/jack/Desktop/imagebot/codetalk.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
#http://paulbourke.net/fractals/
STR = (text_model.make_short_sentence(140))
#STR = ("#All_in_One - #WordCloud #Create - Added ability to randomly choose an image background  #Automated")
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "tmp/TM_POST1.jpg"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])

!showme tmp/TM_POST1.jpg

!locate codetalk

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
#images/perlin001-art.png
custom = "images/paper002.jpg"
filename0=(custom)
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
    font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 40)
    text_title = (255, 255,230) # bright green
    blur_title = (0, 0, 0)   # black
    #textin = (generate_the_word("wordcloud.txt"))
    i2 = draw_blurred_back(inp, (15, 4), "Processing JS", font, text_title, blur_title)
    
    #txt = Image.new('RGBA', i.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
    # get a drawing context
    signature_ = "@Jacknorthrup Instagram and @jacklnorthrup TwitterBot Project" 
    #get length in pixel of signature_
    sizeS,ln = fnt.getsize(signature_)
    #add 15 pixels to right border
    pt = sizeS+15
    width, height = inp.size
    #marginx starting point of signature_
    marginx = pt
    #bottom margin
    marginy = 35
    x = width - marginx
    y = height - marginy
    

    text_sig = (255, 255,230) # bright green
    blur_sig = (0, 0, 0)   # black
    txt=draw_blurred_back(i2,(x,y), signature_, fnt, text_sig, blur_sig)
    out = Image.alpha_composite(i2, txt)
    out.save("copies/test_image.jpg")
    im=Image.open("copies/test_image.jpg")

import sqlite3
from time import sleep 
import sys
conn = sqlite3.connect('/home/jack/snippet.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
filein = open("allsnippets.txt","w");filein.close()
filein = open("allsnippets.txt","a")
for row in c.execute('SELECT rowid, * FROM snippet'):    

    info= (row)[2]
    info = str(info)
    info = info+"\n\n"
    filein.write(info)
    
    
filein.close()    

import sqlite3
from time import sleep 
import sys
conn = sqlite3.connect('/home/jack/snippet.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
filein = open("allsnippets.txt","w");filein.close()
filein = open("allsnippets.txt","a")
for row in c.execute('SELECT rowid, * FROM snippet'):    
    count=count+1
    sleep(.25)
    print "ID : ",(row)[0],(row)[2]," -- KEYWORDS",(row)[3],"\n"
    if count > req:
        conn.close()
        sys.exit()

import sqlite3
import sys
conn = sqlite3.connect('/home/jack/snippet.db')
conn.text_factory = str
c = conn.cursor()
filein = open("allsnippets.txt","w");filein.close()
filein = open("allsnippets.txt","a")
rows = c.execute('SELECT snippet FROM snippet') 
for row in rows:
     print row

import sqlite3
import sys
from time import sleep
conn = sqlite3.connect('/home/jack/snippet.db')
conn.text_factory = str
c = conn.cursor()
filein = open("allsnippets.txt","w");filein.close()
filein = open("allsnippets.txt","a")
rows = c.execute('SELECT rowid, * FROM snippet') 
for row in rows:
    #sleep(1)
    #print row[2]
    filein.write(row[2])

import sqlite3
import sys
conn = sqlite3.connect('/home/jack/snippet.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
search = raw_input("Search : ")
for row in c.execute('SELECT rowid, * FROM snippet WHERE keywords MATCH ?', (search,)):    
    count=count+1
    print "ID : ",(row)[0],(row)[2]," -- KEYWORDS",(row)[3],"\n"
    if count > req:
        conn.close()
        sys.exit()

import sqlite3
import sys
conn = sqlite3.connect('/home/jack/snippet.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
search = raw_input("Search : ")
for row in c.execute('SELECT rowid, * FROM snippet WHERE snippet MATCH ?', (search,)):    
    count=count+1
    print "ID : ",(row)[0],(row)[2]," -- KEYWORDS",(row)[3],"\n"
    if count > req:
        conn.close()
        sys.exit()
        
------------------        

import sqlite3
import base64
conn = sqlite3.connect('/home/jack/snippet.db') 
c = conn.cursor()
conn.text_factory = str
file = """
import json
import sys
from time import sleep
import sqlite3
import csv
conn = sqlite3.connect('notebooks.db')
conn.text_factory=str 
c = conn.cursor()
#c.execute("DELETE title, line FROM ipynb where rowid MATCH '362113' "):
#c.execute("delete from ipynb where rowid=362113;"):
c.execute("DELETE FROM ipynb WHERE rowid = ?", (362113,))
conn.commit()
conn.close()
        
"""
keywords = "delete sqlite by rowid delete id rowid ROWID"
encodedlistvalue=base64.b64encode(file)
c.execute("INSERT INTO snippet VALUES (?,?,?)", (encodedlistvalue, file, keywords))
conn.commit()
conn.close()

%%writefile UnicodeToAscii.py
def unicodetoascii(text):

    uni2ascii = {
            ord('\xe2\x80\x99'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\x9c'.decode('utf-8')): ord('"'),
            ord('\xe2\x80\x9d'.decode('utf-8')): ord('"'),
            ord('\xe2\x80\x9e'.decode('utf-8')): ord('"'),
            ord('\xe2\x80\x9f'.decode('utf-8')): ord('"'),
            ord('\xc3\xa9'.decode('utf-8')): ord('e'),
            ord('\xe2\x80\x9c'.decode('utf-8')): ord('"'),
            ord('\xe2\x80\x93'.decode('utf-8')): ord('-'),
            ord('\xe2\x80\x92'.decode('utf-8')): ord('-'),
            ord('\xe2\x80\x94'.decode('utf-8')): ord('-'),
            ord('\xe2\x80\x94'.decode('utf-8')): ord('-'),
            ord('\xe2\x80\x98'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\x9b'.decode('utf-8')): ord("'"),

            ord('\xe2\x80\x90'.decode('utf-8')): ord('-'),
            ord('\xe2\x80\x91'.decode('utf-8')): ord('-'),

            ord('\xe2\x80\xb2'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\xb3'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\xb4'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\xb5'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\xb6'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\xb7'.decode('utf-8')): ord("'"),

            ord('\xe2\x81\xba'.decode('utf-8')): ord("+"),
            ord('\xe2\x81\xbb'.decode('utf-8')): ord("-"),
            ord('\xe2\x81\xbc'.decode('utf-8')): ord("="),
            ord('\xe2\x81\xbd'.decode('utf-8')): ord("("),
            ord('\xe2\x81\xbe'.decode('utf-8')): ord(")"),

                            }
    return text.decode('utf-8').translate(uni2ascii).encode('ascii')

#print unicodetoascii("weren\xe2\x80\x99t")  

import UnicodeToAscii
UnicodeToAscii.unicodetoascii()

import UnicodeToAscii
text = """
'\xe2\x81\xbafd fdfdf df \xe2\x81\xbb decode \xe2\x81\xbc code 'utf-8\xe2\x81\xbd' 
code'\xe2\x81\xbe'.decode('utf-8'))"""
UnicodeToAscii.unicodetoascii(text)

import sqlite3
import sys
conn = sqlite3.connect('/home/jack/snippet.db')
conn.text_factory = str
c = conn.cursor()
count=0;req=200
search = raw_input("Search : ")
for row in c.execute('SELECT rowid, * FROM snippet WHERE snippet MATCH ?', (search,)):    
    count=count+1
    print "ID : ",(row)[0],(row)[2]," -- KEYWORDS",(row)[3],"\n"
    if count > req:
        conn.close()
        sys.exit()

import sqlite3
import base64
conn = sqlite3.connect('/home/jack/snippet.db') 
c = conn.cursor()
conn.text_factory = str
file = """

"""
keywords = """

"""
encodedlistvalue=base64.b64encode(file)
c.execute("INSERT INTO snippet VALUES (?,?,?)", (encodedlistvalue, file, keywords))
conn.commit()
conn.close()

import os
import sys
from PIL import Image
import shutil
import time
import random

filename0=("images/sun002.png")
#filename1=("/home/jack/Desktop/imagebot/instagram/20170828173214.png")
filename1=("/home/jack/Desktop/Processing/Processing/images/experiment000a.png")
shutil.copy2(filename0, 'copies/') # complete target filename given
shutil.copy2(filename1, 'copies/')# target filename is /dst/dir/file.ext

aa = Image.open(filename0).convert("RGB")
#bb = Image.open("/home/jack/Documents/GG.jpg").convert("RGB")
bb = Image.open(filename1).convert("RGB")
xx=aa.resize((640,640), Image.NEAREST)
yy=bb.resize((640,640), Image.NEAREST)
xx.save("copies/aa.png")
yy.save("copies/bb.png")
src = Image.open('copies/aa.png').convert('RGB')
dst = Image.open('copies/bb.png').convert('RGB')
src.save("copies/aa.png")
dst.save("copies/bb.png")



n = 5 #number of partitions per channel.


src_handle = Image.open("copies/bb.png")
dst_handle = Image.open("copies/aa.png")
src = src_handle.load()
dst = dst_handle.load()
assert src_handle.size[0]*src_handle.size[1] == dst_handle.size[0]*dst_handle.size[1],"images must be same size"

def makePixelList(img):
    l = []
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            l.append((x,y))
    return l

lsrc = makePixelList(src_handle)
ldst = makePixelList(dst_handle)

def sortAndDivide(coordlist,pixelimage,channel): #core
    global src,dst,n
    retlist = []
    #sort
    coordlist.sort(key=lambda t: pixelimage[t][channel])
    #divide
    partitionLength = int(len(coordlist)/n)
    if partitionLength <= 0:
        partitionLength = 1
    if channel < 2:
        for i in range(0,len(coordlist),partitionLength):
            retlist += sortAndDivide(coordlist[i:i+partitionLength],pixelimage,channel+1)
    else:
        retlist += coordlist
    return retlist

print(src[lsrc[0]])

lsrc = sortAndDivide(lsrc,src,0)
ldst = sortAndDivide(ldst,dst,0)

for i in range(len(ldst)):
    dst[ldst[i]] = src[lsrc[i]]
    
    

filename = time.strftime("images/exchange%Y%m%d%H%M%S.png")
dst_handle.save(filename)

shutil.copy2(filename, "copies/")
print filename

# %load titlenpost.py
#!/home/jack/anaconda2/python
import random
from random import randint
import time
import markovify
import os
import sys
import Key
sys.path.insert(1, "/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
nap = randint(100,635)
time.sleep(nap)
path = r"output/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)
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
    font = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 30)
    text_title = (255, 255,230) # bright green
    blur_title = (0, 0, 0)   # black
    #textin = (generate_the_word("wordcloud.txt"))
    i2 = draw_blurred_back(inp, (15, 4), "Python Generated Art", font, text_title, blur_title)
    
    #txt = Image.new('RGBA', i.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
    # get a drawing context
    signature_ = "@Jacknorthrup Instagram and @jacklnorthrup TwitterBot Project" 
    #get length in pixel of signature_
    sizeS,ln = fnt.getsize(signature_)
    #add 15 pixels to right border
    pt = sizeS+12
    width, height = inp.size
    #marginx starting point of signature_
    marginx = pt
    #bottom margin
    marginy = 35
    x = width - marginx
    y = height - marginy    
    text_sig = (255, 255,230) # bright green
    blur_sig = (0, 0, 0)   # black
    txt=draw_blurred_back(i2,(x,y), signature_, fnt, text_sig, blur_sig)
    out = Image.alpha_composite(i2, txt)
    out.save("tmp/TM_POST1.jpg")


#removed keys for privacy reasons
CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#path = 'images/NewFolder'
f = open("/home/jack/Desktop/imagebot/codetalk.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
#http://paulbourke.net/fractals/
STR = (text_model.make_short_sentence(140))
#STR = ("#All_in_One - #WordCloud #Create - Added ability to randomly choose an image background  #Automated")
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "tmp/TM_POST1.jpg"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])

#%%writefile titlenpost.py
#!/home/jack/anaconda2/python
import random
from random import randint
import time
import markovify
import os
import sys
import Key
sys.path.insert(1, "/home/jack/anaconda2/envs/py27/lib/python2.7/site-packages")
import twython
from twython import Twython
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter
#nap = randint(100,635)
#time.sleep(nap)
path = r"output/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
#filename0=(path+base_image)
filename0 ="Images/segmented20171201092551.png"

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
    #fnt = "/home/jack/.fonts/dontmix.ttf"
    fnt = "/home/jack/.fonts/Exo-Black.ttf"
    font = ImageFont.truetype(fnt, 30)
    text_title = (255, 255,230) # bright green
    blur_title = (0, 0, 0)   # black
    #textin = (generate_the_word("wordcloud.txt"))
    #i2 = draw_blurred_back(inp, (15, 4), "Python Generated Art", font, text_title, blur_title)
    i2 = draw_blurred_back(inp, (45, 35), "Python Generated Art", font, text_title, blur_title)
    
    #txt = Image.new('RGBA', i.size, (255,255,255,0))

    # get a font
    fnt = "/home/jack/.fonts/dontmix.ttf"
    #fnt = "/home/jack/.fonts/Exo-Black.ttf"    
    
    #fnt = ImageFont.truetype(fnt, 20)
    fnt = ImageFont.truetype(fnt, 24)
    # get a drawing context
    signature_ = "@Jacknorthrup Instagram and @jacklnorthrup TwitterBot Project" 
    #get length in pixel of signature_
    sizeS,ln = fnt.getsize(signature_)
    #add 15 pixels to right border
    pt = sizeS+12
    width, height = inp.size
    #marginx starting point of signature_
    marginx = pt
    #bottom margin
    #marginy = 35
    marginy = 55
    x = width - marginx
    y = height - marginy    
    text_sig = (255, 255,230) # bright green
    blur_sig = (0, 0, 0)   # black
    txt=draw_blurred_back(i2,(x,y), signature_, fnt, text_sig, blur_sig)
    out = Image.alpha_composite(i2, txt)
    out.save("tmp/TM_POST1.jpg")


#removed keys for privacy reasons
CONSUMER_KEY = Key.twiter()[0]
CONSUMER_SECRET = Key.twiter()[1]
ACCESS_KEY = Key.twiter()[2]
ACCESS_SECRET = Key.twiter()[3]

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#path = 'images/NewFolder'
f = open("/home/jack/Desktop/imagebot/codetalk.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
#http://paulbourke.net/fractals/
STR = (text_model.make_short_sentence(140))
#STR = " #Python Segmentation Art"
#STR = ("#All_in_One - #WordCloud #Create - Added ability to randomly choose an image background  #Automated")
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "tmp/TM_POST1.jpg"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

photo = open(PATH,'rb')
#response = twitter.upload_media(media=photo)
#twitter.update_status(status=STR, media_ids=[response['media_id']])

!showme tmp/TM_POST1.jpg

!ls /home/jack/Desktop/post

!ls tmp

!showme /home/jack/Desktop/PROCESSING/color-wander/images/kk.png

import sys
from PIL import Image
import shutil
import time
import random
import os, errno
try:
    os.makedirs("instagram/")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
try:
    os.makedirs("junk2/")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise        
filename1='tmp/seg001.png'
filename0='/home/jack/Desktop/PROCESSING/color-wander/images/kk.png'
shutil.copy2(filename0, 'instagram/') # complete target filename given
shutil.copy2(filename1, 'instagram/')# target filename is /dst/dir/file.ext

aa = Image.open(filename0).convert("RGB")
#bb = Image.open("/home/jack/Documents/GG.jpg").convert("RGB")
bb = Image.open(filename1).convert("RGB")
xx=aa.resize((640,640), Image.NEAREST)
yy=bb.resize((640,640), Image.NEAREST)
xx.save("junk2/aa.png")
yy.save("junk2/bb.png")
src = Image.open('junk2/aa.png').convert('RGB')
dst = Image.open('junk2/bb.png').convert('RGB')
src.save("junk2/aa.png")
dst.save("junk2/bb.png")
n = 5 #number of partitions per channel.
src_handle = Image.open("junk2/bb.png")
dst_handle = Image.open("junk2/aa.png")
src = src_handle.load()
dst = dst_handle.load()
assert src_handle.size[0]*src_handle.size[1] == dst_handle.size[0]*dst_handle.size[1],"images must be same size"

def makePixelList(img):
    l = []
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            l.append((x,y))
    return l

lsrc = makePixelList(src_handle)
ldst = makePixelList(dst_handle)

def sortAndDivide(coordlist,pixelimage,channel): #core
    global src,dst,n
    retlist = []
    #sort
    coordlist.sort(key=lambda t: pixelimage[t][channel])
    #divide
    partitionLength = int(len(coordlist)/n)
    if partitionLength <= 0:
        partitionLength = 1
    if channel < 2:
        for i in range(0,len(coordlist),partitionLength):
            retlist += sortAndDivide(coordlist[i:i+partitionLength],pixelimage,channel+1)
    else:
        retlist += coordlist
    return retlist

print(src[lsrc[0]])

lsrc = sortAndDivide(lsrc,src,0)
ldst = sortAndDivide(ldst,dst,0)

for i in range(len(ldst)):
    dst[ldst[i]] = src[lsrc[i]]
    
    
filename = time.strftime("junk2/PalletteTemp.jpg")

dst_handle.save(filename)

shutil.copy2(filename, "instagram/")
print filename

!showme junk2/PalletteTemp.jpg


!showme junk2/aa.png

# Simple bijective function
#   Basically encodes any integer into a base(n) string,
#     where n is ALPHABET.length.
#   Based on pseudocode from http://stackoverflow.com/questions/742013/how-to-code-a-url-shortener/742047#742047

ALPHABET = list("abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
  # make your own alphabet using:
  # (('a'..'z').to_a + ('A'..'Z').to_a + (0..9).to_a).shuffle.join

def bijective_encode(i):
    # from http://refactormycode.com/codes/125-base-62-encoding
    if i == 0:
        return ALPHABET[0]
    s = ''
    base = len(ALPHABET)
    while i > 0:
        s += ALPHABET[i % base]
        i /= base
    return s[::-1] # reverse string


def bijective_decode(s):
    # based on base2dec() in Tcl translation 
    # at http://rosettacode.org/wiki/Non-decimal_radices/Convert#Ruby
    i = 0
    base = len(ALPHABET)
    for char in s:
        i = i * base + ALPHABET.index(char)
    return i

# Two little demos:

numbers = 1234567890
result = bijective_encode(numbers)
print result #xyz

letters = 'Jack Northrup'
new_number = bijective_decode(letters)
print new_number #66

import pickledb
db = pickledb.load('example.db', False)


tx = db.get('key')
print tx




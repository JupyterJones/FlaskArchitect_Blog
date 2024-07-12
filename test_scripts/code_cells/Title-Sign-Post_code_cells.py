!mkdir /home/jack/hidden

import sys
sys.path.append("/home/jack/hidden") # go to parent dir
import key
print(KEY())

%%writefile KEYtest.py
def KEY():
    key= "This is a key"
    return (key)



import KEYtest
print(KEY())


%%writefile /home/jack/hidden/__init__.py
def KEY():
    twitter="CeiWVwKXfsNq6tIkJJENJyb5c"
    return (twitter)

sys.path.insert(0, "/home/jack/hidden")
import key
CONSUMER_KEY = twitter()
print (CONSUMER_KEY)

%%writefile /home/jack/hidden/key.py
def key():
    twiter="CeiWVwKXfsNq6tIkJJENJyb5c"
    return twiter

import home.jack.hidden.key

#ONE TIME MANUAL POSTS
#!/home/jack/anaconda2/python
import random
from random import randint
import time
import markovify
import os
import sys
sys.path.insert(0, "/home/jack/hidden")
import key
#sys.path.insert(1, "/home/jack/Desktop/pycode/vpython2")
import twython
from twython import Twython
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter

#custom = "/home/jack/Desktop/post/ball009.png"
#custom = "/home/jack/Desktop/PROCESSING/color-wander/images/kk.png"
#custom = PAth+"gg.png"
#custom = "junk2/PalletteTemp.jpg"

#PATH = "clouddream/backup/deepdream/images/"
#custom = PATH+"8conv3fc_DSN-pool4-100-mountain.jpg"

custom = "Last-GRU-network-loss-1.2412-plot-for-Directory-kolbrin_2018-0724094637.png"
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
    i2 = draw_blurred_back(inp, (115, 10), "LSTM Model Training Plots", font, text_title, blur_title)
    font0 = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
    i2 = draw_blurred_back(i2, (115, 100), "GRU model", font0, text_title, blur_title)    
    i2 = draw_blurred_back(i2, (115, 120), "1662 Samples", font0, text_title, blur_title)    
    
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
    out.save("TM_POST.png")

#removed keys for privacy reasons
CONSUMER_KEY = key.twiter()[0]
CONSUMER_SECRET = key.twiter()[1]
ACCESS_KEY = key.twiter()[2]
ACCESS_SECRET = key.twiter()[3]

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#f = open("codetalk.txt")
#text = f.read()
#text_model = markovify.Text(text)
#STR = (text_model.make_short_sentence(140))
STR = ("Text Generation Model - notice the abnormalies from experimentation")
# USE BELOW for no signature
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "TM_POST.png"
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')
image = open(PATH,'rb')
response = twitter.upload_media(media=image)
twitter.update_status(status=STR, media_ids=[response['media_id']])


!showme TM_POST.png

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


import numpy
numpy.version.version
#'1.16.6' bakup-clonebase

%%writefile tweetout
#!/home/jack/miniconda3/envs/cloned_base/bin/python
import numpy as np
import random
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageFilter 
import os
import sys
import markovify
import twython
from twython import Twython
import time
import shutil
from randtext import randTXT
STR = randTXT()
Hash = ["#twitme #Python #100DaysOfCode\n","#Python #100DaysOfCode #PythonBots #codefor30days\n" ]
hashnum = randint(0,len(Hash)-1)
hashs =Hash[hashnum]
# add the hash to STR generated with randTXT()
STR = hashs+STR
STR= STR[:225]
print(STR)
# Open background image and work out centre
x = 720//2
y = 480//2

# The text we want to add
#text = "NFT TwitterBot Project"
text = STR
# Create font
font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 12)

#nap=randint(10,400)
#time.sleep(nap)
path = r"4-publish-images/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename1=(path+base_image)

bg = Image.open(filename1).convert('RGB')
x = bg.width//2
y = bg.height//2
src_path = filename1
dst_path = "3-resource_images/"
shutil.move(src_path, dst_path)
# The text we want to add
text = "NFT TwitterBot Project"
text=STR[:249]
print("len(text): ",len(text))
# Create font
font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 12)

# Create piece of canvas to draw text on and blur
blurred = Image.new('RGBA', bg.size)
draw = ImageDraw.Draw(blurred)
CH = randint(0,1)
if CH == 0:COLor = ["white","black"]
elif CH == 1:COLor = ["black","white"]  
draw.text(xy=(x-20,y+130), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x-21,y+131), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x-19,y+129), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x-20,y+130), text=text, fill=COLor[0], font=font, anchor='mm')
blurred = blurred.filter(ImageFilter.BoxBlur(2))

# Paste soft text onto background
bg.paste(blurred,blurred)

# Draw on sharp text
draw = ImageDraw.Draw(bg)
draw.text(xy=(x-20,y+130), text=text, fill=COLor[1], font=font, anchor='mm')
postage = ["perferations.png","perferations+.png","usa-perferations.png","usar-perferations.png","usal-perferations.png"]
Num = randint( 0, len(postage)-1)
BOARDER = postage[Num]
mask=Image.open(BOARDER).convert('RGBA') 
bg.paste(mask, (0,0), mask=mask)
bg.save('result.png')
#removed keys for privacy reasons
CONSUMER_KEY = 'APIkey()[0]'
CONSUMER_SECRET = 'APIkey()[1]'
ACCESS_KEY = 'APIkey()[2]'
ACCESS_SECRET = 'APIkey()[3]'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
PATH = "result.png"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])

from PIL import Image
im = Image.open(PATH)
im



!ls 

#!/home/jack/miniconda3/envs/cloned_base/bin/python
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageFilter 
import os
import sys
import markovify
import twython
from twython import Twython
import time
# Open background image and work out centre

path = r"2-resource_images/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)


bg = Image.open(filename0).convert('RGB')
bg =bg.resize((720,480),Image.ANTIALIAS)
x = bg.width//2
y = bg.height//2

# The text we want to add
text = "NFT TwitterBot Project"

# Create font
font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 40)

# Create piece of canvas to draw text on and blur
blurred = Image.new('RGBA', bg.size)
draw = ImageDraw.Draw(blurred)
draw.text(xy=(x,y+190), text=text, fill='black', font=font, anchor='mm')
blurred = blurred.filter(ImageFilter.BoxBlur(7))

# Paste soft text onto background
bg.paste(blurred,blurred)

# Draw on sharp text
draw = ImageDraw.Draw(bg)
draw.text(xy=(x,y+190), text=text, fill='white', font=font, anchor='mm')
#xx=0
#yy=0
#bg.paste("peferations.png", (xx,yy)) 
# paste an onerlay image
#perferations.png
#mask=Image.open("perferations.png").convert('RGBA') 
#bg.paste(mask, (x,y), mask=mask)
#bg.paste("peferations.png", box=(0, 0) + original.size) 
bg.save('result.png')
timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "records/"+timestr+"_.png"
bg.save(filename)
im =Image.open('result.png')
im



#nap=randint(10,400)
#time.sleep(nap)
path = r"3-resource_images/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)

bg = Image.open(filename0).convert('RGB')
x = bg.width//2
y = bg.height//2

# The text we want to add
text = "NFT TwitterBot Project"


# Create font
font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 40)

# Create piece of canvas to draw text on and blur
blurred = Image.new('RGBA', bg.size)
draw = ImageDraw.Draw(blurred)
draw.text(xy=(x,y+190), text=text, fill='black', font=font, anchor='mm')
blurred = blurred.filter(ImageFilter.BoxBlur(7))

# Paste soft text onto background
bg.paste(blurred,blurred)

# Draw on sharp text
draw = ImageDraw.Draw(bg)
draw.text(xy=(x,y+190), text=text, fill='white', font=font, anchor='mm')
mask=Image.open("perferations.png").convert('RGBA') 
bg.paste(mask, (0,0), mask=mask)
bg.save('result.png')
#removed keys for privacy reasons
CONSUMER_KEY = 'APIkey()[0]'
CONSUMER_SECRET = 'APIkey()[1]'
ACCESS_KEY = 'APIkey()[2]'
ACCESS_SECRET = 'APIkey()[3]'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#path = 'images/NewFolder'
with open("sart.txt") as f:
    data = f.read()
data_model = markovify.Text(data)
STR = data_model.make_sentence()
#STR = ("#All_in_One - #WordCloud #Create - Added ability to randomly choose an image background  #Automated")
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "/home/jack/Desktop/dockercommands/newtest/NEwtest2.png"
#PATH = "result.png"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])


from PIL import Image
im = Image.open("result.png")
im

#!/home/jack/miniconda3/envs/cloned_base/bin/python
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageFilter 
import os
import sys
import markovify
import twython
from twython import Twython
import time


CONSUMER_KEY = 'APIkey()[0]'
CONSUMER_SECRET = 'APIkey()[1]'
ACCESS_KEY = 'APIkey()[2]'
ACCESS_SECRET = 'APIkey()[3]'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#path = 'images/NewFolder'
with open("sart.txt") as f:
    data = f.read()
data_model = markovify.Text(data)
STR = data_model.make_sentence()

PATH = "result7.png"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])


Hash = ["#twitme #Python #100DaysOfCode\n","#Python #100DaysOfCode #PythonBots #codefor30days\n" ]
hashnum = randint(0,len(Hash)-1)
hashs =Hash[hashnum]
hashs

tweet="UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUuu'place': None, 'contributors': None,\
'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 0, 'favorite_count': 0, \
'favorited': False0, 'favorited': False, 'retweeted': False, 'possibly_sensitive': False, 'lang': 'en'}"
Text = (tweet[:240])

print("len(Text): ",len(Text),"\n",Text)

st


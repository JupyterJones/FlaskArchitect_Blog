#%%writefile use-TWITTERBOT-choose-and-sign.py
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
import shutil
# Open background image and work out centre

path = r"publish/"
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
src_path = filename0
dst_path = "Processed-Images/"
shutil.move(src_path, dst_path)
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
path = r"publish/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename1=(path+base_image)

bg = Image.open(filename1).convert('RGB')
x = bg.width//2
y = bg.height//2
src_path = filename1
dst_path = "Processed-Images/"
shutil.move(src_path, dst_path)
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
#PATH = "images/TM_POST.png"
PATH = "result.png"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])


import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageChops 
import os
import sys
import markovify
import twython
from twython import Twython
import time

%%writefile ImageBot
#!/bin/bash

while true; do
  python ImageBot.py
  echo "posted :"
  date
  sleep 1800s
done

!ls A*


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

path = r"publish/"
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
# Creates a dark text shadow for the white text so the text will show even on a light image
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
path = r"publish/"
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
#PATH = "images/TM_POST.png"
PATH = "result.png"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])


with open("sart.txt") as f:
    data = f.read()

    data_model = markovify.Text(data)
STR = data_model.make_sentence()

print(STR)

print("----------------------------")

# Print a randomly-generated sentences of no more than 280 characters
print(data_model.make_short_sentence(280))



!locate *.ttf

# Text file to 

%%writefile sart.txt
Alice in Wonderland (along with Through the Looking Glass) is one of the most famous children’s books of all time. It has been made into an iconic Disney film, as well as a recent Tim Burton release and countless other adaptations. The story of a young girl falling down a rabbit-hole and entering a strange, surreal world where nothing quite makes sense captures that childhood state when rules are not yet known and the imagination is as powerful as reality.

Written by Lewis Carroll, Alice in Wonderland is a classic in a children’s literary genre known as ‘nonsense’. Nonsense literature presents language and situations which are not normal. In English, this is a genre that rose to prominence in Victorian England, where literature and books were beginning to take on an ever-greater importance in the childhood experience of growing up.

Many examples from the books show Lewis Carroll’s ability to create a sense of the uncanny. The characters regularly show no respect for the basic rules of language. ‘When I use a word’, announces Humpty Dumpty, ‘it means just what I choose it to’. Humpty Dumpty has other views on words, telling Alice that ‘they’ve a temper, some of them—particularly verbs, they’re the proudest—adjectives you can do anything with, but not verbs’. The novel features a famous poem, The Jabberwocky, which features dozens of made-up words, as in the immortal line ‘and the mome raths outgrabe’. The strange sounds of these new words take the reader back to a time when every sound was something new and bizarre.

It is not just language that is played around with. The very laws of physics are upside down. A memorable scene in Through the Looking-Glass depicts Alice and the Red Queen running as fast as they can. When Alice asks where they are running to, the Red Queen scolds Alice, and explains that they are running merely to stay in the same place. When Alice enquires how they might go about actually getting somewhere else, the Red Queen explains that they’d have to run twice as fast.  Of course, as they are already at full pace, this makes no sense whatsoever. Time is also a source of nonsense. At the Tea Party, the Mad Hatter explains that his watch is ‘exactly two days slow’. This means, of course, that his watch is telling exactly the right time as it would be if it were on time.

It is easy to see these examples of nonsense as nothing more than childish fantasy. Yet there is more to nonsense than non-sense.  Lewis Carroll was a famous mathematician and many of his seemingly childish ideas draw on complex ideas of the nature of language, truth and logic. There are political aspects to his nonsense. Alice is told the story of The Walrus and the Carpenter, in which oysters are tricked by the two main characters and then eaten. The Walrus speaks a great deal of nonsense in order to ignore the protests of the oysters. In the Walrus and the Carpenter, nonsense becomes a tool used by the powerful to bewilder and exploit the weak and helpless.

Alice in Wonderland is originally a children’s story, but its meaning, especially its use of nonsense, goes far beyond this. Adults have enjoyed the novel for over a century. It is nonsense that is the key to its continued success, allowing the reader to shake off the rules and shapes of normal life, and return to the unlimited and eternally baffling visions of a half-forgotten childhood.

%%writefile titles.txt
Python Fun
Python Graphics
Generator
Word Cloud
Graphics
Fun w/Python
Python Stuff
PYTHON !!!
Love`en Python
Creative Python
Graphic Fun
Twitter Post
Fun Images
Jupyter Notebook

 List="""ancient%20manuscript%20art/
 animal%20eyes/
 antique%20art/
 antique%20book%20covers/
 antique%20tools/
 art%20nouveau/
 Australian%20Lizards/
 AutoImageCrawler/
 binary_images/
 black%20and%20white%20art%20nouveau%20drawings/
 Black%20Swan/
 Blobfish/
 Blue%20Tongue%20Lizard/
 cars/
 cartoon/
 deep%20sea%20fish/
 Dingo/
 dragonfly-720x480/
 dragonfly-downloads/
 Echidna/
 Headless%20Chicken%20Monster/
 image_resources/
 jellyfish/
 Kangaroo/
 Koala/
 marblepaper/
 old_photo/
 output/
 Platypus/
 polarized/
 posterize/
 publish/
 pxhere/
 records/
 reptiles/
 Roman%20Architecture/
 segmented/
 spaceshuttle/
 starfish/
 steampunk%20armor/
 Sugar%20Glider/
 tarantula/
 Tasmanian%20Tiger/
 texture/
 tmpseg/
 videoframes/
 vintage%20advertisments/
 vintage%20bottle%20labels/
 vintage%20childrens%20illustrations/
 vintage%20clothing%20patterns/
 vintage%20magazine%20covers/
 vintage%20postcards/
"""
lines= List.split("\n")
for line in lines:
    print(line, end= "  ")

ancient%20manuscript%20art/  animal%20eyes/  antique%20art/  antique%20book%20covers/  antique%20tools/  
art%20nouveau/  Australian%20Lizards/  AutoImageCrawler/  binary_images/  
black%20and%20white%20art%20nouveau%20drawings/  Black%20Swan/  Blobfish/  Blue%20Tongue%20Lizard/  cars/  
cartoon/  deep%20sea%20fish/  Dingo/  dragonfly-720x480/  dragonfly-downloads/  Echidna/  
Headless%20Chicken%20Monster/  image_resources/  jellyfish/  Kangaroo/  Koala/  marblepaper/  
old_photo/  output/  Platypus/  polarized/  posterize/  publish/  pxhere/  records/  reptiles/  
Roman%20Architecture/  segmented/  spaceshuttle/  starfish/  steampunk%20armor/  Sugar%20Glider/  
tarantula/  Tasmanian%20Tiger/  texture/  tmpseg/  videoframes/  vintage%20advertisments/  
vintage%20bottle%20labels/  vintage%20childrens%20illustrations/  vintage%20clothing%20patterns/  
vintage%20magazine%20covers/  vintage%20postcards/    

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import time
import random
import os
# Open background image and work out centre

#path = r"Australian%20Lizards/"
#path = r"marblepaper/"
path = r"polarized/"
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

timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "records/"+timestr+"_.png"
bg.save(filename)
im =Image.open('result.png')
im

#%%writefile ImageBot1.py
#!/home/jack/anaconda2/bin
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageChops 
import os
import sys
import markovify
import twython
from twython import Twython
import time
#nap=randint(10,400)
#time.sleep(nap)
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

PATH = "result.png"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])


import shutil

# absolute path
src_path = r"E:\pynative\reports\sales.txt"
dst_path = r"E:\pynative\account\sales.txt"
shutil.move(src_path, dst_path)

!mkdir Processed-Images

!ls Processed-Images

!chmod +x use-TWITTERBOT-choose-and-sign.py

%%writefile ImageBot
#!/bin/bash

while true; do
  ./use-TWITTERBOT-choose-and-sign.py
  echo "posted :"
  date
  sleep 1800s
done

!./use-TWITTERBOT-choose-and-sign.py

im =Image.open('result.png')
im






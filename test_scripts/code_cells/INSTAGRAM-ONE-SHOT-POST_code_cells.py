ls junk/*

Choose = ["insta-usa-perferations.png", "insta-philippines-perferations.png","insta-perferations.png"]
from random import randint
num = randint(0,2)
print (Choose[num])


PatH=["publish/", "output/", "posterize/", "marblepaper/", "old_photo/", "texture/", "polarized/"]
num2 = randint(0,6)
print (PatH[num2])

#import Image and ImageEnhance modules
from PIL import Image, ImageEnhance, ImageChops
from random import randint
PatH=["publish/", "output/", "posterize/", "marblepaper/", "old_photo/", "texture/", "polarized/"]
num2 = randint(0,6)
path = PatH[num2]
base_image = random.choice([
x for x in os.listdir(path)
if os.path.isfile(os.path.join(path, x))
    ])
file=(path+base_image)

im = Image.open(file)# Open an Image file
im = im.resize((960,960), Image.ANTIALIAS)
print(im.size)
Brighten = ImageEnhance.Brightness(im) # Create a Brightness class
brightimage = Brighten.enhance(1.1)
brightimage.save("junk/temp-brightened.jpg") # Save results
 
im = Image.open("junk/temp-brightened.jpg") # Open the Image
sharpened = ImageEnhance.Sharpness(im) # Create an object using Sharpness
sharpenedimage = sharpened.enhance(1.1)
sharpenedimage.save("junk/temp-sharpenedimage.jpg") # Save results
 
im = Image.open('junk/temp-sharpenedimage.jpg') # Open the Image
contrast = ImageEnhance.Contrast(im) # Create an object using Sharpness
contrastedimage = contrast.enhance(1.1)
contrastedimage.save('junk/temp-contrastedimage.jpg') # Save results
 
im = Image.open("junk/temp-contrastedimage.jpg")
width, height = im.size   # Get dimensions
#im = im.resize((2*width,2*height), "Image.NEAREST" (0))
#im = im.resize((2*width,2*height), Image.ANTIALIAS)
Choose = ["insta-usa-perferations.png", "insta-philippines-perferations.png","insta-perferations.png"]
num = randint(0,2)
border = (Choose[num])
mask=Image.open(border).convert('RGBA') 
im.paste(mask, (0,0), mask=mask)
im.save('junk/temp1.jpg')
im    

%%writefile mkimag.py
#import Image and ImageEnhance modules
from PIL import Image, ImageEnhance, ImageChops
from random import randint
import random
import os
import time
def mkimag():
    PatH=["publish/", "output/", "posterize/", "marblepaper/", "old_photo/", "texture/", "polarized/"]
    num2 = randint(0,6)
    path = PatH[num2]
    base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
        ])
    file=(path+base_image)

    im = Image.open(file)# Open an Image file
    im = im.resize((960,960), Image.ANTIALIAS)
    #print(im.size)
    Brighten = ImageEnhance.Brightness(im) # Create a Brightness class
    brightimage = Brighten.enhance(1.1)
    brightimage.save("junk/temp-brightened.jpg") # Save results
 
    im = Image.open("junk/temp-brightened.jpg") # Open the Image
    sharpened = ImageEnhance.Sharpness(im) # Create an object using Sharpness
    sharpenedimage = sharpened.enhance(1.1)
    sharpenedimage.save("junk/temp-sharpenedimage.jpg") # Save results
 
    im = Image.open('junk/temp-sharpenedimage.jpg') # Open the Image
    contrast = ImageEnhance.Contrast(im) # Create an object using Sharpness
    contrastedimage = contrast.enhance(1.1)
    contrastedimage.save('junk/temp-contrastedimage.jpg') # Save results
 
    im = Image.open("junk/temp-contrastedimage.jpg")
    width, height = im.size   # Get dimensions
    #im = im.resize((2*width,2*height), "Image.NEAREST" (0))
    #im = im.resize((2*width,2*height), Image.ANTIALIAS)
    Choose = ["insta-usa-perferations.png", "insta-philippines-perferations.png","insta-perferations.png"]
    num = randint(0,2)
    border = (Choose[num])
    mask=Image.open(border).convert('RGBA') 
    im.paste(mask, (0,0), mask=mask)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "junk/insta"+timestr+"_.jpg"
    im.save('junk/temp1.jpg')
    return im    

ls *.py

from mkimag import mkimag
im = mkimag()
im

%%writefile post-to-instagram.py
#!/home/jack/miniconda3/envs/cloned_base/bin/python
from instabot import Bot
import os
import shutil
import markovify
from PIL import Image, ImageEnhance, ImageChops
from mkimag import mkimag
import time
im = mkimag()


with open("sart.txt") as f:
    data = f.read()
data_model = markovify.Text(data)
STR = data_model.make_sentence()



def clean_up(i):
    dir = "config"
    remove_me = "imgs\{}.REMOVE_ME".format(i)
    # checking whether config folder exists or not
    if os.path.exists(dir):
        try:
            # removing it so we can upload new image
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    if os.path.exists(remove_me):
        src = os.path.realpath("junk/{}".format(i))
        os.rename(remove_me, src)


def upload_post(i):
    bot = Bot()

    bot.login(username="jacklnorthrup", password="Pxyackjs22")
    bot.upload_photo("junk/{}".format(i), caption=STR)


#if __name__ == '__main__':
# enter name of your image bellow
image_name = "temp1.jpg"
clean_up(image_name)
upload_post(image_name)



!./post-to-instagram.py

#import Image and ImageEnhance modules
from PIL import Image, ImageEnhance
  
file = "junk/temp.jpg"
im = Image.open(file)  # Open an Image file
Brighten = ImageEnhance.Brightness(im) # Create a Brightness class
brightimage = Brighten.enhance(1.2)
brightimage.show() #show results

brightimage.save("junk/temp-brightened.jpg") # Save results

# This will import Image and ImageChops modules
from PIL import Image, ImageEnhance, ImageChops
  
im = Image.open("junk/temp-brightened.jpg") # Open the Image
sharpened = ImageEnhance.Sharpness(im) # Create an object using Sharpness
  
sharpenedimage = sharpened.enhance(4.0)
sharpenedimage.show() #show results
sharpenedimage.save("junk/temp-sharpenedimage.jpg") # Save results

# This will import Image and ImageChops modules
from PIL import Image, ImageEnhance, ImageChops
im = Image.open('junk/temp-sharpenedimage.jpg') # Open the Image
contrast = ImageEnhance.Contrast(im) # Create an object using Sharpness
contrastedimage = contrast.enhance(1.7)
contrastedimage.show() #show results
contrastedimage.save('junk/temp-contrastedimage.jpg') # Save results

from PIL import Image, ImageEnhance, ImageFilter
import random
import os
im = Image.open("junk/temp-contrastedimage.jpg")
width, height = im.size   # Get dimensions
#im = im.resize((2*width,2*height), "Image.NEAREST" (0))
#im = im.resize((2*width,2*height), Image.ANTIALIAS)
print(im.size)

# Crop the center of the image

mask=Image.open("insta-perferations.png").convert('RGBA') 
im.paste(mask, (0,0), mask=mask)
im.save('junk/temp1.jpg')
im    

from instabot import Bot
import os
import shutil
from PIL import Image, ImageEnhance, ImageChops

def clean_up(i):
    dir = "config"
    remove_me = "imgs\{}.REMOVE_ME".format(i)
    # checking whether config folder exists or not
    if os.path.exists(dir):
        try:
            # removing it so we can upload new image
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    if os.path.exists(remove_me):
        src = os.path.realpath("junk/{}".format(i))
        os.rename(remove_me, src)


def upload_post(i):
    bot = Bot()

    bot.login(username="jacklnorthrup", password="Pxyackjs22")
    bot.upload_photo("junk/{}".format(i), caption="""im = Image.open(filename0)
    width, height = im.size   # Get dimensions
    #im = im.resize((2*width,2*height), "Image.NEAREST" (0))
    im = im.resize((2*width,2*height), Image.ANTIALIAS)
    print(im.size)
    width, height = im.size 
    new_width =960
    new_height =960
    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2""")


#if __name__ == '__main__':
# enter name of your image bellow
image_name = "temp1.jpg"
clean_up(image_name)
upload_post(image_name)



from PIL import Image, ImageEnhance, ImageFilter
import random
import os
path = r"ManRay/"
def BaseImage(path):
    base_image = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    filename0=(path+base_image)

    im = Image.open(filename0)
    width, height = im.size   # Get dimensions
    #im = im.resize((2*width,2*height), "Image.NEAREST" (0))
    im = im.resize((2*width,2*height), Image.ANTIALIAS)
    print(im.size)
    width, height = im.size 
    new_width =960
    new_height =960
    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2

    # Crop the center of the image
    im = im.crop((left, top, right, bottom))
    filter = ImageEnhance.Brightness(im)
    enhanced_image = ImageFilter.Filter(1.2)
    mask=Image.open("insta-perferations.png").convert('RGBA') 
    enhanced_image.paste(mask, (0,0), mask=mask)
    enhanced_image.save('junk/temp1.jpg')
    return enhanced_image

path = r"ManRay/"
BaseImage(path)    

Filter = ImageEnhance.Brightness(im)
new_image = im.ImageFilter.Filter(1.2)

new_image.show()

from PIL import Image
import random
import os
path = r"ManRay/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)

im = Image.open(filename0)
width, height = im.size   # Get dimensions
#im = im.resize((2*width,2*height), "Image.NEAREST" (0))
im = im.resize((2*width,2*height), Image.ANTIALIAS)
print(im.size)
width, height = im.size 
new_width =960
new_height =960
left = (width - new_width)/2
top = (height - new_height)/2
right = (width + new_width)/2
bottom = (height + new_height)/2

# Crop the center of the image
im = im.crop((left, top, right, bottom))
im.save('junk/temp.jpg')
im

INFO Found Here:
 17 https://www.instagram.com jlnorthrup pxyackjs22

INFO Found Here:
 107 https://instagram.com jacklnorthrup Pxyackjs22

INFO Found Here:
 110 https://instagram.com pxyackjs22


image = image.resize((x, y), Image.ANTIALIAS)

from instabot import Bot
bot=Bot()
 
bot.login(username = "jacklnorthrup",
          password = "Pxyackjs22")
 

from instabot import Bot
bot=Bot()
 
bot.login(username = "jacklnorthrup",
          password = "Pxyackjs22")
 
# Recommended to put the photo
# you want to upload in the same
# directory where this Python code
# is located else you will have
# to provide full path for the photo
bot.upload_photo("junk/temp.jpg",
                 caption ="I just extended my TwitterBot to Instagram")

from instabot import Bot
import random 
 
bot = Bot()
bot.login(username = "jacklnorthrup", password = "Pxyackjs22")
 

path = r"ManRay/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)




bot.upload_photo("junk/temp.jpg",
                 caption ="I just extended my TwitterBot to Instagram")

!mkdir instagram

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
text = "NFT Instagram Project"

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
bg.save('junk/temp.jpg')
timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "instagram/"+timestr+"_.png"
bg.save(filename)
im =Image.open('junk/temp.jpg')
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
mask=Image.open("insta-perferations.png").convert('RGBA') 
bg.paste(mask, (0,0), mask=mask)
bg.save('junk/temp.jpg')
with open("sart.txt") as f:
    data = f.read()
data_model = markovify.Text(data)
STR = data_model.make_sentence()


!ls *.png

from PIL import Image
im = Image.open("junk/temp.jpg")
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





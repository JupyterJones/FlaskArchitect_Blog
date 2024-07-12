https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html#module-PIL.ImageFilter
https://github.com/gmortuza/Deep-Learning-Specialization/blob/master/4.%20Convolutional%20Neural%20Networks/week%204/Programming%20assignment/Neural%20Style%20Transfer/Art_Generation_with_Neural_Style_Transfer_v3a.ipynb

import os
import tensorflow as tf
# Load compressed models from tensorflow_hub
os.environ['TFHUB_MODEL_LOAD_FORMAT'] = 'COMPRESSED'
import IPython.display as display

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (12, 12)
mpl.rcParams['axes.grid'] = False

import numpy as np
import PIL.Image
import time
import functools

def tensor_to_image(tensor):
    tensor = tensor*255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor)>3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
    return PIL.Image.fromarray(tensor)
def load_img(path_to_img):
    max_dim = 512
    img = tf.io.read_file(path_to_img)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)

    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim

    new_shape = tf.cast(shape * scale, tf.int32)

    img = tf.image.resize(img, new_shape)
    img = img[tf.newaxis, :]
    return img
def imshow(image, title=None):
    if len(image.shape) > 3:
        image = tf.squeeze(image, axis=0)

    plt.imshow(image)
    if title:
        plt.title(title)

!mkdir preped_images

content = "images/farming.jpg"
content_path = prep_content(content)
style = "/home/jack/Pictures/UNTITLED_55.JPG"
style_path = prep_style(style)


from PIL import Image
import os

def prep_content(content):
    PI = Image.open(content)
    PI = PI.resize((720,480), Image.NEAREST)
    CFilename = os.path.basename(content)
    PI.save("preped_images/Content_"+CFilename)
    Content_data="preped_images/Content_"+CFilename
    return Content_data
    
def prep_style(style):
    PI = Image.open(style)
    PI = PI.resize((720,480), Image.NEAREST)
    SFilename = os.path.basename(style)
    PI.save("preped_images/Style_"+SFilename)
    Style_data="preped_images/Style_"+SFilename
    return Style_data    

from tensorflow.python.ops.numpy_ops import np_config
np_config.enable_numpy_behavior()
from PIL import Image
import os

def prep_content(content):
    PI = Image.open(content)
    PI = PI.resize((720,480), Image.NEAREST)
    CFilename = os.path.basename(content)
    PI.save("preped_images/Content_"+CFilename)
    Content_data="preped_images/Content_"+CFilename
    return Content_data
    
def prep_style(style):
    PI = Image.open(style)
    PI = PI.resize((720,480), Image.NEAREST)
    SFilename = os.path.basename(style)
    PI.save("preped_images/Style_"+SFilename)
    Style_data="preped_images/Style_"+SFilename
    return Style_data    

content = "/home/jack/Desktop/TENSORFLOW/images/ahoy.png"


style = "/home/jack/Desktop/TENSORFLOW/images/colors01.png"
#print (prep_style(style))

content_image = load_img(prep_content(content))
style_image = load_img(prep_style(style))

print(content_image.size)
print(style_image.size)
plt.subplot(1, 2, 1)
imshow(content_image, 'Content Image')

plt.subplot(1, 2, 2)
imshow(style_image, 'Style Image')


from PIL import Image
import tensorflow_hub as hub
import time
hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

#hub_model = hub.load("models/magenta_arbitrary-image-stylization-v1-256_2")
stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
im = tensor_to_image(stylized_image)
timestr = time.strftime("%Y%m%d-%H%M%S")
savefile = "images/"+timestr+".jpg"
im.save(savefile)
print(im.size)
im

iml = im.resize((720,480), Image.NEAREST)
iml.save("720x480/temp.jpg")
iml

from PIL import Image, ImageEnhance
im = Image.open("720x480/temp.jpg")
enhancer = ImageEnhance.Sharpness(im)
factor = 1.5
im_s_1 = enhancer.enhance(factor)
im_s_1.save('720x480/Sharpened-temp.jpg');
im_s_1

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
Hash = ["#AIart #Tensorflow #twitme #Python #100DaysOfCode\n","#tensorflow #styletransfer #PythonGraphics #PIL #PythonImageLibrary\n","#NFTartist #NFTProject #NEARnft #nearNFTs \n","#NFT #NFTs #NFTCommunity #NFTdrop #nftart\n","#CreativeCoding  #AI #genart #p5js #Generative\n","#twitme #Python #100DaysOfCode\n","#Python #100DaysOfCode #PythonBots #codefor30days\n" ]
hashnum = randint(0,len(Hash)-1)
hashs =Hash[0]
# add the hash to STR generated with randTXT()
STR = hashs+STR
STR= STR[:180]
print(STR)
# Open background image and work out centre
x = 720//2
y = 480//2

# The text we want to add
#text = "NFT TwitterBot Project"
text = STR
# Create font
font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)

#nap=randint(10,400)
#time.sleep(nap)
'''
path = r"/home/jack/Desktop/Imagedata/4-publish-images/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])'''
filename1='images/result.png'

bg = Image.open(filename1).convert('RGB')
x = bg.width//2
y = bg.height//2
src_path = filename1
#dst_path = "/home/jack/Desktop/Imagedata/3-resource_images/"
#shutil.move(src_path, dst_path)

# The text we want to add
text=STR[:249]
print("len(text): ",len(text))
# Create font
font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)

# Create piece of canvas to draw text on and blur
blurred = Image.new('RGBA', bg.size)
draw = ImageDraw.Draw(blurred)
CH = randint(0,1)
if CH == 0:COLor = ["white","black"]
elif CH == 1:COLor = ["black","white"]  
draw.text(xy=(x-15,y+160), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x-16,y+161), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x-14,y+159), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x-15,y+160), text=text, fill=COLor[0], font=font, anchor='mm')
blurred = blurred.filter(ImageFilter.BoxBlur(2))

# Paste soft text onto background
bg.paste(blurred,blurred)

# Draw on sharp text
draw = ImageDraw.Draw(bg)
draw.text(xy=(x-15,y+160), text=text, fill=COLor[1], font=font, anchor='mm')
#postage = ["perferations.png","perferations+.png","frames.png","usa-perferations.png","usar-perferations.png","usal-perferations.png"]
#Num = randint( 0, len(postage)-1)
#BOARDER ="overlays/tensorlow-frames.png"
#BOARDER ="overlays/nouveau-black-frame1.png"
#mask=Image.open(BOARDER).convert('RGBA') 
#bg.paste(mask, (0,0), mask=mask)
bg.save('images/useresult.png')
#removed keys for privacy reasons
CONSUMER_KEY = 'APIkey()[0]'
CONSUMER_SECRET = 'APIkey()[1]'
ACCESS_KEY = 'APIkey()[2]'
ACCESS_SECRET = 'APIkey()[3]'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
PATH = "images/useresult.png"
timestr = time.strftime("%Y%m%d-%H%M%S")
print (timestr+".png")

#python program to check if a directory exists
import os
path = "posted"
# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:
    # Create a new directory because it does not exist
    os.makedirs(path)
    print("The new directory is created!")
shutil.copy(PATH, "posted/"+timestr+".png")
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

photo = open(PATH,'rb')
#photo = open("images/waves1.gif","rb")
#response = twitter.upload_media(media=photo)
#twitter.update_status(status=STR, media_ids=[response['media_id']])

im = Image.open(PATH)
im

response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])

# Importing Image and ImageFilter module from PIL package
from PIL import Image, ImageFilter

# creating a image object
im1 = Image.open('720x480/Sharpened-temp.jpg')
enhancer = ImageEnhance.Contrast(im1)
# applying the EDGE_ENHANCE filter
#im2 = im1.filter(ImageFilter.EDGE_ENHANCE)
factor = 1.2 #increase contrast
im2 = enhancer.enhance(factor)
im2.save('720x480/SharpenedC.jpg')
im2


from PIL import Image
 
# creating a image object (main image)
im1 = Image.open('720x480/SharpenedC.jpg')
 
# creating a image object (image which is to be paste on main image)
im2 = Image.open("overlays/tensorlow-frames.png")
#im2 = Image.open("overlays/nouveau-black-frame.png")
 
# pasting im2 on im1 background.paste(foreground, (0, 0), foreground)
#background.show()

im1.paste(im2, (0, 0), im2)
print(im1.size) 
# to show specified image
im1.save("images/result.png")
im1.show()

from tensorflow.python.ops.numpy_ops import np_config
np_config.enable_numpy_behavior()
#content_path = "images/myra.jpg"
#style_path = "images/f6a1489aa194f55436d39d8bb6c19b1c.jpg"
#content_path = "images/scorpion.png"

#content_path = "/home/jack/Pictures/UNTITLED_55.JPG"
#style_path = "images/farming.jpg"
#style_path = "/home/jack/Desktop/TENSORFLOW/images/Screenshot_1.png"

#content = "images/farming.jpg"
content = "/home/jack/Desktop/TENSORFLOW/torchimages/images/arts_model20221005-172637_42.png"
#content = "images/OPKJIHUG.jpg"
#print (prep_content(content))

#style = "/home/jack/Pictures/UNTITLED_55.JPG"
style = "images/OPKJIHUG.jpg"
#style = "/home/jack/Desktop/TENSORFLOW/torchimages/images/arts_model20221005-172637_42.png"
#print (prep_style(style))

content_image = load_img(prep_content(content))
style_image = load_img(prep_style(style))
print(content_image.size)
print(style_image.size)
plt.subplot(1, 2, 1)
imshow(content_image, 'Content Image')

plt.subplot(1, 2, 2)
imshow(style_image, 'Style Image')


from PIL import Image
import tensorflow_hub as hub
import time
hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
#hub_model = hub.load("models/magenta_arbitrary-image-stylization-v1-256_2")
stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
im = tensor_to_image(stylized_image)
timestr = time.strftime("%Y%m%d-%H%M%S")
savefile = "images/"+timestr+".jpg"
im.save(savefile)
print(im.size)
im









from PIL import Image
 
# creating a image object (main image)
im1 = Image.open('720x480/Sharpened-temp.jpg')
 
# creating a image object (image which is to be paste on main image)
im2 = Image.open("overlays/tensorlow-frames.png")
 
# pasting im2 on im1 background.paste(foreground, (0, 0), foreground)
#background.show()

im1.paste(im2, (0, 0), im2)
print(im1.size) 
# to show specified image
im1.save("images/result.png")
im1.show()



from PIL import Image
import tensorflow_hub as hub
import time
hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
#hub_model = hub.load("models/magenta_arbitrary-image-stylization-v1-256_2")
stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
im = tensor_to_image(stylized_image)
timestr = time.strftime("%Y%m%d-%H%M%S")
savefile = "images/"+timestr+".jpg"
im.save(savefile)
print(im.size)
im

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
Hash = ["#AIart #Tensorflow #twitme #Python #100DaysOfCode","#tensorflow #styletransfer #PythonGraphics #PIL #PythonImageLibrary\n","#NFTartist #NFTProject #NEARnft #nearNFTs \n","#NFT #NFTs #NFTCommunity #NFTdrop #nftart\n","#CreativeCoding  #AI #genart #p5js #Generative\n","#twitme #Python #100DaysOfCode\n","#Python #100DaysOfCode #PythonBots #codefor30days\n" ]
hashnum = randint(0,len(Hash)-1)
hashs =Hash[0]
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
font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)

#nap=randint(10,400)
#time.sleep(nap)
'''
path = r"/home/jack/Desktop/Imagedata/4-publish-images/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])'''
filename1='images/result.png'

bg = Image.open(filename1).convert('RGB')
x = bg.width//2
y = bg.height//2
src_path = filename1
#dst_path = "/home/jack/Desktop/Imagedata/3-resource_images/"
#shutil.move(src_path, dst_path)

# The text we want to add
text=STR[:249]
print("len(text): ",len(text))
# Create font
font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)

# Create piece of canvas to draw text on and blur
blurred = Image.new('RGBA', bg.size)
draw = ImageDraw.Draw(blurred)
CH = randint(0,1)
if CH == 0:COLor = ["white","black"]
elif CH == 1:COLor = ["black","white"]  
draw.text(xy=(x-15,y+150), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x-16,y+151), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x-14,y+149), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x-15,y+150), text=text, fill=COLor[0], font=font, anchor='mm')
blurred = blurred.filter(ImageFilter.BoxBlur(2))

# Paste soft text onto background
bg.paste(blurred,blurred)

# Draw on sharp text
draw = ImageDraw.Draw(bg)
draw.text(xy=(x-15,y+150), text=text, fill=COLor[1], font=font, anchor='mm')
#postage = ["perferations.png","perferations+.png","frames.png","usa-perferations.png","usar-perferations.png","usal-perferations.png"]
#Num = randint( 0, len(postage)-1)
#BOARDER ="overlays/tensorlow-frames.png"
#mask=Image.open(BOARDER).convert('RGBA') 
#bg.paste(mask, (0,0), mask=mask)
bg.save('images/useresult.png')
#removed keys for privacy reasons
CONSUMER_KEY = 'APIkey()[0]'
CONSUMER_SECRET = 'APIkey()[1]'
ACCESS_KEY = 'APIkey()[2]'
ACCESS_SECRET = 'APIkey()[3]'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
PATH = "images/useresult.png"
timestr = time.strftime("%Y%m%d-%H%M%S")
print (timestr+".png")

#python program to check if a directory exists
import os
path = "posted"
# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:
    # Create a new directory because it does not exist
    os.makedirs(path)
    print("The new directory is created!")
shutil.copy(PATH, "posted/"+timestr+".png")
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

photo = open(PATH,'rb')
#photo = open("images/waves1.gif","rb")
#response = twitter.upload_media(media=photo)
#twitter.update_status(status=STR, media_ids=[response['media_id']])

def load_img(path_to_img):
    max_dim = 512
    img = tf.io.read_file(path_to_img)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)

    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim

    new_shape = tf.cast(shape * scale, tf.int32)

    img = tf.image.resize(img, new_shape)
    img = img[tf.newaxis, :]
    return img
def imshow(image, title=None):
    if len(image.shape) > 3:
        image = tf.squeeze(image, axis=0)

    plt.imshow(image)
    if title:
        plt.title(title)
        
content_image = load_img(content_path)
style_image = load_img(style_path)

plt.subplot(1, 2, 1)
imshow(content_image, 'Content Image')

plt.subplot(1, 2, 2)
imshow(style_image, 'Style Image')


from PIL import Image, ImageFilter
 
# creating a image object
im1 = Image.open(r"C:\Users\sadow984\Desktop\download2.JPG")
 
# applying the EDGE_ENHANCE filter
im2 = im1.filter(ImageFilter.EDGE_ENHANCE)
 
im2.show()

!ls images

content_path = "images/VoidROV(@voidrov)Instagram2.png"
#style_path = "images/VoidROV(@voidrov)Instagram1.png"
style_path = "images/VoidROV(@voidrov)Instagram1.png"

#content_path = "images/Halloween.jpg"
content_path = "images/myra.jpg"
#style_path = "images/myra.jpg"
#style_path = "images/01c353e2271bd42776398752ec3c6a17.jpg"
#style_path = "images/paper_0091lines.png"
#style_path = "images/marble2.jpg"
style_path = "images/f6a1489aa194f55436d39d8bb6c19b1c.jpg"
content_image = load_img(content_path)
style_image = load_img(style_path)

plt.subplot(1, 2, 1)
imshow(content_image, 'Content Image')

plt.subplot(1, 2, 2)
imshow(style_image, 'Style Image')


def load_img(path_to_img):
    max_dim = 512
    img = tf.io.read_file(path_to_img)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)

    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim

    new_shape = tf.cast(shape * scale, tf.int32)

    img = tf.image.resize(img, new_shape)
    img = img[tf.newaxis, :]
    return img
def imshow(image, title=None):
    if len(image.shape) > 3:
        image = tf.squeeze(image, axis=0)

    plt.imshow(image)
    if title:
        plt.title(title)
        
content_image = load_img(content_path)
style_image = load_img(style_path)

plt.subplot(1, 2, 1)
imshow(content_image, 'Content Image')

plt.subplot(1, 2, 2)
imshow(style_image, 'Style Image')


from PIL import Image
import tensorflow_hub as hub
import time
hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
im = tensor_to_image(stylized_image)
timestr = time.strftime("%Y%m%d-%H%M%S")
savefile = "images/"+timestr+".jpg"
im.save(savefile)
print(im.size)
im

iml = im.resize((720,480), Image.NEAREST)
iml.save("720x480/temp.jpg")

from PIL import Image, ImageEnhance
im = Image.open("720x480/temp.jpg")
enhancer = ImageEnhance.Sharpness(im)

#factor = 1
#im_s_1 = enhancer.enhance(factor)
#im_s_1.save('original-image-1.png');

#factor = 0.05
#im_s_1 = enhancer.enhance(factor)
#im_s_1.save('blurred-image.png');

factor = 2.5
im_s_1 = enhancer.enhance(factor)
im_s_1.save('720x480/Sharpened-temp.jpg');
im_s_1

# Importing Image and ImageFilter module from PIL package
from PIL import Image, ImageFilter

# creating a image object
im1 = Image.open('720x480/Sharpened-temp.jpg')

# applying the EDGE_ENHANCE filter
im2 = im1.filter(ImageFilter.EDGE_ENHANCE)

im2#.show()


from PIL import Image
 
# creating a image object (main image)
im1 = Image.open('720x480/Sharpened-temp.jpg')
 
# creating a image object (image which is to be paste on main image)
im2 = Image.open("overlays/tensorlow-frames.png")
 
# pasting im2 on im1 background.paste(foreground, (0, 0), foreground)
#background.show()

im1.paste(im2, (0, 0), im2)
print(im1.size) 
# to show specified image
im1.save("images/result.png")
im1.show()



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
Hash = ["#AIart #Tensorflow #twitme #Python #100DaysOfCode","#tensorflow #styletransfer #PythonGraphics #PIL #PythonImageLibrary\n","#NFTartist #NFTProject #NEARnft #nearNFTs \n","#NFT #NFTs #NFTCommunity #NFTdrop #nftart\n","#CreativeCoding  #AI #genart #p5js #Generative\n","#twitme #Python #100DaysOfCode\n","#Python #100DaysOfCode #PythonBots #codefor30days\n" ]
hashnum = randint(0,len(Hash)-1)
hashs =Hash[0]
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
font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)

#nap=randint(10,400)
#time.sleep(nap)
'''
path = r"/home/jack/Desktop/Imagedata/4-publish-images/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])'''
filename1='images/result.png'

bg = Image.open(filename1).convert('RGB')
x = bg.width//2
y = bg.height//2
src_path = filename1
#dst_path = "/home/jack/Desktop/Imagedata/3-resource_images/"
#shutil.move(src_path, dst_path)

# The text we want to add
text=STR[:249]
print("len(text): ",len(text))
# Create font
font = ImageFont.truetype('/snap/gnome-3-38-2004/99/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)

# Create piece of canvas to draw text on and blur
blurred = Image.new('RGBA', bg.size)
draw = ImageDraw.Draw(blurred)
CH = randint(0,1)
if CH == 0:COLor = ["white","black"]
elif CH == 1:COLor = ["black","white"]  
draw.text(xy=(x-15,y+150), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x-16,y+151), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x-14,y+149), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x-15,y+150), text=text, fill=COLor[0], font=font, anchor='mm')
blurred = blurred.filter(ImageFilter.BoxBlur(2))

# Paste soft text onto background
bg.paste(blurred,blurred)

# Draw on sharp text
draw = ImageDraw.Draw(bg)
draw.text(xy=(x-15,y+150), text=text, fill=COLor[1], font=font, anchor='mm')
#postage = ["perferations.png","perferations+.png","frames.png","usa-perferations.png","usar-perferations.png","usal-perferations.png"]
#Num = randint( 0, len(postage)-1)
BOARDER ="overlays/tensorlow-frames.png"
mask=Image.open(BOARDER).convert('RGBA') 
bg.paste(mask, (0,0), mask=mask)
bg.save('images/useresult.png')
#removed keys for privacy reasons
CONSUMER_KEY = 'APIkey()[0]'
CONSUMER_SECRET = 'APIkey()[1]'
ACCESS_KEY = 'APIkey()[2]'
ACCESS_SECRET = 'APIkey()[3]'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
PATH = "images/useresult.png"
timestr = time.strftime("%Y%m%d-%H%M%S")
print (timestr+".png")

#python program to check if a directory exists
import os
path = "posted"
# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:
    # Create a new directory because it does not exist
    os.makedirs(path)
    print("The new directory is created!")
shutil.copy(PATH, "posted/"+timestr+".png")
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

photo = open(PATH,'rb')
#photo = open("images/waves1.gif","rb")
#response = twitter.upload_media(media=photo)
#twitter.update_status(status=STR, media_ids=[response['media_id']])

im = Image.open(PATH)
im

im = Image.open(PATH)
im



response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])

!mkdir instaposted

ins =Image.open(PATH)
ins = ins.resize((720,720), Image.NEAREST)
ins.save("instaposted/girl.png")
ins

!wget https://storage.googleapis.com/download.tensorflow.org/example_images/YellowLabradorLooking_new.jpg -O images/YellowLabradorLooking_new.jpg
!wget https://storage.googleapis.com/download.tensorflow.org/example_images/Vassily_Kandinsky%2C_1913_-_Composition_7.jpg -O images/kandinsky5.jpg

content_url = ""
style_url = ""
content_path = tf.keras.utils.get_file('YellowLabradorLooking_new.jpg', )
style_path = tf.keras.utils.get_file('kandinsky5.jpg',)


path_to_img = "images/YellowLabradorLooking_new.jpg"
#path_to_img = "images/Vassily_Kandinsky%2C_1913_-_Composition_7.jpg"
path_to_img = "/home/jack/Desktop/TENSORFLOW/images/map-of-usa.jpg"

content_path = "images/YellowLabradorLooking_new.jpg"
#path_to_img = "images/Vassily_Kandinsky%2C_1913_-_Composition_7.jpg"
style_path = "/home/jack/Desktop/TENSORFLOW/images/map-of-usa.jpg"

#content_path = "images/YellowLabradorLooking_new.jpg"
content_path = "/home/jack/Desktop/Imagedata/3-resource_images/08993.jpg"
#path_to_img = "images/Vassily_Kandinsky%2C_1913_-_Composition_7.jpg"
style_path = "/home/jack/Desktop/TENSORFLOW/images/JoPoism-Paintings.jpg"

!ls images

content_path = "images/sized.jpg"
style_path = "images/tweetyjill.png"

Filters=["BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EDGE_ENHANCE_MORE", "EMBOSS", "FIND_EDGES", "SHARPEN", "SMOOTH", "SMOOTH_MORE"]


from PIL import ImageFilter

im1 = iml.filter(ImageFilter.BLUR)

im2 = iml.filter(ImageFilter.MinFilter(3))
im3 = iml.filter(ImageFilter.MinFilter)  # same as MinFilter(3)

!ls overlays

!ls images

# Created for debug
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
print (timestr+".png")

#python program to check if a directory exists
import os
path = "posted"
# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:
    # Create a new directory because it does not exist
    os.makedirs(path)
    print("The new directory is created!")
shutil.move("images/useresult.png", "posted/"+timestr+".png")

# %load /home/jack/miniconda3/envs/cloned_base/lib/python3.9/site-packages/PIL/ImageFilter.py
#
# The Python Imaging Library.
# $Id$
#
# standard filters
#
# History:
# 1995-11-27 fl   Created
# 2002-06-08 fl   Added rank and mode filters
# 2003-09-15 fl   Fixed rank calculation in rank filter; added expand call
#
# Copyright (c) 1997-2003 by Secret Labs AB.
# Copyright (c) 1995-2002 by Fredrik Lundh.
#
# See the README file for information on usage and redistribution.
#
import functools


class Filter:
    pass


class MultibandFilter(Filter):
    pass


class BuiltinFilter(MultibandFilter):
    def filter(self, image):
        if image.mode == "P":
            raise ValueError("cannot filter palette images")
        return image.filter(*self.filterargs)


class Kernel(BuiltinFilter):
    """
    Create a convolution kernel.  The current version only
    supports 3x3 and 5x5 integer and floating point kernels.

    In the current version, kernels can only be applied to
    "L" and "RGB" images.

    :param size: Kernel size, given as (width, height). In the current
                    version, this must be (3,3) or (5,5).
    :param kernel: A sequence containing kernel weights.
    :param scale: Scale factor. If given, the result for each pixel is
                    divided by this value.  The default is the sum of the
                    kernel weights.
    :param offset: Offset. If given, this value is added to the result,
                    after it has been divided by the scale factor.
    """

    name = "Kernel"

    def __init__(self, size, kernel, scale=None, offset=0):
        if scale is None:
            # default scale is sum of kernel
            scale = functools.reduce(lambda a, b: a + b, kernel)
        if size[0] * size[1] != len(kernel):
            raise ValueError("not enough coefficients in kernel")
        self.filterargs = size, scale, offset, kernel


class RankFilter(Filter):
    """
    Create a rank filter.  The rank filter sorts all pixels in
    a window of the given size, and returns the ``rank``'th value.

    :param size: The kernel size, in pixels.
    :param rank: What pixel value to pick.  Use 0 for a min filter,
                 ``size * size / 2`` for a median filter, ``size * size - 1``
                 for a max filter, etc.
    """

    name = "Rank"

    def __init__(self, size, rank):
        self.size = size
        self.rank = rank

    def filter(self, image):
        if image.mode == "P":
            raise ValueError("cannot filter palette images")
        image = image.expand(self.size // 2, self.size // 2)
        return image.rankfilter(self.size, self.rank)


class MedianFilter(RankFilter):
    """
    Create a median filter. Picks the median pixel value in a window with the
    given size.

    :param size: The kernel size, in pixels.
    """

    name = "Median"

    def __init__(self, size=3):
        self.size = size
        self.rank = size * size // 2


class MinFilter(RankFilter):
    """
    Create a min filter.  Picks the lowest pixel value in a window with the
    given size.

    :param size: The kernel size, in pixels.
    """

    name = "Min"

    def __init__(self, size=3):
        self.size = size
        self.rank = 0


class MaxFilter(RankFilter):
    """
    Create a max filter.  Picks the largest pixel value in a window with the
    given size.

    :param size: The kernel size, in pixels.
    """

    name = "Max"

    def __init__(self, size=3):
        self.size = size
        self.rank = size * size - 1


class ModeFilter(Filter):
    """
    Create a mode filter. Picks the most frequent pixel value in a box with the
    given size.  Pixel values that occur only once or twice are ignored; if no
    pixel value occurs more than twice, the original pixel value is preserved.

    :param size: The kernel size, in pixels.
    """

    name = "Mode"

    def __init__(self, size=3):
        self.size = size

    def filter(self, image):
        return image.modefilter(self.size)


class GaussianBlur(MultibandFilter):
    """Blurs the image with a sequence of extended box filters, which
    approximates a Gaussian kernel. For details on accuracy see
    <https://www.mia.uni-saarland.de/Publications/gwosdek-ssvm11.pdf>

    :param radius: Standard deviation of the Gaussian kernel.
    """

    name = "GaussianBlur"

    def __init__(self, radius=2):
        self.radius = radius

    def filter(self, image):
        return image.gaussian_blur(self.radius)


class BoxBlur(MultibandFilter):
    """Blurs the image by setting each pixel to the average value of the pixels
    in a square box extending radius pixels in each direction.
    Supports float radius of arbitrary size. Uses an optimized implementation
    which runs in linear time relative to the size of the image
    for any radius value.

    :param radius: Size of the box in one direction. Radius 0 does not blur,
                   returns an identical image. Radius 1 takes 1 pixel
                   in each direction, i.e. 9 pixels in total.
    """

    name = "BoxBlur"

    def __init__(self, radius):
        self.radius = radius

    def filter(self, image):
        return image.box_blur(self.radius)


class UnsharpMask(MultibandFilter):
    """Unsharp mask filter.

    See Wikipedia's entry on `digital unsharp masking`_ for an explanation of
    the parameters.

    :param radius: Blur Radius
    :param percent: Unsharp strength, in percent
    :param threshold: Threshold controls the minimum brightness change that
      will be sharpened

    .. _digital unsharp masking: https://en.wikipedia.org/wiki/Unsharp_masking#Digital_unsharp_masking

    """  # noqa: E501

    name = "UnsharpMask"

    def __init__(self, radius=2, percent=150, threshold=3):
        self.radius = radius
        self.percent = percent
        self.threshold = threshold

    def filter(self, image):
        return image.unsharp_mask(self.radius, self.percent, self.threshold)


class BLUR(BuiltinFilter):
    name = "Blur"
    # fmt: off
    filterargs = (5, 5), 16, 0, (
        1, 1, 1, 1, 1,
        1, 0, 0, 0, 1,
        1, 0, 0, 0, 1,
        1, 0, 0, 0, 1,
        1, 1, 1, 1, 1,
    )
    # fmt: on


class CONTOUR(BuiltinFilter):
    name = "Contour"
    # fmt: off
    filterargs = (3, 3), 1, 255, (
        -1, -1, -1,
        -1,  8, -1,
        -1, -1, -1,
    )
    # fmt: on


class DETAIL(BuiltinFilter):
    name = "Detail"
    # fmt: off
    filterargs = (3, 3), 6, 0, (
        0,  -1,  0,
        -1, 10, -1,
        0,  -1,  0,
    )
    # fmt: on


class EDGE_ENHANCE(BuiltinFilter):
    name = "Edge-enhance"
    # fmt: off
    filterargs = (3, 3), 2, 0, (
        -1, -1, -1,
        -1, 10, -1,
        -1, -1, -1,
    )
    # fmt: on


class EDGE_ENHANCE_MORE(BuiltinFilter):
    name = "Edge-enhance More"
    # fmt: off
    filterargs = (3, 3), 1, 0, (
        -1, -1, -1,
        -1,  9, -1,
        -1, -1, -1,
    )
    # fmt: on


class EMBOSS(BuiltinFilter):
    name = "Emboss"
    # fmt: off
    filterargs = (3, 3), 1, 128, (
        -1, 0, 0,
        0,  1, 0,
        0,  0, 0,
    )
    # fmt: on


class FIND_EDGES(BuiltinFilter):
    name = "Find Edges"
    # fmt: off
    filterargs = (3, 3), 1, 0, (
        -1, -1, -1,
        -1,  8, -1,
        -1, -1, -1,
    )
    # fmt: on


class SHARPEN(BuiltinFilter):
    name = "Sharpen"
    # fmt: off
    filterargs = (3, 3), 16, 0, (
        -2, -2, -2,
        -2, 32, -2,
        -2, -2, -2,
    )
    # fmt: on


class SMOOTH(BuiltinFilter):
    name = "Smooth"
    # fmt: off
    filterargs = (3, 3), 13, 0, (
        1, 1, 1,
        1, 5, 1,
        1, 1, 1,
    )
    # fmt: on


class SMOOTH_MORE(BuiltinFilter):
    name = "Smooth More"
    # fmt: off
    filterargs = (5, 5), 100, 0, (
        1, 1,  1, 1, 1,
        1, 5,  5, 5, 1,
        1, 5, 44, 5, 1,
        1, 5,  5, 5, 1,
        1, 1,  1, 1, 1,
    )
    # fmt: on


class Color3DLUT(MultibandFilter):
    """Three-dimensional color lookup table.

    Transforms 3-channel pixels using the values of the channels as coordinates
    in the 3D lookup table and interpolating the nearest elements.

    This method allows you to apply almost any color transformation
    in constant time by using pre-calculated decimated tables.

    .. versionadded:: 5.2.0

    :param size: Size of the table. One int or tuple of (int, int, int).
                 Minimal size in any dimension is 2, maximum is 65.
    :param table: Flat lookup table. A list of ``channels * size**3``
                  float elements or a list of ``size**3`` channels-sized
                  tuples with floats. Channels are changed first,
                  then first dimension, then second, then third.
                  Value 0.0 corresponds lowest value of output, 1.0 highest.
    :param channels: Number of channels in the table. Could be 3 or 4.
                     Default is 3.
    :param target_mode: A mode for the result image. Should have not less
                        than ``channels`` channels. Default is ``None``,
                        which means that mode wouldn't be changed.
    """

    name = "Color 3D LUT"

    def __init__(self, size, table, channels=3, target_mode=None, **kwargs):
        if channels not in (3, 4):
            raise ValueError("Only 3 or 4 output channels are supported")
        self.size = size = self._check_size(size)
        self.channels = channels
        self.mode = target_mode

        # Hidden flag `_copy_table=False` could be used to avoid extra copying
        # of the table if the table is specially made for the constructor.
        copy_table = kwargs.get("_copy_table", True)
        items = size[0] * size[1] * size[2]
        wrong_size = False

        numpy = None
        if hasattr(table, "shape"):
            try:
                import numpy
            except ImportError:  # pragma: no cover
                pass

        if numpy and isinstance(table, numpy.ndarray):
            if copy_table:
                table = table.copy()

            if table.shape in [
                (items * channels,),
                (items, channels),
                (size[2], size[1], size[0], channels),
            ]:
                table = table.reshape(items * channels)
            else:
                wrong_size = True

        else:
            if copy_table:
                table = list(table)

            # Convert to a flat list
            if table and isinstance(table[0], (list, tuple)):
                table, raw_table = [], table
                for pixel in raw_table:
                    if len(pixel) != channels:
                        raise ValueError(
                            "The elements of the table should "
                            "have a length of {}.".format(channels)
                        )
                    table.extend(pixel)

        if wrong_size or len(table) != items * channels:
            raise ValueError(
                "The table should have either channels * size**3 float items "
                "or size**3 items of channels-sized tuples with floats. "
                f"Table should be: {channels}x{size[0]}x{size[1]}x{size[2]}. "
                f"Actual length: {len(table)}"
            )
        self.table = table

    @staticmethod
    def _check_size(size):
        try:
            _, _, _ = size
        except ValueError as e:
            raise ValueError(
                "Size should be either an integer or a tuple of three integers."
            ) from e
        except TypeError:
            size = (size, size, size)
        size = [int(x) for x in size]
        for size1D in size:
            if not 2 <= size1D <= 65:
                raise ValueError("Size should be in [2, 65] range.")
        return size

    @classmethod
    def generate(cls, size, callback, channels=3, target_mode=None):
        """Generates new LUT using provided callback.

        :param size: Size of the table. Passed to the constructor.
        :param callback: Function with three parameters which correspond
                         three color channels. Will be called ``size**3``
                         times with values from 0.0 to 1.0 and should return
                         a tuple with ``channels`` elements.
        :param channels: The number of channels which should return callback.
        :param target_mode: Passed to the constructor of the resulting
                            lookup table.
        """
        size1D, size2D, size3D = cls._check_size(size)
        if channels not in (3, 4):
            raise ValueError("Only 3 or 4 output channels are supported")

        table = [0] * (size1D * size2D * size3D * channels)
        idx_out = 0
        for b in range(size3D):
            for g in range(size2D):
                for r in range(size1D):
                    table[idx_out : idx_out + channels] = callback(
                        r / (size1D - 1), g / (size2D - 1), b / (size3D - 1)
                    )
                    idx_out += channels

        return cls(
            (size1D, size2D, size3D),
            table,
            channels=channels,
            target_mode=target_mode,
            _copy_table=False,
        )

    def transform(self, callback, with_normals=False, channels=None, target_mode=None):
        """Transforms the table values using provided callback and returns
        a new LUT with altered values.

        :param callback: A function which takes old lookup table values
                         and returns a new set of values. The number
                         of arguments which function should take is
                         ``self.channels`` or ``3 + self.channels``
                         if ``with_normals`` flag is set.
                         Should return a tuple of ``self.channels`` or
                         ``channels`` elements if it is set.
        :param with_normals: If true, ``callback`` will be called with
                             coordinates in the color cube as the first
                             three arguments. Otherwise, ``callback``
                             will be called only with actual color values.
        :param channels: The number of channels in the resulting lookup table.
        :param target_mode: Passed to the constructor of the resulting
                            lookup table.
        """
        if channels not in (None, 3, 4):
            raise ValueError("Only 3 or 4 output channels are supported")
        ch_in = self.channels
        ch_out = channels or ch_in
        size1D, size2D, size3D = self.size

        table = [0] * (size1D * size2D * size3D * ch_out)
        idx_in = 0
        idx_out = 0
        for b in range(size3D):
            for g in range(size2D):
                for r in range(size1D):
                    values = self.table[idx_in : idx_in + ch_in]
                    if with_normals:
                        values = callback(
                            r / (size1D - 1),
                            g / (size2D - 1),
                            b / (size3D - 1),
                            *values,
                        )
                    else:
                        values = callback(*values)
                    table[idx_out : idx_out + ch_out] = values
                    idx_in += ch_in
                    idx_out += ch_out

        return type(self)(
            self.size,
            table,
            channels=ch_out,
            target_mode=target_mode or self.mode,
            _copy_table=False,
        )

    def __repr__(self):
        r = [
            f"{self.__class__.__name__} from {self.table.__class__.__name__}",
            "size={:d}x{:d}x{:d}".format(*self.size),
            f"channels={self.channels:d}",
        ]
        if self.mode:
            r.append(f"target_mode={self.mode}")
        return "<{}>".format(" ".join(r))

    def filter(self, image):
        from . import Image

        return image.color_lut_3d(
            self.mode or image.mode,
            Image.LINEAR,
            self.channels,
            self.size[0],
            self.size[1],
            self.size[2],
            self.table,
        )


!ls overlays

# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Pix2pix.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import time
from absl import app
from absl import flags

import tensorflow as tf

FLAGS = flags.FLAGS

flags.DEFINE_integer('buffer_size', 400, 'Shuffle buffer size')
flags.DEFINE_integer('batch_size', 1, 'Batch Size')
flags.DEFINE_integer('epochs', 1, 'Number of epochs')
flags.DEFINE_string('path', None, 'Path to the data folder')
flags.DEFINE_boolean('enable_function', True, 'Enable Function?')

IMG_WIDTH = 256
IMG_HEIGHT = 256
AUTOTUNE = tf.data.experimental.AUTOTUNE


def load(image_file):
  """Loads the image and generates input and target image.

  Args:
    image_file: .jpeg file

  Returns:
    Input image, target image
  """
  image = tf.io.read_file(image_file)
  image = tf.image.decode_jpeg(image)

  w = tf.shape(image)[1]

  w = w // 2
  real_image = image[:, :w, :]
  input_image = image[:, w:, :]

  input_image = tf.cast(input_image, tf.float32)
  real_image = tf.cast(real_image, tf.float32)

  return input_image, real_image


def resize(input_image, real_image, height, width):
  input_image = tf.image.resize(input_image, [height, width],
                                method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
  real_image = tf.image.resize(real_image, [height, width],
                               method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)

  return input_image, real_image


def random_crop(input_image, real_image):
  stacked_image = tf.stack([input_image, real_image], axis=0)
  cropped_image = tf.image.random_crop(
      stacked_image, size=[2, IMG_HEIGHT, IMG_WIDTH, 3])

  return cropped_image[0], cropped_image[1]


def normalize(input_image, real_image):
  input_image = (input_image / 127.5) - 1
  real_image = (real_image / 127.5) - 1

  return input_image, real_image


@tf.function
def random_jitter(input_image, real_image):
  """Random jittering.

  Resizes to 286 x 286 and then randomly crops to IMG_HEIGHT x IMG_WIDTH.

  Args:
    input_image: Input Image
    real_image: Real Image

  Returns:
    Input Image, real image
  """
  # resizing to 286 x 286 x 3
  input_image, real_image = resize(input_image, real_image, 286, 286)

  # randomly cropping to 256 x 256 x 3
  input_image, real_image = random_crop(input_image, real_image)

  if tf.random.uniform(()) > 0.5:
    # random mirroring
    input_image = tf.image.flip_left_right(input_image)
    real_image = tf.image.flip_left_right(real_image)

  return input_image, real_image


def load_image_train(image_file):
  input_image, real_image = load(image_file)
  input_image, real_image = random_jitter(input_image, real_image)
  input_image, real_image = normalize(input_image, real_image)

  return input_image, real_image


def load_image_test(image_file):
  input_image, real_image = load(image_file)
  input_image, real_image = resize(input_image, real_image,
                                   IMG_HEIGHT, IMG_WIDTH)
  input_image, real_image = normalize(input_image, real_image)

  return input_image, real_image


def create_dataset(path_to_train_images, path_to_test_images, buffer_size,
                   batch_size):
  """Creates a tf.data Dataset.

  Args:
    path_to_train_images: Path to train images folder.
    path_to_test_images: Path to test images folder.
    buffer_size: Shuffle buffer size.
    batch_size: Batch size

  Returns:
    train dataset, test dataset
  """
  train_dataset = tf.data.Dataset.list_files(path_to_train_images)
  train_dataset = train_dataset.shuffle(buffer_size)
  train_dataset = train_dataset.map(
      load_image_train, num_parallel_calls=AUTOTUNE)
  train_dataset = train_dataset.batch(batch_size)

  test_dataset = tf.data.Dataset.list_files(path_to_test_images)
  test_dataset = test_dataset.map(
      load_image_test, num_parallel_calls=AUTOTUNE)
  test_dataset = test_dataset.batch(batch_size)

  return train_dataset, test_dataset


class InstanceNormalization(tf.keras.layers.Layer):
  """Instance Normalization Layer (https://arxiv.org/abs/1607.08022)."""

  def __init__(self, epsilon=1e-5):
    super(InstanceNormalization, self).__init__()
    self.epsilon = epsilon

  def build(self, input_shape):
    self.scale = self.add_weight(
        name='scale',
        shape=input_shape[-1:],
        initializer=tf.random_normal_initializer(1., 0.02),
        trainable=True)

    self.offset = self.add_weight(
        name='offset',
        shape=input_shape[-1:],
        initializer='zeros',
        trainable=True)

  def call(self, x):
    mean, variance = tf.nn.moments(x, axes=[1, 2], keepdims=True)
    inv = tf.math.rsqrt(variance + self.epsilon)
    normalized = (x - mean) * inv
    return self.scale * normalized + self.offset


def downsample(filters, size, norm_type='batchnorm', apply_norm=True):
  """Downsamples an input.

  Conv2D => Batchnorm => LeakyRelu

  Args:
    filters: number of filters
    size: filter size
    norm_type: Normalization type; either 'batchnorm' or 'instancenorm'.
    apply_norm: If True, adds the batchnorm layer

  Returns:
    Downsample Sequential Model
  """
  initializer = tf.random_normal_initializer(0., 0.02)

  result = tf.keras.Sequential()
  result.add(
      tf.keras.layers.Conv2D(filters, size, strides=2, padding='same',
                             kernel_initializer=initializer, use_bias=False))

  if apply_norm:
    if norm_type.lower() == 'batchnorm':
      result.add(tf.keras.layers.BatchNormalization())
    elif norm_type.lower() == 'instancenorm':
      result.add(InstanceNormalization())

  result.add(tf.keras.layers.LeakyReLU())

  return result


def upsample(filters, size, norm_type='batchnorm', apply_dropout=False):
  """Upsamples an input.

  Conv2DTranspose => Batchnorm => Dropout => Relu

  Args:
    filters: number of filters
    size: filter size
    norm_type: Normalization type; either 'batchnorm' or 'instancenorm'.
    apply_dropout: If True, adds the dropout layer

  Returns:
    Upsample Sequential Model
  """

  initializer = tf.random_normal_initializer(0., 0.02)

  result = tf.keras.Sequential()
  result.add(
      tf.keras.layers.Conv2DTranspose(filters, size, strides=2,
                                      padding='same',
                                      kernel_initializer=initializer,
                                      use_bias=False))

  if norm_type.lower() == 'batchnorm':
    result.add(tf.keras.layers.BatchNormalization())
  elif norm_type.lower() == 'instancenorm':
    result.add(InstanceNormalization())

  if apply_dropout:
    result.add(tf.keras.layers.Dropout(0.5))

  result.add(tf.keras.layers.ReLU())

  return result


def unet_generator(output_channels, norm_type='batchnorm'):
  """Modified u-net generator model (https://arxiv.org/abs/1611.07004).

  Args:
    output_channels: Output channels
    norm_type: Type of normalization. Either 'batchnorm' or 'instancenorm'.

  Returns:
    Generator model
  """

  down_stack = [
      downsample(64, 4, norm_type, apply_norm=False),  # (bs, 128, 128, 64)
      downsample(128, 4, norm_type),  # (bs, 64, 64, 128)
      downsample(256, 4, norm_type),  # (bs, 32, 32, 256)
      downsample(512, 4, norm_type),  # (bs, 16, 16, 512)
      downsample(512, 4, norm_type),  # (bs, 8, 8, 512)
      downsample(512, 4, norm_type),  # (bs, 4, 4, 512)
      downsample(512, 4, norm_type),  # (bs, 2, 2, 512)
      downsample(512, 4, norm_type),  # (bs, 1, 1, 512)
  ]

  up_stack = [
      upsample(512, 4, norm_type, apply_dropout=True),  # (bs, 2, 2, 1024)
      upsample(512, 4, norm_type, apply_dropout=True),  # (bs, 4, 4, 1024)
      upsample(512, 4, norm_type, apply_dropout=True),  # (bs, 8, 8, 1024)
      upsample(512, 4, norm_type),  # (bs, 16, 16, 1024)
      upsample(256, 4, norm_type),  # (bs, 32, 32, 512)
      upsample(128, 4, norm_type),  # (bs, 64, 64, 256)
      upsample(64, 4, norm_type),  # (bs, 128, 128, 128)
  ]

  initializer = tf.random_normal_initializer(0., 0.02)
  last = tf.keras.layers.Conv2DTranspose(
      output_channels, 4, strides=2,
      padding='same', kernel_initializer=initializer,
      activation='tanh')  # (bs, 256, 256, 3)

  concat = tf.keras.layers.Concatenate()

  inputs = tf.keras.layers.Input(shape=[None, None, 3])
  x = inputs

  # Downsampling through the model
  skips = []
  for down in down_stack:
    x = down(x)
    skips.append(x)

  skips = reversed(skips[:-1])

  # Upsampling and establishing the skip connections
  for up, skip in zip(up_stack, skips):
    x = up(x)
    x = concat([x, skip])

  x = last(x)

  return tf.keras.Model(inputs=inputs, outputs=x)


def discriminator(norm_type='batchnorm', target=True):
  """PatchGan discriminator model (https://arxiv.org/abs/1611.07004).

  Args:
    norm_type: Type of normalization. Either 'batchnorm' or 'instancenorm'.
    target: Bool, indicating whether target image is an input or not.

  Returns:
    Discriminator model
  """

  initializer = tf.random_normal_initializer(0., 0.02)

  inp = tf.keras.layers.Input(shape=[None, None, 3], name='input_image')
  x = inp

  if target:
    tar = tf.keras.layers.Input(shape=[None, None, 3], name='target_image')
    x = tf.keras.layers.concatenate([inp, tar])  # (bs, 256, 256, channels*2)

  down1 = downsample(64, 4, norm_type, False)(x)  # (bs, 128, 128, 64)
  down2 = downsample(128, 4, norm_type)(down1)  # (bs, 64, 64, 128)
  down3 = downsample(256, 4, norm_type)(down2)  # (bs, 32, 32, 256)

  zero_pad1 = tf.keras.layers.ZeroPadding2D()(down3)  # (bs, 34, 34, 256)
  conv = tf.keras.layers.Conv2D(
      512, 4, strides=1, kernel_initializer=initializer,
      use_bias=False)(zero_pad1)  # (bs, 31, 31, 512)

  if norm_type.lower() == 'batchnorm':
    norm1 = tf.keras.layers.BatchNormalization()(conv)
  elif norm_type.lower() == 'instancenorm':
    norm1 = InstanceNormalization()(conv)

  leaky_relu = tf.keras.layers.LeakyReLU()(norm1)

  zero_pad2 = tf.keras.layers.ZeroPadding2D()(leaky_relu)  # (bs, 33, 33, 512)

  last = tf.keras.layers.Conv2D(
      1, 4, strides=1,
      kernel_initializer=initializer)(zero_pad2)  # (bs, 30, 30, 1)

  if target:
    return tf.keras.Model(inputs=[inp, tar], outputs=last)
  else:
    return tf.keras.Model(inputs=inp, outputs=last)


def get_checkpoint_prefix():
  checkpoint_dir = './training_checkpoints'
  checkpoint_prefix = os.path.join(checkpoint_dir, 'ckpt')

  return checkpoint_prefix


class Pix2pix(object):
  """Pix2pix class.

  Args:
    epochs: Number of epochs.
    enable_function: If true, train step is decorated with tf.function.
    buffer_size: Shuffle buffer size..
    batch_size: Batch size.
  """

  def __init__(self, epochs, enable_function):
    self.epochs = epochs
    self.enable_function = enable_function
    self.lambda_value = 100
    self.loss_object = tf.keras.losses.BinaryCrossentropy(from_logits=True)
    self.generator_optimizer = tf.keras.optimizers.Adam(2e-4, beta_1=0.5)
    self.discriminator_optimizer = tf.keras.optimizers.Adam(2e-4, beta_1=0.5)
    self.generator = unet_generator(output_channels=3)
    self.discriminator = discriminator()
    self.checkpoint = tf.train.Checkpoint(
        generator_optimizer=self.generator_optimizer,
        discriminator_optimizer=self.discriminator_optimizer,
        generator=self.generator,
        discriminator=self.discriminator)

  def discriminator_loss(self, disc_real_output, disc_generated_output):
    real_loss = self.loss_object(
        tf.ones_like(disc_real_output), disc_real_output)

    generated_loss = self.loss_object(tf.zeros_like(
        disc_generated_output), disc_generated_output)

    total_disc_loss = real_loss + generated_loss

    return total_disc_loss

  def generator_loss(self, disc_generated_output, gen_output, target):
    gan_loss = self.loss_object(tf.ones_like(
        disc_generated_output), disc_generated_output)

    # mean absolute error
    l1_loss = tf.reduce_mean(tf.abs(target - gen_output))
    total_gen_loss = gan_loss + (self.lambda_value * l1_loss)
    return total_gen_loss

  def train_step(self, input_image, target_image):
    """One train step over the generator and discriminator model.

    Args:
      input_image: Input Image.
      target_image: Target image.

    Returns:
      generator loss, discriminator loss.
    """
    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
      gen_output = self.generator(input_image, training=True)

      disc_real_output = self.discriminator(
          [input_image, target_image], training=True)
      disc_generated_output = self.discriminator(
          [input_image, gen_output], training=True)

      gen_loss = self.generator_loss(
          disc_generated_output, gen_output, target_image)
      disc_loss = self.discriminator_loss(
          disc_real_output, disc_generated_output)

    generator_gradients = gen_tape.gradient(
        gen_loss, self.generator.trainable_variables)
    discriminator_gradients = disc_tape.gradient(
        disc_loss, self.discriminator.trainable_variables)

    self.generator_optimizer.apply_gradients(zip(
        generator_gradients, self.generator.trainable_variables))
    self.discriminator_optimizer.apply_gradients(zip(
        discriminator_gradients, self.discriminator.trainable_variables))

    return gen_loss, disc_loss

  def train(self, dataset, checkpoint_pr):
    """Train the GAN for x number of epochs.

    Args:
      dataset: train dataset.
      checkpoint_pr: prefix in which the checkpoints are stored.

    Returns:
      Time for each epoch.
    """
    time_list = []
    if self.enable_function:
      self.train_step = tf.function(self.train_step)

    for epoch in range(self.epochs):
      start_time = time.time()
      for input_image, target_image in dataset:
        gen_loss, disc_loss = self.train_step(input_image, target_image)

      wall_time_sec = time.time() - start_time
      time_list.append(wall_time_sec)

      # saving (checkpoint) the model every 20 epochs
      if (epoch + 1) % 20 == 0:
        self.checkpoint.save(file_prefix=checkpoint_pr)

      template = 'Epoch {}, Generator loss {}, Discriminator Loss {}'
      print (template.format(epoch, gen_loss, disc_loss))

    return time_list


def run_main(argv):
  del argv
  kwargs = {'epochs': FLAGS.epochs, 'enable_function': FLAGS.enable_function,
            'path': FLAGS.path, 'buffer_size': FLAGS.buffer_size,
            'batch_size': FLAGS.batch_size}
  main(**kwargs)


def main(epochs, enable_function, path, buffer_size, batch_size):
  path_to_folder = path

  pix2pix_object = Pix2pix(epochs, enable_function)

  train_dataset, _ = create_dataset(
      os.path.join(path_to_folder, 'train/*.jpg'),
      os.path.join(path_to_folder, 'test/*.jpg'),
      buffer_size, batch_size)
  checkpoint_pr = get_checkpoint_prefix()
  print ('Training ...')
  return pix2pix_object.train(train_dataset, checkpoint_pr)


if __name__ == '__main__':
  app.run(run_main)




import IPython.display as display

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (12, 12)
mpl.rcParams['axes.grid'] = False

import numpy as np
import PIL.Image
import time
import functools

import tensorflow_hub as hub
hub_model = hub.load('/home/jack/Desktop/TENSORFLOW/Models/magenta_arbitrary-image-stylization-v1-256_2.tar.gz')
stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
tensor_to_image(stylized_image)


import tensorflow_hub as hub
hub_model = hub.load('/home/jack/Desktop/TENSORFLOW/Models/saved_model.pb')
stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
tensor_to_image(stylized_image)


import tensorflow as tf
dir(tf.test)

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

mnist=input_data.read_data_sets("MNIST_data")

import os
import sys
import scipy.io
import scipy.misc
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from PIL import Image
from nst_utils import *

import numpy as np
import tensorflow as tf

class CONFIG:
    IMAGE_WIDTH = 400
    IMAGE_HEIGHT = 300
    COLOR_CHANNELS = 3
    NOISE_RATIO = 0.6
    MEANS = np.array([123.68, 116.779, 103.939]).reshape((1,1,1,3)) 
    VGG_MODEL = 'pretrained-model/imagenet-vgg-verydeep-19.mat' # Pick the VGG 19-layer model by from the paper "Very Deep Convolutional Networks for Large-Scale Image Recognition".
    STYLE_IMAGE = 'images/stone_style.jpg' # Style image to use.
    CONTENT_IMAGE = 'images/content300.jpg' # Content image to use.
    OUTPUT_DIR = 'output/'
    
def load_vgg_model(path):
    """
    Returns a model for the purpose of 'painting' the picture.
    Takes only the convolution layer weights and wrap using the TensorFlow
    Conv2d, Relu and AveragePooling layer. VGG actually uses maxpool but
    the paper indicates that using AveragePooling yields better results.
    The last few fully connected layers are not used.
    Here is the detailed configuration of the VGG model:
        0 is conv1_1 (3, 3, 3, 64)
        1 is relu
        2 is conv1_2 (3, 3, 64, 64)
        3 is relu    
        4 is maxpool
        5 is conv2_1 (3, 3, 64, 128)
        6 is relu
        7 is conv2_2 (3, 3, 128, 128)
        8 is relu
        9 is maxpool
        10 is conv3_1 (3, 3, 128, 256)
        11 is relu
        12 is conv3_2 (3, 3, 256, 256)
        13 is relu
        14 is conv3_3 (3, 3, 256, 256)
        15 is relu
        16 is conv3_4 (3, 3, 256, 256)
        17 is relu
        18 is maxpool
        19 is conv4_1 (3, 3, 256, 512)
        20 is relu
        21 is conv4_2 (3, 3, 512, 512)
        22 is relu
        23 is conv4_3 (3, 3, 512, 512)
        24 is relu
        25 is conv4_4 (3, 3, 512, 512)
        26 is relu
        27 is maxpool
        28 is conv5_1 (3, 3, 512, 512)
        29 is relu
        30 is conv5_2 (3, 3, 512, 512)
        31 is relu
        32 is conv5_3 (3, 3, 512, 512)
        33 is relu
        34 is conv5_4 (3, 3, 512, 512)
        35 is relu
        36 is maxpool
        37 is fullyconnected (7, 7, 512, 4096)
        38 is relu
        39 is fullyconnected (1, 1, 4096, 4096)
        40 is relu
        41 is fullyconnected (1, 1, 4096, 1000)
        42 is softmax
    """
    
    vgg = scipy.io.loadmat(path)

    vgg_layers = vgg['layers']
    
    def _weights(layer, expected_layer_name):
        """
        Return the weights and bias from the VGG model for a given layer.
        """
        wb = vgg_layers[0][layer][0][0][2]
        W = wb[0][0]
        b = wb[0][1]
        layer_name = vgg_layers[0][layer][0][0][0][0]
        assert layer_name == expected_layer_name
        return W, b

        return W, b

    def _relu(conv2d_layer):
        """
        Return the RELU function wrapped over a TensorFlow layer. Expects a
        Conv2d layer input.
        """
        return tf.nn.relu(conv2d_layer)

    def _conv2d(prev_layer, layer, layer_name):
        """
        Return the Conv2D layer using the weights, biases from the VGG
        model at 'layer'.
        """
        W, b = _weights(layer, layer_name)
        W = tf.constant(W)
        b = tf.constant(np.reshape(b, (b.size)))
        return tf.nn.conv2d(prev_layer, filter=W, strides=[1, 1, 1, 1], padding='SAME') + b

    def _conv2d_relu(prev_layer, layer, layer_name):
        """
        Return the Conv2D + RELU layer using the weights, biases from the VGG
        model at 'layer'.
        """
        return _relu(_conv2d(prev_layer, layer, layer_name))

    def _avgpool(prev_layer):
        """
        Return the AveragePooling layer.
        """
        return tf.nn.avg_pool(prev_layer, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # Constructs the graph model.
    graph = {}
    graph['input']   = tf.Variable(np.zeros((1, CONFIG.IMAGE_HEIGHT, CONFIG.IMAGE_WIDTH, CONFIG.COLOR_CHANNELS)), dtype = 'float32')
    graph['conv1_1']  = _conv2d_relu(graph['input'], 0, 'conv1_1')
    graph['conv1_2']  = _conv2d_relu(graph['conv1_1'], 2, 'conv1_2')
    graph['avgpool1'] = _avgpool(graph['conv1_2'])
    graph['conv2_1']  = _conv2d_relu(graph['avgpool1'], 5, 'conv2_1')
    graph['conv2_2']  = _conv2d_relu(graph['conv2_1'], 7, 'conv2_2')
    graph['avgpool2'] = _avgpool(graph['conv2_2'])
    graph['conv3_1']  = _conv2d_relu(graph['avgpool2'], 10, 'conv3_1')
    graph['conv3_2']  = _conv2d_relu(graph['conv3_1'], 12, 'conv3_2')
    graph['conv3_3']  = _conv2d_relu(graph['conv3_2'], 14, 'conv3_3')
    graph['conv3_4']  = _conv2d_relu(graph['conv3_3'], 16, 'conv3_4')
    graph['avgpool3'] = _avgpool(graph['conv3_4'])
    graph['conv4_1']  = _conv2d_relu(graph['avgpool3'], 19, 'conv4_1')
    graph['conv4_2']  = _conv2d_relu(graph['conv4_1'], 21, 'conv4_2')
    graph['conv4_3']  = _conv2d_relu(graph['conv4_2'], 23, 'conv4_3')
    graph['conv4_4']  = _conv2d_relu(graph['conv4_3'], 25, 'conv4_4')
    graph['avgpool4'] = _avgpool(graph['conv4_4'])
    graph['conv5_1']  = _conv2d_relu(graph['avgpool4'], 28, 'conv5_1')
    graph['conv5_2']  = _conv2d_relu(graph['conv5_1'], 30, 'conv5_2')
    graph['conv5_3']  = _conv2d_relu(graph['conv5_2'], 32, 'conv5_3')
    graph['conv5_4']  = _conv2d_relu(graph['conv5_3'], 34, 'conv5_4')
    graph['avgpool5'] = _avgpool(graph['conv5_4'])
    
    return graph

def generate_noise_image(content_image, noise_ratio = CONFIG.NOISE_RATIO):
    """
    Generates a noisy image by adding random noise to the content_image
    """
    
    # Generate a random noise_image
    noise_image = np.random.uniform(-20, 20, (1, CONFIG.IMAGE_HEIGHT, CONFIG.IMAGE_WIDTH, CONFIG.COLOR_CHANNELS)).astype('float32')
    
    # Set the input_image to be a weighted average of the content_image and a noise_image
    input_image = noise_image * noise_ratio + content_image * (1 - noise_ratio)
    
    return input_image


def reshape_and_normalize_image(image):
    """
    Reshape and normalize the input image (content or style)
    """
    
    # Reshape image to mach expected input of VGG16
    image = np.reshape(image, ((1,) + image.shape))
    
    # Substract the mean to match the expected input of VGG16
    image = image - CONFIG.MEANS
    
    return image


def save_image(path, image):
    
    # Un-normalize the image so that it looks good
    image = image + CONFIG.MEANS
    
    # Clip and Save the image
    image = np.clip(image[0], 0, 255).astype('uint8')
scipy.misc.imsave(path, image)

import re
import os
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers
from kaggle_datasets import KaggleDatasets
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import time
from IPython import display
import PIL

try:
    tpu = tf.distribute.cluster_resolver.TPUClusterResolver()
    print('Device:', tpu.master())
    tf.config.experimental_connect_to_cluster(tpu)
    tf.tpu.experimental.initialize_tpu_system(tpu)
    strategy = tf.distribute.experimental.TPUStrategy(tpu)
except:
    strategy = tf.distribute.get_strategy()
print('Number of replicas:', strategy.num_replicas_in_sync)
    
print(tf.__version__)

# What version of Python do you have?
import sys

import tensorflow.keras
import pandas as pd
import sklearn as sk
import tensorflow as tf

check_gpu = len(tf.config.list_physical_devices('GPU'))>0

print(f"Tensor Flow Version: {tf.__version__}")
print(f"Keras Version: {tensorflow.keras.__version__}")
print()
print(f"Python {sys.version}")
print(f"Pandas {pd.__version__}")
print(f"Scikit-Learn {sk.__version__}")
print("GPU is", "available" if check_gpu \
      else "NOT AVAILABLE")


import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import torch.nn.init as nninit
import torch.onnx



class net(nn.Module):
    def __init__(self):
        super(net, self).__init__()

        self.ln1 = nn.Linear(10, 32, bias=True)
        self.ln2 = nn.Linear(32, 32, bias=True)
        self.ln3 = nn.Linear(32, 32, bias=True)
        self.ln4 = nn.Linear(32, 32, bias=True)
        self.ln5 = nn.Linear(32, 3, bias=False)

        nn.init.uniform_(self.ln1.weight, a=-1, b=1)
        nn.init.uniform_(self.ln2.weight, a=-1, b=1)

        nn.init.normal_(self.ln3.weight)
        nn.init.normal_(self.ln4.weight)
        nn.init.normal_(self.ln5.weight)

        self.tanh1 = nn.Tanh()
        self.tanh2 = nn.Tanh()
        self.tanh3 = nn.Tanh()
        self.tanh4 = nn.Tanh()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        U = self.ln1(x)
        U = self.tanh1(U)

        U = self.ln2(U)
        U = self.tanh2(U)

        U = self.ln3(U)
        U = self.tanh3(U)

        U = self.ln4(U)
        U = self.tanh4(U)

        U = self.ln5(U)
        return self.sigmoid(U)

height = 480
width = 720
scale = 0.3
z_size = 7  
num_images = 200
alpha = 1  # constant for shifting vector z

model_dir = 'models/'
base_name = "images/"
model_name = 'arts_model'
pytorch_ending = ".pt"
onnx_ending = ".onnx"


def createInputVec(z,x,y):
    '''
    Create the input vector for the neural net
    '''
    
    r = math.sqrt(((x*scale-(x*scale/2))**2) + ((y*scale-(y*scale/2))**2) )
    z_size = len(z)
    input = torch.rand(1,z_size + 3)
    
    for i in range(z_size):
        input[0][i] = z[i] * scale
        
    input[0][z_size] = x * scale
    input[0][z_size+1] = y * scale
    input[0][z_size+2] = r
    input = Variable(input)
    return input

def update_z(z, alpha=1):
    '''
    shifts the vector z by alpha
    '''
    
    for i in range (len(z)):
        z[i] = z[i] + alpha
    return z


!mkdir torchimages/images/



G = net()
z = torch.rand(z_size)
import time
#batch produce images
for i in range(num_images):
    print("Please wait while creating image no. "+str(i+1))

    update_z(z, alpha)
     
    image = np.zeros((height * width, 3)) 
    for h in range(height):
        
        for w in range(width):
            input = createInputVec(z,h,w)
            image[h * width + w] = G(input).data.numpy()

    image = image.reshape(height, width,3)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    #savefile = "images/"+timestr+".jpg"
    #im.save(savefile)
    image_name = "torchimages/"+base_name + model_name + timestr+ "_" + str(i+1)+ ".png"
    print(image_name)

    #imgplot = plt.imshow(image)
    #plt.show()
    plt.imsave(image_name, image)


# save pytorch model
torch.save(G, model_dir + model_name + pytorch_ending)

# save onnx model
dummy_input = torch.randn(1, z_size + 3) # same size as input.shape
torch.onnx.export(G, dummy_input, model_dir + model_name + onnx_ending)
torch.onnx.export(G, dummy_input, model_dir + model_name + "_40000"+ onnx_ending)  # create a second model for batch inference


!mkdir models

def tensor_to_image(tensor):
    tensor = tensor*255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor)>3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
    return PIL.Image.fromarray(tensor)
def load_img(path_to_img):
    max_dim = 512
    img = tf.io.read_file(path_to_img)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)

    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim

    new_shape = tf.cast(shape * scale, tf.int32)

    img = tf.image.resize(img, new_shape)
    img = img[tf.newaxis, :]
    return img
def imshow(image, title=None):
    if len(image.shape) > 3:
        image = tf.squeeze(image, axis=0)

    plt.imshow(image)
    if title:
        plt.title(title)

import cv2

!ffmpeg -framerate 60 -pattern_type glob -i 'torchimages/images/*.png' -r 15 -vf scale=720:480 out.gif

import tensorflow as tf
# Converting a SavedModel to a TensorFlow Lite model.
saved_model_dir = r"models"
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()

# Converting a tf.Keras model to a TensorFlow Lite model.
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Converting ConcreteFunctions to a TensorFlow Lite model.
converter = tf.lite.TFLiteConverter.from_concrete_functions([func])
tflite_model = converter.convert()


def load_model(model_name):
    base_url = 'http://download.tensorflow.org/models/object_detection/'
    model_file = model_name + '.tar.gz'
    model_dir = tf.keras.utils.get_file(
    fname=model_name, 
    origin=base_url + model_file,
    untar=True)

    model_dir = pathlib.Path(model_dir)/"saved_model"

    model = tf.saved_model.load(str(model_dir))
    model = model.signatures['serving_default']

    return model


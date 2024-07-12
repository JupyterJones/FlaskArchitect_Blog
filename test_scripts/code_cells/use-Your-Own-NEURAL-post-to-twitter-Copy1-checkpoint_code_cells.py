#!/home/jack/miniconda3/envs/cloned_base/bin/python
from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageFilter, ImageEnhance
from tensorflow.python.ops.numpy_ops import np_config
np_config.enable_numpy_behavior()
import random
import os
import numpy as np
from random import randint
import sys
import markovify
import twython
from twython import Twython
import time
import shutil
from randtext import randTXT
import tensorflow as tf
import tensorflow_hub as hub
import os
import tensorflow as tf
# Load compressed models from tensorflow_hub
os.environ['TFHUB_MODEL_LOAD_FORMAT'] = 'COMPRESSED'
import IPython.display as display
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (12, 12)
mpl.rcParams['axes.grid'] = False
import PIL.Image

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


path = r"/home/jack/Desktop/Imagedata/0-original-images/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
content=(path+base_image)
print("content"+path+base_image)

#content = "/home/jack/Pictures/1022362.jpg"


path = r"/home/jack/Desktop/Imagedata/4-publish-images/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
style=(path+base_image)
print("style"+path+base_image)
#style = "/home/jack/Pictures/1022362.jpg

content_image = load_img(prep_content(content))
style_image = load_img(prep_style(style))
# A node server http-server was started in Directory before the "Models" directory
hub_model = hub.load('http://localhost:8080/Models/magenta_arbitrary-image-stylization-v1-256_2.tar.gz')
#hub_model = hub.load('http://localhost:8080/Models/magenta_arbitrary-image-stylization-v1-256_fp16_transfer_1.tflite')
stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
im = tensor_to_image(stylized_image)
timestr = time.strftime("%Y%m%d-%H%M%S")
savefile = "images/"+timestr+".jpg"
im.save(savefile)
#print(im.size)
#im
iml = im.resize((720,480), Image.NEAREST)
iml.save("720x480/temp.jpg")
#iml

im = Image.open("720x480/temp.jpg")
enhancer = ImageEnhance.Sharpness(im)
factor = 1.5
im_s_1 = enhancer.enhance(factor)


factor = 0.5 #decrease constrast
enhancer = ImageEnhance.Contrast(im_s_1)

factor = 1.5 #increase contrast
im_output = enhancer.enhance(factor)
im_output.save('720x480/Sharpened-temp.jpg');


STR = randTXT()
Hash = ["#AIart #Tensorflow #twitme #Python #100DaysOfCode\n","#tensorflow #styletransfer #PythonGraphics #PIL #PythonImageLibrary\n","#NFTartist #NFTProject #NEARnft #nearNFTs \n","#NFT #NFTs #NFTCommunity #NFTdrop #nftart\n","#CreativeCoding  #AI #genart #p5js #Generative\n","#twitme #Python #100DaysOfCode\n","#Python #100DaysOfCode #PythonBots #codefor30days\n" ]
hashnum = randint(0,len(Hash)-1)
hashs =Hash[0]
# add the hash to STR generated with randTXT()
STR = hashs
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
#filename1='images/result.png'
filename1='720x480/Sharpened-temp.jpg'

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
draw.text(xy=(x-10,y+220), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x-11,y+221), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x-12,y+219), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x-10,y+218), text=text, fill=COLor[0], font=font, anchor='mm')
blurred = blurred.filter(ImageFilter.BoxBlur(2))

# Paste soft text onto background
bg.paste(blurred,blurred)

# Draw on sharp text
draw = ImageDraw.Draw(bg)
draw.text(xy=(x-10,y+220), text=text, fill=COLor[1], font=font, anchor='mm')
postage = ["perferations.png","perferations+.png","frames.png","usa-perferations.png","usar-perferations.png","usal-perferations.png"]
Num = randint( 0, len(postage)-1)
BOARDER ="overlays/frame-lite.png"
#BOARDER ="overlays/nouveau-black-frame1.png"
#BOARDER = "overlays/"+postage[Num]
mask=Image.open(BOARDER).convert('RGBA') 
bg.paste(mask, (0,0), mask=mask)
bg.save('images/useresult1.png')
#removed keys for privacy reasons
CONSUMER_KEY = 'APIkey()[0]'
CONSUMER_SECRET = 'APIkey()[1]'
ACCESS_KEY = 'APIkey()[2]'
ACCESS_SECRET = 'APIkey()[3]'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
PATH = "images/useresult.png"
timestr = time.strftime("%Y%m%d-%H%M%S")
#print (timestr+".png")

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
STR0 = randTXT()
STRu= STR0[:180]
print(STRu)
im

print(STRu)

response = twitter.upload_media(media=photo)
twitter.update_status(status=STRu, media_ids=[response['media_id']])









!pwd

!http-server /home/jack/Desktop/TENSORFLOW/models/magenta_arbitrary-image-stylization-v1-256_2/

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

from tensorflow.python.ops.numpy_ops import np_config
np_config.enable_numpy_behavior()
from PIL import Image
import random
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


path = r"/home/jack/Desktop/Imagedata/0-original-images/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
content=(path+base_image)
print("content"+path+base_image)

#content = "/home/jack/Pictures/1022362.jpg"
#content = "/home/jack/Desktop/TENSORFLOW/images/default-file-q4.png"

path = r"/home/jack/Desktop/Imagedata/4-publish-images/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
style=(path+base_image)
print("style"+path+base_image)
#style = "/home/jack/Pictures/JuanjoCristianitarotdeck/juanjo-cristiani-11.png"
#style = "/home/jack/Pictures/0_.jpg"
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
import tensorflow as tf
import tensorflow_hub as hub
import time
hub_model = hub.load('http://localhost:8080/Models/magenta_arbitrary-image-stylization-v1-256_2.tar.gz')
#hub_model = hub.load('http://localhost:8080/Models/magenta_arbitrary-image-stylization-v1-256_fp16_transfer_1.tflite')
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
STR = hashs
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
#filename1='images/result.png'
filename1='720x480/Sharpened-temp.jpg'

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
draw.text(xy=(x-10,y+220), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x-11,y+221), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x-12,y+219), text=text, fill=COLor[0], font=font, anchor='mm')
draw.text(xy=(x-10,y+218), text=text, fill=COLor[0], font=font, anchor='mm')
blurred = blurred.filter(ImageFilter.BoxBlur(2))

# Paste soft text onto background
bg.paste(blurred,blurred)

# Draw on sharp text
draw = ImageDraw.Draw(bg)
draw.text(xy=(x-10,y+220), text=text, fill=COLor[1], font=font, anchor='mm')
postage = ["perferations.png","perferations+.png","frames.png","usa-perferations.png","usar-perferations.png","usal-perferations.png"]
Num = randint( 0, len(postage)-1)
BOARDER ="overlays/frame-lite.png"
#BOARDER ="overlays/nouveau-black-frame1.png"
#BOARDER = "overlays/"+postage[Num]
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

response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])



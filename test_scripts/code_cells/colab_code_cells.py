
import tensorflow_hub as hub
import random
from PIL import Image
import os
import sys
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import time

def load_img(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img
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
print("content: "+path+base_image)

#content = "/home/jack/Pictures/1022362.jpg"
path = r"/home/jack/Desktop/Imagedata/4-publish-images/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
style=(path+base_image)
print("style: "+path+base_image)
#style = "/home/jack/Pictures/1022362.jpg

content_image = load_img(prep_content(content))
style_image = load_img(prep_style(style))
content_image.shape
def tensor_to_image(tensor):
    tensor = tensor*255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor)>3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
        return Image.fromarray(tensor)
tensor = style_image
im = tensor_to_image(tensor)
timestr = time.strftime("%Y%m%d-%H%M%S")
savefile = "images/"+timestr+".jpg"
print(savefile)
im.save(savefile)
#TensorShape([1, 200, 200, 3])


im = Image.open(savefile)
print(im.size)
im


!mkdir /home/jack/Desktop/Imagedata/newstuff

%matplotlib inline
from matplotlib import pyplot as plt
path = r"/home/jack/Desktop/Imagedata/0-original-images/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
content=(path+base_image)
print("content: "+path+base_image)

#content = "/home/jack/Pictures/1022362.jpg"
path = r"/home/jack/Desktop/Imagedata/4-publish-images/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
style=(path+base_image)
print("style: "+path+base_image)

im1 = Image.open(content)
im2 = Image.open(style)

plt.figure(figsize = (10,10))
plt.imshow(im1)
plt.imshow(im2, alpha=0.5)


from PIL import Image
import time
import random
import os

def mknewimage(path1,path2):
    base_image = random.choice([
        x for x in os.listdir(path1)
        if os.path.isfile(os.path.join(path1, x))
    ])
    content=(path1+base_image)
    print("content: "+path1+base_image)

    #content = "/home/jack/Pictures/1022362.jpg"
    #path2 = r"/home/jack/Desktop/Imagedata/4-publish-images/"
    base_image = random.choice([
        x for x in os.listdir(path2)
        if os.path.isfile(os.path.join(path2, x))
    ])
    style=(path2+base_image)
    print("style: "+path2+base_image)

    im1 = Image.open(content)
    background = im1.resize((720,480), Image.BICUBIC)
    im2 = Image.open(style)
    overlay = im2.resize((720,480), Image.BICUBIC)
    #background = Image.open(content)
    #overlay = Image.open(style)

    background = background.convert("RGBA")
    overlay = overlay.convert("RGBA")

    new_img = Image.blend(background, overlay, 0.6)

    timestr = time.strftime("%Y%m%d-%H%M%S")
    savefile = "/home/jack/Desktop/Imagedata/newstuff/"+timestr+".png"
    print(savefile)

    new_img.save(savefile,"PNG")
    return new_img

for x in range(0,300):
    time.sleep(5)
    path1 = r"/home/jack/Desktop/Imagedata/0-original-images/"
    path2 = r"/home/jack/Desktop/Imagedata/4-publish-images/"
    nim = mknewimage(path1,path2)
    print(x,nim)


for x in range(300,900):
    time.sleep(5)
    path1 = r"/home/jack/Desktop/Imagedata/0-original-images/"
    path2 = r"/home/jack/Desktop/Imagedata/4-publish-images/"
    nim = mknewimage(path1,path2)
    print(x,nim)


def mknewimage(path1):
    base_image = random.choice([
        x for x in os.listdir(path1)
        if os.path.isfile(os.path.join(path1, x))
    ])
    content=(path1+base_image)
    print("content: "+path1+base_image)
path1 = r"/home/jack/Desktop/Imagedata/0-original-images/"
mknewimage(path1)

from PIL import Image
import time


def mknewimage(path1,path2):
    base_image = random.choice([
        x for x in os.listdir(path1)
        if os.path.isfile(os.path.join(path1, x))
    ])
    content=(path1+base_image)
    print("content: "+path1+base_image)

    #content = "/home/jack/Pictures/1022362.jpg"
    #path2 = r"/home/jack/Desktop/Imagedata/4-publish-images/"
    base_image = random.choice([
        x for x in os.listdir(path2)
        if os.path.isfile(os.path.join(path2, x))
    ])
    style=(path2+base_image)
    print("style: "+path2+base_image)

    im1 = Image.open(content)
    background = im1.resize((720,480), Image.BICUBIC)
    im2 = Image.open(style)
    overlay = im2.resize((720,480), Image.BICUBIC)
 

    background = background.convert("RGBA")
    overlay = overlay.convert("RGBA")

    new_img = Image.blend(background, overlay, 0.6)

    timestr = time.strftime("%Y%m%d-%H%M%S")
    savefile = "/home/jack/Desktop/Imagedata/newstuff/"+timestr+".png"
    print(savefile)

    new_img.save(savefile,"PNG")
    return new_img


path1 = r"/home/jack/Desktop/Imagedata/0-original-images/"
path2 = r"/home/jack/Desktop/Imagedata/4-publish-images/"
nim = mknewimage(path1,path2)
nim

img = im
PI = Image.open("/home/jack/Desktop/Imagedata/4-publish-images/00257polarized.jpg")
PI = PI.resize((720,480), Image.NEAREST)

import numpy as np
mask = img
#mask[3:-3, 3:-3] = 1 # white square in black background
im = mask + PI#np.random.randn(10,10) * 0.01 # random image
masked = np.ma.masked_where(mask == 0, mask)

import matplotlib.pyplot as plt
plt.figure()
plt.subplot(1,2,1)
plt.imshow(im, 'gray', interpolation='none')
plt.subplot(1,2,2)
plt.imshow(im, 'gray', interpolation='none')
plt.imshow(masked, 'jet', interpolation='none', alpha=0.7)
plt.show()


import numpy as np
mask = np.zeros((10,10))
mask[3:-3, 3:-3] = 1 # white square in black background
im = mask + np.random.randn(10,10) * 0.01 # random image
masked = np.ma.masked_where(mask == 0, mask)

import matplotlib.pyplot as plt
plt.figure()
plt.subplot(1,2,1)
plt.imshow(im, 'gray', interpolation='none')
plt.subplot(1,2,2)
plt.imshow(im, 'gray', interpolation='none')
plt.imshow(masked, 'jet', interpolation='none', alpha=0.7)
plt.show()


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
im_s_1.save('720x480/Sharpened-temp.jpg');


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

im

def load_img(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img


from PIL import Image
im = Image.open(savefile)
print(im.size)
im

style_image

import time

def tensor_to_image(tensor):
    tensor = tensor*255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor)>3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
        return Image.fromarray(tensor)
tensor = style_image
im = tensor_to_image(tensor)
timestr = time.strftime("%Y%m%d-%H%M%S")
savefile = "images/"+timestr+".jpg"
print(savefile)
im.save(savefile)

# A node server http-server was started in Directory before the "Models" directory
hub_model = hub.load('http://localhost:8080/Models/magenta_arbitrary-image-stylization-v1-256_2.tar.gz')
#hub_model = hub.load('http://localhost:8080/Models/magenta_arbitrary-image-stylization-v1-256_fp16_transfer_1.tflite')


content_image = load_image('profile.jfif')
style_image = load_image('monet.jpeg')

2. Visualize Output

content_image.shape

TensorShape([1, 200, 200, 3])

plt.imshow(np.squeeze(style_image))
plt.show()



def random_image(path0):
        random_file = random.choice(os.listdir(path0))
        random_file_path = os.path.join(path0, random_file)
        return random_file_path
    
def random_image2(path1):
        random_file = random.choice(os.listdir(path1))
        random_file_path = os.path.join(path1, random_file)
        return random_file_path
    
path0 = "/home/jack/Desktop/Imagedata/0-original-images/"
content=random_image(path0)
print("content"+content)
#content = "/home/jack/Pictures/1022362.jpg"

path1 = "/home/jack/Desktop/Imagedata/4-publish-images/"
style=random_image2(path1)
print("style"+style)
    


#!/home/jack/miniconda3/envs/cloned_base/bin/python
from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageFilter, ImageEnhance
import PIL
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
import matplotlib.pyplot as plt
def main():
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

    
    #find a random image in the folder and return the path
    def random_image(path0):
        random_file = random.choice(os.listdir(path0))
        random_file_path = os.path.join(path0, random_file)
        return random_file_path
    path0 = "/home/jack/Desktop/Imagedata/0-original-images/"
    content=random.choice([x for x in os.listdir(path0) if os.path.isfile(os.path.join(path0, x))])
    #content=random_image(path0)
    print("content"+content)
    #content = "/home/jack/Pictures/1022362.jpg"
    
    def random_image2(path1):
        random_file = random.choice(os.listdir(path1))
        random_file_path = os.path.join(path1, random_file)
        return random_file_path
    path1 = "/home/jack/Desktop/Imagedata/4-publish-images/"
    style=random.choice([x for x in os.listdir(path1) if os.path.isfile(os.path.join(path1, x))])
    #style=random_image2(path1)
    print("style"+style)
    
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
    im_s_1.save('720x480/Sharpened-temp.jpg');


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
    im

    #response = twitter.upload_media(media=photo)
    #twitter.update_status(status=STR, media_ids=[response['media_id']])

main()

import os
import random
import dircache

dir = 'posted/'
filename = random.choice(dircache.listdir(dir))
path = os.path.join(dir, filename)
print(path)




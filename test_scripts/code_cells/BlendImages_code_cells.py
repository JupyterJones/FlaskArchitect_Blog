!ls tmpseg

from PIL import Image
import time
# Function to change the image size
def changeImageSize(maxWidth, 
                    maxHeight, 
                    image):
    
    widthRatio  = maxWidth/image.size[0]
    heightRatio = maxHeight/image.size[1]

    newWidth    = int(widthRatio*image.size[0])
    newHeight   = int(heightRatio*image.size[1])

    newImage    = image.resize((newWidth, newHeight))
    return newImage
    
# Take two images for blending them together   
image1 = Image.open("tmpseg/20220921-072955__10.png")
image2 = Image.open("tmpseg/20220921-072811__10.png")

# Make the images of uniform size
image3 = changeImageSize(720, 480, image1)
image4 = changeImageSize(720, 480, image2)

# Make sure images got an alpha channel
image5 = image3.convert("RGBA")
image6 = image4.convert("RGBA")

# Display the original images
#image5.show()
#image6.show()

# alpha-blend the images with varying values of alpha
alphaBlended1 = Image.blend(image5, image6, alpha=.2)
alphaBlended2 = Image.blend(image5, image6, alpha=.4)

# Display the alpha-blended images
#alphaBlended1.show()
timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "segmented/"+timestr+"_.png"
im = alphaBlended1.save(filename)
img = Image.open(filename)
img
#alphaBlended2.show()

!mkdir segmented

!ls -d */

#%%writefile Blender.py
from PIL import Image
import time
import random
import os
# Function to change the image size
def changeImageSize(maxWidth, 
                    maxHeight, 
                    image):
    
    widthRatio  = maxWidth/image.size[0]
    heightRatio = maxHeight/image.size[1]

    newWidth    = int(widthRatio*image.size[0])
    newHeight   = int(heightRatio*image.size[1])

    newImage    = image.resize((newWidth, newHeight))
    return newImage

path = r"Australian%20Lizards/"
base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
filename0=(path+base_image)



patho = r"black%20and%20white%20art%20nouveau%20drawings/"
base_image = random.choice([
    x for x in os.listdir(patho)
    if os.path.isfile(os.path.join(patho, x))
])
filename00=(patho+base_image)





# Take two images for blending them together   
image1 = Image.open(filename0)
image2 = Image.open(filename00)
def Blendem(image1, image2,  Image1Alpha =.2, Image2Alpha =.4 ):
    # Make the images of uniform size
    image3 = changeImageSize(720, 480, image1)
    image4 = changeImageSize(720, 480, image2)

    # Make sure images got an alpha channel
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    # alpha-blend the images with varying values of alpha
    Image1Alpha =.2
    Image2Alpha =.4
    alphaBlended1 = Image.blend(image5, image6, alpha=Image1Alpha)
    alphaBlended2 = Image.blend(image5, image6, alpha=Image2Alpha)

    # Display the alpha-blended images
    #alphaBlended1.show()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "segmented/"+timestr+"XX.png"
    im = alphaBlended1.save(filename)
    #img = Image.open(filename)
    #img
    #alphaBlended2.show()
    return im

Blendem(image1, image2,  Image1Alpha =.1, Image2Alpha =.9 )

image1 = Image.open("tmpseg/20220921-072955__10.png")
image2 = Image.open("tmpseg/20220921-072811__10.png")
Blendem(image1, image2)

!ls segmented

im




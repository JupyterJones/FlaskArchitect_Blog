%%writefile auto_canny.py
# import the necessary packages
import numpy as np
import argparse
import glob
import cv2
def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
	# return the edged image
	return edged

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to input dataset of images")
args = vars(ap.parse_args())
# loop over the images
for imagePath in glob.glob(args["images"] + "/*.jpg"):
	# load the image, convert it to grayscale, and blur it slightly
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (3, 3), 0)
	# apply Canny edge detection using a wide threshold, tight
	# threshold, and automatically determined threshold
	wide = cv2.Canny(blurred, 10, 200)
	tight = cv2.Canny(blurred, 225, 250)
	auto = auto_canny(blurred)
	# show the images
	cv2.imshow("Original", image)
	cv2.imshow("Edges", np.hstack([wide, tight, auto]))
	cv2.waitKey(0)


import numpy as np
import argparse
import glob
import cv2
import imageio
def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
	# return the edged image
	return edged


#note7
from PIL import Image
import numpy as np
import cv2
import imageio
from FileNameP import FilenameByTime


def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    # return the edged image
    return edged

#image = cv2.imread('mahotastest/orig-color.png')
filename1 = '/home/jack/Desktop/Imagedata/0-original-images/07082orig.jpg'
image = cv2.imread(filename1)
edged = auto_canny(image, sigma=0.33)
inverted = cv2.bitwise_not(edged)
cv2.imwrite("mahotastest/temp2.png", inverted)
cv2.imwrite(FilenameByTime("mahotastest/"), inverted)



# Open Front Image
#frontimage = Image.open('mahotastest/inverted-bitwise-note3_6.png').convert("1")
frontimage = Image.open('mahotastest/temp2.png').convert("1")
frontImage = frontimage.convert("RGBA")
datas = frontImage.getdata()


newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

frontImage.putdata(newData)
#frontImage.save("mahotastest/frontImage-note7.png", "PNG")

# Back Image
#image = cv2.imread('mahotastest/orig-color.png')
#filename1 = '/home/jack/Desktop/Imagedata/0-original-images/05140orig.jpg'
# Open Background Image
background = Image.open(filename1)
#background = cv2.imread('mahotastest/orig-color.png')#.convert("RGBA")

# Convert image to RGBA
#frontImage = frontImage.convert("RGBA")

# Convert image to RGBA
#background = background.convert("RGBA")

# Calculate width to be at the center
width = (frontimage.width - frontimage.width) // 2

# Calculate height to be at the center
height = (frontimage.height - frontimage.height) // 2

# Paste the frontImage at (width, height)
background.paste(frontImage, (width, height), frontImage)

# Save this image
background.save("mahotastest/-atlast000.png", format="png")
savefile = FilenameByTime("mahotastest/")
background.save(savefile, format="png")
#background = background.convert("RGB")

%%writefile OutlineImage.py
"""
USE:
from OutlineImage import *
orig_file = "junk/00000.jpg"
new_extension = ".jnk"
NEW = change_extension(orig_file,new_extension)
print(NEW)

filename1 = '/home/jack/Desktop/Imagedata/0-original-images/07082orig.jpg' 
outfile_png = '/home/jack/Desktop/dockercommands/images/useresult.png'
outlineJ(filename1,outfile_jpg)
outlineP(filename1,outfile_png)

"""
from PIL import Image
import numpy as np
import cv2
import imageio
from FileNameP import FilenameByTime
from pathlib import Path as change_ext
#p = change_ext('mysequence.jpg')
#p.rename(p.with_suffix('.png'))

def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    # return the edged image
    return edged

#image = cv2.imread('mahotastest/orig-color.png')
def change_extension(orig_file,new_extension):
    p = change_ext(orig_file)
    new_name = p.rename(p.with_suffix(new_extension))
    return new_name
    
def outlineJ(filename1,outfile_jpg):
    image = cv2.imread(filename1)
    edged = auto_canny(image, sigma=0.33)
    inverted = cv2.bitwise_not(edged)
    cv2.imwrite("mahotastest/temp2.png", inverted)
    cv2.imwrite(FilenameByTime("mahotastest/"), inverted)
    # Open Front Image
    #frontimage = Image.open('mahotastest/inverted-bitwise-note3_6.png').convert("1")
    frontimage = Image.open('mahotastest/temp2.png').convert("1")
    frontImage = frontimage.convert("RGBA")
    datas = frontImage.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    frontImage.putdata(newData)
    # Open Background Image
    background = Image.open(filename1)
    # Calculate width to be at the center
    width = (frontimage.width - frontimage.width) // 2
    # Calculate height to be at the center
    height = (frontimage.height - frontimage.height) // 2
    # Paste the frontImage at (width, height)
    background.paste(frontImage, (width, height), frontImage)
    # Save this image
    background.save(outfile_jpg, format="jpg")
    savefile = FilenameByTime("mahotastest/")
    background.save(savefile, format="jpg")
    #background = background.convert("RGB")
    return background
def outlineP(filename1,outfile_png):
    image = cv2.imread(filename1)
    edged = auto_canny(image, sigma=0.33)
    inverted = cv2.bitwise_not(edged)
    cv2.imwrite("mahotastest/temp2.png", inverted)
    cv2.imwrite(FilenameByTime("mahotastest/"), inverted)
    # Open Front Image
    #frontimage = Image.open('mahotastest/inverted-bitwise-note3_6.png').convert("1")
    frontimage = Image.open('mahotastest/temp2.png').convert("1")
    frontImage = frontimage.convert("RGBA")
    datas = frontImage.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    frontImage.putdata(newData)
    # Open Background Image
    background = Image.open(filename1)
    # Calculate width to be at the center
    width = (frontimage.width - frontimage.width) // 2
    # Calculate height to be at the center
    height = (frontimage.height - frontimage.height) // 2
    # Paste the frontImage at (width, height)
    background.paste(frontImage, (width, height), frontImage)
    # Save this image
    background.save(outfile_png, format="png")
    savefile = FilenameByTime("mahotastest/")
    background.save(savefile, format="png")
    #background = background.convert("RGB")
    return background

!ls junk

from OutlineImage import *
orig_file = "junk/00000.jpg"
new_extension = ".jnk"
NEW = change_extension(orig_file,new_extension)
print(NEW)

import OutlineImage
import cv2
filename1 = '/home/jack/Documents/FezEqP0XEAE4JdSl.jpg'
image = cv2.imread(filename1)
imout = OutlineImage.auto_canny(image)
cv2.imwrite('/home/jack/Documents/XXFezEqP0XEAE4JdSl.jpg', imout)

from OutlineImage import outlineP
#filename1 = '/home/jack/Desktop/Imagedata/textured-images/RANDOM-smoothness25.91-threshhold4_20220922230108.jpg' 
filename1 = '/home/jack/Documents/FezEqP0XEAE4JdSl.jpg'
outfileP = '/home/jack/Desktop/dockercommands/images/useresult25.png'
outlineP(filename1,outfileP)

from PIL import Image
im = Image.open(outfileP)
im

from PIL import Image
im = Image.open(savefile)
im

from PIL import Image
im = Image.open(filename1)
im




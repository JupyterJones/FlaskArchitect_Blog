!ls

imagedir = open("images.list", "r")
IMAGES =[]
for images in imagedir:
    if "docker" not in images:
        images = images.replace("\n","")
        IMAGES.append(images)


print ( len(IMAGES))

from random import randint
rnd = randint(0, len(IMAGES))
print(IMAGES[rnd])

!mkdir image_resources

import PIL

from PIL import Image

cnt = 0
for i in range(30):
    cnt =cnt+1
    rnd = randint(0, len(IMAGES))
    im = Image.open(IMAGES[rnd])
    newsize = (720, 480)
    im1 = im.resize(newsize)
    im1.save("image_resources/00"+str(cnt)+".jpg")

!mkdir blacknwhite_resources

import cv2
cnt = 0
for i in range(30):
    cnt = cnt +1
    rnd = randint(0, len(IMAGES))
    #im = Image.open(IMAGES[rnd])
    originalImage = cv2.imread(IMAGES[rnd])
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow('Black white image', blackAndWhiteImage)
    cv2.imwrite(filename, img)

  
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2



from PIL import Image
from scipy.misc import imsave
import numpy


def binarize_image(img_path, target_path, threshold):
    """Binarize an image."""
    image_file = Image.open(img_path)
    image = image_file.convert('L')  # convert image to monochrome
    image = numpy.array(image)
    image = binarize_array(image, threshold)
    imsave(target_path, image)


#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Binarize (make it black and white) an image with Python."""

from PIL import Image
from scipy.misc import imsave
import numpy


def binarize_image(img_path, target_path, threshold):
    """Binarize an image."""
    image_file = Image.open(img_path)
    image = image_file.convert('L')  # convert image to monochrome
    image = numpy.array(image)
    image = binarize_array(image, threshold)
    imsave(target_path, image)


def binarize_array(numpy_array, threshold=200):
    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
    return numpy_array


def get_parser():
    """Get parser object for script xy.py."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input",
                        dest="input",
                        help="read this file",
                        metavar="FILE",
                        required=True)
    parser.add_argument("-o", "--output",
                        dest="output",
                        help="write binarized file hre",
                        metavar="FILE",
                        required=True)
    parser.add_argument("--threshold",
                        dest="threshold",
                        default=200,
                        type=int,
                        help="Threshold when to show white")
    return parser


if __name__ == "__main__":
    args = get_parser().parse_args()
    binarize_image(args.input, args.output, args.threshold)


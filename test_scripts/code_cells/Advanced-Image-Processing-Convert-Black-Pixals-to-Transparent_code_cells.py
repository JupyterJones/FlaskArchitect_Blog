import numpy as np
import skimage.io
import skimage.viewer
import matplotlib.pyplot as plt
import ipympl

from skimage.io import imsave as saveitas

import skimage                 # form 1, load whole skimage library
import skimage.io              # form 2, load skimage.io module only
from skimage.io import imread  # form 3, load only the imread function
import numpy as np             # form 4, load all of numpy into an object called np
from skimage.io import imsave as saveit

%matplotlib widget
import mahotas

import mahotas
%matplotlib inline
import mahotas.demos
import numpy as np
from pylab import imshow, gray, show
from os import path

#photo = mahotas.imread('/home/jack/Desktop/dockercommands/images/useresult.png', as_grey=True)
photo = mahotas.imread('/home/jack/Desktop/dockercommands/images/useresult.png', as_grey=False)
photo = photo.astype(np.uint8)

#gray()
imshow(photo)
#show()
#photo

# importing required libraries
import numpy as np
import mahotas
from pylab import imshow, show

# loading image
img = mahotas.imread('/home/jack/Desktop/dockercommands/images/20221010-160527.jpg')

# showing the original image
imshow(img)
show()


!mkdir mahotastest

# input/Output with Mahotas

import mahotas as mh
image = mh.imread('file.png')
mh.imsave('copy.png', image)

#test-001
import cv2
import numpy as np
import imageio
image = cv2.imread('/home/jack/Desktop/dockercommands/AI/u-09294misc.jpg')
original = image.copy()
mask = np.zeros(image.shape, dtype=np.uint8)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=3)

cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
for c in cnts:
    cv2.drawContours(mask, [c], -1, (255,255,255), -1)
    break

close = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=4)
close = cv2.cvtColor(close, cv2.COLOR_BGR2GRAY)
result = cv2.bitwise_and(original, original, mask=close)
result[close==0] = (255,255,255)

img_uint8 = close.astype(np.uint8)
# and then
imageio.imwrite('mahotastest/test-001.jpg', img_uint8)

# importing required libraries
import numpy as np
import mahotas
from pylab import imshow, show

# loading image
#img = mahotas.imread('/home/jack/Desktop/dockercommands/AI/u-09294misc.jpg')
img = mahotas.imread('/home/jack/Desktop/dockercommands/styles/FeIdoA5VIAIuUFR.jpg')
	
# filtering the image
img = img[:, :, 0]
	
# setting gaussian filter
gaussian = mahotas.gaussian_filter(img, 15)

# setting threshold value
gaussian = (gaussian > gaussian.mean())

# creating a labeled image
labeled, n_nucleus = mahotas.label(gaussian)


print("Image")
# showing the gaussian filter
imshow(labeled)
show()


# getting distance map
dmap = mahotas.distance(labeled)

print("Distance Map")
imshow(dmap)
show()



import scipy.misc
#scipy.misc.imsave('mahotastest/001.png', dmap)
saveit('mahotastest/uUFR-1.jpg', dmap)

import numpy as np
import imageio

# suppose that img's dtype is 'float64'
img_uint8 = dmap.astype(np.uint8)
# and then
imageio.imwrite('mahotastest/uUFR-2.jpg', img_uint8)

!cp /home/jack/Desktop/dockercommands/AI/u-09294misc.jpg mahotastest
!cp /home/jack/Desktop/dockercommands/styles/FeIdoA5VIAIuUFR.jpg mahotastest

from PIL import Image
#filename = '/home/jack/Desktop/dockercommands/AI/u-09294misc.jpg'
filename = '/home/jack/Desktop/dockercommands/styles/FeIdoA5VIAIuUFR.jpg'
img = Image.open(filename)
img

# Turn an image upside down and backwords
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
filename = '/home/jack/Desktop/dockercommands/styles/FeIdoA5VIAIuUFR.jpg'
img = mpimg.imread(filename)
plt.imsave("mahotastest/upsidedown-uUFR-2.jpg", img, cmap = 'gray', origin = 'lower')

img_usd = Image.open("mahotastest/upsidedown-uUFR-2.jpg")
img_usd

import numpy
import matplotlib
from matplotlib import pylab, mlab, pyplot
np = numpy
plt = pyplot

from IPython.display import display
from IPython.core.pylabtools import figsize, getfigs

from pylab import *
from numpy import *

# load the image
filename = '/home/jack/Desktop/dockercommands/styles/FeIdoA5VIAIuUFR.jpg'
image = skimage.io.imread(filename)

fig, ax = plt.subplots()
plt.imshow(image)

import numpy as np
import glob
import matplotlib.pyplot as plt
import skimage.io
import skimage.color
import skimage.filters
%matplotlib inline

# load the image
filename = '/home/jack/Desktop/dockercommands/styles/FeIdoA5VIAIuUFR.jpg'
image = skimage.io.imread(filename)

fig, ax = plt.subplots()
plt.imsave("mahotastest/black-2.jpg", image, cmap = 'gray', origin = 'lower')
plt.imshow(image)

# convert the image to grayscale

filename = "mahotastest/black-2.jpg"
image = skimage.io.imread(filename)
gray_image = skimage.color.rgb2gray(image)

# blur the image to denoise
blurred_image = skimage.filters.gaussian(gray_image, sigma = 1.0)

fig, ax = plt.subplots()
plt.imshow(blurred_image, cmap = "gray")

import cv2
import numpy as np

# Load image as Numpy array in BGR order
na = cv2.imread('I5jKW.png')

# Make a True/False mask of pixels whose BGR values sum to more than zero
alpha = np.sum(na, axis=-1) > 0

# Convert True/False to 0/255 and change type to "uint8" to match "na"
alpha = np.uint8(alpha * 255)

# Stack new alpha layer with existing image to go from BGR to BGRA, i.e. 3 channels to 4 channels
res = np.dstack((na, alpha))

# Save result
cv2.imwrite('result.png', res)

# create a histogram of the blurred grayscale image
histogram, bin_edges = np.histogram(blurred_image, bins = 256, range = (0.0, 1.0))

fig, ax = plt.subplots()
plt.plot(bin_edges[0: -1], histogram)
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim(0, 1.0)

# create a mask based on the threshold
t = 0.8
binary_mask = blurred_image < t

fig, ax = plt.subplots()
plt.imshow(binary_mask, cmap = "gray")

from skimage.io import imsave as saveitas
# use the binary_mask to select the "interesting" part of the image
selection = image.copy()
selection[~binary_mask] = 0

fig, ax = plt.subplots()
saveitas('mahotastest/selection-uUFR-1.jpg', selection)
plt.imshow(selection)

gray_image = skimage.io.imread(filename, as_gray = True)
histogram, bin_edges = np.histogram(gray_image, bins = 256, range = (0.0, 1.0))

fig, ax = plt.subplots()
plt.plot(bin_edges[0: -1], histogram)
plt.title("Graylevel histogram")
plt.xlabel("gray value")
plt.ylabel("pixel count")
plt.xlim(0, 1.0)

# Works Great !
import cv2
import numpy as np
import matplotlib.image
# Load image as Numpy array in BGR order
na = cv2.imread('mahotastest/selection-uUFR-1.jpg')

# Make a True/False mask of pixels whose BGR values sum to more than zero
alpha = np.sum(na, axis=-1) > 0

# Convert True/False to 0/255 and change type to "uint8" to match "na"
#alpha = np.uint8(alpha * 255)
#alpha = np.uint8(alpha * 200)
alpha = np.uint8(alpha * 100)
# Stack new alpha layer with existing image to go from BGR to BGRA, i.e. 3 channels to 4 channels
res = np.dstack((na, alpha))


matplotlib.image.imsave('mahotastest/matplotlib-name100.png', res)

# Save result
cv2.imwrite('mahotastest/selection-uUFR-1-jpg-alpha100.png', res)

#test-2 Not Good Only for a bad mask
import cv2
import numpy as np

# load image
img = cv2.imread('mahotastest/selection-uUFR-1.jpg')

# threshold on black to make a mask
color = (0,0,0)
mask = np.where((img==color).all(axis=2), 0, 255).astype(np.uint8)

# put mask into alpha channel
result = img.copy()
result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
result[:, :, 3] = mask

# save resulting masked image
cv2.imwrite('mahotastest/selection-tranaparent-test-2.jpg', result)
cv2.imwrite('mahotastest/selection-tranaparent-mask-test-2.jpg', mask)
# display result, though it won't show transparency


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import mahotas as mh
filename = '/home/jack/Desktop/dockercommands/styles/FeIdoA5VIAIuUFR.jpg'
img = mpimg.imread(filename)
feId = mh.colors.rgb2grey(img)
imshow(feId)

import numpy as np
import glob
import matplotlib.pyplot as plt
import skimage.io
import skimage.color
import skimage.filters %
   matplotlib widget

# load the image
image = skimage.io.imread("data/shapes-01.jpg")

fig, ax = plt.subplots()
plt.imshow(image)

import matplotlib
matplotlib.__version__

pylab.cumsum?

Signature: pylab.cumsum(a, axis=None, dtype=None, out=None)
Docstring:
Return the cumulative sum of the elements along a given axis.

Parameters
----------
a : array_like
    Input array.
axis : int, optional
    Axis along which the cumulative sum is computed. The default
    (None) is to compute the cumsum over the flattened array.
dtype : dtype, optional
    Type of the returned array and of the accumulator in which the
    elements are summed.  If `dtype` is not specified, it defaults
    to the dtype of `a`, unless `a` has an integer dtype with a
    precision less than that of the default platform integer.  In
    that case, the default platform integer is used.
out : ndarray, optional
    Alternative output array in which to place the result. It must
    have the same shape and buffer length as the expected output
    but the type will be cast if necessary. See :ref:`ufuncs-output-type` for
    more details.

Returns
-------
cumsum_along_axis : ndarray.
    A new array holding the result is returned unless `out` is
    specified, in which case a reference to `out` is returned. The
    result has the same size as `a`, and the same shape as `a` if
    `axis` is not None or `a` is a 1-d array.

See Also
--------
sum : Sum array elements.
trapz : Integration of array values using the composite trapezoidal rule.
diff : Calculate the n-th discrete difference along given axis.

Notes
-----
Arithmetic is modular when using integer types, and no error is
raised on overflow.

``cumsum(a)[-1]`` may not be equal to ``sum(a)`` for floating-point
values since ``sum`` may use a pairwise summation routine, reducing
the roundoff-error. See `sum` for more information.

Examples
--------
>>> a = np.array([[1,2,3], [4,5,6]])
>>> a
array([[1, 2, 3],
       [4, 5, 6]])
>>> np.cumsum(a)
array([ 1,  3,  6, 10, 15, 21])
>>> np.cumsum(a, dtype=float)     # specifies type of output value(s)
array([  1.,   3.,   6.,  10.,  15.,  21.])

>>> np.cumsum(a,axis=0)      # sum over rows for each of the 3 columns
array([[1, 2, 3],
       [5, 7, 9]])
>>> np.cumsum(a,axis=1)      # sum over columns for each of the 2 rows
array([[ 1,  3,  6],
       [ 4,  9, 15]])

``cumsum(b)[-1]`` may not be equal to ``sum(b)``

>>> b = np.array([1, 2e-9, 3e-9] * 1000000)
>>> b.cumsum()[-1]
1000000.0050045159
>>> b.sum()
1000000.0050000029
File:      ~/miniconda3/envs/cloned_base/lib/python3.9/site-packages/numpy/core/fromnumeric.py
Type:      function


import pylab
import scipy
p=set(dir(pylab))
s=set(dir(scipy))
k=p.intersection(s)
conflicts = [f for f in k if getattr(scipy, f) is not getattr(pylab, f)]
import matplotlib
matplotlib.__version__
conflicts
results:
['cumsum', 'ptp', 'fix', 'ravel', '__file__', 'ones', 'rank', 'tri',
 'insert', 'arange', 'indices', 'loads', 'where', 'mean', 'argmax', 'nonzero',
 'asarray', 'sum', 'polyfit', 'prod', 'log2', 'power', 'cumproduct', 'corrcoef',
 'meshgrid', '__name__', 'cov', 'cumprod', 'vander', 'arccos', 'load', 'array',
 'iterable', 'eye', 'log', 'sometrue', 'alltrue', 'zeros', 'log10', '__doc__',
 'empty', 'polyval', 'arcsin', 'arctanh', 'linspace', 'typecodes', 'copy',
 'std', 'fromfunction', 'argmin', 'trapz', 'binary_repr', 'sqrt', 'take',
 'product', 'repeat', 'trace', 'compress', 'array2string', 'amax', 'identity',
 'amin', 'fromstring', 'average', 'base_repr', 'reshape']    

numpy.cumsum?
conflicts

pylab.cumsum?

result:
Signature: pylab.cumsum(a, axis=None, dtype=None, out=None)
Docstring:
Return the cumulative sum of the elements along a given axis.

Parameters
----------
a : array_like
    Input array.
axis : int, optional
    Axis along which the cumulative sum is computed. The default
    (None) is to compute the cumsum over the flattened array.
dtype : dtype, optional
    Type of the returned array and of the accumulator in which the
    elements are summed.  If `dtype` is not specified, it defaults
    to the dtype of `a`, unless `a` has an integer dtype with a
    precision less than that of the default platform integer.  In
    that case, the default platform integer is used.
out : ndarray, optional
    Alternative output array in which to place the result. It must
    have the same shape and buffer length as the expected output
    but the type will be cast if necessary. See :ref:`ufuncs-output-type` for
    more details.

Returns
-------
cumsum_along_axis : ndarray.
    A new array holding the result is returned unless `out` is
    specified, in which case a reference to `out` is returned. The
    result has the same size as `a`, and the same shape as `a` if
    `axis` is not None or `a` is a 1-d array.

See Also
--------
sum : Sum array elements.
trapz : Integration of array values using the composite trapezoidal rule.
diff : Calculate the n-th discrete difference along given axis.

Notes
-----
Arithmetic is modular when using integer types, and no error is
raised on overflow.

``cumsum(a)[-1]`` may not be equal to ``sum(a)`` for floating-point
values since ``sum`` may use a pairwise summation routine, reducing
the roundoff-error. See `sum` for more information.

Examples
--------
>>> a = np.array([[1,2,3], [4,5,6]])
>>> a
array([[1, 2, 3],
       [4, 5, 6]])
>>> np.cumsum(a)
array([ 1,  3,  6, 10, 15, 21])
>>> np.cumsum(a, dtype=float)     # specifies type of output value(s)
array([  1.,   3.,   6.,  10.,  15.,  21.])

>>> np.cumsum(a,axis=0)      # sum over rows for each of the 3 columns
array([[1, 2, 3],
       [5, 7, 9]])
>>> np.cumsum(a,axis=1)      # sum over columns for each of the 2 rows
array([[ 1,  3,  6],
       [ 4,  9, 15]])

``cumsum(b)[-1]`` may not be equal to ``sum(b)``

>>> b = np.array([1, 2e-9, 3e-9] * 1000000)
>>> b.cumsum()[-1]
1000000.0050045159
>>> b.sum()
1000000.0050000029
File:      ~/miniconda3/envs/cloned_base/lib/python3.9/site-packages/numpy/core/fromnumeric.py
Type:      function
    
    













import twython
from twython import Twython
from APIkey import APIkey
CONSUMER_KEY = APIkey()[0]
CONSUMER_SECRET = APIkey()[1]
ACCESS_KEY = APIkey()[2]
ACCESS_SECRET = APIkey()[3]

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

def post(message):
    #twitter.update_status(status='See how easy using Twython is!')
    twitter.update_status(status=message)#, in_reply_to_status_id=twitter_id)

STR ="""
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
# apply Canny edge detection using a wide threshold, tight
# threshold, and automatically determined threshold
wide = cv2.Canny(blurred, 10, 200)
cv2.imwrite("mahotastest/wide.jpg", wide)
"""
message = STR
print(len(message))


post(message)

from twython import Twython
from APIkey import APIkey
CONSUMER_KEY = APIkey()[0]
CONSUMER_SECRET = APIkey()[1]
ACCESS_KEY = APIkey()[2]
ACCESS_SECRET = APIkey()[3]

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
STR ="""
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
# apply Canny edge detection using a wide threshold, tight
# threshold, and automatically determined threshold
wide = cv2.Canny(blurred, 10, 200)
cv2.imwrite("mahotastest/wide.jpg", wide)
"""
message = STR
photo = open('/home/jack/Desktop/dockercommands/mahotastest/wide-inverted.jpg', 'rb')
response = twitter.upload_media(media = photo)
twitter.update_status(status = STR, media_ids = [response['media_id']])

from twython
import Twython
twitter = Twython(APP_KEY, APP_SECRET,
   OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

photo = open('/path/to/file/image.jpg', 'rb')
response = twitter.upload_media(media = photo)
twitter.update_status(status = 'Checkout this cool image!', media_ids = [response['media_id']])

video = open('/path/to/file/video.mp4', 'rb')
response = twitter.upload_video(media = video, media_type = 'video/mp4')
twitter.update_status(status = 'Checkout this cool video!', media_ids = [response['media_id']])

response = twitter.upload_media(media=photo)
twitter.update_status(status=STRu, media_ids=[response['media_id']])

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
filename1 = '/home/jack/Desktop/dockercommands/images/useresult.png'
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
background.save(FilenameByTime("mahotastest/"), format="png")
#background = background.convert("RGB")




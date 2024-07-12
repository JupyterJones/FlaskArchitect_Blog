!sudo locate slicPython

!du -hs /home/conda/Desktop/NoteBooks/GRAPHICS/superpixels/slicPython

!ls

from IPython.core.display import HTML
HTML("""
<style>
#notebook-container {
    padding: 15px;
    background-color: #ffebcd;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.3);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.3);
}
</style>
""")

import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io

%pylab inline
%matplotlib inline 


!wget https://jacknorthrup.com/INSTAGRAM/003.jpg

img = img_as_float(io.imread('003.jpg'))
io.imshow(img);

for segs in (10, 50, 100, 300, 500, 1000):
    segments = slic(img, n_segments = segs, sigma = 4)
    fig = plt.figure(figsize=(12,4), dpi=300)
    #ax = fig.add_axes([0, 0, 1, 1])
    plt.tick_params(axis='x',which='both',bottom='off',top='off',labelbottom='off') 
    #plt.tick_params(axis='Y',which='both',bottom='off',top='off',labelbottom='off') 
    imshow(mark_boundaries(img, segments, (0,0,0)))
plt.show()

for segs in (10, 50, 100, 300, 500, 1000):
    segments = slic(img, n_segments = segs, sigma = 4)
    fig = plt.figure(figsize=(12,4), dpi=300)
    #ax = fig.add_axes([0, 0, 1, 1])
    plt.tick_params(axis='x',which='both',bottom='off',top='off',labelbottom='off') 
    #plt.tick_params(axis='Y',which='both',bottom='off',top='off',labelbottom='off') 
    imshow(mark_boundaries(img, segments, (0,0,0)))
plt.show()


from __future__ import print_function

import matplotlib.pyplot as plt
import numpy as np

from skimage.data import astronaut
from skimage.segmentation import felzenszwalb, slic, quickshift
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float

segments_fz = felzenszwalb(img, scale=100, sigma=0.5, min_size=50)
segments_slic = slic(img, n_segments=250, compactness=10, sigma=1)
segments_quick = quickshift(img, kernel_size=3, max_dist=6, ratio=0.5)

print("Felzenszwalb's number of segments: %d" % len(np.unique(segments_fz)))
print("Slic number of segments: %d" % len(np.unique(segments_slic)))
print("Quickshift number of segments: %d" % len(np.unique(segments_quick)))

fig, ax = plt.subplots(1, 3)
fig.set_size_inches(16, 8, forward=True)
fig.subplots_adjust(0.05, 0.05, 0.95, 0.95, 0.05, 0.05)

ax[0].imshow(mark_boundaries(img, segments_fz))
ax[0].set_title("Felzenszwalbs's method")
ax[1].imshow(mark_boundaries(img, segments_slic))
ax[1].set_title("SLIC")
ax[2].imshow(mark_boundaries(img, segments_quick))
ax[2].set_title("Quickshift")
for a in ax:
    a.set_xticks(())
    a.set_yticks(())
plt.show()

import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io

%pylab inline
%matplotlib inline 
img = img_as_float(io.imread('003.jpg'))
#io.imshow(img);
for segs in (10, 50, 100, 300, 500, 1000):
    segments = slic(img, n_segments = segs, sigma = 4)
    fig = plt.figure(figsize=(12,4), dpi=200)
    #ax = fig.add_axes([0, 0, 1, 1])
    plt.tick_params(axis='x',which='both',bottom='off',top='off',labelbottom='off') 
    #plt.tick_params(axis='Y',which='both',bottom='off',top='off',labelbottom='off') 
    imshow(mark_boundaries(img, segments, (0,0,0)))
plt.show()

from PIL import Image
img = Image.open("images/coffee002.png") 
img = img.convert("RGB")
img.save("images/coffee002.jpg")

import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io
from PIL import Image
%pylab inline
%matplotlib inline 
def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

img = Image.open("images/coffee002.jpg")    
img = img.convert('P', palette=Image.ADAPTIVE, colors=36)    
img.save("003a.png")    
   
img = img_as_float(io.imread('003a.png'))



#io.imshow(img);
segs = 360
segments = slic(img, n_segments = segs, sigma = 4)
fig = plt.figure(figsize=(12,4), dpi=200)
#ax = fig.add_axes([0, 0, 1, 1])
#plt.tick_params(axis='x',which='both',bottom='off',top='off',labelbottom='off') 
#plt.tick_params(axis='Y',which='both',bottom='off',top='off',labelbottom='off') 
plt.axis('off')
imshow(mark_boundaries(img, segments, (0,0,0)))
plt.savefig("test2.png", bbox_inches='tight')
im = Image.open("test2.png")
im = trim(im)
im.resize((640,640), Image.NEAREST)
im = im.convert("RGB")
im.save('coffee002.jpg')
im.show()

import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io
from PIL import Image
%pylab inline
%matplotlib inline 
def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

img = Image.open("003.jpg")    
img = img.convert('P', palette=Image.ADAPTIVE, colors=36)    
img.save("003a.png")    
   
img = img_as_float(io.imread('003a.png'))



#io.imshow(img);
segs = 360
segments = slic(img, n_segments = segs, sigma = 4)
fig = plt.figure(figsize=(12,4), dpi=200)
#ax = fig.add_axes([0, 0, 1, 1])
#plt.tick_params(axis='x',which='both',bottom='off',top='off',labelbottom='off') 
#plt.tick_params(axis='Y',which='both',bottom='off',top='off',labelbottom='off') 
plt.axis('off')
imshow(mark_boundaries(img, segments, (0,0,0)))
plt.savefig("test2.png", bbox_inches='tight')
im = Image.open("test2.png")
im = trim(im)
im.resize((640,640), Image.NEAREST)
im = im.convert("RGB")
im.save('test2.jpg')
im.show()



import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io
from PIL import Image
%pylab inline
%matplotlib inline 
def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    
img = img_as_float(io.imread('003.jpg'))
#io.imshow(img);
segs = 1000
segments = slic(img, n_segments = segs, sigma = 4)
fig = plt.figure(figsize=(12,4), dpi=200)
#ax = fig.add_axes([0, 0, 1, 1])
#plt.tick_params(axis='x',which='both',bottom='off',top='off',labelbottom='off') 
#plt.tick_params(axis='Y',which='both',bottom='off',top='off',labelbottom='off') 
plt.axis('off')
imshow(mark_boundaries(img, segments, (0,0,0)))
plt.savefig("test2.png", bbox_inches='tight')
im = Image.open("test2.png")
im = trim(im)
im.resize((640,640), Image.NEAREST)
im = im.convert("RGB")
im.save('test2.jpg')
im.show()

from PIL import Image
im=Image.open("test2.png")
im

from PIL import Image
im=Image.open("test2.png")
im.size
im.getbbox()
im2=im.crop(im.getbbox())
im2.size


from PIL import Image, ImageChops

def trim(im, border):
    bg = Image.new(im.mode, im.size, border)
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

def create_thumbnail(path, xsize,ysize):
    image = Image.open(path)
    name, extension = path.split('.')
    options = {}
    if 'transparency' in image.info:
        options['transparency'] = image.info["transparency"]
  
    image.thumbnail((xsize, ysize), Image.ANTIALIAS)
    image = trim(image, 255) ## Trim whitespace
    image.save(name + '_new.' + extension, **options)
    return image


create_thumbnail('test2.png', 640, 640)

!ls *.png

from PIL import Image, ImageChops

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

im = Image.open("coffee002.jpg")
im = trim(im)
im = im.resize((640,640), Image.NEAREST)
im.show()


image_data_bw = image_data[:,:,3]


from numpy import random
import matplotlib.pyplot as plt

data = random.random((5,5))
img = plt.imshow(data, interpolation='nearest')
img.set_cmap('hot')
plt.axis('off')
plt.savefig("test.png", bbox_inches='tight')

import matplotlib.pyplot as plt
import numpy as np
%pylab inline
%matplotlib inline 

ncols = 5
nrows = 3

# create the plots
fig = plt.figure()
axes = [ fig.add_subplot(nrows, ncols, r * ncols + c) for r in range(1, nrows) for c in range(1, ncols) ]

# add some data
for ax in axes:
    ax.plot(np.random.random(10), np.random.random(10), '.')

# remove the x and y ticks
for ax in axes:
    ax.set_xticks([])
    ax.set_yticks([])

def autocrop_image2(image):
    image_data = np.asarray(image)
    image_data_bw = image_data[:,:,3]
    non_empty_columns = np.where(image_data_bw.max(axis=0) > 0)[0]
    non_empty_rows = np.where(image_data_bw.max(axis=1) > 0)[0]
    cropBox = (min(non_empty_rows), max(non_empty_rows),
               min(non_empty_columns), max(non_empty_columns))

    image_data_new = image_data[cropBox[0]:cropBox[
        1] + 1, cropBox[2]:cropBox[3] + 1, :]

    new_image = Image.fromarray(image_data_new)
    return new_image

from PIL import Image
im=Image.open("test2.png")
bbox = im.convert("RGBa").getbbox()
im0 = autocrop_image2(bbox)
im0

!locate override.css



im=Image.open("test2.png")
bbox = im.convert("RGBA")
bbox

from PIL import Image
import numpy as np
def autocrop_image2(image):
    #image.load()
    image_data = np.asarray(image)
    image_data_bw = image_data.max(axis=2)
    non_empty_columns = np.where(image_data_bw.max(axis=0) > 0)[0]
    non_empty_rows = np.where(image_data_bw.max(axis=1) > 0)[0]
    cropBox = (min(non_empty_rows), max(non_empty_rows),
               min(non_empty_columns), max(non_empty_columns))

    image_data_new = image_data[cropBox[0]:cropBox[
        1] + 1, cropBox[2]:cropBox[3] + 1, :]

    new_image = Image.fromarray(image_data_new)
    return new_image
im=Image.open("test2.png")
bbox = im.convert("RGBA").getbbox()
im0 = autocrop_image2(bbox)
im0

# import the necessary packages
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import cv2
def clust(IMAGE):
    # construct the argument parser and parse the arguments
    # load the image and convert it from BGR to RGB so that
    # we can dispaly it with matplotlib
    image = cv2.imread(IMAGE)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # show our image
    return image
    
IMAGE = "test2.png"    
im = clust(IMAGE)

cv2.imwrite("NEWim.png", im)

from PIL import Image
imN= Image.open("NEWim.png")
imN

import markdown
class MD(str):
    def _repr_html_(self):
        return markdown.markdown(self)
    
STR="""
<div style ="border:1px solid red;padding:15px;">    
<h3>Help on function mark_boundaries in module skimage.segmentation.boundaries:</h3>

<p style = "color:blue">mark_boundaries(image, label_img, color=(1, 1, 0), outline_color=None, mode='outer', background_label=0)
Return image with boundaries between labeled regions highlighted.</p>
Parameters
----------<pre>
    image : (M, N[, 3]) array
        Grayscale or RGB image.
    label_img : (M, N) array of int
        Label array where regions are marked by different integer values.
    color : length-3 sequence, optional
        RGB color of boundaries in the output image.
    outline_color : length-3 sequence, optional
        RGB color surrounding boundaries in the output image. If None, no
        outline is drawn.
    mode : string in {'thick', 'inner', 'outer', 'subpixel'}, optional
        The mode for finding boundaries.
    background_label : int, optional
        Which label to consider background (this is only useful for
        modes ``inner`` and ``outer``).
</pre>    
Returns
-------
    marked : (M, N, 3) array of float
        An image in which the boundaries between labels are
        superimposed on the original image.
</div>
"""
MD(STR)    

!ls ~/.jupyter/custom

# %load ~/.jupyter/custom/current_theme.txt
monokai

!python color_kmeans.py --image 003.jpg --clusters 3

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import numpy as np
import cv2
%pylab inline
%matplotlib inline 
def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins = numLabels)

    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()

    # return the histogram
    return hist

def plot_colors(hist, centroids):
    # initialize the bar chart representing the relative frequency
    # of each of the colors
    bar = np.zeros((50, 300, 3), dtype = "uint8")
    startX = 0

    # loop over the percentage of each cluster and the color of
    # each cluster
    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
            color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar

def Clust(iMage, clusters):
    # load the image and convert it from BGR to RGB so that
    # we can dispaly it with matplotlib
    image = cv2.imread(iMage)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # show our image
    plt.figure()
    plt.axis("off")
    plt.imshow(image)

    # reshape the image to be a list of pixels
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    # cluster the pixel intensities
    clt = KMeans(clusters)
    clt.fit(image)

    # build a histogram of clusters and then create a figure
    # representing the number of pixels labeled to each color
    hist = utilz.centroid_histogram(clt)
    bar = utilz.plot_colors(hist, clt.cluster_centers_)

    # show our color bart
    plt.figure()
    plt.axis("off")
    plt.imshow(bar)
    plt.show()

iMage = "003.jpg"
clusters = 6
Clust(iMage, clusters)    

%%writefile utilz.py
# import the necessary packages
import numpy as np
import cv2

def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins = numLabels)

    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()

    # return the histogram
    return hist

def plot_colors(hist, centroids):
    # initialize the bar chart representing the relative frequency
    # of each of the colors
    bar = np.zeros((50, 300, 3), dtype = "uint8")
    startX = 0

    # loop over the percentage of each cluster and the color of
    # each cluster
    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
            color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar

import time
from matplotlib import pyplot as plt
from skimage import future
from skimage import data, segmentation, filters, color, io
from skimage.future import graph
from matplotlib import pyplot as plt

img = io.imread("test2.jpg")
labels = segmentation.slic(img, compactness=30, n_segments=400)
g = future.graph.rag_mean_color(img, labels)
def weight_boundary(graph, src, dst, n):
    default = {'weight': 0.0, 'count': 0}
    count_src = graph[src].get(n, default)['count']
    count_dst = graph[dst].get(n, default)['count']
    weight_src = graph[src].get(n, default)['weight']
    weight_dst = graph[dst].get(n, default)['weight']
    count = count_src + count_dst
    return {
        'count': count,
        'weight': (count_src * weight_src + count_dst * weight_dst)/count
    }
def merge_boundary(graph, src, dst):
    """Call back called before merging 2 nodes.
    In this case we don't need to do any computation here.""" 
    pass

labels2 = future.graph.merge_hierarchical(labels, g, thresh=0.08, rag_copy=False,
                                   in_place_merge=True,
                                   merge_func=merge_boundary,
                                   weight_func=weight_boundary)

#graph.show_rag(labels, g, img)
#plt.title('RAG after hierarchical merging')
plt.figure(dpi=200)
out = color.label2rgb(labels2, img, kind='avg')
plt.axis("off")
plt.imshow(out)
io.imsave("Stest2.png", out)
#plt.title('Final segmentation')

plt.show()    
    

!showme Stest2.png

import time
from matplotlib import pyplot as plt
from skimage import future
from skimage import data, segmentation, filters, color
from skimage import graph, data, io
from skimage.future import graph
from matplotlib import pyplot as plt
from PIL import Image, ImageChops

img = io.imread("test2.jpg")
labels = segmentation.slic(img, compactness=30, n_segments=400)
g = future.graph.rag_mean_color(img, labels)
def weight_boundary(graph, src, dst, n):
    default = {'weight': 0.0, 'count': 0}
    count_src = graph[src].get(n, default)['count']
    count_dst = graph[dst].get(n, default)['count']
    weight_src = graph[src].get(n, default)['weight']
    weight_dst = graph[dst].get(n, default)['weight']
    count = count_src + count_dst
    return {
        'count': count,
        'weight': (count_src * weight_src + count_dst * weight_dst)/count
    }
def merge_boundary(graph, src, dst):
    """Call back called before merging 2 nodes.
    In this case we don't need to do any computation here.""" 
    pass

labels2 = future.graph.merge_hierarchical(labels, g, thresh=0.08, rag_copy=False,
                                   in_place_merge=True,
                                   merge_func=merge_boundary,
                                   weight_func=weight_boundary)

#graph.show_rag(labels, g, img)
#plt.title('RAG after hierarchical merging')
plt.figure(dpi=200)
out = color.label2rgb(labels2, img, kind='avg')
plt.axis("off")
io.imsave("Stest2.png", out)
IMG =Image.open("Stest2.png")
IMG

import time
from matplotlib import pyplot as plt
from skimage import future
from skimage import data, segmentation, filters, color
from skimage import graph, data, io
from skimage.future import graph
from matplotlib import pyplot as plt
from PIL import Image, ImageChops

img = io.imread("test2.jpg")
labels = segmentation.slic(img, compactness=30, n_segments=400)
g = future.graph.rag_mean_color(img, labels)
def weight_boundary(graph, src, dst, n):
    default = {'weight': 0.0, 'count': 0}
    count_src = graph[src].get(n, default)['count']
    count_dst = graph[dst].get(n, default)['count']
    weight_src = graph[src].get(n, default)['weight']
    weight_dst = graph[dst].get(n, default)['weight']
    count = count_src + count_dst
    return {
        'count': count,
        'weight': (count_src * weight_src + count_dst * weight_dst)/count
    }
def merge_boundary(graph, src, dst):
    """Call back called before merging 2 nodes.
    In this case we don't need to do any computation here.""" 
    pass

labels2 = future.graph.merge_hierarchical(labels, g, thresh=0.08, rag_copy=False,
                                   in_place_merge=True,
                                   merge_func=merge_boundary,
                                   weight_func=weight_boundary)

#graph.show_rag(labels, g, img)
#plt.title('RAG after hierarchical merging')
plt.figure(dpi=200)
out = color.label2rgb(labels2, img, kind='avg')
plt.axis("off")
io.imsave("Stest2.png", out)
IMG =Image.open("Stest2.png")
IMG

import time
from matplotlib import pyplot as plt
from skimage import future
from skimage import data, segmentation, filters, color
from skimage import graph, data, io
from skimage.future import graph
from matplotlib import pyplot as plt
from PIL import Image, ImageChops
def main(imgagefile):
    img = io.imread(imgagefile)
    labels = segmentation.slic(img, compactness=30, n_segments=400)
    g = future.graph.rag_mean_color(img, labels)
    def weight_boundary(graph, src, dst, n):
        default = {'weight': 0.0, 'count': 0}
        count_src = graph[src].get(n, default)['count']
        count_dst = graph[dst].get(n, default)['count']
        weight_src = graph[src].get(n, default)['weight']
        weight_dst = graph[dst].get(n, default)['weight']
        count = count_src + count_dst
        return {
            'count': count,
            'weight': (count_src * weight_src + count_dst * weight_dst)/count
        }
    def merge_boundary(graph, src, dst):
        """Call back called before merging 2 nodes.
        In this case we don't need to do any computation here.""" 
        pass

    labels2 = future.graph.merge_hierarchical(labels, g, thresh=0.08, rag_copy=False,
                                       in_place_merge=True,
                                       merge_func=merge_boundary,
                                       weight_func=weight_boundary)
    out = color.label2rgb(labels2, img, kind='avg')
    io.imsave("Stest2.png", out)
    IMG =Image.open("Stest2.png")
    IMG

im = trim(im)
im.resize((640,640), Image.NEAREST)
im = im.convert("RGB")
im.save('Stest2.jpg')
im.show()

plt.savefig("test2.png", bbox_inches='tight')
im = Image.open("test2.png")
im = trim(im)
im.resize((640,640), Image.NEAREST)
im = im.convert("RGB")
im.save('test2.jpg')
im.show()

from PIL import Image, ImageChops

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

im = Image.open("coffee002.jpg")
im = trim(im)
im = im.resize((640,640), Image.NEAREST)
im.show()

%%writefile utils.py
# import the necessary packages
import numpy as np
import cv2
 
def centroid_histogram(clt):
	# grab the number of different clusters and create a histogram
	# based on the number of pixels assigned to each cluster
	numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
	(hist, _) = np.histogram(clt.labels_, bins = numLabels)
 
	# normalize the histogram, such that it sums to one
	hist = hist.astype("float")
	hist /= hist.sum()
 
	# return the histogram
	return hist


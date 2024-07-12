# we will need a 'Dummy image' below in our code
!wget -O images/testimage.jpg https://upload.wikimedia.org/wikipedia/en/b/b0/Black_%26_White_Handshake_-_Still_from_the_film_Colour_Blind_%282009%29.JPG

# Check size of downloaded 'Dummy image'
from PIL import Image
im = Image.open('images/testimage.jpg')
im.size

# Resize that giant 'Dummy image'
from PIL import Image
im = Image.open('images/testimage.jpg')
w, h = im.size
newW = int(w/10)
newH = int(h/10)
smallim = im.resize((newW, newH), Image.NEAREST)
smallim.save("images/small_image.jpg")

# get the keycode for whatever letter is entered in the parentheses 
ord('r')

# get the key for whatever keycode is entered in the parentheses 
unichr(33)

import os
os.system('kbd_mode -s')

# This will test our s to " EXIT "
import sys
import cv2
img = cv2.imread('images/small_image.jpg') # load a dummy image
while(1):
    cv2.imshow('img',img)
    k = cv2.waitKey(0)
    if k==27:    # Esc key to stop
        break
    elif k==115:  # normally -1 returned,so don't print it
        print "s"
    else:
        print "Good Bye"
        cv2.destroyAllWindows() 
        sys.exit()
        

# Capture an image - not video - to work with
import sys
import cv2
from cv2 import *
# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    namedWindow("cam-test",WINDOW_AUTOSIZE)
    imshow("cam-test",img)
    
while(1):
    cv2.imshow('cam-test',img)
    k = cv2.waitKey(0)
    if k==115:  # print "s"
        destroyWindow("cam-test")
        cv2.imwrite("images/000000.jpg",img) #save image
        cam.release() 
        cv2.destroyAllWindows()
        
    if k==114:    
        s, img = cam.read()
    if k==27:    # Esc key to stop
        break
        cv2.destroyAllWindows()
    else:
        print "Good Bye"
        cv2.destroyAllWindows() 
        sys.exit()
        
cam.release() 
cv2.destroyAllWindows()       

!ls images/000000.jpg

from PIL import Image, ImageEnhance
ima = Image.open("images/000000.jpg")
ima

# Sharpen an image using PIL
#import modules
import sys  
import os
from PIL import Image, ImageEnhance

# Open image
ima = Image.open("images/000000.jpg")

# Create an enhancer object
enhancer = ImageEnhance.Sharpness(ima)

# Apply a level of enhancment
factor_rd = enhancer.enhance(2.8)

# Show results 'factor_rd'
factor_rd.show("ImageEnhance", factor_rd)

# Show original 'ima'
ima.show("Orig", ima)

# Save enhanced Image
factor_rd.save("images/ImageEnhance-webcam8-1.8.jpg")



#import modules
import sys  
import os
from PIL import Image, ImageEnhance

# Open image
ima = Image.open("images/000000.jpg")

# Create an enhancer object
enhancer = ImageEnhance.Sharpness(ima)

# Apply a level of enhancment
factor_rd = enhancer.enhance(2.8)

# Show results 'factor_rd'
factor_rd.show("ImageEnhance", factor_rd)

# Show original 'ima'
ima.show("Orig", ima)

# Save enhanced Image
factor_rd.save("images/ImageEnhance-webcam8-1.8.jpg")



# Put the enhance controls in a trackbar
import cv2
from matplotlib import pyplot as plt
import numpy as np

def nothing(x):
    pass
cv2.namedWindow('ImageEnhance', True)
im = cv2.imread('images/000000.jpg')

min_value = 0
max_value = 0

while(1):
    
    cv2.createTrackbar('min_value','ImageEnhance',0,5,nothing)
    cv2.createTrackbar('max_value','ImageEnhance',0,5,nothing)
    min_value = cv2.getTrackbarPos('min_value', 'ImageEnhance')
    max_value = cv2.getTrackbarPos('max_value', 'ImageEnhance')

    #canny_edge = cv2.Canny(img, min_value, max_value)
    a = -2
    c = 17
    # Create an enhancer object
    kernel = np.array([[a,a,a], [a,c,a], [a,a,a]])
    im = cv2.filter2D(im, -1, kernel)
    
    #enhancer = ImageEnhance.Sharpness(ima)

    # Apply a level of enhancment
    #factor_rd = enhancer.enhance(max_value*.1)

    # Show results 'factor_rd'
    cv2.imshow("ImageEnhance", im)
    print (min_value)
    if(cv2.waitKey(0) & 0xFF == ord('q')):
        break

#cap.release()
cv2.destroyAllWindows()


import cv2
import sys
im = cv2.imread('images/000000.jpg')

while(1):
    cv2.imshow("ImageEnhance", im)
    
    k = cv2.waitKey(0)
    if k==115:  # print "s"
        destroyWindow("cam-test")
        cv2.imwrite("images/000000.jpg",img) #save image
        cam.release() 
        cv2.destroyAllWindows()
        
    elif k==27:    # Esc key to stop
        break
        cv2.destroyAllWindows()
    else:
           print "Good Bye"
           
    sys.exit()
cv2.destroyAllWindows()       

from PIL import Image
me = Image.open('images/ImageEnhance-webcam8-1.8.jpg')
print me.size



from PIL import Image
me = Image.open('images/ImageEnhance-webcam8-1.8.jpg')
width, height = me.size
leftIn = 100
lefttop = 20
RightIn = width-leftIn
RightBottom = 460
imCrop = leftIn,lefttop,RightIn,RightBottom
#crop 
cropim = me.crop(imCrop)
#me.crop(ul, lr)
#me
print imCrop
cropim.save("images/webcam-crop.jpg")
cropim

# Check image size
from PIL import Image
iop = Image.open("images/webcam-crop.jpg")
print iop.size

from PIL import ImageOps
wboder = 5
ImageOps.expand(Image.open('images/webcam-crop.jpg'),border=wboder,fill='black').save('images/webcam-border.jpg')
view = Image.open('images/webcam-border.jpg')
#view.show("Orig", view)
view

!ls

# Apply Image Blur and Canny Edge
import cv2
from matplotlib import pyplot as plt
 
def nothing(x):
    pass
cv2.namedWindow('canny_edge', True)
img_noblur = cv2.imread('images/000000.jpg', 0)
img = cv2.blur(img_noblur, (7,7))
 
#canny_edge = cv2.Canny(img, 0, 0)
 
#cv2.imshow('image', img)
#cv2.imshow('canny_edge', canny_edge)
while(1):
    
    cv2.createTrackbar('min_value','canny_edge',0,500,nothing)
    cv2.createTrackbar('max_value','canny_edge',0,500,nothing)



    min_value = cv2.getTrackbarPos('min_value', 'canny_edge')
    max_value = cv2.getTrackbarPos('max_value', 'canny_edge')

    canny_edge = cv2.Canny(img, min_value, max_value)
    cv2.imshow('img', img)
    cv2.imshow('canny_edge', canny_edge)    

    #print ilowH, ilowS, ilowV
    if(cv2.waitKey(True) & 0xFF == ord('q')):
        break


cv2.destroyAllWindows()


import numpy as np
import cv2

image = cv2.imread("images/webcam-border.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Blur parameters must be an ODD number
# GaussianBlur removes the small artifacts
blur = cv2.GaussianBlur(gray,(11,11),0)

#circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 300, np.array([]), 10, 30, 60, 300)
#circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 300, np.array([]), 5, 5, 100, 100)
ret,thresh1 = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
edges = cv2.Canny(thresh1, 100,200)
imagem = cv2.bitwise_not(edges)

result = cv2.bitwise_and(image,image, mask=imagem)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 1)
        cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow("Blur", blur)
#cv2.imshow("Circled", circles)
cv2.imshow("Thresh", thresh1)
cv2.imshow("edges", edges)
cv2.imshow("imagem", imagem)
cv2.imshow("Original", image)
cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()



import numpy as np
import cv2

image = cv2.imread("images/webcam-border.png")
#image = cv2.imread("images/webcam-border.png", 0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#blur = cv2.GaussianBlur(gray,(9,9),0)

#circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 300, np.array([]), 10, 30, 60, 300)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 300, np.array([]), 5, 5, 100, 100)
ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
edges = cv2.Canny(thresh1, 100,200)
imagem = cv2.bitwise_not(edges)

res = cv2.bitwise_and(image,image, mask=imagem)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 1)
        cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)

#cv2.imshow("Circled", image)
#cv2.imshow("Thresh", thresh1)
#cv2.imshow("edges", edges)
cv2.imshow("imagem", imagem)
cv2.imshow("res", res)

cv2.waitKey(0)
cv2.destroyAllWindows()

from PIL import Image
import cv2
from cv2 import *
picture = Image.new( 'RGB', (150,150), "black")

# Get the size of the image
width, height = picture.size
# Get the size of the image
for x in range(0, width - 1):
     for y in range(0, height - 1):
        
        while (h<x):
            while (v <y):

                if (cx + cy < 100):
                    new_color = (0,0,255)
                    else:
                    new_color = (0,0,0) 
                    v=v+1
                    else:    
                    h=h+1
                    v=0        




                    picture.putpixel( (x,y), new_color)
                    picture.save("images/new_color-blackk.jpg")
                    #!showme images/new_color-face_300.jpg



from PIL import Image
import cv2
from cv2 import *
from math import cos
picture = Image.new( 'RGB', (200,200), "white")

c=10
# Get the size of the image
width, height = picture.size
fx = x-width*-1
fy = y-height*-1
# Get the size of the image
for x in range(0, width - 1):
     for y in range(0, height - 1):
        fx = x-width*-1
        fy = y-height*-1
        color = picture.getpixel((x, y))
        if (cos(x+y) <2):
            k = abs(cos(fx+fy)*fx)
            c = int(k)
            k1 = abs(fx**2-fy**2)
            c1 = int(k)
            #c = (abs(cos(fx)*fy**2*.01)
            new_color = (c,c1,0)
        else:
            new_color = (0,c1,c)
            
            print c,c1, cos(x+y)
            picture.putpixel( (x,y), new_color)
            picture.save("images/new_color-black4.jpg")
        
        
        

from PIL import Image, ImageOps
import cv2
from cv2 import *

picture = Image.new( 'RGB', (5,5), "black")
# Get the size of the image
x, y = picture.size
h = x*-1
v = y*-1
while (h < x):
    while (v < y):
        #cx = x-(width)
        #cy = y-(height)
        #if (cx**2 + cy**2 == 0):
        #   print x,y
        #else:
        #   new_color = (0,0,0)
        print x,y,h,v
        v = v +1    
h = h + 1


!showme images/new_color-black6.jpg

from PIL import Image
import cv2
from cv2 import *
from math import cos
picture = Image.new( 'RGB', (40,40), "white")

c=10
# Get the size of the image
width, height = picture.size
#fx = x-width*-1
#fy = y-height*-1
fx = x-width
fy = y-height
# Get the size of the image
for x in range(0, width - 1):
     for y in range(0, height - 1):
        fx = int(cos(x-width/2*-1)*10)
        fy = y-height/2*-1
        color = picture.getpixel((x, y))
        if ((fx+fy) < 420):
            zz = fy -300
            new_color = (fx,zz,0)
            picture.putpixel( (x,y), new_color)
        else:
            vv = int((fx+fy)/2)-50
            new_color = (vv,0,fy)
            picture.putpixel( (x,y), new_color)
            print new_color, fx, zz, vv
            
            picture.save("images/new_color-black6.jpg")
        
        
        

from PIL import Image
import cv2
from cv2 import *
from math import cos
picture = Image.new( 'RGB', (256,256), "white")

c=10
# Get the size of the image
width, height = picture.size
#fx = x-width*-1
#fy = y-height*-1
fx = x-width
fy = y-height
# Get the size of the image
for x in range(0, width - 1):
     for y in range(0, height - 1):
        fx = x-width/2*-1
        fy = y-height/2*-1
        color = picture.getpixel((x, y))
        if ((x+y) < 0):
            
            new_color = (fx,fy,0)
        else:
            new_color = (0,fx,fy)
            picture.putpixel( (x,y), new_color)
            #print new_color, fx, fy
            
            picture.save("images/new_color-black1.jpg")
        
        
        

from PIL import Image, ImageOps
picture.save("images/new_color-black.jpg")
#wboder = width+10
wboder = 10
ImageOps.expand(Image.open('images/new_color-black.jpg'),border=wboder,fill='white').save('images/imaged-with-border.png')
!showme images/imaged-with-border.png

ImageOps.expand(picture),border=10,fill="white").save('images/imaged-with-border.png')

cv2.namedWindow('Creation') 

from PIL import Image, ImageOps
import cv2
from cv2 import *

picture = Image.new( 'RGB', (150,150), "black")

# Get the size of the image
width, height = picture.size
# Get the size of the image
for x in range(0, width - 1):
     for y in range(0, height - 1):
        cx = x-(width/2)
        cy = y-(height/2)
        if (cx**2 + cy**2 == 0):
           new_color = (0,0,255)
        else:
           new_color = (0,0,0)
        picture.putpixel( (x,y), new_color)
        picture.save("images/images/000000.jpg")
        #!showme images/new_color-face_300.jpg
        wboder = 10
        ImageOps.expand(Image.open('images/00-new_color-black.jpg'), border=wboder, fill='white').save('images/000imaged-with-border.png')


from PIL import Image, ImageOps
import cv2
from cv2 import *

picture = Image.new( 'RGB', (5,5), "black")
# Get the size of the image
x, y = picture.size
h = x*-1
v = y*-1
print h,v,x,y



from PIL import Image, ImageOps
import cv2
from cv2 import *
cv2.namedWindow('BinaryThreshold') 
height = -50
width = -50

picture = Image.new( 'RGB', (50,50), "black")
# Get the size of the image
x, y = picture.size
h = x*-1
v = y*-1


while (height < abs(height)):
    while (width < abs(width)):
        cx = x-(width)
        cy = y-(height)
        if (cx**2 + cy**2 == 0):
           print x,y
        else:
           new_color = (0,0,0)

    width = width +1    
height = height + 1


from PIL import Image
testimage = Image.open("images/new_color-black.jpg")
w, h = testimage.size
print w
print h
testimage

from PIL import Image
iop = Image.open("images/webcam-border.png")
print iop.size

sized = iop.resize((450,450), Image.NEAREST)
sized.save("images/webcam-borderS.png")

!showme images/webcam-borderS.png

from PIL import Image
cropim = sized.crop((130,100,450,330))
cropim.save("images/cropim.png")

import cv2
import numpy as np
from matplotlib import pyplot as plt
cvimg = cv2.imread('images/webcam.jpg',0)
ret,thresh1 = cv2.threshold(cvimg,127,255,cv2.THRESH_BINARY)
cv2.imwrite("images/thresh1.png", thresh1)

!showme images/thresh1.png

from PIL import Image
img0 = Image.open("images/thresh1.png")
imga = img0.convert("RGBA")
imga
imga.save("images/img0.png")

import numpy as np
import cv2

image = cv2.imread("images/cropim.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray,(15,15),0)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 300, np.array([]), 10, 30, 60, 300)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 1)
        cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow("Circled", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np
import cv2

image = cv2.imread("images/thresh1.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#blur = cv2.GaussianBlur(gray,(9,9),0)

#circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 300, np.array([]), 10, 30, 60, 300)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 300, np.array([]), 5, 5, 100, 100)
ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
edges = cv2.Canny(thresh1, 100,200)
imagem = cv2.bitwise_not(edges)

res = cv2.bitwise_and(image,image, mask=imagem)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 1)
        cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)

#cv2.imshow("Circled", image)
#cv2.imshow("Thresh", thresh1)
#cv2.imshow("edges", edges)
cv2.imshow("imagem", imagem)
cv2.imshow("res", res)

cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np
import cv2


image = cv2.imread("images/webcam-border.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(9,9),0)

#circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 300, np.array([]), 10, 30, 60, 300)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 300, np.array([]), 5, 5, 100, 100)
ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
edges = cv2.Canny(image, 100,200)
imagem = cv2.bitwise_not(edges)

#res = cv2.bitwise_and(image,image, mask=imagem)
res = cv2.bitwise_and(image,image, mask=thresh1)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 1)
        cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)

#cv2.imshow("Circled", image)
#cv2.imshow("Thresh", thresh1)
cv2.imshow("edges", edges)
cv2.imshow("imagem", imagem)
cv2.imshow("res", res)

cv2.imwrite("images/edges-01.png", edges)
cv2.imwrite("images/imagem-01.png", imagem)
cv2.imwrite("images/res.png-01", res)





cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np
import cv2


image = cv2.imread("images/webcam-border.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(9,9),0)

#circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 300, np.array([]), 10, 30, 60, 300)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 300, np.array([]), 5, 5, 100, 100)
ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
edges = cv2.Canny(image, 100,200)
imagem = cv2.bitwise_not(edges)

#res = cv2.bitwise_and(image,image, mask=imagem)
res = cv2.bitwise_and(image,image, mask=thresh1)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 1)
        cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)

#cv2.imshow("Circled", image)
#cv2.imshow("Thresh", thresh1)
cv2.imshow("edges", edges)
cv2.imshow("imagem", imagem)
cv2.imshow("res", res)

cv2.imwrite("images/edges-01.png", edges)
cv2.imwrite("images/imagem-01.png", imagem)
cv2.imwrite("images/res.png-01", res)





cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
from matplotlib import pyplot as plt
 
def nothing(x):
    pass
cv2.namedWindow('canny_edge') 
img_noblur = cv2.imread('images/webcam-border.jpg', 0)
img = cv2.blur(img_noblur, (7,7))
min_value = 0
max_value = 500

cv2.createTrackbar('min_value','canny_edge',0,500,nothing)
cv2.createTrackbar('max_value','canny_edge',0,500,nothing)
while 1:
    # exit on ESC key
    k = cv2.waitKey(0)
    if k == 27:
        break
     
    min_value = cv2.getTrackbarPos('min_value', 'canny_edge')
    max_value = cv2.getTrackbarPos('max_value', 'canny_edge')

    canny_edge = cv2.Canny(img, min_value, max_value)
    cv2.imshow('image', img)
    cv2.imshow('canny_edge', canny_edge)    
    
cv2.waitKey(0)
cv2.destroyAllWindows()

# In progress
import numpy as np
import cv2
from matplotlib import pyplot as plt
#img_noblur = cv2.imread('images/webcam.jpg', 0)
#img = cv2.blur(img_noblur, (7,7))
#img = cv2.imread("images/webcam-border.jpg", 0)
img = cv2.imread("images/webcam-border.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(9,9),0)


# slider callbacks
def printThreshold(x):
    print "threshold",x
def printGaussianBlur(x):
    print "gaussian blur kernel size",x
# make a window to add sliders/preview to
cv2.namedWindow('processed')
#make some sliders
cv2.createTrackbar('threshold','processed',60,255,printThreshold)
cv2.createTrackbar('gaussian blur','processed',3,20,printGaussianBlur)
# load image

# continously process for quick feedback
while 1:
    # exit on ESC key
    k = cv2.waitKey(0)
    if k == 27:
        break

    # Gaussian Blur ( x2 +1 = in order to provide odd number for kernel size)
    kernelSize = ((cv2.getTrackbarPos('gaussian blur','processed') * 2) + 1)
    blur = cv2.GaussianBlur(img,(kernelSize,kernelSize),0)
    # Threshold
    ret,thresh = cv2.threshold(blur,cv2.getTrackbarPos('threshold','processed',),255,0)
    # show result
    cv2.imshow('gaussian blur',blur)
    cv2.imshow('thresh ',thresh)

   
    
    
# exit
cv2.destroyAllWindows()

import numpy as np
import cv2
from matplotlib import pyplot as plt

# slider callbacks
def printThreshold(x):
    print "threshold",x
def printGaussianBlur(x):
    print "gaussian blur kernel size",x
# make a window to add sliders/preview to
cv2.namedWindow('processed')
#make some sliders
cv2.createTrackbar('threshold','processed',60,255,printThreshold)
cv2.createTrackbar('gaussian blur','processed',3,10,printGaussianBlur)
# load image
img = cv2.imread('images/webcam-border.jpg',0)
# continously process for quick feedback
while 1:
    # exit on ESC key
    k = cv2.waitKey(0)
    if k == 27:
        break
    

    # Gaussian Blur ( x2 +1 = odd number for kernel size)
    kernelSize = ((cv2.getTrackbarPos('gaussian blur','processed') * 2) + 1)
    blur = cv2.GaussianBlur(img,(kernelSize,kernelSize),0)
    # Threshold
    ret,thresh = cv2.threshold(blur,cv2.getTrackbarPos('threshold','processed',),255,0)
    # show result
    cv2.imshow('processed ',thresh)

# exit
cv2.destroyAllWindows()

import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
#img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')
cv2.namedWindow('hsv')
cv2.namedWindow('masq')
#cap = cv2.VideoCapture(0)

img = cv2.imread('images/webcam-border.jpg', 1)

# create trackbars for color change
cv2.createTrackbar('R-low','image',0,255,nothing)
cv2.createTrackbar('R-high','image',0,255,nothing)

cv2.createTrackbar('G-low','image',0,255,nothing)
cv2.createTrackbar('G-high','image',0,255,nothing)

cv2.createTrackbar('B-low','image',0,255,nothing)
cv2.createTrackbar('B-high','image',0,255,nothing)


while(1):
    #ret, img = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
        

    # get current positions of four trackbars
    rl = cv2.getTrackbarPos('Rlow','image')
    rh = cv2.getTrackbarPos('Rhigh','image')

    gl = cv2.getTrackbarPos('G-low','image')
    gh = cv2.getTrackbarPos('G-high','image')

    bl = cv2.getTrackbarPos('B-low','image')
    bh = cv2.getTrackbarPos('B-high','image')

    lower = np.array([rl,gl,bl])
    upper = np.array([rh,gh,bh])

    #print(rl)

    img[:] = [bl,gl,rl]

    # Threshold the HSV image to get only certain colors
    mask = cv2.inRange(hsv, Rlow,Rhigh)    


    res = cv2.bitwise_and(img, img, mask= mask)

    cv2.imshow('image',img)
    cv2.imshow('mask',mask)
    cv2.imshow('hsv',hsv)
    cv2.imshow('res',res)
    
     # exit on ESC key
    k = cv2.waitKey(0)
    if k == 27:
        break


cv2.destroyAllWindows()

#Python Program to blur image
import cv2 
#This will give an error if you don't have cv2 module
def nothing(x):
    pass

img = cv2.imread('images/webcam2.jpg', 1) 

cv2.createTrackbar('low','image',5,25,nothing)
cv2.createTrackbar('high','image',5,25,nothing)

while(1):
  
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    
    # get current positions of four trackbars
    k1 = cv2.getTrackbarPos('low','image')
    k2 = cv2.getTrackbarPos('high','image')
    
    lower = np.array([k1])
    upper = np.array([k2])
    
    #make sure that you have saved it in the same folder
    #blurImg = cv2.blur(img,(k1, k2)) #You can change the kernel size as you want
    #cv2.imshow('blurred image',blurImg)
    cv2.imshow('image',img)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
        

    # get current positions of four trackbars
    k1 = cv2.getTrackbarPos('low','image')
    k2 = cv2.getTrackbarPos('high','image')

    #print(rl)

   

    # Threshold the HSV image to get only certain colors
    mask = cv2.inRange(hsv, lower, upper)    

cv2.destroyAllWindows()


import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
#img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')
cv2.namedWindow('hsv')
cv2.namedWindow('masq')
#cap = cv2.VideoCapture(0)

img = cv2.imread('images/webcam2.jpg', 1)

# create trackbars for color change
cv2.createTrackbar('R-low','image',0,255,nothing)
cv2.createTrackbar('R-high','image',0,255,nothing)

cv2.createTrackbar('G-low','image',0,255,nothing)
cv2.createTrackbar('G-high','image',0,255,nothing)

cv2.createTrackbar('B-low','image',0,255,nothing)
cv2.createTrackbar('B-high','image',0,255,nothing)


while(1):
    #ret, img = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    res = cv2.bitwise_and(img, img, mask= mask)
    cv2.imshow('image',img)
    cv2.imshow('res',res)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
        

    # get current positions of four trackbars
    rl = cv2.getTrackbarPos('R-low','image')
    rh = cv2.getTrackbarPos('R-high','image')

    gl = cv2.getTrackbarPos('G-low','image')
    gh = cv2.getTrackbarPos('G-high','image')

    bl = cv2.getTrackbarPos('B-low','image')
    bh = cv2.getTrackbarPos('B-high','image')

    lower = np.array([rl,gl,bl])
    upper = np.array([rh,gh,bh])

    #print(rl)

    img[:] = [bl,gl,rl]

    # Threshold the HSV image to get only certain colors
    mask = cv2.inRange(hsv, lower, upper)    


    

    cv2.imshow('image',img)
    cv2.imshow('mask',mask)
    cv2.imshow('hsv',hsv)
    cv2.imshow('res',res)


cv2.destroyAllWindows()

low_val  = [0 0 0, ..., 249 249 250],[math.floor(n_cols * half_percent)]
print low_val

# ______ WORKS WELL _______
# Get Colors from a Trackbar
import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,300,3), np.uint8)
#Name your window
cv2.namedWindow('image')

# create trackbars for color change place them in namedWindow('image')
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()

import cv2
from matplotlib import pyplot as plt
 
def nothing(x):
    pass
 
img_noblur = cv2.imread('images/webcam2.jpg', 0)
img = cv2.blur(img_noblur, (7,7))
canny_edge = cv2.Canny(img, 0, 0)

cv2.createTrackbar('min_value','canny_edge',0,500,nothing)
cv2.createTrackbar('max_value','canny_edge',0,500,nothing)
 



min_value = cv2.getTrackbarPos('min_value', 'canny_edge')
max_value = cv2.getTrackbarPos('max_value', 'canny_edge')

canny_edge = cv2.Canny(img, min_value, max_value)
cv2.imshow('image', img)
cv2.imshow('canny_edge', canny_edge)
  
    
    
    
# exit on ESC key
k = cv2.waitKey(1)
if k == 27:

        
      
        
     cv2.destroyAllWindows()        
        

#I'm using Python OpenCV to implement an adaptive skin color filter that uses haarcascades to detect an upright face, followed by filtering the face ROI to remove non-skin features like eyebrows, glasses etc to get the average skin tone (in RGB). Then I convert the image to HSV and extract the HSV values close to the average I obtained. Here is my code:
import cv2
import numpy as np
from functions import *
def nothing(x):
    pass
#cap = cv2.VideoCapture(0)
cap = cv2.imread("images/webcam2.jpg")
face_cascade = cv2.CascadeClassifier('/home/jack/Desktop/deep-dream-generator/notebooks/haarcascades/haarcascade_frontalface_alt.xml')
#cv2.namedWindow('Video')
#cv2.moveWindow('Video',5,5)
#cv2.namedWindow('HSV_Thresh')
#cv2.moveWindow('HSV_Thresh',655,5)
cv2.createTrackbar('tval', 'Video', 29, 255, nothing)
cv2.createTrackbar('htoler', 'HSV_Thresh', 17, 100, nothing)
cv2.createTrackbar('stoler', 'HSV_Thresh', 25, 100, nothing)
cv2.createTrackbar('vtoler', 'HSV_Thresh', 84, 100, nothing)

kernel = np.ones((5, 5), np.uint8)# 5X5 erosion kernel
bavg=0
ravg=0
gavg=0
while True: 
    tval1=cv2.getTrackbarPos('tval', 'cap')#thresh value to remove non skin components from face
    htoler_val=cv2.getTrackbarPos('htoler', 'HSV_Thresh')
    stoler_val=cv2.getTrackbarPos('stoler', 'HSV_Thresh')
    vtoler_val=cv2.getTrackbarPos('vtoler', 'HSV_Thresh')
    #ret,img=cv2.imread("image_sized.png")#Read from source
    img=cv2.imread("images/webcam2.jpg")#Read from source
    img[0:100,0:100] = [255,255,255]
    thresh_hsv_toler=img    
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    for (x,y,w,h) in faces:
        bavg=0
        ravg=0
        gavg=0
        numpix=0
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi_face = img[y:y+h, x:x+w]
        #avg_col=img[100,100]
        rect_face=img[y:y+h-h/8,x+w/7:x+w-w/5]#extract only skin features from remaining bg
        mask=cv2.inRange(rect_face,(tval1,tval1,tval1),(255,255,255))
        mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
        tone=cv2.subtract(mask,rect_face)
        tone=cv2.subtract(mask,tone)
        (rows,cols,col)=tone.shape # 480 rows and 640 cols; 3 values for RGB img
        for i in range(rows): #note the presence of colon
            for j in range(cols):
                if (tone[i,j,0]!=0 and tone[i,j,0]!=0 and tone[i,j,0]!=0):
                    bavg=bavg+tone[i,j,0]
                    gavg=gavg+tone[i,j,1]
                    ravg=ravg+tone[i,j,2]
                    numpix=numpix+1
                    bavg=bavg/numpix
                    gavg=gavg/numpix
                    ravg=ravg/numpix
                    '''print "bavg="+str(bavg)
                    print "gavg="+str(gavg)
                    print "ravg="+str(ravg)
                    print "numpix="+str(numpix)'''
                    cv2.circle(img, (50,50), 20, (bavg,gavg,ravg), 50)#get obtained average colour on screen


                    cv2.imshow('skin_mask', tone)
                    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
                    thresh_hsv_toler=cv2.inRange(hsv,(hsv[50,50,0]-htoler_val,hsv[50,50,1]-stoler_val,hsv[50,50,2]-vtoler_val),(hsv[50,50,0]+htoler_val,hsv[50,50,1]+stoler_val,hsv[50,50,2]+vtoler_val))

                    thresh_hsv_toler=cv2.dilate(thresh_hsv_toler, kernel, iterations=1)
                    thresh_hsv_toler=cv2.cvtColor(thresh_hsv_toler,cv2.COLOR_GRAY2BGR)#superimposing binary mask on image
                    hsv_filter=cv2.subtract(thresh_hsv_toler,img)
                    hsv_filter=cv2.subtract(thresh_hsv_toler,hsv_filter)



                    cv2.imshow('HSV_Thresh', hsv_filter)
                    cv2.imshow('Video', img)
                    if(cv2.waitKey(10) & 0xFF == ord('b')):
                        break
                    cv2.imshow('Video', img)

!ls images

#I'm using Python OpenCV to implement an adaptive skin color filter that uses haarcascades to detect an upright face, followed by filtering the face ROI to remove non-skin features like eyebrows, glasses etc to get the average skin tone (in RGB). Then I convert the image to HSV and extract the HSV values close to the average I obtained. Here is my code:
import cv2
import numpy as np
from functions import *
def nothing(x):
    pass
#cap = cv2.VideoCapture(0)
cap = cv2.imread("images/webcam.border.jpg")
face_cascade = cv2.CascadeClassifier('/home/jack/Desktop/deep-dream-generator/notebooks/haarcascades/haarcascade_frontalface_alt.xml')
cv2.namedWindow('Video')
cv2.moveWindow('Video',5,5)
cv2.namedWindow('HSV_Thresh')
cv2.moveWindow('HSV_Thresh',655,5)
cv2.createTrackbar('tval', 'Video', 29, 255, nothing)
cv2.createTrackbar('htoler', 'HSV_Thresh', 17, 100, nothing)
cv2.createTrackbar('stoler', 'HSV_Thresh', 25, 100, nothing)
cv2.createTrackbar('vtoler', 'HSV_Thresh', 84, 100, nothing)

kernel = np.ones((5, 5), np.uint8)# 5X5 erosion kernel
bavg=0
ravg=0
gavg=0
while True: 
    tval1=cv2.getTrackbarPos('tval', 'Video')#thresh value to remove non skin components from face
    htoler_val=cv2.getTrackbarPos('htoler', 'HSV_Thresh')
    stoler_val=cv2.getTrackbarPos('stoler', 'HSV_Thresh')
    vtoler_val=cv2.getTrackbarPos('vtoler', 'HSV_Thresh')
    #ret,img=cv2.imread("image_sized.png")#Read from source
    img=cv2.imread("image_sized.png")#Read from source
    img[0:100,0:100] = [255,255,255]
    thresh_hsv_toler=img    
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    for (x,y,w,h) in faces:
        bavg=0
        ravg=0
        gavg=0
        numpix=0
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi_face = img[y:y+h, x:x+w]
        #avg_col=img[100,100]
        rect_face=img[y:y+h-h/8,x+w/7:x+w-w/5]#extract only skin features from remaining bg
        mask=cv2.inRange(rect_face,(tval1,tval1,tval1),(255,255,255))
        mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
        tone=cv2.subtract(mask,rect_face)
        tone=cv2.subtract(mask,tone)
        (rows,cols,col)=tone.shape # 480 rows and 640 cols; 3 values for RGB img
        for i in range(rows): #note the presence of colon
            for j in range(cols):
                if (tone[i,j,0]!=0 and tone[i,j,0]!=0 and tone[i,j,0]!=0):
                    bavg=bavg+tone[i,j,0]
                    gavg=gavg+tone[i,j,1]
                    ravg=ravg+tone[i,j,2]
                    numpix=numpix+1
                    bavg=bavg/numpix
                    gavg=gavg/numpix
                    ravg=ravg/numpix
                    '''print "bavg="+str(bavg)
                    print "gavg="+str(gavg)
                    print "ravg="+str(ravg)
                    print "numpix="+str(numpix)'''
                    cv2.circle(img, (50,50), 20, (bavg,gavg,ravg), 50)#get obtained average colour on screen


                    cv2.imshow('skin_mask', tone)
                    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
                    thresh_hsv_toler=cv2.inRange(hsv,(hsv[50,50,0]-htoler_val,hsv[50,50,1]-stoler_val,hsv[50,50,2]-vtoler_val),(hsv[50,50,0]+htoler_val,hsv[50,50,1]+stoler_val,hsv[50,50,2]+vtoler_val))

                    thresh_hsv_toler=cv2.dilate(thresh_hsv_toler, kernel, iterations=1)
                    thresh_hsv_toler=cv2.cvtColor(thresh_hsv_toler,cv2.COLOR_GRAY2BGR)#superimposing binary mask on image
                    hsv_filter=cv2.subtract(thresh_hsv_toler,img)
                    hsv_filter=cv2.subtract(thresh_hsv_toler,hsv_filter)



                    cv2.imshow('HSV_Thresh', hsv_filter)


                    if(cv2.waitKey(10) & 0xFF == ord('b')):
                        break
                    cv2.imshow('Video', img)

#I'm using Python OpenCV to implement an adaptive skin color filter that uses haarcascades to detect an upright face, followed by filtering the face ROI to remove non-skin features like eyebrows, glasses etc to get the average skin tone (in RGB). Then I convert the image to HSV and extract the HSV values close to the average I obtained. Here is my code:
import cv2
import numpy as np
from functions import *
def nothing(x):
    pass
#cap = cv2.VideoCapture(0)
cap = cv2.imread("images/image_sized.png")
face_cascade = cv2.CascadeClassifier('/home/jack/Desktop/deep-dream-generator/notebooks/haarcascades/haarcascade_frontalface_alt.xml')
cv2.namedWindow('Video')
cv2.moveWindow('Video',5,5)
cv2.namedWindow('HSV_Thresh')
cv2.moveWindow('HSV_Thresh',655,5)
cv2.createTrackbar('tval', 'Video', 29, 255, nothing)
cv2.createTrackbar('htoler', 'HSV_Thresh', 17, 100, nothing)
cv2.createTrackbar('stoler', 'HSV_Thresh', 25, 100, nothing)
cv2.createTrackbar('vtoler', 'HSV_Thresh', 84, 100, nothing)

kernel = np.ones((5, 5), np.uint8)# 5X5 erosion kernel
bavg=0
ravg=0
gavg=0
while True: 
    tval1=cv2.getTrackbarPos('tval', 'Video')#thresh value to remove non skin components from face
    htoler_val=cv2.getTrackbarPos('htoler', 'HSV_Thresh')
    stoler_val=cv2.getTrackbarPos('stoler', 'HSV_Thresh')
    vtoler_val=cv2.getTrackbarPos('vtoler', 'HSV_Thresh')
    #ret,img=cv2.imread("image_sized.png")#Read from source
    img=cv2.imread("images/image_sized.png")#Read from source
    img[0:100,0:100] = [255,255,255]
    thresh_hsv_toler=img    
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    for (x,y,w,h) in faces:
        bavg=0
        ravg=0
        gavg=0
        numpix=0
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi_face = img[y:y+h, x:x+w]
        #avg_col=img[100,100]
        rect_face=img[y:y+h-h/8,x+w/7:x+w-w/5]#extract only skin features from remaining bg
        mask=cv2.inRange(rect_face,(tval1,tval1,tval1),(255,255,255))
        mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
        tone=cv2.subtract(mask,rect_face)
        tone=cv2.subtract(mask,tone)
        (rows,cols,col)=tone.shape # 480 rows and 640 cols; 3 values for RGB img
        for i in range(rows): #note the presence of colon
            for j in range(cols):
                if (tone[i,j,0]!=0 and tone[i,j,0]!=0 and tone[i,j,0]!=0):
                bavg=bavg+tone[i,j,0]
                gavg=gavg+tone[i,j,1]
                ravg=ravg+tone[i,j,2]
                numpix=numpix+1
                bavg=bavg/numpix
                gavg=gavg/numpix
                ravg=ravg/numpix
                '''print "bavg="+str(bavg)
                print "gavg="+str(gavg)
                print "ravg="+str(ravg)
                print "numpix="+str(numpix)'''
                cv2.circle(img, (50,50), 20, (bavg,gavg,ravg), 50)#get obtained average colour on screen


                cv2.imshow('skin_mask', tone)
                hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
                thresh_hsv_toler=cv2.inRange(hsv,(hsv[50,50,0]-htoler_val,hsv[50,50,1]-stoler_val,hsv[50,50,2]-vtoler_val),(hsv[50,50,0]+htoler_val,hsv[50,50,1]+stoler_val,hsv[50,50,2]+vtoler_val))

                thresh_hsv_toler=cv2.dilate(thresh_hsv_toler, kernel, iterations=1)
                thresh_hsv_toler=cv2.cvtColor(thresh_hsv_toler,cv2.COLOR_GRAY2BGR)#superimposing binary mask on image
                hsv_filter=cv2.subtract(thresh_hsv_toler,img)
                hsv_filter=cv2.subtract(thresh_hsv_toler,hsv_filter)



                cv2.imshow('HSV_Thresh', hsv_filter)


                if(cv2.waitKey(10) & 0xFF == ord('b')):
                break
                cv2.imshow('Video', img)

#I'm using Python OpenCV to implement an adaptive skin color filter that uses haarcascades to detect an upright face, followed by filtering the face ROI to remove non-skin features like eyebrows, glasses etc to get the average skin tone (in RGB). Then I convert the image to HSV and extract the HSV values close to the average I obtained. Here is my code:

import cv2
import numpy as np
from functions import *
def nothing(x):
    pass
#cap = cv2.VideoCapture(0)
cap = cv2.imread("images/image_sized.png")
face_cascade = cv2.CascadeClassifier('/home/jack/Desktop/deep-dream-generator/notebooks/haarcascades/haarcascade_frontalface_alt.xml')
cv2.namedWindow('Video')
cv2.moveWindow('Video',5,5)
cv2.namedWindow('HSV_Thresh')
cv2.moveWindow('HSV_Thresh',655,5)
cv2.createTrackbar('tval', 'Video', 29, 255, nothing)
cv2.createTrackbar('htoler', 'HSV_Thresh', 17, 100, nothing)
cv2.createTrackbar('stoler', 'HSV_Thresh', 25, 100, nothing)
cv2.createTrackbar('vtoler', 'HSV_Thresh', 84, 100, nothing)

kernel = np.ones((5, 5), np.uint8)# 5X5 erosion kernel
bavg=0
ravg=0
gavg=0
while True: 
    tval1=cv2.getTrackbarPos('tval', 'Video')#thresh value to remove non skin components from face
    htoler_val=cv2.getTrackbarPos('htoler', 'HSV_Thresh')
    stoler_val=cv2.getTrackbarPos('stoler', 'HSV_Thresh')
    vtoler_val=cv2.getTrackbarPos('vtoler', 'HSV_Thresh')
    #ret,img=cv2.imread("image_sized.png")#Read from source
    img=cv2.imread("image_sized.png")#Read from source
    img[0:100,0:100] = [255,255,255]
    thresh_hsv_toler=img    
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    for (x,y,w,h) in faces:
        bavg=0
        ravg=0
        gavg=0
        numpix=0
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi_face = img[y:y+h, x:x+w]
        #avg_col=img[100,100]
        rect_face=img[y:y+h-h/8,x+w/7:x+w-w/5]#extract only skin features from remaining bg
        mask=cv2.inRange(rect_face,(tval1,tval1,tval1),(255,255,255))
        mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
        tone=cv2.subtract(mask,rect_face)
        tone=cv2.subtract(mask,tone)
        (rows,cols,col)=tone.shape # 480 rows and 640 cols; 3 values for RGB img
    for i in range(rows): #note the presence of colon
        for j in range(cols):
            if (tone[i,j,0]!=0 and tone[i,j,0]!=0 and tone[i,j,0]!=0):
            bavg=bavg+tone[i,j,0]
            gavg=gavg+tone[i,j,1]
            ravg=ravg+tone[i,j,2]
            numpix=numpix+1
            bavg=bavg/numpix
            gavg=gavg/numpix
            ravg=ravg/numpix
            '''print "bavg="+str(bavg)
            print "gavg="+str(gavg)
            print "ravg="+str(ravg)
            print "numpix="+str(numpix)'''
            cv2.circle(img, (50,50), 20, (bavg,gavg,ravg), 50)#get obtained average colour on screen


            cv2.imshow('skin_mask', tone)
            hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
            thresh_hsv_toler=cv2.inRange(hsv,(hsv[50,50,0]-htoler_val,hsv[50,50,1]-stoler_val,hsv[50,50,2]-vtoler_val),(hsv[50,50,0]+htoler_val,hsv[50,50,1]+stoler_val,hsv[50,50,2]+vtoler_val))

            thresh_hsv_toler=cv2.dilate(thresh_hsv_toler, kernel, iterations=1)
            thresh_hsv_toler=cv2.cvtColor(thresh_hsv_toler,cv2.COLOR_GRAY2BGR)#superimposing binary mask on image
            hsv_filter=cv2.subtract(thresh_hsv_toler,img)
            hsv_filter=cv2.subtract(thresh_hsv_toler,hsv_filter)



            cv2.imshow('HSV_Thresh', hsv_filter)


        if(cv2.waitKey(10) & 0xFF == ord('b')):
break
    cv2.imshow('Video', img)

!pip install functions

#!/usr/bin/env python

'''
Coherence-enhancing filtering example
=====================================
inspired by
  Joachim Weickert "Coherence-Enhancing Shock Filters"
  http://www.mia.uni-saarland.de/Publications/weickert-dagm03.pdf
'''

# Python 2/3 compatibility
from __future__ import print_function
import sys
PY3 = sys.version_info[0] == 3

if PY3:
    xrange = range

import numpy as np
import cv2

def coherence_filter(img, sigma = 11, str_sigma = 11, blend = 0.5, iter_n = 4):
    h, w = img.shape[:2]

    for i in xrange(iter_n):
        print(i)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        eigen = cv2.cornerEigenValsAndVecs(gray, str_sigma, 3)
        eigen = eigen.reshape(h, w, 3, 2)  # [[e1, e2], v1, v2]
        x, y = eigen[:,:,1,0], eigen[:,:,1,1]

        gxx = cv2.Sobel(gray, cv2.CV_32F, 2, 0, ksize=sigma)
        gxy = cv2.Sobel(gray, cv2.CV_32F, 1, 1, ksize=sigma)
        gyy = cv2.Sobel(gray, cv2.CV_32F, 0, 2, ksize=sigma)
        gvv = x*x*gxx + 2*x*y*gxy + y*y*gyy
        m = gvv < 0

        ero = cv2.erode(img, None)
        dil = cv2.dilate(img, None)
        img1 = ero
        img1[m] = dil[m]
        img = np.uint8(img*(1.0 - blend) + img1*blend)
    print('done')
    return img


if __name__ == '__main__':
    import sys
    try:
        fn = sys.argv[1]
    except:
        fn = 'images/image_sized.png'

    src = cv2.imread(fn)

    def nothing(*argv):
        pass

    def update():
        sigma = cv2.getTrackbarPos('sigma', 'control')*2+1
        str_sigma = cv2.getTrackbarPos('str_sigma', 'control')*2+1
        blend = cv2.getTrackbarPos('blend', 'control') / 10.0
        print('sigma: %d  str_sigma: %d  blend_coef: %f' % (sigma, str_sigma, blend))
        dst = coherence_filter(src, sigma=sigma, str_sigma = str_sigma, blend = blend)
        cv2.imshow('dst', dst)

    cv2.namedWindow('control', 0)
    cv2.createTrackbar('sigma', 'control', 9, 15, nothing)
    cv2.createTrackbar('blend', 'control', 7, 10, nothing)
    cv2.createTrackbar('str_sigma', 'control', 9, 15, nothing)


    print('Press SPACE to update the image\n')

    cv2.imshow('src', src)
    update()
    while True:
        ch = cv2.waitKey()
        if ch == ord(' '):
            update()
        if ch == 27:
            break
cv2.destroyAllWindows()

import cv2;
import numpy as np;
 
# Read image
im_in = cv2.imread("images/webcam-border.png", cv2.IMREAD_GRAYSCALE);
 
# Threshold.
# Set values equal to or above 220 to 0.
# Set values below 220 to 255.
 
th, im_th = cv2.threshold(im_in, 120, 255, cv2.THRESH_BINARY_INV);
 
# Copy the thresholded image.
im_floodfill = im_th.copy()
 
# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
 
# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (0,0), 255);
 
# Invert floodfilled image
im_floodfill_inv = cv2.bitwise_not(im_floodfill)
 
# Combine the two images to get the foreground.
im_out = im_th | im_floodfill_inv
 
# Display images.
cv2.imshow("Thresholded Image", im_th)
cv2.imshow("Floodfilled Image", im_floodfill)
cv2.imshow("Inverted Floodfilled Image", im_floodfill_inv)
cv2.imshow("Foreground", im_out)
while True:
    ch = 0xFF & cv2.waitKey()
    if ch == 27:
        break
        
cv2.destroyAllWindows()       

update(dummy=35,65,img = cv2.imread("images/webcam-border.png"))       

import cv2
label = cv2.imread("images/webcam-border.png")
ormap = np.bitwise_or(label,detmap).astype(uint8)
mask = np.zeros((image_size+2,imagesize+2),np.uint8)
for y in range(image_size):
    for x in range(image_size):
        if label[y,x]>0:
            cv2.floodFill(ormap,mask,(y,x),0)

import numpy as np
import cv2

image = cv2.imread("images/webcam-border.png")
h, w = image.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
mask[:] |= 0
flags = 4
flags |= cv2.FLOODFILL_FIXED_RANGE
           
for x in range(20,image.shape[1]-20, 20):
    for y in range(20,image.shape[0]-20, 20):
        print x, y
        mask[:] = 0
        flooded = image.copy()
        print 'starting flood fill'
        size = cv2.floodFill(flooded,mask,(x,y),(0,)*3, (40,)*3, (40,)*3, flags)[0]            

import numpy as np
import cv2

image = cv2.imread("images/webcam-border.png")
for x in range(20,image.shape[1]-20, 20):
    for y in range(20,image.shape[0]-20, 20):
        print x, y
        mask[:] = 0
        flooded = image.copy()
        print 'starting flood fill'
        size = cv2.floodFill(flooded,mask,(x,y),(0,)*3, (40,)*3, (40,)*3, flags)[0]
        

# Python program for Detection of a 
# specific color(blue here) using OpenCV with Python
import cv2
import numpy as np 
 
# Webcamera no 0 is used to capture the frames
cap = cv2.VideoCapture(0) 
 
# This drives the program into an infinite loop.
while(1):       
    # Captures the live stream frame-by-frame
    _, frame = cap.read() 
    # Converts images from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([110,50,50])
    upper_red = np.array([130,255,255])
 
# Here we are defining range of bluecolor in HSV
# This creates a mask of blue coloured 
# objects found in the frame.
mask = cv2.inRange(hsv, lower_red, upper_red)
 
# The bitwise and of the frame and mask is done so 
# that only the blue coloured objects are highlighted 
# and stored in res
res = cv2.bitwise_and(frame,frame, mask= mask)
cv2.imshow('frame',frame)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
 
# This displays the frame, mask 
# and res which we created in 3 separate windows.
k = cv2.waitKey(5) &amp; 0xFF
if k == 27:
break
 
# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()
 
# release the captured frame
cap.release()

# Python program for Detection of a 
# specific color(blue here) using OpenCV with Python
import cv2
import numpy as np 
 
# Webcamera no 0 is used to capture the frames
cap = cv2.VideoCapture(0) 
 
# This drives the program into an infinite loop.
while(1):       
    # Captures the live stream frame-by-frame
    _, frame = cap.read() 
    # Converts images from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #lower_red = np.array([110,50,50])
    #upper_red = np.array([130,255,255])
    cv2.createTrackbar('lowH','image',ilowH,180,callback)
    cv2.createTrackbar('highH','image',ihighH,255,callback)
    lH = cv2.getTrackbarPos('lowH','image')
    hH = cv2.getTrackbarPos('highH','image')
    
    
    
    
    lower_red = np.array([lH,0,0])
    upper_red = np.array([hH,255,255])
 
    # Here we are defining range of bluecolor in HSV
    # This creates a mask of blue coloured 
    # objects found in the frame.
    mask = cv2.inRange(hsv, lower_red, upper_red)
    mask = mask - 255
    # The bitwise and of the frame and mask is done so 
    # that only the blue coloured objects are highlighted 
    # and stored in res
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    # This displays the frame, mask 
    # and res which we created in 3 separate windows.
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()


!ls

# Python program for Detection of a 
# specific color(blue here) using OpenCV with Python
import cv2
import numpy as np 
 
# Webcamera no 0 is used to capture the frames
cap = cv2.VideoCapture(0) 
cv2.namedWindow('image') 
# This drives the program into an infinite loop.
ilowH = 180
IhighH = 255

while(1):       
    # Captures the live stream frame-by-frame
    _, frame = cap.read() 
    # Converts images from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #lower_red = np.array([110,50,50])
    #upper_red = np.array([130,255,255])
    
    
    cv2.createTrackbar('lowH','image',ilowH,180,callback)
    cv2.createTrackbar('highH','image',ihighH,255,callback)
    lH = cv2.getTrackbarPos('lowH','image')
    hH = cv2.getTrackbarPos('highH','image')
    
    
    
    
    lower_red = np.array([lH,0,0])
    upper_red = np.array([hH,255,255])
 
    # Here we are defining range of bluecolor in HSV
    # This creates a mask of blue coloured 
    # objects found in the frame.
    mask = cv2.inRange(hsv, lower_red, upper_red)
    mask = mask - 255
    # The bitwise and of the frame and mask is done so 
    # that only the blue coloured objects are highlighted 
    # and stored in res
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    # This displays the frame, mask 
    # and res which we created in 3 separate windows.
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()


#WORKING FINE
import cv2
import numpy as np

def callback(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('image')

ilowH = 180
ihighH = 255

ilowS = 0
ihighS = 255

ilowV = 0
ihighV = 255

thresl =0
thresh =255

# create trackbars for color change
cv2.createTrackbar('lowH','image',ilowH,180,callback)
cv2.createTrackbar('highH','image',ihighH,255,callback)

cv2.createTrackbar('lowS','image',ilowS,255,callback)
cv2.createTrackbar('highS','image',ihighS,255,callback)

cv2.createTrackbar('lowV','image',ilowV,255,callback)
cv2.createTrackbar('highV','image',ihighV,255,callback)

cv2.createTrackbar('lowT','image',thresl,127,callback)
cv2.createTrackbar('highT','image',thresh,255,callback)


while(1):
    # get current positions of four trackbars
    lH = cv2.getTrackbarPos('lowH','image')
    hH = cv2.getTrackbarPos('highH','image')
    lS = cv2.getTrackbarPos('lowS','image')
    hS = cv2.getTrackbarPos('highS','image')
    lV = cv2.getTrackbarPos('lowV','image')
    hV = cv2.getTrackbarPos('highV','image')
    lT = cv2.getTrackbarPos('lowT','image')
    hT = cv2.getTrackbarPos('highT','image')
    
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv', hsv)
    lower_hsv = np.array([lH, lS, lV])
    higher_hsv = np.array([hH, hS, hV])
    mask = cv2.inRange(hsv, lower_hsv, higher_hsv)
    mask = 255 - mask
    result = cv2.bitwise_or(frame,frame, mask= mask)
    hsvmask = cv2.bitwise_or(hsv,hsv, mask= mask)
    
    ret,thresh2 = cv2.threshold(frame,lT,hT,cv2.THRESH_BINARY) 
    
    
    #result = cv2.bitwise_not(frame,frame, mask= mask)
    #hsvmask = cv2.bitwise_not(hsv,hsv, mask= mask)
    cv2.imshow('thresh2', thresh2)
    cv2.imshow('result', result)
    cv2.imshow('mask', mask)
    cv2.imshow('frame', frame)
    cv2.imshow('hsvmask', hsvmask)
    #print ilowH, ilowS, ilowV
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()


# KEEP to WORK WITH
import cv2
import numpy as np
# Read image
im_in = cv2.imread('images/webcam-border.png', cv2.IMREAD_GRAYSCALE)

th, im_th = cv2.threshold(im_in, 50, 65, cv2.THRESH_BINARY_INV)
# Copy the thresholded image.
im_floodfill = im_th.copy()
# Mask used to flood filling.
h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (0,0), 255)
# Invert floodfilled image
im_floodfill_inv = cv2.bitwise_not(im_floodfill)
# Combine the two images to get the foreground.
im_out = im_th | im_floodfill_inv
# Display images.
cv2.imshow("Foreground", im_out)
cv2.waitKey(0)

#Creating a ghost 

import cv2
import numpy as np
 
c = cv2.VideoCapture(0)
_,f = c.read()
 
avg1 = np.float32(f)
avg2 = np.float32(f)
 
while(1):
    _,f = c.read()
     
    cv2.accumulateWeighted(f,avg1,0.1)
    cv2.accumulateWeighted(f,avg2,0.01)
     
    res1 = cv2.convertScaleAbs(avg1)
    res2 = cv2.convertScaleAbs(avg2)
 
    cv2.imshow('img',f)
    cv2.imshow('avg1',res1)
    cv2.imshow('avg2',res2)
    k = cv2.waitKey(20)
 
    if k == 27:
        break
 
cv2.destroyAllWindows()
c.release()

import cv2
import sys
sys.path.insert(0, "/home/jack/Desktop/pycode/vpython2/webcam/samples")
import video
import numpy as np


def nothing(x):
    pass
def Circles():
    cv2.namedWindow('Circles')
    cv2.namedWindow('parameters')

    cv2.createTrackbar('dp', 'parameters', 1, 20, nothing)
    cv2.createTrackbar('minDist', 'parameters', 10, 700, nothing)
    cv2.createTrackbar('CannyParam', 'parameters', 1, 300, nothing)
    cv2.createTrackbar('AccumulatorThrs', 'parameters', 1, 100, nothing)
    cv2.createTrackbar('minRadius', 'parameters', 1, 50, nothing)
    cv2.createTrackbar('maxRadius', 'parameters', 51, 700, nothing)


    image = cv2.imread('images/webcam-border.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    gray = gray[:,:,2]
    #cv2.imshow('ImageGray', gray)
    while True:
        dp = cv2.getTrackbarPos('dp', 'parameters')
        minDist = cv2.getTrackbarPos('minDist', 'parameters')
        CannyParam = cv2.getTrackbarPos('CannyParam', 'parameters')
        AccumulatorThrs = cv2.getTrackbarPos('AccumulatorThrs', 'parameters')
        minRadius = cv2.getTrackbarPos('minRadius', 'parameters')
        maxRadius = cv2.getTrackbarPos('maxRadius', 'parameters')

        circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,dp,minDist,CannyParam,AccumulatorThrs,minRadius,maxRadius)
        circles = np.uint16(np.around(circles))

        for i in circles[0,:]:
            cv2.circle(image,(i[0],i[1]),i[2],(0,255,0),2)
            cv2.circle(image,(i[0],i[1]),2,(0,0,255),3)

            cv2.imshow('Circles', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

Circles()

import cv2
import numpy as np

def nothing(x):
    pass
def Foo(int,void*);
    
# Create a black image, a window
img = cv2.imread("images/webcam-border.png")
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('A','image',0,1000,Foo)

#cv2.CreateTrackbar(trackbarName, windowName, value, count, onChange)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    a = cv2.getTrackbarPos('A','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()

%reset -f

from __future__ import print_function
 
import numpy as np
import cv2
 
img = cv2.imread("images/webcam-border.png", True)


if img is None:
     print('Failed to load image file:', fn)
     sys.exit(1)
 
     h, w = img.shape[:2]
     mask = np.zeros((h+2, w+2), np.uint8)
     seed_pt = None
     fixed_range = True
     connectivity = 4
 
     def update(dummy=None):
         if seed_pt is None:
             #cv2.imshow('floodfill', img)
             cv2.namedWindow('floodfill') 
             return
         flooded = img.copy()
         mask[:] = 0
         lo = cv2.getTrackbarPos('lo', 'floodfill')
         hi = cv2.getTrackbarPos('hi', 'floodfill')
         flags = connectivity
         if fixed_range:
             flags |= cv2.FLOODFILL_FIXED_RANGE
         cv2.floodFill(flooded, mask, seed_pt, (255, 255, 255), (lo,)*3, (hi,)*3, flags)
         cv2.circle(flooded, seed_pt, 2, (0, 0, 255), -1)
         cv2.imshow('floodfill', flooded)
 
     def onmouse(event, x, y, flags, param):
         global seed_pt
         if flags & cv2.EVENT_FLAG_LBUTTON:
             seed_pt = x, y
             update()
 
             update()
             cv2.setMouseCallback('floodfill', onmouse)
             cv2.createTrackbar('lo', 'floodfill', 20, 255, update)
             cv2.createTrackbar('hi', 'floodfill', 20, 255, update)

             while True:
                 ch = cv2.waitKey()
                 if ch == 27:
                     break
                 if ch == ord('f'):
                     fixed_range = not fixed_range
                     print('using %s range' % ('floating', 'fixed')[fixed_range])
                     update()
                 if ch == ord('c'):
                     connectivity = 12-connectivity
                     print('connectivity =', connectivity)
                     update()
             cv2.destroyAllWindows()


import cv2
#write simple update function to pass the trackbar position as *arg    
def update(*arg): 
    pass

#create display window for image
cv2.namedWindow('BinaryThreshold') 

#read in image
img = cv2.imread(r'images/webcam-border.png',0)

#instantiate trackbar that goes in our named window and uses callback function
cv2.createTrackbar('ThreshAdjust','BinaryThreshold',5,15,update)

#initialize thresholds
thresh1=11
thresh2=5

#loop really just runs until the escape key causes a break
while(True):

    #sets threshold 2 to trackbar position
    thresh2=cv2.getTrackbarPos('ThreshAdjust','BinaryThreshold')   
    #apply laplacian filter to ehance edge gradients
    th = cv2.Laplacian(img,cv2.CV_8UC1)
    #binarize image with adaptive threshold
    result = cv2.adaptiveThreshold(th,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,thresh1,thresh2) 

    #show filtered image
    cv2.imshow('BinaryThreshold',result)
    #waits for escape key then breaks out of loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

#close our display window     
cv2.destroyAllWindows()

# ______ WORKS WELL _______
# Get Colors from a Trackbar
import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,300,3), np.uint8)
#Name your window
cv2.namedWindow('image')

# create trackbars for color change place them in namedWindow('image')
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()

#/usr/bin/env python
#Works Run from Jupyter Note book

'''
Floodfill sample.

Usage:
floodfill.py [<image>]

Click on the image to set seed point

Keys:
f     - toggle floating range
c     - toggle 4/8 connectivity
ESC   - exit
'''

import numpy as np
from scipy import ndimage
import cv2
import math
import svgfig


img = cv2.imread("images/webcam-border.png", True)
#img = cv2.imread(fn, True)
h, w = img.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
seed_pt = None
fixed_range = True
connectivity = 4
history = np.zeros((h+2, w+2), np.uint8)

def update_floodfill(dummy=None):
    global history
    if seed_pt is None:
        cv2.imshow('floodfill', img)
        return
    flooded = img.copy()
    mask[:] = 0
    lo = cv2.getTrackbarPos('lo', 'floodfill')
    hi = cv2.getTrackbarPos('hi', 'floodfill')
    flags = (8 | 255 << 8) | cv2.FLOODFILL_MASK_ONLY
    cv2.floodFill(flooded, mask, seed_pt, (255, 0, 0), (lo,)*3, (hi,)*3,
                  flags)

    # find outmost contour and fill it to remove everything inside
    _,contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(mask, contours[0], 0, 255, cv2.FILLED)

    # find edges
    edges = cv2.Canny(mask, 80, 120)

    # show blue lines on floodfill to show guessed lines
    lines = cv2.HoughLinesP(edges, 1, math.pi/180, 1, 20, 2)
    for line in lines[0]:
        cv2.line(flooded, (line[0], line[1]), (line[2], line[3]), (255, 0, 0), 1)
    cv2.circle(flooded, seed_pt, 2, (0, 0, 255), -1)

    history = np.bitwise_or(history, edges)

    # inverse it so that it's black edges on white
    edges = cv2.bitwise_not(edges)

    cv2.imshow('history', cv2.bitwise_not(history))
    cv2.imshow('floodfill', flooded)

def update_canny(dummy=None):
    contour_map = np.zeros((h+2, w+2), np.uint8)
    blue, green, red = cv2.split(img)

    # Run canny edge detection on each channel
    stroke = cv2.getTrackbarPos('stroke', 'canny')
    lo = cv2.getTrackbarPos('lo', 'canny')
    hi = cv2.getTrackbarPos('hi', 'canny')
    min_size = cv2.getTrackbarPos('min_size', 'canny')
    max_size = cv2.getTrackbarPos('max_size', 'canny')
    blue_edges = cv2.Canny(img, lo, hi)
    green_edges = cv2.Canny(img, lo, hi)
    red_edges = cv2.Canny(img, lo, hi)
    rgb_edges = blue_edges | green_edges | red_edges
    cv2.imshow('edges', cv2.bitwise_not(rgb_edges))

    _,contours, hierarchies = cv2.findContours(rgb_edges, cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    filtered = []
    for cnt, hierarchy in zip(contours, hierarchies[0]):
        if hierarchy[3] < 0:
            area = cv2.contourArea(cnt)
            if area >= min_size and area <= max_size:
                filtered.append(cnt)

    cv2.drawContours(contour_map, filtered, -1, 255, stroke)  # cv2.cv.CV_FILLED

    lined = img.copy()
    lines = cv2.HoughLinesP(contour_map, 1, math.pi/180, 1, 20, 2)
    for line in lines[0]:
        cv2.line(lined, (line[0], line[1]), (line[2], line[3]), (255, 0, 0), 1)

    cv2.imshow('lined', lined)
    cv2.imshow('contours', cv2.bitwise_not(contour_map))

def onmouse(event, x, y, flags, param):
    global seed_pt
    if flags & cv2.EVENT_FLAG_LBUTTON:
        seed_pt = x, y
        update_floodfill()

update_floodfill()
cv2.setMouseCallback('floodfill', onmouse)
cv2.createTrackbar('lo', 'floodfill', 10, 255, update_floodfill)
cv2.createTrackbar('hi', 'floodfill', 10, 255, update_floodfill)

cv2.imshow('canny', img)
# cv2.setMouseCallback('canny', update_canny)
cv2.createTrackbar('min_size', 'canny', 200, 4000, update_canny)
cv2.createTrackbar('max_size', 'canny', 4000, 60000, update_canny)
cv2.createTrackbar('lo', 'canny', 60, 255, update_canny)
cv2.createTrackbar('hi', 'canny', 180, 255, update_canny)
cv2.createTrackbar('stroke', 'canny', 2, 6, update_canny)
update_canny()

while True:
    ch = 0xFF & cv2.waitKey()
    if ch == 27:
        break
cv2.destroyAllWindows()



import cv2
#write simple update function to pass the trackbar position as *arg    
def update(*arg): 
    pass

#create display window for image
cv2.namedWindow('BinaryThreshold') 

#read in image
img = cv2.imread(r'images/webcam-border.png',0)

#instantiate trackbar that goes in our named window and uses callback function
cv2.createTrackbar('ThreshAdjust','BinaryThreshold',5,15,update)

#initialize thresholds
thresh1=11
thresh2=5

#loop really just runs until the escape key causes a break
while(True):

    #sets threshold 2 to trackbar position
    thresh2=cv2.getTrackbarPos('ThreshAdjust','BinaryThreshold')   
    #apply laplacian filter to ehance edge gradients
    th = cv2.Laplacian(img,cv2.CV_8UC1)
    #binarize image with adaptive threshold
    result = cv2.adaptiveThreshold(th,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,thresh1,thresh2) 

    #show filtered image
    cv2.imshow('BinaryThreshold',result)
    #waits for escape key then breaks out of loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

#close our display window     
cv2.destroyAllWindows()

https://github.com/owainlewis/awesome-artificial-intelligence

http://www.kdnuggets.com/2015/06/top-20-python-machine-learning-open-source-projects.html

from nltk.parse import stanford
from nltk import Tree
import os
import sys
import getopt

# sys.path.append('~/Downloads/en') # put where you downloaded the nodebox/linguistics

import en

from nltk.parse import stanford

# Put where you downloaded the stanford-parser-full...
os.environ['STANFORD_PARSER'] = '.' #'~/Downloads/stanford-parser-full-2015-04-20/'
os.environ['STANFORD_MODELS'] = '.' #'~/Downloads/stanford-parser-full-2015-04-20/'

smap = {}


class Node(list):
    def __init__(self, label):
        self.label = label
        self.prev = DummyNode()

    def set(self, key, value):
        self.append((key, value))
        if isinstance(value.prev, DummyNode):
            value.prev = self

    def get(self, key):
        for k, v in self:
            if key == k:
                return v
        return DummyNode()

    def complete(self, tokens, qtype):
        # print tokens
        if len(tokens) == 0:
            if qtype.lower() == "why":
                cur_node = self.get('because') or self.get('since')
                ret = [cur_node.label]

                cur_node = cur_node.get('.')
                prev_node = cur_node.prev
                while prev_node.label not in smap:
                    ret.append(prev_node.label)
                    prev_node = prev_node.prev
                ret.append(prev_node.label)

                while cur_node.label not in smap and len(cur_node) > 0:
                    ret.append(cur_node.label)
                    cur_node = cur_node[0][1]
                ret.append(cur_node.label)
                return ' '.join(ret)

            else:
                if self.label in smap:
                    return self.label
                if not isinstance(self.get('.'), DummyNode):
                    return self.get('.').label
                elif len(self) > 0:
                    return self[0][0] + " " + self[0][1].complete(tokens, qtype)
                else:
                    return "Unsure"
        else:
            token = get_word(tokens[0])
            if tokens[0].label() in ["VB", "VBD", "VBZ"]:
                token = get_root_word(token)
            if tokens[0].label() == "NP":
                return self.complete(tokens[1:], qtype)

            for k, v in self:
                if k == token:
                    return v.complete(tokens[1:], qtype)
            return "Answer unclear"

    def matches(self, tokens):
        # print tokens
        if len(tokens) == 0:
            return True

        if tokens[0].label() == "NP":
            if not isinstance(self.get('.'), DummyNode):
                return self.get('.').matches(tokens)
            if self.label != get_word(tokens[0]).upper():
                return False
            else:
                return self.matches(tokens[1:])

        token = get_word(tokens[0])
        if tokens[0].label() in ["VB", "VBD", "VBZ"]:
            token = get_root_word(token)

        for k, v in self:
            if k == token:
                return v.matches(tokens[1:])
        return False


class DummyNode(Node):

    def __init__(self):
        self.label = "Answer unclear"

    def get(self, key):
        return self

    def __nonzero__(self):
        return False


def get_word(tree):
    if isinstance(tree, Tree):
        words = []
        for child in tree:
            words.append(get_word(child))
        return ' '.join(words)
    else:
        return tree


def get_root_word(word):
    if word in ['is', 'was']:
        return 'is'
    return en.verb.present(word)


def get_node(label):
    if label not in smap:
        smap[label] = Node(label)
    return smap[label]


def flatten_tree(tree):
    # print tree
    if len(tree) > 0:
        if isinstance(tree[0], Tree):
            if isinstance(tree, Tree) and tree.label() == "NP":
                return [tree]
            tokens = []
            for child in tree:
                tokens += flatten_tree(child)
            return tokens
        else:
            return [tree]
    else:
        return []


def get_tokens(tokens):
    tokens = tokens[1:-1]
    ret = []
    start = 0
    stack = 0
    for i in xrange(len(tokens)):
        if tokens[i] == "(":
            if stack == 0:
                start = i
            stack += 1
        elif tokens[i] == ")":
            stack -= 1
            if stack < 0:
                print "Brack mismatch: " + str(tokens)
            if stack == 0:
                ret.append(get_tokens(tokens[start:i + 1]))
        else:
            if stack == 0:
                ret.append(tokens[i])
    if stack != 0:
        print "Bracket mismatch: " + str(tokens)
    return ret


def matches(match_str, tree):
    tokens = get_tokens(match_str.split())
    return match_tokens(tokens, tree)


def match_tokens(tokens, tree):

    if len(tokens) == 0:
        return True

    if tokens[0] is not '.' and tree.label() not in tokens[0].split('/'):
        return False

    if tokens[-1] == '$':
        if len(tree) != len(tokens[:-1]) - 1:
            return False
        else:
            tokens = tokens[:-1]

    if len(tree) < len(tokens) - 1:
        return False

    for i in xrange(len(tokens) - 1):
        if not match_tokens(tokens[i + 1], tree[i]):
            return False
    return True

# Returns subject


def describe(tree):

    if not isinstance(tree, Tree):
        print "ERROR"
    if tree.label() == "ROOT":
        describe(tree[0])
        return

    # Augment data
    if matches('( S ( NP ) ( VP ( VBP ) ( ADJP ) ) )', tree):
        _, subject = describe(tree[0])
        action = get_root_word(get_word(tree[1][0]))
        action_node = Node(action)
        adj = get_word(tree[1][1])
        adj_node = Node(adj)

    # Sentences
    if matches('( S ( NP ) ( VP ) )', tree):
        _, subject = describe(tree[0])
        action, action_node = describe(tree[1])

        subject.set(action, action_node)
        return action, action_node
    if matches('( S ( VP ) )', tree):
        return describe(tree[0])

    # NOUNS
    if matches('( NP )', tree):
        # Ex: The dog
        word = get_word(tree).upper()
        return word, get_node(word)

    # PROPOSITIONS
    if matches('( PP ( . ) ( NP ) )', tree):
        # to the mall
        # with her parents
        _, obj = describe(tree[1])
        prop = get_word(tree[0])

        return prop, obj
    if matches('( PRT )', tree):
        prt = get_word(tree)
        return prt, Node(prt)

    # VERBS
    if matches('( VP ( VBD ) ( VP ) $ )', tree):
        action = get_root_word(get_word(tree[0]))

        return action, Node(action)

    if matches('( VP ( VB/VBD ) $ )', tree):
        action = get_root_word(get_word(tree))
        return action, Node(action)

    if matches('( VP ( VB/VBZ/VBP/VPZ/VBD/VBG/VBN ) ( PP ) )', tree):
        action = get_root_word(get_word(tree[0]))
        action_node = Node(action)
        prop, prop_node = describe(tree[1])
        action_node.set(prop, prop_node)
        return action, action_node

    if matches('( VP ( VB/VBZ/VBP/VPZ/VBD/VBG/VBN ) ( PRT ) ( NP ) )', tree):
        action = get_root_word(get_word(tree[0]))
        action_node = Node(action)
        prt, prt_node = describe(tree[1])
        action_node.set(prt, prt_node)
        _, obj = describe(tree[2])
        prt_node.set('.', obj)
        return action, action_node

    if matches('( VP ( VB/VBZ/VBP/VPZ/VBD/VBG/VBN ) ( NP ) )', tree):
        action = get_root_word(get_word(tree[0]))
        action_node = Node(action)

        _, obj = describe(tree[1])
        action_node.set('.', obj)

        if matches('( VP ( VB/VBZ/VBP/VPZ/VBD/VBG/VBN ) ( NP ) ( PP ) )', tree):
            # Assume rest is PP
            for pp_node in tree[2:]:
                prop, prop_node = describe(pp_node)
                action_node.set(prop, prop_node)

        if matches('( VP ( VB/VBZ/VBP/VPZ/VBD/VBG/VBN ) ( NP ) ( SBAR ) )', tree):
            # SBAR at end
            sbar, sbar_node = describe(tree[2])
            action_node.set(sbar, sbar_node)


        return action, action_node

    if matches('( VP ( VB/VBZ/VBP/VPZ/VBD/VBG ) ( S ) )', tree):
        s, s_node = describe(tree[1])
        action = get_root_word(get_word(tree[0]))
        action_node = Node(action)

        action_node.set(s, s_node)
        return action, action_node

    if matches('( VP ( TO ) ( VP ) )', tree):
        to_node = Node('to')
        action, action_node = describe(tree[1])

        to_node.set(action, action_node)

        return 'to', to_node

    if matches('( VP ( VB/VBZ/VBP/VPZ/VBD/VBG/VBN ) ( ADJP ) )', tree):
        action = get_root_word(get_word(tree[0]))
        action_node = Node(action)

        adj = get_node(get_word(tree[1]))

        action_node.set('.', adj)
        return action, action_node
    if matches('( VP ( VB/VBZ/VBP/VPZ/VBD/VBG/VBN ) ( SBAR ) )', tree):
        action = get_root_word(get_word(tree[0]))
        action_node = Node(action)

        sbar, sbar_node = describe(tree[1])
        action_node.set(sbar, sbar_node)
        return action, action_node

    # SBAR
    if matches('( SBAR ( IN ) ( S ) )', tree):
        prop = get_word(tree[0])
        prop_node = Node(prop)
        s, s_node = describe(tree[1])

        prop_node.set('.', s_node)

        return prop, prop_node

    raise ValueError("ERROR reading " + str(tree))


def answer(tree):
    tree = tree[0]
    if tree.label() != "SBARQ":
        print "ERROR not a question: " + str(tree)
        return None

    # What did Mary / Where did Mary ( ... )
    if matches('( SBARQ ( WHNP/WHADVP ) ( SQ ( VBZ/VBD/VBP ) ( NP ) ) )', tree):

        qtype = get_word(tree[0])
        subject = get_word(tree[1][1]).upper()
        verb = get_root_word(get_word(tree[1][0]))

        if verb is 'is':
            return get_node(subject).get('is').complete([], qtype)
        else:
            tokens = flatten_tree(tree[1][2:])
            return get_node(subject).complete(tokens, qtype)

    # What has blue eyes
    if matches('( SBARQ ( WHNP ) ( SQ ( VP/VBZ ) ) )', tree):
        tokens = flatten_tree(tree[1])
        objs = []
        for obj in smap:
            if smap[obj].matches(tokens):
                objs.append(obj)

        if len(objs) == 0:
            return "Nothing"
        return ','.join(objs)

    print "ERROR answering"

def usage():
    print "Usage: " + sys.argv[0] + " [-d]"

def main(argv):

    debug = False

    try:
        opts, args = getopt.getopt(argv, "hd",["help","debug"])
    except getopt.GetoptError as e:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ["-h", "help"]:
            usage()
            sys.exit(2)
        if opt in ["-d", "debug"]:
            debug = True

    parser = stanford.StanfordParser()

    line = raw_input("Enter line: ")

    while line != 'stop':
        sent = list(parser.raw_parse(line))[0]
        if debug:
            print sent # print parse tree
        if sent[0].label() == "SBARQ":
            print answer(sent)
        else:
            try:
                describe(sent)
            except ValueError as e:
                print "Error describing sentence. " + e
            if debug:
                print smap # print semantic map
        line = raw_input("Enter line: ")


if __name__ == "__main__":
    main(sys.argv[1:])

# Example:
"""
Mary went sledding
Where did Mary go? sledding
The boy played soccer with a ball
What did the boy play? soccer
What did the boy play soccer with? a ball
Mary went to the mall
Where did Mary go? to the mall
Where did Mary go to? the mall
Mary likes eating peanuts
What does Mary like eating? peanuts
What does Mary like? eating peanuts
Mary likes to eat peanuts
What does Mary like? To eat peanuts
What does Mary like to eat? peanuts
Mark likes to smoke
What does Mary like? to smoke
Blueberries are blue
What color are blueberries? blue
James ran because James was scared
Why did James run? because James was scared
"""

https://github.com/berlius/artificial-intelligence

https://github.com/BotCube/awesome-bots

https://gitlab.idiap.ch/groups/bob

https://github.com/wayaai

http://www.dmoztools.net/Computers/Artificial_Intelligence/Machine_Learning/Software/

http://www.clips.ua.ac.be/pattern

#WORKING FINE
import cv2
import numpy as np

def callback(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('image')

ilowH = 0
ihighH = 179

ilowS = 0
ihighS = 255

ilowV = 0
ihighV = 255

# create trackbars for color change
cv2.createTrackbar('lowH','image',ilowH,179,callback)
cv2.createTrackbar('highH','image',ihighH,179,callback)

cv2.createTrackbar('lowS','image',ilowS,255,callback)
cv2.createTrackbar('highS','image',ihighS,255,callback)

cv2.createTrackbar('lowV','image',ilowV,255,callback)
cv2.createTrackbar('highV','image',ihighV,255,callback)



while(1):
    # get current positions of four trackbars
    lH = cv2.getTrackbarPos('lowH','image')
    hH = cv2.getTrackbarPos('highH','image')
    lS = cv2.getTrackbarPos('lowS','image')
    hS = cv2.getTrackbarPos('highS','image')
    lV = cv2.getTrackbarPos('lowV','image')
    hV = cv2.getTrackbarPos('highV','image')
    
    
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv', hsv)
    lower_hsv = np.array([lH, lS, lV])
    higher_hsv = np.array([hH, hS, hV])
    mask = cv2.inRange(hsv, lower_hsv, higher_hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('frame', frame)
    #print ilowH, ilowS, ilowV
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()


# Normalizing Filter
import cv2 as cv
img = cv2.imread('images/webcam-border.png')
#img = cv.imread(path)
newImage = img.copy()
newImage = cv.resize(newImage, (600, 600))
nim = cv.normalize(newImage, newImage, 20, 200, cv.NORM_MINMAX)
cv.imshow('orig', img)
cv.imshow('dst_rt', nim)
cv.waitKey(0)
cv.destroyAllWindows()

https://medium.com/technology-invention-and-more/how-to-build-a-simple-neural-network-in-9-lines-of-python-code-cc8f23647ca1

from numpy import exp, array, random, dot
training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
training_set_outputs = array([[0, 1, 1, 0]]).T
random.seed(1)
synaptic_weights = 2 * random.random((3, 1)) - 1
for iteration in xrange(10000):
    output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
print 1 / (1 + exp(-(dot(array([1, 0, 0]), synaptic_weights))))


from numpy import exp, array, random, dot


class NeuralNetwork():
    def __init__(self):
        # Seed the random number generator, so it generates the same numbers
        # every time the program runs.
        random.seed(1)

        # We model a single neuron, with 3 input connections and 1 output connection.
        # We assign random weights to a 3 x 1 matrix, with values in the range -1 to 1
        # and mean 0.
        self.synaptic_weights = 2 * random.random((3, 1)) - 1

    # The Sigmoid function, which describes an S shaped curve.
    # We pass the weighted sum of the inputs through this function to
    # normalise them between 0 and 1.
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # The derivative of the Sigmoid function.
    # This is the gradient of the Sigmoid curve.
    # It indicates how confident we are about the existing weight.
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # We train the neural network through a process of trial and error.
    # Adjusting the synaptic weights each time.
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in xrange(number_of_training_iterations):
            # Pass the training set through our neural network (a single neuron).
            output = self.think(training_set_inputs)

            # Calculate the error (The difference between the desired output
            # and the predicted output).
            error = training_set_outputs - output

            # Multiply the error by the input and again by the gradient of the Sigmoid curve.
            # This means less confident weights are adjusted more.
            # This means inputs, which are zero, do not cause changes to the weights.
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

            # Adjust the weights.
            self.synaptic_weights += adjustment

    # The neural network thinks.
    def think(self, inputs):
        # Pass inputs through our neural network (our single neuron).
        return self.__sigmoid(dot(inputs, self.synaptic_weights))


if __name__ == "__main__":

    #Intialise a single neuron neural network.
    neural_network = NeuralNetwork()

    print "Random starting synaptic weights: "
    print neural_network.synaptic_weights

    # The training set. We have 4 examples, each consisting of 3 input values
    # and 1 output value.
    training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_set_outputs = array([[0, 1, 1, 0]]).T

    # Train the neural network using a training set.
    # Do it 10,000 times and make small adjustments each time.
    neural_network.train(training_set_inputs, training_set_outputs, 10000)

    print "New synaptic weights after training: "
    print neural_network.synaptic_weights

    # Test the neural network with a new situation.
    print "Considering new situation [1, 0, 0] -> ?: "
    print neural_network.think(array([1, 0, 0]))














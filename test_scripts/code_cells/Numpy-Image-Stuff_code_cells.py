import cv2
from PIL import Image
import tensorflow as tf

!ls ../*.png

imagefile= "../sienfield.png"

imc = cv2.imread(imagefile) 
print(imc)

imagefile= "../sienfield.png"
imp = Image.open(imagefile)
pix_val = list(imp.getdata())
print(pix_val[:100])

from PIL import Image
newImg = Image.new('RGB', (10,10), "black")
pixels = newImg.load()
pixels[0,0] = (0,3,0)
newImg.save("point.jpg")
savedImage = Image.open("point.jpg")
pixelsSaved = savedImage.load()

print (pixels[0,0])
print (pixelsSaved[0,0])

savedImage

for i in range(100):
    print (pix_val[i])

!pwd

#!/usr/bin/env python3

import numpy as np
import cv2

# Load image in greyscale
imagefile = "../sienfield.jpg"
im = cv2.imread(imagefile, cv2.IMREAD_GRAYSCALE)
h, w = im.shape
print(h,w)
# Make empty white RGB canvas same size
# I don't think VideoWriter likes greyscale frames, only 3-channel ones
canvas = np.full((h,w,3), 255, np.uint8)

# Create video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output.mp4", fourcc, 30.0, im.shape)
VID = []
cnt = 0
for y in range(h):
    for x in range(w):

        # Copy a grey pixel from image to RGB canvas
        canvas[y,x,:] = im[y,x], im[y,x], im[y,x]
        data = canvas[y,x]
        VID.append(data)
        print(data)#im = Image.fromarray(data)
       # im.save("makevideo/"+str(cnt)+".jpg")
        # Write every 100th frame to video to speed it up
        if cnt % 100 ==  0:
            out.write(canvas)
        # Count frames
        cnt += 1
        

out.release()


print(len(VID))
print (455*415)

lst=['a','b','c']
print("Original list",lst)
new_lst=(','.join(lst))
print("After removing bracket",new_lst)


IMAGEdata = []
for line in VID:
    line0 = str(line)
    line0 = line0.replace("[","")
    line0 = line0.replace("]","")
    IMAGEdata.append(line0)
print (len(IMAGEdata))

from PIL import Image
from numpy import asarray
image = Image.open('flower/1.jpg')
#convert image to numpy array
data = asarray(image)
#data is array format of image


print(IMAGEdata[30:])

from PIL import Image
im = Image.fromarray(IMAGEdata)
im.save("makevideo/your_file.jpg")


#%%writefile sienfield.py
#!/usr/bin/env python3
################################################################################
# Run like this:
#
# ./sienfield.py | ffmpeg -y -f rawvideo -pix_fmt gray8 -video_size 400x400 -i - -c:v h264 -pix_fmt yuv420p video.mov
################################################################################

from PIL import Image
import sys
pixels =[]
# Load image in greyscale
imagefile = "../sienfield.jpg"
im = Image.open(imagefile).convert('L')
h, w = im.size
print(im.size)

# Make empty white canvas same size
canvas = Image.new('L', im.size, 'white')

cnt = 0
for y in range(h):
    for x in range(w):
        # Copy a pixel from image to canvas
        canvas.putpixel((x+cnt,y), im.getpixel((x,y)))
        pixels.append(im.getpixel((x,y)))
        canvas.save("makevideo/"+str(cnt)+".jpg")
        # Write every 100th frame to video to speed it up
        #if cnt % 100 ==  0:
        #    sys.stdout.buffer.write(canvas.tobytes())

        # Count frames
        cnt += 1


#%%writefile sienfield.py
#!/usr/bin/env python3
################################################################################
# Run like this:
#
# ./sienfield.py | ffmpeg -y -f rawvideo -pix_fmt gray8 -video_size 400x400 -i - -c:v h264 -pix_fmt yuv420p video.mov
################################################################################

from PIL import Image
import sys
pixels =[]
# Load image in greyscale
imagefile = "../sienfield.jpg"
im = Image.open(imagefile).convert('L')
h, w = im.size
print(im.size)

# Make empty white canvas same size
canvas = Image.new('L', im.size, 'white')

cnt = 0
for inc in range(h*w):
    x = cnt+1
    y = cnt

    # Copy a pixel from image to canvas
    print(x,y,end="-")
    canvas.putpixel((x,y), im.getpixel((x,y)))
    pixels.append(im.getpixel((x,y)))
    canvas.save("makevideo/"+str(cnt)+".jpg")
    if inc % 415 == 0:
        y = cnt
    cnt += 1


for i in range(0,100):
    if i % 25 ==0:print(i)

print (len(pixels))

from PIL import Image

def newImg():
    img = Image.new('RGB', (100, 100))
    
    img.putpixel((30,60), (155,155,55))
    img.save('sqr.png')

    return img

wallpaper = newImg()
wallpaper.show()

!mkdir makevideo

!./sienfield.py | ffmpeg -y -f rawvideo -pix_fmt gray8 -video_size 400x400 -i - -c:v h264 -pix_fmt yuv420p video.mp4

!chmod +x sienfield.py




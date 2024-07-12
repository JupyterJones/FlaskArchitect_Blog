import sys
import time
from PIL import Image, ImageChops, ImageEnhance, ImageFilter, ImageDraw, ImageFont 
from time import sleep
import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")


import time
timestr = time.strftime("%Y%m%d%H%M%S")
filename = "Image-Stuff-Files/"+timestr+'_.txt'
print (filename)

import sys
sys.path.insert(0, "Image-Stuff-Files")
import GraphicJunkdb

import time
timestr = time.strftime("%Y-%m-%d %H:%M:%S")
print timestr

# Create Image from Tuples

tupledlist=[(171, 46, 10)]
from PIL import Image
OUTPUT_IMAGE_SIZE = (100, 100)
for frame_number, color in enumerate(tupledlist):
    print (frame_number,color)
    image = Image.new('RGB', OUTPUT_IMAGE_SIZE, color=color)
    image.save("Image-Stuff-Files/path.png")

im = Image.open('Image-Stuff-Files/path.png')
im

image=Image.open("Image-Stuff-Files/path.png")
print(list(image.getdata()))

!wget -O Image-Stuff-Files/leaves.jpg https://jacknorthrup.com/image2/017.jpg

from PIL import Image
# create an empty list called Tuples
Tuples = []
# Open Image-Stuff-Files/leaves.jpg
im = Image.open("Image-Stuff-Files/leaves.jpg")
# Resize image to 400x400
im = im.resize((400,400), Image.BICUBIC)
# save the resized image
im.save("Image-Stuff-Files/LEAF.png")

# Open the resized image Image-Stuff-Files/leaves.jpg
image=Image.open("Image-Stuff-Files/LEAF.png") 
tup = (list(image.getdata()))
for line in tup:
    line = str(line)
    Tuples.append(line+",")
    
tup = (list(image.getdata()))
for line in tup:
    line = str(line)
    Tuples.append(line+",")

image=Image.open("Image-Stuff-Files/LEAF.png") 
tup = (list(image.getdata()))
print tup

from PIL import Image
Tuples = []

image=Image.open("Image-Stuff-Files/SMALL.jpg") 
tup = (list(image.getdata()))
for line in tup:
    line = str(line)
    Tuples.append(line+",")

from PIL import Image
f = open('Image-Stuff-Files/LEAFpng.txt', 'w')

# Open the resized image Image-Stuff-Files/leaves.jpg
image=Image.open("Image-Stuff-Files/LEAF.png") 
tup = (list(image.getdata()))
tup = str(tup)
f.write(tup)
f.close()

from PIL import Image
f = open('Image-Stuff-Files/LEAFpng.txt', 'r').read()
OUTPUT_IMAGE_SIZE = (400, 400)
image = Image.new('RGB', OUTPUT_IMAGE_SIZE, color='white')
# the eval() function changes the string to a tuple
image.putdata(eval(f))
image.save("Image-Stuff-Files/LEAFpng.png")
image

from PIL import Image
f = open('Image-Stuff-Files/LEAFpng.txt', 'r').read()
OUTPUT_IMAGE_SIZE = (800, 200)
image = Image.new('RGB', OUTPUT_IMAGE_SIZE, color='white')
# the eval() function changes the string to a tuple
image.putdata(eval(f))
image.save("Image-Stuff-Files/LEAFpng.png")
image

f = open('Image-Stuff-Files/Tuples.txt', 'w')
count = 0
for line in Tuples:
    count = count +1
All = count
print All
cnt = 0
for line in Tuples:
    f.write(line)
f.close()    

x= 600
y = x*x
print y

from PIL import Image
f = open('Image-Stuff-Files/Tuples.txt', 'r').read()
OUTPUT_IMAGE_SIZE = (50, 50)
image = Image.new('RGB', OUTPUT_IMAGE_SIZE, color='white')
# the eval() function changes the string to a tuple
image.putdata(eval(f))
image.save("Image-Stuff-Files/path2.png")
image
    

from PIL import Image
f = open('Image-Stuff-Files/small.txt', 'r').read()
OUTPUT_IMAGE_SIZE = (50, 50)
image = Image.new('RGB', OUTPUT_IMAGE_SIZE, color='white')
# the eval() function changes the string to a tuple
image.putdata(eval(f))
image.save("Image-Stuff-Files/path2.png")
image
    

import numpy as np
from PIL import Image
someimage = "Image-Stuff-Files/LEAF.png"
img = Image.open(someimage).convert('1', dither=Image.NONE)
a_img = np.asarray(img) * 255
b_img = abs(a_img - 255)  
img.putdata(b_img)
c_img = np.asarray(img) * 255
c_img

from PIL import Image
img2 = Image.open("Image-Stuff-Files/leaves.jpg")
img3 = img2.resize((400,400), Image.BICUBIC)
img3.save("Image-Stuff-Files/LEAF3.jpg")
img3.size
im = Image.open("Image-Stuff-Files/LEAF3.jpg")
im

import numpy as np
from PIL import Image
img2 = Image.open('Image-Stuff-Files/leaves.jpg')
img3 = img2.resize((400,400), Image.BICUBIC)
img3.save('Image-Stuff-Files/leaf.jpg')
img2 = Image.open('Image-Stuff-Files/leaf.jpg').convert('1', dither=Image.NONE)
img3 = img2.resize((400,400), Image.BICUBIC)
OUTPUT_IMAGE_SIZE = (400, 400)
img = Image.new('RGB', OUTPUT_IMAGE_SIZE, color='white')
a_img = np.asarray(img3) * 255
# do some stuff with buffer
a_img = abs(a_img - 255)  
img.putdata(a_img.flatten())
img

import numpy as np
from PIL import Image
img2 = Image.open("Image-Stuff-Files/leaves.jpg")
img3 = img2.resize((50,50), Image.BICUBIC)
img3.save("Image-Stuff-Files/leaf50.jpg")
img2 = Image.open("Image-Stuff-Files/leaf50.jpg").convert('1', dither=Image.NONE)
img3 = img2.resize((50,50), Image.BICUBIC)
OUTPUT_IMAGE_SIZE = (50, 50)
img = Image.new('RGB', OUTPUT_IMAGE_SIZE, color='white')
a_img = np.asarray(img3) * 255
# do some stuff with buffer
a_img = abs(a_img - 255)
print (a_img)
img.putdata(a_img.flatten())
img.save("Image-Stuff-Files/SMALL.jpg")

from PIL import Image
img = Image.open("Image-Stuff-Files/SMALL.jpg")
img

from PIL import Image
Tuples = []

image=Image.open("Image-Stuff-Files/SMALL.jpg") 
tup = (list(image.getdata()))
for line in tup:
    line = str(line)
    Tuples.append(line+",")

list_of_pixels = list(im.getdata())
# Do something to the pixels...
im2 = Image.new(im.mode, im.size)
im2.putdata(list_of_pixels)
im2.save("Image-Stuff-Files/list_of_pixels.jpg")
im2

f = open('Image-Stuff-Files/Tuples.txt', 'w')
count = 0
for line in Tuples:
    count = count +1
All = count
print All
cnt = 0
for line in Tuples:
    cnt = cnt +1
    line = line.replace('\n', '')
    f.write(line)
f.close()    

from PIL import Image
Tuples = []

image=Image.open("Image-Stuff-Files/SMALL.jpg") 
tup = (list(image.getdata()))
for line in tup:
    line = str(line)
    Tuples.append(line+",")

from PIL import Image
f = open('Image-Stuff-Files/small.txt', 'r').read()
OUTPUT_IMAGE_SIZE = (50, 50)
image = Image.new('RGB', OUTPUT_IMAGE_SIZE, color='white')
# the eval() function changes the string to a tuple
image.putdata(eval(f))
image.save("Image-Stuff-Files/path2.png")
image
    



from PIL import Image
img = Image.open("Image-Stuff-Files/SMALL.jpg")
list_of_pixels = list(img.getdata())
# Do something to the pixels...
im2 = Image.new(img.mode, img.size)
im2.putdata(list_of_pixels)
im2

f = open('Image-Stuff-Files/small.txt', 'w')
from PIL import Image
img = Image.open("Image-Stuff-Files/SMALL.jpg")
list_of_pixels = list(img.getdata())
list_of_pixels = str(list_of_pixels)
f.write(list_of_pixels)

from PIL import Image
f = open('Image-Stuff-Files/small.txt', 'r').read()
print f

from PIL import Image
f = open('Image-Stuff-Files/small.txt', 'r').read()
OUTPUT_IMAGE_SIZE = (50, 50)
image = Image.new('RGB', OUTPUT_IMAGE_SIZE, color='white')
# the eval() function changes the string to a tuple
image.putdata(eval(f))
image.save("Image-Stuff-Files/path2.png")
image
    

!wget -O Image-Stuff-Files/STAMP.jpg https://jacknorthrup.com/postoids/postoid%20%285%29.jpg

from PIL import Image
Tuples = []
im = Image.open("Image-Stuff-Files/STAMP.jpg")
#im = im.resize((400,400), Image.BICUBIC)
im.save("Image-Stuff-Files/stamp.png")
w,h = im.size


image=Image.open("Image-Stuff-Files/stamp.png")

tup = (list(image.getdata()))
for line in tup:
    line = str(line)
    Tuples.append(line+",")
    
#tup = (list(image.getdata()))
#for line in tup:
#    line = str(line)
#    Tuples.append(line+",")
    
f = open('Image-Stuff-Files/Tuples1.txt', 'w')
count = 0
for line in Tuples:
    count = count +1
All = count
print All
cnt = 0
for line in Tuples:
    f.write(line)
f.close()        

f = open('Image-Stuff-Files/Tuples1.txt', 'r').read()
print len(f)
OUTPUT_IMAGE_SIZE = (w, h)
image = Image.new('RGB', OUTPUT_IMAGE_SIZE, color='white')
# the eval() function changes the string to a tuple
image.putdata(eval(f))
print image.size
image.save("Image-Stuff-Files/path3.png")
image    

LST = []
f = open('Image-Stuff-Files/Tuples.txt', 'r').readlines()
LST.append(f)

from random import randint 
from PIL import Image, ImageColor
col = str(randint(1,255))
im = Image.new("RGB", (32, 32), ImageColor.getrgb("rgb("+col+", 216, 230)"))
im.save('Image-Stuff-Files/simplePixel.png')
im

from PIL import Image, ImageColor
col0 = str(randint(1,255));col1 = str(randint(1,255));col3 = str(randint(1,255))
im = Image.new("RGB", (32, 32), ImageColor.getrgb("rgb("+col0+","+col1+","+col3+")"))
               
im.save('Image-Stuff-Files/simplePixel.png')
im

print "".join(Tuples)

image.putdata(tupledlist)
image.save("Image-Stuff-Files/path2.png")
image
    

from PIL import Image, ImageColor
from random import randint
for x in range(1024):
    col = randint(1, 255)
    #color = ("rgb("+str(col)+", 216, 230)")
    color = ('rgb(20,150,150)')
    im = Image.new("RGB", (132, 132), ImageColor.getrgb(color))
    im.save('Image-Stuff-Files/simplePixel.png')
    im

!showme Image-Stuff-Files/simplePixel.png

#Note r g b values are 0, 255,0* 
from PIL import Image
img = Image.new('RGB', [50,50], 0x000000)
color = (20, 255, 255)

img.putpixel((10,15),(color))   
img.save('Image-Stuff-Files/lolmini2.jpg')
img

#Note r g b values are 0, 255,0* 
from PIL import Image
import math
inc = 0
img = Image.new('RGB', [640,640], 0x000000)
color = (0, 0, 55)
colors = (50, 25, 255)
for x in range(640):
    for y in range(640):
        #print x,y
        inc = inc+1
        if math.cos(float(x+inc)) >= math.cos(float(y+inc**2)):
            img.putpixel((x,y),(color))
        if math.cos(float(x+inc**3)) >= math.cos(float(y+inc**2)):
            img.putpixel((x,y),(colors))       
img.save('Image-Stuff-Files/denim2.jpg')
img
        

#Note r g b values are 0, 255,0* 
from PIL import Image
import math
inc = 0
TOT = []
img = Image.new('RGB', [300,300], 0x000000)
color = (0, 0, 55)
colors = (50, 25, 255)
colorw = (255, 225, 0)
for x in range(300):
    for y in range(300):
        #print x,y
        inc = inc+1
        if math.cos(float(x+inc)) >= math.cos(float(y+inc**2)):
            img.putpixel((x,y),(color))
        if math.cos(float(y+inc**3)) >= math.cos(float(x+inc)):
            img.putpixel((x,y),(colors))
        #if math.cos(float(x+inc**3))+ math.cos(float(y+inc**2))==0:
        if (math.cos(float(x))+ math.cos(float(y**2))) >0 and (math.cos(float(x))+ math.cos(float(y**2)))<.21:
            img.putpixel((x,y),(colorw))             
            
            
img.save('Image-Stuff-Files/denim2l.jpg')
img
        

#Note r g b values are 0, 255,0* 
from PIL import Image
import math
inc = 0
TOT = []
size = 500
img = Image.new('RGB', [size,size], 0x000000)
color = (0, 0, 55)
colors = (250, 25, 255)
colorw = (255, 225, 0)
for x in range(size):
    for y in range(size):
        #print x,y
        inc = inc+1
        if math.cos(float(x+inc)) >= math.cos(float(y+inc**2)):
            img.putpixel((x,y),(color))
        if math.cos(float(x+inc**3)) >= math.cos(float(y+inc**2)):
            img.putpixel((x,y),(colors))
        #if math.cos(float(x+inc**3))+ math.cos(float(y+inc**2))==0:
        if (math.cos(float(x))+ math.cos(float(y))) >-.02 and (math.cos(float(x))+ math.cos(float(y)))<.085:
            img.putpixel((x,y),(colorw))
img.save('Image-Stuff-Files/denim2r.jpg')
img
# if (math.cos(float(x))+ math.cos(float(y))) >-.25 and (math.cos(float(x))+ math.cos(float(y)))<.25:
# if (math.cos(float(x))+ math.cos(float(y))) >-.05 and (math.cos(float(x))+ math.cos(float(y)))<.05:
# if (math.cos(float(x))+ math.cos(float(y))) >-.015 and (math.cos(float(x))+ math.cos(float(y)))<.015:
# if (math.cos(float(x))+ math.cos(float(y))) >-.02 and (math.cos(float(x))+ math.cos(float(y)))<.085:

#Note r g b values are 0, 255,0* 
from PIL import Image
import math
inc = 0
TOT = []
size = 500
img = Image.new('RGB', [size,size], 0x000000)
color = (0, 0, 55)
colors = (50, 25, 255)
colorw = (255, 225, 0)
for x in range(size):
    for y in range(size):
        #print x,y
        inc = inc+1
        if math.cos(float(x+inc)) >= math.cos(float(y+inc**2)):
            img.putpixel((x,y),(color))
        if math.cos(float(x+inc**3)) >= math.cos(float(y+inc**2)):
            img.putpixel((x,y),(colors))
        #if math.cos(float(x+inc**3))+ math.cos(float(y+inc**2))==0:
        if (math.cos(float(x))+ math.cos(float(y))) >-.015 and (math.cos(float(x))+ math.cos(float(y)))<.015:
            img.putpixel((x,y),(colorw))
img.save('Image-Stuff-Files/denim2B.jpg')
img
# if (math.cos(float(x))+ math.cos(float(y))) >-.25 and (math.cos(float(x))+ math.cos(float(y)))<.25:
# if (math.cos(float(x))+ math.cos(float(y))) >-.05 and (math.cos(float(x))+ math.cos(float(y)))<.05:
# if (math.cos(float(x))+ math.cos(float(y))) >-.015 and (math.cos(float(x))+ math.cos(float(y)))<.015:
# if (math.cos(float(x))+ math.cos(float(y))) >-.02 and (math.cos(float(x))+ math.cos(float(y)))<.085:

#Note r g b values are 0, 255,0* 
from PIL import Image
import math
inc = 0
img = Image.new('RGB', [640,640], 0x000000)
color = (50, 255, 255)
colors = (50, 25, 255)
for x in range(640):
    for y in range(640):
        #print x,y
        inc = inc+1
        if math.cos(float(x+inc)) >= math.cos(float(y+inc**2)):
            img.putpixel((x,y),(color))
        if math.cos(float(x+inc**3)) >= math.cos(float(y+inc**2)):
            img.putpixel((x,y),(colors))       
img.save('Image-Stuff-Files/denim03.jpg')
img
        

import os
import os.path
title = 'Image-Stuff-Files/ipynb-list.txt'
f= open(title,'a')
f.close()
count=0
for dirpath, dirnames, filenames in os.walk('/home/conda'):
    for filename in [f for f in filenames if f.endswith('.ipynb')]:
        count=count+1
        Path = os.path.join(dirpath, filename)
        with open(title, 'a') as outfile:
            path = Path+'\n'
            outfile.write(path)

%%writefile Image-Stuff-Files/NED
#!/usr/local/bin/python
import sys
import sqlite3
conn = sqlite3.connect("/home/TEMP/Databases/NED.db")
conn.text_factory = str
c = conn.cursor()
if len(sys.argv) < 3:
    print "\n*****************************************"
    print "Not enough options were passed."     
    print "NED requires 2 arguments. the first -H , -R , -I , -D or -S .\nThe second can be a period."
    print "If printing the database -T also add a filename of your choice ( no quotes required ):"
    print " Example: NED -T Data2Text.txt"   
    print "If wanting to read all entries use -R . (use the period)" 
    print "even use the period with help.  -H .   must be entered."
    print "*****************************************\n"
    sys.exit()
mod = sys.argv[1]
def create():
    import sqlite3
    conn = sqlite3.connect("/home/TEMP/Databases/NED.db")
    conn.text_factory = str
    c = conn.cursor()
    c.execute("CREATE VIRTUAL TABLE PROJECT using FTS4 (input)")
    conn.commit()
    text = "Database Created"
    return text

def insert(data,conn=conn, c=c):
    c.execute("INSERT into PROJECT values (?)", (data,))
    for row in c.execute("SELECT ROWID,* FROM PROJECT ORDER BY ROWID DESC LIMIT 1"):
        print "\nPOST VERIFIED:\n",row[0],row[1]
    conn.commit()
    conn.close()
    return data

def search(data,conn=conn, c=c):
    for row in c.execute("SELECT ROWID,* FROM PROJECT WHERE input MATCH ?",(data,)):
        print "\nINFO Found Here:\n",row[0],row[1]
    conn.commit()
    conn.close()
    return data

def delete(rowid,conn=conn, c=c):
    c.execute("DELETE FROM PROJECT WHERE rowid = ?", (rowid,))
    conn.commit()
    conn.close()
    text = "ROWID "+rowid+" Deleted"
    return text

def main():
    conn = sqlite3.connect("/home/TEMP/Databases/NED.db")
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        print row[0],": ",row[1]
        
def Dsearch():
    conn = sqlite3.connect("/home/TEMP/Databases/NED.db")
    conn.text_factory = str
    search = raw_input("Detail Search: ")
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        if search in row[1]:
            print row[0],": ",row[1] 

def prtmain(filename):
    fn = open(filename, "w")
    conn = sqlite3.connect("/home/TEMP/Databases/NED.db")
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        TEXT = "id:"+str(row[0])+"\n"+str(row[1])
        TEXT = str(TEXT)
        TEXT = TEXT.replace('\\n','\n')
        TEXT = "".join(TEXT)
        fn.write(TEXT+'\n----\n')

def HELP():
    TXT = """
    USE: NED argv[1] argv[2]
    argv[1] sets the mod:
    -I insert / -D delete / -R read / -H help
    examples:
    Notice the entry is in parenthese.
    -I  to insert "STUFF to be inserted"
    NED -I "STUFF to be inserted"
    -D to delete where rowid is 3
    NED -D 3
    Notice the period after -R . 
    -R . read all
    To search for the term "current project"
    NED -S current project
    -S "current project"
    To 'EXACT DETAIL' search" Notice the period after -DS
    NED -DS .
    -H help on options
    NED -H .
    """
    print TXT

if mod == "-H" or mod == "h":
    HELP()        
if mod == "-R":
    main()
if mod == "-I":
    data = sys.argv[2]
    insert(data)
if mod == "-D":
    rowid = sys.argv[2]
    delete(rowid) 
if mod == "-S":
    data = sys.argv[2]
    search(data)
if mod == "-DS":
    print ("Exact Text SEARCH.")
    Dsearch()
if mod == "-T":
    filename = sys.argv[2]
    prtmain(filename)
if mod == "-CREATE":
    create()
    print create
else:
    print "_________________\n"
    print sys.argv[2],"Command Completed"
    

%%writefile Image-Stuff-Files/GraphicJunkdb.py
def getcolumns(database='db.sqlite3'):
    import sqlite3
    conn = sqlite3.connect(database)
    c = conn.cursor()
    print ('Verify All Data')
    print("----------------")
    cursor01 = c.execute('select * from pixel')
    #cursor.description is description of columns
    names1 = list(map(lambda x: x[0], cursor01.description))
    print("Table: pixel         Columns:",names1)
    cursor02 = c.execute('select * from tupples')
    names2 = list(map(lambda x: x[0], cursor02.description))
    print("Table: tupples       Columns:",names2)
    cursor03 = c.execute('select * from alpha')
    names3 = list(map(lambda x: x[0], cursor03.description))
    print("Table: alpha         Columns:",names3)
    cursor04 = c.execute('select * from XY')
    names4 = list(map(lambda x: x[0], cursor04.description))
    print("Table: XY            Columns:",names4)
    cursor05 = c.execute('select * from NOTES')
    names5 = list(map(lambda x: x[0], cursor05.description))
    print("Table: notes          Columns:",names5)
    cursor06 = c.execute('select * from CODE')
    names6 = list(map(lambda x: x[0], cursor06.description))
    print("Table: CODE         Columns:",names6)
    cursor07 = c.execute('select * from association')
    names7 = list(map(lambda x: x[0], cursor07.description))
    print("Table: association         Columns:",names7)    
    
if __name__ == "__main__":
    getcolumns()
    

print "finished"


!ls *.png

%%writefile test2.png
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABAAAAAIACAYAAAAczR65AAAgAElEQVR4Xly9SZNt23qeNbOu9t7n3ApZFVbY90pAmHAPOv4pkvgvNG1kaNEiggZNHEEQQYMIoGMiANshCRsb5GsJCwmLq3ule4qdO6u1MpP3ed5vrNx27pMnVzHnmGN8dTW+cfQ3f/s/fr3fvtzuHx+2l+PjbTs62l63/PHftr28vvDRth2

def cvt_2_base64(file_name):
    with open(file_name , "rb") as image_file :
        data = base64.b64encode(image_file.read())
    return data.decode('utf-8')

file_name= "2color-20x20.png"
cvt_2_base64(file_name)

my_str = 'hello '

my_bytes = b'James Doe'
print(my_bytes)
result = my_str.encode('utf-8') + my_bytes

print(result)  # 👉️ b'hello James Doe'

import struct
var = struct.pack('hhl', 5, 10, 15)
print(var)
print(struct.unpack('hhl', var))

import struct
# ctypes is imported to create a string buffer
import ctypes

# As shown in previous example
size = struct.calcsize('hhl')
print(size)

# Buffer 'buff' is created from ctypes
buff = ctypes.create_string_buffer(size)

# struct.pack_into() packs data into buff and it doesn't return any value
# struct.unpack_from() unpacks data from buff, returns a tuple of values
print(struct.pack_into('hhl', buff, 0, 5, 10, 15))
print(struct.unpack_from('hhl', buff, 0))

@reboot /usr/local/bin/screen

# Exploration in PNG
#
# Just poking through the PNG file structure.
#
# Found weird output when examining MacOS screenshots. They contain an
# "iDOT" chunk, the purpose of which I couldn't determine. This chunk type
# is not part of the PNG standard, and seems to break some programs'
# ability to process these files, according to complaints I'm finding on
# Google. See sample output below. If no one's already done it, maybe there
# is some value in writing e script to strip out these invalid iDOT chunks.

import sys, struct

filename = "2color-20x20.png"
fh = open(filename, 'rb')

chunksize = 1

# The first eight bits on a PNG are always these:
first_eight = [137,80,78,71,13,10,26,10]
valid_count = 0;
i = 0
while i < 8:
    first_byte = fh.read(chunksize)
    val = struct.unpack('B',first_byte)[0]
    if first_eight[i] == val:
        valid_count += 1
    else:
        print ("ERROR: Invalid PNG signature")
        exit(-1)
    i += 1;

if valid_count == 8:
    print ("Valid PNG signature")

# Process the image header chunk to output some useful file info.
# I didn't make special functions for any other chunk type
def process_ihdr():
    # The ! is necessary because PNGs being Portable "NETWORK" Graphics use
    # network byte ordering (which is big-endian). 
    width = struct.unpack('!I', fh.read(4))[0]
    print ("width: ", width)
    height = struct.unpack('!I', fh.read(4))[0]
    print ("height: ", height)
    bit_depth = struct.unpack('B', fh.read(1))[0]
    colour_type = struct.unpack('B', fh.read(1))[0]
    compression_method = struct.unpack('B', fh.read(1))[0]
    filter_method = struct.unpack('B', fh.read(1))[0]
    interlace_method = struct.unpack('B', fh.read(1))[0]
    print ("bit_depth: ", bit_depth)
    print ("colour_type: ", colour_type)
    print ("compression_method: ", compression_method)
    print ("filter_method: ", filter_method)
    print ("interlace_method: ", interlace_method)
    fh.read(4)

# Process all the chunks and print a summary of each. 
idats_found = 0
idats_bytes = 0
while (True):
    chlen = fh.read(4)
    #chlen.encode('utf-8')
    print(chlen)

    if chlen == "":
        break

    chunk_length = struct.unpack('!I',chlen)[0]

    chunk_type = ""
    for i in range(4):
        #chunk_type.encode('utf-8') 
        #chunk_type += (struct.unpack('c',fh.read(1))[0])
        #chunk_type += (struct.unpack('c'))#,fh.read(1))[0])
    # Instead of printing the same report for each IDAT chunk, just
    # print a summary at the end, to reduce flooding your console
    if (chunk_type != "IDAT"):
        print("It is IDAT")
        print ("=" * 20)
        print ("chunk_length: " + str(chunk_length))    
        print ("chunk_type: ", chunk_type)
    else:
        idats_found += 1
        idats_bytes += chunk_length

    if (chunk_type == "IHDR"):
        process_ihdr()
    else:
        data = fh.read(chunk_length)
        crc = fh.read(4)

print ("=" * 20)
print ("Found a total of " + str(idats_found) + " IDAT chunks consuming " + str(idats_bytes) + " bytes.")

# Close the file
fh.close()


import base64
msg = bytes("SGVsbG8gd29ybGQh", encoding='utf-8')
decoded = base64.b64decode(msg)
print(decoded.decode('utf-8'))

import base64
msg = "Hello world!"
encoded = base64.b64encode(bytes(msg, encoding='utf-8'))
print(encoded.decode('utf-8'))

#with open('2color-20x20.png', 'r', encoding='utf-8') as f:
with open('2color-20x20.png', 'r', encoding= 'ISO-8859-1') as f:    
    # ✅ get list of all lines
    lines = f.read()
    print(lines)
       

# For both Python 2.7 and Python 3.x
import base64
with open("imageToSave-junk.png", "wb") as f:
    f.write(base64.decodebytes(Data.encode()))

with open('test2.png', 'r', encoding='utf-8') as f:
    # ✅ get list of all lines
    lines = f.readlines()
    for line in lines:
        Data =line[22:]
        

import base64
with open("/home/jack/Downloads/image.png", "r") as fh:
    lines = fh.readlines()
    for line in lines:
        Data =line[22:]
        image_data = base64.decodebytes(Data.encode())

# For both Python 2.7 and Python 3.x
import base64
with open("imageToSave.png", "wb") as f:
    f.write(base64.decodebytes(Data.encode()))

# For both Python 2.7 and Python 3.x
import base64
with open("imageToSave2.png", "wb") as f:
    f.write(image_data)

from PIL import Image
im = Image.open("imageToSave2.png")
im

from PIL import Image
im = Image.open("imageToSave.png")
print (im.size)
im

!pwd

DATA = base64.decodebytes(Data.encode())

from PIL import Image
import io

image_data = Data # byte values of the image
image = Image.open(io.BytesIO(DATA))
image.show()

https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes

Modes

The mode of an image is a string which defines the type and depth of a pixel in the image. Each pixel uses the full range of the bit depth. So a 1-bit pixel has a range of 0-1, an 8-bit pixel has a range of 0-255 and so on. The current release supports the following standard modes:

        1 (1-bit pixels, black and white, stored with one pixel per byte)

        L (8-bit pixels, black and white)

        P (8-bit pixels, mapped to any other mode using a color palette)

        RGB (3x8-bit pixels, true color)

        RGBA (4x8-bit pixels, true color with transparency mask)

        CMYK (4x8-bit pixels, color separation)

        YCbCr (3x8-bit pixels, color video format)

            Note that this refers to the JPEG, and not the ITU-R BT.2020, standard

        LAB (3x8-bit pixels, the L*a*b color space)

        HSV (3x8-bit pixels, Hue, Saturation, Value color space)

        I (32-bit signed integer pixels)

        F (32-bit floating point pixels)


Since strings because Unicode in Python 3, I think you'll need to use Image.frombytes() to do the same thing. – 
martineau
Apr 29 at 12:11
Note that you can convert a Python 3 string into bytes via my_string.encode('latin1')

PIL.Image.frombytes(mode, size, data, decoder_name='raw', *args)

img = Image.frombytes('RGB', (1024, 512), Data, 'RGB', 'F;16')

img = Image.frombytes('RGB', (1024, 512), Data, 'raw', 'F;16')

img = Image.fromstring('L', (1024, 512), Data, 'raw', 'F;16')

rawData = open("foo.raw" 'rb').read()
imgSize = (h,w)
img = Image.fromstring('L', imgSize, rawData, 'raw', 'F;16')
img.save("foo.png")

from PIL import Image
from PIL.PngImagePlugin import PngInfo

targetImage = Image.open("pathToImage.png")

metadata = PngInfo()
metadata.add_text("MyNewString", "A string")
metadata.add_text("MyNewInt", str(1234))

targetImage.save("NewPath.png", pnginfo=metadata)
targetImage = Image.open("NewPath.png")

print(targetImage.text)


!python mosaic.py /home/jack/Desktop/imagebot/instagram/Symbiosis01imploded.png circles/resize

import PIL
from PIL import Image
im=Image.open('myra002.jpg')
im

import PIL
from PIL import Image
im=Image.open('myra002.jpg')
im2 = im.resize((640,640), Image.ANTIALIAS)
im2.save('new_002.jpg')
im2

import PIL
from PIL import Image
im=Image.open('man003.jpg')
im.size
im

This notebook makes a module to create a graphic mosaic. Graphic files created by make_tiles.py 
can used in mosaic.py to create a mosaic. The names of the graphic images are the based on time of creation.

import matplotlib

!cp Immanip/datename.py Mosaics

%%writefile Mosaics/__init__.py
#"Ver.2""

%%writefile Mosaics/make_tiles.py
#!/usr/local/bin/python
#GOOD DO NOT TOUCH
def maketiles(quantity):
    from PIL import Image
    from PIL import ImageDraw
    from random import randint
    from Mosaics import datename
    from time import sleep
    counter = 0
    while counter <= quantity:
        #Bcolor = (randint(0, 255), randint(0, 255), randint(0, 255))
        Bcolor = (randint(10, 155), randint(11, 155), randint(1, 155))
        im = Image.new('RGB', (50,50), (Bcolor))
        transparent_area = (randint(0, 50), randint(0, 50), randint(5, 50), randint(5, 50))

        mask=Image.new('1', im.size, color=255)
        draw=ImageDraw.Draw(mask) 
        draw.rectangle(transparent_area, fill=0)
        im.putalpha(mask)

        color2 = (randint(0, 155), randint(0, 155), randint(0, 155))
        overlay = Image.new('RGB', (50,50), (color2))

        sav = Image.composite(im, overlay, im)
        sleep(1)
        filename = "mosaic/"+datename.date_name()
        sav.save(filename)

        h = randint(15, 20)
        v = randint(25, 50)
        color = (randint(10, 155), randint(0, 155), randint(10, 155))

        im = Image.new('RGB', (50,50), (color))
        x, y =  im.size
        eX, eY = h, v #Size of Bounding Box for ellipse
        bbox =  (x/2 - eX/2, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
        draw = ImageDraw.Draw(im)
        color2 = (randint(2, 155), randint(2, 155), randint(2, 155))
        draw.ellipse(bbox, fill=color2)
        sleep(1)
        filename = "mosaic/"+datename.date_name()
        im.save(filename)

        counter = counter +1
        

#%%writefile trans.py
#!/usr/local/bin/python
#GOOD DO NOT TOUCH
def maketiles(quantity):
    from PIL import Image
    from PIL import ImageDraw
    from random import randint
    import sys
    from Mosaics import datename
    from time import sleep
    counter = 0
    while counter <= quantity:
        #Bcolor = (randint(0, 255), randint(0, 255), randint(0, 255))
        Bcolor = (randint(10, 155), randint(11, 155), randint(1, 155))
        im = Image.new('RGBA', (35,35), (Bcolor))
        #transparent_area = (randint(0, 50), randint(0, 50), randint(5, 50), randint(5, 50))
        transparent_area = 0,0,50,50
        mask=Image.new('1', im.size, color=255)
        draw=ImageDraw.Draw(mask) 
        draw.rectangle(transparent_area, fill=0)
        im.putalpha(mask)

        color2 = (randint(0, 155), randint(0, 155), randint(0, 155))
        overlay = Image.new('RGBA', (50,50), (color2))

        sav = Image.composite(im, overlay, im)
        sleep(1)
        filename = "mosaic/"+datename.date_name()
        sav.save(filename)

        h = randint(15, 20)
        v = randint(25, 50)
        h = 35
        v = 35
        #color = (randint(10, 155), randint(0, 155), randint(10, 155))
        color = 255, 0, 0
        #im = Image.new('RGB', (50,50), (color))
        im = Image.new('RGBA', (50,50))
        x, y =  im.size
        eX, eY = h, v #Size of Bounding Box for ellipse
        bbox =  (x/2 - eX/2, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
        draw = ImageDraw.Draw(im)
        color2 = (randint(2, 155), randint(2, 155), randint(2, 155))
        draw.ellipse(bbox, fill=color2)
        sleep(1)
        filename = "circles/TEST_"+datename.date_name()
        im.save(filename)

        counter = counter +1
maketiles(500)        

!mkdir circles/resize

#%%writefile trans.py
#!/usr/local/bin/python
#GOOD DO NOT TOUCH
def maketiles(quantity):
    from PIL import Image
    from PIL import ImageDraw
    from random import randint
    import sys
    sys.path.insert(0, "/home/jack/Desktop/deep-dream-generator/notebooks")
    from Mosaics import datename
    from time import sleep
    counter = 0
    while counter <= quantity:
        #Bcolor = (randint(0, 255), randint(0, 255), randint(0, 255))
        Bcolor = (randint(10, 155), randint(11, 155), randint(1, 155))
        im = Image.new('RGBA', (35,35), (Bcolor))
        #transparent_area = (randint(0, 50), randint(0, 50), randint(5, 50), randint(5, 50))
        transparent_area = 0,0,50,50
        mask=Image.new('1', im.size, color=255)
        draw=ImageDraw.Draw(mask) 
        draw.rectangle(transparent_area, fill=0)
        im.putalpha(mask)

        color2 = (randint(0, 155), randint(0, 155), randint(0, 155))
        overlay = Image.new('RGBA', (50,50), (color2))

        sav = Image.composite(im, overlay, im)
        sleep(1)
        filename = "mosaic/"+datename.date_name()
        sav.save(filename)

        h = randint(15, 20)
        v = randint(25, 50)
        h = 35
        v = 35
        #color = (randint(10, 155), randint(0, 155), randint(10, 155))
        color = 255, 0, 0
        #im = Image.new('RGB', (50,50), (color))
        im = Image.new('RGBA', (50,50))
        x, y =  im.size
        eX, eY = h, v #Size of Bounding Box for ellipse
        bbox =  (x/2 - eX/2, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
        draw = ImageDraw.Draw(im)
        color2 = (randint(2, 155), randint(2, 155), randint(2, 155))
        draw.ellipse(bbox, fill=color2)
        sleep(1)
        filename = "circles/TEST_"+datename.date_name()
        im.save(filename)

        counter = counter +1
maketiles(500)        

#%%writefile trans.py
#!/usr/local/bin/python
#GOOD DO NOT TOUCH
def maketiles(quantity):
    from PIL import Image
    from PIL import ImageDraw
    from random import randint
    import sys
    sys.path.insert(0, "/home/jack/Desktop/deep-dream-generator/notebooks")
    from Mosaics import datename
    from time import sleep
    counter = 0
    while counter <= quantity:
        Bcolor = (randint(0, 255), randint(0, 255), randint(0, 255))
        #Bcolor = (randint(10, 155), randint(11, 155), randint(1, 155))
        im = Image.new('RGBA', (35,35), (Bcolor))
        #transparent_area = (randint(0, 50), randint(0, 50), randint(5, 50), randint(5, 50))
        transparent_area = 0,0,35,35
        mask=Image.new('1', im.size, color=255)
        draw=ImageDraw.Draw(mask) 
        draw.rectangle(transparent_area, fill=0)
        im.putalpha(mask)

        #color2 = (randint(0, 155), randint(0, 155), randint(0, 155))
        #color2 = (randint(0, 255), randint(0, 255), randint(0, 255))
        color2 = (randint(45, 135), randint(45, 135), randint(45, 135))
        overlay = Image.new('RGBA', (35,35), (color2))

        sav = Image.composite(im, overlay, im)
        sleep(1)
        filename = "mosaic/"+datename.date_name()
        sav.save(filename)

        
        h = 35
        v = 35
        #color = (randint(10, 155), randint(0, 155), randint(10, 155))
        color = 255, 0, 0
        #im = Image.new('RGB', (50,50), (color))
        im = Image.new('RGBA', (35,35))
        x, y =  im.size
        eX, eY = h, v #Size of Bounding Box for ellipse
        bbox =  (x/2 - eX/2, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
        draw = ImageDraw.Draw(im)        
        #color2 = (randint(2, 155), randint(2, 155), randint(2, 155))
        draw.ellipse(bbox, fill=color2)
        
        
        sleep(1)
        filename = "circles/TEST_"+datename.date_name()
        im.save(filename)

        counter = counter +1
maketiles(500)        

#%%writefile trans.py
#!/usr/local/bin/python
#GOOD DO NOT TOUCH
def maketiles(quantity):
    from PIL import Image
    from PIL import ImageDraw
    from random import randint
    import sys
    import time
    from time import sleep
    counter = 0
    while counter <= quantity:
        Bcolor = (randint(0, 255), randint(0, 255), randint(0, 255))
        #Bcolor = (randint(10, 155), randint(11, 155), randint(1, 155))
        im = Image.new('RGBA', (35,35), (Bcolor))
        #transparent_area = (randint(0, 50), randint(0, 50), randint(5, 50), randint(5, 50))
        transparent_area = 0,0,35,35
        mask=Image.new('1', im.size, color=255)
        draw=ImageDraw.Draw(mask) 
        draw.rectangle(transparent_area, fill=0)
        im.putalpha(mask)

        #color2 = (randint(0, 155), randint(0, 155), randint(0, 155))
        #color2 = (randint(0, 255), randint(0, 255), randint(0, 255))
        r=randint(45, 235)
        g=randint(45, 235)
        b=randint(45, 235)
        rr=r+30
        gg=g+30
        bb=b+30
        color1 = (r,g,b)
        color2 = (rr,gg,bb)
        overlay = Image.new('RGBA', (35,35), (color2))

        sav = Image.composite(im, overlay, im)
     
        filename = "mosaic/"+datename.date_name()
        sav.save(filename)

        
        h = 35
        v = 35
        #color = (randint(10, 155), randint(0, 155), randint(10, 155))
        color = 255, 0, 0
        #im = Image.new('RGB', (50,50), (color))
        im = Image.new('RGBA', (35,35))
        x, y =  im.size
        eX, eY = h, v #Size of Bounding Box for ellipse
        bbox =  (x/2 - eX/2, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
        draw = ImageDraw.Draw(im)        
        #color2 = (randint(2, 155), randint(2, 155), randint(2, 155))
        draw.ellipse(bbox, fill=color1)
        
        h = 18
        v = 18
        #color = (randint(10, 155), randint(0, 155), randint(10, 155))
        color = 255, 0, 0
        #im = Image.new('RGB', (50,50), (color))
        #im = Image.new('RGBA', (35,35))
        x, y =  im.size
        eX, eY = h, v #Size of Bounding Box for ellipse
        bbox =  (x/2 - eX/2, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
        draw = ImageDraw.Draw(im)        
        #color2 = (randint(2, 155), randint(2, 155), randint(2, 155))
        draw.ellipse(bbox, fill=color2)        
        
        
        pre = time.strftime("%Y%m%d%H%M%S")
        current_milli_time = lambda: int(round(time.time() * 1000))
        x = current_milli_time()
        x=str(x)

        filename = "circles/"+pre+x+".png"
        im.save(filename)
        filename2 = "circles/resize/"+pre+x+".png"
        im2 = im.resize((20,20), Image.NEAREST)
        im2.save(filename2)

        counter = counter +1
maketiles(1000)        

import time

pre = time.strftime("%Y%m%d%H%M%S")
current_milli_time = lambda: int(round(time.time() * 1000))
x = current_milli_time()
x=str(x)
filename = "circles/resize/"+pre+x+".png"
print filename

!mkdir circles

%%writefile Mosaics/__init__.py 
"ver 2.1"

from Mosaics import make_tiles
#help(make_tiles)
make_tiles.maketiles(20)

import Mosaics
help(Mosaics)

!locate Mosaics

#GOOD DO NOT TOUCH

from PIL import Image
from PIL import ImageDraw
from random import randint
from Mosaics import datename
from time import sleep
counter = 0
while counter <= 10:
    #Bcolor = (randint(0, 255), randint(0, 255), randint(0, 255))
    Bcolor = (randint(10, 155), randint(11, 155), randint(1, 155))
    im = Image.new('RGB', (50,50), (Bcolor))
    transparent_area = (randint(0, 50), randint(0, 50), randint(5, 50), randint(5, 50))
    
    mask=Image.new('1', im.size, color=255)
    draw=ImageDraw.Draw(mask) 
    draw.rectangle(transparent_area, fill=0)
    im.putalpha(mask)
    
    color2 = (randint(0, 155), randint(0, 155), randint(0, 155))
    overlay = Image.new('RGB', (50,50), (color2))
    
    sav = Image.composite(im, overlay, im)
    sleep(1)
    filename = "mosaic/"+datename.date_name()
    sav.save(filename)
    
    h = randint(15, 20)
    v = randint(25, 50)
    color = (randint(10, 155), randint(0, 155), randint(10, 155))

    im = Image.new('RGB', (50,50), (color))
    x, y =  im.size
    eX, eY = h, v #Size of Bounding Box for ellipse
    bbox =  (x/2 - eX/2, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
    draw = ImageDraw.Draw(im)
    color2 = (randint(2, 155), randint(2, 155), randint(2, 155))
    draw.ellipse(bbox, fill=color2)
    sleep(1)
    filename = "mosaic/"+datename.date_name()
    im.save(filename)
   
    counter = counter +1

!mkdir toadslices 

!cp toads.jpg toadslices/

import PIL
from PIL import Image
im=Image.open('/home/jack/Desktop/imagebot/instagram/myra.png')
im.save("myra.png")

#When I checked the original image size it was (400,422) 
import PIL
from PIL import Image
im=Image.open('myra.png')
im

#When I checked the original image size it was (400,422) 
import PIL
from PIL import Image
im=Image.open('myra.png')
im.size

!mkdir toadslic

import PIL
from PIL import Image
im=Image.open('myra.jpg')
nm = im.resize((640,640), Image.NEAREST)
nm.save("myra.png")

import image_slicer

import image_slicer
image_slicer.slice('new/new.png', 3000)

!python mosaic.py myra.png circles/

#I wanted to round image size to even tens, so I resized it
import PIL
from PIL import Image
im3=Image.open('toad2.jpg')
im3.resize((640,640), Image.ANTIALIAS)
im3.save('toad4.jpg') 

%%writefile mosaic.py
import sys
import os
from PIL import Image
from multiprocessing import Process, Queue, cpu_count
import multiprocessing

# Change these 3 config parameters to suit your needs...
TILE_SIZE      = 20		# height/width of mosaic tiles in pixels

TILE_MATCH_RES = 2		# tile matching resolution (higher values give better fit but require more processing)
ENLARGEMENT    = 3		
#TILE_MATCH_RES = 1		# tile matching resolution (higher values give better fit but require more processing)
#ENLARGEMENT    = 3		# the mosaic image will be this many times wider and taller than the original

TILE_BLOCK_SIZE = TILE_SIZE / max(min(TILE_MATCH_RES, TILE_SIZE), 1)
#WORKER_COUNT = max(cpu_count() - 1, 1)
WORKER_COUNT = multiprocessing.cpu_count()
OUT_FILE = 'myra001.jpg'
EOQ_VALUE = None

class TileProcessor:
	def __init__(self, tiles_directory):
		self.tiles_directory = tiles_directory

	def __process_tile(self, tile_path):
		try:
			img = Image.open(tile_path)
			# tiles must be square, so get the largest square that fits inside the image
			w = img.size[0]
			h = img.size[1]
			min_dimension = min(w, h)
			w_crop = (w - min_dimension) / 2
			h_crop = (h - min_dimension) / 2
			img = img.crop((w_crop, h_crop, w - w_crop, h - h_crop))

			large_tile_img = img.resize((TILE_SIZE, TILE_SIZE), Image.ANTIALIAS)
			small_tile_img = img.resize((TILE_SIZE/TILE_BLOCK_SIZE, TILE_SIZE/TILE_BLOCK_SIZE), Image.ANTIALIAS)

			return (large_tile_img.convert('RGB'), small_tile_img.convert('RGB'))
		except:
			return (None, None)

	def get_tiles(self):
		large_tiles = []
		small_tiles = []

		print 'Reading tiles from \'%s\'...' % (self.tiles_directory, )

		# search the tiles directory recursively
		for root, subFolders, files in os.walk(self.tiles_directory):
			for tile_name in files:
				tile_path = os.path.join(root, tile_name)
				large_tile, small_tile = self.__process_tile(tile_path)
				if large_tile:
					large_tiles.append(large_tile)
					small_tiles.append(small_tile)
		
		print 'Processed %s tiles.' % (len(large_tiles),)

		return (large_tiles, small_tiles)

class TargetImage:
	def __init__(self, image_path):
		self.image_path = image_path

	def get_data(self):
		print 'Processing main image...'
		img = Image.open(self.image_path)
		w = img.size[0] * ENLARGEMENT
		h = img.size[1]	* ENLARGEMENT
		large_img = img.resize((w, h), Image.ANTIALIAS)
		w_diff = (w % TILE_SIZE)/2
		h_diff = (h % TILE_SIZE)/2
		
		# if necesary, crop the image slightly so we use a whole number of tiles horizontally and vertically
		if w_diff or h_diff:
			large_img = large_img.crop((w_diff, h_diff, w - w_diff, h - h_diff))

		small_img = large_img.resize((w/TILE_BLOCK_SIZE, h/TILE_BLOCK_SIZE), Image.ANTIALIAS)

		image_data = (large_img.convert('RGB'), small_img.convert('RGB'))

		print 'Main image processed.'

		return image_data

class TileFitter:
	def __init__(self, tiles_data):
		self.tiles_data = tiles_data

	def __get_tile_diff(self, t1, t2, bail_out_value):
		diff = 0
		for i in range(len(t1)):
			#diff += (abs(t1[i][0] - t2[i][0]) + abs(t1[i][1] - t2[i][1]) + abs(t1[i][2] - t2[i][2]))
			diff += ((t1[i][0] - t2[i][0])**2 + (t1[i][1] - t2[i][1])**2 + (t1[i][2] - t2[i][2])**2)
			if diff > bail_out_value:
				# we know already that this isnt going to be the best fit, so no point continuing with this tile
				return diff
		return diff

	def get_best_fit_tile(self, img_data):
		best_fit_tile_index = None
		min_diff = sys.maxint
		tile_index = 0

		# go through each tile in turn looking for the best match for the part of the image represented by 'img_data'
		for tile_data in self.tiles_data:
			diff = self.__get_tile_diff(img_data, tile_data, min_diff)
			if diff < min_diff:
				min_diff = diff
				best_fit_tile_index = tile_index
			tile_index += 1

		return best_fit_tile_index

def fit_tiles(work_queue, result_queue, tiles_data):
	# this function gets run by the worker processes, one on each CPU core
	tile_fitter = TileFitter(tiles_data)

	while True:
		try:
			img_data, img_coords = work_queue.get(True)
			if img_data == EOQ_VALUE:
				break
			tile_index = tile_fitter.get_best_fit_tile(img_data)
			result_queue.put((img_coords, tile_index))
		except KeyboardInterrupt:
			pass

	# let the result handler know that this worker has finished everything
	result_queue.put((EOQ_VALUE, EOQ_VALUE))

class ProgressCounter:
	def __init__(self, total):
		self.total = total
		self.counter = 0

	def update(self):
		self.counter += 1
		sys.stdout.write("Progress: %s%% %s" % (100 * self.counter / self.total, "\r"))
    	sys.stdout.flush();

class MosaicImage:
	def __init__(self, original_img):
		self.image = Image.new(original_img.mode, original_img.size)
		self.x_tile_count = original_img.size[0] / TILE_SIZE
		self.y_tile_count = original_img.size[1] / TILE_SIZE
		self.total_tiles  = self.x_tile_count * self.y_tile_count

	def add_tile(self, tile_data, coords):
		img = Image.new('RGB', (TILE_SIZE, TILE_SIZE))
		img.putdata(tile_data)
		self.image.paste(img, coords)

	def save(self, path):
		self.image.save(path)

def build_mosaic(result_queue, all_tile_data_large, original_img_large):
	mosaic = MosaicImage(original_img_large)

	active_workers = WORKER_COUNT
	while True:
		try:
			img_coords, best_fit_tile_index = result_queue.get()

			if img_coords == EOQ_VALUE:
				active_workers -= 1
				if not active_workers:
					break
			else:
				tile_data = all_tile_data_large[best_fit_tile_index]
				mosaic.add_tile(tile_data, img_coords)

		except KeyboardInterrupt:
			pass

	mosaic.save(OUT_FILE)
	print '\nFinished, output is in', OUT_FILE

def compose(original_img, tiles):
	print 'Building mosaic, press Ctrl-C to abort...'
	original_img_large, original_img_small = original_img
	tiles_large, tiles_small = tiles

	mosaic = MosaicImage(original_img_large)

	all_tile_data_large = map(lambda tile : list(tile.getdata()), tiles_large)
	all_tile_data_small = map(lambda tile : list(tile.getdata()), tiles_small)

	work_queue   = Queue(WORKER_COUNT)	
	result_queue = Queue()

	try:
		# start the worker processes that will build the mosaic image
		Process(target=build_mosaic, args=(result_queue, all_tile_data_large, original_img_large)).start()

		# start the worker processes that will perform the tile fitting
		for n in range(WORKER_COUNT):
			Process(target=fit_tiles, args=(work_queue, result_queue, all_tile_data_small)).start()

		progress = ProgressCounter(mosaic.x_tile_count * mosaic.y_tile_count)
		for x in range(mosaic.x_tile_count):
			for y in range(mosaic.y_tile_count):
				large_box = (x * TILE_SIZE, y * TILE_SIZE, (x + 1) * TILE_SIZE, (y + 1) * TILE_SIZE)
				small_box = (x * TILE_SIZE/TILE_BLOCK_SIZE, y * TILE_SIZE/TILE_BLOCK_SIZE, (x + 1) * TILE_SIZE/TILE_BLOCK_SIZE, (y + 1) * TILE_SIZE/TILE_BLOCK_SIZE)
				work_queue.put((list(original_img_small.crop(small_box).getdata()), large_box))
				progress.update()

	except KeyboardInterrupt:
		print '\nHalting, saving partial image please wait...'

	finally:
		# put these special values onto the queue to let the workers know they can terminate
		for n in range(WORKER_COUNT):
			work_queue.put((EOQ_VALUE, EOQ_VALUE))

def mosaic(img_path, tiles_path):
	tiles_data = TileProcessor(tiles_path).get_tiles()
	image_data = TargetImage(img_path).get_data()
	compose(image_data, tiles_data)

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print 'Usage: %s <image> <tiles directory>\r' % (sys.argv[0],)
	else:
		mosaic(sys.argv[1], sys.argv[2])



%%writefile mosaic.py
#using
import sys
import os
from PIL import Image
from multiprocessing import Process, Queue, cpu_count
import multiprocessing

# Change these 3 config parameters to suit your needs...
TILE_SIZE      = 25		# height/width of mosaic tiles in pixels

TILE_MATCH_RES = 1		# tile matching resolution (higher values give better fit but require more processing)
ENLARGEMENT    = 4		
#TILE_MATCH_RES = 1		# tile matching resolution (higher values give better fit but require more processing)
#ENLARGEMENT    = 3		# the mosaic image will be this many times wider and taller than the original

TILE_BLOCK_SIZE = TILE_SIZE / max(min(TILE_MATCH_RES, TILE_SIZE), 1)
#WORKER_COUNT = max(cpu_count() - 1, 1)
WORKER_COUNT = multiprocessing.cpu_count()
OUT_FILE = 'myra002.jpg'
EOQ_VALUE = None

class TileProcessor:
	def __init__(self, tiles_directory):
		self.tiles_directory = tiles_directory

	def __process_tile(self, tile_path):
		try:
			img = Image.open(tile_path)
			# tiles must be square, so get the largest square that fits inside the image
			w = img.size[0]
			h = img.size[1]
			min_dimension = min(w, h)
			w_crop = (w - min_dimension) / 2
			h_crop = (h - min_dimension) / 2
			img = img.crop((w_crop, h_crop, w - w_crop, h - h_crop))

			large_tile_img = img.resize((TILE_SIZE, TILE_SIZE), Image.ANTIALIAS)
			small_tile_img = img.resize((TILE_SIZE/TILE_BLOCK_SIZE, TILE_SIZE/TILE_BLOCK_SIZE), Image.ANTIALIAS)

			return (large_tile_img.convert('RGB'), small_tile_img.convert('RGB'))
		except:
			return (None, None)

	def get_tiles(self):
		large_tiles = []
		small_tiles = []

		print 'Reading tiles from \'%s\'...' % (self.tiles_directory, )

		# search the tiles directory recursively
		for root, subFolders, files in os.walk(self.tiles_directory):
			for tile_name in files:
				tile_path = os.path.join(root, tile_name)
				large_tile, small_tile = self.__process_tile(tile_path)
				if large_tile:
					large_tiles.append(large_tile)
					small_tiles.append(small_tile)
		
		print 'Processed %s tiles.' % (len(large_tiles),)

		return (large_tiles, small_tiles)

class TargetImage:
	def __init__(self, image_path):
		self.image_path = image_path

	def get_data(self):
		print 'Processing main image...'
		img = Image.open(self.image_path)
		w = img.size[0] * ENLARGEMENT
		h = img.size[1]	* ENLARGEMENT
		large_img = img.resize((w, h), Image.ANTIALIAS)
		w_diff = (w % TILE_SIZE)/2
		h_diff = (h % TILE_SIZE)/2
		
		# if necesary, crop the image slightly so we use a whole number of tiles horizontally and vertically
		if w_diff or h_diff:
			large_img = large_img.crop((w_diff, h_diff, w - w_diff, h - h_diff))

		small_img = large_img.resize((w/TILE_BLOCK_SIZE, h/TILE_BLOCK_SIZE), Image.ANTIALIAS)

		image_data = (large_img.convert('RGB'), small_img.convert('RGB'))

		print 'Main image processed.'

		return image_data

class TileFitter:
	def __init__(self, tiles_data):
		self.tiles_data = tiles_data

	def __get_tile_diff(self, t1, t2, bail_out_value):
		diff = 0
		for i in range(len(t1)):
			#diff += (abs(t1[i][0] - t2[i][0]) + abs(t1[i][1] - t2[i][1]) + abs(t1[i][2] - t2[i][2]))
			diff += ((t1[i][0] - t2[i][0])**2 + (t1[i][1] - t2[i][1])**2 + (t1[i][2] - t2[i][2])**2)
			if diff > bail_out_value:
				# we know already that this isnt going to be the best fit, so no point continuing with this tile
				return diff
		return diff

	def get_best_fit_tile(self, img_data):
		best_fit_tile_index = None
		min_diff = sys.maxint
		tile_index = 0

		# go through each tile in turn looking for the best match for the part of the image represented by 'img_data'
		for tile_data in self.tiles_data:
			diff = self.__get_tile_diff(img_data, tile_data, min_diff)
			if diff < min_diff:
				min_diff = diff
				best_fit_tile_index = tile_index
			tile_index += 1

		return best_fit_tile_index

def fit_tiles(work_queue, result_queue, tiles_data):
	# this function gets run by the worker processes, one on each CPU core
	tile_fitter = TileFitter(tiles_data)

	while True:
		try:
			img_data, img_coords = work_queue.get(True)
			if img_data == EOQ_VALUE:
				break
			tile_index = tile_fitter.get_best_fit_tile(img_data)
			result_queue.put((img_coords, tile_index))
		except KeyboardInterrupt:
			pass

	# let the result handler know that this worker has finished everything
	result_queue.put((EOQ_VALUE, EOQ_VALUE))

class ProgressCounter:
	def __init__(self, total):
		self.total = total
		self.counter = 0

	def update(self):
		self.counter += 1
		sys.stdout.write("Progress: %s%% %s" % (100 * self.counter / self.total, "\r"))
    	sys.stdout.flush();

class MosaicImage:
	def __init__(self, original_img):
		self.image = Image.new(original_img.mode, original_img.size)
		self.x_tile_count = original_img.size[0] / TILE_SIZE
		self.y_tile_count = original_img.size[1] / TILE_SIZE
		self.total_tiles  = self.x_tile_count * self.y_tile_count

	def add_tile(self, tile_data, coords):
		img = Image.new('RGB', (TILE_SIZE, TILE_SIZE))
		img.putdata(tile_data)
		self.image.paste(img, coords)

	def save(self, path):
		self.image.save(path)

def build_mosaic(result_queue, all_tile_data_large, original_img_large):
	mosaic = MosaicImage(original_img_large)

	active_workers = WORKER_COUNT
	while True:
		try:
			img_coords, best_fit_tile_index = result_queue.get()

			if img_coords == EOQ_VALUE:
				active_workers -= 1
				if not active_workers:
					break
			else:
				tile_data = all_tile_data_large[best_fit_tile_index]
				mosaic.add_tile(tile_data, img_coords)

		except KeyboardInterrupt:
			pass

	mosaic.save(OUT_FILE)
	print '\nFinished, output is in', OUT_FILE

def compose(original_img, tiles):
	print 'Building mosaic, press Ctrl-C to abort...'
	original_img_large, original_img_small = original_img
	tiles_large, tiles_small = tiles

	mosaic = MosaicImage(original_img_large)

	all_tile_data_large = map(lambda tile : list(tile.getdata()), tiles_large)
	all_tile_data_small = map(lambda tile : list(tile.getdata()), tiles_small)

	work_queue   = Queue(WORKER_COUNT)	
	result_queue = Queue()

	try:
		# start the worker processes that will build the mosaic image
		Process(target=build_mosaic, args=(result_queue, all_tile_data_large, original_img_large)).start()

		# start the worker processes that will perform the tile fitting
		for n in range(WORKER_COUNT):
			Process(target=fit_tiles, args=(work_queue, result_queue, all_tile_data_small)).start()

		progress = ProgressCounter(mosaic.x_tile_count * mosaic.y_tile_count)
		for x in range(mosaic.x_tile_count):
			for y in range(mosaic.y_tile_count):
				large_box = (x * TILE_SIZE, y * TILE_SIZE, (x + 1) * TILE_SIZE, (y + 1) * TILE_SIZE)
				small_box = (x * TILE_SIZE/TILE_BLOCK_SIZE, y * TILE_SIZE/TILE_BLOCK_SIZE, (x + 1) * TILE_SIZE/TILE_BLOCK_SIZE, (y + 1) * TILE_SIZE/TILE_BLOCK_SIZE)
				work_queue.put((list(original_img_small.crop(small_box).getdata()), large_box))
				progress.update()

	except KeyboardInterrupt:
		print '\nHalting, saving partial image please wait...'

	finally:
		# put these special values onto the queue to let the workers know they can terminate
		for n in range(WORKER_COUNT):
			work_queue.put((EOQ_VALUE, EOQ_VALUE))

def mosaic(img_path, tiles_path):
	tiles_data = TileProcessor(tiles_path).get_tiles()
	image_data = TargetImage(img_path).get_data()
	compose(image_data, tiles_data)

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print 'Usage: %s <image> <tiles directory>\r' % (sys.argv[0],)
	else:
		mosaic(sys.argv[1], sys.argv[2])



%%writefile mosaic.py
import sys
import os
from PIL import Image
from multiprocessing import Process, Queue, cpu_count
import multiprocessing

# Change these 3 config parameters to suit your needs...
TILE_SIZE      = 24		# height/width of mosaic tiles in pixels

TILE_MATCH_RES = 2		# tile matching resolution (higher values give better fit but require more processing)
ENLARGEMENT    = 2		
#TILE_MATCH_RES = 1		# tile matching resolution (higher values give better fit but require more processing)
#ENLARGEMENT    = 3		# the mosaic image will be this many times wider and taller than the original

TILE_BLOCK_SIZE = TILE_SIZE / max(min(TILE_MATCH_RES, TILE_SIZE), 1)
#WORKER_COUNT = max(cpu_count() - 1, 1)
WORKER_COUNT = multiprocessing.cpu_count()
OUT_FILE = 'myra003.jpg'
EOQ_VALUE = None

class TileProcessor:
	def __init__(self, tiles_directory):
		self.tiles_directory = tiles_directory

	def __process_tile(self, tile_path):
		try:
			img = Image.open(tile_path)
			# tiles must be square, so get the largest square that fits inside the image
			w = img.size[0]
			h = img.size[1]
			min_dimension = min(w, h)
			w_crop = (w - min_dimension) / 2
			h_crop = (h - min_dimension) / 2
			img = img.crop((w_crop, h_crop, w - w_crop, h - h_crop))

			large_tile_img = img.resize((TILE_SIZE, TILE_SIZE), Image.ANTIALIAS)
			small_tile_img = img.resize((TILE_SIZE/TILE_BLOCK_SIZE, TILE_SIZE/TILE_BLOCK_SIZE), Image.ANTIALIAS)

			return (large_tile_img.convert('RGB'), small_tile_img.convert('RGB'))
		except:
			return (None, None)

	def get_tiles(self):
		large_tiles = []
		small_tiles = []

		print 'Reading tiles from \'%s\'...' % (self.tiles_directory, )

		# search the tiles directory recursively
		for root, subFolders, files in os.walk(self.tiles_directory):
			for tile_name in files:
				tile_path = os.path.join(root, tile_name)
				large_tile, small_tile = self.__process_tile(tile_path)
				if large_tile:
					large_tiles.append(large_tile)
					small_tiles.append(small_tile)
		
		print 'Processed %s tiles.' % (len(large_tiles),)

		return (large_tiles, small_tiles)

class TargetImage:
	def __init__(self, image_path):
		self.image_path = image_path

	def get_data(self):
		print 'Processing main image...'
		img = Image.open(self.image_path)
		w = img.size[0] * ENLARGEMENT
		h = img.size[1]	* ENLARGEMENT
		large_img = img.resize((w, h), Image.ANTIALIAS)
		w_diff = (w % TILE_SIZE)/2
		h_diff = (h % TILE_SIZE)/2
		
		# if necesary, crop the image slightly so we use a whole number of tiles horizontally and vertically
		if w_diff or h_diff:
			large_img = large_img.crop((w_diff, h_diff, w - w_diff, h - h_diff))

		small_img = large_img.resize((w/TILE_BLOCK_SIZE, h/TILE_BLOCK_SIZE), Image.ANTIALIAS)

		image_data = (large_img.convert('RGB'), small_img.convert('RGB'))

		print 'Main image processed.'

		return image_data

class TileFitter:
	def __init__(self, tiles_data):
		self.tiles_data = tiles_data

	def __get_tile_diff(self, t1, t2, bail_out_value):
		diff = 0
		for i in range(len(t1)):
			#diff += (abs(t1[i][0] - t2[i][0]) + abs(t1[i][1] - t2[i][1]) + abs(t1[i][2] - t2[i][2]))
			diff += ((t1[i][0] - t2[i][0])**2 + (t1[i][1] - t2[i][1])**2 + (t1[i][2] - t2[i][2])**2)
			if diff > bail_out_value:
				# we know already that this isnt going to be the best fit, so no point continuing with this tile
				return diff
		return diff

	def get_best_fit_tile(self, img_data):
		best_fit_tile_index = None
		min_diff = sys.maxint
		tile_index = 0

		# go through each tile in turn looking for the best match for the part of the image represented by 'img_data'
		for tile_data in self.tiles_data:
			diff = self.__get_tile_diff(img_data, tile_data, min_diff)
			if diff < min_diff:
				min_diff = diff
				best_fit_tile_index = tile_index
			tile_index += 1

		return best_fit_tile_index

def fit_tiles(work_queue, result_queue, tiles_data):
	# this function gets run by the worker processes, one on each CPU core
	tile_fitter = TileFitter(tiles_data)

	while True:
		try:
			img_data, img_coords = work_queue.get(True)
			if img_data == EOQ_VALUE:
				break
			tile_index = tile_fitter.get_best_fit_tile(img_data)
			result_queue.put((img_coords, tile_index))
		except KeyboardInterrupt:
			pass

	# let the result handler know that this worker has finished everything
	result_queue.put((EOQ_VALUE, EOQ_VALUE))

class ProgressCounter:
	def __init__(self, total):
		self.total = total
		self.counter = 0

	def update(self):
		self.counter += 1
		sys.stdout.write("Progress: %s%% %s" % (100 * self.counter / self.total, "\r"))
    	sys.stdout.flush();

class MosaicImage:
	def __init__(self, original_img):
		self.image = Image.new(original_img.mode, original_img.size)
		self.x_tile_count = original_img.size[0] / TILE_SIZE
		self.y_tile_count = original_img.size[1] / TILE_SIZE
		self.total_tiles  = self.x_tile_count * self.y_tile_count

	def add_tile(self, tile_data, coords):
		img = Image.new('RGB', (TILE_SIZE, TILE_SIZE))
		img.putdata(tile_data)
		self.image.paste(img, coords)

	def save(self, path):
		self.image.save(path)

def build_mosaic(result_queue, all_tile_data_large, original_img_large):
	mosaic = MosaicImage(original_img_large)

	active_workers = WORKER_COUNT
	while True:
		try:
			img_coords, best_fit_tile_index = result_queue.get()

			if img_coords == EOQ_VALUE:
				active_workers -= 1
				if not active_workers:
					break
			else:
				tile_data = all_tile_data_large[best_fit_tile_index]
				mosaic.add_tile(tile_data, img_coords)

		except KeyboardInterrupt:
			pass

	mosaic.save(OUT_FILE)
	print '\nFinished, output is in', OUT_FILE

def compose(original_img, tiles):
	print 'Building mosaic, press Ctrl-C to abort...'
	original_img_large, original_img_small = original_img
	tiles_large, tiles_small = tiles

	mosaic = MosaicImage(original_img_large)

	all_tile_data_large = map(lambda tile : list(tile.getdata()), tiles_large)
	all_tile_data_small = map(lambda tile : list(tile.getdata()), tiles_small)

	work_queue   = Queue(WORKER_COUNT)	
	result_queue = Queue()

	try:
		# start the worker processes that will build the mosaic image
		Process(target=build_mosaic, args=(result_queue, all_tile_data_large, original_img_large)).start()

		# start the worker processes that will perform the tile fitting
		for n in range(WORKER_COUNT):
			Process(target=fit_tiles, args=(work_queue, result_queue, all_tile_data_small)).start()

		progress = ProgressCounter(mosaic.x_tile_count * mosaic.y_tile_count)
		for x in range(mosaic.x_tile_count):
			for y in range(mosaic.y_tile_count):
				large_box = (x * TILE_SIZE, y * TILE_SIZE, (x + 1) * TILE_SIZE, (y + 1) * TILE_SIZE)
				small_box = (x * TILE_SIZE/TILE_BLOCK_SIZE, y * TILE_SIZE/TILE_BLOCK_SIZE, (x + 1) * TILE_SIZE/TILE_BLOCK_SIZE, (y + 1) * TILE_SIZE/TILE_BLOCK_SIZE)
				work_queue.put((list(original_img_small.crop(small_box).getdata()), large_box))
				progress.update()

	except KeyboardInterrupt:
		print '\nHalting, saving partial image please wait...'

	finally:
		# put these special values onto the queue to let the workers know they can terminate
		for n in range(WORKER_COUNT):
			work_queue.put((EOQ_VALUE, EOQ_VALUE))

def mosaic(img_path, tiles_path):
	tiles_data = TileProcessor(tiles_path).get_tiles()
	image_data = TargetImage(img_path).get_data()
	compose(image_data, tiles_data)

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print 'Usage: %s <image> <tiles directory>\r' % (sys.argv[0],)
	else:
		mosaic(sys.argv[1], sys.argv[2])



#GOOD DO NOT TOUCH
from PIL import Image
from PIL import ImageDraw
from random import randint
from Mimages import datename
counter = 0
while counter <= 100:
    Bcolor = (randint(0, 255), randint(0, 255), randint(0, 255))
    im = Image.new('RGB', (50,50), (Bcolor))
    transparent_area = (randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50))
    
    mask=Image.new('1', im.size, color=255)
    draw=ImageDraw.Draw(mask) 
    draw.rectangle(transparent_area, fill=0)
    im.putalpha(mask)
    
    color2 = (randint(0, 255), randint(0, 255), randint(0, 255))
    overlay = Image.new('RGB', (50,50), (color2))
    
    sav = Image.composite(im, overlay, im)
    filename = "mosaic/"+datename.date_name()
    sav.save(filename)
    
    h = randint(15, 50)
    v = randint(15, 50)
    color = (randint(0, 255), randint(0, 255), randint(0, 255))

    im = Image.new('RGB', (50,50), (color))
    x, y =  im.size
    eX, eY = h, v #Size of Bounding Box for ellipse
    bbox =  (x/2 - eX/2, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
    draw = ImageDraw.Draw(im)
    color2 = (randint(2, 255), randint(2, 255), randint(2, 255))
    draw.ellipse(bbox, fill=color2)
    filename = "mosaic/"+datename.date_name()
    im.save(filename)
    counter = counter +1

from os import listdir
from PIL import Image
path1 = "bugs/processed-faces/square/"    
for filename in listdir(path1):
    if filename.endswith('.png'):
        try:
            img = Image.open(path1+filename) # open the image file
            img.verify() # verify that it is, in fact an image
        except (IOError, SyntaxError) as e:
            print('Bad file:', filename) # print out the names of corrupt files


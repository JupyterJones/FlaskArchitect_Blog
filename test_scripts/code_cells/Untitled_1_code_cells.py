from PIL import Image, ImageSequence

def zoom_effect(bg_file, fg_file):
    bg = Image.open(bg_file).convert('RGBA')
    bg = bg.resize((640,640), Image.BICUBIC)
    fg = Image.open(fg_file).convert('RGBA')
    fg = fg.resize((bg.size), Image.BICUBIC)
    fg_copy = fg.copy()
    fg_copy = fg_copy.resize((int(fg_copy.width), int(fg_copy.height)))
    result_images = []
    for i in range(10):
        size = (int(fg_copy.width * (i+1)/10), int(fg_copy.height * (i+1)/10))
        fg_copy_resized = fg_copy.resize(size)
        fg_copy_resized.putalpha(int((i+1)*255/10))
        fg_copy_resized = fg_copy_resized.convert('RGBA')
        fg_copy_resized.putalpha(int((i+1)*255/10))
        result = bg.copy()
        x = int((bg.width - fg_copy_resized.width)/2)
        y = int((bg.height - fg_copy_resized.height)/2)
        result.alpha_composite(fg_copy_resized, (x, y))
        result.save("gifs/_"+str(i)+".png")
        result_images.append(result)
    # Save the resulting images as a GIF animation
    result_images[0].save('gifs/zoom_effect.gif', save_all=True, append_images=result_images[1:], optimize=False, duration=100, loop=0)
#zoom_effect(bg_file, fg_file)
zoom_effect("gifs/background.jpg", "gifs/focus.png")


from PIL import Image, ImageSequence

def zoom_effect(bg_file, fg_file):
    bg = Image.open(bg_file).convert('RGBA')
    fg = Image.open(fg_file).convert('RGBA')
    fg = fg.resize((bg.size), Image.BICUBIC)
    fg.putalpha(0)
    fg_copy = fg.copy()
    fg_copy = fg_copy.resize((int(fg_copy.width), int(fg_copy.height)))
    fg_copy.putalpha(0)
    result_images = []
    for i in range(10):
        size = (int(fg_copy.width * (i+1)/10), int(fg_copy.height * (i+1)/10))
        fg_copy_resized = fg_copy.resize(size)
        fg_copy_resized.putalpha(int((i+1)*255/10))
        result = bg.copy()
        x = int((bg.width - fg_copy_resized.width)/2)
        y = int((bg.height - fg_copy_resized.height)/2)
        result.alpha_composite(fg_copy_resized, (x, y))
        result = Image.blend(bg, result, (i+1)/10)
        result.save("gifs/_"+str(i)+".png")
        result_images.append(result)
    # Save the resulting images as a GIF animation
    result_images[0].save('gifs/zoom_effect.gif', save_all=True, append_images=result_images[1:], optimize=False, duration=100, loop=0)

zoom_effect("gifs/background.jpg", "gifs/focus.png")
#Problem: Notice the line, result.save("gifs/_"+str(i)+".png") I did that to check the #images generated that all have black 'focus' overlays in various opacities the same as #the resulting zoom_effect.gif. 

import os
total_size = 0
for root, dirs, files in os.walk('/home/jack'):
    for file in files:
        if file.endswith('.ipynb'):
            filepath = os.path.join(root, file)
            total_size += os.path.getsize(filepath)
total_size_mb = total_size / (1024 * 1024)
print(f"Total size of Jupyter notebooks: {total_size_mb:.2f} MB")

import os
import shutil

src_dir = '/home/jack'  # Replace this with the root directory where you want to search for Jupyter notebooks
dst_dir = '/path/to/destination/directory/'  # Replace this with the destination directory where you want to copy the notebooks
notebooks = {}  # Dictionary to keep track of notebook names and sequence numbers

for root, dirs, files in os.walk(src_dir):
    for file in files:
        if file.endswith('.ipynb'):
            src_path = os.path.join(root, file)
            dst_path = os.path.join(dst_dir, file)
            if file in notebooks:
                # Increment sequence number for duplicate file names
                notebooks[file] += 1
                name, ext = os.path.splitext(file)
                new_name = f"{name}_{notebooks[file]}{ext}"
                dst_path = os.path.join(dst_dir, new_name)
            else:
                notebooks[file] = 0
            try:
                shutil.copy2(src_path, dst_path)
            except PermissionError:
                # Skip directories that we don't have permission to read
                continue

print("Done copying Jupyter notebooks!")


from PIL import Image, ImageSequence

def zoom_effect(bg_file, fg_file):
    bg = Image.open(bg_file).convert('RGBA')
    fg = Image.open(fg_file).convert('RGBA')
    fg = fg.resize((bg.size), Image.BICUBIC)
    fg_copy = fg.copy()
    fg_copy = fg_copy.resize((int(fg_copy.width), int(fg_copy.height)))
    fg_copy.putalpha(0)
    result_images = []
    for i in range(10):
        size = (int(fg_copy.width * (i+1)/10), int(fg_copy.height * (i+1)/10))
        fg_copy_resized = fg_copy.resize(size)
        fg_copy_resized.putalpha(int((i+1)*255/10))
        result = bg.copy()
        x = int((bg.width - fg_copy_resized.width)/2)
        y = int((bg.height - fg_copy_resized.height)/2)
        result.alpha_composite(fg_copy_resized, (x, y))
        result_images.append(result)
    # Save the resulting images as a GIF animation
    result_images[0].save('gifs/zoom_effect.gif', save_all=True, append_images=result_images[1:], optimize=False, duration=100, loop=0)

if __name__ == "__main__":
    zoom_effect("gifs/background.jpg", "gifs/focus.png")


from PIL import Image, ImageSequence
def zoom_effect(bg_file, fg_file):
    bg = Image.open(bg_file).convert('RGBA')
    fg = Image.open(fg_file)
    fg = fg.resize((bg.size), Image.BICUBIC)
    fg = fg.convert('RGBA')
    fg_copy = fg.copy()
    fg_copy = fg_copy.resize((int(fg_copy.width), int(fg_copy.height)))
    fg_copy.putalpha(0)
    result_images = []
    for i in range(10):
        size = (int(fg_copy.width * (i+1)/10), int(fg_copy.height * (i+1)/10))
        fg_copy_resized = fg_copy.resize(size)
        fg_copy_resized.putalpha(int((i+1)*255/10))
        result = bg.copy()
        x = int((bg.width - fg_copy_resized.width)/2)
        y = int((bg.height - fg_copy_resized.height)/2)
        result.alpha_composite(fg_copy_resized, (x, y))
        result_images.append(result)
    # Save the resulting images as a GIF animation
    result_images[0].save('gifs/zoom_effect.gif', save_all=True, append_images=result_images[1:], optimize=False, duration=100, loop=0)
bg_file = "gifs/background.jpg"
fg_file = "gifs/focus.jpg"
zoom_effect(bg_file, fg_file)


from PIL import Image, ImageSequence

def zoom_effect(bg_file, fg_file):
    bg = Image.open(bg_file).convert('RGBA')
    fg = Image.open(fg_file).convert('RGBA')
    fg_copy = fg.copy()
    fg_copy = fg_copy.resize((int(fg_copy.width), int(fg_copy.height)))
    fg_copy.putalpha(0)
    result_images = []
    for i in range(10):
        size = (int(fg_copy.width * (i+1)/10), int(fg_copy.height * (i+1)/10))
        fg_copy_resized = fg_copy.resize(size)
        fg_copy_resized.putalpha(int((i+1)*255/10))
        result = bg.copy()
        result.alpha_composite(fg_copy_resized)
        result_images.append(result)

    # Save the resulting images as a GIF animation
    result_images[0].save('zoom_effect.gif', save_all=True, append_images=result_images[1:], optimize=False, duration=100, loop=0)

#if __name__ == "__main__":
bg_file = "/home/jack/Downloads/00de3/lexica/e12768a8-747e-4fd0-98d4-6f094f2962b3.jpeg"
fg_file = "/home/jack/Desktop/dockercommands/gypsy-princess11.jpg"
zoom_effect(bg_file, fg_file)


from PIL import Image, ImageSequence

def zoom_effect(bg_file, fg_file):
    bg = Image.open(bg_file)
    fg = Image.open(fg_file).convert('RGBA')
    fg_copy = fg.copy()
    fg_copy = fg_copy.resize((int(fg_copy.width/2), int(fg_copy.height/2)), resample=Image.BICUBIC)
    fg_copy.putalpha(0)
    result_images = []
    for i in range(10):
        size = (int(fg_copy.width * (i+1)/10), int(fg_copy.height * (i+1)/10))
        fg_copy_resized = fg_copy.resize(size, resample=Image.BICUBIC)
        fg_copy_resized.putalpha(int((i+1)*255/10))
        result = bg.copy()
        result.alpha_composite(fg_copy_resized)
        result_images.append(result)

    # Save the resulting images as a GIF animation
    result_images[0].save('zoom_effect.gif', save_all=True, append_images=result_images[1:], optimize=False, duration=100, loop=0)
       
#if __name__ == "__main__":
bg_file = "gifs/background.jpg"
fg_file = "gifs/focus.jpg"
zoom_effect(bg_file, fg_file)


!ls gifs

from PIL import Image, ImageSequence
def zoom_effect(bg_file, fg_file):
    bg = Image.open(bg_file)
    print(bg.size[0])
    fg = Image.open(fg_file)
    fg = fg.resize((bg.size), Image.BICUBIC)
    fg_copy = fg.copy()
    fg_copy = fg_copy.resize((int(fg_copy.width/2), int(fg_copy.height/2)))
    fg_copy.putalpha(0)
    result_images = []
    for i in range(10):
        size = (int(fg_copy.width * (i+1)/10), int(fg_copy.height * (i+1)/10))
        print('size',size)
        fg_copy_resized = fg_copy.resize(size)
        fg_copy_resized.putalpha(int((i+1)*255/10))
        result = bg.copy()
        print(result.size)
        result.paste(fg_copy_resized, (bg.size[0]//2,bg.size[1]//2), fg_copy_resized)
        result.save(str(i)+".png")
        result_images.append(result)

    # Save the resulting images as a GIF animation
    result_images[0].save('zoom_effect.gif', save_all=True, append_images=result_images[1:], optimize=False, duration=100, loop=0)
        
#if __name__ == "__main__":
bg_file = "/home/jack/Downloads/00de3/lexica/e12768a8-747e-4fd0-98d4-6f094f2962b3.jpeg"
fg_file = "/home/jack/Desktop/dockercommands/gypsy-princess11.jpg"
zoom_effect(bg_file, fg_file)






from PIL import Image

def zoom_effect(bg_file, fg_file):
    bg = Image.open(bg_file)
    fg = Image.open(fg_file)
    fg_copy = fg.copy()
    fg_copy = fg_copy.resize((int(fg_copy.width/2), int(fg_copy.height/2)))
    fg_copy.putalpha(0)
    result_images = []
    for i in range(10):
        size = (int(fg_copy.width * (i+1)/10), int(fg_copy.height * (i+1)/10))
        fg_copy_resized = fg_copy.resize(size)
        fg_copy_resized.putalpha(int((i+1)*255/10))
        result = bg.copy()
        result.paste(fg_copy_resized, (0, 0), fg_copy_resized)
        result_images.append(result)
    for i in range(len(result_images)):
        result_images[i].save("result" + str(i) + ".jpg")

if __name__ == "__main__":
    zoom_effect("background.jpg", "focus.jpg")


from processing_py import *
from random import choice, shuffle, uniform, gauss

brush = {"x":None, "y":None, "px":None, "py":None}

colors = [
	(112, 112,  74, 150), # green
	(245, 198, 110, 150), # yellow
	(242, 229, 194, 150), # cream
	(115, 106,  97, 150), # light grey
	(215,  90,  34, 150), # orange
	(235,  61,   0, 150)] # red-orange
shuffle(colors)

def setup():
  size(400,400)
  base = colors.pop()
  background(base[0], base[1], base[2])

def draw():
  global brush
  if frameCount == 40:
    brush = {"x": mouseX, "y": mouseY, "px": mouseX-1, "py": mouseY-1}
  elif frameCount > 40:
    brush["x"] += (mouseX - brush["x"]) / 12
    brush["y"] += (mouseY - brush["y"]) / 12
    drizzle()
    brush["px"] = brush["x"]
    brush["py"] = brush["y"]
  
def drizzle():
  d = dist(brush["px"], brush["py"], brush["x"], brush["y"])
  s = min(15, 1+30/(d+0.0001))
  strokeWeight(s)
  stroke(0)
  line(brush["px"], brush["py"], brush["x"], brush["y"])
  stroke(255)
  line(width-brush["px"], height-brush["py"], width-brush["x"], height-brush["y"])

def stipple(bx, by, c):
  noStroke()
  fill(c)
  for i in range(2):
    d = uniform(3, 12)
    ellipse(bx + uniform(-30,30), by+uniform(-30,30), d, d)

def splatter(bx, by):
  rgb = choice(colors) 
  bx += uniform(-15,15)
  by += uniform(-15,15)
  mx = 5*(mouseX-pmouseX)
  my = 5*(mouseY-pmouseY)
  for i in range(80):
    x = bx + mx*gauss(0,0.25)
    y = by + my*gauss(0,0.25)
    d = dist(bx, by, x, y)
    s = min(10, 150/(d+0.00001))
    alpha = 255 - s*5
    noStroke()
    c = color(rgb[0], rgb[1], rgb[2], alpha)
    fill(c)
    ellipse(x,y,s,s)

def mouseMoved():
  if frameCount % 7 == 0:
    stipple(mouseX, mouseY, 0)
    stipple(width-mouseX, height-mouseY, 255)
    splatter(mouseX, mouseY)
    splatter(width-mouseX, height-mouseY)

setup()

from processing_py import *

app = App(600,400) # create window: width, height
app.background(255,0,0) # set background:  red, green, blue
app.redraw() # refresh the window

#app.exit() # close the window


from processing_py import *

app = App(600,400) # create window: width, height
app.background(0,0,0) # set background:  red, green, blue
app.fill(255,255,0) # set color for objects: red, green, blue
app.rect(100,100,200,100) # draw a rectangle: x0, y0, size_x, size_y
app.fill(0,0,255) # set color for objects: red, green, blue
app.ellipse(300,200,50,50) # draw a circle: center_x, center_y, size_x, size_y
app.redraw() # refresh the window


from processing_py import *
app = App(600,400) # create window: width, height

while(True):
   app.background(0,0,0) # set background:  red, green, blue
   app.fill(255,255,0) # set color for objects: red, green, blue
   app.ellipse(app.mouseX,app.mouseY,50,50) # draw a circle: center_x, center_y, size_x, size_y
   app.redraw() # refresh the window


import numpy as np
from PIL import Image
from math import *


im =Image.open("/home/jack/Desktop/EXP_notebooks/lexica_nubian/819x768/e036ce39-9802-4a3e-aa13-229b62152824.jpg")
PATH=im.size


t=PATH[0]
path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))
im

import imageio
import numpy as np
from PIL import Image

def create_square(size=(3, 3), color=(255, 0, 0, 200)):
    square = Image.new('RGBA', size, color)
    return square

def paste_square(image, position, square):
    x, y = position
    image.paste(square, (x, y, x + square.width, y + square.height), square)

def bezier_curve(t, p0, p1, p2, p3):
    return (
        int((1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0]),
        int((1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1])
    )

im = Image.open("/home/jack/Desktop/EXP_notebooks/lexica_nubian/819x768/e036ce39-9802-4a3e-aa13-229b62152824.jpg").convert("RGBA") 
image_size = im.size

width = image_size[0]
height = image_size[1]

# Define control points for the Bézier curve
p0 = (width // 4, height // 4)
p1 = (width // 2, 0)
p2 = (3 * width // 4, 3 * height // 4)
p3 = (width, height // 2)

# Generate points along the Bézier curve
path = lambda t: bezier_curve(t, p0, p1, p2, p3)

square = create_square()

# Create a copy of the original image to keep it unchanged
result_image = im.copy()

# Create a list to store frames
frames = []

# Paste the square along the path on top of the original image and save each frame
for t in np.linspace(0, 1, width):
    position = path(t)
    paste_square(result_image, position, square)
    frame = np.array(result_image)
    frames.append(frame)
    # Save each frame as an image
    imageio.imwrite(f"frame_{t}.png", frame)

# Compile frames into an mp4 video using ffmpeg
imageio.mimsave('output.mp4', frames, fps=24)

print("Video saved successfully!")


from PIL import Image, ImageDraw
import numpy as np

def create_square(size=(3, 3), color=(255, 0, 0, 200)):
    square = Image.new('RGBA', size, color)
    return square

def paste_square(image, position, square):
    x, y = position
    image.paste(square, (x, y, x + square.width, y + square.height), square)

def bezier_curve(t, p0, p1, p2, p3):
    return (
        int((1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0]),
        int((1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1])
    )

im = Image.open("/home/jack/Desktop/EXP_notebooks/lexica_nubian/819x768/e036ce39-9802-4a3e-aa13-229b62152824.jpg").convert("RGBA") 
image_size = im.size

width = image_size[0]
height = image_size[1]

# Define control points for the Bézier curve
p0 = (width // 4, height // 4)
p1 = (width // 2, 0)
p2 = (3 * width // 4, 3 * height // 4)
p3 = (width, height // 2)

# Generate points along the Bézier curve
path = lambda t: bezier_curve(t, p0, p1, p2, p3)

square = create_square()

# Create a copy of the original image to keep it unchanged
result_image = im.copy()

# Paste the square along the path on top of the original image
for t in np.linspace(0, 1, width):
    position = path(t)
    paste_square(result_image, position, square)

# Display both the original image and the modified image
result_image


from PIL import Image, ImageDraw
import numpy as np

def create_square(size=(3, 3), color=(255, 0, 0, 200)):
    square = Image.new('RGBA', size, color)
    return square

def paste_square(image, position, square):
    x, y = position
    image.paste(square, (x, y, x + square.width, y + square.height), square)

im = Image.open("/home/jack/Desktop/EXP_notebooks/lexica_nubian/819x768/e036ce39-9802-4a3e-aa13-229b62152824.jpg").convert("RGBA") 
image_size = im.size

width = image_size[0]
height = image_size[1]

path = lambda t: (int(width/2 + 100 * np.sin(2 * np.pi * t / width)), int(height/2))

square = create_square()

# Create a copy of the original image to keep it unchanged
result_image = im.copy()

# Paste the square along the path on top of the original image
for w in range(width):
    position = path(w)
    paste_square(result_image, position, square)

# Display both the original image and the modified image
result_image.show()


from PIL import Image, ImageDraw
import numpy as np

def create_square(size=(30, 30), color=(255, 0, 0, 150)):
    square = Image.new('RGBA', size, color)
    return square

def paste_square(image, position, square):
    x, y = position
    image.paste(square, (x, y, x + square.width, y + square.height), square)

im = Image.open("/home/jack/Desktop/EXP_notebooks/lexica_nubian/819x768/e036ce39-9802-4a3e-aa13-229b62152824.jpg").convert("RGBA") 
image_size = im.size

width = image_size[0]
height = image_size[1]

#path = lambda t: (int(100 * np.sin(2 * np.pi * t / width)), int(50 * np.cos(2 * np.pi * t / width)))
#path = lambda t: (int(width/2), int((height/2) * np.sin(2 * np.pi * t / width)))
path = lambda t: (int(width/2 + 100 * np.sin(2 * np.pi * t / width)), int(height/2))

square = create_square()

# Create a copy of the original image to keep it unchanged
result_image = im.copy()

# Paste the square along the path on top of the original image
for w in range(width):
    position = path(w)
    paste_square(result_image, position, square)

# Display both the original image and the modified image
result_image




from PIL import Image, ImageDraw
import numpy as np

def create_square(size=(3, 3), color=(255, 0, 0, 250)):
    square = Image.new('RGBA', size, color)
    return square

def paste_square(image, position, square):
    x, y = position
    image.paste(square, (x, y, x + square.width, y + square.height), square)

im = Image.open("/home/jack/Desktop/EXP_notebooks/lexica_nubian/819x768/e036ce39-9802-4a3e-aa13-229b62152824.jpg").convert("RGBA") 
image_size = im.size

width = image_size[0]
height = image_size[1]

path = lambda t: (int(100 * np.sin(2 * np.pi * t / width)), int(50 * np.cos(2 * np.pi * t / width)))

square = create_square()

# Create a copy of the original image to keep it unchanged
result_image = im.copy()

# Paste the square along the path on top of the original image
for w in range(width):
    position = path(w)
    paste_square(result_image, position, square)

# Display both the original image and the modified image

result_image




from PIL import Image, ImageDraw
import numpy as np

def create_square(size=(3, 3), color=(255, 0, 0)):
    square = Image.new('RGB', size, color)
    return square

def paste_square(image, position, square):
    image.paste(square, position, square)

im = Image.open("/home/jack/Desktop/EXP_notebooks/lexica_nubian/819x768/e036ce39-9802-4a3e-aa13-229b62152824.jpg")
image_size = im.size

width = image_size[0]
height = image_size[1]

path = lambda t: (int(100 * np.sin(2 * np.pi * t / width)), int(50 * np.cos(2 * np.pi * t / width)))

square = create_square()

# Create a copy of the original image to keep it unchanged
result_image = im.copy()

# Paste the square along the path on top of the original image
for w in range(width):
    position = path(w)
    paste_square(result_image, position, square)

# Display both the original image and the modified image
im.show()
result_image.show()


from PIL import Image, ImageDraw
import numpy as np

def create_square(size=(3, 3), color=(255, 0, 0)):
    square = Image.new('RGB', size, color)
    return square

def paste_square(image, position, square):
    image.paste(square, position)

im = Image.open("/home/jack/Desktop/EXP_notebooks/lexica_nubian/819x768/e036ce39-9802-4a3e-aa13-229b62152824.jpg")
image_size = im.size

width = image_size[0]
height = image_size[1]

path = lambda t: (int(100 * np.sin(2 * np.pi * t / width)), int(50 * np.cos(2 * np.pi * t / width)))

square = create_square()

# Create a new image with the same size as the original image
result_image = Image.new('RGB', (width, height), (255, 255, 255))

draw = ImageDraw.Draw(result_image)

# Paste the square along the path
for w in range(width):
    position = path(w)
    paste_square(result_image, position, square)

# Display or save the result_image
result_image


from PIL import Image
import numpy as np

im = Image.open("/home/jack/Desktop/EXP_notebooks/lexica_nubian/819x768/e036ce39-9802-4a3e-aa13-229b62152824.jpg")
image_size = im.size

width = image_size[0]
path = lambda t: (100 * np.sin(2 * np.pi * t / width), 50 * np.cos(2 * np.pi * t / width))

for w in range(width):
    print(path(w))


im =Image.open("/home/jack/Desktop/EXP_notebooks/lexica_nubian/819x768/e036ce39-9802-4a3e-aa13-229b62152824.jpg")
PATH=im.size

t=PATH[0]
path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))
print(path)
for w in path:
    print(w)




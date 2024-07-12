def create_square():
    square=Image.open("/home/jack/Desktop/EXP_notebooks/leo/00036.jpg").resize((100,200),Image.BICUBIC)
    return square

import numpy as np
from PIL import Image
import imageio
def create_square():
    square=Image.open("leo/00036.jpg").resize((100,200),Image.BICUBIC).convert("RGBA")
    return square

def paste_square(image, position, square):
    x, y = position
    #SIZE=square.size
    #square=square.resize((SIZE[0]+8,SIZE[1]+8),Image.BICUBIC)
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
    SIZE=square.size
    square=square.resize((SIZE[0]+1,SIZE[1]+1),Image.BICUBIC)    
    paste_square(result_image, position, square)
    frame = np.array(result_image)
    frames.append(frame)
    print(".",end="-")

# Compile frames into an mp4 video using ffmpeg
imageio.mimsave('output32324.mp4', frames, fps=24)

print("Video saved successfully!")


!vlc output32324.mp4

import numpy as np
from PIL import Image
import imageio

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

# Compile frames into an mp4 video using ffmpeg
imageio.mimsave('output3232.mp4', frames, fps=24)

print("Video saved successfully!")


import os
import shutil
import logging
from PIL import Image

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#665x972 
def move_images(source_dir, width, height):
    dest_dir=source_dir+"/"+str(width)+"x"+str(height)
    try:
        # Create destination directory if it doesn't exist
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            logging.info(f"Created destination directory: {dest_dir}")

        # Iterate through files in the source directory
        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)
            
            # Check if the file is an image
            if os.path.isfile(source_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                try:
                    # Get image dimensions
                    image_width, image_height = get_image_dimensions(source_path)
                    # If the image matches the specified width and height, move it to the destination directory
                    if image_width == width and image_height == height:
                        dest_path = os.path.join(dest_dir, filename)
                        shutil.move(source_path, dest_path)
                        logging.info(f"Moved {filename} to {dest_dir}")
                except Exception as e:
                    logging.error(f"Error processing {filename}: {e}")
            else:
                logging.info(f"Ignored {filename} as it's not an image file")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
    return width, height

# Source and destination directories
source_directory = '/home/jack/Desktop/EXP_notebooks/lexica/'
#destination_directory = '/home/jack/Desktop/EXP_notebooks/lexica/512x768'

SIZE='614x819'.split('x')
width = int(SIZE[0])
height = int(SIZE[1])
print(width,height)

move_images(source_directory,width,height)


SIZE='563x1126'.split('x')
width = int(SIZE[0])
height = int(SIZE[1])
print(width,height)

import glob
imsizes=set()
def move_images(source_dir, width, height):
    dest_dir=source_dir+"/"+str(width)+"x"+str(height)
    try:
        # Create destination directory if it doesn't exist
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            logging.info(f"Created destination directory: {dest_dir}")

        # Iterate through files in the source directory
        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)
            
            # Check if the file is an image
            if os.path.isfile(source_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                try:
                    # Get image dimensions
                    image_width, image_height = get_image_dimensions(source_path)
                    # If the image matches the specified width and height, move it to the destination directory
                    if image_width == width and image_height == height:
                        dest_path = os.path.join(dest_dir, filename)
                        shutil.move(source_path, dest_path)
                        logging.info(f"Moved {filename} to {dest_dir}")
                except Exception as e:
                    logging.error(f"Error processing {filename}: {e}")
            else:
                logging.info(f"Ignored {filename} as it's not an image file")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
    return width, height
image_paths=glob.glob('/home/jack/Desktop/EXP_notebooks/alien/*.jpg')
for image_path in image_paths:
    imsizes.add(get_image_dimensions(image_path))
#print(len(imsizes))
for ims in imsizes:
    Im=str(ims)
    Im=Im.replace('(','')
    Im=Im.replace(')','')
    #print("Im: ",Im)
    SIZE=Im.split(',')
    width = int(SIZE[0])
    height = int(SIZE[1])
    print(str(width)+"x"+str(height))
    source_directory = '/home/jack/Desktop/EXP_notebooks/alien/'
    move_images(source_directory,width,height)
    
    #print(ims)

ALLOWED_EXTENSIONS = {'jpg', 'png', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def find_videos_in_directory(directory):
    video_files = []
    for root, dirs, files in os.walk(directory):
        # Restrict the search to the specified directory and its subdirectories
        if root.startswith(directory):
            for file in files:
                if allowed_file(file):
                    video_files.append(os.path.join(root, file))
    return video_files
directory="lexica_nubian/614x1075/"
find_videos_in_directory(directory)

ALLOWED_EXTENSIONS = {'jpg', 'png', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
image_files = []
def find_images_in_directory(directory):

    for root, dirs, files in os.walk(directory):
        # Restrict the search to the specified directory and its subdirectories
        if root.startswith(directory):
            for file in files:
                if allowed_file(file):
                    image_files.append(os.path.join(root, file))
    return video_files
directory="."
find_images_in_directory(directory)

for files in image_files:
    if "/614x" in files:
        print(files)




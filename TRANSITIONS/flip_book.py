'''
This script combines multiple images into a video using imageio and FFmpeg.
The script's results are stored in the output directory.
This is a very basic example of combining images into a video with a page flip effect.
Run the script with the path to the directory containing the images as an argument.
Example: python3 flip_books.py /home/jack/Desktop/HDD500/collections/images/backgrounds-01a
'''
import os
import subprocess
from PIL import Image
import glob
import random
import imageio
import numpy as np
from sys import argv
import shutil
import uuid
#/home/jack/Desktop/HDD500/collections/images/backgrounds-01a
collections ="/home/jack/Desktop/HDD500/collections"
image_directory = collections+"/images/backgrounds-01a/"
image_directory = argv[1]
output_directory = image_directory+"output_videos/"
print("image_directory",image_directory)
output_video_path = '576x768_combined_flip_books.mp4'
# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Get the list of images in the directory
image_list = sorted(glob.glob(image_directory + '*.jpg'))
random.shuffle(image_list)
print("image_list",len(image_list))

# Initialize a list to store the paths of generated videos
video_paths = []

# Iterate through consecutive pairs of images
for i in range(len(image_list) - 1):
    base_image_path = image_list[i]
    image_to_paste_path = image_list[i + 1]
    print("base_image_path",base_image_path)
    print("image_to_paste_path",image_to_paste_path)
    # Open the base image (the larger transparent PNG)
    base_image = Image.open(base_image_path).convert("RGBA")
    bs = base_image.size
    print("bs",bs)

    # Create a list to store individual frames
    IMG_SRC = []

    # Open each image to paste and create frames
    for j in range(0, bs[0], 15):
        current_frame = base_image.copy()
        image_to_paste = Image.open(image_to_paste_path).convert("RGBA")
        print("image_to_paste size",image_to_paste.size)
        image_to_paste = image_to_paste.resize((bs[0] - j, bs[1]), Image.BICUBIC)

        # Determine the position where you want to paste the smaller image on the larger image
        x = 0
        y = 0
        paste_position = (x, y)

        # Ensure that the smaller image is not larger than the base image
        if image_to_paste.size[0] + paste_position[0] <= base_image.size[0] and \
                image_to_paste.size[1] + paste_position[1] <= base_image.size[1]:
            # Paste the smaller image onto the larger image
            current_frame.paste(image_to_paste, paste_position, image_to_paste)

            # Append the current frame to the list
            IMG_SRC.append(np.array(current_frame))

    # Save the frames as an MP4 video using imageio
    output_video_path = f'{output_directory}output_video_{i}.mp4'
    print("output_video_path",output_video_path)
    imageio.mimsave(output_video_path, IMG_SRC, fps=30)

input_directory = output_directory
output_directory = "/home/jack/Desktop/EXPERIMENTAL/"
output_video_name = output_video_path

# Get the list of video files in the input directory
video_files = sorted([f for f in os.listdir(input_directory) if f.endswith(".mp4")])
random.shuffle(video_files)
# Create a text file containing the list of input videos for FFmpeg
input_list_path = os.path.join(output_directory, "input_list.txt")
with open(input_list_path, 'w') as input_list_file:
    for video_file in video_files:
        input_list_file.write(f"file '{os.path.join(input_directory, video_file)}'\n")
output_video_name = "final_result.mp4"
# Run FFmpeg to concatenate the videos
ffmpeg_command = f"ffmpeg -y -f concat -safe 0 -i {input_list_path} -c copy {output_video_name}"
subprocess.run(ffmpeg_command, shell=True)
#use uuid to create a unique name for the output video
output_video_name = "/home/jack/Desktop/HDD500/collections/vids/"+str(uuid.uuid4()) + ".mp4"
# copy the output video to the output directory /home/jack/Desktop/HDD500/collections/vids/
shutil.copyfile(output_video_path, os.path.join(output_directory, output_video_name))

random.shuffle(video_files)
# Create a text file containing the list of input videos for FFmpeg
input_list_path = os.path.join(output_directory, "input_list.txt")
with open(input_list_path, 'w') as input_list_file:
    for video_file in video_files:
        input_list_file.write(f"file '{os.path.join(input_directory, video_file)}'\n")
output_video_name = "final_result.mp4"
# Run FFmpeg to concatenate the videos
ffmpeg_command = f"ffmpeg -y -f concat -safe 0 -i {input_list_path} -c copy {output_video_name}"
subprocess.run(ffmpeg_command, shell=True)
#use uuid to create a unique name for the output video
output_video_name = "/home/jack/Desktop/HDD500/collections/vids/"+str(uuid.uuid4()) + ".mp4"
# copy the output video to the output directory /home/jack/Desktop/HDD500/collections/vids/
shutil.copyfile(output_video_path, os.path.join(output_directory, output_video_name))


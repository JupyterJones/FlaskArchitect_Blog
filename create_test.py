import os
from PIL import Image
from sys import argv
# Define the output video format
output_format = 'mp4'

# Define the output file name
output_filename = 'zoom_effect.mp4'

# Define the start frame
start_frame = 0

# Define the end frame
end_frame = len(os.listdir('.')) - 1

# Create an empty list to store frames
frames = []

# Loop through all image files in the directory
for filename in os.listdir(argv[1]):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Open the image file
        img = Image.open(f'./{filename}')
        
        # Add the current frame to the list
        frames.append(img)

# Convert the list of frames into a sequence of frames for FFMPEG
seq = [ImageSequenceWriter().convert(frames)]

# Use FFMPEG to write the sequence to a video file
ffmpeg.write(seq, output_filename)

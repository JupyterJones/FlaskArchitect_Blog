import os
import sys
import subprocess
from PIL import Image

# Directory containing the images
image_dir = sys.argv[1]

# Define the output video format
output_format = 'mp4'

# Define the output file name
output_filename = 'zoom_effect.mp4'

# Create an empty list to store frames
frames = []

# Loop through all image files in the directory
for filename in sorted(os.listdir(image_dir)):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Open the image file
        img = Image.open(os.path.join(image_dir, filename))
        
        # Add the current frame to the list
        frames.append(img)

# Directory to save individual frames
frame_dir = 'frames'
os.makedirs(frame_dir, exist_ok=True)

# Save frames as image files
for i, frame in enumerate(frames):
    frame.save(os.path.join(frame_dir, f'frame_{i:04d}.png'))

# Create video with zoom effect using ffmpeg
zoom_effect_command = [
    'ffmpeg', '-hide_banner', '-framerate', '60', '-i', os.path.join(frame_dir, 'frame_%04d.png'),
    '-vf', "scale=8000:-1,zoompan=z='zoom+0.001':x=iw/2-(iw/zoom/2):y=0:d=1:fps=60",
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-y', output_filename
]

# Execute the command
subprocess.run(zoom_effect_command)

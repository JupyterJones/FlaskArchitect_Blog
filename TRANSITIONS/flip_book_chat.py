import os
import subprocess
from PIL import Image
import glob
import random
import imageio
import numpy as np
import shutil
import uuid

def main(image_directory):
    # Create output directory for videos
    output_directory = os.path.join(image_directory, "output_videos")
    os.makedirs(output_directory, exist_ok=True)

    # Get list of images in the directory
    image_list = sorted(glob.glob(os.path.join(image_directory, '*.jpg')))
    random.shuffle(image_list)

    # Initialize list to store paths of generated videos
    video_paths = []

    # Iterate through consecutive pairs of images
    for i in range(len(image_list) - 1):
        base_image_path = image_list[i]
        image_to_paste_path = image_list[i + 1]

        # Open the base image (the larger transparent PNG)
        base_image = Image.open(base_image_path).convert("RGBA")
        bs = base_image.size

        # Create list to store individual frames
        IMG_SRC = []

        # Open each image to paste and create frames
        for j in range(0, bs[0], 15):
            current_frame = base_image.copy()
            image_to_paste = Image.open(image_to_paste_path).convert("RGBA")
            image_to_paste = image_to_paste.resize((bs[0] - j, bs[1]), Image.BICUBIC)

            # Determine position to paste smaller image on larger image
            x = 0
            y = 0
            paste_position = (x, y)

            # Ensure smaller image does not exceed base image dimensions
            if (image_to_paste.size[0] + paste_position[0] <= base_image.size[0] and
                image_to_paste.size[1] + paste_position[1] <= base_image.size[1]):
                # Paste smaller image onto larger image
                current_frame.paste(image_to_paste, paste_position, image_to_paste)

                # Append current frame to list
                IMG_SRC.append(np.array(current_frame))

        # Save frames as MP4 video using imageio
        output_video_path = os.path.join(output_directory, f'output_video_{i}.mp4')
        imageio.mimsave(output_video_path, IMG_SRC, fps=30)
        video_paths.append(output_video_path)

    # Concatenate generated videos into final video
    concatenated_video_path = os.path.join(output_directory, 'final_result.mp4')
    with open(os.path.join(output_directory, 'input_list.txt'), 'w') as input_list_file:
        for video_path in video_paths:
            input_list_file.write(f"file '{video_path}'\n")
    ffmpeg_command = f"ffmpeg -y -f concat -safe 0 -i {os.path.join(output_directory, 'input_list.txt')} -c copy {concatenated_video_path}"
    subprocess.run(ffmpeg_command, shell=True)

    # Generate unique name for output video using uuid
    output_video_name = os.path.join('/home/jack/Desktop/HDD500/collections/vids', str(uuid.uuid4()) + '.mp4')

    # Copy concatenated video to output directory
    shutil.copyfile(concatenated_video_path, output_video_name)

    # Clean up temporary files
    shutil.rmtree(output_directory)

# Check if script is run as main module
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python flip_book_chat.py <image_directory>")
        sys.exit(1)
    
    # Get image directory from command line argument
    image_directory = sys.argv[1]
    main(image_directory)

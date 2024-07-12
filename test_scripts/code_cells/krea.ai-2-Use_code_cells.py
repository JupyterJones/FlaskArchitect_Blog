!ls /mnt/HDD500/

import os
import shutil

# Function to get two sample images from directories with over 10 images
def get_sample_images(folder_path, samples_folder):
    # Create samples directory if it doesn't exist
    if not os.path.exists(samples_folder):
        os.makedirs(samples_folder)

    # Traverse directory
    for root, dirs, files in os.walk(folder_path):
        image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        if len(image_files) > 10:
            # Copy two sample images
            sample_images = image_files[:2]
            for image_file in sample_images:
                src_path = os.path.join(root, image_file)
                # Construct new filename
                new_filename = os.path.join(samples_folder, '_' + root.replace('/', '_') + '_' + image_file)
                # Copy file with new filename
                shutil.copy(src_path, new_filename)
                print(f"Copied {src_path} to {new_filename}")


# Specify the folder path to search for images
#folder_path = '/home/jack'
#folder_path = '/home/jack/Desktop/HDD500/'
folder_path = '/mnt/HDD500/'

# Specify the folder path to save sample images
samples_folder = 'SAMPLES'

# Call the function to get sample images from directories with over 10 images
get_sample_images(folder_path, samples_folder)
folder_path = '/home/jack'
get_sample_images(folder_path, samples_folder)

import os
import shutil

# Function to get two sample images from directories with over 10 images
def get_sample_images(folder_path, samples_folder):
    # Create samples directory if it doesn't exist
    if not os.path.exists(samples_folder):
        os.makedirs(samples_folder)

    # Traverse directory
    for root, dirs, files in os.walk(folder_path):
        image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        if len(image_files) > 10:
            # Copy two sample images
            sample_images = image_files[:2]
            for image_file in sample_images:
                src_path = os.path.join(root, image_file)
                dst_path = os.path.join(samples_folder, image_file.replace('/', '_'))
                shutil.copy(src_path, dst_path)
                print(f"Copied {src_path} to {dst_path}")

# Specify the folder path to search for images
#folder_path = '/home/jack'
#folder_path = '/home/jack/Desktop/HDD500/'
folder_path = '/mnt/HDD500/'

# Specify the folder path to save sample images
samples_folder = 'SAMPLES'

# Call the function to get sample images from directories with over 10 images
get_sample_images(folder_path, samples_folder)


import os
import datetime

# Function to find images created in the last two days
def find_images_last_two_days(folder_path):
    # Get current date
    current_date = datetime.datetime.now()

    # Calculate two days ago
    two_days_ago = current_date - datetime.timedelta(days=2)

    # List to store image files
    image_files = []

    # Traverse directory
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Check if the file is an image file and created within the last two days
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')) and \
                    os.path.getctime(file_path) > two_days_ago.timestamp():
                image_files.append(file_path)
                print(len(image_files),end='.')

    return image_files

# Specify the folder path where you want to search for images
#folder_path = '/home/jack'
#folder_path = '/home/jack/Desktop/HDD500/'
folder_path = '/mnt/HDD500/'

# Call the function to find images created in the last two days
images_last_two_days = find_images_last_two_days(folder_path)

# Specify the output file path
output_file_path = 'mnt_image_files_last_two_days.txt'

# Write the image file paths to the output file
with open(output_file_path, 'w') as file:
    for image_file in images_last_two_days:
        file.write(image_file + '\n')

print(f"Results saved to {output_file_path}")


import os
import datetime

# Function to find images created in the last two days
def find_images_last_two_days(folder_path):
    # Get current date
    current_date = datetime.datetime.now()

    # Calculate two days ago
    two_days_ago = current_date - datetime.timedelta(days=2)

    # List to store image files
    image_files = []

    # Traverse directory
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Check if the file is an image file and created within the last two days
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')) and \
                    os.path.getctime(file_path) > two_days_ago.timestamp():
                image_files.append(file_path)

    return image_files

# Specify the folder path where you want to search for images
folder_path = '/home/jack'

# Call the function to find images created in the last two days
images_last_two_days = find_images_last_two_days(folder_path)

# Print the list of image files
print("Images created in the last two days:")
for image_file in images_last_two_days:
    print(image_file)



/home/jack/Desktop/SCRIPTS/krea_orig/vokoscreenNG-2024-02-12_09-46-55.mkv



vid = sorted(glob.glob(Videos), key=lambda x: os.path.getmtime(x), reverse=True)


import glob
import os
#Videos="/home/jack/Desktop/HDD500/Videos/*.mkv"
#Videos="/home/jack/Desktop/SCRIPTS/krea_orig/*.mkv"
Videos="/home/jack/Desktop/SCRIPTS/krea_orig/*.mkv"
#Videos = "/path/to/videos/*.mp4"  # Replace with your actual path and file extension

# Get a list of video file paths
vid = sorted(glob.glob(Videos), key=lambda x: os.path.getctime(x),reverse=True)
VIDEOS=[]
# Print the sorted list
for video in vid:
    VIDEOS.append(video)
    #print(video)
print(VIDEOS[0])

import string
def remove_punctuation(DIR):
    return DIR.translate(str.maketrans('', '', string.punctuation))

Input_Video=VIDEOS[0]
import subprocess

def play_video_with_vlc(video_path):
    try:
        # Use subprocess to launch VLC player with the video file
        subprocess.run(['vlc', video_path])
    except Exception as e:
        print(f"Error: {e}")

# Replace '/path/to/your/video.mp4' with the actual path to your video file
video_path = VIDEOS[0]
#video_path = "/home/jack/Desktop/SCRIPTS/krea_orig/vokoscreenNG-2024-01-13_13-03-53.mkv"
play_video_with_vlc(video_path)

DIR=Input_Video.split("/")[-1]
new_dir=remove_punctuation(DIR)
print(new_dir)

print(VIDEOS[0][:-5])



import subprocess
import logging

# Configure logging
logging.basicConfig(filename='ffmpeg_remove_duplicates.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def remove_duplicate_frames(input_video, output_video):
    try:
        # Run ffmpeg command to remove duplicate frames
        ffmpeg_command = [
            'ffmpeg','-hide_banner',
            '-i', input_video,
            '-vf', 'mpdecimate,setpts=N/FRAME_RATE/TB',
            '-c:a', 'copy',
            '-y',
            output_video
        ]

        # Log the ffmpeg command
        logging.info(f'Running ffmpeg command: {" ".join(ffmpeg_command)}')

        # Execute the ffmpeg command
        subprocess.run(ffmpeg_command, check=True)

        logging.info('Duplicate frames removed successfully.')

    except subprocess.CalledProcessError as e:
    
        logging.error(f'Error occurred: {e}')
        raise
if __name__ == "__main__":
    #input_video_path = '/home/jack/Videos/vokoscreenNG-2023-12-20_13-20-32.mkv'
    input_video_path = VIDEOS[0]
    #output_video_path = VIDEOS[0][:-5]+"No_dups.mp4"
    input_video_path=video_path
    output_video_path=video_path[:-5]+"No_dups.mp4"
    print(output_video_path)

    # Call the function to remove duplicate frames
    remove_duplicate_frames(input_video_path, output_video_path)


!vlc {output_video_path}



#!ls /home/jack/Desktop/SCRIPTS/krea_orig/

!ls {output_video_path}

out_vid=VIDEOS[0][:-5]+"shorts.mp4"
print(out_vid)

out_vid=output_video_path[:-5]+"shorts.mp4"
print(out_vid)


!ffmpeg -i {output_video_path} -y -t 15 {out_vid}

!vlc {out_vid}


import os
import cv2
from datetime import datetime

def log_message(log_file_path, level, message):
    """
    Write a log message to the specified log file.
    
    Args:
    - log_file_path (str): Path to the log file.
    - level (str): Log level (e.g., INFO, ERROR).
    - message (str): Log message to be written.
    """
    # Get the directory of the log file
    log_directory = os.path.dirname(log_file_path)
    
    # Create the log directory if it doesn't exist
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Format the log message
    formatted_message = f"{timestamp} - {level} - {message}\n"

    # Write the message to the log file
    with open(log_file_path, 'a') as log_file:
        log_file.write(formatted_message)

def extract_frames(video_file, output_directory, log_file):
    """
    Extract frames from a video file and save them as JPG images.
    
    Args:
    - video_file (str): Path to the input video file.
    - output_directory (str): Directory to save the extracted frames.
    - log_file (str): Path to the log file.
    """
    try:
        # Open the video file
        cap = cv2.VideoCapture(video_file)

        # Create the output directory if it doesn't exist
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Extract and save frames
        frame_count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame_path = os.path.join(output_directory, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_path, frame)
            frame_count += 1
        cap.release()

        log_message(log_file, 'INFO', f"Successfully extracted {frame_count} frames from {video_file}")
    except Exception as e:
        log_message(log_file, 'ERROR', f"Error extracting frames from {video_file}: {str(e)}")

def main():
    # Specify the paths
    video_file = "vokoscreenNG-2024-02-12_09-46-5No_dupshorts.mp4"  # Change this to your input video file
    output_directory = "KREA_output_images/"  # Change this to the desired output folder
    log_file = 'extract_frames.log'
    
    # Call the extract_frames function
    extract_frames(video_file, output_directory, log_file)

if __name__ == "__main__":
    main()


import os
import cv2
from datetime import datetime

def log_message(log_file_path, level, message):
    log_directory = os.path.dirname(log_file_path)
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    formatted_message = f"{timestamp} - {level} - {message}\n"

    with open(log_file_path, 'a') as log_file:
        log_file.write(formatted_message)

def extract_frames(video_file, output_directory, log_file):
    try:
        cap = cv2.VideoCapture(video_file)

        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        frame_count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame_path = os.path.join(output_directory, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_path, frame)
            frame_count += 1
        cap.release()

        log_message(log_file, 'INFO', f"Successfully extracted {frame_count} frames from {video_file}")
    except Exception as e:
        log_message(log_file, 'ERROR', f"Error extracting frames from {video_file}: {str(e)}")

def main():
    video_file = "vokoscreenNG-2024-02-12_09-46-5No_dupshorts.mp4"  
    # Change this to your input video file
    output_directory = "KREA_output_images/"  # Change this to the desired output folder

    log_file = 'extract_frames.log'
    extract_frames(video_file, output_directory, log_file)

if __name__ == "__main__":
    main()


import logging

# Configure logging
logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Example usage of logging
def main():
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

if __name__ == "__main__":
    main()


import os
import moviepy.editor as mp
import logging

# Get the current directory
current_dir = os.getcwd()
log_file = os.path.join(current_dir, "conversion.log")

# Configure logging to save messages to both console and a log file
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    handlers=[logging.FileHandler(log_file),
                              logging.StreamHandler()])

def convert_video_to_images(video_path, output_folder):
    """
    Convert an MP4 video to JPG images.

    Parameters:
        video_path (str): Path to the input MP4 video file.
        output_folder (str): Path to the output folder where JPG images will be saved.
    """
    try:
        # Load the video clip
        clip = mp.VideoFileClip(video_path)
        
        # Print debug information
        logging.info(f"Video duration: {clip.duration} seconds")
        logging.info(f"Total frames: {clip.reader.nframes}")

        # Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Iterate over each frame and save it as a JPG image
        for i, frame in enumerate(clip.iter_frames()):
            output_path = os.path.join(output_folder, f"frame_{i}.jpg")
            logging.info(f"Saving frame {i} as {output_path}")
            mp.imsave(output_path, frame)

        logging.info("Conversion completed successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    video_path = "vokoscreenNG-2024-02-12_09-46-5No_dupshorts.mp4"  
    # Change this to your input video file
    output_folder = "KREA_output_images/"  # Change this to the desired output folder

    convert_video_to_images(video_path, output_folder)


!pwd

import os
from datetime import datetime

def log_message(log_file_path, level, message):
    """
    Write a log message to the specified log file.
    
    Args:
    - log_file_path (str): Path to the log file.
    - level (str): Log level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL).
    - message (str): Log message to be written.
    """
    # Create the directory if it doesn't exist
    log_directory = os.path.dirname(log_file_path)
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Format the log message
    formatted_message = f"{timestamp} - {level} - {message}\n"

    # Write the message to the log file
    with open(log_file_path, 'a') as log_file:
        log_file.write(formatted_message)

# Example usage of the logging function
def main():
    log_file_path = '/home/jack/Desktop/EXP_notebooks/example.log'
    log_message(log_file_path, 'DEBUG', 'This is a debug message')
    log_message(log_file_path, 'INFO', 'This is an info message')
    log_message(log_file_path, 'WARNING', 'This is a warning message')
    log_message(log_file_path, 'ERROR', 'This is an error message')
    log_message(log_file_path, 'CRITICAL', 'This is a critical message')

if __name__ == "__main__":
    main()


!cat example.log

!cat conversion.log

import os
import moviepy.editor as mp
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def convert_video_to_images(video_path, output_folder):
    """
    Convert an MP4 video to JPG images.

    Parameters:
        video_path (str): Path to the input MP4 video file.
        output_folder (str): Path to the output folder where JPG images will be saved.
    """
    try:
        # Load the video clip
        clip = mp.VideoFileClip(video_path)
        
        # Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Iterate over each frame and save it as a JPG image
        for i, frame in enumerate(clip.iter_frames()):
            output_path = os.path.join(output_folder, f"frame_{i}.jpg")
            print(output_path)
            mp.imsave(output_path, frame)
            logging.info(f"Saved frame {i} as {output_path}")

        logging.info("Conversion completed successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    video_path = "/home/jack/Desktop/SCRIPTS/krea_orig/vokoscreenNG-2024-02-12_09-46-5No_dupshorts.mp4"  # Change this to your input video file
    output_folder = "KREA_output_images/"  # Change this to the desired output folder

    convert_video_to_images(video_path, output_folder)


!ls KREA_output_images/

import subprocess
import logging

# Configure logging
logging.basicConfig(filename='ffmpeg_slow_down.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def slow_down_video(input_video, output_video, slowdown_factor):
    try:
        # Run ffmpeg command to slow down the video by a specified factor without audio
        ffmpeg_command = [
            'ffmpeg','-ss','1',
            '-i', input_video,
            '-vf', f'setpts={slowdown_factor}*PTS',
            '-an', '-y', # Remove audio
            output_video
        ]

        # Log the ffmpeg command
        logging.info(f'Running ffmpeg command: {" ".join(ffmpeg_command)}')

        # Execute the ffmpeg command
        subprocess.run(ffmpeg_command, check=True)

        logging.info(f'Video slowed down by {slowdown_factor} times without audio successfully.')

    except subprocess.CalledProcessError as e:
        logging.error(f'Error occurred: {e}')
        raise

if __name__ == "__main__":
    #input_video_path = '/home/jack/Desktop/SCRIPTS/all-in-one_no_dupesS.mp4'
    input_video_path = out_vid
    #output_video_path = '/home/jack/Desktop/SCRIPTS/all-in-one_no_dupesS_10_kdenlive_ready.mp4'
    output_video_path = out_vid[:-5]+'_slowed_5.mp4'
    slowdown_factor = 8.0  # Adjust this factor as needed

    # Call the function to slow down the video
    slow_down_video(input_video_path, output_video_path, slowdown_factor)
!vlc {output_video_path}

print(output_video_path)

!vlc {output_video_path}

!add_frame {output_video_path}

!vlc temp/final_output3.mp4



import os
from moviepy.video.io.VideoFileClip import VideoFileClip
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def split_video(input_path, output_dir, num_parts=6):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Open the video file
    video_clip = VideoFileClip(input_path)

    # Get the duration of the video
    total_duration = video_clip.duration

    # Calculate the duration for each part
    part_duration = total_duration / num_parts

    logger.info(f"Splitting {input_path} into {num_parts} equal parts.")

    # Loop through each part and write it to a new file
    for i in range(num_parts):
        start_time = i * part_duration
        end_time = (i + 1) * part_duration

        # Create a subclip
        subclip = video_clip.subclip(start_time, end_time)

        # Output file path
        output_path = os.path.join(output_dir, f"{i + 1}sound.mp4")

        # Write subclip to file
        subclip.write_videofile(output_path, codec="libx264", audio_codec="aac")

        logger.info(f"Part {i + 1} saved to {output_path}")

    # Close the video clip
    video_clip.close()

if __name__ == "__main__":
    # Input video file path
    input_video_path = "/home/jack/Videos/edited_original_sound.mp4"

    # Output directory for split videos
    output_directory = "/home/jack/Videos"

    # Number of parts to split the video into
    num_parts = 6

    # Call the split_video function
    split_video(input_video_path, output_directory, num_parts)


!mkdir mixamo

import cv2

vidcap = cv2.VideoCapture('mixamo.mp4')
success, image = vidcap.read()
count = 1

while success:
    # Save frame as image with zero-padded filename
    cv2.imwrite("mixamo/{:05d}.jpg".format(count), image)
    success, image = vidcap.read()
    count += 1



ffmpeg -i output2a.mp4 -vf setpts=4*PTS -an -y output_video.mp4

print(len(VIDEOS))

vid=VIDEOS[0]

!ls /mnt/HDD500/EXPER/static/assets/Title_Image02.png



!locate /MUSIC/

!ls /mnt/HDD500/collections/Music/*.mp3

%%writefile /usr/local/bin/add_frame
#!/home/jack/miniconda3/envs/cloned_base/bin/python
from moviepy.video.compositing.transitions import slide_in
from moviepy.video.fx import all
from moviepy.editor import *
import glob
import random
from PIL import Image
import cv2
import os
import uuid
import shutil
from sys import argv

def add_title_image(video_path, hex_color = "#A52A2A"):
    hex_color=random.choice(["#A52A2A","#ad1f1f","#16765c","#7a4111","#9b1050","#8e215d","#2656ca"])
    # Define the directory path
    directory_path = "temp"
    # Check if the directory exists
    if not os.path.exists(directory_path):
        # If not, create it
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created.")
    else:
        print(f"Directory '{directory_path}' already exists.") 
    # Load the video file and title image
    video_clip = VideoFileClip(video_path)
    print(video_clip.size)
    width, height = video_clip.size
    title_image_path = "/mnt/HDD500/EXPER/static/assets/Title_Image02.png"
    # Set the desired size of the padded video (e.g., video width + padding, video height + padding)
    padded_size = (width + 90, height + 90)

    # Calculate the position for centering the video within the larger frame
    x_position = (padded_size[0] - video_clip.size[0]) / 2
    y_position = (padded_size[1] - video_clip.size[1]) / 2
    #hex_color = "#09723c"
    # Remove the '#' and split the hex code into R, G, and B components
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)

    # Create an RGB tuple
    rgb_tuple = (r, g, b)

    # Create a blue ColorClip as the background
    blue_background = ColorClip(padded_size, color=rgb_tuple)

    # Add the video clip on top of the red background
    padded_video_clip = CompositeVideoClip([blue_background, video_clip.set_position((x_position, y_position))])
    padded_video_clip = padded_video_clip.set_duration(video_clip.duration)
    #title_image_path = "/home/jack/Desktop/EXPER/static/assets/Title_Image02.png"
    # Load the title image
    title_image = ImageClip(title_image_path)

    # Set the duration of the title image
    title_duration = video_clip.duration
    title_image = title_image.set_duration(title_duration)

    print(video_clip.size)
    # Position the title image at the center and resize it to fit the video dimensions
    #title_image = title_image.set_position(("left", "top"))
    title_image = title_image.set_position((0, -5))
    #video_clip.size = (620,620)
    title_image = title_image.resize(padded_video_clip.size)

    # Position the title image at the center and resize it to fit the video dimensions
    #title_image = title_image.set_position(("center", "center")).resize(video_clip.size)

    # Create a composite video clip with the title image overlay
    composite_clip = CompositeVideoClip([padded_video_clip, title_image])
    # Limit the length to 58 seconds
    composite_clip = composite_clip.subclip(0, 32)
    # Load a random background music
    mp3_files = glob.glob("/mnt/HDD500/FlaskAppArchitect_Flask_App_Creator/static/MUSIC/*.mp3")
    random.shuffle(mp3_files)

    # Now choose a random MP3 file from the shuffled list
    mp_music = random.choice(mp3_files)

    # Load the background music without setting duration
    music_clip = AudioFileClip(mp_music)
    music_clip = music_clip.subclip(0, 32)
    fade_duration = 1.0
    music_clip = music_clip.audio_fadein(fade_duration).audio_fadeout(fade_duration)
    # Set the audio of the composite clip to the background music
    composite_clip = composite_clip.set_audio(music_clip)
    output_path = 'temp/final_output3.mp4'
    # Export the final video with the background music
    composite_clip.write_videofile(output_path)
    uid = str(uuid.uuid4())  # Generate a unique ID using uuid
    mp4_file =  f"/home/jack/Desktop/HDD500/collections/vids/Ready_Post_{uid}.mp4"
    shutil.copyfile(output_path, mp4_file)     
    print(mp4_file)
    VIDEO = output_path
    return VIDEO
if __name__=="__main__":
    #video_path = "/mnt/HDD500/EXPER/static/assets/Title_Image02.png"
    video_path = argv[1]
    add_title_image(video_path, hex_color = "#A52A2A")    


/home/jack/Desktop/SCRIPTS/krea_orig/vokoscreenNG-2024-01-14_22-30-05.mkv

print(VIDEOS[0])



import cv2
import ipywidgets as widgets
from IPython.display import display, clear_output

def play_video(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open the video file.")
        return

    # Create an output widget for displaying video frames
    out = widgets.Output()
    display(out)

    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # Check if the video has ended
        if not ret:
            break

        # Display the frame in the output widget
        with out:
            clear_output(wait=True)
            _, img = cv2.imencode('.jpeg', cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            display(widgets.Image(value=img.tobytes(), format='jpeg'))

        try:
            # Attempt to capture keyboard input
            key = cv2.waitKey(25) & 0xFF

            # Exit the loop when the user presses 'q'
            if key == ord('q'):
                break
        except KeyboardInterrupt:
            # Handle KeyboardInterrupt (e.g., stop button in Jupyter)
            break

    # Release the video capture object
    cap.release()

# Replace '/path/to/your/video.mp4' with the actual path to your video file
video_path = VIDEOS[0]
play_video(video_path)


import cv2
import ipywidgets as widgets
from IPython.display import display, clear_output

def play_video(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open the video file.")
        return

    # Create an output widget for displaying video frames
    out = widgets.Output()
    display(out)

    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # Check if the video has ended
        if not ret:
            break

        # Display the frame in the output widget
        with out:
            clear_output(wait=True)
            cv2.imshow('Video Player', frame)
            display(frame)

        try:
            # Attempt to capture keyboard input
            key = cv2.waitKey(25) & 0xFF

            # Exit the loop when the user presses 'q'
            if key == ord('q'):
                break
        except KeyboardInterrupt:
            # Handle KeyboardInterrupt (e.g., stop button in Jupyter)
            break

    # Release the video capture object
    cap.release()

# Replace '/path/to/your/video.mp4' with the actual path to your video file
video_path = VIDEOS[0]
play_video(video_path)


import cv2

def play_video(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open the video file.")
        return

    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # Check if the video has ended
        if not ret:
            break

        # Display the frame
        cv2.imshow('Video Player', frame)

       
    # Release the video capture object and close the window
    cap.release()
    cv2.destroyAllWindows()

# Replace '/path/to/your/video.mp4' with the actual path to your video file
video_path = VIDEOS[1]
play_video(video_path)


!ls /home/jack/Desktop/SCRIPTS/krea_orig/vokoscreenNG-2024-01-13_13-03-53.mkv


/home/jack/Videos/vokoscreenNG-2023-12-19_20-01-14.mkv
/home/jack/Videos/edited_original.mp4
/home/jack/Videos/vokoscreenNG-2023-12-20_13-20-32.mkv


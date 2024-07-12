import sys
import glob
import random
import sqlite3
import os
import datetime
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
from moviepy.editor import ImageClip, concatenate_videoclips, CompositeVideoClip
THE_GOAL = '''\n
open an image directory and select a random 3 images
'''
STEPS='''\n
    1. create a logger
    2. Create a database of transition steps between images.
    3. Save transition steps to the database.
    4. Retrieve transition steps from the database.
    5. Recreate the transition clips from the database entries.
    6. Save transition clips to the database.
    7. Retrieve transition clips from the database.
    8. Recreate the transition clips from the database entries.
    9. Create a video of the transition clips.
 A. Implement logit function to log events:
    Status: complete   
 B. Implement initialize_db function to initialize the database:
    Status: complete
 C. :    
'''
# Logit function to log events
def logit(argvs):
    argv = argvs   
    log_file = "dbzoom_log.txt"  # Replace with the actual path to your log file
    timestamp = datetime.datetime.now().strftime("%A_%b-%d-%Y_%H-%M-%S")
    with open(log_file, "a") as log:
        log.write(f"{timestamp}: {argv}\n")

logit("Starting dbzoom.py")

def initialize_db(conn):
    logging.info("Initializing the database")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transitions (
            id INTEGER PRIMARY KEY,
            step INTEGER,
            image1 TEXT,
            image2 TEXT,
            duration INTEGER
        )
    ''')
    conn.commit()

from PIL import Image
import moviepy.editor as mpy
import os

def create_zoom_frames(image_path, output_dir, num_frames=300, zoom_factor=1.15):
    """Create zoom effect frames and save them."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    img = Image.open(image_path)
    width, height = img.size
    width =width*.25
    height = height*.25


    center_x, center_y = width // 2, height // 2

    for i in range(num_frames):
        scale = 1 + (zoom_factor - 1) * (i / (num_frames - 1))
        new_width = int(width * scale)
        new_height = int(height * scale)
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        left = (new_width - width) // 2
        top = (new_height - height) // 2
        right = left + width
        bottom = top + height
        cropped_img = resized_img.crop((left, top, right, bottom))
        frame_path = os.path.join(output_dir, f"frame_{i:03d}.png")
        cropped_img.save(frame_path)
        print(f"Saved {frame_path}")

def create_zoom_video(frames_dir, output_video_path, fps=30):
    """Create a video from saved frames."""
    frame_files = [os.path.join(frames_dir, f) for f in sorted(os.listdir(frames_dir)) if f.endswith('.png')]
    clips = [mpy.ImageClip(m).set_duration(1/fps) for m in frame_files]
    video = mpy.concatenate_videoclips(clips, method="compose")
    video.write_videofile(output_video_path, fps=fps)
    print(f"Saved video: {output_video_path}")

def main():
    image_path = '/home/jack/Desktop/FlaskArchitect/static/images/stari-june8/00003.jpg'  # Replace with the path to your image
    output_frames_dir = 'zoom_frames'
    output_video_path = 'zoom_effect.mp4'

    # Create zoom effect frames
    create_zoom_frames(image_path, output_frames_dir)

    # Create video from frames
    create_zoom_video(output_frames_dir, output_video_path)

if __name__ == '__main__':
    main()









"""



def save_transition_step(conn, step, image1, image2, duration):
    logging.info(f"Saving transition step {step} to database")
    cursor = conn.cursor()
    
    # Insert the transition data into the database
    cursor.execute('''
        INSERT INTO transitions (step, image1, image2, duration)
        VALUES (?, ?, ?, ?)
    ''', (step, image1, image2, duration))
    
    conn.commit()
    logging.info(f"Transition step {step} saved successfully")

def get_transition_steps(conn):
    logging.info("Retrieving transition steps from database")
    cursor = conn.cursor()
    
    # Retrieve all transition steps from the database
    cursor.execute('''
        SELECT image1, image2, duration FROM transitions ORDER BY step
    ''')
    rows = cursor.fetchall()
    
    if rows:
        logging.info("Transition steps retrieved successfully")
        return rows
    else:
        logging.warning("No transition steps found in database")
        return []

def zoom_image(image_path, zoom=5.0):
    # Load the image and calculate the new dimensions
    zoomed_img = Image.open(image_path)
    img = Image.open(image_path)
    width, height = img.size
    crop=5
    zoom_img = zoomed_img.resize((width+crop, height+crop))
    # cropped image = original image size
    zoom_img = zoom_img.crop((crop//2, crop//2, width+crop//2, height+crop//2))

    # Calculate the crop size
    crop_size = min(width, height)

    # Calculate the new width and height based on the zoom factor
    new_width = int(width * zoom)
    new_height = int(height * zoom)

    # Calculate the crop coordinates
    x = (new_width - crop_size) // 2
    y = (new_height - crop_size) // 2
    
    # Convert the zoom image to RGB mode
    zoom_img = zoom_img.convert("RGB")
    
    # Construct the zoom image path
    base, ext = os.path.splitext(image_path)
    zoom_img_path = f"{base}_zoom{ext}"
    
    zoom_img.save(zoom_img_path)
    return zoom_img_path

def create_transition(image1, image2, duration=20):
    # Create a transition effect between two images over 20 seconds
    logging.info("Creating transition effect")
    clip1 = ImageClip(image1).set_duration(duration).crossfadeout(duration)
    clip2 = ImageClip(image2).set_duration(duration).crossfadein(duration)
    
    # Composite clip to combine the two clips
    transition_clip = CompositeVideoClip([clip1, clip2.set_start(duration / 2)])
    
    return transition_clip

# Create an in-memory SQLite database
conn = sqlite3.connect(':memory:')
initialize_db(conn)

# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.error("Please provide the path to the image directory")
        sys.exit(1)
    
    image_dir = sys.argv[1]
    image_files = glob.glob(f"{image_dir}/*.jpg")
    
    if len(image_files) < 3:
        logging.error("Please provide at least 3 images in the directory")
        sys.exit(1)
    
    # Randomly select 3 images
    selected_images = random.sample(image_files, 3)
    logging.info(f"Selected images: {selected_images}")
    
    # Quantize selected images
    zoom_images = [quantize_image(image) for image in selected_images]
    
    # Create transition clips
    transition1 = create_transition(zoom_images[0], zoom_images[1], duration=20)
    transition2 = create_transition(zoom_images[1], zoom_images[2], duration=20)
    
    # Save transition steps to the database
    save_transition_step(conn, 1, zoom_images[0], zoom_images[1], 20)
    save_transition_step(conn, 2, zoom_images[1], zoom_images[2], 20)
    
    # Retrieve transition steps from the database
    transition_steps = get_transition_steps(conn)
    
    # Recreate the transition clips from the database entries
    recreated_clips = [create_transition(image1, image2, duration) for image1, image2, duration in transition_steps]
    
    # Concatenate the transition clips to create the final video
    final_video = concatenate_videoclips(recreated_clips)
    final_video.write_videofile("result.mp4", fps=24)
    
    # Close the connection
    conn.close()
"""
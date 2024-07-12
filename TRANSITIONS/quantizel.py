import sys
import glob
import random
import sqlite3
import logging
import os
from PIL import Image
from moviepy.editor import ImageClip, concatenate_videoclips, CompositeVideoClip

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def initialize_db(conn):
    logging.info("Initializing the database")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transitions (
            id INTEGER PRIMARY KEY,
            step INTEGER,
            image_path TEXT,
            num_colors INTEGER
        )
    ''')
    conn.commit()

def save_transition_step(conn, step, image_path, num_colors):
    logging.info(f"Saving transition step {step} to database")
    cursor = conn.cursor()
    
    # Insert the transition data into the database
    cursor.execute('''
        INSERT INTO transitions (step, image_path, num_colors)
        VALUES (?, ?, ?)
    ''', (step, image_path, num_colors))
    
    conn.commit()
    logging.info(f"Transition step {step} saved successfully")

def get_transition_steps(conn):
    logging.info("Retrieving transition steps from database")
    cursor = conn.cursor()
    
    # Retrieve all transition steps from the database
    cursor.execute('''
        SELECT image_path, num_colors FROM transitions ORDER BY step
    ''')
    rows = cursor.fetchall()
    
    if rows:
        logging.info("Transition steps retrieved successfully")
        return rows
    else:
        logging.warning("No transition steps found in database")
        return []

def quantize_image(image_path, num_colors):
    logging.info(f"Quantizing image: {image_path} to {num_colors} colors")
    img = Image.open(image_path)
    quantized_img = img.quantize(colors=num_colors, method=Image.MEDIANCUT)
    
    # Convert the quantized image to RGB mode
    quantized_img = quantized_img.convert("RGB")
    
    # Construct the quantized image path
    base, ext = os.path.splitext(image_path)
    quantized_img_path = f"{base}_quantized_{num_colors}{ext}"
    
    quantized_img.save(quantized_img_path)
    return quantized_img_path

def create_transition(image1, image2, duration=5):
    # Create a transition effect between two images over specified duration
    logging.info(f"Creating transition effect from {image1} to {image2} over {duration} seconds")
    
    clip1 = ImageClip(image1).set_duration(duration)
    clip2 = ImageClip(image2).set_duration(duration)
    
    # Fade in the second image while fading out the first image
    transition_clip = CompositeVideoClip([clip1.crossfadeout(duration), clip2.crossfadein(duration)])
    
    return transition_clip

# Create an in-memory SQLite database
conn = sqlite3.connect('Images.db')
initialize_db(conn)

# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.error("Please provide the path to the image directory")
        sys.exit(1)
    
    image_dir = sys.argv[1]
    print(image_dir)
    image_files = glob.glob(f"{image_dir}/*.jpg")
    
    if len(image_files) < 2:
        logging.error("Please provide at least 2 images in the directory")
        sys.exit(1)
    
    # Sort image files to ensure consistent order
    image_files.sort()
    
    # Quantization steps from 256 down to 6 colors
    colors = list(range(256, 5, -5))
    
    # Quantize images gradually and save transition steps
    for i in range(len(image_files)):
        if i == len(image_files) - 1:
            break
        
        image1 = image_files[i]
        image2 = image_files[i + 1]
        
        for num_colors in colors:
            quantized_image2 = quantize_image(image2, num_colors)
            save_transition_step(conn, i * len(colors) + (256 - num_colors) // 5, quantized_image2, num_colors)
    
    # Retrieve transition steps from the database
    transition_steps = get_transition_steps(conn)
    
    # Create transition clips from retrieved steps
    transition_clips = []
    for idx, (image_path, num_colors) in enumerate(transition_steps):
        if idx == 0:
            continue
        
        prev_image_path, _ = transition_steps[idx - 1]
        transition_clip = create_transition(prev_image_path, image_path, duration=5)
        transition_clips.append(transition_clip)
    
    # Concatenate transition clips to create the final video
    final_video = concatenate_videoclips(transition_clips)
    final_video.write_videofile("result.mp4", fps=24)
    
    # Close the connection
    conn.close()

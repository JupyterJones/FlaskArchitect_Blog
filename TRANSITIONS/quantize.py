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
            image1 TEXT,
            image2 TEXT,
            duration INTEGER
        )
    ''')
    conn.commit()

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

def quantize_image(image_path, num_colors=16):
    logging.info(f"Quantizing image: {image_path} to {num_colors} colors")
    img = Image.open(image_path)
    quantized_img = img.quantize(colors=num_colors, method=Image.MEDIANCUT)
    
    # Convert the quantized image to RGB mode
    quantized_img = quantized_img.convert("RGB")
    
    # Construct the quantized image path
    base, ext = os.path.splitext(image_path)
    quantized_img_path = f"{base}_quantized{ext}"
    
    quantized_img.save(quantized_img_path)
    return quantized_img_path

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
    quantized_images = [quantize_image(image) for image in selected_images]
    
    # Create transition clips
    transition1 = create_transition(quantized_images[0], quantized_images[1], duration=20)
    transition2 = create_transition(quantized_images[1], quantized_images[2], duration=20)
    
    # Save transition steps to the database
    save_transition_step(conn, 1, quantized_images[0], quantized_images[1], 20)
    save_transition_step(conn, 2, quantized_images[1], quantized_images[2], 20)
    
    # Retrieve transition steps from the database
    transition_steps = get_transition_steps(conn)
    
    # Recreate the transition clips from the database entries
    recreated_clips = [create_transition(image1, image2, duration) for image1, image2, duration in transition_steps]
    
    # Concatenate the transition clips to create the final video
    final_video = concatenate_videoclips(recreated_clips)
    final_video.write_videofile("result.mp4", fps=24)
    
    # Close the connection
    conn.close()

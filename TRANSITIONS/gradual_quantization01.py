import sys
import glob
import random
import datetime
import sqlite3
import os
from PIL import Image
from moviepy.editor import ImageClip, concatenate_videoclips, CompositeVideoClip

# Logit function to log events
def logit(message):
    timestamp = datetime.datetime.now().strftime("%A_%b-%d-%Y_%H-%M-%S")
    log_message = f"{timestamp}: {message}"
    print(log_message)
    with open("app_log.txt", "a") as log_file:
        log_file.write(log_message + "\n")

def initialize_db(conn):
    logit("Initializing the database")
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
    logit(f"Saving transition step {step} to database")
    cursor = conn.cursor()
    
    # Insert the transition data into the database
    cursor.execute('''
        INSERT INTO transitions (step, image_path, num_colors)
        VALUES (?, ?, ?)
    ''', (step, image_path, num_colors))
    
    conn.commit()
    logit(f"Transition step {step} saved successfully")

def get_transition_steps(conn):
    logit("Retrieving transition steps from database")
    cursor = conn.cursor()
    
    # Retrieve all transition steps from the database
    cursor.execute('''
        SELECT image_path, num_colors FROM transitions ORDER BY step
    ''')
    rows = cursor.fetchall()
    
    if rows:
        logit("Transition steps retrieved successfully")
        return rows
    else:
        logit("No transition steps found in database")
        return []

def quantize_image(image_path, num_colors):
    logit(f"Quantizing image: {image_path} to {num_colors} colors")
    img = Image.open(image_path)
    quantized_img = img.quantize(colors=num_colors, method=Image.MEDIANCUT)
    
    # Convert the quantized image to RGB mode
    quantized_img = quantized_img.convert("RGB")
    
    # Save the quantized image path to the database
    base, ext = os.path.splitext(image_path)
    quantized_img_path = f"{base}_quantized_{num_colors}{ext}"
    quantized_img.save(quantized_img_path)
    
    return quantized_img_path

def create_transition(image1, image2, duration=5):
    # Create a transition effect between two images over specified duration
    logit(f"Creating transition effect from {image1} to {image2} over {duration} seconds")
    
    clip1 = ImageClip(image1).set_duration(duration)
    clip2 = ImageClip(image2).set_duration(duration)
    
    # Fade in the second image while fading out the first image
    transition_clip = CompositeVideoClip([clip1.crossfadeout(duration), clip2.crossfadein(duration)])
    
    return transition_clip

if __name__ == "__main__":
    print("Starting Gradual Quantization")
    logit("Starting Gradual Quantization")
    
    # Connect to the SQLite database
    conn = sqlite3.connect('3.db')
    initialize_db(conn)
    
    # Read image directory from command line argument
    if len(sys.argv) < 2:
        logit("Please provide the image directory as a command line argument")
        sys.exit(1)
    
    image_dir = sys.argv[1]
    logit(f"Image directory: {image_dir}")
    
    # Validate directory existence
    if not os.path.exists(image_dir):
        logit(f"Directory {image_dir} does not exist")
        sys.exit(1)
    
    # List all .jpg files in the directory
    image_files = glob.glob(f"{image_dir}/*.jpg")
    
    # Validate image files existence and count
    if len(image_files) < 2:
        logit("Please provide at least 2 images in the directory")
        sys.exit(1)
    
    # Shuffle and select 3 random images
    random.shuffle(image_files)
    image_files = random.sample(image_files, 3)
    
    # Quantization steps from 256 down to 6 colors
    colors = list(range(256, 6, -2))
    
    # Quantize images gradually and save transition steps
    for i in range(len(image_files) - 1):
        image1 = image_files[i]
        image2 = image_files[i + 1]
        
        for num_colors in colors:
            # Quantize image2 and save the path to the database
            quantized_img_path = quantize_image(image2, num_colors)
            save_transition_step(conn, i * len(colors) + (256 - num_colors) // 10, quantized_img_path, num_colors)
    
    # Retrieve transition steps from the database
    transition_steps = get_transition_steps(conn)
    
    # Create transition clips from retrieved steps
    transition_clips = []
    for idx, (quantized_img_path, num_colors) in enumerate(transition_steps):
        if idx == 0:
            continue
        
        prev_quantized_img_path, _ = transition_steps[idx - 1]
        transition_clip = create_transition(prev_quantized_img_path, quantized_img_path, duration=.5)
        transition_clips.append(transition_clip)
    
    # Concatenate transition clips to create the final video
    final_video = concatenate_videoclips(transition_clips)
    final_video.write_videofile("result.mp4", fps=24)
    
    # Close the connection
    conn.close()

import sqlite3
import os
from PIL import Image, ImageOps
import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database setup
DB_NAME = 'images.db'
TABLE_NAME = 'processed_images'

def create_database():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image BLOB NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    logging.info("Database and table created successfully.")

def save_image_to_db(image_data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(f'''
        INSERT INTO {TABLE_NAME} (image) VALUES (?)
    ''', (sqlite3.Binary(image_data),))
    conn.commit()
    conn.close()
    logging.info("Image saved to database successfully.")

def apply_perspective(image):
    width, height = image.size
    coeffs = (
        1, -0.15, 0,  # left side
        0, 1, 0,      # top side
        0, 0, 1       # bottom side
    )
    transformed_image = image.transform((width, height), Image.PERSPECTIVE, coeffs, Image.BICUBIC)
    return transformed_image

def main(image_path, output_dir, iterations=200):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    original_image = Image.open(image_path)
    width, height = original_image.size
    current_image = original_image

    for i in range(iterations):
        logging.info(f"Processing iteration {i + 1}/{iterations}...")
        
        # Apply perspective transformation
        transformed_image = apply_perspective(current_image)
        
        # Slightly resize the image larger
        new_size = (int(width * 1.15), int(height * 1.15))
        resized_image = transformed_image.resize(new_size, resample=3)
        
        # Crop back to original size
        left = (resized_image.width - width) // 2
        top = (resized_image.height - height) // 2
        right = (resized_image.width + width) // 2
        bottom = (resized_image.height + height) // 2
        cropped_image = resized_image.crop((left, top, right, bottom))
        
        # Save to database
        img_byte_arr = cropped_image.tobytes()
        save_image_to_db(img_byte_arr)
        
        # Save the image to the output directory for verification (optional)
        cropped_image.save(os.path.join(output_dir, f'image_{i+1}.png'))
        
        # Update the current image for the next iteration
        current_image = cropped_image

    logging.info("Processing complete.")

if __name__ == '__main__':
    create_database()
    main('static/images/00001.jpg', 'output_images')

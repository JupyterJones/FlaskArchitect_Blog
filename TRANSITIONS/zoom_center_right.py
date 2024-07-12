import sqlite3
import io
from PIL import Image
import numpy as np
import cv2
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

def save_image_to_db(image):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    c.execute(f'''
        INSERT INTO {TABLE_NAME} (image) VALUES (?)
    ''', (sqlite3.Binary(img_byte_arr),))
    conn.commit()
    conn.close()
    logging.info("Image saved to database successfully.")

def retrieve_images_from_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(f'SELECT image FROM {TABLE_NAME}')
    rows = c.fetchall()
    images = [Image.open(io.BytesIO(row[0])) for row in rows]
    conn.close()
    logging.info("Images retrieved from database successfully.")
    return images

def apply_perspective_and_zoom(image, perspective_factor, scale_factor):
    width, height = image.size
    
    coeffs = (
        1 + perspective_factor, perspective_factor, -width * perspective_factor / 2,
        0, 1 + perspective_factor, -height * perspective_factor / 2,
        0, 0, 1
    )
    
    transformed_image = image.transform((width, height), Image.PERSPECTIVE, coeffs, resample=3)

    new_size = (int(width * scale_factor), int(height * scale_factor))
    resized_image = transformed_image.resize(new_size, resample=3)

    left = (resized_image.width - width) // 2
    top = (resized_image.height - height) // 2
    right = left + width
    bottom = top + height
    cropped_image = resized_image.crop((left, top, right, bottom))

    return cropped_image

def main(image_path, iterations=200):
    original_image = Image.open(image_path)
    width, height = original_image.size
    perspective_increment = 0.001  # Incremental perspective change per iteration
    scale_increment = 0.005  # Incremental zoom scale per iteration

    for i in range(iterations):
        logging.info(f"Processing iteration {i + 1}/{iterations}...")
        perspective_factor = perspective_increment * (i + 1)
        scale_factor = 1 + (scale_increment * (i + 1))
        transformed_image = apply_perspective_and_zoom(original_image, perspective_factor, scale_factor)
        save_image_to_db(transformed_image)

    logging.info("Processing complete.")
    create_video_from_db()

def create_video_from_db():
    images = retrieve_images_from_db()
    if not images:
        logging.error("No images found in the database.")
        return

    width, height = images[0].size
    video_path = 'output_video.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(video_path, fourcc, 10, (width, height))

    for image in images:
        frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        video.write(frame)
        logging.info("Added frame to video.")

    video.release()
    logging.info(f"Video created successfully: {video_path}")

if __name__ == '__main__':
    create_database()
    main('static/images/00001.jpg')

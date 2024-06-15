import sqlite3
import os
import base64

# Database and image file paths
DATABASE = 'test.db'
IMAGE_FILE = 'static/images/logo.jpg'
OUTPUT_IMAGE = 'db_image.jpg'

# Initialize SQLite database and create table
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                data BLOB NOT NULL
            )
        ''')
        conn.commit()

# Insert image into database
def insert_image(filename):
    with open(filename, 'rb') as file:
        image_data = file.read()
        image_data = base64.b64encode(image_data).decode('utf-8')  # Encode as base64
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO images (filename, data) VALUES (?, ?)', (os.path.basename(filename), image_data))
        conn.commit()

# Retrieve image from database and save as a file
def retrieve_image(output_filename):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT data FROM images LIMIT 1')
        image_data = cursor.fetchone()[0]
        image_data = base64.b64decode(image_data)  # Decode base64 to binary
    with open(output_filename, 'wb') as file:
        file.write(image_data)

# Main function
def main():
    # Initialize the database and create table
    init_db()

    # Insert the image into the database
    insert_image(IMAGE_FILE)
    print(f'Inserted image {IMAGE_FILE} into database {DATABASE}.')

    # Retrieve the image from the database and save as a new file
    retrieve_image(OUTPUT_IMAGE)
    print(f'Retrieved image and saved as {OUTPUT_IMAGE}.')

if __name__ == '__main__':
    main()

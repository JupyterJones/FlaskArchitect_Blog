import os
import sqlite3
import io
from PIL import Image
import moviepy.editor as mpy
import numpy as np

def create_zoom_frames(image_path, conn, num_frames=300, zoom_factor=2.0):
    """Create zoom effect frames and save them to the database."""
    img = Image.open(image_path)
    width, height = img.size
    width=width*.25
    height=height*.25
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS frames (
                        id INTEGER PRIMARY KEY,
                        frame BLOB NOT NULL
                      )''')

    for i in range(num_frames):
        scale = 1 + (zoom_factor - 1) * (i / (num_frames - 1))
        print(f"Creating frame {i + 1}/{num_frames} with scale {scale}")
        new_width = int(width * scale)
        new_height = int(height * scale)
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        left = (new_width - width) // 2
        top = (new_height - height) // 2
        right = left + width
        bottom = top + height
        cropped_img = resized_img.crop((left, top, right, bottom))
        # Convert cropped_img to numpy array and check shape
        img_array = np.array(cropped_img)
        if len(img_array.shape) == 3:  # img is an RGB(A) numpy array
            img_array = img_array[..., :3]  # Drop alpha channel if present

        # Save frame to in-memory bytes buffer
        buffer = io.BytesIO()
        Image.fromarray(img_array).save(buffer, format='PNG')
        buffer.seek(0)

        # Insert the frame into the database
        cursor.execute('INSERT INTO frames (frame) VALUES (?)', (buffer.read(),))
        conn.commit()

        print(f"Saved frame {i + 1}/{num_frames} to database")

def retrieve_frames(conn):
    """Retrieve frames from the database and return them as a list of Image objects."""
    cursor = conn.cursor()
    cursor.execute('SELECT frame FROM frames ORDER BY id')
    frames = cursor.fetchall()
    images = []

    for frame in frames:
        buffer = io.BytesIO(frame[0])
        img = Image.open(buffer)
        images.append(img)

    return images

def create_zoom_video(images, output_video_path, fps=30):
    """Create a video from a list of Image objects."""
    clips = [mpy.ImageClip(np.array(img)).set_duration(1/fps) for img in images]
    video = mpy.concatenate_videoclips(clips, method="compose")
    video.write_videofile(output_video_path, fps=fps)
    print(f"Saved video: {output_video_path}")

def main():
    image_path =  '/mnt/HDD500/FlaskArchitect/static/images/may29/00001.jpg'  # Replace with the path to your image
    output_video_path = 'zoom_center.mp4'
    db_path = 'zoom_center.db'

    # Create a connection to the database
    conn = sqlite3.connect(db_path)

    # Create zoom effect frames and save them to the database
    create_zoom_frames(image_path, conn)

    # Retrieve frames from the database
    frames = retrieve_frames(conn)

    # Create video from frames
    create_zoom_video(frames, output_video_path)

    # Close the database connection
    conn.close()

if __name__ == '__main__':
    main()

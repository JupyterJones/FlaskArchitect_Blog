import sqlite3
import io
from PIL import Image, ImageEnhance
import numpy as np
import moviepy.editor as mpy

def create_zoom_frames(image_path, db_path, num_frames=500, zoom_factor=3.5):
    """Create zoom effect frames and save them to the database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS frames (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            frame BLOB NOT NULL
        )
    ''')

    img = Image.open(image_path)
    width, height = img.size

    for i in range(num_frames):
        scale = 1 + (zoom_factor - 1) * (i / (num_frames - 1))
        new_width = int(width * scale)
        new_height = int(height * scale)
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)

        # Calculate cropping coordinates for top center focus
        left = (new_width - width) // 2
        top = 0
        right = left + width
        bottom = height

        cropped_img = resized_img.crop((left, top, right, bottom))
        
        # Save frame to database
        buffer = io.BytesIO()
        cropped_img.save(buffer, format="PNG")
        cursor.execute('INSERT INTO frames (frame) VALUES (?)', (buffer.getvalue(),))
        print(f"Saved frame {i + 1}/{num_frames} to database")

    conn.commit()
    conn.close()

def retrieve_frames(conn):
    """Retrieve frames from the database and return them as a list of Image objects."""
    cursor = conn.cursor()
    cursor.execute('SELECT frame FROM frames ORDER BY id')
    frames = cursor.fetchall()
    images = []

    for frame in frames:
        buffer = io.BytesIO(frame[0])
        img = Image.open(buffer)
        images.append(np.array(img))

    return images

def create_video_from_db(db_path, output_video_path, fps=30):
    """Create a video from frames stored in the database."""
    conn = sqlite3.connect(db_path)
    
    # Retrieve frames from the database
    frames = retrieve_frames(conn)
    
    # Create a video from the frames
    clips = [mpy.ImageClip(img).set_duration(1/fps) for img in frames]
    video = mpy.concatenate_videoclips(clips, method="compose")
    video.write_videofile(output_video_path, fps=fps)
    
    print(f"Saved video: {output_video_path}")
    
    conn.close()

def main():
    image_path = '/home/jack/Desktop/FlaskArchitect/static/images/june2/00003.jpg'  # Replace with the path to your image
    db_path = 'frames500.db'  # Path to your SQLite database
    output_video_path = 'zoom_effect-500.mp4'  # Output video file path

    # Create zoom effect frames and save them to the database
    create_zoom_frames(image_path, db_path)

    # Create a video from frames stored in the database
    create_video_from_db(db_path, output_video_path)

if __name__ == '__main__':
    main()

import sqlite3
import io
from PIL import Image
import numpy as np
import moviepy.editor as mpy

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

def create_video_from_db(db_path, output_video_path, fps=30):
    """Create a video from frames stored in the database."""
    # Connect to the database
    conn = sqlite3.connect(db_path)
    
    # Retrieve frames from the database
    frames = retrieve_frames(conn)
    
    # Convert PIL Images to NumPy arrays
    numpy_frames = [np.array(img) for img in frames]

    # Create a video from the frames
    clips = [mpy.ImageClip(img).set_duration(1/fps) for img in numpy_frames]
    video = mpy.concatenate_videoclips(clips, method="compose")
    video.write_videofile(output_video_path, fps=fps)
    
    print(f"Saved video: {output_video_path}")
    
    # Close the database connection
    conn.close()

def main():
    db_path = 'frames.db'  # Path to your SQLite database
    output_video_path = 'new_zoom_effect.mp4'  # Output video file path

    # Create a video from frames stored in the database
    create_video_from_db(db_path, output_video_path)

if __name__ == '__main__':
    main()

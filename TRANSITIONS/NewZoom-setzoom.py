import sqlite3
import io
import numpy as np
from PIL import Image
import moviepy.editor as mpy
import os
import sys

def create_zoom_frames(image_path, db_path, num_frames=500, zoom_factor=3.5, focus_x=0.5, focus_y=0.5):
    """
    Create zoom effect frames focusing on a specific point and save them to the database.

    :param image_path: Path to the input image.
    :param db_path: Path to the SQLite database.
    :param num_frames: Number of frames to generate.
    :param zoom_factor: Maximum zoom factor.
    :param focus_x: X-coordinate of the focus point (relative, 0 to 1).
    :param focus_y: Y-coordinate of the focus point (relative, 0 to 1).
    """
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

        # Calculate cropping coordinates for the specified focus point
        focus_x_new = focus_x * new_width
        focus_y_new = focus_y * new_height
        left = int(focus_x_new - (width * focus_x))
        top = int(focus_y_new - (height * focus_y))
        right = left + width
        bottom = top + height

        # Ensure cropping box is within the image bounds
        left = max(0, min(left, new_width - width))
        top = max(0, min(top, new_height - height))
        right = left + width
        bottom = top + height

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

# Main execution
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <image_path> <output_video_path> [num_frames] [zoom_factor] [focus_x] [focus_y]")
        sys.exit(1)

    image_path = sys.argv[1]
    output_video_path = sys.argv[2]
    
    # Extract the base name (file name with extension)
    base_name = os.path.basename(image_path)

    # Remove the file extension
    name_without_extension = os.path.splitext(base_name)[0]

    # Create the db_path by appending '.db' to the name without extension
    db_path = name_without_extension + ".db"

    # Optional parameters with default values
    num_frames = int(sys.argv[3]) if len(sys.argv) > 3 else 500
    zoom_factor = float(sys.argv[4]) if len(sys.argv) > 4 else 3.5
    focus_x = float(sys.argv[5]) if len(sys.argv) > 5 else 0.5
    focus_y = float(sys.argv[6]) if len(sys.argv) > 6 else 0.5

    print(f"Image path: {image_path}")
    print(f"Database path: {db_path}")
    print(f"Output video path: {output_video_path}")
    print(f"Number of frames: {num_frames}")
    print(f"Zoom factor: {zoom_factor}")
    print(f"Focus X: {focus_x}")
    print(f"Focus Y: {focus_y}")

    # Create zoom frames and store them in the database
    create_zoom_frames(image_path, db_path, num_frames, zoom_factor, focus_x, focus_y)

    # Create a video from the frames stored in the database
    create_video_from_db(db_path, output_video_path, fps=30)

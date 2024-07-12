"""
To zoom into different locations, you need to modify the cropping coordinates dynamically
based on the desired focus points (x, y). When you zoom into a specific point, you need
to ensure that point remains in the same relative position in the frame after resizing
the image.
Here’s a detailed explanation and a modified version of your function to allow zooming
into a specified point (x, y):
    Calculate the scale factor: This is the same as your current implementation,
    determining the new size of the image at each frame.
    Resize the image: Resize the image using the calculated scale factor.
    Calculate cropping coordinates:
        Determine the new dimensions of the resized image.
        Calculate the new coordinates for the point (x, y) after resizing.
        Calculate the top-left corner of the cropping area to ensure the point (x, y)
        remains centered or at a specific position.
    Crop the resized image:
        Ensure the cropping area is within the bounds of the resized image.
        Adjust the cropping box if necessary to ensure it does not exceed the image dimensions.
Here’s the complete modified script:
python
"""
import sqlite3
import io
from PIL import Image
from sys import argv
import os
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
    
    conn.close()

def main():
    image_path = '/path/to/your/image.jpg'  # Replace with the path to your image
    db_path = 'frames.db'  # Path to your SQLite database
    output_video_path = 'zoom_effect.mp4'  # Output video file path

    # Create zoom effect frames and save them to the database
    create_zoom_frames(image_path, db_path)

    # Create a video from frames stored in the database
    create_video_from_db(db_path, output_video_path)


if __name__ == "__main__":
    if len(argv) != 6:
        print("Usage: python zoom_with_directions.py <image_path> <db_path> <num_frames> <zoom_factor> <focus_x> <focus_y>")
    print("Example: python zoom_with_directions.py path_to_image.jpg frames.db 500 3.5 0.5 0.5")
    # Extract the base name (file name with extension)
    image_path= argv[1]
    base_name = os.path.basename(image_path)

    # Remove the file extension
    name_without_extension = os.path.splitext(base_name)[0]

    # Create the db_path by appending '.db' to the name without extension
    db_path = name_without_extension + ".db"
    print(db_path)
     #, db_path, num_frames, zoom_factor, focus_x, focus_y = argv[1:]    
    create_zoom_frames(image_path, db_path, num_frames=500, zoom_factor=3.5, focus_x=0.5, focus_y=0.5) 
# Example usage:
# create_zoom_frames('path_to_image.jpg', 'frames.db', num_frames=500, zoom_factor=3.5, focus_x=0.5, focus_y=0.5)
"""
Explanation of Changes:

    Focus Points: The parameters focus_x and focus_y are introduced to specify the
    focus point. These should be provided as relative values (0 to 1), where (0,0)
    is the top-left and (1,1) is the bottom-right of the image.

    Resizing: The image is resized as before.

    Calculating Cropping Coordinates:
        The new coordinates of the focus point are calculated based on the resized image
        dimensions.
        The top-left corner of the cropping box is calculated to keep the focus point
        in the same relative position after resizing.

    Cropping: The crop box is adjusted to ensure it stays within the bounds of the resized image.

This way, you can zoom into any point in the image by specifying the relative coordinates
of that point. For instance, to zoom into a point at (300, 500) in an image of size
(width, height), you would set focus_x = 300 / width and focus_y = 500 / height.
"""
import cv2
import numpy as np
from moviepy.editor import VideoFileClip

# Define your own color palette as an array of RGB values
palette = np.array([[255, 0, 0],     # Red
                    [0, 255, 0],     # Green
                    [0, 0, 255],     # Blue
                    [255, 255, 0],   # Yellow
                    [255, 0, 255],   # Magenta
                    [0, 255, 255]])  # Cyan

def quantize_to_palette(image, palette):
    # Convert image to float32
    data = np.float32(image).reshape((-1, 3))

    # Calculate the distance from each pixel to each color in the palette
    distances = np.sqrt(((data[:, np.newaxis] - palette[np.newaxis, :]) ** 2).sum(axis=2))

    # Find the index of the closest color in the palette for each pixel
    closest_palette_indices = np.argmin(distances, axis=1)

    # Map each pixel to the closest color in the palette
    quantized_data = palette[closest_palette_indices]

    return quantized_data.reshape(image.shape)

def process_frame(frame):
    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Quantize the frame to the palette
    frame_quantized = quantize_to_palette(frame_rgb, palette)

    # Convert frame to uint8 if it's not already
    if frame_quantized.dtype != np.uint8:
        frame_quantized = frame_quantized.astype(np.uint8)

    # Convert the frame back to BGR
    frame_bgr = cv2.cvtColor(frame_quantized, cv2.COLOR_RGB2BGR)
    return frame_bgr

# Input video path
input_video_path = "/home/jack/Desktop/FlaskBlog/static/videos/flip_book.mp4"

# Output video path
output_video_path = "/home/jack/Desktop/FlaskBlog/static/videos/quantized_flip_book2.mp4"

# Process the video frame by frame and apply the quantization
clip = VideoFileClip(input_video_path)

# Print video details for debugging
print("Duration:", clip.duration)
print("FPS:", clip.fps)

# Process each frame in the video using process_frame function
new_clip = clip.fl_image(process_frame)

# Set the duration of the new clip to match the original clip
new_clip = new_clip.set_duration(clip.duration)

# Write the processed video without sound
new_clip.write_videofile(output_video_path, codec="libx264", audio=False)

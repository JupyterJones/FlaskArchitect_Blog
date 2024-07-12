from PIL import Image
import moviepy.editor as mpy
import os

def create_zoom_frames(image_path, output_dir, num_frames=30, zoom_factor=1.5):
    """Create zoom effect frames and save them."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    img = Image.open(image_path)
    width, height = img.size

    for i in range(num_frames):
        scale = 1 + (zoom_factor - 1) * (i / (num_frames - 1))
        new_width = int(width * scale)
        new_height = int(height * scale)
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        left = 0
        top = new_height - height
        right = left + width
        bottom = top + height
        cropped_img = resized_img.crop((left, top, right, bottom))
        frame_path = os.path.join(output_dir, f"frame_{i:03d}.png")
        cropped_img.save(frame_path)
        print(f"Saved {frame_path}")

def create_zoom_video(frames_dir, output_video_path, fps=30):
    """Create a video from saved frames."""
    frame_files = [os.path.join(frames_dir, f) for f in sorted(os.listdir(frames_dir)) if f.endswith('.png')]
    clips = [mpy.ImageClip(m).set_duration(1/fps) for m in frame_files]
    video = mpy.concatenate_videoclips(clips, method="compose")
    video.write_videofile(output_video_path, fps=fps)
    print(f"Saved video: {output_video_path}")

def main():
    image_path = '/path/to/your/image.jpg'  # Replace with the path to your image
    output_frames_dir = 'zoom_frames'
    output_video_path = 'zoom_effect.mp4'

    # Create zoom effect frames
    create_zoom_frames(image_path, output_frames_dir)

    # Create video from frames
    create_zoom_video(output_frames_dir, output_video_path)

if __name__ == '__main__':
    main()

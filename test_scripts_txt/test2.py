import os
import subprocess
import logging
import glob
import random
from moviepy.editor import VideoFileClip, CompositeVideoClip, ColorClip, ImageClip, AudioFileClip
from PIL import Image
import uuid
import shutil

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def slowem():
    vid_list = glob.glob("out*.mp4")
    cnt = 0
    for vid in vid_list:
        cnt += 1
        output_file = f"cnt_{cnt}.mp4"
        cmd = ["ffmpeg", "-i", vid, "-filter:v", "setpts=2*PTS", "-c:a", "copy", "-y", output_file]
        logging.info(f"Slowing down video: {vid} to {output_file}")
        subprocess.run(cmd, check=True)
    logging.info("All videos have been slowed down.")

def reverse_and_concatenate_video(input_video, output_video):
    try:
        if not os.path.exists(input_video):
            logging.error(f"Input video '{input_video}' not found.")
            return
        
        # Step 1: Reverse the input video
        reversed_video = input_video[:-4] + "_reversed.mp4"
        logging.info(f"Reversing the input video to {reversed_video}...")
        reverse_command = ["ffmpeg", "-hide_banner", "-i", input_video, "-vf", "reverse", "-an", "-y", reversed_video]
        subprocess.run(reverse_command, check=True)

        # Step 2: Concatenate the original and reversed videos
        concat_command = [
            "ffmpeg",
            "-i", input_video,
            "-i", reversed_video,
            "-filter_complex", "[0:v][1:v]concat=n=2:v=1:a=0[outv]",
            "-map", "[outv]", "-y", output_video
        ]
        logging.info(f"Concatenating {input_video} and {reversed_video} into {output_video}...")
        subprocess.run(concat_command, check=True)

        logging.info("Video concatenation completed successfully!")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error occurred: {e}")

def scale_and_process_video(filepath):
    filename = os.path.basename(filepath)
    logging.info(f"Processing {filename}")

    # Define output filenames
    output_1 = os.path.join(os.getcwd(), f"output_{filename}")
    output_2 = os.path.join(os.getcwd(), f"output_2_{filename}")
    final_output = os.path.join(os.getcwd(), f"final_{filename}")

    # First scaling and zooming
    command1 = [
        "ffmpeg", "-i", filepath, "-vf",
        "fps=60,scale=8000:-1,zoompan=z='pzoom+0.001':x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):d=1:s=512x768:fps=60",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-y", output_1
    ]
    subprocess.run(command1, check=True)
    logging.info(f"First processing step complete for {output_1}")

    # Second scaling and zooming with unsharp filter
    command2 = [
        "ffmpeg", "-i", output_1, "-vf",
        "fps=60,scale=8000:-1,zoompan=z='pzoom+0.001':x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):d=1:s=512x768:fps=60,unsharp=3:3:0.5:3:3:0.5",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-y", output_2
    ]
    subprocess.run(command2, check=True)
    logging.info(f"Second processing step complete for {output_2}")

    # Third scaling and zooming with unsharp filter
    command3 = [
        "ffmpeg", "-i", output_2, "-vf",
        "fps=60,scale=8000:-1,zoompan=z='pzoom+0.001':x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):d=1:s=512x768:fps=60,unsharp=3:3:0.5:3:3:0.5",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-y", final_output
    ]
    subprocess.run(command3, check=True)
    logging.info(f"Third processing step complete for {final_output}")

    # Add title image and music
    processed_video = add_title_image(final_output)
    return processed_video

def add_title_image(video_path, hex_color=None):
    if hex_color is None:
        hex_color = random.choice(["#A52A2A", "#ad1f1f", "#16765c", "#7a4111", "#9b1050", "#8e215d", "#2656ca"])
    
    # Load the video file
    video_clip = VideoFileClip(video_path)
    width, height = video_clip.size
    duration = video_clip.duration
    logging.info(f"Video size: {width}x{height}, Duration: {duration}")

    # Set the desired size of the padded video (e.g., video width + padding, video height + padding)
    padded_size = (width + 50, height + 50)

    # Calculate the position for centering the video within the larger frame
    x_position = (padded_size[0] - video_clip.size[0]) / 2
    y_position = (padded_size[1] - video_clip.size[1]) / 2

    # Remove the '#' and split the hex code into R, G, and B components
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)

    # Create an RGB tuple
    rgb_tuple = (r, g, b)

    # Create a ColorClip as the background
    background_clip = ColorClip(padded_size, color=rgb_tuple)

    # Add the video clip on top of the background
    padded_video_clip = CompositeVideoClip([background_clip, video_clip.set_position((x_position, y_position))])
    padded_video_clip = padded_video_clip.set_duration(video_clip.duration)

    # Load a random title image
    title_image_path = random.choice(glob.glob("/mnt/HDD500/FlaskArchitect/static/assets/*512x768.png"))
    title_image = ImageClip(title_image_path).set_duration(video_clip.duration).set_position((0, -5)).resize(padded_video_clip.size)

    # Create a composite video clip with the title image overlay
    composite_clip = CompositeVideoClip([padded_video_clip, title_image])
    composite_clip = composite_clip.set_duration(video_clip.duration)

    # Load a random background music
    music_path = random.choice(glob.glob("/mnt/HDD500/FlaskArchitect/static/audio/*.mp3"))
    music_clip = AudioFileClip(music_path).set_duration(video_clip.duration)
    fade_duration = 1.0
    music_clip = music_clip.audio_fadein(fade_duration).audio_fadeout(fade_duration)

    # Set the audio of the composite clip to the background music
    composite_clip = composite_clip.set_audio(music_clip)

    # Generate a unique ID for the output file
    uid = uuid.uuid4().hex
    output_path = f'/mnt/HDD500/FlaskArchitect/static/images/post/{uid}.mp4'
    composite_clip.write_videofile(output_path, codec="libx264")
    
    # Copy the final video to another location
    mp4_file = f"/mnt/HDD500/collections/vids/Ready_Post_{uid}.mp4"
    shutil.copyfile(output_path, mp4_file)
    logging.info(f"Final video saved to {mp4_file}")

    return output_path

def process_videos():
    for filepath in glob.glob(os.path.join(os.getcwd(), "cnt*.mp4")):
        logging.info(f"Processing video: {filepath}")
        processed_video = add_title_image(filepath)
        command = f"alien_add_frame_1024 {processed_video}"
        subprocess.run(command, shell=True)
        logging.info(f"Processed video saved to {processed_video}")

# Example usage
if __name__ == "__main__":
    # Process all mp4 files in the current directory
    mp4_files = glob.glob("*.mp4")
    for mp4_file in mp4_files:
        input_video = mp4_file
        output_video = "output_" + input_video
        reverse_and_concatenate_video(input_video, output_video)
    slowem()
    process_videos()
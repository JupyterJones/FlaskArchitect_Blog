import subprocess
import os
from moviepy.editor import VideoFileClip
from moviepy.editor import *


def overlay_logo(final_video):
    # Path to the logo file (adjust as per your file structure)
    logo_path = "/home/jack/Desktop/FlaskArchitect/static/assets/ghost.png"
    #get final_video duration
    video_clip = VideoFileClip(final_video)
    duration = video_clip.duration
    # Output filename with logo

    
    # Calculate start time for overlay to fade in
    fade_start = max(duration - 2, 0)  # Start overlay 2 seconds before the end

    # Overlay command with fade-in effect
    overlay_command = [
        "ffmpeg", "-i", final_video, "-i", logo_path,
        "-filter_complex", f"[0:v][1:v]overlay=main_w-overlay_w-10:main_h-overlay_h-10:enable='between(t,{fade_start},{duration})',fade=t=in:st={fade_start}:d=2",
        "-c:a", "copy", "-y", "FINAL.mp4"
    ]
    subprocess.run(overlay_command, check=True)
    print('complete')
    
if __name__ == '__main__':      
    overlay_logo('01.mp4')    

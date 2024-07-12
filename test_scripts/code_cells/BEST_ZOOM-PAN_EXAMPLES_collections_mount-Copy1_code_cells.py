import subprocess
import numpy as np
import logging
import glob
import random
import uuid
# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def zoom_pan_nonlinear1(input_path, output_path):
    try:
        # Define a non-linear path (in this case, a bezier curve)
        path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))

        # Build the updated ffmpeg command with zoom pan effect
        ffmpeg_cmd = [
            'ffmpeg',
            '-i', input_path,
            '-vf', "scale=24000:-1,zoompan=z='if(lte(zoom,1.0),1.5,max(1.001,zoom-0.0003))':x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):d=25*60:s=512x768:fps=60",
            '-c:a', 'aac',
            '-c:v', 'libx264',
            '-y',  # Overwrite output file if it already exists
            output_path
        ]

        # Run the ffmpeg command using subprocess

        subprocess.run(ffmpeg_cmd, check=True)
        
        
        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while running ffmpeg: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")        

def zoom_pan_nonlinear2(input_path, output_path):
    try:
        # Define a non-linear path (in this case, a bezier curve)
        path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))

        # Build the updated ffmpeg command with zoom pan effect
        #ffmpeg -loop 1 -framerate 60 -i yodayofeb6/00047.jpg -vf "scale=8000:-1,zoompan=z='zoom+0.001':x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):d=35*60:s=512x768:fps=60" -t 35 -c:v libx264 -pix_fmt yuv420p -y output3.
        ffmpeg_cmd = [
            'ffmpeg','-loop','1',
            '-i', input_path,
            '-vf', "scale=8000:-1,zoompan=z='zoom+0.001':x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):d=30*60:s=512x768:fps=60",
            '-t','30',
            '-c:a', 'aac',
            '-c:v', 'libx264',
            '-y',  # Overwrite output file if it already exists
            output_path
        ]

        # Run the ffmpeg command using subprocess
        subprocess.run(ffmpeg_cmd, check=True)        
        
        
        
        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while running ffmpeg: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")



# Example usage
if __name__ == "__main__":
    for i in range(0,20):
        input_image_path = random.choice(glob.glob("yodayofeb6/*.jpg"))
        output_video_path = "Videos/"+str(uuid.uuid4()) + "+.mp4"
        zoom_pan_nonlinear1(input_image_path, output_video_path)
        input_image_path = random.choice(glob.glob("yodayofeb6/*.jpg"))
        output_video_path = "Videos/"+str(uuid.uuid4()) + "++.mp4"
        zoom_pan_nonlinear2(input_image_path, output_video_path)

https://creatomate.com/blog/how-to-zoom-images-and-videos-using-ffmpeg

!frame_only /home/jack/Desktop/EXP_notebooks/leo/Final_Enda.mp4

!ffmpeg -loop 1 -framerate 60 -i yodayofeb6/00047.jpg -vf "scale=8000:-1,zoompan=z='zoom+0.001':x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):d=35*60:s=512x768:fps=60" -t 35 -c:v libx264 -pix_fmt yuv420p -y output3.

!ffmpeg -loop 1 -framerate 60 -i image.jpg -vf "scale=8000:-1,zoompan=z='zoom+0.001':x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):d=35*60:s=512x768:fps=60" -t 35 -c:v libx264 -pix_fmt yuv420p -y output3.mp4
    
!vlc  output3.mp4  

import subprocess
import numpy as np
import logging
import glob
import random
import uuid
# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def zoom_pan_nonlinear(input_path, output_path):
    try:
        # Define a non-linear path (in this case, a bezier curve)
        path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))

        # Build the updated ffmpeg command with zoom pan effect
        ffmpeg_cmd = [
            'ffmpeg',
            '-i', input_path,
            '-vf', "scale=24000:-1,zoompan=z='if(lte(zoom,1.0),1.5,max(1.001,zoom-0.0003))':x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):d=25*60:s=512x768:fps=60",
            '-c:a', 'aac',
            '-c:v', 'libx264',
            '-y',  # Overwrite output file if it already exists
            output_path
        ]

        # Run the ffmpeg command using subprocess
        subprocess.run(ffmpeg_cmd, check=True)

        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while running ffmpeg: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")



# Example usage
if __name__ == "__main__":
    input_image_path = random.choice(glob.glob("yodayofeb6/*.jpg"))
    output_video_path = str(uuid.uuid4()) + "__.mp4"


    zoom_pan_nonlinear(input_image_path, output_video_path)








!ffmpeg -loop 1 -framerate 60 -i image.jpg -vf "scale=24000:-1,zoompan=z='if(lte(zoom,1.0),1.5,max(1.001,zoom-0.0003))':x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):d=25*60:s=512x768:fps=60" -t 25 -c:v libx264 -pix_fmt yuv420p -y outputZZ.mp4
!vlc  outputZZ.mp4  

!ffmpeg -loop 1 -framerate 60 -i image.jpg -vf "scale=24000:-1,zoompan=z='if(lte(zoom,1.0),1.5,max(1.001,zoom-0.0003))':x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):d=25*60:s=512x768:fps=60" -t 25 -c:v libx264 -pix_fmt yuv420p -y outputZZ.mp4
!vlc  outputZZ.mp4  

!add_frame outputZZ.mp4  

!vlc outputZZ.mp4 





!ffmpeg -loop 1 -framerate 60 -i yodayofeb6/00047.jpg -vf "scale=8000:-1,zoompan=z='zoom+0.001':x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):d=35*60:s=512x768:fps=60" -t 35 -c:v libx264 -pix_fmt yuv420p -y output3.mp4
    
!vlc  output3.mp4  





!ffmpeg -loop 1 -framerate 60 -i image.jpg -vf "scale=8000:-1,zoompan=z='zoom+0.001':x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):d=15*60:s=512x768:fps=60" -t 15 -c:v libx264 -pix_fmt yuv420p -y output1.mp4
    
!vlc  output1.mp4  



!ffmpeg -loop 1 -framerate 60 -i image.jpg -vf "scale=8000:-1,zoompan=z='zoom+0.001':x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):d=5*60:s=512x768:fps=60" -t 5 -c:v libx264 -pix_fmt yuv420p -y output.mp4

import subprocess
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def zoom_pan_nonlinear(input_path, output_path):
    try:
        # Define a non-linear path (in this case, a bezier curve)
        path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))

        # Build the updated ffmpeg command with zoom pan effect
        ffmpeg_cmd = [
            'ffmpeg',
            '-i', input_path,
            '-vf', f'zoompan=z=\'if(eq(on,0),1.5+0.1*sin(2*PI*t),1)\':x=\'if(eq(on,0),100*t,100)\':y=\'if(eq(on,0),50*t,50)\':fps=24',
            '-c:a', 'aac',
            '-c:v', 'libx264',
            '-y',  # Overwrite output file if it already exists
            output_path
        ]

        # Run the ffmpeg command using subprocess
        subprocess.run(ffmpeg_cmd, check=True)

        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while running ffmpeg: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")



# Example usage
if __name__ == "__main__":
    input_image_path = "image.jpg"
    output_video_path = "video.mp4"

    zoom_pan_nonlinear(input_image_path, output_video_path)


!vlc output.mp4





import moviepy.editor as mp
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def zoom_pan_nonlinear(input_path, output_path):
    try:
        # Load the image
        clip = mp.ImageClip(input_path, duration=5)

        # Define a non-linear path (in this case, a bezier curve)
        path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))

        # Apply the zoom pan effect with the non-linear path
        zoom_pan_clip = (clip.fx(mp.vfx.mirror_x)
                         .fx(mp.vfx.freeze, 2)
                         .fx(mp.vfx.speedx, 0.5)
                         .resize(0.8)
                         .set_position(('center', 'center'))
                         .fl(lambda gf, t: gf(t).set_position(path(t))))

        # Set the frames per second (fps) for the final video
        fps = 24

        # Set up the final video clip
        final_clip = mp.CompositeVideoClip([zoom_pan_clip.set_duration(5)], size=(clip.size[0], clip.size[1]))

        # Write the final video to the specified output path with the specified fps
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=fps)

        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_image_path = "image.jpg"
    output_video_path = "video.mp4"

    zoom_pan_nonlinear(input_image_path, output_video_path)




import moviepy.editor as mp
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def zoom_pan_nonlinear(input_path, output_path):
    try:
        # Load the image
        clip = mp.ImageClip(input_path, duration=5)

        # Define a non-linear path (in this case, a bezier curve)
        path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))

        # Apply the zoom pan effect with the non-linear path
        zoom_pan_clip = (clip.fx(mp.vfx.mirror_x)
                         .fx(mp.vfx.freeze, 2)
                         .fx(mp.vfx.speedx, 0.5)
                         .resize(0.8)
                         .set_position(('center', 'center'))
                         .set_position(lambda t: path(t)))

        # Set the frames per second (fps) for the final video
        fps = 24

        # Set up the final video clip
        final_clip = mp.CompositeVideoClip([zoom_pan_clip.set_duration(5)], size=(clip.size[0], clip.size[1]))

        # Write the final video to the specified output path with the specified fps
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=fps)

        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_image_path = "image.jpg"
    output_video_path = "video.mp4"

    zoom_pan_nonlinear(input_image_path, output_video_path)


import moviepy.editor as mp
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def zoom_pan_nonlinear(input_path, output_path):
    try:
        # Load the image
        clip = mp.ImageClip(input_path, duration=5)

        # Define a non-linear path (in this case, a bezier curve)
        path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))

        # Apply the zoom pan effect with the non-linear path
        zoom_pan_clip = (clip.fx(mp.vfx.mirror_x)
                         .fx(mp.vfx.freeze, 2)
                         .fx(mp.vfx.speedx, 0.5)
                         .set_position(lambda t: ('center', 'center'))
                         .resize(0.8)
                         .set_position(lambda t: path(t)))

        # Set the frames per second (fps) for the final video
        fps = 24

        # Set up the final video clip
        final_clip = mp.CompositeVideoClip([zoom_pan_clip.set_duration(5)], size=(clip.size[0], clip.size[1]))

        # Write the final video to the specified output path with the specified fps
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=fps)

        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_image_path = "image.jpg"
    output_video_path = "video.mp4"

    zoom_pan_nonlinear(input_image_path, output_video_path)




import moviepy.editor as mp
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def zoom_pan_nonlinear(input_path, output_path):
    try:
        # Load the image
        clip = mp.ImageClip(input_path, duration=5)

        # Define a non-linear path (in this case, a bezier curve)
        path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))

        # Apply the zoom pan effect with the non-linear path
        zoom_pan_clip = clip.fx(mp.vfx.mirror_x)
        zoom_pan_clip = zoom_pan_clip.fx(mp.vfx.freeze, 2)
        zoom_pan_clip = zoom_pan_clip.fx(mp.vfx.speedx, 0.5)
        zoom_pan_clip = zoom_pan_clip.set_position(('center', 'center')).resize(0.8)

        # Apply the non-linear path to the position
        zoom_pan_clip = zoom_pan_clip.set_position(lambda t: ('center', 'center')).set_position(path)

        # Set the frames per second (fps) for the final video
        fps = 24

        # Set up the final video clip
        final_clip = mp.CompositeVideoClip([zoom_pan_clip.set_duration(5)], size=(clip.size[0], clip.size[1]))

        # Write the final video to the specified output path with the specified fps
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=fps)

        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_image_path = "image.jpg"
    output_video_path = "video.mp4"

    zoom_pan_nonlinear(input_image_path, output_video_path)


import moviepy.editor as mp
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def zoom_pan_nonlinear(input_path, output_path):
    try:
        # Load the image
        clip = mp.ImageClip(input_path, duration=5)

        # Define a non-linear path (in this case, a bezier curve)
        path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))

        # Apply the zoom pan effect with the non-linear path
        zoom_pan_clip = clip.fx(mp.vfx.mirror_x)
        zoom_pan_clip = zoom_pan_clip.fx(mp.vfx.freeze, 2)
        zoom_pan_clip = zoom_pan_clip.fx(mp.vfx.speedx, 0.5)
        zoom_pan_clip = zoom_pan_clip.set_position(('center', 'center')).resize(0.8)

        # Apply the non-linear path to the position
        zoom_pan_clip = zoom_pan_clip.fl(lambda gf, t: gf(t).set_position(('center', 'center')).set_position(('center', 'center')).set_position(('center', 'center')).set_position(path(t)))

        # Set the frames per second (fps) for the final video
        fps = 24

        # Set up the final video clip
        final_clip = mp.CompositeVideoClip([zoom_pan_clip.set_duration(5)], size=(clip.size[0], clip.size[1]))

        # Write the final video to the specified output path with the specified fps
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=fps)

        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_image_path = "image.jpg"
    output_video_path = "video.mp4"

    zoom_pan_nonlinear(input_image_path, output_video_path)




import moviepy.editor as mp
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def zoom_pan_nonlinear(input_path, output_path):
    try:
        # Load the image
        clip = mp.ImageClip(input_path, duration=5)

        # Define a non-linear path (in this case, a bezier curve)
        path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))

        # Apply the zoom pan effect with the non-linear path
        zoom_pan_clip = clip.fx(mp.vfx.mirror_x)
        zoom_pan_clip = zoom_pan_clip.fx(mp.vfx.freeze, 2)
        zoom_pan_clip = zoom_pan_clip.fx(mp.vfx.speedx, 0.5)
        zoom_pan_clip = zoom_pan_clip.set_position(('center', 'center')).resize(0.8)

        # Set the frames per second (fps) for the final video
        fps = 24

        # Set up the final video clip
        final_clip = mp.CompositeVideoClip([zoom_pan_clip.set_duration(5)], size=(clip.size[0], clip.size[1]))

        # Write the final video to the specified output path with the specified fps
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=fps)

        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_image_path = "image.jpg"
    output_video_path = "video.mp4"

    zoom_pan_nonlinear(input_image_path, output_video_path)




import moviepy.editor as mp
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def zoom_pan_nonlinear(input_path, output_path):
    try:
        # Load the image
        clip = mp.ImageClip(input_path, duration=5)

        # Define a non-linear path (in this case, a bezier curve)
        path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))

        # Apply the zoom pan effect with the non-linear path
        zoom_pan_clip = (clip.fx(mp.vfx.zoom_in, 1.5)
                         .fx(mp.vfx.zoom_out, 1.5)
                         .fl(lambda gf, t: gf(t)[:, int(path(t)[1]):int(path(t)[1]) + clip.size[1]]))

        # Set the frames per second (fps) for the final video
        fps = 24

        # Set up the final video clip
        final_clip = mp.CompositeVideoClip([zoom_pan_clip.set_duration(5)], size=(clip.size[0], clip.size[1]))

        # Write the final video to the specified output path with the specified fps
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=fps)

        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_image_path = "image.jpg"
    output_video_path = "video.mp4"

    zoom_pan_nonlinear(input_image_path, output_video_path)


import moviepy.editor as mp
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def zoom_pan_nonlinear(input_path, output_path):
    try:
        # Load the image
        clip = mp.ImageClip(input_path, duration=5)

        # Define a non-linear path (in this case, a bezier curve)
        path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))

        # Apply the zoom pan effect with the non-linear path
        zoom_pan_clip = clip.resize(1.5).zoom(1.5).fl(lambda gf, t: gf(t)[:, int(path(t)[1]):int(path(t)[1])+clip.size[1]])

        # Set the frames per second (fps) for the final video
        fps = 24

        # Set up the final video clip
        final_clip = mp.CompositeVideoClip([zoom_pan_clip.set_duration(5)], size=(clip.size[0], clip.size[1]))

        # Write the final video to the specified output path with the specified fps
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=fps)

        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_image_path = "image.jpg"
    output_video_path = "video.mp4"

    zoom_pan_nonlinear(input_image_path, output_video_path)




import moviepy.editor as mp
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def zoom_pan_nonlinear(input_path, output_path):
    try:
        # Load the image
        clip = mp.ImageClip(input_path, duration=5)

        # Define a non-linear path (in this case, a bezier curve)
        path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))

        # Apply the zoom pan effect with the non-linear path
        zoom_pan_clip = clip.resize(1.5).fl(lambda gf, t: gf(t)[:, int(path(t)[1]):int(path(t)[1])+clip.size[1]])

        # Set the frames per second (fps) for the final video
        fps = 24

        # Set up the final video clip
        final_clip = mp.CompositeVideoClip([zoom_pan_clip], size=(clip.size[0], clip.size[1]))

        # Write the final video to the specified output path with the specified fps
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=fps)

        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":  
    
    input_image_path = "yodayofeb6/9b9c9202-a5d1-45ba-b262-2f5d93731a61_width=512&height=768.jpg"
    output_video_path = "video.mp4"
    
    zoom_pan_nonlinear(input_image_path, output_video_path)


!vlc video.mp4

import moviepy.editor as mp
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def zoom_pan_nonlinear(input_path, output_path):
    try:
        # Load the image
        clip = mp.ImageClip(input_path, duration=5)

        # Define a non-linear path (in this case, a bezier curve)
        path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))

        # Apply the zoom pan effect with the non-linear path
        zoom_pan_clip = clip.resize(1.5).fl(lambda gf, t: gf(t)[:, int(path(t)[1]):int(path(t)[1])+clip.size[1]])

        # Set up the final video clip
        final_clip = mp.CompositeVideoClip([zoom_pan_clip], size=(clip.size[0], clip.size[1]))

        # Write the final video to the specified output path
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_image_path = "yodayofeb6/9b9c9202-a5d1-45ba-b262-2f5d93731a61_width=512&height=768.jpg"
    output_video_path = "video.mp4"

    zoom_pan_nonlinear(input_image_path, output_video_path)


import moviepy.editor as mp
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def zoom_pan_nonlinear(input_path, output_path):
    try:
        # Load the image
        clip = mp.ImageClip(input_path, duration=5)

        # Define a non-linear path (in this case, a bezier curve)
        path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))

        # Apply the zoom pan effect with the non-linear path
        zoom_pan_clip = clip.resize(1.5).fx(mp.vfx.pan, path)

        # Set up the final video clip
        final_clip = mp.CompositeVideoClip([zoom_pan_clip], size=(clip.size[0], clip.size[1]))

        # Write the final video to the specified output path
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_image_path = "yodayofeb6/9b9c9202-a5d1-45ba-b262-2f5d93731a61_width=512&height=768.jpg"
    output_video_path = "video.mp4"
    zoom_pan_nonlinear(input_image_path, output_video_path)


import moviepy.editor as mp
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def zoom_pan_nonlinear(input_path, output_path):
    try:
        # Load the image
        clip = mp.ImageClip(input_path, duration=5)

        # Define a non-linear path (in this case, a bezier curve)
        path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))

        # Apply the zoom pan effect with the non-linear path
        zoom_pan_clip = clip.fx(mp.fx.resize, 1.5).fx(mp.pan, path)

        # Set up the final video clip
        final_clip = mp.CompositeVideoClip([zoom_pan_clip], size=(clip.size[0], clip.size[1]))

        # Write the final video to the specified output path
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_image_path = "/home/jack/Desktop/EXP_notebooks/yodayofeb6/9b9c9202-a5d1-45ba-b262-2f5d93731a61_width=512&height=768.jpg"
    output_video_path = "video.mp4"
    zoom_pan_nonlinear(input_image_path, output_video_path)


import moviepy.editor as mp
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def zoom_pan_nonlinear(input_path, output_path):
    try:
        # Load the image
        clip = mp.ImageClip(input_path, duration=5)

        # Define a non-linear path (in this case, a bezier curve)
        path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))

        # Apply the zoom pan effect with the non-linear path
        zoom_pan_clip = clip.fx(mp.resize, 1.5).fx(mp.pan, path)

        # Set up the final video clip
        final_clip = mp.CompositeVideoClip([zoom_pan_clip], size=(clip.size[0], clip.size[1]))

        # Write the final video to the specified output path
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_image_path = "/home/jack/Desktop/EXP_notebooks/yodayofeb6/9b9c9202-a5d1-45ba-b262-2f5d93731a61_width=512&height=768.jpg"
    output_video_path = "video.mp4"
    zoom_pan_nonlinear(input_image_path, output_video_path)


import moviepy.editor as mp
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def zoom_pan_nonlinear(input_path, output_path):
    try:
        # Load the image
        clip = mp.ImageClip(input_path, duration=5)

        # Define a non-linear path (in this case, a bezier curve)
        path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))

        # Apply the zoom pan effect with the non-linear path
        zoom_pan_clip = clip.fx(mp.zoom.in_scale, 1.5).fx(mp.pan, path)

        # Set up the final video clip
        final_clip = mp.CompositeVideoClip([zoom_pan_clip], size=(clip.size[0], clip.size[1]))

        # Write the final video to the specified output path
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_image_path = "/home/jack/Desktop/EXP_notebooks/yodayofeb6/9b9c9202-a5d1-45ba-b262-2f5d93731a61_width=512&height=768.jpg"
    output_video_path = "video.mp4"

    zoom_pan_nonlinear(input_image_path, output_video_path)


import glob
import random
from PIL import Image
DIR= random.choice(glob.glob("/home/jack/Desktop/collections_mount/images/*"))+"/"
print(DIR)
imaGE = random.choice(glob.glob(DIR+"*.jpg"))
print (imaGE)
im =Image.open(imaGE)
im

import glob
import random
from PIL import Image
DIR= random.choice(glob.glob("/home/jack/Desktop/collections_mount/images/*"))+"/"
print(DIR)
imaGE = random.choice(glob.glob(DIR+"*.jpg"))
print (imaGE)
im =Image.open(imaGE)
im

import subprocess
import numpy as np
import logging
import uuid
import os
# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def zoom_pan_nonlinear(input_path, output_dir):
    try:
        # Define a non-linear path (in this case, a bezier curve)
        path = lambda t: (100 * np.sin(2 * np.pi * t), 50 * np.cos(2 * np.pi * t))

        # Generate a unique filename for the output video
        output_filename = str(uuid.uuid4()) + ".mp4"
        output_path = os.path.join(output_dir, output_filename)

        # Build the updated ffmpeg command with zoom pan effect
        ffmpeg_cmd = [
            'ffmpeg',
            '-i', input_path,
            '-vf', f'zoompan=z=\'if(eq(on,0),1.5+0.1*sin(2*PI*t),1)\':x=\'if(eq(on,0),100*t,100)\':y=\'if(eq(on,0),50*t,50)\':fps=24',
            '-c:a', 'aac',
            '-c:v', 'libx264',
            '-y',  # Overwrite output file if it already exists
            output_path
        ]

        # Run the ffmpeg command using subprocess
        subprocess.run(ffmpeg_cmd, check=True)

        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while running ffmpeg: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_image_path = "image.jpg"
    output_directory = "Videos"

    zoom_pan_nonlinear(input_image_path, output_directory)


!mkdir Videos

import subprocess
import numpy as np
import logging
import uuid

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def zoom_pan_nonlinear(input_path, output_dir):
    try:
        # Generate a unique filename for the output video
        output_filename = str(uuid.uuid4()) + ".mp4"
        output_path = os.path.join(output_dir, output_filename)

        # Build the updated ffmpeg command with zoom pan effect
        ffmpeg_cmd = [
            'ffmpeg',
            '-i', input_path,
            '-vf', f'zoompan=z=\'if(eq(on,0),1.5+0.1*sin(2*PI*t),1)\':x=\'if(eq(on,0),100*t,100)\':y=\'if(eq(on,0),50*t,50)\':fps=24',
            '-c:a', 'aac',
            '-c:v', 'libx264',
            '-y',  # Overwrite output file if it already exists
            output_path
        ]

        # Run the ffmpeg command using subprocess
        subprocess.run(ffmpeg_cmd, check=True)

        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while running ffmpeg: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_image_path = "image.jpg"
    output_directory = "Videos"

    zoom_pan_nonlinear(input_image_path, output_directory)


import subprocess
import numpy as np
import logging
import os
import uuid

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def zoom_pan_nonlinear(input_path, output_dir):
    try:
        # Generate a unique filename for the output video
        output_filename = str(uuid.uuid4()) + ".mp4"
        output_path = os.path.join(output_dir, output_filename)

        # Build the updated ffmpeg command with zoom pan effect
        ffmpeg_cmd = [
            'ffmpeg','-hide_banner',
            '-i', input_path,
            '-vf', f'zoompan=d=5:fps=24:z=\'if(eq(on,0),1.5+0.1*sin(2*PI*t),1)\':x=\'if(eq(on,0),100*t,100)\':y=\'if(eq(on,0),50*t,50)\':s=WxH',
            '-c:a', 'aac',
            '-c:v', 'libx264',
            '-y',  # Overwrite output file if it already exists
            output_path
        ]

        # Run the ffmpeg command using subprocess
        subprocess.run(ffmpeg_cmd, check=True)

        logging.info(f"Zoom pan effect with a non-linear path applied. Output saved to {output_path}")

    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while running ffmpeg: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_image_path = "image.jpg"
    output_directory = "Videos"

    zoom_pan_nonlinear(input_image_path, output_directory)


!ffmpeg -hide_banner -i image.jpg -vf \ "zoompan=d=5:fps=24:z='if(eq(on,0),1.5+0.1*sin(2*PI*t),1)':x='if(eq(on,0),100*t,100)':y='if(eq(on,0),50*t,50)':s=512x768" \
-c:a aac -c:v libx264 -y outputss.mp4


!ffmpeg -hide_banner -i image.jpg -vf \ "zoompan=d=5:fps=24:z='if(eq(on,0),1.5+0.1*sin(2*PI*t),1)':x='if(eq(on,0),100*t,100)':y='if(eq(on,0),50*t,50)':s=512x768" \
-c:a aac -c:v libx264 -y outputss.mp4


!ffmpeg -f lavfi -i haldclutsrc=8 -vf "hue=H=2*PI*t:s=sin(2*PI*t)+1, curves=cross_process" -t 10 -c:v ffv1 clut.nut

!ffmpeg -f lavfi -i mandelbrot -i clut.nut -filter_complex '[0][1] haldclut' -t 20 mandelclut.mkv

!ffmpeg -f lavfi -i haldclutsrc=8 -vf "hue=H=2*PI*t:s=sin(2*PI*t)+.001, curves=cross_process" -t 120 -c:v ffv1 -y clut1.nut

!ffmpeg -f lavfi -i mandelbrot -i clut1.nut -filter_complex '[0][1] haldclut' -t 160 -y mandelclut40.mkv

!vlc mandelclut40.mkv

ffmpeg -i input.mp4 -ignore_loop 0 -i input.gif -filter_complex overlay=shortest=1 out.mkv



import cv2
import os
import random
import time
import datetime
from PIL import Image

NAMES = []

def generate_filename():
    # Get current time in nanoseconds since epoch
    current_time_ns = datetime.datetime.now().timestamp() * 1e9

    # Format the time string
    time_str = f"{current_time_ns:.0f}"

    # Create a filename with the timestamp
    filename = f"junk/image_{time_str}.png"
    return filename

def vid2img(End, outputpath):
    # Create directory if it doesn't exist
    if not os.path.exists('junk'):
        os.makedirs('junk')
    if not os.path.exists(outputpath):
        os.makedirs(outputpath)

    count = 0
    filename = "/mnt/HDD500/collections/complete_mp4_video/24sept-output-slow-3per-sec-jpgs.mp4"
    vidcap = cv2.VideoCapture(filename)

    # Get total number of frames
    totalFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    randomFrameNumber = random.randint(0, totalFrames)

    # Set frame position
    vidcap.set(cv2.CAP_PROP_POS_FRAMES, randomFrameNumber)
    success, image = vidcap.read()

    # Generate filename using generate_filename() function
    filename = generate_filename()

    if success:
        print("count:", count, end="|")
        count += 1 
        cv2.imwrite(filename, image)

    # Open image with PIL and resize
    im = Image.open(filename)
    im = im.resize((720, 480))
    im.save(filename)

    # Re-open resized image with PIL
    nim = Image.open(filename)
    NAMES.append(filename)
    
    return nim

if __name__ == "__main__":
    End = 6
    outputpath = 'EXP'
    for i in range(End):
        print(i)
        vid2img(End, outputpath)
    
    for name in NAMES:
        print(name)

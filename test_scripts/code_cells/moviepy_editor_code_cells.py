from processing_py import *

app = App(600,400) # create window: width, height
app.background(255,0,0) # set background:  red, green, blue
app.redraw() # refresh the window

#app.exit() # close the window


import av
import numpy as np
from PIL import Image
import glob
import random
from genfilename import genfilename
all_im_objects = []
image_files = []
# create a list of filenames drom a directory
directory = "/home/jack/Downloads/00de3/PicFinder.AI-Unleash_Your_Creativity_with_AI-Generated_Images_files/"

images_per_frame = 24
fps = 24
duration = 60
#sort the *.jpg files
for i in range(0,duration*fps):
    random_img = random.choice(glob.glob(directory+"*.jpg"))
    image_files.append(random_img)
    #video duration and frame rate

# get enough files for the rquired duration and fps [:duration*fps]
imgs = image_files[:duration*fps]
"""for sequ_num in range(0,len(imgs)):
    # open each image and append all_im_objects with the image_object
    im = Image.open(imgs[sequ_num])
    all_im_objects.append(im)
"""
for sequ_num in range(0,len(imgs)):
    # open each image and append all_im_objects with the image_object repeated 24 times
    im = Image.open(imgs[sequ_num])
    im = im.resize((512,512), Image.BICUBIC)
    for _ in range(24):
        all_im_objects.append(im)
total_frames = duration * fps
container = av.open(genfilename(".mkv"), mode="w")
stream = container.add_stream("mpeg4", rate=fps)
stream.width = 512
stream.height = 512
stream.pix_fmt = "yuv420p"
for frame_i in range(total_frames):
    img = all_im_objects[frame_i]
    img_np = np.array(img)
    frame = av.VideoFrame.from_ndarray(img_np, format="rgb24")
    for packet in stream.encode(frame):
        container.mux(packet)
# Flush stream
for packet in stream.encode():
    container.mux(packet)
# Close the file
container.close()

import os
import subprocess
import glob
from PIL import Image
import cv2
import av
import av.datasets


# We want an H.264 stream in the Annex B byte-stream format.
# We haven't exposed bitstream filters yet, so we're gonna use the `ffmpeg` CLI.
h264_path = "new_night-sky.h264"
if not os.path.exists(h264_path):
    subprocess.check_call(
        [
            "ffmpeg",
            "-i",
            av.datasets.curated("pexels/time-lapse-video-of-night-sky-857195.mp4"),
            "-vcodec",
            "copy",
            "-an",
            "-bsf:v",
            "h264_mp4toannexb",
            h264_path,
        ]
    )


fh = open(h264_path, "rb")

codec = av.CodecContext.create("h264", "r")

while True:

    chunk = fh.read(1 << 16)

    packets = codec.parse(chunk)
    print("Parsed {} packets from {} bytes:".format(len(packets), len(chunk)))

    for packet in packets:

        print("   ", packet)

        frames = codec.decode(packet)
        for frame in frames:
            print("       ", frame)

    # We wait until the end to bail so that the last empty `buf` flushes
    # the parser.
    if not chunk:
        break


all_im_objects = []
duration = 4
fps = 24
all_img = sorted(glob.glob("/home/jack/Downloads/00de3/PicFinder.AI-Unleash_Your_Creativity_with_AI-Generated_Images_files/*.jpg"))
imgs = all_img[:duration*fps]
print(len(imgs))
for sequ_num in range(0,len(imgs)):
    im = Image.open(imgs[sequ_num])
    all_im_objects.append(im)
print(len(all_im_objects))

#https://pyav.org/docs/stable/

#https://pyav.org/docs/stable/
import av
import numpy as np
duration = 4
fps = 24
total_frames = duration * fps
container = av.open("test.mp4", mode="w")
stream = container.add_stream("mpeg4", rate=fps)
stream.width = 480
stream.height = 320
stream.pix_fmt = "yuv420p"

for frame_i in range(total_frames):

    img = np.empty((480, 320, 3))
    img[:, :, 0] = 0.5 + 0.5 * np.sin(2 * np.pi * (0 / 3 + frame_i / total_frames))
    img[:, :, 1] = 0.5 + 0.5 * np.sin(2 * np.pi * (1 / 3 + frame_i / total_frames))
    img[:, :, 2] = 0.5 + 0.5 * np.sin(2 * np.pi * (2 / 3 + frame_i / total_frames))

    img = np.round(255 * img).astype(np.uint8)
    img = np.clip(img, 0, 255)

    frame = av.VideoFrame.from_ndarray(img, format="rgb24")
    for packet in stream.encode(frame):
        container.mux(packet)

# Flush stream
for packet in stream.encode():
    container.mux(packet)

# Close the file
container.close()


from PIL import Image
import numpy as np

import av
import av.datasets
#vid = "pexels/time-lapse-video-of-sunset-by-the-sea-854400.mp4"
vid ="/home/jack/Desktop/HDD500/complete-videos/ArchivedImages.mp4"
container = av.open(
    av.datasets.curated(vid)
)
container.streams.video[0].thread_type = "AUTO"  # Go faster!

columns = []
for frame in container.decode(video=0):

    print(frame)
    array = frame.to_ndarray(format="rgb24")

    # Collapse down to a column.
    column = array.mean(axis=1)

    # Convert to bytes, as the `mean` turned our array into floats.
    column = column.clip(0, 255).astype("uint8")

    # Get us in the right shape for the `hstack` below.
    column = column.reshape(-1, 1, 3)

    columns.append(column)

# Close the file, free memory
container.close()

full_array = np.hstack(columns)
full_img = Image.fromarray(full_array, "RGB")
full_img = full_img.resize((800, 200))
full_img.save("barcode2.jpg", quality=85)


import av
import av.datasets


content = av.datasets.curated("pexels/time-lapse-video-of-night-sky-857195.mp4")
with av.open(content) as container:
    # Signal that we only want to look at keyframes.
    stream = container.streams.video[0]
    stream.codec_context.skip_frame = "NONKEY"

    for frame in container.decode(stream):

        print(frame)

        # We use `frame.pts` as `frame.index` won't make must sense with the `skip_frame`.
        frame.to_image().save(
            "night-sky.{:04d}.jpg".format(frame.pts),
            quality=80,
        )

import av
import av.datasets
input_ = av.open(av.datasets.curated("pexels/time-lapse-video-of-night-sky-857195.mp4"))
#input_ = av.open("/home/jack/Desktop/dockercommands/c0M0J040g0B070q0.mp4","r")
output = av.open("remuxed01.mkv", "w")

# Make an output stream using the input as a template. This copies the stream
# setup from one to the other.
in_stream = input_.streams.video[0]
out_stream = output.add_stream(template=in_stream)

for packet in input_.demux(in_stream):

    print(packet)

    # We need to skip the "flushing" packets that `demux` generates.
    if packet.dts is None:
        continue

    # We need to assign the packet to the new stream.
    packet.stream = out_stream

    output.mux(packet)

input_.close()
output.close()

import os
import subprocess
import av
import av.datasets

# We want an H.264 stream in the Annex B byte-stream format.
# We haven't exposed bitstream filters yet, so we're gonna use the `ffmpeg` CLI.
h264_path = "night-sky.h264"
if not os.path.exists(h264_path):
    subprocess.check_call(
        [
            "ffmpeg",
            "-i",
            av.datasets.curated("pexels/time-lapse-video-of-night-sky-857195.mp4"),
            "-vcodec",
            "copy",
            "-an",
            "-bsf:v",
            "h264_mp4toannexb",
            h264_path,
        ]
    )


fh = open(h264_path, "rb")

codec = av.CodecContext.create("h264", "r")

while True:

    chunk = fh.read(1 << 16)

    packets = codec.parse(chunk)
    print("Parsed {} packets from {} bytes:".format(len(packets), len(chunk)))

    for packet in packets:

        print("   ", packet)

        frames = codec.decode(packet)
        for frame in frames:
            print("       ", frame)

    # We wait until the end to bail so that the last empty `buf` flushes
    # the parser.
    if not chunk:
        break


#To edit videos using Python, you can use libraries such as OpenCV or moviepy. 

#https://pyav.org/docs/stable/
#use functions such as `cv2.VideoCapture` to open a video file and `cv2.VideoWriter` to write the edited video to a file. 

from moviepy.editor import VideoFileClip

def crop_video(input_file, output_file):
    clip = VideoFileClip(input_file)
    cropped_clip = clip.crop(x1=0, y1=0, x2=clip.w/2, y2=clip.h/2)
    cropped_clip.write_videofile(output_file)

input_file = "/home/jack/Desktop/HDD500/complete-videos/15out.mp4"
output_file = "output.mp4"
crop_video(input_file, output_file)






av.open(format='avfoundation', file='0') 
 av.open(file, mode='r', **kwargs)

    Main entrypoint to opening files/streams.

    Parameters

            file (str) – The file to open, which can be either a string or a file-like object.

            mode (str) – "r" for reading and "w" for writing.

            format (str) – Specific format to use. Defaults to autodect.

            options (dict) – Options to pass to the container and all streams.

            container_options (dict) – Options to pass to the container.

            stream_options (list) – Options to pass to each stream.

            metadata_encoding (str) – Encoding to use when reading or writing file metadata. Defaults to "utf-8".

            metadata_errors (str) – Specifies how to handle encoding errors; behaves like str.encode parameter. Defaults to "strict".

            buffer_size (int) – Size of buffer for Python input/output operations in bytes. Honored only when file is a file-like object. Defaults to 32768 (32k).

            timeout (float or tuple) – How many seconds to wait for data before giving up, as a float, or a (open timeout, read timeout) tuple.

    For devices (via libavdevice), pass the name of the device to format, e.g.:

# Open webcam on OS X.

av.open(format='avfoundation', file='0') 


%%writefile genfilename.py
import string
import random
def genfilename(ext = ".png"):
    ran = []
    chars = string.printable
    for car in chars:
        ran.append(car)
    for x in range(0,20):
        nm = random.choice(ran[10:52])+str(x)
        nm = nm + random.choice(ran[10:52])+str(x)
        nm = nm + random.choice(ran[10:52])+str(x)
        nm = nm + random.choice(ran[:52])+str(x)
        nm = nm + random.choice(ran[:52])+str(x)
        nm = nm + random.choice(ran[:52])+str(x)
        nm = nm + random.choice(ran[:52])+str(x)
        nm = nm + random.choice(ran[10:52])+str(x)+ext
        return nm
    
print (genfilename(".txt"))  

from diffusers import StableDiffusionPipeline
import torch
model_id = "prompthero/openjourney"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
prompt = "retro serie of different cars with different colors and shapes, mdjrny-v4 style"
image = pipe(prompt).images[0]
image.save("./retro_cars.png")

https://huggingface.co/prompthero/openjourney?text=mdjrny-v4+style+A+highly+detailed+beautiful+gypsy+princess+with+an+art+nouveau+background+style+of+Alphonse+Mucha


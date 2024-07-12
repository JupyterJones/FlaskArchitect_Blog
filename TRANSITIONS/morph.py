import cv2
import numpy as np
from moviepy.editor import ImageSequenceClip
from sys import argv
import os

image_folder = argv[1]
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

alpha = 0.5  # Morphing parameter
morphed_frames = []

for i in range(len(images) - 1):
    img1 = cv2.imread(os.path.join(image_folder, images[i]))
    img2 = cv2.imread(os.path.join(image_folder, images[i + 1]))

    for j in np.arange(0, 2, 0.1):  # Generate 10 intermediate frames
        morphed_frame = cv2.addWeighted(img1, j, img2, 1 - j, 0)
        morphed_frames.append(morphed_frame)

clip = ImageSequenceClip(morphed_frames, fps=30)
clip.write_videofile("morphed_output.mp4")
import cv2
import numpy as np 
# Read images
dst = cv2.imread("/home/jack/Desktop/FlaskBlog/TRANSITIONS/images/images/00002.jpg")
src = cv2.imread("/home/jack/Desktop/FlaskBlog/TRANSITIONS/images/images/00002.jpg")
src_mask = np.zeros(src.shape, src.dtype)
#poly = np.array([ [1,100], [1,50], [151,63], [254,37], [298,90], [272,134], [43,122] ], np.int32)
#array the center 300x300


cv2.fillPoly(src_mask, [poly], (255, 255, 255))
# This is where the CENTER where thr 'poly' will be placed
center = (250,125)
# Clone seamlessly.
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)
# Write result
cv2.imwrite("/home/jack/Desktop/FlaskBlog/TRANSITIONS/images/01-cloning-example5.jpg", output)
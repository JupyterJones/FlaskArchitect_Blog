import cv2
import numpy as np

# Load image01.jpg and image02.jpg
image01_path = 'images/00001.jpg'
image02_path = 'images/00002.jpg'

image01 = cv2.imread(image01_path)
image02 = cv2.imread(image02_path)
print(f'Image01 shape: {image01.shape}')
print(f'Image02 shape: {image02.shape}')

# Ensure both images are of the same size (resize if necessary)
if image01.shape != image02.shape:
    image02 = cv2.resize(image02, (image01.shape[1], image01.shape[0]))

# Create a mask for image02 (all non-zero values)
mask = 255 * np.ones_like(image02, dtype=np.uint8)

# Define the ROI for cloning (make sure it fits within image01 dimensions)
rows, cols, _ = image02.shape
# Define ROIs as an array (x, y, width, height) for each ROI
roi = np.array([[100, 178, 300, 250], [400, 400, 400, 100]])

# Validate ROI dimensions
if roi[0] < 0 or roi[1] < 0 or roi[0] + roi[2] > image01.shape[1] or roi[1] + roi[3] > image01.shape[0]:
    raise ValueError('ROI exceeds dimensions of image01. Adjust ROI coordinates and size.')

# Perform seamless cloning
output = cv2.seamlessClone(image02, image01, mask, (roi[0] + cols // 2, roi[1] + rows // 2), cv2.NORMAL_CLONE)

# Display and save the result
cv2.imshow('Seamless Cloning Result', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the result
output_path = 'seamless_cloning_result.jpg'
cv2.imwrite(output_path, output)
print(f'Seamless cloning result saved at {output_path}')

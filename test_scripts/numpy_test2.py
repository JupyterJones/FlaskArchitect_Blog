import numpy as np
import cv2
from PIL import Image
from io import BytesIO


# Create a 3D array
c = np.array([[(1.5, 2, 3), (4, 5, 6)], [(3, 2, 1), (4, 5, 6)]])
print('\n3D array')
print('c = np.array([[(1.5, 2, 3), (4, 5, 6)], [(3, 2, 1), (4, 5, 6)]])')
print(c)

# Create an array of zeros
d = np.zeros((3, 4))
print('\nArray of zeros')
print('d = np.zeros((3, 4))')
print(d)

# Create an array of ones
e = np.ones((2, 3, 4), dtype=np.int16)
print('\nArray of ones')
print('e = np.ones((2, 3, 4), dtype=np.int16)')
print(e)

# Create an array of evenly spaced values
f = np.arange(10, 25, 5)
print('\nArray of evenly spaced values')
print('f = np.arange(10, 25, 5)')
print(f)

# Create an array of evenly spaced values (number of samples)
g = np.linspace(0, 2, 9)
print('\nArray of evenly spaced values (number of samples)')
print('g = np.linspace(0, 2, 9)')
print(g)

# Create a constant array
h = np.full((2, 2), 7)
print('\nConstant array')
print('h = np.full((2, 2), 7)')
print(h)

# Create a 2x2 identity matrix
i = np.eye(2)
print('\n2x2 Identity matrix')
print('i = np.eye(2)')
print(i)

# Create an array with random values
j = np.random.random((2, 2))
print('\nArray with random values')
print('j = np.random.random((2, 2))')
print(j)

# Create an empty array
k = np.empty((3, 2))
print('\nEmpty array')
print('k = np.empty((3, 2))')
print(k)

# Save and load arrays
a = np.array([1, 2, 3])
b = np.array([10, 15, 20])

np.save('my_array', a)
print('\nArray saved to disk: my_array.npy')

loaded_array = np.load('my_array.npy')
print('\nLoaded array from disk')
print(loaded_array)

np.savez('array.npz', a, b)
print('\nArrays saved to compressed format: array.npz')

loaded_npz = np.load('array.npz')
print('\nLoaded arrays from compressed format')
print(loaded_npz['arr_0'])
print(loaded_npz['arr_1'])

# Save and load text files
np.savetxt('myarray.txt', a, delimiter=' ')
print('\nArray saved to text file: myarray.txt')

loaded_txt = np.loadtxt('myarray.txt')
print('\nLoaded array from text file')
print(loaded_txt)

# Inspecting arrays
print('\nInspecting arrays')
print('Shape of a:', a.shape)
print('Length of a:', len(a))
print('Number of dimensions of b:', b.ndim)
print('Number of elements in e:', e.size)
print('Data type of b:', b.dtype)
print('Name of data type of b:', b.dtype.name)
print('Convert b to int:', b.astype(int))

# Data types
print('\nData types')
print('np.int64:', np.int64)
print('np.float32:', np.float32)
print('np.complex:', np.complex128)
print('np.bool:', np.bool_)
print('np.object:', np.object_)
print('np.string_:', np.string_)
print('np.unicode_:', np.unicode_)

# Array mathematics
print('\nArray mathematics')

# Define compatible arrays for operations
a = np.array([[1.5, 2, 3], [4, 5, 6]])
b = np.array([[1, 2, 3], [4, 5, 6]])

print('a - b')
print(a - b)
print('np.subtract(a, b)')
print(np.subtract(a, b))

print('b + a')
print(b + a)
print('np.add(b, a)')
print(np.add(b, a))

print('a / b')
print(a / b)
print('np.divide(a, b)')
print(np.divide(a, b))

print('a * b')
print(a * b)
print('np.multiply(a, b)')
print(np.multiply(a, b))

print('np.exp(b)')
print(np.exp(b))

print('np.sqrt(b)')
print(np.sqrt(b))

print('np.sin(a)')
print(np.sin(a))

print('np.cos(b)')
print(np.cos(b))

print('np.log(a)')
print(np.log(a))

# For dot product, ensure compatible shapes
e = np.array([[1, 2], [3, 4]])
f = np.array([[5, 6], [7, 8]])

print('e.dot(f)')
print(e.dot(f))

# Comparison
print('\nComparison')
print('a == b')
print(a == b)
print('a < 2')
print(a < 2)
print('np.array_equal(a, b)')
print(np.array_equal(a, b))

# Copying arrays
print('\nCopying arrays')
h = a.view()
print('View of array a')
print(h)

h_copy = np.copy(a)
print('Copy of array a')
print(h_copy)

h_deep_copy = a.copy()
print('Deep copy of array a')
print(h_deep_copy)

# Sorting arrays
print('\nSorting arrays')
a = np.array([[3, 2, 1], [6, 5, 4]])
print('Original array a')
print(a)

a.sort()
print('Sorted array a')
print(a)

c.sort(axis=0)
print('Sorted array c along axis 0')
print(c)

# Subsetting, slicing, indexing
print('\nSubsetting, slicing, indexing')
a = np.array([1, 2, 3])
print('a[2]')
print(a[2])

b = np.array([[1, 2, 3], [4, 5, 6]])
print('b[1,2]')
print(b[1, 2])

print('a[0:2]')
print(a[0:2])

print('b[0:2,1]')
print(b[0:2, 1])

print('b[:1]')
print(b[:1])

print('c[1,...]')
print(c[1, ...])

print('a[::-1]')
print(a[::-1])

# Boolean indexing
print('\nBoolean indexing')
print('a[a < 2]')
print(a[a < 2])

# Fancy indexing
print('\nFancy indexing')
print('b[[1,0,1,0],[0,1,2,0]]')
print(b[[1, 0, 1, 0], [0, 1, 2, 0]])

print('b[[1,0,1,0]][:,[0,1,2,0]]')
print(b[[1, 0, 1, 0]][:, [0, 1, 2, 0]])

# Combining arrays
print('\nCombining arrays')
a = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[7, 8, 9], [10, 11, 12]])

print('Concatenate arrays a and d along axis 0')
print(np.concatenate((a, d), axis=0))

print('Concatenate arrays a and d along axis 1')
print(np.concatenate((a, d), axis=1))

print('Stack arrays vertically (row-wise)')
print(np.vstack((a, d)))

print('Stack arrays horizontally (column-wise)')
print(np.hstack((a, d)))

print('Column stack arrays')
print(np.column_stack((a, d)))

# Splitting arrays
print('\nSplitting arrays')
a = np.array([1, 2, 3, 4, 5, 6])
print('Split array a into 3 parts')
print(np.hsplit(a, 3))

c = np.array([[1.5, 2, 3], [4, 5, 6], [3, 2, 1], [4, 5, 6]])
print('Split array c into 2 parts vertically')
print(np.vsplit(c, 2))

# Create a 3D array
c = np.array([[(1.5, 2, 3), (4, 5, 6)], [(3, 2, 1), (4, 5, 6)]])
print('\n3D array')
print('c = np.array([[(1.5, 2, 3), (4, 5, 6)], [(3, 2, 1), (4, 5, 6)]])')
print(c)

# Create an array of zeros
d = np.zeros((3, 4))
print('\nArray of zeros')
print('d = np.zeros((3, 4))')
print(d)

# Create an array of ones
e = np.ones((2, 3), dtype=np.int16)
print('\nArray of ones')
print('e = np.ones((2, 3), dtype=np.int16)')
print(e)

# Create an array of evenly spaced values
f = np.arange(10, 25, 5)
print('\nArray of evenly spaced values')
print('f = np.arange(10, 25, 5)')
print(f)

# Create an array of evenly spaced values (number of samples)
g = np.linspace(0, 2, 9)
print('\nArray of evenly spaced values (number of samples)')
print('g = np.linspace(0, 2, 9)')
print(g)

# Create a constant array
h = np.full((2, 2), 7)
print('\nConstant array')
print('h = np.full((2, 2), 7)')
print(h)

# Create a 2x2 identity matrix
i = np.eye(2)
print('\n2x2 identity matrix')
print('i = np.eye(2)')
print(i)

# Create an array with random values
j = np.random.random((2, 2))
print('\nArray with random values')
print('j = np.random.random((2, 2))')
print(j)

# Create an empty array
k = np.empty((3, 2))
print('\nEmpty array')
print('k = np.empty((3, 2))')
print(k)

# I/O Saving & Loading on Disk
a = np.array([1, 2, 3])
b = np.array([10, 15, 20])
np.save('my_array', a)
np.savez('array.npz', a, b)
loaded_array = np.load('my_array.npy')
print('\nLoaded array from disk')
print(loaded_array)

# Saving & Loading Text Files
np.savetxt('myarray.txt', a, delimiter=' ')
loaded_txt_array = np.loadtxt('myarray.txt')
print('\nLoaded text array from disk')
print(loaded_txt_array)

# Inspecting Your Array
print('\nInspecting arrays')
print('a.shape:', a.shape)  # Array dimensions
print('len(a):', len(a))  # Length of array
print('b.ndim:', b.ndim)  # Number of array dimensions
print('e.size:', e.size)  # Number of array elements
print('b.dtype:', b.dtype)  # Data type of array elements
print('b.dtype.name:', b.dtype.name)  # Name of data type
print('b.astype(int):', b.astype(int))  # Convert an array to a different type

# Data Types
print('\nData types')
print('np.int64:', np.int64)  # Signed 64-bit integer types
print('np.float32:', np.float32)  # Standard double-precision floating point
print('complex:', complex)  # Complex numbers represented by 128 floats (use Python built-in 'complex')
print('np.complex128:', np.complex128)  # Alternatively, use np.complex128 for NumPy complex type
print('bool:', bool)  # Boolean type storing TRUE and FALSE values (use Python built-in 'bool')
print('np.bool_:', np.bool_)  # Alternatively, use np.bool_ for NumPy boolean type
print('object:', object)  # Python object type (use Python built-in 'object')
print('np.bytes_:', np.bytes_)  # Fixed-length string type
print('np.str_:', np.str_)  # Fixed-length unicode type

# Array Mathematics
a = np.array([[1.5, 2, 3], [4, 5, 6]])
b = np.array([[1, 2, 3], [4, 5, 6]])

print('\nArray Mathematics')
print('Subtraction')
print('g = a - b')
print(a - b)
print('np.subtract(a, b)')
print(np.subtract(a, b))

print('Addition')
print('b + a')
print(b + a)
print('np.add(b, a)')
print(np.add(b, a))

print('Division')
print('a / b')
print(a / b)
print('np.divide(a, b)')
print(np.divide(a, b))

print('Multiplication')
print('a * b')
print(a * b)
print('np.multiply(a, b)')
print(np.multiply(a, b))

print('Exponentiation')
print('np.exp(b)')
print(np.exp(b))

print('Square root')
print('np.sqrt(b)')
print(np.sqrt(b))

print('Sines')
print('np.sin(a)')
print(np.sin(a))

print('Cosines')
print('np.cos(b)')
print(np.cos(b))

print('Natural logarithm')
print('np.log(a)')
print(np.log(a))

# Ensure e and f are aligned for dot product
e = np.ones((2, 2), dtype=np.int16)  # Adjust e to be 2x2
f = np.full((2, 2), 7)  # Adjust f to be 2x2

print('Dot product')
print('e.dot(f)')
print(e.dot(f))

# Comparison
print('\nComparison')
print('a == b')
print(a == b)
print('a < 2')
print(a < 2)
print('np.array_equal(a, b)')
print(np.array_equal(a, b))

# Copying Arrays
print('\nCopying arrays')
h = a.view()  # Create a view of the array with the same data
print('a.view()')
print(h)

print('np.copy(a)')
print(np.copy(a))

h = a.copy()  # Create a deep copy of the array
print('a.copy()')
print(h)

# Sorting Arrays
print('\nSorting arrays')
print('a.sort()')
a.sort()
print(a)

print('c.sort(axis=0)')
c.sort(axis=0)
print(c)

# Ensure 'a' has enough elements
a = np.array([1, 2, 3])
print('\nArray a')
print('a = np.array([1, 2, 3])')
print(a)

import numpy as np

# Create a 3D array
c = np.array([[(1.5, 2, 3), (4, 5, 6)], [(3, 2, 1), (4, 5, 6)]])
print('\n3D array')
print('c = np.array([[(1.5, 2, 3), (4, 5, 6)], [(3, 2, 1), (4, 5, 6)]])')
print(c)

# Create an array of zeros
d = np.zeros((3, 4))
print('\nArray of zeros')
print('d = np.zeros((3, 4))')
print(d)

# Create an array of ones
e = np.ones((2, 3), dtype=np.int16)
print('\nArray of ones')
print('e = np.ones((2, 3), dtype=np.int16)')
print(e)

# Create an array of evenly spaced values
f = np.arange(10, 25, 5)
print('\nArray of evenly spaced values')
print('f = np.arange(10, 25, 5)')
print(f)

# Create an array of evenly spaced values (number of samples)
g = np.linspace(0, 2, 9)
print('\nArray of evenly spaced values (number of samples)')
print('g = np.linspace(0, 2, 9)')
print(g)

# Create a constant array
h = np.full((2, 2), 7)
print('\nConstant array')
print('h = np.full((2, 2), 7)')
print(h)

# Create a 2x2 identity matrix
i = np.eye(2)
print('\n2x2 identity matrix')
print('i = np.eye(2)')
print(i)

# Create an array with random values
j = np.random.random((2, 2))
print('\nArray with random values')
print('j = np.random.random((2, 2))')
print(j)

# Create an empty array
k = np.empty((3, 2))
print('\nEmpty array')
print('k = np.empty((3, 2))')
print(k)

# I/O Saving & Loading on Disk
a = np.array([1, 2, 3])
b = np.array([10, 15, 20])
np.save('my_array', a)
np.savez('array.npz', a, b)
loaded_array = np.load('my_array.npy')
print('\nLoaded array from disk')
print(loaded_array)

# Saving & Loading Text Files
np.savetxt('myarray.txt', a, delimiter=' ')
loaded_txt_array = np.loadtxt('myarray.txt')
print('\nLoaded text array from disk')
print(loaded_txt_array)

# Inspecting Your Array
print('\nInspecting arrays')
print('a.shape:', a.shape)  # Array dimensions
print('len(a):', len(a))  # Length of array
print('b.ndim:', b.ndim)  # Number of array dimensions
print('e.size:', e.size)  # Number of array elements
print('b.dtype:', b.dtype)  # Data type of array elements
print('b.dtype.name:', b.dtype.name)  # Name of data type
print('b.astype(int):', b.astype(int))  # Convert an array to a different type

# Data Types
print('\nData types')
print('np.int64:', np.int64)  # Signed 64-bit integer types
print('np.float32:', np.float32)  # Standard double-precision floating point
print('complex:', complex)  # Complex numbers represented by 128 floats (use Python built-in 'complex')
print('np.complex128:', np.complex128)  # Alternatively, use np.complex128 for NumPy complex type
print('bool:', bool)  # Boolean type storing TRUE and FALSE values (use Python built-in 'bool')
print('np.bool_:', np.bool_)  # Alternatively, use np.bool_ for NumPy boolean type
print('object:', object)  # Python object type (use Python built-in 'object')
print('np.bytes_:', np.bytes_)  # Fixed-length string type
print('np.str_:', np.str_)  # Fixed-length unicode type

# Array Mathematics
a = np.array([[1.5, 2, 3], [4, 5, 6]])
b = np.array([[1, 2, 3], [4, 5, 6]])

print('\nArray Mathematics')
print('Subtraction')
print('g = a - b')
print(a - b)
print('np.subtract(a, b)')
print(np.subtract(a, b))

print('Addition')
print('b + a')
print(b + a)
print('np.add(b, a)')
print(np.add(b, a))

print('Division')
print('a / b')
print(a / b)
print('np.divide(a, b)')
print(np.divide(a, b))

print('Multiplication')
print('a * b')
print(a * b)
print('np.multiply(a, b)')
print(np.multiply(a, b))

print('Exponentiation')
print('np.exp(b)')
print(np.exp(b))

print('Square root')
print('np.sqrt(b)')
print(np.sqrt(b))

print('Sines')
print('np.sin(a)')
print(np.sin(a))

print('Cosines')
print('np.cos(b)')
print(np.cos(b))

print('Natural logarithm')
print('np.log(a)')
print(np.log(a))

# Ensure e and f are aligned for dot product
e = np.ones((2, 2), dtype=np.int16)  # Adjust e to be 2x2
f = np.full((2, 2), 7)  # Adjust f to be 2x2

print('Dot product')
print('e.dot(f)')
print(e.dot(f))

# Comparison
print('\nComparison')
print('a == b')
print(a == b)
print('a < 2')
print(a < 2)
print('np.array_equal(a, b)')
print(np.array_equal(a, b))

# Copying Arrays
print('\nCopying arrays')
h = a.view()  
# Create a view of the array with the same data
print('a.view()')
print(h)

print('np.copy(a)')
print(np.copy(a))

h = a.copy()  
# Create a deep copy of the array
print('a.copy()')
print(h)

# Sorting Arrays
print('\nSorting arrays')
print('a.sort()')
a.sort()
print(a)

print('c.sort(axis=0)')
c.sort(axis=0)
print(c)

# Ensure 'a' has enough elements
a = np.array([1, 2, 3])
print('\nArray a')
print('a = np.array([1, 2, 3])')
print(a)

# Subsetting, Slicing, Indexing
print('\nSubsetting, slicing, indexing')
print('a[2]')
print(a[2])

print('b[1,2]')
print(b[1, 2])

print('a[0:2]')
print(a[0:2])

print('b[0:2,1]')
print(b[0:2, 1])

print('b[:1]')
print(b[:1])

print('c[1,...]')
print(c[1, ...])

print('a[::-1]')
print(a[::-1])

print('Boolean Indexing')
print('a[a < 2]')
print(a[a < 2])

print('Fancy Indexing')
print('b[[1,0,1, 0],[0,1, 2, 0]]')
print(b[[1, 0, 1, 0], [0, 1, 2, 0]])

print('b[[1,0,1, 0]][:,[0,1,2,0]]')
print(b[[1, 0, 1, 0]][:, [0, 1, 2, 0]])

# Array Manipulation
print('\nArray manipulation')
print('Transposing array')
i = np.transpose(b)
print('np.transpose(b)')
print(i)
print('i.T')
print(i.T)

print('Changing array shape')
print('b.ravel()')
print(b.ravel())
print('g.reshape(3, -2)')
print(g.reshape(3, -2))

print('Adding/Removing Elements')
h = np.array([[1, 2, 3], [4, 5, 6]])
print('h.resize((2,6))')
h.resize((2, 6))
print(h)
print('np.append(h,g)')
print(np.append(h, g))
print('np.insert(a, 1, 5)')
print(np.insert(a, 1, 5))
print('np.delete(a, [1])')
print(np.delete(a, [1]))





# Example arrays (adjust to match your actual data)
a = np.array([1, 2, 3])  # 1-dimensional array
d = np.array([[4, 5, 6], [7, 8, 9]])  # 2-dimensional array with shape (2, 3)

# Check shapes
print("Shape of a:", a.shape)  # Output: (3,)
print("Shape of d:", d.shape)  # Output: (2, 3)

# Reshape `a` to be compatible with `d` if needed
a = np.expand_dims(a, axis=0)  # Reshape `a` to (1, 3)
print('Combining arrays')
print('np.concatenate((a, d), axis=0)')
print(np.concatenate((a, d), axis=0))
print('np.vstack((a, b))')
print(np.vstack((a, b)))
print('np.r_[e, f]')
print(np.r_[e, f])

# Example arrays (adjust to match your actual data)
a = np.array([1, 2, 3])  # 1-dimensional array
d = np.array([[4, 5, 6], [7, 8, 9]])  # 2-dimensional array with shape (2, 3)

# Check shapes
print("Shape of a:", a.shape)  # Output: (3,)
print("Shape of d:", d.shape)  # Output: (2, 3)

# Reshape `a` to be compatible with `d` if needed
a = np.expand_dims(a, axis=0)  # Reshape `a` to (1, 3)

# Now, concatenate along axis 0
result = np.concatenate((a, d), axis=0)
print("Concatenated array:")
print(result)
print("Shape of concatenated array:", result.shape)

# Example arrays (adjust to match your actual data)
import numpy as np
import cv2
from PIL import Image
from io import BytesIO

# Create a grayscale image array
gray_img = np.zeros((256, 256), dtype=np.uint8)
print('\nGrayscale Image')
print('gray_img = np.zeros((256, 256), dtype=np.uint8)')
print(gray_img)

# Create a color image array
color_img = np.zeros((256, 256, 3), dtype=np.uint8)
print('\nColor Image')
print('color_img = np.zeros((256, 256, 3), dtype=np.uint8)')
print(color_img)

# Read an image using OpenCV (cv2)
img_path = '00004.jpg'
opencv_img = cv2.imread(img_path)
print('\nRead Image using OpenCV (cv2)')
print(f'opencv_img = cv2.imread("{img_path}")')
print(opencv_img)

# Convert an image to grayscale using OpenCV
gray_opencv_img = cv2.cvtColor(opencv_img, cv2.COLOR_BGR2GRAY)
print('\nConvert Image to Grayscale using OpenCV')
print('gray_opencv_img = cv2.cvtColor(opencv_img, cv2.COLOR_BGR2GRAY)')
print(gray_opencv_img)

# Convert an image array to PIL Image
pil_img = Image.fromarray(opencv_img)
print('\nConvert Image Array to PIL Image')
print('pil_img = Image.fromarray(opencv_img)')
print(pil_img)

# Convert a PIL Image to numpy array
numpy_img = np.array(pil_img)
print('\nConvert PIL Image to Numpy Array')
print('numpy_img = np.array(pil_img)')
print(numpy_img)

# Save an image using OpenCV
save_path = 'image.jpg'
cv2.imwrite(save_path, opencv_img)
print(f'\nSave Image using OpenCV: {save_path}')

# Load an image from BytesIO using PIL
bytes_img = BytesIO()
pil_img.save(bytes_img, format='JPEG')
bytes_img.seek(0)
loaded_pil_img = Image.open(bytes_img)
loaded_numpy_img = np.array(loaded_pil_img)
print('\nLoad Image from BytesIO using PIL')
print('loaded_pil_img = Image.open(bytes_img)')
print('loaded_numpy_img = np.array(loaded_pil_img)')

# Resize an image using OpenCV
resized_img = cv2.resize(opencv_img, (512, 512))
print('\nResize Image using OpenCV')
print('resized_img = cv2.resize(opencv_img, (512, 512))')
print(resized_img)

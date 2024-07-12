import numpy as np
# Create a 1D array
a = np.array([1, 2, 3])
print('\n1D array')
print('a = np.array([1, 2, 3])')
print(a)

# Create a 2D array
b = np.array([(1.5, 2, 3), (4, 5, 6)])
print('\n2D array')
print('b = np.array([(1.5, 2, 3), (4, 5, 6)])')
print(b)

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
f = np.eye(2)
print('\n2x2 Identity matrix')
print('f = np.eye(2)')
print(f)

# Create an array with random values
g = np.random.random((2, 2))
print('\nArray with random values')
print('g = np.random.random((2, 2))')
print(g)

# Create an empty array
h = np.empty((3, 2))
print('\nEmpty array')
print('h = np.empty((3, 2))')
print(h)

# Save and load arrays on disk
a = np.array([1, 2, 3])
b = np.array([10, 15, 20])
np.save('my_array', a)
np.savez('array.npz', a, b)
loaded_a = np.load('my_array.npy')
loaded_data = np.load('array.npz')

print('\nSaved and loaded array a')
print('np.save("my_array", a)')
print('loaded_a = np.load("my_array.npy")')
print(loaded_a)

print('\nSaved and loaded arrays a and b in .npz file')
print('np.savez("array.npz", a, b)')
print('loaded_data = np.load("array.npz")')
print('loaded_data["arr_0"]:', loaded_data['arr_0'])
print('loaded_data["arr_1"]:', loaded_data['arr_1'])

# Save and load text files
np.savetxt('myarray.txt', a, delimiter=" ")
loaded_txt = np.loadtxt("myarray.txt")

print('\nSaved and loaded text file')
print('np.savetxt("myarray.txt", a, delimiter=" ")')
print('loaded_txt = np.loadtxt("myarray.txt")')
print(loaded_txt)

# Inspecting your array
print('\nInspecting your array')
print('a.shape:', a.shape)  # Array dimensions
print('len(a):', len(a))    # Length of array
print('b.ndim:', b.ndim)    # Number of array dimensions
print('e.size:', e.size)    # Number of array elements
print('b.dtype:', b.dtype)  # Data type of array elements
print('b.dtype.name:', b.dtype.name)  # Name of data type
print('b.astype(int):', b.astype(int))  # Convert an array to a different type

# Data types
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

# Array mathematics
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1.5, 2, 3], [4, 5, 6]])

print('\nArray mathematics')
print('Subtraction')
print('g = a - b')
g = a - b
print(g)

print('np.subtract(a, b)')
g = np.subtract(a, b)
print(g)

print('Addition')
print('b + a')
g = b + a
print(g)

print('np.add(b, a)')
g = np.add(b, a)
print(g)

print('Division')
print('a / b')
g = a / b
print(g)

print('np.divide(a, b)')
g = np.divide(a, b)
print(g)

print('Multiplication')
print('a * b')
g = a * b
print(g)

print('np.multiply(a, b)')
g = np.multiply(a, b)
print(g)

print('Exponentiation')
print('np.exp(b)')
g = np.exp(b)
print(g)

print('Square root')
print('np.sqrt(b)')
g = np.sqrt(b)
print(g)

print('Print sines of an array')
print('np.sin(a)')
g = np.sin(a)
print(g)

print('Elementwise cosine')
print('np.cos(b)')
g = np.cos(b)
print(g)

print('Elementwise natural logarithm')
print('np.log(a)')
g = np.log(a)
print(g)

print('Dot product')
print('e.dot(f)')
g = e.dot(f)
print(g)

# Comparison
print('\nComparison')
print('Elementwise comparison')
print('a == b')
g = a == b
print(g)

print('a < 2')
g = a < 2
print(g)

print('Arraywise comparison')
print('np.array_equal(a, b)')
g = np.array_equal(a, b)
print(g)

# Copying arrays
print('\nCopying arrays')
print('Create a view of the array with the same data')
h = a.view()
print('h = a.view()')
print(h)

print('Create a copy of the array')
h = np.copy(a)
print('h = np.copy(a)')
print(h)

print('Create a deep copy of the array')
h = a.copy()
print('h = a.copy()')
print(h)

# Sorting arrays
print('\nSorting arrays')
print('Sort an array')
a.sort()
print('a.sort()')
print(a)

print('Sort the elements of an array\'s axis')
c = np.array([[(1.5, 2, 3), (4, 5, 6)], [(3, 2, 1), (4, 5, 6)]])
c.sort(axis=0)
print('c.sort(axis=0)')
print(c)

# Subsetting, slicing, indexing
print('\nSubsetting, slicing, indexing')
print('Select the element at the 2nd index')
print('a[2]')
print(a[2])

print('Select the element at row 1 column 2')
print('b[1, 2]')
print(b[1, 2])

print('Select items at index 0 and 1')
print('a[0:2]')
print(a[0:2])

print('Select items at rows 0 and 1 in column 1')
print('b[0:2, 1]')
print(b[0:2, 1])

print('Select all items at row 0')
print('b[:1]')
print(b[:1])

print('Same as [1,:,:]')
print('c[1,...]')
print(c[1, ...])

print('Reversed array a')
print('a[::-1]')
print(a[::-1])

# Boolean indexing
print('\nBoolean indexing')
print('Select elements from a less than 2')
print('a[a < 2]')
print(a[a < 2])

# Fancy indexing
print('\nFancy indexing')
print('Select elements (1, 0), (0, 1), (1, 2), and (0, 0)')
print('b[[1, 0, 1, 0], [0, 1, 2, 0]]')
print(b[[1, 0, 1, 0], [0, 1, 2, 0]])

print('Select a subset of the matrix’s rows and columns')
print('b[[1, 0, 1, 0]][:, [0, 1, 2, 0]]')
print(b[[1, 0, 1, 0]][:, [0, 1, 2, 0]])

# Array manipulation
print('\nArray manipulation')
print('Transpose array')
print('i = np.transpose(b)')
i = np.transpose(b)
print(i)

print('Permute array dimensions')
print('i.T')
print(i.T)

print('Flatten the array')
print('b.ravel()')
print(b.ravel())

print('Reshape, but don’t change data')
print('g.reshape(3, -1)')
print(g.reshape(3, -1))

print('Return a new array with shape (2, 6)')
print('h.resize((2, 6))')
h.resize((2, 6))
print(h)

print('Append items to an array')
print('np.append(h, g)')
print(np.append(h, g))

print('Insert items in an array')
print('np.insert(a, 1, 5)')
print(np.insert(a, 1, 5))

print('Delete items from an array')
print('np.delete(a, [1])')
print(np.delete(a, [1]))

# Combining arrays
print('\nCombining arrays')
print('Concatenate arrays')
print('np.concatenate((a, d), axis=0)')
d = np.array([[10, 15, 20]])
print(np.concatenate((a, d), axis=0))

print('Stack arrays vertically (row wise)')
print('np.vstack((a, b))')
print(np.vstack((a, b)))

print('Stack arrays vertically (row wise)')
print('np.r_[e, f]')
print(np.r_[e, f])

print('Stack arrays horizontally (column wise)')
print('np.hstack((e, f))')
print(np.hstack((e, f)))

print('Create stacked column wise arrays')
print('np.column_stack((a, d))')
print(np.column_stack((a, d)))

print('Create stacked column wise arrays')
print('np.c_[a, d]')
print(np.c_[a, d])

# Splitting arrays
print('\nSplitting arrays')
print('Split the array horizontally at the 3rd index')
print('np.hsplit(a, 3)')
print(np.hsplit(a, 3))

print('Split the array vertically at the 2nd index')
print('np.vsplit(c, 2)')
print(np.vsplit(c, 2))

'''Numpy Arrays
np.linspace(0,2,9) #Create an array of evenlyspaced values (number of samples)
e = np.full((2,2),7)#Create a constant array
f = np.eye(2) #Create a 2X2 identity matrix
np.random.random((2,2)) #Create an array with random values
np.empty((3,2)) #Create an empty array I/O Saving & Loading on Disk
np.save('my_array' , a)
np.savez( 'array.npz', a, b)
np.load( 'my_array.npy') Saving & Loading Text Files
np.loadtxt("myfile.txt")
np.genfromtxt("my_file.csv", delimiter= ',')
np.savetxt( "myarray.txt", a, delimiter= " ") Asking For Help
np.info(np.ndarray.dtype) Inspecting Your Array
a.shape #Array dimensions
len(a)#Length of array
b.ndim #Number of array dimensions
e.size #Number of array elements
b.dtype #Data type of array elements
b.dtype.name #Name of data type
b.astype(int). #Convert an array to a different type Data Types
np.int64 #Signed 64-bit integer types
np.float32. #Standard double-precision floating point
np.complex. #Complex numbers represented by 128 floats
np.bool #Boolean type storing TRUE and FALSE values
np.object #Python object type
np.string_ #Fixed-length string type
np.unicode_ #Fixed-length unicode type Array Mathematics Arithmetic Operations
g = a - b. #Subtraction array([[-0.5,0. ,0.], [-3. , -3. , -3. ]])
np.subtract(a,b) #Subtraction
b + a #Addition array([[ 2.5, 4. , 6.],[5. ,7. ,9. ]])
np.add(b,a) #Addition
a/b #Division array([[0.66666667,1. ,1.],[0.25 ,0.4 ,0.5 ]])
np.divide(a,b) #Division
a * b #Multiplication array([[1.5, 4. ,9.],[ 4. , 10. , 18. ]])
np.multiply(a,b) #Multiplication
np.exp(b) #Exponentiation
np.sqrt(b) #Square root
np.sin(a) #Print sines of an array
np.cos(b) #Elementwise cosine
np.log(a)#Elementwise natural logarithm
e.dot(f) #Dot product array([[7.,7.],[7.,7.]]) Comparison
a == b #Elementwise comparison array([[False , True, True], [ False,False ,False ]], dtype=bool)
a < 2 #Elementwise comparison array([True, False, False], dtype=bool)
np.array_equal(a, b) #Arraywise comparison Copying Arrays h = a.view()#Create a view of the array with the same data
np.copy(a) #Create a copy of the array h = a.copy() #Create a deep copy of the array Sorting Arrays
a.sort() #Sort an array
c.sort(axis=0) #Sort the elements of an array's axis Subsetting, Slicing, Indexing Subsetting
a[2] #Select the element at the 2nd index 3
b[1,2] #Select the element at row 1 column 2(equivalent to b[1][2]) 6.0 Slicing
a[0:2]#Select items at index 0 and 1 array([1, 2])
b[0:2,1] #Select items at rows 0 and 1 in column 1 array([ 2.,5.])
b[:1] #Select all items at row0(equivalent to b[0:1, :]) array([[1.5, 2., 3.]])
c[1,...] #Same as[1,:,:] array([[[ 3., 2.,1.],[ 4.,5., 6.]]])
a[ : : -1] #Reversed array a array([3, 2, 1]) Boolean Indexing
a[a #Select elements from a less than 2 array([1]) Fancy Indexing
b[[1,0,1, 0],[0,1, 2, 0]] #Select elements(1,0),(0,1),(1,2) and(0,0) array([ 4. , 2. , 6. ,1.5])
b[[1,0,1, 0]][:,[0,1,2,0]] #Select a subset of the matrix’s rows and columns array([[ 4. ,5. , 6. , 4.],[1.5, 2. , 3. ,1.5],[ 4. ,5. , 6. , 4.],[1.5, 2. , 3. ,1.5]]) Array Manipulation Transposing Array
i = np.transpose(b) #Permute array dimensions
i.T #Permute array dimensions Changing Array Shape
b.ravel() #Flatten the array
g.reshape(3, -2) #Reshape, but don’t change data Adding/Removing Elements h.resize((2,6)) #Return a new arraywith shape(2,6)
np.append(h,g) #Append items to an array
np.insert(a,1,5) #Insert items in an array
np.delete(a,[1]) #Delete items from an array Combining Arrays
np.concatenate((a,d),axis=0) #Concatenate arrays array([1, 2, 3, 10, 15, 20])
np.vstack((a,b) #Stack arrays vertically(row wise) array([[1. , 2. , 3.],[1.5, 2. , 3.],[ 4. ,5. , 6. ]])
np.r_[e,f] #Stack arrays vertically(row wise)
np.hstack((e,f)) #Stack arrays horizontally(column wise) array([[7.,7.,1.,0.],[7.,7.,0.,1.]])
np.column_stack((a,d)) #Create stacked column wise arrays array([[1, 10],[ 2, 15],[ 3, 20]])
np.c_[a,d] #Create stacked column wise arrays Splitting Arrays
np.hsplit(a,3) #Split the array horizontally at the 3rd index [array([1]),array([2]),array([3])]
np.vsplit(c,2) #Split the array vertically at the 2nd index [array([[[ 1.5, 2. ,1.],[ 4. ,5. , 6. ]]]), array([[[ 3., 2., 3.],[ 4.,5., 6.]]]) 

Creating Arrays

a = np.array([1,2,3])
b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
c = np.array([[(1.5,2,3), (4,5,6)],[(3,2,1), (4,5,6)]], dtype = float) Initial Placeholders
np.zeros((3,4)) #Create an array of zeros
np.ones((2,3,4),dtype=np.int16) #Create an array of ones
d = np.arange(10,25,5)#Create an array of evenly spaced values (step value)
'''
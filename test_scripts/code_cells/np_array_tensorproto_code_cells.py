import numpy
import onnx
import os
from onnx import numpy_helper


# Preprocessing: create a Numpy array
numpy_array = numpy.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=float)
print('Original Numpy array:\n{}\n'.format(numpy.array2string(numpy_array)))

# Convert the Numpy array to a TensorProto
tensor = numpy_helper.from_array(numpy_array)
print('TensorProto:\n{}'.format(tensor))

# Convert the TensorProto to a Numpy array
new_array = numpy_helper.to_array(tensor)
print('After round trip, Numpy array:\n{}\n'.format(numpy.array2string(numpy_array)))

# Save the TensorProto
with open(os.path.join('resources', 'tensor.pb'), 'wb') as f:
    f.write(tensor.SerializeToString())

# Load the TensorProto
new_tensor = onnx.TensorProto()
with open(os.path.join('resources', 'tensor.pb'), 'rb') as f:
    new_tensor.ParseFromString(f.read())
print('After saving and loading, new TensorProto:\n{}'.format(new_tensor))


import onnx
import os


# Preprocessing: load the old model
old_model_path = os.path.join('resources', 'single_relu.onnx')
onnx_model = onnx.load(old_model_path)

# Preprocessing: get the path to the saved model
new_model_path = os.path.join('resources', 'single_relu_new.onnx')

# Save the ONNX model
onnx.save(onnx_model, new_model_path)

print('The model is saved.')


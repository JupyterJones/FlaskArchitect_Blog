#@title Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tensorflow as tf

class Model(tf.Module):

  @tf.function(input_signature=[tf.TensorSpec(shape=[None], dtype=tf.float32)])
  def encode(self, x):
    result = tf.strings.as_string(x)
    return {
         "encoded_result": result
    }

  @tf.function(input_signature=[tf.TensorSpec(shape=[None], dtype=tf.string)])
  def decode(self, x):
    result = tf.strings.to_number(x)
    return {
         "decoded_result": result
    }

model = Model()

# Save the model
SAVED_MODEL_PATH = 'content/saved_models/coding'

tf.saved_model.save(
    model, SAVED_MODEL_PATH,
    signatures={
      'encode': model.encode.get_concrete_function(),
      'decode': model.decode.get_concrete_function()
    })

# Convert the saved model using TFLiteConverter
converter = tf.lite.TFLiteConverter.from_saved_model(SAVED_MODEL_PATH)
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS,  # enable TensorFlow Lite ops.
    tf.lite.OpsSet.SELECT_TF_OPS  # enable TensorFlow ops.
]
tflite_model = converter.convert()

# Print the signatures from the converted model
interpreter = tf.lite.Interpreter(model_content=tflite_model)
signatures = interpreter.get_signature_list()
print(signatures)

# Generate a Keras model.
keras_model = tf.keras.Sequential(
    [
        tf.keras.layers.Dense(2, input_dim=4, activation='relu', name='x'),
        tf.keras.layers.Dense(1, activation='relu', name='output'),
    ]
)

# Convert the keras model using TFLiteConverter.
# Keras model converter API uses the default signature automatically.
converter = tf.lite.TFLiteConverter.from_keras_model(keras_model)
tflite_model = converter.convert()

# Print the signatures from the converted model
interpreter = tf.lite.Interpreter(model_content=tflite_model)

signatures = interpreter.get_signature_list()
print(signatures)

model = Model()

# Convert the concrete functions using TFLiteConverter
converter = tf.lite.TFLiteConverter.from_concrete_functions(
    [model.encode.get_concrete_function(),
     model.decode.get_concrete_function()], model)
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS,  # enable TensorFlow Lite ops.
    tf.lite.OpsSet.SELECT_TF_OPS  # enable TensorFlow ops.
]
tflite_model = converter.convert()

# Print the signatures from the converted model
interpreter = tf.lite.Interpreter(model_content=tflite_model)
signatures = interpreter.get_signature_list()
print(signatures)

# Load the TFLite model in TFLite Interpreter
interpreter = tf.lite.Interpreter(model_content=tflite_model)

# Print the signatures from the converted model
signatures = interpreter.get_signature_list()
print('Signature:', signatures)

# encode and decode are callable with input as arguments.
encode = interpreter.get_signature_runner('encode')
decode = interpreter.get_signature_runner('decode')

# 'encoded' and 'decoded' are dictionaries with all outputs from the inference.
input = tf.constant([1, 2, 3], dtype=tf.float32)
print('Input:', input)
encoded = encode(x=input)
print('Encoded result:', encoded)
decoded = decode(x=encoded['encoded_result'])
print('Decoded result:', decoded)


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

@tf.function(input_signature=[
    tf.TensorSpec(shape=[None], dtype=tf.float32)
])
def f(x):
  return tf.cosh(x)

# Evaluate the tf.function
result = f(tf.constant([0.0]))
print (f"result = {result}")

# Convert the tf.function
converter = tf.lite.TFLiteConverter.from_concrete_functions(
    [f.get_concrete_function()], f)
try:
  fb_model = converter.convert()
except Exception as e:
  print(f"Got an exception: {e}")

@tf.lite.experimental.authoring.compatible
@tf.function(input_signature=[
    tf.TensorSpec(shape=[None], dtype=tf.float32)
])
def f(x):
  return tf.cosh(x)

# Evaluate the tf.function
result = f(tf.constant([0.0]))
print (f"result = {result}")


compatibility_log = '\n'.join(f.get_compatibility_log())
print (f"compatibility_log = {compatibility_log}")

@tf.lite.experimental.authoring.compatible(raise_exception=True)
@tf.function(input_signature=[
    tf.TensorSpec(shape=[None], dtype=tf.float32)
])
def f(x):
  return tf.cosh(x)

# Evaluate the tf.function
try:
  result = f(tf.constant([0.0]))
  print (f"result = {result}")
except Exception as e:
  print(f"Got an exception: {e}")

target_spec = tf.lite.TargetSpec()
target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS,
    tf.lite.OpsSet.SELECT_TF_OPS,
]
@tf.lite.experimental.authoring.compatible(converter_target_spec=target_spec, raise_exception=True)
@tf.function(input_signature=[
    tf.TensorSpec(shape=[None], dtype=tf.float32)
])
def f(x):
  return tf.cosh(x)

# Evaluate the tf.function
result = f(tf.constant([0.0]))
print (f"result = {result}")


target_spec = tf.lite.TargetSpec()
target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS,
    tf.lite.OpsSet.SELECT_TF_OPS,
]
target_spec.experimental_supported_backends = ["GPU"]
@tf.lite.experimental.authoring.compatible(converter_target_spec=target_spec)
@tf.function(input_signature=[
    tf.TensorSpec(shape=[4, 4], dtype=tf.float32)
])
def func(x):
  y = tf.cosh(x)
  return y + tf.slice(x, [1, 1], [1, 1])

result = func(tf.ones(shape=(4,4), dtype=tf.float32))


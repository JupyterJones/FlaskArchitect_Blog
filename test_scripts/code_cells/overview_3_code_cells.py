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

!pip install tf-nightly --upgrade
!pip install jax --upgrade
!pip install jaxlib --upgrade

import numpy as np
import tensorflow as tf
import functools

import time
import itertools

import numpy.random as npr

import jax.numpy as jnp
from jax import jit, grad, random
from jax.example_libraries import optimizers
from jax.example_libraries import stax


def _one_hot(x, k, dtype=np.float32):
  """Create a one-hot encoding of x of size k."""
  return np.array(x[:, None] == np.arange(k), dtype)

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
train_images, test_images = train_images / 255.0, test_images / 255.0
train_images = train_images.astype(np.float32)
test_images = test_images.astype(np.float32)

train_labels = _one_hot(train_labels, 10)
test_labels = _one_hot(test_labels, 10)

def loss(params, batch):
  inputs, targets = batch
  preds = predict(params, inputs)
  return -jnp.mean(jnp.sum(preds * targets, axis=1))

def accuracy(params, batch):
  inputs, targets = batch
  target_class = jnp.argmax(targets, axis=1)
  predicted_class = jnp.argmax(predict(params, inputs), axis=1)
  return jnp.mean(predicted_class == target_class)

init_random_params, predict = stax.serial(
    stax.Flatten,
    stax.Dense(1024), stax.Relu,
    stax.Dense(1024), stax.Relu,
    stax.Dense(10), stax.LogSoftmax)

rng = random.PRNGKey(0)

step_size = 0.001
num_epochs = 10
batch_size = 128
momentum_mass = 0.9


num_train = train_images.shape[0]
num_complete_batches, leftover = divmod(num_train, batch_size)
num_batches = num_complete_batches + bool(leftover)

def data_stream():
  rng = npr.RandomState(0)
  while True:
    perm = rng.permutation(num_train)
    for i in range(num_batches):
      batch_idx = perm[i * batch_size:(i + 1) * batch_size]
      yield train_images[batch_idx], train_labels[batch_idx]
batches = data_stream()

opt_init, opt_update, get_params = optimizers.momentum(step_size, mass=momentum_mass)

@jit
def update(i, opt_state, batch):
  params = get_params(opt_state)
  return opt_update(i, grad(loss)(params, batch), opt_state)

_, init_params = init_random_params(rng, (-1, 28 * 28))
opt_state = opt_init(init_params)
itercount = itertools.count()

print("\nStarting training...")
for epoch in range(num_epochs):
  start_time = time.time()
  for _ in range(num_batches):
    opt_state = update(next(itercount), opt_state, next(batches))
  epoch_time = time.time() - start_time

  params = get_params(opt_state)
  train_acc = accuracy(params, (train_images, train_labels))
  test_acc = accuracy(params, (test_images, test_labels))
  print("Epoch {} in {:0.2f} sec".format(epoch, epoch_time))
  print("Training set accuracy {}".format(train_acc))
  print("Test set accuracy {}".format(test_acc))

serving_func = functools.partial(predict, params)
x_input = jnp.zeros((1, 28, 28))
converter = tf.lite.TFLiteConverter.experimental_from_jax(
    [serving_func], [[('input1', x_input)]])
tflite_model = converter.convert()
with open('jax_mnist.tflite', 'wb') as f:
  f.write(tflite_model)

expected = serving_func(train_images[0:1])

# Run the model with TensorFlow Lite
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
interpreter.set_tensor(input_details[0]["index"], train_images[0:1, :, :])
interpreter.invoke()
result = interpreter.get_tensor(output_details[0]["index"])

# Assert if the result of TFLite model is consistent with the JAX model.
np.testing.assert_almost_equal(expected, result, 1e-5)

def representative_dataset():
  for i in range(1000):
    x = train_images[i:i+1]
    yield [x]

converter = tf.lite.TFLiteConverter.experimental_from_jax(
    [serving_func], [[('x', x_input)]])
tflite_model = converter.convert()
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
tflite_quant_model = converter.convert()
with open('jax_mnist_quant.tflite', 'wb') as f:
  f.write(tflite_quant_model)

expected = serving_func(train_images[0:1])

# Run the model with TensorFlow Lite
interpreter = tf.lite.Interpreter(model_content=tflite_quant_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
interpreter.set_tensor(input_details[0]["index"], train_images[0:1, :, :])
interpreter.invoke()
result = interpreter.get_tensor(output_details[0]["index"])

# Assert if the result of TFLite model is consistent with the Jax model.
np.testing.assert_almost_equal(expected, result, 1e-5)

!du -h jax_mnist.tflite
!du -h jax_mnist_quant.tflite


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

!pip install --quiet --upgrade tf-nightly
!pip install --quiet --upgrade tensorflow-datasets

import collections
import functools
import matplotlib.pyplot as plt
import os
import tempfile
import tensorflow as tf
import tensorflow.experimental.numpy as tnp
import tensorflow_datasets as tfds

gpus = tf.config.list_physical_devices('GPU')
if gpus:
  tf.config.set_logical_device_configuration(gpus[0], [
      tf.config.LogicalDeviceConfiguration(memory_limit=128),
      tf.config.LogicalDeviceConfiguration(memory_limit=128)])
  devices = tf.config.list_logical_devices('GPU')
else:
  cpus = tf.config.list_physical_devices('CPU')
  tf.config.set_logical_device_configuration(cpus[0], [
      tf.config.LogicalDeviceConfiguration(),
      tf.config.LogicalDeviceConfiguration()])
  devices = tf.config.list_logical_devices('CPU')

print("Using following virtual devices", devices)

NUM_CLASSES = 10
BATCH_SIZE = 64
INPUT_SIZE = 28 * 28

def process_data(data_dict):
  images = tnp.asarray(data_dict['image']) / 255.0
  images = images.reshape(-1, INPUT_SIZE).astype(tnp.float32)
  labels = tnp.asarray(data_dict['label'])
  labels = tnp.eye(NUM_CLASSES, dtype=tnp.float32)[labels]
  return images, labels

with tf.device("CPU:0"):
  train_dataset = tfds.load('mnist', split='train', shuffle_files=True, 
                            batch_size=BATCH_SIZE).map(process_data)
  test_dataset = tfds.load('mnist', split='test', shuffle_files=True, 
                          batch_size=-1)
  x_test, y_test = process_data(test_dataset)

  # Plots some examples.
  images, labels = next(iter(train_dataset.take(1)))
  _, axes = plt.subplots(1, 8, figsize=(12, 96))
  for i, ax in enumerate(axes):
    ax.imshow(images[i].reshape(28, 28), cmap='gray')
    ax.axis("off")
    ax.set_title("Label: %d" % int(tnp.argmax(labels[i])))

class Dense(tf.Module):

  def __init__(self, units, use_relu=True):
    self.wt = None
    self.bias = None
    self._use_relu = use_relu
    self._built = False
    self._units = units

  def __call__(self, inputs):
    if not self._built:
      self._build(inputs.shape)
    x = tnp.add(tnp.matmul(inputs, self.wt), self.bias)
    if self._use_relu:
      return tnp.maximum(x, 0.)
    else:
      return x

  @property
  def params(self):
    assert self._built
    return [self.wt, self.bias]

  def _build(self, input_shape):
    size = input_shape[1]
    stddev = 1 / tnp.sqrt(size)
    # Note that model parameters are `tf.Variable` since they requires
    # mutation, which is currently unsupported by TensorFlow NumPy.
    # Also note interoperation with TensorFlow APIs below.
    self.wt = tf.Variable(
        tf.random.truncated_normal(
            [size, self._units], stddev=stddev, dtype=tf.float32))
    self.bias = tf.Variable(tf.zeros([self._units], dtype=tf.float32))
    self._built = True

class Model(tf.Module):
  """A  three layer neural network."""

  def __init__(self):
    self.layer1 = Dense(128)
    self.layer2 = Dense(32)
    self.layer3 = Dense(NUM_CLASSES, use_relu=False)

  def __call__(self, inputs):
    x = self.layer1(inputs)
    x = self.layer2(x)
    return self.layer3(x)

  @property
  def params(self):
    return self.layer1.params + self.layer2.params + self.layer3.params

def forward(model, inputs, labels):
  """Computes prediction and loss."""
  logits = model(inputs)
  # TensorFlow's loss function has numerically stable implementation of forward
  # pass and gradients. So we prefer that here.
  loss = tf.nn.softmax_cross_entropy_with_logits(labels, logits)
  mean_loss = tnp.mean(loss)
  return logits, mean_loss

def compute_gradients(model, inputs, labels):
  """Computes gradients of loss based on `labels` and prediction on `inputs`."""
  with tf.GradientTape() as tape:
    tape.watch(inputs)
    _, loss = forward(model, inputs, labels)
  gradients = tape.gradient(loss, model.params)
  return gradients

def compute_sgd_updates(gradients, learning_rate):
  """Computes parameter updates based on SGD update rule."""
  return [-learning_rate * grad for grad in gradients]

def apply_updates(model, updates):
  """Applies `update` to `model.params`."""
  for param, update in zip(model.params, updates):
    param.assign_add(update)

def evaluate(model, images, labels):
  """Evaluates accuracy for `model`'s predictions."""
  prediction = model(images)
  predicted_class = tnp.argmax(prediction, axis=-1)
  actual_class = tnp.argmax(labels, axis=-1)
  return float(tnp.mean(predicted_class == actual_class))

NUM_EPOCHS = 10

@tf.function
def train_step(model, input, labels, learning_rate):
  gradients = compute_gradients(model, input, labels)
  updates = compute_sgd_updates(gradients, learning_rate)
  apply_updates(model, updates)

# Creates and build a model.
model = Model()

accuracies = []
for _ in range(NUM_EPOCHS):
  for inputs, labels in train_dataset:
    train_step(model, inputs, labels, learning_rate=0.1)
  accuracies.append(evaluate(model, x_test, y_test))

def plot_accuracies(accuracies):
  plt.plot(accuracies)
  plt.xlabel("epoch")
  plt.ylabel("accuracy")
  plt.title("Eval accuracy vs epoch")

plot_accuracies(accuracies)

# A temporary directory to save our models into.
dir = tempfile.TemporaryDirectory()

# We take our model, and create a wrapper for it.
class SaveableModel(Model):
  @tf.function
  def __call__(self, inputs):
    return super().__call__(inputs)

saveable_model = SaveableModel()

# This saves a concrete function that we care about.
outputs = saveable_model(x_test)

# This saves the model to disk.
tf.saved_model.save(saveable_model, dir.name)

loaded = tf.saved_model.load(dir.name)
outputs_loaded = loaded(x_test)

# Ensure that the loaded model preserves the weights
# of the saved model.
assert tnp.allclose(outputs, outputs_loaded)

import threading
import queue

# Note that this code currently relies on dispatching operations from python
# threads.
class ReplicatedFunction(object):
  """Creates a callable that will run `fn` on each device in `devices`."""

  def __init__(self, fn, devices, **kw_args):
    self._shutdown = False

    def _replica_fn(device, input_queue, output_queue):
      while not self._shutdown:
        inputs = input_queue.get()
        with tf.device(device):
          output_queue.put(fn(*inputs, **kw_args))

    self.threads = []
    self.input_queues = [queue.Queue() for _ in devices]
    self.output_queues = [queue.Queue() for _ in devices]
    for i, device in enumerate(devices):
      thread = threading.Thread(
          target=_replica_fn,
          args=(device, self.input_queues[i], self.output_queues[i]))
      thread.start()
      self.threads.append(thread)

  def __call__(self, *inputs):
    all_inputs = zip(*inputs)
    for input_queue, replica_input, in zip(self.input_queues, all_inputs):
      input_queue.put(replica_input)
    return [q.get() for q in self.output_queues]

  def __del__(self):
    self._shutdown = True
    for t in self.threads:
      t.join(3)
    self.threads = None

def collective_mean(inputs, num_devices):
  """Performs collective mean reduction on inputs."""
  outputs = []
  for instance_key, inp in enumerate(inputs):
    outputs.append(tnp.asarray(
      tf.raw_ops.CollectiveReduce(
          input=inp, group_size=num_devices, group_key=0,
          instance_key=instance_key, merge_op='Add', final_op='Div',
          subdiv_offsets=[])))
  return outputs

# This is similar to `train_step` except for an extra collective reduction of
# gradients
@tf.function
def replica_step(model, inputs, labels,
                 learning_rate=None, num_devices=None):
  gradients = compute_gradients(model, inputs, labels)
  # Note that each replica performs a reduction to compute mean of gradients.
  reduced_gradients = collective_mean(gradients, num_devices)
  updates = compute_sgd_updates(reduced_gradients, learning_rate)
  apply_updates(model, updates)

models = [Model() for _ in devices]

# The code below builds all the model objects and copies model parameters from
# the first model to all the replicas.
def init_model(model):
  model(tnp.zeros((1, INPUT_SIZE), dtype=tnp.float32))
  if model != models[0]:
    # Copy the first models weights into the other models.
    for p1, p2 in zip(model.params, models[0].params):
      p1.assign(p2)

with tf.device(devices[0]):
  init_model(models[0])
# Replicate and run the parameter initialization.
ReplicatedFunction(init_model, devices[1:])(models[1:])

# Replicate the training step
replicated_step = ReplicatedFunction(
    replica_step, devices, learning_rate=0.1, num_devices=len(devices))

accuracies = []
print("Running distributed training on devices: %s" % devices)
for _ in range(NUM_EPOCHS):
  for inputs, labels in train_dataset:
    replicated_step(models,
                    tnp.split(inputs, len(devices)),
                    tnp.split(labels, len(devices)))
  accuracies.append(evaluate(models[0], x_test, y_test))

plot_accuracies(accuracies)


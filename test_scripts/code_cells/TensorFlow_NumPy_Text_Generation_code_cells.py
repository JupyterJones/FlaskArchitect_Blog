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
import tensorflow.experimental.numpy as tnp

import numpy as np
import os
import time

path_to_file = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')

# Read, then decode for py2 compat.
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
# length of text is the number of characters in it
print ('Length of text: {} characters'.format(len(text)))

# Take a look at the first 250 characters in text
print(text[:250])

# The unique characters in the file
vocab = sorted(set(text))
print ('{} unique characters'.format(len(vocab)))

# Creating a mapping from unique characters to indices
char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

text_as_int = np.array([char2idx[c] for c in text])

# The maximum length sentence we want for a single input in characters
seq_length = 100
examples_per_epoch = len(text)//(seq_length+1)

# Create training examples / targets
char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)

for i in char_dataset.take(5):
  print(idx2char[i.numpy()])

sequences = char_dataset.batch(seq_length+1, drop_remainder=True)

for item in sequences.take(5):
  print(repr(''.join(idx2char[item.numpy()])))

def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text

dataset = sequences.map(split_input_target)

for input_example, target_example in  dataset.take(1):
  print ('Input data: ', repr(''.join(idx2char[input_example.numpy()])))
  print ('Target data:', repr(''.join(idx2char[target_example.numpy()])))

for i, (input_idx, target_idx) in enumerate(zip(input_example[:5], target_example[:5])):
    print("Step {:4d}".format(i))
    print("  input: {} ({:s})".format(input_idx, repr(idx2char[input_idx])))
    print("  expected output: {} ({:s})".format(target_idx, repr(idx2char[target_idx])))

# Batch size
BATCH_SIZE = 64

# Buffer size to shuffle the dataset
# (TF data is designed to work with possibly infinite sequences,
# so it doesn't attempt to shuffle the entire sequence in memory. Instead,
# it maintains a buffer in which it shuffles elements).
BUFFER_SIZE = 10000

dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

dataset

# Length of the vocabulary in chars
vocab_size = len(vocab)

# The embedding dimension
embedding_dim = 256

# Number of RNN units
rnn_units = 1024

class Embedding:

  def __init__(self, vocab_size, embedding_dim):
    self._vocab_size = vocab_size
    self._embedding_dim = embedding_dim
    self._built = False

  def __call__(self, inputs):
    if not self._built:
      self.build(inputs)
    return tnp.take(self.weights, inputs, axis=0)

  def build(self, inputs):
    del inputs
    self.weights = tf.Variable(tnp.random.randn(
        self._vocab_size, self._embedding_dim).astype(np.float32))
    self._built = True


class GRUCell:
  """Builds a traditional GRU cell with dense internal transformations.

  Gated Recurrent Unit paper: https://arxiv.org/abs/1412.3555
  """

  def __init__(self, n_units, forget_bias=0.0):
    self._n_units = n_units
    self._forget_bias = forget_bias
    self._built = False

  def __call__(self, inputs):
    if not self._built:
      self.build(inputs)
    x, gru_state = inputs
    # Dense layer on the concatenation of x and h.
    y = tnp.dot(tnp.concatenate([x, gru_state], axis=-1), self.w1) + self.b1
    # Update and reset gates.
    u, r = tnp.split(tf.sigmoid(y), 2, axis=-1)
    # Candidate.
    c = tnp.dot(tnp.concatenate([x, r * gru_state], axis=-1), self.w2) + self.b2
    new_gru_state = u * gru_state + (1 - u) * tnp.tanh(c)
    return new_gru_state

  def build(self, inputs):
    # State last dimension must be n_units.
    assert inputs[1].shape[-1] == self._n_units
    # The dense layer input is the input and half of the GRU state.
    dense_shape = inputs[0].shape[-1] + self._n_units
    self.w1 = tf.Variable(tnp.random.uniform(
        -0.01, 0.01, (dense_shape, 2 * self._n_units)).astype(tnp.float32))
    self.b1 = tf.Variable((tnp.random.randn(2 * self._n_units) * 1e-6 + self._forget_bias
               ).astype(tnp.float32))
    self.w2 = tf.Variable(tnp.random.uniform(
        -0.01, 0.01, (dense_shape, self._n_units)).astype(tnp.float32))
    self.b2 = tf.Variable((tnp.random.randn(self._n_units) * 1e-6).astype(tnp.float32))
    self._built = True

  @property
  def weights(self):
    return (self.w1, self.b1, self.w2, self.b2)


class GRU:

  def __init__(self, n_units, forget_bias=0.0, stateful=False):
    self._cell = GRUCell(n_units, forget_bias)
    self._stateful = stateful
    self._built = False

  def __call__(self, inputs):
    if not self._built:
      self.build(inputs)
    if self._stateful:
      state = self.state.read_value()
    else:
      state = self._init_state(inputs.shape[0])    
    inputs = tnp.transpose(inputs, (1, 0, 2))
    output =  tf.scan(
        lambda gru_state, x: self._cell((x, gru_state)),
        inputs, state)
    if self._stateful:
      self.state.assign(output[-1, ...])
    return tnp.transpose(output, [1, 0, 2])

  def _init_state(self, batch_size):
    return tnp.zeros([batch_size, self._cell._n_units], tnp.float32)

  def reset_state(self):
    if not self._stateful:
      return
    self.state.assign(tf.zeros_like(self.state))

  def create_state(self, batch_size):
    self.state = tf.Variable(self._init_state(batch_size))

  def build(self, inputs):
    s = inputs.shape[0:1] + inputs.shape[2:]
    shapes = (s, s[:-1] + (self._cell._n_units,))   
    self._cell.build([tf.TensorSpec(x, tf.float32) for x in shapes])
    if self._stateful:
      self.create_state(inputs.shape[0])
    else:
      self.state = ()
    self._built = True
    
  @property
  def weights(self):
    return self._cell.weights


class Dense:

  def __init__(self, n_units, activation=None):
    self._n_units = n_units
    self._activation = activation
    self._built = False

  def __call__(self, inputs):
    if not self._built:
      self.build(inputs)
    y = tnp.dot(inputs, self.w) +self.b
    if self._activation != None:
      y = self._activation(y)
    return y

  def build(self, inputs):
    shape_w = (inputs.shape[-1], self._n_units)
    lim = tnp.sqrt(6.0 / (shape_w[0] + shape_w[1]))
    self.w = tf.Variable(tnp.random.uniform(-lim, lim, shape_w).astype(tnp.float32))
    self.b = tf.Variable((tnp.random.randn(self._n_units) * 1e-6).astype(tnp.float32))
    self._built = True

  @property
  def weights(self):
    return (self.w, self.b)


class Model:

  def __init__(self, vocab_size, embedding_dim, rnn_units, forget_bias=0.0, stateful=False, activation=None):
    self._embedding = Embedding(vocab_size, embedding_dim)
    self._gru = GRU(rnn_units, forget_bias=forget_bias, stateful=stateful)
    self._dense = Dense(vocab_size, activation=activation)
    self._layers = [self._embedding, self._gru, self._dense]
    self._built = False

  def __call__(self, inputs):
    if not self._built:
      self.build(inputs)
    xs = inputs
    for layer in self._layers:
      xs = layer(xs)
    return xs
    
  def build(self, inputs):
    self._embedding.build(inputs)
    self._gru.build(tf.TensorSpec(inputs.shape + (self._embedding._embedding_dim,), tf.float32))
    self._dense.build(tf.TensorSpec(inputs.shape + (self._gru._cell._n_units,), tf.float32))
    self._built = True

  @property
  def weights(self):
    return [layer.weights for layer in self._layers]

  @property
  def state(self):
    return self._gru.state

  def create_state(self, *args):
    self._gru.create_state(*args)

  def reset_state(self, *args):
    self._gru.reset_state(*args)


model = Model(
  vocab_size = vocab_size,
  embedding_dim=embedding_dim,
  rnn_units=rnn_units,
  stateful=True)

  for input_example_batch, target_example_batch in dataset.take(1):
    input_example_batch = tnp.asarray(input_example_batch)
    example_batch_predictions = model(input_example_batch)
    print(example_batch_predictions.shape, "# (batch_size, sequence_length, vocab_size)")

example_batch_predictions[0]

sampled_indices = tf.random.categorical(example_batch_predictions[0], num_samples=1)
sampled_indices = tf.squeeze(sampled_indices,axis=-1).numpy()

sampled_indices

print("Input: \n", repr("".join(idx2char[input_example_batch[0]])))
print()
print("Next Char Predictions: \n", repr("".join(idx2char[sampled_indices ])))

def one_hot(labels, n):
  return (labels[..., np.newaxis] == tnp.arange(n)).astype(np.float32)

def loss_fn(labels, predictions):
  predictions = tf.nn.log_softmax(predictions)
  return -tnp.sum(predictions * one_hot(tnp.asarray(labels), predictions.shape[-1]), axis=-1)

example_batch_loss  = loss_fn(target_example_batch, example_batch_predictions)
print("Prediction shape: ", example_batch_predictions.shape, " # (batch_size, sequence_length, vocab_size)")
print("scalar_loss:      ", tnp.mean(example_batch_loss))

class Adam:

  def __init__(self, learning_rate=0.001, b1=0.9, b2=0.999, eps=1e-7):
    self._lr = learning_rate
    self._b1 = b1
    self._b2 = b2
    self._eps = eps
    self._built = False

  def build(self, weights):
    self._m = tf.nest.map_structure(lambda x: tf.Variable(tnp.zeros_like(x)), weights)
    self._v = tf.nest.map_structure(lambda x: tf.Variable(tnp.zeros_like(x)), weights)
    self._step = tf.Variable(tnp.asarray(0, np.int64))
    self._built = True

  def _update(self, weights_var, grads, m_var, v_var):
    b1 = self._b1
    b2 = self._b2
    eps = self._eps
    step = tnp.asarray(self._step, np.float32)
    lr = self._lr
    weights = tnp.asarray(weights_var)
    m = tnp.asarray(m_var)
    v = tnp.asarray(v_var)
    m = (1 - b1) * grads + b1 * m  # First  moment estimate.
    v = (1 - b2) * (grads ** 2) + b2 * v  # Second moment estimate.
    mhat = m / (1 - b1 ** (step + 1))  # Bias correction.
    vhat = v / (1 - b2 ** (step + 1))   
    weights_var.assign_sub((lr * mhat / (tnp.sqrt(vhat) + eps)).astype(weights.dtype))
    m_var.assign(m)
    v_var.assign(v)

  def apply_gradients(self, weights, grads):
    if not self._built:
      self.build(weights)
    tf.nest.map_structure(lambda *args: self._update(*args), weights, grads, self._m, self._v)
    self._step.assign_add(1)

  @property
  def state(self):
    return (self._step, self._m, self._v)


optimizer = Adam()

@tf.function
def train_step(inp, target):
  with tf.GradientTape() as tape:
    # tape.watch(tf.nest.flatten(weights))
    predictions = model(inp)
    loss = tnp.mean(loss_fn(target, predictions))
  weights = model.weights
  grads = tape.gradient(loss, weights)
  optimizer.apply_gradients(weights, grads)
  return loss

# Training step
EPOCHS = 10

model.create_state(BATCH_SIZE)

for epoch in range(EPOCHS):
  start = time.time()

  # initializing the hidden state at the start of every epoch
  model.reset_state()

  for (batch_n, (inp, target)) in enumerate(dataset):
    loss = train_step(inp, target)

    if batch_n % 100 == 0:
      template = 'Epoch {} Batch {} Loss {}'
      print(template.format(epoch+1, batch_n, loss))

  print ('Epoch {} Loss {}'.format(epoch+1, loss))
  print ('Time taken for 1 epoch {} sec\n'.format(time.time() - start))

def generate_text(model, start_string):
  # Evaluation step (generating text using the learned model)

  # Number of characters to generate
  num_generate = 1000

  # Converting our start string to numbers (vectorizing)
  input_eval = [char2idx[s] for s in start_string]
  input_eval = tf.expand_dims(input_eval, 0)

  # Empty string to store our results
  text_generated = []

  # Low temperatures results in more predictable text.
  # Higher temperatures results in more surprising text.
  # Experiment to find the best setting.
  temperature = 1.0

  # Here batch size == 1
  model.create_state(1)
  for i in range(num_generate):
      predictions = model(input_eval)
      # remove the batch dimension
      predictions = tf.squeeze(predictions, 0)

      # using a categorical distribution to predict the character returned by the model
      predictions = predictions / temperature
      predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()

      # We pass the predicted character as the next input to the model
      # along with the previous hidden state
      input_eval = tf.expand_dims([predicted_id], 0)

      text_generated.append(idx2char[predicted_id])

  return (start_string + ''.join(text_generated))

print(generate_text(model, start_string=u"ROMEO: "))


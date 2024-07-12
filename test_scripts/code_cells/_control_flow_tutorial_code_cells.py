import tensorflow as tf

import traceback
import contextlib

# Some helper code to demonstrate the kinds of errors you might encounter.
@contextlib.contextmanager
def assert_raises(error_class):
  try:
    yield
  except error_class as e:
    print('Caught expected exception \n  {}:'.format(error_class))
    traceback.print_exc(limit=2)
  except Exception as e:
    raise e
  else:
    raise Exception('Expected {} to be raised but no error was raised!'.format(
        error_class))

def test_tf_cond(f, *args):
  g = f.get_concrete_function(*args).graph
  if any(node.name == 'cond' for node in g.as_graph_def().node):
    print("{}({}) uses tf.cond.".format(
        f.__name__, ', '.join(map(str, args))))
  else:
    print("{}({}) executes normally.".format(
        f.__name__, ', '.join(map(str, args))))

  print("  result: ",f(*args).numpy())

@tf.function
def dropout(x, training=True):
  if training:
    x = tf.nn.dropout(x, rate=0.5)
  return x

test_tf_cond(dropout, tf.ones([10], dtype=tf.float32), True)

test_tf_cond(dropout, tf.ones([10], dtype=tf.float32), tf.constant(True))

@tf.function
def f(x):
  if x > 0:
    x = x + 1.
    print("Tracing `then` branch")
  else:
    x = x - 1.
    print("Tracing `else` branch")
  return x

f(-1.0).numpy()

f(1.0).numpy()

f(tf.constant(1.0)).numpy()

@tf.function
def f():
  if tf.constant(True):
    x = tf.ones([3, 3])
  return x

# Throws an error because both branches need to define `x`.
with assert_raises(ValueError):
  f()

@tf.function
def f(x, y):
  if bool(x):
    y = y + 1.
    print("Tracing `then` branch")
  else:
    y = y - 1.
    print("Tracing `else` branch")
  return y

f(True, 0).numpy()

f(False, 0).numpy()

with assert_raises(TypeError):
  f(tf.constant(True), 0.0)

def test_dynamically_unrolled(f, *args):
  g = f.get_concrete_function(*args).graph
  if any(node.name == 'while' for node in g.as_graph_def().node):
    print("{}({}) uses tf.while_loop.".format(
        f.__name__, ', '.join(map(str, args))))
  elif any(node.name == 'ReduceDataset' for node in g.as_graph_def().node):
    print("{}({}) uses tf.data.Dataset.reduce.".format(
        f.__name__, ', '.join(map(str, args))))
  else:
    print("{}({}) gets unrolled.".format(
        f.__name__, ', '.join(map(str, args))))


@tf.function
def for_in_range():
  x = 0
  for i in range(5):
    x += i
  return x

test_dynamically_unrolled(for_in_range)

@tf.function
def for_in_tfrange():
  x = tf.constant(0, dtype=tf.int32)
  for i in tf.range(5):
    x += i
  return x

test_dynamically_unrolled(for_in_tfrange)

@tf.function
def for_in_tfdataset():
  x = tf.constant(0, dtype=tf.int64)
  for i in tf.data.Dataset.range(5):
    x += i
  return x

test_dynamically_unrolled(for_in_tfdataset)

@tf.function
def while_py_cond():
  x = 5
  while x > 0:
    x -= 1
  return x

test_dynamically_unrolled(while_py_cond)

@tf.function
def while_tf_cond():
  x = tf.constant(5)
  while x > 0:
    x -= 1
  return x

test_dynamically_unrolled(while_tf_cond)

@tf.function
def while_py_true_py_break(x):
  while True:  # py true
    if x == 0: # py break
      break
    x -= 1
  return x

test_dynamically_unrolled(while_py_true_py_break, 5)

@tf.function
def buggy_while_py_true_tf_break(x):
  while True:   # py true
    if tf.equal(x, 0): # tf break
      break
    x -= 1
  return x

with assert_raises(TypeError):
  test_dynamically_unrolled(buggy_while_py_true_tf_break, 5)

@tf.function
def while_tf_true_tf_break(x):
  while tf.constant(True): # tf true
    if x == 0:  # py break
      break
    x -= 1
  return x

test_dynamically_unrolled(while_tf_true_tf_break, 5)

@tf.function
def buggy_py_for_tf_break():
  x = 0
  for i in range(5):  # py for
    if tf.equal(i, 3): # tf break
      break
    x += i
  return x

with assert_raises(TypeError):
  test_dynamically_unrolled(buggy_py_for_tf_break)

@tf.function
def tf_for_py_break():
  x = 0
  for i in tf.range(5): # tf for
    if i == 3:  # py break
      break
    x += i
  return x

test_dynamically_unrolled(tf_for_py_break)

batch_size = 2
seq_len = 3
feature_size = 4

def rnn_step(inp, state):
  return inp + state

@tf.function
def dynamic_rnn(rnn_step, input_data, initial_state):
  # [batch, time, features] -> [time, batch, features]
  input_data = tf.transpose(input_data, [1, 0, 2])
  max_seq_len = input_data.shape[0]

  states = tf.TensorArray(tf.float32, size=max_seq_len)
  state = initial_state
  for i in tf.range(max_seq_len):
    state = rnn_step(input_data[i], state)
    states = states.write(i, state)
  return tf.transpose(states.stack(), [1, 0, 2])
  
dynamic_rnn(rnn_step,
            tf.random.uniform([batch_size, seq_len, feature_size]),
            tf.zeros([batch_size, feature_size]))

@tf.function
def buggy_loop_var_uninitialized():
  for i in tf.range(3):
    x = i
  return x

with assert_raises(ValueError):
  buggy_loop_var_uninitialized()

@tf.function
def f():
  x = tf.constant(0)
  for i in tf.range(3):
    x = i
  return x

f()

@tf.function
def buggy_loop_type_changes():
  x = tf.constant(0, dtype=tf.float32)
  for i in tf.range(3): # Yields tensors of type tf.int32...
    x = i
  return x

with assert_raises(TypeError):
  buggy_loop_type_changes()

@tf.function
def buggy_concat():
  x = tf.ones([0, 10])
  for i in tf.range(5):
    x = tf.concat([x, tf.ones([1, 10])], axis=0)
  return x

with assert_raises(ValueError):
  buggy_concat()

@tf.function
def concat_with_padding():
  x = tf.zeros([5, 10])
  for i in tf.range(5):
    x = tf.concat([x[:i], tf.ones([1, 10]), tf.zeros([4-i, 10])], axis=0)
    x.set_shape([5, 10])
  return x

concat_with_padding()



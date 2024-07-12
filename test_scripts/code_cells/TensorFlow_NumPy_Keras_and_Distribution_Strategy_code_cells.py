!pip install --quiet --upgrade tf-nightly

import tensorflow as tf
import tensorflow.experimental.numpy as tnp

# Creates 3 logical GPU devices for demonstrating distribution.
gpu_device = tf.config.list_physical_devices("GPU")[0]
tf.config.set_logical_device_configuration(
    gpu_device, [tf.config.LogicalDeviceConfiguration(128)] * 3)


dense_layer = tf.keras.layers.Dense(5)
inputs = tnp.random.randn(2, 3).astype(tnp.float32)
outputs = dense_layer(inputs)
print("Shape:", outputs.shape)
print("Class:", outputs.__class__)

class ProjectionLayer(tf.keras.layers.Layer):
  """Linear projection layer using TF NumPy."""

  def __init__(self, units):
    super(ProjectionLayer, self).__init__()
    self._units = units

  def build(self, input_shape):
    stddev = tnp.sqrt(self._units).astype(tnp.float32)
    initial_value = tnp.random.randn(input_shape[1], self._units).astype(
        tnp.float32) / stddev
    # Note that TF NumPy can interoperate with tf.Variable.
    self.w = tf.Variable(initial_value, trainable=True)

  def call(self, inputs):
    return tnp.matmul(inputs, self.w)

# Call with ndarray inputs
layer = ProjectionLayer(2)
tnp_inputs = tnp.random.randn(2, 4).astype(tnp.float32)
print("output:", layer(tnp_inputs))

# Call with tf.Tensor inputs
tf_inputs = tf.random.uniform([2, 4])
print("\noutput: ", layer(tf_inputs))

batch_size = 3
units = 5
model = tf.keras.Sequential([tf.keras.layers.Dense(units),
                             ProjectionLayer(2)])

print("Calling with ND Array inputs")
tnp_inputs = tnp.random.randn(batch_size, units).astype(tnp.float32)
output = model.call(tnp_inputs)
print("Output shape %s.\nOutput class: %s\n" % (output.shape, output.__class__))

print("Calling with tensor inputs")
tf_inputs = tf.convert_to_tensor(tnp_inputs)
output = model.call(tf_inputs)
print("Output shape %s.\nOutput class: %s" % (output.shape, output.__class__))


# Initialize the strategy
gpus = tf.config.list_logical_devices("GPU")
print("Using following GPUs", gpus)

strategy = tf.distribute.MirroredStrategy(gpus)

@tf.function
def replica_fn():
  replica_id = tf.distribute.get_replica_context().replica_id_in_sync_group
  print("Running on device %s" % replica_id.device)
  return tnp.asarray(replica_id) * 5

print(strategy.run(replica_fn).values)

# Test running the model in a distributed setting.
model = tf.keras.Sequential([tf.keras.layers.Dense(units), ProjectionLayer(2)])

@tf.function
def model_replica_fn():
  inputs = tnp.random.randn(batch_size, units).astype(tnp.float32)
  return model.call(inputs)

print("Outputs:\n", strategy.run(model_replica_fn).values)


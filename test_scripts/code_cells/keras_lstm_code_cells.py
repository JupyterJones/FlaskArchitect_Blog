!pip install tf-nightly --upgrade

import numpy as np
import tensorflow as tf

model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(28, 28), name='input'),
    tf.keras.layers.LSTM(20),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax, name='output')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.summary()

# Load MNIST dataset.
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
x_train = x_train.astype(np.float32)
x_test = x_test.astype(np.float32)

# Change this to True if you want to test the flow rapidly.
# Train with a small dataset and only 1 epoch. The model will work poorly
# but this provides a fast way to test if the conversion works end to end.
_FAST_TRAINING = False
_EPOCHS = 5
if _FAST_TRAINING:
  _EPOCHS = 1
  _TRAINING_DATA_COUNT = 1000
  x_train = x_train[:_TRAINING_DATA_COUNT]
  y_train = y_train[:_TRAINING_DATA_COUNT]

model.fit(x_train, y_train, epochs=_EPOCHS)
model.evaluate(x_test, y_test, verbose=0)


converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Run the model with TensorFlow to get expected results.
expected = model.predict(x_test[0:1])

# Run the model with TensorFlow Lite
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
interpreter.set_tensor(input_details[0]["index"], x_test[0:1, :, :])
interpreter.invoke()
result = interpreter.get_tensor(output_details[0]["index"])

# Assert if the result of TFLite model is consistent with the TF model.
np.testing.assert_almost_equal(expected, result)
print("Done. The result of TensorFlow matches the result of TensorFlow Lite.")




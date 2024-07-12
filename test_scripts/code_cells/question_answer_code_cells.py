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

!sudo apt -y install libportaudio2
!pip install -q tflite-model-maker-nightly

import numpy as np
import os

import tensorflow as tf
assert tf.__version__.startswith('2')

from tflite_model_maker import model_spec
from tflite_model_maker import question_answer
from tflite_model_maker.config import ExportFormat
from tflite_model_maker.question_answer import DataLoader

spec = model_spec.get('mobilebert_qa_squad')

train_data_path = tf.keras.utils.get_file(
    fname='triviaqa-web-train-8000.json',
    origin='https://storage.googleapis.com/download.tensorflow.org/models/tflite/dataset/triviaqa-web-train-8000.json')
validation_data_path = tf.keras.utils.get_file(
    fname='triviaqa-verified-web-dev.json',
    origin='https://storage.googleapis.com/download.tensorflow.org/models/tflite/dataset/triviaqa-verified-web-dev.json')

train_data = DataLoader.from_squad(train_data_path, spec, is_training=True)
validation_data = DataLoader.from_squad(validation_data_path, spec, is_training=False)

model = question_answer.create(train_data, model_spec=spec)

model.summary()

model.evaluate(validation_data)

model.export(export_dir='.')

model.export(export_dir='.', export_format=ExportFormat.VOCAB)

model.evaluate_tflite('model.tflite', validation_data)

new_spec = model_spec.get('mobilebert_qa')
new_spec.seq_len = 512


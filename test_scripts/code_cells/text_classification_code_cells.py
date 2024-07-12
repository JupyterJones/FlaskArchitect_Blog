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

from tflite_model_maker import model_spec
from tflite_model_maker import text_classifier
from tflite_model_maker.config import ExportFormat
from tflite_model_maker.text_classifier import AverageWordVecSpec
from tflite_model_maker.text_classifier import DataLoader

import tensorflow as tf
assert tf.__version__.startswith('2')
tf.get_logger().setLevel('ERROR')

data_dir = tf.keras.utils.get_file(
      fname='SST-2.zip',
      origin='https://dl.fbaipublicfiles.com/glue/data/SST-2.zip',
      extract=True)
data_dir = os.path.join(os.path.dirname(data_dir), 'SST-2')

import pandas as pd

def replace_label(original_file, new_file):
  # Load the original file to pandas. We need to specify the separator as
  # '\t' as the training data is stored in TSV format
  df = pd.read_csv(original_file, sep='\t')

  # Define how we want to change the label name
  label_map = {0: 'negative', 1: 'positive'}

  # Excute the label change
  df.replace({'label': label_map}, inplace=True)

  # Write the updated dataset to a new file
  df.to_csv(new_file)

# Replace the label name for both the training and test dataset. Then write the
# updated CSV dataset to the current folder.
replace_label(os.path.join(os.path.join(data_dir, 'train.tsv')), 'train.csv')
replace_label(os.path.join(os.path.join(data_dir, 'dev.tsv')), 'dev.csv')

spec = model_spec.get('average_word_vec')

train_data = DataLoader.from_csv(
      filename='train.csv',
      text_column='sentence',
      label_column='label',
      model_spec=spec,
      is_training=True)
test_data = DataLoader.from_csv(
      filename='dev.csv',
      text_column='sentence',
      label_column='label',
      model_spec=spec,
      is_training=False)

model = text_classifier.create(train_data, model_spec=spec, epochs=10)

loss, acc = model.evaluate(test_data)

model.export(export_dir='average_word_vec')

mb_spec = model_spec.get('mobilebert_classifier')

train_data = DataLoader.from_csv(
      filename='train.csv',
      text_column='sentence',
      label_column='label',
      model_spec=mb_spec,
      is_training=True)
test_data = DataLoader.from_csv(
      filename='dev.csv',
      text_column='sentence',
      label_column='label',
      model_spec=mb_spec,
      is_training=False)

model = text_classifier.create(train_data, model_spec=mb_spec, epochs=3)

model.summary()

loss, acc = model.evaluate(test_data)

model.export(export_dir='mobilebert/')

model.export(export_dir='mobilebert/', export_format=[ExportFormat.LABEL, ExportFormat.VOCAB])

accuracy = model.evaluate_tflite('mobilebert/model.tflite', test_data)
print('TFLite model accuracy: ', accuracy)

new_model_spec = model_spec.get('mobilebert_classifier')
new_model_spec.seq_len = 256

new_model_spec = AverageWordVecSpec(wordvec_dim=32)

new_train_data = DataLoader.from_csv(
      filename='train.csv',
      text_column='sentence',
      label_column='label',
      model_spec=new_model_spec,
      is_training=True)

model = text_classifier.create(new_train_data, model_spec=new_model_spec)

model = text_classifier.create(new_train_data, model_spec=new_model_spec, epochs=20)

new_test_data = DataLoader.from_csv(
      filename='dev.csv',
      text_column='sentence',
      label_column='label',
      model_spec=new_model_spec,
      is_training=False)

loss, accuracy = model.evaluate(new_test_data)

spec = model_spec.get('bert_classifier')


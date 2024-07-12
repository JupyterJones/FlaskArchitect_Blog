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
!pip install -q tflite-model-maker
!pip install gdown

from tflite_model_maker import searcher

!gdown https://drive.google.com/uc?id=0BwmD_VLjROrfTHk4NFg2SndKcjQ
!gdown https://drive.google.com/uc?id=0BwmD_VLjROrfM1BxdkxVaTY2bWs

!wget -O all_train.txt https://raw.githubusercontent.com/abisee/cnn-dailymail/master/url_lists/all_train.txt
!tar xzf cnn_stories.tgz
!tar xzf dailymail_stories.tgz

#@title Save the highlights and urls to the CSV file
#@markdown Load the highlights from the stories of CNN / Daily Mail, map urls with highlights, and save them to the CSV file.

CNN_FRACTION = 0.05 #@param {type:"number"}
DAILYMAIL_FRACTION = 0.05 #@param {type:"number"}

import csv
import hashlib
import os
import tensorflow as tf

dm_single_close_quote = u"\u2019"  # unicode
dm_double_close_quote = u"\u201d"
END_TOKENS = [
    ".", "!", "?", "...", "'", "`", '"', dm_single_close_quote,
    dm_double_close_quote, ")"
]  # acceptable ways to end a sentence


def read_file(file_path):
  """Reads lines in the file."""
  lines = []
  with tf.io.gfile.GFile(file_path, "r") as f:
    for line in f:
      lines.append(line.strip())
  return lines


def url_hash(url):
  """Gets the hash value of the url."""
  h = hashlib.sha1()
  url = url.encode("utf-8")
  h.update(url)
  return h.hexdigest()


def get_url_hashes_dict(urls_path):
  """Gets hashes dict that maps the hash value to the original url in file."""
  urls = read_file(urls_path)
  return {url_hash(url): url[url.find("id_/") + 4:] for url in urls}


def find_files(folder, url_dict):
  """Finds files corresponding to the urls in the folder."""
  all_files = tf.io.gfile.listdir(folder)
  ret_files = []
  for file in all_files:
    # Gets the file name without extension.
    filename = os.path.splitext(os.path.basename(file))[0]
    if filename in url_dict:
      ret_files.append(os.path.join(folder, file))
  return ret_files


def fix_missing_period(line):
  """Adds a period to a line that is missing a period."""
  if "@highlight" in line:
    return line
  if not line:
    return line
  if line[-1] in END_TOKENS:
    return line
  return line + "."


def get_highlights(story_file):
  """Gets highlights from a story file path."""
  lines = read_file(story_file)

  # Put periods on the ends of lines that are missing them
  # (this is a problem in the dataset because many image captions don't end in
  # periods; consequently they end up in the body of the article as run-on
  # sentences)
  lines = [fix_missing_period(line) for line in lines]

  # Separate out article and abstract sentences
  highlight_list = []
  next_is_highlight = False
  for line in lines:
    if not line:
      continue  # empty line
    elif line.startswith("@highlight"):
      next_is_highlight = True
    elif next_is_highlight:
      highlight_list.append(line)

  # Make highlights into a single string.
  highlights = "\n".join(highlight_list)

  return highlights

url_hashes_dict = get_url_hashes_dict("all_train.txt")
cnn_files = find_files("cnn/stories", url_hashes_dict)
dailymail_files = find_files("dailymail/stories", url_hashes_dict)

# The size to be selected.
cnn_size = int(CNN_FRACTION * len(cnn_files))
dailymail_size = int(DAILYMAIL_FRACTION * len(dailymail_files))
print("CNN size: %d"%cnn_size)
print("Daily Mail size: %d"%dailymail_size)

with open("cnn_dailymail.csv", "w") as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=["highlights", "urls"])
  writer.writeheader()

  for file in cnn_files[:cnn_size] + dailymail_files[:dailymail_size]:
    highlights = get_highlights(file)
    # Gets the filename which is the hash value of the url.
    filename = os.path.splitext(os.path.basename(file))[0]
    url = url_hashes_dict[filename]
    writer.writerow({"highlights": highlights, "urls": url})


!wget -O universal_sentence_encoder.tflite https://storage.googleapis.com/download.tensorflow.org/models/tflite_support/searcher/text_to_image_blogpost/text_embedder.tflite

data_loader = searcher.TextDataLoader.create("universal_sentence_encoder.tflite", l2_normalize=True)
data_loader.load_from_csv("cnn_dailymail.csv", text_column="highlights", metadata_column="urls")

scann_options = searcher.ScaNNOptions(
      distance_measure="dot_product",
      tree=searcher.Tree(num_leaves=140, num_leaves_to_search=4),
      score_ah=searcher.ScoreAH(dimensions_per_block=1, anisotropic_quantization_threshold=0.2))
model = searcher.Searcher.create_from_data(data_loader, scann_options)

model.export(
      export_filename="searcher.tflite",
      userinfo="",
      export_format=searcher.ExportFormat.TFLITE)

from tflite_support.task import text

# Initializes a TextSearcher object.
searcher = text.TextSearcher.create_from_file("searcher.tflite")

# Searches the input query.
results = searcher.search("The Airline Quality Rankings Report looks at the 14 largest U.S. airlines.")
print(results)


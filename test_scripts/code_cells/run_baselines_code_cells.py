# Clone the conversational datasets repository.
!git clone https://github.com/PolyAI-LDN/conversational-datasets.git

import os
from getpass import getpass

# We use a consistent random sample of the train and test sets for the
# baselines.
# Please ask matthen@gmail.com for the URL, and enter it here.
# (You could also generate your own random sample, and exact results may vary
# slightly).
os.environ['DATA_URL'] = getpass("Enter URL: ")

# Download and extract the data.
!mkdir -p conversational-datasets/data
!wget -q "${DATA_URL}" -O conversational-datasets/data/data.zip
!cd conversational-datasets/data && unzip -o data.zip

# Install extra pip dependencies.
!pip install bert-tensorflow glog tf-sentencepiece
%env  TFHUB_CACHE_DIR=/content/tfhub
%env  PYTHONPATH=/content/conversational-datasets

# Run all the baselines.
# It will take over an hour.
!cd conversational-datasets && ./baselines/run_baselines.sh
!cat conversational-datasets/baselines/results.csv

# Run just a single baseline:
! cd conversational-datasets && python baselines/run_baseline.py \
    --method USE_QA_SIM \
    --train_dataset data/amazon-train-sampled \
    --test_dataset data/amazon-test-sampled


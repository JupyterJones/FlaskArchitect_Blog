!pip install -q deeppavlov

# %load https://raw.githubusercontent.com/deepmipt/DeepPavlov/master/deeppavlov/configs/faq/tfidf_logreg_en_faq.json
{
  "dataset_reader": {
    "class_name": "faq_reader",
    "x_col_name": "Question",
    "y_col_name": "Answer",
    "data_url": "http://files.deeppavlov.ai/faq/school/faq_school_en.csv"
  },
  "dataset_iterator": {
    "class_name": "data_learning_iterator"
  },
  "chainer": {
    "in": "q",
    "in_y": "y",
    "pipe": [
      {
        "class_name": "stream_spacy_tokenizer",
        "in": "q",
        "id": "my_tokenizer",
        "lemmas": true,
        "out": "q_token_lemmas"
      },
      {
        "ref": "my_tokenizer",
        "in": "q_token_lemmas",
        "out": "q_lem"
      },
      {
        "in": [
          "q_lem"
        ],
        "out": [
          "q_vect"
        ],
        "fit_on": [
          "q_lem"
        ],
        "id": "tfidf_vec",
        "class_name": "sklearn_component",
        "save_path": "{MODELS_PATH}/faq/mipt/en_mipt_faq_v4/tfidf.pkl",
        "load_path": "{MODELS_PATH}/faq/mipt/en_mipt_faq_v4/tfidf.pkl",
        "model_class": "sklearn.feature_extraction.text:TfidfVectorizer",
        "infer_method": "transform"
      },
      {
        "id": "answers_vocab",
        "class_name": "simple_vocab",
        "fit_on": [
          "y"
        ],
        "save_path": "{MODELS_PATH}/faq/mipt/en_mipt_faq_v4/en_mipt_answers.dict",
        "load_path": "{MODELS_PATH}/faq/mipt/en_mipt_faq_v4/en_mipt_answers.dict",
        "in": "y",
        "out": "y_ids"
      },
      {
        "in": "q_vect",
        "fit_on": [
          "q_vect",
          "y_ids"
        ],
        "out": [
          "y_pred_proba"
        ],
        "class_name": "sklearn_component",
        "main": true,
        "save_path": "{MODELS_PATH}/faq/mipt/en_mipt_faq_v4/logreg.pkl",
        "load_path": "{MODELS_PATH}/faq/mipt/en_mipt_faq_v4/logreg.pkl",
        "model_class": "sklearn.linear_model:LogisticRegression",
        "infer_method": "predict_proba",
        "C": 1000,
        "penalty": "l2"
      },
      {
        "in": "y_pred_proba",
        "out": "y_pred_ids",
        "class_name": "proba2labels",
        "max_proba": true
      },
      {
        "in": "y_pred_ids",
        "out": "y_pred_answers",
        "ref": "answers_vocab"
      }
    ],
    "out": [
      "y_pred_answers",
      "y_pred_proba"
    ]
  },
  "train": {
    "evaluation_targets": [],
    "class_name": "fit_trainer"
  },
  "metadata": {
    "variables": {
      "ROOT_PATH": "~/.deeppavlov",
      "DOWNLOADS_PATH": "{ROOT_PATH}/downloads",
      "MODELS_PATH": "{ROOT_PATH}/models"
    },
    "download": [
      {
        "url": "http://files.deeppavlov.ai/faq/mipt/en_mipt_faq_v4.tar.gz",
        "subdir": "{MODELS_PATH}/faq/mipt"
      }
    ]
  }
}


!python -m deeppavlov install tfidf_logreg_en_faq

!python -m deeppavlov interact tfidf_logreg_en_faq -d

from deeppavlov import configs
from deeppavlov.core.common.file import read_json
from deeppavlov.core.commands.infer import build_model

faq = build_model(configs.faq.tfidf_logreg_en_faq, download = True)
a = faq(["I need help"])
a

!python -m deeppavlov train tfidf_logreg_en_faq

%%bash
wget -q http://files.deeppavlov.ai/faq/school/faq_school_en.csv -O faq.csv
echo "What's DeepPavlov?, DeepPavlov is an open-source conversational AI library" >> faq.csv

from deeppavlov import configs, train_model

model_config = read_json(configs.faq.tfidf_logreg_en_faq)
model_config["dataset_reader"]["data_path"] = "/content/faq.csv"
model_config["dataset_reader"]["data_url"] = None
faq = train_model(model_config)
a = faq(["tell me about DeepPavlov"])
a


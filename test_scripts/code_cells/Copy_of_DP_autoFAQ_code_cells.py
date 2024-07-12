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

!ls

%%bash
wget -q http://files.deeppavlov.ai/faq/school/faq_school_en.csv -O faq.csv
echo "What's DeepPavlov?, DeepPavlov is an open-source conversational AI library" >> faq.csv

from deeppavlov import configs, train_model

model_config = read_json(configs.faq.tfidf_logreg_en_faq)
model_config["dataset_reader"]["data_path"] = "faq.csv"
model_config["dataset_reader"]["data_url"] = None
faq = train_model(model_config)
a = faq(["tell me about DeepPavlov"])
a

a = faq(["What if I fail an exam?"])
a

!ls

# %load faq.csv
Question,Answer
What is the preparatory course?,"The preparatory course is a special educational program lasting one academic year — that is, between seven and 10 months. Students taking this course study Russian, mathematics, and physics. The course ends with an exam, and the passing students receive a certificate of completion."
I am interested in the preparatory course.,"The preparatory course is a special educational program lasting one academic year — that is, between seven and 10 months. Students taking this course study Russian, mathematics, and physics. The course ends with an exam, and the passing students receive a certificate of completion."
Do you have a preparatory course?,"The preparatory course is a special educational program lasting one academic year — that is, between seven and 10 months. Students taking this course study Russian, mathematics, and physics. The course ends with an exam, and the passing students receive a certificate of completion."
What is an invitation letter?,An invitation is an official document prepared by the Ministry of Internal Affairs of the Russian Federation. It confirms that the student to whom the invitation is addressed has been admitted to the university. The invitation contains the student’s passport data and specifies the full designation of the university. This document needs to be submitted to the Russian Embassy in order to receive a visa. The internal affairs ministry usually issues the invitation letter within 45 days.
How can I get a visa from the Russian Embassy?,An invitation is an official document prepared by the Ministry of Internal Affairs of the Russian Federation. It confirms that the student to whom the invitation is addressed has been admitted to the university. The invitation contains the student’s passport data and specifies the full designation of the university. This document needs to be submitted to the Russian Embassy in order to receive a visa. The internal affairs ministry usually issues the invitation letter within 45 days.
How long does it take to issue an invitation letter?,An invitation is an official document prepared by the Ministry of Internal Affairs of the Russian Federation. It confirms that the student to whom the invitation is addressed has been admitted to the university. The invitation contains the student’s passport data and specifies the full designation of the university. This document needs to be submitted to the Russian Embassy in order to receive a visa. The internal affairs ministry usually issues the invitation letter within 45 days.
Where should I submit the invitation letter?,An invitation is an official document prepared by the Ministry of Internal Affairs of the Russian Federation. It confirms that the student to whom the invitation is addressed has been admitted to the university. The invitation contains the student’s passport data and specifies the full designation of the university. This document needs to be submitted to the Russian Embassy in order to receive a visa. The internal affairs ministry usually issues the invitation letter within 45 days.
What does registration mean?,"Registration grants a foreign citizen the legal right to stay on the territory of Russia. It is usually provided for a period of one year and needs to be renewed annually. To prolong your registration, submit an application about three weeks before it expires. Upon arrival at the university, a student needs to register at the International Department of MIPT within three days, including the day of arrival. The registration stamp is put on the migration card. It is recommended that the passport be renewed before a trip to Russia for the full period of study."
Where can I get registration?,"Registration grants a foreign citizen the legal right to stay on the territory of Russia. It is usually provided for a period of one year and needs to be renewed annually. To prolong your registration, submit an application about three weeks before it expires. Upon arrival at the university, a student needs to register at the International Department of MIPT within three days, including the day of arrival. The registration stamp is put on the migration card. It is recommended that the passport be renewed before a trip to Russia for the full period of study."
For how long can I get registration?,"Registration grants a foreign citizen the legal right to stay on the territory of Russia. It is usually provided for a period of one year and needs to be renewed annually. To prolong your registration, submit an application about three weeks before it expires. Upon arrival at the university, a student needs to register at the International Department of MIPT within three days, including the day of arrival. The registration stamp is put on the migration card. It is recommended that the passport be renewed before a trip to Russia for the full period of study."
How to prolong registration?,"Registration grants a foreign citizen the legal right to stay on the territory of Russia. It is usually provided for a period of one year and needs to be renewed annually. To prolong your registration, submit an application about three weeks before it expires. Upon arrival at the university, a student needs to register at the International Department of MIPT within three days, including the day of arrival. The registration stamp is put on the migration card. It is recommended that the passport be renewed before a trip to Russia for the full period of study."
Is it possible to study and work at the same time?,"Students at Russian universities are required to attend all lectures as only the knowledge gained during classroom instruction enables one to become a skilled and knowledgeable professional. This means that side job opportunities are limited to working after classes, on weekends, or during vacations. However, even that should probably be reserved for when you have gotten to know the country and the language better. Usually, it is during the junior year that getting a job really becomes an option, but only if you study well and attend all mandatory classes."
Do you permit work during studies?,"Students at Russian universities are required to attend all lectures as only the knowledge gained during classroom instruction enables one to become a skilled and knowledgeable professional. This means that side job opportunities are limited to working after classes, on weekends, or during vacations. However, even that should probably be reserved for when you have gotten to know the country and the language better. Usually, it is during the junior year that getting a job really becomes an option, but only if you study well and attend all mandatory classes."
Can I combine study and work?,"Students at Russian universities are required to attend all lectures as only the knowledge gained during classroom instruction enables one to become a skilled and knowledgeable professional. This means that side job opportunities are limited to working after classes, on weekends, or during vacations. However, even that should probably be reserved for when you have gotten to know the country and the language better. Usually, it is during the junior year that getting a job really becomes an option, but only if you study well and attend all mandatory classes."
Do I have to attend all lectures?,"Students at Russian universities are required to attend all lectures as only the knowledge gained during classroom instruction enables one to become a skilled and knowledgeable professional. This means that side job opportunities are limited to working after classes, on weekends, or during vacations. However, even that should probably be reserved for when you have gotten to know the country and the language better. Usually, it is during the junior year that getting a job really becomes an option, but only if you study well and attend all mandatory classes."
How long does the academic year last?,"The academic year lasts 10 months — from Sept. 1 to June 30 — and consists of two semesters. The first semester begins Sept. 1 and ends Jan. 25, and the second is between Feb. 9 and June 30. Between the semesters, the students are on vacations. The brief winter break lasts two weeks, from Jan. 25 to Feb. 9, and the summer vacations are two months long, from July 1 to Aug. 30. During that time, some students stay in Russia, while others go back home to spend time with their families."
Where can I find the academic calendar?,"The academic year lasts 10 months — from Sept. 1 to June 30 — and consists of two semesters. The first semester begins Sept. 1 and ends Jan. 25, and the second is between Feb. 9 and June 30. Between the semesters, the students are on vacations. The brief winter break lasts two weeks, from Jan. 25 to Feb. 9, and the summer vacations are two months long, from July 1 to Aug. 30. During that time, some students stay in Russia, while others go back home to spend time with their families."
Do you have a vacation between semesters?,"The academic year lasts 10 months — from Sept. 1 to June 30 — and consists of two semesters. The first semester begins Sept. 1 and ends Jan. 25, and the second is between Feb. 9 and June 30. Between the semesters, the students are on vacations. The brief winter break lasts two weeks, from Jan. 25 to Feb. 9, and the summer vacations are two months long, from July 1 to Aug. 30. During that time, some students stay in Russia, while others go back home to spend time with their families."
How many semesters are there?,"The academic year lasts 10 months — from Sept. 1 to June 30 — and consists of two semesters. The first semester begins Sept. 1 and ends Jan. 25, and the second is between Feb. 9 and June 30. Between the semesters, the students are on vacations. The brief winter break lasts two weeks, from Jan. 25 to Feb. 9, and the summer vacations are two months long, from July 1 to Aug. 30. During that time, some students stay in Russia, while others go back home to spend time with their families."
How long does the summer vacation last?,"The academic year lasts 10 months — from Sept. 1 to June 30 — and consists of two semesters. The first semester begins Sept. 1 and ends Jan. 25, and the second is between Feb. 9 and June 30. Between the semesters, the students are on vacations. The brief winter break lasts two weeks, from Jan. 25 to Feb. 9, and the summer vacations are two months long, from July 1 to Aug. 30. During that time, some students stay in Russia, while others go back home to spend time with their families."
What documents are required for admission?,"The papers you need are: passport, documents certifying prior education (with transcripts), medical certificate confirming your good health. The submitted documents have to be translated into Russian."
Should I translate the submitted documents into Russian?,"The papers you need are: passport, documents certifying prior education (with transcripts), medical certificate confirming your good health. The submitted documents have to be translated into Russian."
Do I need to attach a transcript of prior education to the submitted documents?,"The papers you need are: passport, documents certifying prior education (with transcripts), medical certificate confirming your good health. The submitted documents have to be translated into Russian."
What are the tuition fees?,"A program taught in Russian will cost you 250,000 rubles per year. The fees on English-taught programs are higher, at 400,000 rubles per year."
How much should I pay for English-taught programs?,"A program taught in Russian will cost you 250,000 rubles per year. The fees on English-taught programs are higher, at 400,000 rubles per year."
How expensive is it to study in Russian?,"A program taught in Russian will cost you 250,000 rubles per year. The fees on English-taught programs are higher, at 400,000 rubles per year."
Should I insure my life?,"Life and health insurance are obligatory for any foreign citizen arriving in Russia to study. The cost of life and health insurance is 8,200 rubles per year. A student needs to carry the insurance policy specifying the phone number of the insurance company and the emergency health service at all times. All Russian universities have medical offices for first aid and general medical care."
What if I need first aid or general medical care?,"All Russian universities have medical offices for first aid and general medical care."
What’s the cost of life insurance?,"Life and health insurance are obligatory for any foreign citizen arriving in Russia to study. The cost of life and health insurance is 8,200 rubles per year. A student needs to carry the insurance policy specifying the phone number of the insurance company and the emergency health service at all times. All Russian universities have medical offices for first aid and general medical care."
Do you have a medical office in the university?,"All Russian universities have medical offices for first aid and general medical care."
Is life insurance obligatory?,"Life and health insurance are obligatory for any foreign citizen arriving in Russia to study. The cost of life and health insurance is 8,200 rubles per year. A student needs to carry the insurance policy specifying the phone number of the insurance company and the emergency health service at all times. All Russian universities have medical offices for first aid and general medical care."
In which cases can a student be expelled from the university?,"You can be expelled from the university: of your own free will, for health reasons, for poor academic progress. In the latter case, the grounds for expelling a student are: not passing the exams in multiple subjects in the allotted time at the end of a semester, repeatedly failing an exam or not turning up for it in the designated time, failing an exam in front of the board of examiners, which usually convenes after three failed attempts, violating rules of conduct or other regulations."
How many failing attempts are permitted on exams?,"You can be expelled from the university: of your own free will, for health reasons, for poor academic progress. In the latter case, the grounds for expelling a student are: not passing the exams in multiple subjects in the allotted time at the end of a semester, repeatedly failing an exam or not turning up for it in the designated time, failing an exam in front of the board of examiners, which usually convenes after three failed attempts, violating rules of conduct or other regulations."
How to get a bank card?,Visit the social service on the second floor of the building housing the dining hall. The social service is next to local internal affairs office.
Where can I get a bank card?,Visit the social service on the second floor of the building housing the dining hall. The social service is next to local internal affairs office.
How to get a social card?,"To issue a social card, you need to visit a multifunctional center in Moscow. Fill in the application provided at the multifunctional center. You need to have a notarized copy of your passport and your student ID with you. The latter refers to the credential you use daily to gain access to university buildings."
Where can I get a social card?,"To issue a social card, you need to visit a multifunctional center in Moscow. Fill in the application provided at the multifunctional center. You need to have a notarized copy of your passport and your student ID with you. The latter refers to the credential you use daily to gain access to university buildings."
Do I need a social card?,"To issue a social card, you need to visit a multifunctional center in Moscow. Fill in the application provided at the multifunctional center. You need to have a notarized copy of your passport and your student ID with you. The latter refers to the credential you use daily to gain access to university buildings."
What if I have a problem or other questions?,"If you have any further inquiries, you can address them to the International Students Office, which is located in the Auditorium Building, Room 315. The phone number is (7-495) 408-7043."
I need assistance.,"If you have any further inquiries, you can address them to the International Students Office, which is located in the Auditorium Building, Room 315. The phone number is (7-495) 408-7043."
I need help.,"If you have any further inquiries, you can address them to the International Students Office, which is located in the Auditorium Building, Room 315. The phone number is (7-495) 408-7043."
Can you help me?,"If you have any further inquiries, you can address them to the International Students Office, which is located in the Auditorium Building, Room 315. The phone number is (7-495) 408-7043."
What's DeepPavlov?, DeepPavlov is an open-source conversational AI library


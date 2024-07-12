!ls chatterbot-corpus/chatterbot_corpus/data/english

# Title_Maker 
# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import logging

# Comment out the following line to disable verbose logging
logging.basicConfig(level=logging.INFO)

def coptitle(coptit):
    copt = open(coptit+".corpus.json","w")
    copbrac ="{"
    copsp = "\n    \""
    copclo = "\": ["
    copt.write(copbrac+copsp+coptit+copclo)
    copt.close()
coptit = raw_input('title')
coptitle(coptit)
       

# Copra_Maker
# -*- coding: utf-8 -*-
from chatterbot import ChatBot

import logging

# Comment out the following line to disable verbose logging
logging.basicConfig(level=logging.INFO)

speak = raw_input('speak')
respond = raw_input('respond')
space = "            \""
txtstart = "        ["
txtspace = "            "
txtend = "        ],"

def copraIn():

    cop = open("tagalog.corpus.json","a")
    #cop.write("\n"+ txspace + "\""+txtstart + speak + "\"\n" + txspace + "\""+respond+"\"" + "\n" + txtend)
    cop.write("\n"+txtstart+"\n"+space+speak+"\""+txtspace+"\n"+space+respond+"\"\n"+txtend)
    cop.close()

    

copraIn()

%%writefile tagalog.corpus.json
{
    "tagalog": [
        [
            "Good evening!",            
            "Magandang Gabi!"
        ],
        [
            "How are you?",            
            "Mabuti naman,Salamat!"
        ],
        [
            "Mabuti naman,Salamat!",            
            "At ikaw? "
        ],
        [
            "How are you",            
            "I'm fine, thanks! And you?"
        ],
        [
            "How are you?",            
            "Kumusta?"
        ],
        [
            "How are you?",            
            "Mabuti naman,Salamat!"
        ],
        [
            "Mabuti naman,Salamat!",            
            "At ikaw? "
        ],
        [
            "Hey! Friend!",            
            "Kaibigan! In Tagalog"
        ],
        [
            "Anong bago?",            
            "What's new? Wala naman."
        ],
        [
            "See you later!",            
            "See you later! is Sa muling pagkikita!"
        ],
        [
            "Ako’y nawawala",            
            "You are lost - Ako’y nawawala"
        ],
        [
            "How much is this?",            
            "Magkano ito? means How much is this?"
        ],
        [
            "Excuse me!",            
            "Makikiraan po!"
        ],
        [
            "Makikiraan po!",            
            "Excuse me! ( to pass by) Makikiraan po!"
        ],
        [
            "Come with me!",            
            "Sumama ka sa akin!"
        ],
        [
            "One moment please!",            
            "Isang Saglit lang po."
        ],
        [
            "Go straight! then turn left/ right!",            
            "Diretso lang, tapos kaliwa/kanan!"
        ],
        [
            "Where is the bathroom",            
            "Nasaan ang palikuran - Where is the bathroom"
        ],
        [
            "Can I help you? ",            
            "Pwede ba kitang tulungan?"
        ],
        [
            "See you later!",            
            "Sa muling pagkikita! - See you later!"
        ],
        [
            "how do I say just a little in Tagalog.",            
            "Kaunti lang. Means just a little"
        ],
        [
            "Happy birthday!",            
            "Maligayang Kaarawan! Happy Birthday in Tagalog"
        ],
        [
            "Good night and sweet dreams!",            
            "Gandang Gabi!"
        ],
        [
            "No Problem!",            
            "Walang Problema.."
        ],
        [
            "Pwedeng pakihinaan ang iyong pagsasalita?",            
            "Can You Speak Slowly?"
        ],
        [
            "I do not understand.",            
            "Pwedeng pakihinaan ang iyong pagsasalita?"
        ],
        [
            "How do I say, I Have No Idea.",            
            "Wala akong ideya."
        ],
        [
            "how do I say I Don't Know!",            
            "Hindi ko alam."
        ],
        [
            "How are you ?",            
            "Mabuti!"
        ],
        [
            "Gusto mo ba dito?",            
            "Ang Pilipinas ay magandang bansa."
        ],
        [
            "Gusto ko ang Tagalog.",            
            "I like Tagalog also."
        ],
        [
            "How old are you?",            
            "I am not very old ilang taon ka na?"
        ]
    ]
}

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# Train based on english greetings corpus
chatbot.train("chatterbot.corpus.english.tagalog")

# Train based on the english conversations corpus
chatbot.train("chatterbot.corpus.english.conversations")


from chatterbot import ChatBot

chatbot = ChatBot(
    'MonkMonk',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
#chatbot.train("chatterbot.corpus.english")
#chatbot.train("chatterbot.corpus.english.greetings",
chatbot.train("chatterbot.new-stuff")    
# Get a response to an input statement
chatbot.get_response("Well, Mr. Dudah, How are you ?")



from chatterbot import ChatBot

chatbot = ChatBot(
    'MonkMonk',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

    # Train based on the english corpus
    #chatbot.train("chatterbot.corpus.english")
chatbot.train("chatterbot.corpus.english.greetings")
    # Get a response to an input statement
while True:
    try:
        bot_input = chatbot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break


# %load chatterbot-corpus/chatterbot_corpus/corpus.py
import os


class Corpus(object):

    def __init__(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        self.data_directory = os.path.join(current_directory, 'data')

    def get_file_path(self, dotted_path, extension='json'):
        """
        Reads a dotted file path and returns the file path.
        """

        # If the operating system's file path seperator character is in the string
        if os.sep in dotted_path or '/' in dotted_path:
            # Assume the path is a valid file path
            return dotted_path

        parts = dotted_path.split('.')
        if parts[0] == 'chatterbot':
            parts.pop(0)
            parts[0] = self.data_directory

        corpus_path = os.path.join(*parts)

        if os.path.exists(corpus_path + '.{}'.format(extension)):
            corpus_path += '.{}'.format(extension)

        return corpus_path

    def read_corpus(self, file_name):
        """
        Read and return the data from a corpus json file.
        """
        import json
        import io

        with io.open(file_name, encoding='utf-8') as data_file:
            data = json.load(data_file)
        return data

    def list_corpus_files(self, dotted_path):
        """
        Return a list of file paths to each data file in
        the specified corpus.
        """
        corpus_path = self.get_file_path(dotted_path, extension='corpus.json')
        paths = []

        if os.path.isdir(corpus_path):
            for dirname, dirnames, filenames in os.walk(corpus_path):
                for datafile in filenames:
                    if datafile.endswith('corpus.json'):
                        paths.append(os.path.join(dirname, datafile))
        else:
            paths.append(corpus_path)

        paths.sort()
        return paths

    def load_corpus(self, dotted_path):
        """
        Return the data contained within a specified corpus.
        """
        data_file_paths = self.list_corpus_files(dotted_path)

        corpora = []

        for file_path in data_file_paths:
            corpus = self.read_corpus(file_path)

            for key in list(corpus.keys()):
                corpora.append(corpus[key])

        return corpora



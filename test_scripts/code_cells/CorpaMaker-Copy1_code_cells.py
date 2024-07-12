!ls chatterbot-corpus/chatterbot_corpus/data/english

# Title_Maker 
def coptitle(coptit):
    copt = open("chatterbot-corpus/chatterbot_corpus/data/english/"+ coptit + ".corpus.json","w")
    copbrac ="{"
    copsp = "\n    \""
    copclo = "\": ["
    copt.write(copbrac+copsp+coptit+copclo)
    copt.close()
coptit = raw_input('title')
coptitle(coptit)
       

!rm chatterbot-corpus/chatterbot_corpus/data/english/  chitcht.corpus.json	

!ls chatterbot-corpus/chatterbot_corpus/data/english/

!ls chatterbot-corpus/chatterbot_corpus/data/english/coptit+.corpus.json

# %load chatterbot-corpus/chatterbot_corpus/data/english/chitchat.corpus.json
{
    "chitchat": [
        [
            "Hey, Dude, What you want ?"            
            "I want to know why you call me Dude ?"
        ],

# Copra_Maker
# Fillin the name of the file you just created
speak = raw_input('speak')
respond = raw_input('respond')
space = "            \""
txtstart = "        ["
txtspace = "            "
txtend = "        ],"

def copraIn():

   cop = open("chatterbot-corpus/chatterbot_corpus/data/english/chitchat.corpus.json","a")
   #cop.write("\n"+ txspace + "\""+txtstart + speak + "\"\n" + txspace + "\""+respond+"\"" + "\n" + txtend)
   cop.write("\n"+txtstart+"\n"+space+speak+"\""+txtspace+"\n"+space+respond+"\"\n"+txtend)
   cop.close()


copraIn()

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# Train based on english greetings corpus
chatbot.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
chatbot.train("chatterbot.corpus.english.conversations")


from chatterbot import ChatBot

chatbot = ChatBot(
    'MonkMonk',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
#chatbot.train("chatterbot.corpus.english")
chatbot.train("chatterbot.corpus.english")
# Get a response to an input statement
while True:
    try:
        bot_input = bot.get_response(None)

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



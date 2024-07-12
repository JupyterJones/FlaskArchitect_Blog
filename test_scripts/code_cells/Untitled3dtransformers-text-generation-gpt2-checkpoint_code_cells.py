from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(42)
generator("The release of ", max_length=50, num_return_sequences=10)


generator("I will go crazy for an ", max_length=50, num_return_sequences=10)

generator("Would love to try ", max_length=50, num_return_sequences=10)

import sys
import os
PATH = "/home/jack/Downloads/"
path = os.listdir(PATH)
for i in path:
        print(PATH+i)


from generated_text import gentext
from random import randint
print(len (gentext()))

from generated_text import gentext
from random import randint
end = len (gentext())-1
ID = randint(0,end)
text = str(gentext()[ID])
text = text.replace("\\'t", "'t").replace("{", "").replace("}", "").replace("\\n", " ").replace("\"", "")
STR = text.replace("\\'s","'s'")
print (text)






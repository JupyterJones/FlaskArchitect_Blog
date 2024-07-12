from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(42)
generator("The release of ", max_length=50, num_return_sequences=10)


generator("What was so bad about the ", max_length=50, num_return_sequences=10)

generator("The release of ", max_length=50, num_return_sequences=10
[{'generated_text': "The release of \xa0The World's Dumbest People is the first in a trilogy from David Silverman and David Fincher. You may have heard of this book, called\xa0 The Man Who Sold Your Life, or, as it would come"},
 {'generated_text': "The release of iphone/iPad apps was a big success, with many of them doing well so far. But many customers were not impressed that so many apps weren't working for them. It is now common for an Android phone not to"},
 {'generated_text': 'The release of ichthyosis, a syndrome associated with anemia, has occurred earlier in women and increases in certain risk factors for certain cancers. In some cases, anemia has led to kidney or liver failure; in others, the cause has'},
 {'generated_text': 'The release of \xa0Oscar nominee Amy Poehler, a role he had previously worked out with, helped launch the new era of musical theater in the country. The move to comedy shows has also led to a surge in ticket sales, a move'},
 {'generated_text': 'The release of \xa0The Black Queen \xa0on\xa0 March 23rd, 2013 was one of the most\xa0emotional \xa0scenes ever written. Even during the last months, the release of \xa0The Black Queen \xa0on\xa0 March'},
 {'generated_text': 'The release of vernacular speech will give people the possibility to express their ideas freely and get help for learning.'},
 {'generated_text': 'The release of \xa0A Clockwork Orange has stirred a lot of debate. I mean, what am I going to do?? I mean, what am I going to do with all those hours of thinking? I mean you are now thinking like an old'},
 {'generated_text': 'The release of _____ would mean that the public is no longer immune from being exposed to the threat of mass public suicide, and it could result in serious consequences for public safety, like the loss of lives, and may even lead to further criminal and'},
 {'generated_text': "The release of 々个非来》 is a bold and powerful moment. I can't believe I've read an English book where this happened. Even I wasn't able to read a few paragraphs right now. It"},
 {'generated_text': "The release of ??? was reported by both Chinese and Vietnamese media outlets, with both groups claiming that it was being directed from Beijing.\n\nBut the Chinese government has denied that it directed these groups to commit acts of terror like last weekend's Boston"}]

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






text_a = open("1342-0.txt").read()
text_b = open("84-0.txt").read()

print(text_a[:200])

import random
random.sample(text_b, 20)

a_words = text_a.split()
b_words = text_b.split()

random.sample(a_words, 10)

random.sample(b_words, 10)

from collections import Counter
Counter(text_a).most_common(12)

Counter(a_words).most_common(12)

Counter(b_words).most_common(12)

import sys
!{sys.executable} -m pip install markovify

import markovify

generator_a = markovify.Text(text_a)

print(generator_a.make_sentence())

print(generator_a.make_short_sentence(50))

print(generator_a.make_short_sentence(40, tries=100))

print(generator_a.make_short_sentence(40, test_output=False))

gen_a_1 = markovify.Text(text_a, state_size=1)
gen_a_4 = markovify.Text(text_a, state_size=4)

print("order 1")
print(gen_a_1.make_sentence(test_output=False))
print()
print("order 4")
print(gen_a_4.make_sentence(test_output=False))

class SentencesByChar(markovify.Text):
    def word_split(self, sentence):
        return list(sentence)
    def word_join(self, words):
        return "".join(words)

con_model = SentencesByChar("condescendences", state_size=2)

con_model.make_sentence()

gen_a_char = SentencesByChar(text_a, state_size=7)

print(gen_a_char.make_sentence(test_output=False).replace("\n", " "))

generator_a = markovify.Text(text_a)
generator_b = markovify.Text(text_b)
combo = markovify.combine([generator_a, generator_b], [0.5, 0.5])

print(combo.make_sentence())

# change to "word" for a word-level model
level = "char"
# controls the length of the n-gram
order = 7
# controls the number of lines to output
output_n = 14
# weights between the models; text A first, text B second.
# if you want to completely exclude one model, set its corresponding value to 0
weights = [0.5, 0.5]
# limit sentence output to this number of characters
length_limit = 280

model_cls = markovify.Text if level == "word" else SentencesByChar
gen_a = model_cls(text_a, state_size=order)
gen_b = model_cls(text_b, state_size=order)
gen_combo = markovify.combine([gen_a, gen_b], weights)
for i in range(output_n):
    out = gen_combo.make_short_sentence(length_limit, test_output=False)
    out = out.replace("\n", " ")
    print(out)
    print()

sonnets_text = open("sonnets.txt").read()
sonnets_model = markovify.NewlineText(sonnets_text, state_size=1)

sonnets_model.make_sentence()

for i in range(14):
    print(sonnets_model.make_sentence())

class LinesByChar(markovify.NewlineText):
    def word_split(self, sentence):
        return list(sentence)
    def word_join(self, words):
        return "".join(words)

sonnets_char_model = LinesByChar(sonnets_text, state_size=4)

for i in range(14):
    print(sonnets_char_model.make_sentence())

import json
mood_data = json.loads(open("./moods.json").read())
moods = mood_data['moods']

moods_text = "\n".join(moods)

moods_char_model = LinesByChar(moods_text, state_size=3)

for i in range(24):
    print(moods_char_model.make_sentence())


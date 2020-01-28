#REFER WORDNET10.PY IN "PROJECT'

from nltk.corpus import wordnet
syn = wordnet.synsets('cookbook')
print(syn)
print(syn[0].lemmas()[0].name())
print(syn[0].definition())
print(syn[0].examples())
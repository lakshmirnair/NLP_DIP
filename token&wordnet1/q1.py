
#The sent_tokenize function uses an instance of PunktSentenceTokenizer from the
#nltk.tokenize.punkt module.
a="Hello World. It's good to see you. Thanks for buying this book."
from nltk.tokenize import sent_tokenize
print(sent_tokenize(a))


#The instance used in sent_tokenize() is actually loaded on demand from a pickle
#file. So if you're going to be tokenizing a lot of sentences, it's more efficient to load the
#PunktSentenceTokenizer class once, and call its tokenize() method instead

"""import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')
print(tokenizer.tokenize(a))"""

#split into word

from nltk.tokenize import word_tokenize
print(word_tokenize('Hello World.'))


#The word_tokenize() function is a wrapper function that calls tokenize() on an
#instance of the TreebankWordTokenizer class. It's equivalent to the following code:

from nltk import TreebankWordTokenizer, regexp_tokenize

tr=TreebankWordTokenizer()
print(tr.tokenize('Hello World.'))


#punktwordtokenizer
"""from nltk.tokenize import PunktWordTokenizer
tokenizer = PunktWordTokenizer()
print(tokenizer.tokenize("Can't is a contraction."))"""  #showing import error

#wordpuncttokenizer(saparate the punctuator)
from nltk.tokenize import WordPunctTokenizer
tokenizer = WordPunctTokenizer()
print(tokenizer.tokenize("Can't is a contraction."))

#RegexpTokenizer

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer("[\w']+")
print(tokenizer.tokenize("Can't is a contraction."))


from nltk.tokenize import regexp_tokenize
print(regexp_tokenize("Can't is a contraction.","[\w']+"))
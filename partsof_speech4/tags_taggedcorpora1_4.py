
#TAGGED CORPORA

"""By convention in NLTK, a tagged token is represented using a tuple consisting of the token and the tag.
We can create one of these special tuples from the standard string representation of a tagged token, using the
function str2tuple():
"""

# Reading Tagged Corpora

"""NLTK's corpus readers provide a uniform interface so that you don't have to be concerned with the
 different file formats  like pos_tag,nltk.tag.str2tuple('car/NN')
"""
import nltk
print(nltk.corpus.brown.tagged_words()[1:10])

print(nltk.corpus.brown.tagged_words(tagset='universal')[1:10])

"""import nltk
nltk.download('nps_chat')"""
print(nltk.corpus.nps_chat.tagged_words())

print(nltk.corpus.conll2000.tagged_words())

print(nltk.corpus.treebank.tagged_words())

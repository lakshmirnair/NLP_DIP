import pprint
from nltk.corpus import stopwords
from nltk.corpus import webtext
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

stopset = set(stopwords.words('english'))
filter_stops = lambda w: len(w) < 3 or w in stopset

words = [w.lower() for w in webtext.words('grail.txt')]
bcf = BigramCollocationFinder.from_words(words)
#bcf.apply_word_filter(filter_stops)
results = bcf.nbest(BigramAssocMeasures.likelihood_ratio, 10)

pprint.pprint([' '.join(r) for r in results])



print("exampe2")
from nltk.corpus import stopwords
stopset = set(stopwords.words('english'))
filter_stops = lambda w: len(w) < 3 or w in stopset
"""#bcf.apply_word_filter(filter_stops)
#[('black', 'knight'), ('clop', 'clop'), ('head', 'knight'), ('mumble', 'mumble')]

print(bcf.nbest(BigramAssocMeasures.likelihood_ratio, 4))"""

bcf.apply_word_filter(filter_stops)
print(bcf.nbest(BigramAssocMeasures.likelihood_ratio,10))
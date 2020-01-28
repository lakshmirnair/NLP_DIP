from nltk.collocations import TrigramCollocationFinder
from nltk.corpus import webtext, stopwords
from nltk.metrics import TrigramAssocMeasures
words = [w.lower() for w in webtext.words('singles.txt')]
stopset = set(stopwords.words('english'))
filter_stops = lambda w: len(w) < 3 or w in stopset
tcf = TrigramCollocationFinder.from_words(words)
tcf.apply_word_filter(filter_stops)
tcf.apply_freq_filter(3)
print(tcf.nbest(TrigramAssocMeasures.likelihood_ratio,4))
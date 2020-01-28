#using WordNetLemmatizer from wordnet
a="A cat, cats cacti always."
from sklearn.feature_extraction.text import CountVectorizer
import string
from nltk.stem.wordnet import WordNetLemmatizer
vectorizer = CountVectorizer(min_df=1, stop_words='english')
exclude = list(string.punctuation)
stop=list(sorted(vectorizer.get_stop_words()))
stop_free = " ".join([i for i in a.lower().split() if i not in stop])
punc_free = "".join([ch for ch in stop_free if ch not in exclude])
print(stop_free)
print(punc_free)

lemma = WordNetLemmatizer()
normalized = " ".join([lemma.lemmatize(word) for word in punc_free.split()])
print(normalized)

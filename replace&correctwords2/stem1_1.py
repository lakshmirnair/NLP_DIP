from sklearn.feature_extraction.text import CountVectorizer

a="""Artificial intelligence (AI), sometimes called machine intelligence, is intelligence
 demonstrated by machines, in contrast to the natural intelligence displayed by humans and other animals.  Colloquially, the term 
  "artificial intelligence" is applied when a machine mimics "cognitive" functions that humans associate with other
   human minds, such as learning and problem solving"""
from nltk.tokenize import word_tokenize
at=word_tokenize(a)

#import nltk.stem
#english_stemmer = nltk.stem.SnowballStemmer('english')

from nltk.stem import SnowballStemmer
english_stemmer=SnowballStemmer('english')

class StemmedCountVectorizer(CountVectorizer):

    def build_analyzer(self):
        analyzer = super().build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))

# vectorizer = CountVectorizer(min_df=1, stop_words='english',
# preprocessor=stemmer)
vectorizer = StemmedCountVectorizer(min_df=1, stop_words='english')
xt=vectorizer.fit(at)
print("features")
print(vectorizer.get_feature_names())

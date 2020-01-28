#Lemmatization is very similar to stemming, but is more akin to synonym replacement.

#NOTE:So unlike stemming, you are always left with a valid word that means the same thing.

from nltk.stem import WordNetLemmatizer
lem = WordNetLemmatizer()
print(lem.lemmatize('cooking'))
print(lem.lemmatize('cooking', pos='v'))
print(lem.lemmatize('cookbooks'))
#The WordNetLemmatizer class is a thin wrapper around the wordnet corpus and uses the
#morphy() function of the WordNetCorpusReader class to find a lemma. If no lemma is
#found, or the word itself is a lemma, the word is returned as is.



from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem('believes'))
print(lem.lemmatize('believes'))
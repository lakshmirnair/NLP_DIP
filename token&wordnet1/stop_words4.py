#METHOD:1 USING COUNT VETORIZER

#to find stop words
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(min_df=1,stop_words='english')
#print(sorted(vectorizer.get_stop_words())[0:150])


a="""Artificial intelligence (AI), sometimes called machine intelligence, is intelligence
 demonstrated by machines, in contrast to the natural intelligence displayed by humans and other animals. In computer
  science AI research is defined as the study of "intelligent agents": any device that perceives its environment 
  and takes actions that maximize its chance of successfully achieving its goals.[1] Colloquially, the term 
  "artificial intelligence" is applied when a machine mimics "cognitive" functions that humans associate with other
   human minds, such as learning and problem solving
"""
from nltk import word_tokenize
at=word_tokenize(a)

xt=vectorizer.fit_transform(at)
print(vectorizer.get_feature_names())

#METHOD 2 USING STOPWORDS

#The stopwords corpus is an instance of nltk.corpus.reader.
#WordListCorpusReader. As such, it has a words() method that can take a single
#argument for the file ID, which in this case is 'english', referring to a file containing
#a list of English stopwords. You could also call stopwords.words() with no argument
#to get a list of all stopwords in every language available.

from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))
words = ["Can't", 'is', 'a', 'contraction']
s=[word for word in words if word not in english_stops]
print(s)

# give stop words of all languages available in the packages
print(stopwords.words())
#can see the complete list of languages using the fileids method as follows:
print(stopwords.fileids())
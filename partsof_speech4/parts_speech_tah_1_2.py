from nltk.tokenize import sent_tokenize, word_tokenize
a="Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
x=(word_tokenize(a))

# to print what and all stopwords are in english language according to the package


from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(min_df=1,stop_words='english')

#TO PRINT FIRST 150 STOP WORDS
#print(sorted(vectorizer.get_stop_words())[0:150])

xt=vectorizer.fit_transform(x)
print(vectorizer.get_feature_names())
y=vectorizer.get_feature_names()

#STEMMING
stem=[]
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
for i in y:
    r=stemmer.stem(i)
    stem.append(r)
print(stem)

#PARTS OF SPEECH TAGGING
import nltk
print(nltk.pos_tag(y))


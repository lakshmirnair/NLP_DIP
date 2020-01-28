import gensim

doc1 = "Sugar is bad to consume. My sister likes to have sugar, but not my father."
doc2 = "My father spends a lot of time driving my sister around to dance practice."
doc3 = "Doctors suggest that driving may cause increased stress and blood pressure."
doc4 = "Sometimes I feel pressure to perform well at school, but my father never seems to drive my sister to do better."
doc5 = "Health experts say that Sugar is not good for your lifestyle."


doc_complete = [doc1, doc2, doc3, doc4, doc5]

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df=1, stop_words='english')
stop=list(sorted(vectorizer.get_stop_words()))
exclude = list(string.punctuation)
lemma = WordNetLemmatizer()
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join([ch for ch in stop_free if ch not in exclude])
    normalized = " ".join([lemma.lemmatize(word) for word in punc_free.split()])
    return normalized

doc_clean = [clean(doc) for doc in doc_complete]
print(doc_clean)



# Importing Gensim

from gensim import corpora

#Creating the term dictionary of our courpus, where every unique term is assigned an index.
"""dictionary = corpora.Dictionary(doc_clean)
print(dictionary)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]"""
tot=[]
for i in doc_clean:
    a=[]
    for j in i.split(" "):
        a.append(j)
    tot.append(a)
print(tot)


#To reduce the occurance of the  words
dictionary = corpora.Dictionary(tot)
dictionary.save('abc.txt')  # store the dictionary, for future reference
print(dictionary)

print(dictionary.token2id)


#To actually convert tokenized documents to vectors:
"""doc_term_matrix = [dictionary.doc2bow(doc.split(" ")) for doc in doc_clean]
print(doc_term_matrix)"""
#To actually convert tokenized documents to vectors: in each sentence
doc_term_matrix = [dictionary.doc2bow(doc) for doc in tot]
print(doc_term_matrix)


# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=5, id2word = dictionary, passes=50)
print(ldamodel.print_topics(num_topics=5, num_words=5))


import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
w=WordNetLemmatizer()
def findpos(x):
    t='n'
    if x.startswith("V"):
        t="v"
    elif x.startswith("J"):
        t="a"
    elif x.startswith("R"):
        t="r"
    elif x.startswith("N"):
        t="n"
    return(t)

ft=open('comb.txt','w')
for i in range(50):
   file1="neg"+str(i)
   f1=open("data/"+file1+".txt","r")
   ft.write(f1.read())

for i in range(50):
   file1="pos"+str(i)
   f1=open("data/"+file1+".txt","r")
   ft.write(f1.read())
ft.close()
f=open('comb.txt')
con=f.read()
print(con)
stopwo=set(stopwords.words('english'))
#print(stopwords)
con=con.lower()
word_tokens = word_tokenize(con)
filt_sent= []


for w in word_tokens:
  if (w not in stopwo):
   filt_sent.append(w)
print(filt_sent)

pos=nltk.pos_tag(filt_sent)
print(pos)


"""unigrams = ngrams(lemma,1)
print(Counter(unigrams))
bigrams = ngrams(lemma,2)
print(Counter(bigrams))"""


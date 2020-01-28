#using  the PorterStemmer class and call the stem() function
#"One of the most common stemming algorithms is the Porter stemming algorithm by MartinPorter"
from nltk.stem import PorterStemmer
s = PorterStemmer()
print(s.stem('cooking'))
print(s.stem('cookery'))

#problem ,lemmatization can rectify  this problem
print(s.stem('generous'))
print(s.stem('general'))


#The functions of the LancasterStemmer class are just like the functions of the
#PorterStemmer class, but can produce slightly different results. It is known to
#be slightly more aggressive than the PorterStemmer functions:

print()
print("method 2")
from nltk.stem import LancasterStemmer
s =LancasterStemmer()
print(s.stem('cooking'))
print(s.stem('cookery'))


#The RegexpStemmer class

#You can also construct your own stemmer using the RegexpStemmer class. It takes
#suffix that matches the expression:
from nltk.stem import RegexpStemmer
stemmer = RegexpStemmer('ed')
print(stemmer.stem('cooking'))
print(stemmer.stem('cookery'))
print(stemmer.stem('ingleside'))


#SNOWBALLSTEMMER.The SnowballStemmer class supports 15 non-English languages. It also provides two
#   English stemmers: the original porter algorithm as well as the new English stemming algorithm.

from nltk.stem import SnowballStemmer
print(SnowballStemmer.languages)
print(len(SnowballStemmer.languages))
st=SnowballStemmer('english')
print(st.stem('cooking'))
print(st.stem('studied'))
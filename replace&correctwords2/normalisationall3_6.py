

text='aiUOd'
print(text.lower())
print(text.upper())


#2 removing punctuation

text='She? Hm, why not!'
puncts='.?!'
for sym in puncts:
    text= text.replace(sym,' ')
print(text)




#3 converting numbers into words
from num2words import num2words
a="i was born in 1997 on 25 th october "
from  nltk.tokenize import word_tokenize
xt=list(word_tokenize(a))
print(xt)
s=[]
        #text = text.strip()  to remove white spaces
"""if all(a[i] in "0123456789" for i in range(len(a))):
    print("The string is an integer.")"""
y="0123456789"
for i in xt:
    for j in range(len(i)):
        if(i[j] not in y):
            s.append(i)
            break
        d = int(i)
        k = num2words(d)
        s.append(k)
        break
print(s)


#4  expanding abbrevation
te='USA and GB are ...'
abbrevs={'USA':'United States','GB':'Great Britain'}
for ab in abbrevs:
    te= te.replace(ab,abbrevs[ab])
print(te)

#remove stop words
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df=1, stop_words='english')
stop=list(sorted(vectorizer.get_stop_words()))
a="Artificial intelligence is the intelligence exhibited by machine"
pu = " ".join(set([ch for ch in a.split(" ") if ch not in stop]))
print(pu)

#remove punctuation
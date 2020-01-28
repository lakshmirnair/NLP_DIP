#CONVERT NUMBERS TO WORDS

from num2words import num2words
print(num2words(42))
print(num2words(42, ordinal=True))

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
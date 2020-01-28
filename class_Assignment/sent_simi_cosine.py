from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
s1 ="I love chocalate"
s2="I love dog"
st1 = word_tokenize(s1)
st2 = word_tokenize(s2)
stop = stopwords.words('english')
l1 =[]
l2 =[]

sn1=[]
sn2=[]
for i in st1:
    if (not i in stop):
        sn1.append(i)
sn1=set(sn1)
for j in st2:
    if (not j in stop):
        sn2.append(j)
sn2=set(sn2)



rvector = sn1.union(sn2)
for w in rvector:
	if w in sn1:
          l1.append(1)
	else:
          l1.append(0)
	if w in sn2:
          l2.append(1)
	else:
          l2.append(0)
c = 0
d1=0
d2=0
print(rvector)
for i in range(len(rvector)):
		c=c+ l1[i]*l2[i]
for i in range(len(l1)):
		d1=d1+ l1[i]*l1[i]
d1=float((d1)**0.5)
for i in range(len(l2)):
		d2=d2+ l2[i]*l2[i]
d2=float((d2)**0.5)

cosine = c / d1*d2
print("similarity: ", cosine)

'''c=0
for i in range(len(rvector)):
        c=c+ l1[i]*l2[i]
cosine = c / float((sum(l1)*sum(l2))**0.5)
print("similarity: ", cosine)'''
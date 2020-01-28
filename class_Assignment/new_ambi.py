from nltk.corpus import wordnet
sy1 = []
#antonyms = []
s1="nice"
for syn in wordnet.synsets("nice"):
	for l in syn.lemmas():
		sy1.append(l.name())

print(set(sy1))
k1=list(set(sy1))
#print(set(antonyms))
n1=len(set(sy1))
print(n1)

sy2 = []
#antonyms = []
s2="good"
for syn in wordnet.synsets("good"):
	for l in syn.lemmas():
		sy2.append(l.name())

print(set(sy2))
#print(set(antonyms))
n2=len(set(sy2))
k2=list(set(sy2))
print(n2)

k=[]
for i in range(n2):
    for j in range(n1):
        wordFromList1 = wordnet.synsets(s2)[i]

        wordFromList2 = wordnet.synsets(s1)[j]
        s = wordFromList1.wup_similarity(wordFromList2)
        k.append(s)
print(k)
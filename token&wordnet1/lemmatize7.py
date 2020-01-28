#A lemma (in linguistics), is the canonical form or morphological form of a word.

from nltk.corpus import wordnet
syn = wordnet.synsets('cookbook')[0]
lemmas = syn.lemmas()#find lemmatising word for corresponding synonym we got just before  statement
print(len(lemmas))

#find lemmatised words
print(lemmas[0].name())
print(lemmas[1].name())

#to find synonym of each lemmatised words
print(lemmas[0].synset() == lemmas[1].synset())
print(lemmas[0].synset())
print(lemmas[1].synset())


#find lemmatised words,ie find the word having the root word we found out
print([i.name() for i in syn.lemmas()])

#all possible synonims
synonyms = []
for syn in wordnet.synsets('book'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print(len(synonyms))
print(synonyms)

#there appears to be 38 possible synonyms for the word 'book'. But in
#fact, some synonyms are verb forms, and many synonyms are just different usages of
#'book'.
print(len(set(synonyms)))



#ANTONYMS
gn2 = wordnet.synset('good.n.02')
print(gn2.definition())
evil= gn2.lemmas()[0].antonyms()[0]
print(evil.name)

print(evil.synset().definition())
ga1 = wordnet.synset('good.a.01')
print(ga1.definition())
bad = ga1.lemmas()[0].antonyms()[0]
print(bad.name())

print(bad.synset().definition())


#semantic relationship and similiarity
w1=wordnet.synset("ship.n.01")
w2=wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2))

#ERROR ,when  we want to find similiarity specify the type of word and number which is used to
#  disambiguate the word meaning
"""w1=wordnet.synset("ship")

w2=wordnet.synset("boat")
print(w1.wup_similarity(w2))"""

from nltk.corpus import wordnet
cb = wordnet.synset('cookbook.n.01')
ib = wordnet.synset('instruction_book.n.01')
cb.wup_similarity(ib)
#The wup_similarity method is short for Wu-Palmer Similarity, similiarity is determined by the the difference
# wrt the dicision tree
ref = cb.hypernyms()[0]
print(ref)
print(cb.shortest_path_distance(ref))
print(ib.shortest_path_distance(ref))
print(cb.shortest_path_distance(ib))


#note
dog = wordnet.synsets('dog')[0]
print(dog.wup_similarity(cb))

#Wow, dog and cookbook are apparently 38% similar! This is because "THEY SHARE COMMON HYPERNYMS" further up the tree:
print(sorted(dog.common_hypernyms(cb)))



#comparing verbs
cook = wordnet.synset('cook.v.01')
bake = wordnet.synset('bake.v.02')
print(cook.wup_similarity(bake))


#The relationship is given as -log(p/2d) where p is the shortest path length and d the taxonomy depth.
#prefer "the wup_similarity method."
print(cb.path_similarity(ib))
print(cb.path_similarity(dog))
print(cb.lch_similarity(ib))
print(cb.lch_similarity(dog))


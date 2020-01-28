def getMaxSim(s1, s2):
    if len(wordnet.synsets(s2)) != 0:
        wordFromList1 = wordnet.synsets(s1)[0]

        wordFromList2 = wordnet.synsets(s2)[0]
        s = wordFromList1.wup_similarity(wordFromList2)

        if s == None:

            return 0
        else:
            return s
    else:

        return 0


from nltk.corpus import wordnet

print(getMaxSim("good", "nice"))
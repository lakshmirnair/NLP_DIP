#Synsets are organized in a structure similar to that of an inheritance tree. More abstract terms
#are known as hypernyms and more specific terms are hyponyms. This tree can be traced all
#the way up to a root hypernym.
from nltk.corpus import wordnet
syn = wordnet.synsets('cookbook')[0]
print(syn.hypernyms()) #abstract term
print(syn.hypernyms()[0].hyponyms()) #more specific terms are hyponyms.
print(syn.root_hypernyms())#And all these types of books have the same root hypernym, which is entity


#You can trace the entire path from entity down to cookbook using the hypernym_paths() method
print(syn.hypernym_paths())#The hypernym_paths() method returns a list of lists, where each list starts at the root
#hypernym and ends with the original Synset

#PARTS OF SPEECH
print(syn.pos())


print(len(wordnet.synsets('great')))
print(len(wordnet.synsets('great', pos='n')))
print(len(wordnet.synsets('great', pos='a')))
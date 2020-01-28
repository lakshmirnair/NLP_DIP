#NLTK provides a PunktSentenceTokenizer class that you can train on raw text to produce
#a custom sentence tokenizer. You can get raw text either by reading in a file, or from an NLTK
#corpus using the raw() method.
"""import nltk
nltk.download('webtext')"""
from nltk.corpus import webtext
text = webtext.raw('overheard.txt')
from nltk.tokenize import PunktSentenceTokenizer

sent_tokenizer = PunktSentenceTokenizer(text)
sents1 = sent_tokenizer.tokenize(text)
print(sents1[0])

from nltk.tokenize import sent_tokenize
se2 = sent_tokenize(text)
print(se2[0])#couldnt find any difference

#sentence at 678 only
print(sents1[678])
#sentence at 678 anf 679 ,ineffecient
print(se2[678])


#The PunktSentenceTokenizer class learns from any string, which means you can open a
#text file and read its content. Here is an example of reading overheard.txt directly instead
#of using the raw() corpus method

#(check text book)
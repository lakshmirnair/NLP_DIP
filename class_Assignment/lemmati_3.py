import nltk
from nltk.stem import WordNetLemmatizer

w = WordNetLemmatizer()


def findpos(x):
    t = 'n'
    if x.startswith("V"):
        t = "v"
    elif x.startswith("J"):
        t = "a"
    elif x.startswith("R"):
        t = "r"
    elif x.startswith("N"):
        t = "n"
    return (t)


word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
# First Word tokenization
tokens = nltk.word_tokenize(word_data)
pos = nltk.pos_tag(tokens)
print(pos)
lemma = []
for i in range(len(pos)):
    x = findpos(pos[i][1])
    lemma.append(w.lemmatize(pos[i][0], x))
print(lemma)


import nltk
from nltk.tokenize import word_tokenize
text = word_tokenize("And now for something completely different")
print(nltk.pos_tag(text))

# IF WE DONT KNOW WHAT IS CC,NN,VB MEANS USE THE FUNCTION BELOW. IT GIVES  SIMILIAR KIND OF WORDS IN THE CATEGORY
text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
text.similar('bought')

#By convention in NLTK, a tagged token is represented using a tuple consisting of the token and the tag. We can create
#  one of these special tuples from the standard string representation of a tagged token, using the function str2tuple():
tagged_token = nltk.tag.str2tuple('fly/NN')
print(tagged_token)
print(tagged_token[0])
print(tagged_token[1])

sent = ''' The/AT grand/JJ jury/NN commented/VBD on/IN a/AT number/NN of/IN
     other/AP topics/NNS ,/, AMONG/IN them/PPO the/AT Atlanta/NP and/CC
    Fulton/NP-tl County/NN-tl purchasing/VBG departments/NNS which/WDT it/PPS
     said/VBD ``/`` ARE/BER well/QL operated/VBN and/CC follow/VB generally/RB
     accepted/VBN practices/NNS which/WDT inure/VB to/IN the/AT best/JJT
     interest/NN of/IN both/ABX governments/NNS ''/'' ./.'''
print([nltk.tag.str2tuple(t) for t in sent.split()])
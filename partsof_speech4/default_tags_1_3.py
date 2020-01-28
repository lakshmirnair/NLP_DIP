#Part-of-speech tagging is a necessary step before chunking, which

#Without the part-of-speech tags, a chunker cannot know how to extract
#phrases from a sentence. But with part-of-speech tags, you can tell a chunker how to identify
#phrases based on tag patterns.

#part-of-speech tags for grammar analysis and word sense disambiguation

#All taggers in NLTK are in the nltk.tag package and inherit from the TaggerI base class.
#TaggerI requires all subclasses to implement a tag() method,which takes a list of word  as input
#and returns a tagged word as output

#TaggerI also provides an evaluate() method for evaluating the accuracy of the tagger

from nltk.tag import DefaultTagger
tagger = DefaultTagger('NN')
print(tagger.tag(['Hello', 'World']))
print(tagger.tag(['we', 'are','going']))# WRONG


#SequentialBackoffTagger implements the tag() method, which calls the
#choose_tag() method of the subclass for each index in the tokens list while accumulating
#a history of the previously tagged tokens


"""DefaultTagger is a subclass of SequentialBackoffTagger. Every subclass of
SequentialBackoffTagger must implement the choose_tag() method, which
takes three arguments:
    * The list of tokens
    * The index of the current token whose tag we want to choose
    * The history, which is a list of the previous tags
    SequentialBackoffTagger implements the tag() method, which calls the
choose_tag() method of the subclass for each index in the tokens list while accumulating
a history of the previously tagged tokens. This history is the reason for the Sequential in
SequentialBackoffTagger. We'll get to the backoff portion of the name in the Combining
taggers with backoff tagging recipe. """


#accuracy text
"""So, by just choosing NN for every tag, we can achieve 14 % accuracy testing on one-fourth
of the treebank corpus."""
from nltk.corpus import treebank
test_sents = treebank.tagged_sents()[3000:]
print(tagger.evaluate(test_sents))




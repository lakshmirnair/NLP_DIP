#If stemming and lemmatization
#are a kind of linguistic compression, then word replacement can be thought of as error
#correction or text normalization.


#NORMALISATION
"""
1 eliminating punctuation
2 converting the entire text into lowercase or uppercase
3 converting numbers into words
4 expanding abbreviations
5 canonicalization of text
6 replacing "can't" with "cannot" or "would've" with "would have".
"""

#REPLACEMENT PATTERN  ????

import re #regualar expression package

replacement_patterns = [
(r'won\'t', 'will not'),
(r'can\'t', 'cannot'),
(r'i\'m', 'i am'),
(r'ain\'t', 'is not'),
(r'(\w+)\'ll', '\g<1> will'),
(r'(\w+)n\'t', '\g<1> not'),
(r'(\w+)\'ve', '\g<1> have'),
(r'(\w+)\'s', '\g<1> is'),
(r'(\w+)\'re', '\g<1> are'),
(r'(\w+)\'d', '\g<1> would')
]


class RegexpReplacer(object):
    def __init__(self, patterns=replacement_patterns):
        self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]

    def replace(self, text):
        s = text

        for (pattern, repl) in self.patterns:
            s = re.sub(pattern, repl, s)
        return s


rep=RegexpReplacer()
print(rep.replace("can't is a contradicton"))
print(rep.replace("I should've done that thing I didn't do"))

#What is Regular Expression?
#A regular expression in a programming language is a special text string used for describing a search pattern.
# It is extremely useful for extracting information from text such as code, files, log, spreadsheets or even documents.



import re

from nltk import RegexpTokenizer

xx = "guru99,education is fun"
r1 = re.findall(r"^\w+", xx)
print(r1)
print(re.findall(r"^\w", xx))
print(re.findall(r"\w", xx))
print(re.findall(r"\w+", xx))
print(re.findall(r"w", xx))
print((re.split(r'\s','we are splitting the words')))
print((re.split(r's','split the words')))

#Simple whitespace tokenizer
#tokenizer = RegexpTokenizer('\s+', gaps=True)
tokenizer = RegexpTokenizer('\s',gaps=False)
tokenizer = RegexpTokenizer('\s',gaps=True)
print(tokenizer.tokenize("Can't is a contraction."))
#IF ORDER IS MATTER

from collections import OrderedDict
foo = "mppmt"
f="looooveee"
print("".join(OrderedDict.fromkeys(f)))


foo = 'goose'
print(''.join(sorted(set(foo), key=foo.index)))


foo='moonkeeyyy'
print(''.join([j for i,j in enumerate(foo) if j not in foo[:i]]))
'mpt'

#if order is not important
foo='mppmt'
print(''.join(set(foo)))

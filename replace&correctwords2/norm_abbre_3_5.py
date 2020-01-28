#expand abbrevation

text='USA and GB are ...'
abbrevs={'USA':'United States','GB':'Great Britain'}
for ab in abbrevs:
    text= text.replace(ab,abbrevs[ab])
print(text)
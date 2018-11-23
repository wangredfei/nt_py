import re

s = '2008年发生了很多大事,08奥运,512地震'
s2 = "zhang:1994 li:1993"
'''
pattern = r'(\w)+:(\d+)'
# [('g', '1994'), ('i', '1993')]
pattern = r'(\w+)+:(\d+)'
# [('zhang', '1994'), ('li', '1993')]
l = re.findall(pattern,s2)
print(l)
'''
pattern = r'\d+'
regex = re.compile(pattern)
l = regex.findall(s,0,19)
print(l)

l = re.split(r'\s+',"Hello wo15  N44ao Beijing")
print(l)

s = re.subn(r'\s+','##','hello word haha',1)
print(s)

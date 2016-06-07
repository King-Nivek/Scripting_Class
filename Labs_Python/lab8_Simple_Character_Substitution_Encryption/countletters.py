#!/usr/bin/python
'''
'
'
'''
from random import sample
from sys import argv

file = open(argv[1])
txt_chars = list(file.read())
charCount = {}
for char in txt_chars:
  charCount[ord(char)] = charCount.get(ord(char), 0) + 1

keys = [9,10] + range(32,127)
values = [80,90,86,48,102,46,40,62,71,83,115,43,44,69,101,39,59,99,54,67,100,118,105,33,42,119,88,91,114,109,96,37,79,97,116,55,65,56,125,75,52,111,112,77,103,123,87,10,94,81,76,49,104,68,9,64,57,93,73,60,120,38,70,85,82,89,63,34,110,36,84,113,66,78,108,47,41,61,117,45,58,126,53,92,72,50,124,51,98,122,32,106,74,95,35,107,121]


#sample(keys,len(keys))

#print range(len(values))
#print keys
#print values    
code = dict(zip(keys,values))
keyssort = code.keys()
keyssort.sort()
strFormat = '{0:>2}). {1:>3} | {2:>2} | {3:>4} == {4:>4} | {5:>2} | {6:>3}'
print 'Sorted Character Dictionary:'
print strFormat.format('k','Ord','Ch','cin','cout','Ch','Ord')
k = 1
for i in keyssort:
  if i == 10:
    print strFormat.format(k,
                           i,r"\n",charCount.get(i,' '),
                           charCount.get(code[i],' '),chr(code[i]),code[i],)
  elif i == 9:
    print strFormat.format(k,
                           i,r"\t",charCount.get(i,' '),
                           charCount.get(code[i],' '),chr(code[i]),code[i],)
  elif code[i] == 10:
    print strFormat.format(k,
                           i,chr(i),charCount.get(i,' '),
                           charCount.get(code[i],' '),r"\n",code[i])
  elif code[i] == 9:
    print strFormat.format(k,
                           i,chr(i),charCount.get(i,' '),
                           charCount.get(code[i],' '),r"\t",code[i])
  else:
    print strFormat.format(k,
                           i,chr(i),charCount.get(i,' '),
                           charCount.get(code[i],' '),chr(code[i]),code[i],)
  k += 1

"""
print 'Sorted Character Dictionary:'
print '{0:>5} --> {1:>5} == {2:>5} --> {3:>5} :: {4:>5} --> {5:>5}'.format(
                                'Ord','Char','Ord','Char','cin','cout')
for i in keyssort:
  if i == 10:
    print '{0:>5} --> {1:>5} == {2:>5} --> {3:>5} :: {4:>5} --> {5:>5}'.format(
          i,r"'\n'",code[i],
          "'" + chr(code[i]) + "'",
          charCount[i],charCount[code[i]])
  elif i == 9:
    print '{0:>5} --> {1:>5} == {2:>5} --> {3:>5} :: {4:>5} --> {5:>5}'.format(
          i,r"'\t'",code[i],
          "'" + chr(code[i]) + "'",
          charCount[i],charCount[code[i]])
  elif code[i] == 10:
    print '{0:>5} --> {1:>5} == {2:>5} --> {3:>5} :: {4:>5} --> {5:>5}'.format(
          i,"'" + chr(i) + "'",
          code[i],r"'\n'",
          charCount[i],charCount[code[i]])
  elif code[i] == 9:
    print '{0:>5} --> {1:>5} == {2:>5} --> {3:>5} :: {4:>5} --> {5:>5}'.format(
          i,"'" + chr(i) + "'",
          code[i],r"'\t'",
          charCount[i],charCount[code[i]])
  else:
    print '{0:>5} --> {1:>5} == {2:>5} --> {3:>5} :: {4:>5} --> {5:>5}'.format(
          i,"'" + chr(i) + "'",
          code[i],"'" + chr(code[i]) + "'",
          charCount[i],charCount[code[i]])
"""

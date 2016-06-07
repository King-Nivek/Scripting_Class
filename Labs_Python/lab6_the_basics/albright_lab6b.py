#!/usr/bin/python

'''_____________________________________________________________________________
'
'     Created By:  Kevin M. Albright
'  Creation Date:  03.24.2014
'
'    Modified By:  Kevin M. Albright
'  Last Modified:  03.30.2014
'
'     Assignment:  Lab6b
'      File Name:  albright_lab6b.py
'           From:  Exploring Python p. 42 q. 21
'        Purpose:  This script is to read in a word and print out the number
'                    of letters, vowels, and the percentage or vowels 
'                    contained in the word.  And the number of consonants.
_____________________________________________________________________________'''

vowels = 'aeiou'
num_vowels = 0
input = str.lower(raw_input('Enter a word: '))
for i in range(0, len(input)):
	for k in range(0, len(vowels)):
		if input[i] == vowels[k]:
			num_vowels += 1
print 'Letters: ', len(input)
print 'Vowels: ', num_vowels 
print 'Consonants: ', abs(num_vowels - len(input))
print 'Percentage of vowels: {0:.2%}'.format(float(num_vowels) / len(input))

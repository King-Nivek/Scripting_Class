#!/usr/bin/python

'''_____________________________________________________________________________
'
'     Created By:  Kevin M. Albright
'  Creation Date:  03.24.2014
'
'    Modified By:  Kevin M. Albright
'  Last Modified:  03.30.2014
'
'     Assignment:  Lab6a
'      File Name:  albright_lab6a.py
'           From:  Exploring Python p. 41 q. #7
'        Purpose:  This script is to print out all Pythagorean triples 
'                    consisting of positive integers less then or equal to 20.
_____________________________________________________________________________'''
count = 0
for a in range(1,21):
	for b in range(1,21):
		for c in range(1,21):
			if (a**2 + b**2 == c**2):
				count += 1
				print '{0:>2}). ({1:>2},{2:>3},{3:>3})'.format(count, a, b, c)

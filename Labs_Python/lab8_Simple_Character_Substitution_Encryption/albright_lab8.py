#!/usr/bin/python
'''_____________________________________________________________________________
'
'     Created By:  Kevin M. Albright
'  Creation Date:  04.13.2014
'
'    Modified By:  Kevin M. Albright
'  Last Modified:  04.14.2014
'
'     Assignment:  Lab8
'      File Name:  albright_lab8.py
'        Purpose:  This program will 
'                    (1) Open and read in the contents of provided file name.
'                    (2) Using a dictionary write out to another file the 
'                         values matching keys in the dictionary character by 
'                         character.
'                  The program will check that the provided file name is a
'                    valid file, if invalid will print a message and exit.
'                  If no arguments are provided, will print out instructions on
'                    how to use program.
'                  The user can provide the flag "-d" to have the program
'                    decrypt the provided file.
'                  Encrypted files are named "encrypted_" + filename
'                  Decrypted files are named "decrypted_" + filename
'                    Decrypting will remove "encrypted_" from filename when
'                    making decrypted filename.
'                  Files writen are located in programs directory.
'                  Dictionary keys and values are stored as the ASCII code
'                    values.
_____________________________________________________________________________'''

#from random import sample   ##  Prevusly used to create the First iteration of
                             ##    random values. Tweaked this to get final
                             ##    values used.
from sys import argv
from os.path import isfile   ##  for File checks.
from os.path import basename ##  for file name from path.
from string import lower
from string import replace

#||||  Check input arguments.
if len(argv) == 1:  ##  No arguments prints Instuctions
  print '\n____  To use this script:'
  print '              ./albright_lab8.py filename [-d]'
  print '    Encrypt:  ./albright_lab8.py text.txt'
  print '    Decrypt:  ./albright_lab8.py encrypted_text.txt -d'
  print '       Flag: -d for decryption'
  print '      No flag for encryption.\n'
  exit()
elif len(argv) > 1:        ##  If arguments given.
  if not isfile(argv[1]):  ##  Check for valid file.
    print '\n>>>>>>>  Invalid file.  Please enter a valid file name.\n'
    exit()
  elif len(argv) == 3:     ##  If flag given
    if lower(argv[2]) != '-d':
      print '\n>>>>>>>  Invalid flag.  Please enter -d for decript.'
      print '                          And no flag for encrypt.\n'
      exit()
  elif len(argv) > 3:      ##  If too many argumetns.
    print '\n>>>>>>>  Invalid.  To many input arguments.\n'
    exit()

#||||  Open files, Name Encrypt file or Decrypt file.
fin = open(argv[1])                                   ##  Open input file.
if len(argv) == 3 and argv[2].lower() == '-d':        ##  Create decrypt file.
  fout = open('decrypted_' + replace(basename(argv[1]),'encrypted_','',1),"w")
else:                                                 ##  Create encrypt file.
  fout = open('encrypted_' + basename(argv[1]),"w")

keys = [9,10] + range(32,127)  ##  Create character keys as ordinals.
#sample(keys,len(keys))        ##  Old random values maker.
##  Make values for keys.
values = [80,90,86,48,102,46,40,62,71,83,115,43,44,69,101,39,59,99,54,67,100,118,105,33,42,119,88,91,114,109,96,37,79,97,116,55,65,56,125,75,52,111,112,77,103,123,87,10,94,81,76,49,104,68,9,64,57,93,73,60,120,38,70,85,82,89,63,34,110,36,84,113,66,78,108,47,41,61,117,45,58,126,53,92,72,50,124,51,98,122,32,106,74,95,35,107,121] 

if len(argv) == 3 and argv[2].lower() == '-d':  ## Decrypt dictionary.
  code = dict(zip(values,keys))
else:                                           ##  Encrypt dictionary.
  code = dict(zip(keys,values))

input = fin.read()  ##  Read file.
for char in input:
  if code.has_key(ord(char)):  ##  If code has key print value as char.
    fout.write(chr(code[ord(char)]))
  else:                        ##  Else just reprint char from file.
    fout.write(char)
fout.close()
fin.close()

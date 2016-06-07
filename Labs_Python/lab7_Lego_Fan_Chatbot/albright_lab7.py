#!/usr/bin/python
#'''''''10''''''''20''''''''30''''''''40''''''''50''''''''60''''''''70''''''''80
'''_____________________________________________________________________________
'
'     Created By:  Kevin M. Albright
'  Creation Date:  04.04.2014
'
'    Modified By:  Kevin M. Albright
'  Last Modified:  04.09.2014
'
'     Assignment:  Lab7
'      File Name:  albright_lab7.py
'        Purpose:  This program's theme is to emulate an Adult fan of Lego.
'                    This will give Lego set responses and questions.  
'                    Mostly talk is centered around sets and building.
'                    Not yet implemented is questions and responses about
'                    greeble and amount of Lego owned.
_____________________________________________________________________________'''

import re
import string
from random import choice as rChoice

#::::  Variables
#///////////////////////////////////////
response = ''
bot_name = rChoice(['William','Bob','Joe','Doug','Kevin','Tom','Dr. Core'])
user_name = '???'

#----  Dictionary to hold dictionaries of remarks/sentences.
#///////////////////////////////////////
remarks = {
  'RESPONSES':			{  ##  Layer 1

'SETS':       {  ##  Layer 1.1
1:  'I like to build space themed Lego sets the best.',
2:  'I also like castle sets.',
3:  'And I like pirate sets too.',
							},

'GREEBLE':		{  ##  Layer 1.2
1: ('Greeble is the making of details on things like space ships which\n'
	+ '{0:>14}serves no function except to make it look cooler.\n'.format(' ')
	+ '{0:>14}an example would be the death star in star wars.'.format(' ')),
2: ('But, the star wars sets are some of the best sets on the\n'
	+ '{0:>14}market right now.').format(' '),
3:  'No, we are talking about Lego bricks not star wars.',
							},

'AMOUNT':			{  ##  Layer 1.3
1:  'Wow! that is not much Lego.',
2:  'Wow! that is a lot of Lego.',
3: ('I have not weighed my Lego in a while but I know that I\n'
	+ '{0:>14}have over one hundred pounds of Lego bricks.'.format(' ')),
							},

'BUILD':			{  ##  Layer 1.4
1: ('I usually start trying to build one thing but by the time I finish\n'
	+ '{0:>14}it is usually some thing completely different.'.format(' ')),
2: ('Well, one time I was making a gun turrent but when I\n'
	+ '{0:>14}"finished" it it was a space ship.').format(' '),
							},

'HAPPY':			{  ##  Layer 1.5
1:  'I like Legos, no I love Legos!  They are just awesome!',
2:  'You can say that again.',
							},

'NEGATIVE':		{  ##  Layer 1.6
1:  'What why are you saying that?',
2: ("Whoah! you can't change the topic.  There is only one\n"
	+ "{0:>14}topic to talk about, Legos!".format(' ')),
              },
										},
  'QUESTIONS':			{  ##  Layer 2

'SETS':				{  ##  Layer 2.1
1:  'What kind of sets do you like best?',
2:  'What kind of sets do you like second best?',
							},

'GREEBLE':		{  ##  Layer 2.2
1:  'Do you like greeble?',
2:  'Do you know what greeble is?',
							},

'AMOUNT':			{  ##  Layer 2.3
1:  'How much Lego do you own?',
							},

'BUILD':			{  ##  Layer 2.4
1:  'Do you like building with Lego Bricks?',
2:  'Do you make a plan before building or do you just wing it?',
3:  'What do you like to build?',
4:  'Do you find yourself buying sets just for the parts in them?',
							},

'HAPPY':			{  ##  Layer 2.5
1:  'Why do you like Lego bricks?',
							},

'NEGATIVE':		{  ##  Layer 2.6
1:  'Why do you not like Lego bricks?',
							},
										},

	'NOT_BOT':				{  ##  Layer 3

'NOT_BOT_SUB':{  ##  Layer 3.1
1:  'No, I am not a bot, nor am I a chatbot.',
2: ("Would a chatbot own over a hundred pounds of Lego?  No, I don't\n"
	+ '{0:>14}think so!'.format(' ')),
3: ("I think you're a chatbot, for I know very well that I am of flesh\n"
	+ "{0:>14}and blood!".format(' ')),
							},										
										},
          }
'''
print 'remarks:'
for type in remarks:
  print '  ||  ' + type + ':'
  for category in remarks[type]:
    print '    ||  ' + category + ':'
    for key in remarks[type][category]:
      print '{0:>12}{1:1}'.format(' ', remarks[type][category][key])
    print '    __'
  print '  __'
print '__'
'''

#||||  Search Patterns
#///////////////////////////////////////

#||||  Search for if user is asking a question
wrds_questions = ('what','when','where','which','who','whom','whose','why',
                  "why don't",'how',r'how\ far',r'how\ long',r'how\ many',
                  r'how\ much',r'how\ old',r'how\ come',r'do\ you\ like',)

wrds_bots = ('bots?','chatbots?',r'chat\ bots?',)
wrds_sets = ('space','castle','pirate','sets?','themes?')
wrds_greeble = ('greeble',r'star\ wars',r'death\ star',)
wrds_build = ('build','built','building','make','making','plans?','planning',
              'designs?',)
wrds_amount = ('lots','pounds?','lbs?',r'\d{2,}','couple','two','some',
              r'not\ much',r'a?\ ?few',r'\d{1}',)
wrds_happy = ('like',"love'?s?",'wow','cool','awesome','spectacular','fun',)
wrds_negative = ('no',r'do\ not\ like',r"don't\ like",)
wrds_response = ('space','castle','pirate','sets?','themes?','greeble',r'star\ wars',r'death\ star','build','built','building','make','making','plans?','planning','designs?','lots','pounds?','lbs?',r'\d{2,}','couple','two','some',r'not\ much',r'a?\ ?few',r'\d{1}','like',"love'?s?",'wow','cool','awesome','spectacular','fun','no',r'do\ not\ like',r"don't\ like",)


tags = (r"""((?:\d{2,}|\d{1})|a\ few|awesome|best\ sets|bot|bots|bought|build|building|built|buy|buying|castle|chat\ bot|chatbot|cool|couple|death\ star|design|do\ not\ like|do\ you\ like|don't\ like|finished|fun|greeble|gun\ turrent|have|how|how\ come|how\ far|how\ long|how\ many|how\ much|how\ old|lbs|lego|like|like\ lego|lots|love|love\ lego|make|making|many|moc\ fodder|no|not|not\ much|not\ star\ wars|own|pirate|plan|planning|plans|pounds|sets|sets\ for\ parts|some|space|space\ ship|spectacular|star\ wars|themes|two|what|what\ greeble|when|where|which|who|whom|whose|why|why\ don't|wow)""")


#---- Helper Functions
#///////////////////////////////////////
def get_input(user_name):
  return raw_input(user_name)

def search_input(input, grp_words):
  srch_input = string.lower(input)
  srch_pattern = re.compile(grp_words, re.VERBOSE)
  match = srch_pattern.search(srch_input)
  return match

def findall(input, grp_words):
	srch_input = string.lower(input)
	srch_pattern = re.compile(grp_words, re.VERBOSE)
	found = set(srch_pattern.findall(srch_input))
	return found

def print_responses(bot_name, user_name, response):
  input = get_input('{0:<12}{1:1}\n'.format(bot_name + ': ', response)
  								+ '{0:<12}'.format(user_name + ': '))
  return input

def exit_check(bot_name, input):
  if input == 'quit':
    output = rChoice(['Goodbye.','Farewell.','Talk to you later.',
                      'Have a good day.','Goodbye my friend.'])
    print ('{0:<12}{1:1}\n'.format(bot_name + ': ', output))
    exit()

def is_true(wrds_found, pattern_list):
  count = 0
  #i = 0
  for pttrn in pattern_list:
    for wrds in wrds_found:
      #print 'wrds: ' + wrds
      #print 'pttrn: ' + pttrn
      match = search_input(wrds, pttrn)
      #i += 1
      #print 'match: ' + str(i) + ': ' + str(bool(match))
      
      if match:
        #temp = raw_input(':')
        count += 1
        #print 'count: ' + str(count)
  #print 'return count: ' + str(count)
  return count

#----  Main Section
#///////////////////////////////////////

print('\n\n--INFO--\n'
    + 'To exit type "quit".\n\n')

#||||  Say name. get user's name.
input = print_responses(bot_name,user_name, ('Hi my name is ' + bot_name + '.  '
                                           + "What is you're name?"))

exit_check(bot_name, input)
user_name = input


#||||  Conversation start
response = 'Do you like Lego?'
input = print_responses(bot_name, user_name, response)
exit_check(bot_name, input)

#||||  Initial question answer check
mtch_yes = search_input(input, r'yes')
mtch_no = search_input(input, r'no')

if mtch_yes:
  response = remarks['RESPONSES']['HAPPY'][1]
elif mtch_no:
  response = remarks['RESPONSES']['NEGATIVE'][1]

input = print_responses(bot_name, user_name, response)
exit_check(bot_name, input)

#||||  Loop to respond and get input.
while input != 'quit':
  W_BOT = 0
  W_QUESTION = 1
  W_RESPONSE = 2
  W_SETS = 3
  W_BUILD = 4
  W_GREEBLE =5
  W_AMOUNT = 6
  W_HAPPY = 7
  W_NEGATIVE = 8
  #         [0,1,2,3,4,5,6,7,8]
  weights = [0,0,0,0,0,0,0,0,0]
  #||||  selections
  wrds_found = findall(input, tags)
  weights[W_BOT] = is_true(wrds_found, wrds_bots)
  weights[W_QUESTION] = is_true(wrds_found, wrds_questions)
  #weights[W_RESPONSE] = is_true(wrds_found, wrds_response)
  weights[W_SETS] = is_true(wrds_found, wrds_sets)
  weights[W_BUILD] = is_true(wrds_found, wrds_build)
  #weights[W_GREEBLE] = is_true(wrds_found, wrds_greeble)
  weights[W_AMOUNT] = is_true(wrds_found, wrds_amount)
  weights[W_HAPPY] = is_true(wrds_found, wrds_happy)
  weights[W_NEGATIVE] = is_true(wrds_found, wrds_negative)

  if weights[W_BOT] > 0:
    random = rChoice(remarks['NOT_BOT']['NOT_BOT_SUB'].keys())
    response = remarks['NOT_BOT']['NOT_BOT_SUB'][random]
  elif weights[W_QUESTION] == 0:
    if weights[W_SETS] > 0:
      random = rChoice(remarks['QUESTIONS']['SETS'].keys())
      response = remarks['QUESTIONS']['SETS'][random]
    elif weights[W_BUILD] > 0:
      random = rChoice(remarks['QUESTIONS']['BUILD'].keys())
      response = remarks['QUESTIONS']['BUILD'][random]
    #elif weights[W_GREEBLE] > 0:
      #if greeble 1 not used:
       # response = remarks['QUESTIONS']['GREEBLE'][1]
      #else:
       # response = remarks['QUESTIONS']['GREEBLE'][2]
    elif weights[W_AMOUNT] > 0:
			random = rChoice(remarks['QUESTIONS']['AMOUNT'].keys())
			response = remarks['QUESTIONS']['AMOUNT'][random]
    elif weights[W_HAPPY] > 0:
      random = rChoice(remarks['QUESTIONS']['HAPPY'].keys())
      response = remarks['QUESTIONS']['HAPPY'][random]
    elif weights[W_NEGATIVE] > 0:
      random = rChoice(remarks['QUESTIONS']['NEGATIVE'].keys())
      response = remarks['QUESTIONS']['NEGATIVE'][random]
    else:
      pass
  else: #response:
    if weights[W_SETS] > 0:
      if search_input(input, 'space'):
        response = remarks['RESPONSES']['SETS'][1]
      elif search_input(input, 'castle'):
        response = remarks['RESPONSES']['SETS'][2]
      elif search_input(input, 'pirate'):
        response = remarks['RESPONSES']['SETS'][3]
      else:
        random = rChoice(remarks['RESPONSES']['SETS'].keys())
        response = remarks['RESPONSES']['SETS'][random]
    elif weights[W_BUILD] > 0:
      random = rChoice(remarks['RESPONSES']['BUILD'].keys())
      response = remarks['RESPONSES']['BUILD'][random]
    #elif weights[W_GREEBLE] > 0:
    #	if greeble 1 not used:
    #	  response = remarks['RESPONSES']['GREEBLE'][1]
    #	else:
    #	  response = remarks['RESPONSES']['GREEBLE'][1]
    #elif weights[W_AMOUNT] > 0:
    #	if amount low:
    #	  response = remarks['RESPONSES']['AMOUNT'][1]
    #	elif amount high:
    #	  response = remarks['RESPONSES']['AMOUNT'][1]
    #	else:
    #	  response = remarks['RESPONSES']['AMOUNT'][3]
    elif weights[W_HAPPY] > 0:
      random = rChoice(remarks['RESPONSES']['HAPPY'].keys())
      response = remarks['RESPONSES']['HAPPY'][random]
    elif weights[W_NEGATIVE] > 0:
      random = rChoice(remarks['RESPONSES']['NEGATIVE'].keys())
      response = remarks['RESPONSES']['NEGATIVE'][random]
    
  if max(weights) is 0:
    rand1 = rChoice(remarks['RESPONSES'].keys())
    rand2 = rChoice(remarks['RESPONSES'][rand1].keys())
    response = remarks['RESPONSES'][rand1][rand2]

  input = print_responses(bot_name, user_name, response)
#||||  Random any response
'''
  rand1 = rChoice(remarks['RESPONSES'].keys())
  rand2 = rChoice(remarks['RESPONSES'][rand1].keys())
  response = remarks['RESPONSES'][rand1][rand2]
'''
exit_check(bot_name, input)

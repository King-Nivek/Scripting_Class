#!/usr/bin/python
#'''''''10''''''''20''''''''30''''''''40''''''''50''''''''60''''''''70''''''''80
'''_____________________________________________________________________________
'
'     Created By:  Kevin M. Albright
'  Creation Date:  03.24.2014
'
'    Modified By:  Kevin M. Albright
'  Last Modified:  03.30.2014
'
'     Assignment:  Lab6c
'      File Name:  albright_lab6c.py
'           From:  Exploring Python p. 43 q. #24
'        Purpose:  This program is the game of Craps, which is a dice game.
'                    The game will allow you to start a new game or exit.
'                    If you start a game the first roll will occur.  Then
'                    you will either win, lose or mark point and continue to
'                    roll till you win or lose.  You can use the enter key,
'                    y, or Y for affirmative responses and n or N for negative
'                    responses.  The instructions in the game are written into
'                    the program so I will not repeat them here.
_____________________________________________________________________________'''

'''
'  Function die_roll
'  
'  Uses random.randint() function to generate a random integer [1-6]
'    simulating a die being rolled.
'  Pass in nothing.
'  Returns an integer.
'''
def die_roll():
  import random
  MIN = 1
  MAX = 6
  return random.randint(MIN, MAX)

'''
'  Function rolling_dice
'
'  Simulates the rolling of a pair of dice.  Also, tallies the two dice
'    together, and adds one to rolls.
'  Pass in rolls:int
'  Returns [die1, die2, tally]:list and rolls:int
'''
def rolling_dice(rolls):
  die1 = die_roll()
  die2 = die_roll()
  tally = die1 + die2
  rolls += 1
  return [die1, die2, tally], rolls

'''
'  Function first_roll_check
'
'  Checks the first roll of a round whether the user wins with a [7,11]
'    loses with [2,3,12], or point is on with [4,5,6,8,9,10].  Will return a
'    1 for wins, -1 for loses, and 0 for point on.  Checks start of -2 is 
'    arbitrary, just to be a valid integer but invalid to the checkers later on.
'  Pass in tally:int
'  Returns check:int and mark_point:int
'''
def first_roll_check(tally):
  check = -2
  mark_point = 0
  for win in [7,11]:
    if tally == win:
      check = 1
  for lose in [2,3,12]:
    if tally == lose:
      check = -1
  for point_on in [4,5,6,8,9,10]:
    if tally == point_on:
      check = 0
      mark_point = tally
  return check, mark_point

'''
'  Function mark_point_check
'
'  Used to check all rolls in a round except the first.  Checks if user rolled
'    a 7 and thus loses the round, if they rolled the mark_point and win the
'    round, or if the rolled some other number thus continuing the round.
'  Pass in mark_point:int and tally:int
'''
def mark_point_check(mark_point, tally):
  if tally == 7:
    return -1
  elif tally == mark_point:
    return 1
  else:
    return 0

'''
'  Function get_input
'
'  Gets input from the user.  Displays the output string and returns an
'    uppercase string.
'  Pass in output:string
'  Returns an upper case string
'''
def get_input(output):
  return str.upper(raw_input(output))

'''
'  Function print_out
'
'  Print passed in output string.
'  Pass in output:string
'  Returns nothing
'''
def print_out(output):
  print output

'''
'  Function is_valid
'
'  Checks the input for validity.  Input needs to be a 'Y', 'N', or ''.
'    Returns the input if it is valid, otherwise it will return a '1' which
'    will make loop using this function need to loop around again.
'  Pass in input:string/char
'  Returns input:string/char or '1':string/char
'''
def is_valid(input):
  if input == 'Y' or input == 'N' or input == '':
    return input
  else:
    print_out('>>>>>>>  Invalid Input.  Please enter a y or n for yes or no.\n')
    return '1'

'''
'  Function is_win
'
'  Check if the user won, lost, or continues.  If user wins prints out win and
'    the score, updates points and rounds, and resets rolls to 0.  If user lost
'    prints out lost and the score, resets rolls, and updates rounds.
'  Pass in check:int, points:int, rolls:int, and rounds:int
'  Returns check:int, points:int, rolls:int, and rounds:int
'''
def is_win(check, points, rolls, rounds):
  if check > 0:
    rolls = 0
    points += 1
    rounds += 1
    print_out('')
    print_out('    You Won!')
    print_out('    Score: {0:3>}\n'.format(points))

  elif check < 0:
    rolls = 0
    rounds += 1
    print_out('')
    print_out('    You Lost.')
    print_out('    Score: {0:3>}\n'.format(points))

  else:
    pass
  return check, points, rolls, rounds

'''
'  Function print_dice_roll
'
'  Prints out the dice roll.  Prints the individual die roll and their sum.
'  Pass in dice_group:list, rolls:int
'''
def print_dice_roll(dice_group, rolls):
  DIE1, DIE2, TALLY = 0, 1, 2
  print_out('     Roll: {0:>3}\n'.format(rolls)
          + '       ({0:>1}, {1:>1}) --> {2:>2}'.format(dice_group[DIE1],
                                                        dice_group[DIE2],
                                                        dice_group[TALLY]))

'''
'  Function gameplay
'
'  The main code of a single game.  Holding variables for the function of 
'    the game and loops to go through rolls for making point and if the user 
'    wants to play continue playing the game.
'  Pass in nothing
'  Returns a '1' to support the loop in the calling function/code
'''
def gameplay():
  #  Constants
  DIE1, DIE2, TALLY = 0, 1, 2
  #  Variables
  input = 'Y'
  dice_group = ['tmp1','tmp2','tmp3']
  rolls = 0
  points = 0
  mark_point = 0
  check = -2
  rounds = 1
  
  while input == 'Y' or input == '': # Loops around each round.
    print_out('--  Round: {0:>3}'.format(rounds))
    dice_group, rolls = rolling_dice(rolls)
    print_dice_roll(dice_group, rolls)
    check, mark_point = first_roll_check(dice_group[TALLY])
    check, points, rolls, rounds = is_win(check, points, rolls, rounds)
    if check == 0:
      print_out('\n--> Mark point is: {0:3>}\n'.format(mark_point))
    while check == 0: # Loops around a point mark till it is resolved.
      temp = get_input('Continue: ')
      print_out('')
      dice_group, rolls = rolling_dice(rolls)
      print_dice_roll(dice_group, rolls)
      check =  mark_point_check(mark_point, dice_group[TALLY])
      check, points, rolls, rounds = is_win(check, points, rolls, rounds)
    if check != 0:
      input = '1'
      while not(input == 'Y' or input == 'N' or input == ''): # input check.
        input = get_input('----  Do you want start a new round?' 
                        + ' (y or enter/n): ')
        print_out('')
        input = is_valid(input)
        if input == 'N': # if exiting this game, do this.
          rounds -= 1
          print_out('--> Rounds: {0:>3}\n'.format(rounds)
                  + '    Wins:   {0:>3}\n'.format(points)
                  + '    Lost:   {0:>3}\n'.format(rounds - points)
                  + '    Win %:  {0:>7.2%}\n'.format(float(points) / rounds))
          return '1'

'''
'  Start of Program
'
'  Give introduction to user and then instructions on how to play
'    the game.  Is the outer most loop to exit out of the program
'    cleanly.  
'''
print_out("""
----        Welcome to the dice game Craps!

    The name of the game is Craps.  The rules of the game are:
    A).  On your first roll of a round:  If you roll a
      1).  seven(7) or an eleven(11) you score and win the round.
      2).  two(2), three(3), or a twelve(12) you lose the round.
      3).  four(4), five(5), six(6), eight(8), nine(9), or ten(10)
             point is on and you must continue to roll.
    B).  On continued rounds:  If point is on and roll a
      1).  the point on number  again, you win the round.
      2).  seven(7) you lose the round.
      3).  any other number, roll again.

    You may play multiple rounds per a game, or you may start a 
      new game from the main menu, thus resetting your scores
      without exiting the program.

    Yes and No questions can be answered:
    1).  y or Y or press the enter key for affirmative responses.
    2).  n or N for negative responses.
""")

input = '1'
while not(input == 'Y' or input == 'N' or input == ''):
  input = get_input('    Start a new game? (y or enter/n): ')
  print_out('')
  input = is_valid(input)
  if input == 'Y' or input == '':
    input = gameplay()

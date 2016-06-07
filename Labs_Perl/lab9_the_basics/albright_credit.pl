#!/usr/bin/perl
#_______________________________________________________________________________
#
#     Created By:  Kevin M. Albright
#  Creation Date:  04.21.2014
#
#    Modified By:  Kevin M. Albright
#  Last Modified:  04.26.2014
#
#     Assignment:  Lab9
#      File Name:  albright_credit.pl
#        Purpose:  This program ask the user to input a 16 digit credit card
#                    number.  The script will not except input with to few
#                    digits or to many digits.  The user may use dashes or
#                    spaces to seperate digits into groups of four, or the
#                    user may enter the sequence with spaces, dashes, and
#                    neither so long as when they do use dashes or spaces, 
#                    they are separating a 4th digit from a 5th digit.  The
#                    script will then print out the sequence with four digits
#                    to a line.
#_______________________________________________________________________________

print 'Please enter your credit card number: '; # Instructions
chomp($input = <>); # Get input
# Input search pattern
if ($input =~ /^(?:(\d{4})(?:-| )?(\d{4})(?:-| )?(\d{4})(?:-| )?(\d{4}))$/){
  print "$1\n$2\n$3\n$4\n"; # Print out capture groups, each on their own line.
} else { # Print out invalid input if pattern is not matched.
  print "\n>>>>>>>  Invalid input please try again.\n";
  print "           Good bye.\n\n";
}

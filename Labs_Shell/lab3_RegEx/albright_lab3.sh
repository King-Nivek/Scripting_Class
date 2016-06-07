#!/bin/sh
#_______________________________________________________________________________
#     Created By:  Kevin M. Albright
#  Creation Date:  02.10.2014
#
#    Modified By:  Kevin M. Albright
#  Last Modified:  02.16.2014
#
#     Assignment:  Lab3
#      File Name:  albright_lab3.sh
#        Purpose:  To except input arguments of -e or -p and also a file name.
#                    The -e will have the script scan the file for email 
#                    addresses and the -p will have the script scan for phone 
#                    number in the file.  After scanning the file the script
#                    will print to the screen the email addresses or the phone
#                    numbers depending on what it was searching for.  Also, if
#                    the script is given invalid arguments an error message
#                    will be displayed.  The error shows an example of how to
#                    use the script properly and what two flags are excepted
#                    and what the flag will do.
#_______________________________________________________________________________

#  Checks to see if it was given two null strings.  If either one is null an
#    error message is printed to screen. Otherwise it will go to the else.
if !([ "$1" ] && [ "$2" ]); then
		echo
		echo 
		echo ">>>>>>>    Invalid input! Please enter parameters correctly."
		echo "           Example: ./albright_lab3.sh [flag] [filename]"
		echo "           Valid flags are:"
		echo "               -e, To search for Email addresses."
		echo "               -p, To search for Phone numbers."	
		echo
else	
  #  Switch checks that either -e or -p is in argument 1's spot to be used to
  #    display the proper results.
	case $1 in
    #  Scans for email addresses. Example: firstName.lastName@company.com
		-e)
				echo
				echo
				echo "Email Addresses:"
				echo "------------------------------"
				egrep -o "([a-zA-Z0-9\.\-\_]+)+(@)([a-zA-Z0-9]+)+(\.)([a-z]{3}\>)" $2
				echo "------------------------------End of File"
				echo
				;;

    #  Scans for phone numbers. It will find numbers of these two patterns:
    #    1).  (865)123-4567
    #    2).  865-123-4567
		-p) 
				echo
				echo
				echo "Phone Numbers:"
				echo "------------------------------"
				egrep -o "(\([0-9]+\)|[0-9]+\-)+([0-9]+\-)+([0-9]+)" $2
				echo "------------------------------End of File"
				echo
				;;

     #  An error message if -e or -p was not given as an argument.
		 *) 
				echo
				echo
				echo ">>>>>>>    Invalid input! Please enter parameters correctly."
				echo "           Example: ./albright_lab3.sh [flag] [filename]"
				echo "           Valid flags are:"
				echo "               -e, To search for Email addresses."
				echo "               -p, To search for Phone numbers."	
				echo
				;;
	esac
fi

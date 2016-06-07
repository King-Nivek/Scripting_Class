#!/bin/sh

#_______________________________________________________________________________
#     Created By:  Kevin M. Albright
#  Creation Date:  01.28.2014
#
#    Modified By:  Kevin M. Albright
#  Last Modified:  01.27.2014
#
#     Assignment:  Lab1
#      File Name:  albright_lab1.sh
#        Purpose:  To print out the current Directory,
#						         contents of that directory, the 
#						         processes currently running here,
#						         and the User's currently logged in
#						         and what their current activity is.
#_______________________________________________________________________________


echo
echo "Hello World! This is Kevin's first script."
echo "Quick summary of the current state:"
echo
echo "1) current directory:"
pwd
echo
echo "2) contents of current directory (including permissions):"
ls -l
echo
echo "3) prosses currently running here:"
ps
echo
echo "4) users curently logged on and their activity:"
w
echo

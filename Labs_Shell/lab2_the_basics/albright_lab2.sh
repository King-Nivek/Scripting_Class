#!/bin/sh

#_______________________________________________________________________________
#     Created By:  Kevin M. Albright
#  Creation Date:  02.03.2014
#
#    Modified By:  Kevin M. Albright
#  Last Modified:  02.08.2014
#
#     Assignment:  Lab2
#      File Name:  albright_lab2.sh
#        Purpose:  1).  To print out the total number of bytes taken up by all
#                    of the files in the current directory.
#                  2).  Determine and print out how many files in the current
#                    directory have read, write and execute permissions.
#                  3).  Estimate the number of shell scripts are in the current
#                    directory. A shell script will be defined as a text file
#                    that begins with "#!/bin/sh".
#_______________________________________________________________________________

#  Variables
#/////////////////
reads=0
writes=0
executes=0
totalBytes=0
fileSize=0
KB=0

#  A loop to find and add up the bytes of each 
#    file in the current directory.  Also to
#    count each file the has read, write, and
#    execute permissions.
#//////////////////////////////////////////////
for fileName in *
do
 	#  Counts bytes and add them up
	fileSize=$(wc -c < "$fileName")
	totalBytes=$(($totalBytes+$fileSize))

  #  Counts read permissions
	if [ -r $fileName ] ; then
		reads=$(($reads + 1))
	fi

  #  Counts write permissions
	if [ -w $fileName ] ; then
		writes=$(($writes+1))
	fi

  #  Counts execute permissions
	if [ -x $fileName ] ; then
		executes=$(($executes+1))
	fi

done

#  Figures a rounded amount of kilobytes from the 
#    the total number of bytes.
KB=$((totalBytes / 1024))

#  Prints out all the info to the screen.
#///////////////////////////////////////////
echo
echo
echo "Total size of all files in this directory: $totalBytes bytes (~$KB KB)."
echo "$reads of the files have read permissions."
echo "$writes of the files have write permissions."
echo "$executes of the files have execute permissions."
echo -n "Estimated number of shell script files in this directory: "
grep -x "#\!\/bin\/sh" * | wc -l
echo

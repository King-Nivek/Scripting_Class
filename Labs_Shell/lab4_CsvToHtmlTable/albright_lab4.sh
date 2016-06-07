#!/bin/sh
#_______________________________________________________________________________
#     Created By:  Kevin M. Albright
#  Creation Date:  02.22.2014
#
#    Modified By:  Kevin M. Albright
#  Last Modified:  02.26.2014
#
#     Assignment:  Lab4
#      File Name:  albright_lab4.sh
#        Purpose:  To takes an input that is csv file which also has the data 
#                    fields contained within double quotes.  The Script can also
#                    be given up to three USA state abbreviations that are in 
#                    upper case. Example:
#                    TN TX AZ
#                    These abbreviations will be used to highlight the rows with
#                    that state in a persons data field.  The 1st will be red,
#                    the 2nd will be blue, and the 3rd will be green.  You can
#                    have the script highlight zero, one, two, or all three, so 
#                    all inputs need not be given.  The The script will then  
#                    makes a temp file called albright_lab4.tmp.  Creating  
#                    lines in it to set up the start to an html table.
#                    The script will then use sed to replace [","] with
#                    [</TD><TD>] after that we will insert at the start and end
#                    of each line [<TR><TD>"the data"</TD></TR>].  Also, before
#                    the script deals with the table data it will take the first
#                    line of input.csv and use that to create table headers in a
#                    similar way it makes the table rows and table data.  After
#                    that the script will add the ending lines to finish the
#                    html file.  With this fully working html file the script
#                    will then use sed to find the state rows and color them.
#                    The script will then remove the temp file.  The final
#                    will have a working html table.  Output goes to standard
#                    out, the user can then redirect this as they see fit.
#_______________________________________________________________________________

#  Check to see that there is an input file.
if !([ "$1" ]); then
	echo
	echo ">>>>>>>  No input file argument."
	echo "         Please provide an input file name."
	echo "         Format:  ./albright_lab4.html [File Name] [1st] [2nd] [3rd]"
	echo "         Example: ./albright_lab4.sh input.csv TN FL WY"
	echo "         1st, 2nd, and 3rd are optional arguments.  You can choose"
	echo "           to highlight one, two, or three states, the entire row for"
	echo "           that state will be highlighted. 1st is red, 2nd is blue, and"
	echo "           3rd is green."
	echo ">>>>>>>  Exiting now."
	echo
	exit
fi

#  Variables to check that there are two uppercase letters in the state
#    arguments.  And a variable to to see if the Script should exit or not.
first=$(echo "$2" | egrep -x "[A-Z]{2}" | wc -l)
second=$(echo "$3" | egrep -x "[A-Z]{2}" | wc -l)
third=$(echo "$4" | egrep -x "[A-Z]{2}" | wc -l)
exiting=0

#  Check if 1st state is used, and that two uppercase characters are being used.
if [ "$2" ] ; then 
	if !([ $first -eq 1 ]) ; then
		echo
		echo ">>>>>>>  First state input is invalid."
		exiting=1
	fi
fi
#  Check if 2nd state is used, and that two uppercase characters are being used.
if [ "$3" ] ; then 
	if !([ $second -eq 1 ]) ; then
		echo
		echo ">>>>>>>  Second state input is invalid."
		exiting=1
	fi
fi
#  Check if 3rd state is used, and that two uppercase characters are being used.
if [ "$4" ] ; then 
	if !([ $third -eq 1 ]) ; then
		echo
		echo ">>>>>>>  Third state input is invalid."
		exiting=1
	fi
fi
#  Prints out help to get state arguments in correctly.
if [ $exiting -eq 1 ] ; then
	echo
	echo "         Please use a proper state abbreviation, entering it in as"
	echo "           two uppercase characters, when using the optional state"
	echo "           arguments to highlight up to three rows.  User knowledge"
	echo "           of state abbreviations is assumed."
	echo ">>>>>>>  Exiting now." 
	echo
	exit
fi

#####  Setting up the html beginning.
########################################
echo "<!DOCTYPE HTML>" > albright_lab4.tmp
echo "  <HTML>" >> albright_lab4.tmp
#  Head Start 
echo "    <HEAD>" >> albright_lab4.tmp
#  Adding a title to the page
echo "      <TITLE>" >> albright_lab4.tmp
echo "        Lab 4 Table of Data" >> albright_lab4.tmp
echo "      </TITLE>" >> albright_lab4.tmp
#  Adding some style to the table so it looks nicer.
echo "      <STYLE>" >> albright_lab4.tmp
#  Make the table background a light gray.
echo "        TABLE" >> albright_lab4.tmp
echo "        {" >> albright_lab4.tmp
echo "        background-color:#CCCCCC;" >> albright_lab4.tmp
echo "        }" >> albright_lab4.tmp
#  Collapsing the border of the table so it is a single line.
#    Also setting the thickness of the border.
echo "        TABLE,TR,TH,TD" >> albright_lab4.tmp
echo "        {" >> albright_lab4.tmp
echo "        border:1px solid white;" >> albright_lab4.tmp
echo "        border-collapse:collapse;" >> albright_lab4.tmp
echo "        }" >> albright_lab4.tmp
#  Adding padding around the data that will be in the 
#    table headers and table data.
echo "        TH,TD" >> albright_lab4.tmp
echo "        {" >> albright_lab4.tmp
echo "        padding:5px;" >> albright_lab4.tmp
echo "        }" >> albright_lab4.tmp
echo "      </STYLE>" >> albright_lab4.tmp
echo "    </HEAD>" >> albright_lab4.tmp
#  Body Start
echo "    <BODY>" >> albright_lab4.tmp
#  Table Start
echo "      <TABLE>" >> albright_lab4.tmp

#####  Set up the Table headers.
########################################
#  Use first line only from input file.
#  Replace commas with header end and header start.
#  Add row start header start to the start of a line, and
#    add header end row end to the end of a line. Output to temp file.
sed -re '1!d' \
    -e 's;,;</TH><TH>;g' \
		-e 's;^.*$;<TR><TH>&</TH></TR>;' $1 >> albright_lab4.tmp

#####  Set up the Table data.
########################################
#  Use first line only from input file.
#  Replace "," with data end and data start.
#  Get rid of double quotes (which are now only at the 
#    start and end of each line)
#  Add row start data start to the start of a line, and
#    add data end row end to the end of a line. Output to temp file.
sed -re '1d' \
		-e 's;",";</TD><TD>;g' \
		-e 's;";;g' \
		-e 's;^.*$;<TR><TD>&</TD></TR>;' $1 >> albright_lab4.tmp

#####  Finish up html file.
########################################
#  End Table, Body and HTML tags.
echo "      </TABLE>" >> albright_lab4.tmp
echo "    </BODY>" >> albright_lab4.tmp
echo "  </HTML>" >> albright_lab4.tmp

#####  Find rows that are for the State of Tennessee.
#######################################################
#  Find start with <TR> then has several sections of <TD>"some data"</TD>
#    then has <TD>TN</TD> then several more sections with <TD>"some data"</TD>
#    and finally ends the line with </TR>.  When sed finds these rows it will 
#    replace it with <TR some style and colors>"and then what was captured in
#    group 1, this is repeated three times for each argument.  Which is 
#    everything but the first <TR>.  sed then outputs this to 
#    albright_lab4.html.
sed -re 's;^<TR>((<TD>.*</TD>)+<TD>'$2'</TD>(<TD>.*</TD>)</TR>)$;<TR style="background-color:#990000\; color:#FFFFFF\;">\1;' \
    -e 's;^<TR>((<TD>.*</TD>)+<TD>'$3'</TD>(<TD>.*</TD>)</TR>)$;<TR style="background-color:#000099\; color:#FFFFFF\;">\1;' \
	  -e 's;^<TR>((<TD>.*</TD>)+<TD>'$4'</TD>(<TD>.*</TD>)</TR>)$;<TR style="background-color:#006600\; color:#FFFFFF\;">\1;' albright_lab4.tmp 

#  Removes the temp file.
rm albright_lab4.tmp

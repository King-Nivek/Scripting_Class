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
#      File Name:  albright_words.pl
#        Purpose:  This program takes command line arguments(words to search
#                    for) and with these words searches the file input.txt for
#                    these words, counting the number of times the arg word is
#                    incountered in the input file.  When the search is done,
#                    the results will be printed to screen by count decending
#                    and same count words by alphabete. 
#_______________________________________________________________________________

open(FINP,"input.txt"); # Open file
@raw_data = <FINP>;     # read in file
close(FINP);            # close file

$str_inp = join("",@raw_data);  # join lines together
@tokens = split(/\W/,$str_inp); # split string on non-alphanumaric characters

for($i = 0; $i <= $#ARGV; $i++) {         # Loop through input args
  foreach $tokens(@tokens) {              # Loop through file words
    if(lc($tokens) =~ /\b$ARGV[$i]\b/i) { # If: matches file word to input arg
      $words{lc($ARGV[$i])} += 1;         # add to input arg count
    }#end if
  }#end foreach
}#end for

# Sort values of words, but stores in temp the keys for the sorted values
@sorted = reverse(sort {$words{$a} <=> $words{$b}} keys %words);

@indexs;
@sort_words;

# Sort equal value's keys
for($i = 0, $j = 1; $i < (scalar @sorted) -1; $i++, $j++) { 
  if($words{$sorted[$i]} == $words{$sorted[$j]}) { # if wordV == wordV + j
    $num = $words{$sorted[$i]};                    # store word value
    $k = $j + 1;                                   # store index + 1
    push(@indexs,$i,$j);                           # store index i and j
    while($words{$sorted[$i]} == $num) {           # while word value is same
      if($words{$sorted[$i]} == $words{$sorted[$k]}) { # if wordV == wordV + k
        push(@indexs,$k);                          # store index k
        $k++;                                      # add one to k
      } else {                                     # else change num value
        $num = $words{$sorted[$k]};
      }
    } # end while
    foreach $indexs(@indexs) {
      push(@sort_words,$sorted[$indexs]);        # store words from indexs
    }
    @sort_words = sort(@sort_words);             # Sort words that had == values
    for($n = 0; $n < scalar @sort_words; $n++) { # Change word in sorted to be
      $sorted[$indexs[$n]] = $sort_words[$n];    # a-z sorted for stored indexs
    }
    $i = pop(@indexs);   # Move i value up through already search values
    @indexs = undef;     # Clear saved indexes
    @sort_words = undef; # Clear saved same value words
  }
}

print "\n";
# Print out keys and values, decending values, equal values asendind key.
foreach $sorted(@sorted) {
  printf("%8s%s %2d\n",$sorted,":", $words{$sorted});
}
print "\n";

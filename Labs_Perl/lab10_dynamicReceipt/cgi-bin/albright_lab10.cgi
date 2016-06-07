#!/usr/bin/perl
#_______________________________________________________________________________
#
#     Created By:  Kevin M. Albright
#  Creation Date:  05.03.2014
#
#    Modified By:  Kevin M. Albright
#  Last Modified:  05.04.2014
#
#     Assignment:  Lab10
#      File Name:  albright_lab10.cgi
#        Purpose:  This program will dynamicaly generate a receipt page for 
#                    the albright_lab10.html page.
#_______________________________________________________________________________

use CGI;
$page = new CGI;
print $page->header;
print $page->start_html('Receipt Page');
print "<center>";
@type = $page->param('type');           ## Get chosen Ice cream flavor(s).
$street = $page->param('street');       ## Get Street address.
$phone = $page->param('phone');         ## Get Phone number.
@value;                                 ## Store Ice cream prices.
@strAmounts = ("Subtotal","Sales Tax"); ## Store Titles for table output.
@amounts;                               ## Store amount totals.

#### Eval variable are used to simplify the validity of input arguments.
#
## Check that at least 10 alphanumaic, horizontal spaces, and commas, periods,
#    and apostrophes are used in the street address.
$eval_street = $street !~ /^(?:\w|\h|[.,']){10,}$/gm;

## Check for phone number: () can be used on first group; spaces, periods, or
#    dashes can be used to separate groups.
$eval_phone = $phone !~ /^(\(?(\d){3}\)?(?: |-|.)?(\d){3}(?: |-|.)?(\d){4})$/gm;
$eval_typeLen = scalar @type < 1; ## At least one choice is checked.

## Check that user did not change an ice cream value in the address bar.
$eval_type = 0;
foreach $i(@type) {
  if($i =~ /Chocolate|Vanilla|Strawberry|Mocha Chip|Coffee Crunch/) {
    $eval_type += 1;
  }
}
$eval_type = ($eval_type == scalar @type) ? 0 : 1; ## finish the spoof check.
print "</br></br></br></br>";  ## Spaceing
if($eval_street) { ## Print if bad street.
  print "Invalid address (as best we can tell).</br>";
}
if($eval_phone) { ## Print if bad phone.
  print "Invalid local phone number pattern.</br>";
}
if($eval_typeLen) { ## Print if no choice made.
  print "Please make an icecream selection.</br>";
}
if($eval_type) { ## Print if spoof attempt.
  print "You may not subvert the system!</br>";
}
## all evals must be good.
if(not $eval_street and 
   not $eval_phone and 
   not $eval_type and 
   not $eval_typeLen){
  $subtotal = sprintf("%.2f",(scalar @type * 1.25));  ## Subtotal formatted
  $sales_tax = sprintf("%.2f", ($subtotal * 0.0925)); ## Sales Tax formatted
  $total = sprintf("%.2f", ($subtotal + $sales_tax)); ## Total formatted
  for $i(@type) { ## Number of Choices adding price to list.
    push @value, 1.25;
  }
  push @amounts, ($subtotal, $sales_tax); ## for table printing
  ## Outer table
  print "<table border=1, cellpadding=3, style=\"border-collapse:collapse;border:1px solid black;\">";
  print $page->Tr($page->th({-colspan=>'2', style=>'font-size:xx-large; color:blue;border-color:black;'},
          ['Acme Frozen Treat\'s']));
  print $page->Tr($page->td({-align=>'center', colspan=>'2'},
          ['Contact Information Preview']));
  print $page->Tr(
          $page->td({-style=>'font-weight:bold;'},'Street Address: '),
          $page->td($street));
  print $page->Tr(
          $page->td({-style=>'font-weight:bold;'},['Phone Number: ']),
          $page->td([$phone]));
  print $page->Tr($page->td({-align=>'center', colspan=>'2'},
          ['Order Preview']));
  print "<tr align=center><td colspan=\"2\">";
  print $page->table( ## Inner table for choices and amounts.
          {-border=>1, cellpadding=>3, width=>'200px', style=>'border-collapse:collapse;'},
          $page->Tr([
            $page->th(['Type','Value']),
          ]),
          (map{ ## Print choice type and price.
            $page->Tr( 
              $page->td({-align=>'right'},[$type[$_],$value[$_]]),
            ),}(0..(scalar @type - 1))),
          (map{  ## Print subtotal and sales tax and their amounts.
            $page->Tr(
              $page->td({-align=>'right', style=>'background:#CECECE;'},
                [$strAmounts[$_], $amounts[$_]])
            ),}(0..(scalar @strAmounts -1))),
          $page->Tr(  ## Print Total and its amount.
            $page->td({-align=>'right', style=>'background:#AAAAAA;font-weight:bold;'},
              ['Total','$ '. $total]),
          ),
        ); ## End inner table
  print "</td></tr></table>"; ## End outer table.
  print "</br></br>";
}
print "</center>";
print $page->end_html;
exit(0);

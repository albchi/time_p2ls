#!/bin/sh

# Script Name : time_p2ls.sh
# Description : This simple bash script will prompt user 
# Version     : 0.1
# Date        : 2020/SEPT/19
# Author      : Albert Chiang
# 
# Input (prompted): 
#    for current in California, numerial hour, in 24 hour format  
#    input variable : pdttime
# 
# Output : 
#    time (just hour) in Lithuania & Singapore
#    output variable : $lithtime 
#    output variable : $singtime 
#
# Example:
#    input : What is PDT hour in 24 hour format? 20
#    output : Lithuania, Israel time  6
#    output : Singapore time  11




# no space before and after equal sign! lithtime = 0 
# not necessary to declare variable
lithtime=0 

echo "this input was read on the commnad line" $1

read -p 'What is PDT hour in 24 hour format? ' pdttime

# use $ to use a variable
# need double paran for math expressions
# no space around equal and add signs!
((lithtmp=$pdttime+10)) 
((singtmp=$pdttime+15)) 
((lithtime=$lithtmp%24)) 
((singtime=$singtmp%24)) 


#echo "tmp time "  $lithtmp
echo "PDT time               : "  $pdttime
echo "Lithuania, Israel time : "  $lithtime 
echo "Singapore time         : "  $singtime 



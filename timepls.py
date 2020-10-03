#!/usr/local/bin/python

#from datetime import datetime
import datetime
import sys

# Script Name : time_p2ls.sh
# Description : This simple bash script will prompt user 
# Version     : 0.1
# Date        : 2020/SEPT/19
# Author      : Albert Chiang
# 
# Input (prompted): 
#    for current in California, numerial hour, in 24 hour format  
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
#lithtime=0 
localH=0 

#if [ -z "$1" ] #if [ -z "$my_var" ]
#then
#      #((localH = date +"%H")) #the unix command
#      curtime=$(date +"%H")
#      print "Null input PDT time. Will use local time of " $curtime
#else
#      curtime=$1
#      print "the input was read on the commnad line for PDT time and local version " $1 $curtime
#fi

if len(sys.argv) > 1:
   curtime = int(sys.argv[1])
else:
   #curtime = int(datetime.now()) #bad
   #print(datetime.datetime.now())
   #curtime = int(datetime.now())
   # curtime = 16
   now = datetime.datetime.now()
   curtime = now.hour

#read -p 'What is PDT hour in 24 hour format? ' pdttime

# use $ to use a variable
# need double paran for math expressions
# no space around equal and add signs!

#((lithtmp=$pdttime+10)) 
#((singtmp=$pdttime+15)) 
#((lithtime=$lithtmp%24)) 
#((singtime=$singtmp%24)) 

# debug curtime = 1
cesttmp=curtime+9
lithtmp=curtime+10
singtmp=curtime+15
cesttime=cesttmp%24
lithtime=lithtmp%24
singtime=singtmp%24


#print "tmp time "  $lithtmp
#print "PDT time               : "  $pdttime
#print "CEST time              : "  $cesttime 
#print "Lithuania, Israel time : "  $lithtime 
#print "Singapore time         : "  $singtime 

print ("-----------------------------------")
print ("PDT time               : "), curtime,(" H") #space between argument and double quote MATTERS
print ("CEST time              : "),  cesttime, (" H")
print ("Lithuania, Israel time : "),  lithtime, ("H")
print ("Singapore time         : "),  singtime, (" H")


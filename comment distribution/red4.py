#!/usr/bin/env python

from operator import itemgetter
import sys

current_month = None
current_count = 0
current_list=[]
l=0
month = None

# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # slpiting the data on the basis of tab we have provided in mapper.py
    g=line.split('\t')
    month= g[0]
    count= g[1]
    #count=line.split('\t')[1]
    


    if current_month==month:
        current_count+=1
        current_list.append(int(count))

    else:
        if current_month:
            # write result to STDOUT
            current_list.sort()
            l=(current_list[((current_count+1)//2)-1]+current_list[((current_count+2)//2)-1])/2
            print ('{}\t{}\t{}'.format(current_month, current_count,l))
        current_count = 1
        current_month = month
        current_list= []
        current_list.append(int(count))
if current_month == month:
    print ('{}\t{}\t{}'.format(current_month, current_count,str(l)))
    

#!/usr/bin/env python
# import sys because we need to read and write data to STDIN and STDOUT
import sys
import re

# reading entire line from STDIN (standard input)

for line in sys.stdin:
    pattern=re.compile(r'CreationDate..(\d{4}[-]\d\d)[-]\d\d\w\d\d[:]\d\d[:]\d\d\.\d\d\d.')
    pattern2=re.compile(r'Text..\b(([ |\W+]+)?\w+([ |\W+]+)?\w+?)+\b.')
    matches=pattern.finditer(line)
    matches2=pattern2.finditer(line)
    for match in matches:
        
            
            for match2 in matches2:
                print(match.group(1),end="\t" )
                print(len(match2.group(0)[6:-29].split())-1)
                break
            break

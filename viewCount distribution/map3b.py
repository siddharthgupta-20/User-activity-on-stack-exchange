#/usr/bin/env python
# import sys because we need to read and write data to STDIN and STDOUT
import sys
import re

# reading entire line from STDIN (standard input)
a=[]
for line in sys.stdin:
    pattern1=re.compile(r'\bId..(\d+)\b')
    pattern2=re.compile(r'\bOwnerUserId..(\d+)\b')
    pattern3=re.compile(r'\bViewCount..(\d+)\b')
    matches1=pattern1.finditer(line)
    matches2=pattern2.finditer(line)
    matches3=pattern3.finditer(line)
    
    for match in matches1:
      for match2 in matches2:
        for match3 in matches3:
          print("{}\t{}\t{}".format(match3.group(1),match2.group(1),match.group(1)))
   
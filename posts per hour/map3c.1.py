#/usr/bin/env python
# import sys because we need to read and write data to STDIN and STDOUT
import sys
import re


for line in sys.stdin:
    pattern=re.compile(r'CreationDate..(\d{4}[-]\d\d)[-]\d\d\w(\d\d)[:]\d\d[:]\d\d\.\d\d\d.')
    #print(line)
    matches=pattern.finditer(line)
    
    for match in matches:
      print('{}\t{}'.format(match.group(2),1))
      
    
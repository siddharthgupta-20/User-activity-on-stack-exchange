#!/usr/bin/env python
# import sys because we need to read and write data to STDIN and STDOUT
import sys
import re

for line in sys.stdin:
    pattern=re.compile(r'Tags...?\b([\W\w\w\W]?(\w+.?\w+)[\W\w\w\W]?)+\b')
    matches=pattern.finditer(line)
    
    for match in matches:
        a=match.group(0).split('&lt;')
        a=a[1:]
        for t in a:
            if(t[-1]==';'):
                t=t[0:len(t)-4]
            else:
                t=t[0:len(t)-3]
            print('{}\t{}'.format(t,1))

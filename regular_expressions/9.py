

import re


string = 'purple deepabalank1990@gmail.com monkey dishwasher'
match = re.search(r'([\w.-]+)@([\w.-]+)', string)

if match:
    print match.group()
    print match.group(1)
    print match.group(2)

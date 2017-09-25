
import re


string = 'My name is:Deepa'
match = re.search(r'\w\w:\w\w\w\w\w', string)
if match:
    print 'match found: ', match.group()
else:
    print 'no match'

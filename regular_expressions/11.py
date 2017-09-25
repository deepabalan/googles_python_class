

import re


string = 'purple alice@google.com, blah monkey bob@abc.com blah dishwater'
tuples = re.findall(r'([\w.-]+)@([\w.-]+)', string)
print tuples
for tup in tuples:
    print tup[0]
    print tup[1]

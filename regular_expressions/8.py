

import re


match = re.search(r'^b\w+', 'foobar')
print 'not found', match == None

match = re.search(r'b\w+', 'foobar')
print 'found', match.group() == 'bar'

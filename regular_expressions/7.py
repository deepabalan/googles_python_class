

import re


match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')
print 'found', match.group() == '1 2   3'

match = re.search(r'\d\s*\d\s*\d', 'xx12   3xx')
print 'found', match.group() == '12   3'

match = re.search(r'\d\s*\d\s*\d', 'xx123xx')
print 'found', match.group() == '123'

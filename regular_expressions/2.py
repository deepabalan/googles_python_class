

import re


match = re.search(r'ing', 'piiig')
if match:
    print 'match found', match.group()
else:
    print 'No matches'

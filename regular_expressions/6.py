

import re


match = re.search(r'i+', 'piigiii')
print 'found', match.group() == 'ii'

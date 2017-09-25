

import re


match = re.search(r'D...a', 'Deepa')
if match:
    print match.group()
else:
    print 'no'

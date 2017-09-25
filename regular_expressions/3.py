

import re


match = re.search(r'..g', 'piig')
if match:
    print match.group()

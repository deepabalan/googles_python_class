

import re


match = re.search(r'pi+', 'piiig')
print 'found', match.group() == "piii"



import re


string = 'purple alice@google.com, blah monkey bob@abc.com blah dishwater'

emails = re.findall(r'[\w.-]+@[\w.-]+', string)
print emails
for email in emails:
    print email

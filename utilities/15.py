

import urllib

url = 'https://github.com/deepabalan/google_python_class'

ufile = urllib.urlopen(url)
baseurl = ufile.geturl()
print baseurl

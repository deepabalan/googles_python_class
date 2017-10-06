

import urllib


url = 'https://github.com/deepabalan'

try:
    ufile = urllib.urlopen(url)
    print ufile # file like object
    text = ufile.read()
    print text # read from it, like a file
    info = ufile.info()
    print info
    print info.gettype()
except:
    print 'url not found'



import urllib


def wget2(url):
    try:
        ufile = urllib.urlopen(url)
        if ufile.info().gettype() == 'text/html':
            print ufile.read()
    except IOError:
        print 'problem reading url:', url

wget2()

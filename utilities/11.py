

import urllib


def wget(url):
    ufile = urllib.urlopen(url)
    info = ufile.info()
    if info.gettype() == 'text/html':
        print 'base url:' + ufile.geturl()
        text = ufile.read()
        print text

wget()

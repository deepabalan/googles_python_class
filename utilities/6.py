
import urllib


def wget(url):
    ufile = urllib.urlopen(url)
    info = ufile.info()
    if info.gettype() == 'text/html':
        print 'base url:' + ufile.geturl()
        text = ufile.read()
        print text
    try:
        ufile = urllib.urlopen(url)
        if ufile.info().gettype() == 'text/html':
            print ufile.read()
    except IOError:
            print 'problem reading url:', url
wget('https://github.com/deepabalan')

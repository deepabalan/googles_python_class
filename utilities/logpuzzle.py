

import sys
import urllib

def read_urls(filename):
    ufile = urllib.urlopen(filename)
    text = ufile.read()
    print text
read_urls(sys.argv[1])

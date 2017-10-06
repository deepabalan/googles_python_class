

import urllib
import sys


url = 'https://github.com/deepabalan/S1S2_C_lab/blob/master/10_odd.c'

def my_download(url):
    return urllib.urlretrieve(url, sys.argv[1])

my_download(url)

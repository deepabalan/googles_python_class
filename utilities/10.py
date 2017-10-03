
import sys

filename = 'foo.txt'

try:
    f = open(filename, 'rU')
    text = f.read()
    f.close()
except IOError:
    sys.stderr.write('problem reading:' + filename)

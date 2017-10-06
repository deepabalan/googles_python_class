
import sys


filename = sys.argv[1]
try:
    f = open(filename, 'rU')
    text = f.read()
    print text
    f.close()
except IOError:
    sys.stderr.write('Problem reading: ' + filename)
    sys.exit(1)

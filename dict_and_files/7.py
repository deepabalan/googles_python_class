
import codecs

f = codecs.open('bar.txt', 'rU', 'utf-8')
for line in f:
    print line

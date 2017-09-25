

import sys


def fun(filename):
    f = open(filename, 'rU')
    text = f.read()
    output_file = open('foobar.txt', 'w')
    output_file.write(text)
    output_file.close()
    
fun(sys.argv[1])

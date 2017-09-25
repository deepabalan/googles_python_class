

import os
import sys

def foo(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        print filename

# foo('/home/deepa/technical_stuffs/thinkpython')
foo(sys.argv[1])

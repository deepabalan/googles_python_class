
import sys
import os


def printdir(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        print filename
        path = os.path.join(dir, filename)
        print path
        print os.path.abspath(path)

printdir(sys.argv[1])

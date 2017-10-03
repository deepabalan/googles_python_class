

import sys
import re
import os
import shutil
import commands


def get_special_paths(dirname):
    names = []
    fnames = os.listdir(dirname)
    for fname in fnames:
        match = re.search(r'__(\w+)__', fname)
        if match:
            dir_name = os.path.join(dirname, fname)
            abs_path = os.path.abspath(dir_name)
            names.append(abs_path)
    return names


def copy_to(paths, dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    for path in paths:
        basename = os.path.basename(path)
        destination = os.path.join(dirname, basename)
        shutil.copy(path, destination)

def zip_to(paths, zipfile):
    if not os.path.exists(zipfile):
        os.mkdir(zipfile)
    cmd = 'zip -j ' + zipfile + ' ' + ''.join(paths)
    print "Command I'm going to do: " + cmd
    (status, output) = commands.getstatusoutput(cmd)
    if status:
        sys.stderr.write(output)
        sys.exit(1)

zip_to(get_special_paths(sys.argv[3]), sys.argv[2])
    

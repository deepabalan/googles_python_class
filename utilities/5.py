
import sys
import commands

def listdir(dir):
    cmd = 'ls -l' + dir
    print "Command to run:", cmd
    (status, output) = commands.getstatusoutput(cmd)
    if status:
        sys.stderr.write(output)
        sys.exit(status)
    print output

listdir(sys.argv[1])


import commands

(status, output) = commands.getstatusoutput('ls -l')

print (status, output)

import os
import sys

pid = os.getpid()
file = (sys.argv)[1]

f = open("_PIDS.txt", "a")
f.write('\n' + str(pid))
f.close()

splits = file.split('/')

os.chdir(splits[0] +'/'+ splits[1])
exec(open(splits[2] + ".pyw").read())
import os
import sys

pid = os.getpid()
file = (sys.argv)[1]
print(file + "____")

f = open("_PIDS.txt", "a")
f.write('\n' + str(pid))
f.close()

exec(open(file + ".pyw").read())
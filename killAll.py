import os
import subprocess

f = open("_PIDS.txt", "r")
pids = f.readlines()

# kill process if it's a python process
for pid in pids:
    try:
        pid = pid.rstrip("\n")
        result = subprocess.check_output("wmic process where processId=" + pid + " get name", shell = True, stderr=subprocess.PIPE)
        result = result.decode('utf-8')
        if ("pythonw.exe" in result):
            os.system("taskkill /F /PID " + pid)
            print(pid + " killed")
        else:
            print(pid + " already closed" )
    except:
        # try next
        print(pid + " failed to kill")


# erase contents
file = open("_PIDS.txt","w")
f.close()
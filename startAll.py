import os

programs = ["changeAgrName/changeAgrName"]

for p in programs:
    print("starting " + p)
    os.system("start \"\" pythonw start.pyw \"" + "../" + p + "\"")
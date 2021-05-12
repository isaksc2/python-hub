import os

programs = ["changeAgrName/changeAgrName", "typing-sound/typeSound"]

for p in programs:
    print("starting " + p)
    os.system("start \"\" pythonw start.pyw \"" + "../" + p + "\"")
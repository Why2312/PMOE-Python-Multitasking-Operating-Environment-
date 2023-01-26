import os
import time
from FS.lib.task import task as task
import FS.lib.util as util

from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()

def bootapp_single(path):
    with open(path, "r") as f:
        code = compile(f.read(), path, "exec", optimize=2)
        exec(code)
    return locals()


global rwd

rwd = os.getcwd()

dir = rwd + "/onboot"
shell = rwd + "/bin/shell.py"



print("Launching on_boot scripts...")
for filename in os.listdir(dir):
    f = os.path.join("onboot/", filename)
    if os.path.isfile(f):
        print(f)
        before = time.time()
        bootapp_single(f)
        after = time.time()
        timetotal = after - before
        print(f"{f} took {round(timetotal, 2)} seconds to run.")
print("Launching shell...")
bootapp_single(shell)


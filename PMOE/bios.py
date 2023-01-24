import json
import os
import time

global wait
print("SBIOS ver 0.1")
print("Testing memory...")
wait = time.sleep
del time
wait(3)
try:
    os.chdir("FS")
except:
    print()
del json
print("Running /init.py")
if os.path.isfile("init.py"):
    with open("init.py") as f:
        data = f.read()
        exec(data)
else:
    print("Could not find /init.py, aborting...")
    exit()

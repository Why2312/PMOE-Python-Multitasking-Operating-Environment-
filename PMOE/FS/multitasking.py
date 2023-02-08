from FS.lib import mem,util,task
import time
#Clear the screen
clear()

#Lets start our shell app

with open(rwd + "/mtapps/shell/main.py", "r") as f:
    shellapp = task.task(f.read(), 0, False, "shell", rwd)


print("\033[?25l", end="")

process = shellapp.start()
process.join()
time.sleep(2)


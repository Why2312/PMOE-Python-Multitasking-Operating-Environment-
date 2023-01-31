from FS.lib import mem,util,task
import time
#Clear the screen
clear()

#Lets start our shell app

with open(rwd + "/mtapps/shell/main.py", "r") as f:
    shellapp = task.task(f.read(), 0, False, "shell")


print("\033[?25l", end="")

shellapp.start()
time.sleep(2)
while True:
    current_buffer = task.activetask.video_buffer
    print("\033[H" + current_buffer)


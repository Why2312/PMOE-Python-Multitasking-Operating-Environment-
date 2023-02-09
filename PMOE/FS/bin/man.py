import os

# get help folder path
helpf = rwd + "/help/"
# get command
command = args[0]
max_size = 2048
# open the help file
with open(helpf + command, 'r') as f:
    while True:
        # read max_size
        buf = f.read(max_size)
        if buf == "":
            break
        # print and wait for user pressing enter
        print(buf)
        input()
import os
for i in os.listdir(rwd + "/bin"):
    name,ext = os.path.splitext(i)
    if ext == ".py" or ext == ".exe":
        print(name)
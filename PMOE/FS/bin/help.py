import os
for i in os.listdir(rwd + "/bin"):
    name,ext = os.path.splitext(i)
    print(name)
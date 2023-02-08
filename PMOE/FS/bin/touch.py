import os
filename = args[0]
open(filename, 'a').close()
os.utime(filename, None)
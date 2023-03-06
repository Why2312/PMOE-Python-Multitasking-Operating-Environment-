import os
filename = rwd+format_path(args[0])
open(filename, 'a').close()
os.utime(filename, None)
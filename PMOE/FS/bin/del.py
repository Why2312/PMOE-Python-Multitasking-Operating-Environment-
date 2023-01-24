import os
import shutil
try:
    if os.path.isdir(args[0]):
        shutil.rmtree(args[0])
    else:
        os.remove(args[0])
except:
    errormsg("Invalid Directory/File name")
import os
fullpath = rwd+format_path(args[0])
try:
    if args and args[0]:
        if args[0] == "..":
            chdir(os.path.abspath(os.path.join(os.curdir, "..")))
        elif os.path.exists(fullpath) and os.path.isdir(fullpath):
            chdir(fullpath)
        elif os.path.exists(args[0]) and os.path.isdir(args[0]):
            chdir(args[0])
        else:
            errormsg("Invalid path")
    else:
        print(format_path(os.getcwd()))
except Exception as f:
    errormsg("Directory invalid.")
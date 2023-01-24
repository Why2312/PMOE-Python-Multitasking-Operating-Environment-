import os
try:
    if args and args[0]:
        if args[0] == "..":
            chdir(os.path.abspath(os.path.join(os.curdir, "..")))
        elif os.path.exists(args[0]) and os.path.isdir(args[0]):
            chdir(args[0])
        else:
            errormsg("Invalid path")
    else:
        errormsg("Please provide a path")
except Exception as f:
    errormsg("Directory invalid.")
import os
import shutil

def rm(args):
    try:
        recursive = False
        force = False
        paths = []
        for arg in args:
            if arg == "-r" or arg == "-R":
                recursive = True
            elif arg == "-f" or arg == "-F":
                force = True
            else:
                paths.append(arg)

        if not paths:
            errormsg("rm: missing operand")
            return False

        for path in paths:
            fullpath = os.path.join(os.getcwd(), path)
            if os.path.exists(fullpath):
                if os.path.isdir(fullpath) and not recursive:
                    errormsg("rm: cannot remove '{}': Is a directory".format(path))
                elif not force:
                    answer = input("rm: remove '{}'? (y/n) ".format(path))
                    if answer.lower() != "y":
                        continue

                if os.path.isdir(fullpath):
                    shutil.rmtree(rwd+format_path(fullpath))
                else:
                    os.remove(rwd+format_path(fullpath))
            else:
                errormsg("rm: cannot remove '{}': No such file or directory".format(path))
    except Exception as e:
        errormsg("rm: error:", e)
        return False

    return True

rm(args)
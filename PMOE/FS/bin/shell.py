import os
import re
import subprocess
import FS.lib.util as util
global args
args = []
global bootapp_single
def bootapp_single(path, arg):
    with open(path, "r") as f:
        code = compile(f.read(), path, "exec", optimize=2)
        args = arg
        exec(code)
    return locals()
global ver

with open(rwd + "/asset/version.str", "r") as f:
    ver = f.read()

global chdir
chdir = os.chdir
global errormsg
def errormsg(msg):
    print(util.set_colors((255,0,0), (0,0,0)), end="")
    print(msg)
    print(util.set_colors((255,255,255), (0,0,0)), end="")

def commandparser():
    try:
        print(util.set_colors((255,0,0), (0,0,0)), end="")
        print(os.getcwd() + "$>", end="")
        print(util.set_colors((255,255,255), (0,0,0)), end="")
        i = input()
        i2 = i.split(" ")
        if i2[0].lower() == "exit":
            return True
        elif i2[0].lower() == "nano" and os.name == "posix":
            single_string = " ".join(i2)
            os.system(single_string)
            return False


    except:
        print("\nKeyboardInterrupt, use exit command to exit.")
    full_path = os.path.join(rwd, "bin")
    bin_commands = {os.path.join(full_path, f) for f in os.listdir(full_path)}
    commands = list(bin_commands)
    for f in os.listdir(os.getcwd()):
        full_path = os.path.join(os.getcwd(), f)
        if not os.path.isdir(full_path) and full_path not in bin_commands:
            commands.append(full_path)
    try:
        ic = i2[0].lower() + ".exe"
        ic2 = i2[0].lower() + ".py"
        ic3 = i2[0].lower()
        i2.pop(0)
    except:
        return False
    try:
        for f in commands:
            import subprocess as subprocess
            if os.path.basename(f) == ic:
                subprocess.call([f] + i2)
            elif os.path.basename(f) == ic2:
                bootapp_single(f, i2)
            elif os.path.basename(f) == ic3:
                bootapp_single(f, i2)
    except Exception as f:
        errormsg("PROCESS ERROR: " + str(f))
        return False
    return False


print(util.set_colors((255,255,255), (0,0,0)), end="")
print(os.getcwd())
clear()
global bootimg
global pmoe_url
pmoe_url = open(rwd + "/asset/pmoe_server.lnk", "r").read()
bootig = open(os.getcwd() + "/asset/boot.timg", "r", encoding="utf-8")
bootimg = bootig.read()
print(bootimg)
print(f"Loaded PMOE V{ver} HDD")
while True:
    quit = commandparser()
    if quit: break

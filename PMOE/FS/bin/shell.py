import os
import re
print = None
from FS.drv.print import print
import subprocess
import FS.lib.util as util
global accountn
"""    Programmer: Someoneidk Usage: Modular shell simulating coding experience in the 80's.
    Copyright (C) 2023 Someoneidk

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>."""
global args
args = []
global bootapp_single
def bootapp_single(path, arg):
    with open(path, "r", 10**6) as f:
        code = compile(f.read(), path, "exec", optimize=2)
        args = arg
        exec(code)
    return locals()
global ver
global bytes2human
def bytes2human(n, format="%(value)i%(symbol)s"):
    symbols = ('B', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols[1:]):
        prefix[s] = 1 << (i+1)*10
    for symbol in reversed(symbols[1:]):
        if n >= prefix[symbol]:
            value = float(n) / prefix[symbol]
            return format % locals()
    return format % dict(symbol=symbols[0], value=n)
global format_path
def format_path(path:str):
    path = path.replace('\\', '/')
    # remove everything before and including "/FS"
    path = "/" + path.split("/FS")[-1]
    return path.replace("//", "/")

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
        print(util.set_colors((0,255,0), (0,0,0)), end="")
        print(f"{accountn}@", end="")
        print(util.set_colors((255,0,0), (0,0,0)), end="")
        print(format_path(os.getcwd() + " $ "), end="")
        print(util.set_colors((255,255,255), (0,0,0)), end="")
        i = input()
        i2 = i.split(" ")
        if i2[0].lower() == "exit":
            return True
        elif i2[0].lower() == "logout":
            logout = True
            return "logout"


    except:
        print("\nKeyboardInterrupt, use exit command to exit.")
    if i2[0].lower() == "nano" and os.name == "posix":
        single_string = " ".join(i2)
        os.system(single_string)
        return False
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


def run_shell_cmd(cmd:str):
    i = cmd
    i2 = i.split(" ")
    if i2[0].lower() == "nano" and os.name == "posix":
        single_string = " ".join(i2)
        os.system(single_string)
        return False
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
        executed = False
        for f in commands:
            import subprocess as subprocess
            if os.path.basename(f) == ic:
                subprocess.call([f] + i2)
                executed = True
            elif os.path.basename(f) == ic2:
                bootapp_single(f, i2)
                executed = True
            elif os.path.basename(f) == ic3:
                bootapp_single(f, i2)
                executed = True
        if not executed:
            print("Unkown command: "+ic)
    except Exception as f:
        errormsg("PROCESS ERROR: " + str(f))
        return False


with open(os.path.join(rwd, "home", "root", ".bashrc")) as f:
    cmds = f.readlines()


if __name__ == "__main__":
    global logout
    logout = False
    while True:
        accountn = input("Account name>")
        if os.path.exists(os.path.join(rwd, "home", accountn)):
            print(f"Found account. Logging into {accountn}...")
            break
        else:
            print(f"{accountn} does not exist, try again.")
    print(util.set_colors((255,255,255), (0,0,0)), end="")
    wait(2)
    clear()
    global bootimg
    global pmoe_url
    pmoe_url = open(rwd + "/asset/pmoe_server.lnk", "r").read()
    bootig = open(os.getcwd() + "/asset/boot.timg", "r", encoding="utf-8")
    bootimg = bootig.read()
    print(bootimg)
    print(f"Loaded PMOE V{ver} HDD")
    if accountn == "root":
        print("Running as root shell")

    for i in cmds:
        if i:
            run_shell_cmd(i)
    
    chdir(f"home/{accountn}")
    while True:
        quit = commandparser()
        if quit == "logout": break
        elif quit: exit()

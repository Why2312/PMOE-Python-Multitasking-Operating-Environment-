import os
import time
print = None
from FS.drv.print import print
from FS.lib.task import task as task
import FS.lib.util as util
import shutil
import cgi
global logout
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
from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()

def bootapp_single(path):
    with open(path, "r") as f:
        code = compile(f.read(), path, "exec", optimize=2)
        exec(code)
    return locals()


global rwd

rwd = os.getcwd()

shutil.rmtree(os.path.join(rwd, "tmp"))
os.mkdir(os.path.join(os.path.join(rwd, "tmp")))

dir = rwd + "/onboot"
shell = rwd + "/bin/shell.py"



print("Launching on_boot scripts...")
for filename in os.listdir(dir):
    f = os.path.join("onboot/", filename)
    if os.path.isfile(f) and f.endswith(".py"):
        print(f)
        before = time.time()
        bootapp_single(f)
        after = time.time()
        timetotal = after - before
        print(f"{f} took {round(timetotal, 2)} seconds to run.")
print("Launching shell...")
def launchshell():
    def bootapp_single(path):
        with open(path, "r") as f:
            code = compile(f.read(), path, "exec", optimize=2)
            exec(code)
        return locals()
    bootapp_single(shell)
    os.chdir(rwd)
    clear()
    launchshell()
launchshell()


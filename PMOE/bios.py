import json
import os
import time
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
global wait
print("SBIOS ver 0.1")
print("Testing memory...")
wait = time.sleep
del time
wait(3)
try:
    os.chdir("FS")
except:
    print()
del json
print("Running /init.py")
if os.path.isfile("init.py"):
    with open("init.py") as f:
        data = f.read()
        exec(data)
else:
    print("Could not find /init.py, aborting...")
    exit()

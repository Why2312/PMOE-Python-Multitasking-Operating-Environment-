import os
import zipfile
import FS.lib.util as util

downloaddir = os.getcwd() + "/"
package = args[0]

try:
    print("Applying update     ", end="")
    with zipfile.ZipFile(downloaddir + package, 'r') as zip_ref:
        zip_ref.extractall(downloaddir)
    util.slow_type(".....", 15)
    print(package + " Installed Successfully!")
except:
    errormsg("Issue installing custom PMOE package")
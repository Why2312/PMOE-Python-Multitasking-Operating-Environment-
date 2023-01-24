#Update file to update PMOE.
import requests
import json
import os
import zipfile
import FS.lib.util as util

data = {}

downloaddir = os.path.abspath(rwd + "\\..")

#URL to download from
URL2 = "http://86.123.33.68/PMOE/"
try:
    data["latest"] = f"PMOE_{args[0]}_.zip"
    filetodownload = URL2 + data["latest"]
    yn = input("Update to download: " + data['latest'] + ", Current version: " + ver + " Proceed (y/n)?")
    if yn.lower() == "y":
        print("Downloading Update  ", end="")
        r = requests.get(filetodownload, stream=True, timeout=20)
        util.slow_type(".....", 15)
        print("Saving Update       ", end="")
        with open(downloaddir + "\\PMOE.zip", 'wb') as f:
            for chunk in r.iter_content(chunk_size=64): 
                f.write(chunk)
        util.slow_type(".....", 15)
        print("Applying update     ", end="")
        with zipfile.ZipFile(downloaddir + "\\PMOE.zip", 'r') as zip_ref:
            zip_ref.extractall(downloaddir)
        util.slow_type(".....", 15)
        os.remove(downloaddir + "\\PMOE.zip")
        print(data["latest"] + " Installed Successfully!")
    else:
        print("Declined update, closing...")
except:
    errormsg("Main PMOE server down or invalid version.")
#Update file to update PMOE.
import requests
import json
import os
import zipfile
import FS.lib.util as util


downloaddir = os.path.abspath(rwd + "\\..")

#URL to download from
URL1 = pmoe_url + "/PMOE/latest.json"
URL2 = pmoe_url + "/PMOE/"
try:
    js = requests.get(URL1, timeout=20)
    data = js.json()
    filetodownload = URL2 + data["latest"]
    yn = input("Latest update: " + data['latest'] + ", Current version: " + ver + " Proceed (y/n)?")
    if yn.lower() == "y":
        print("Downloading Update  ", end="")
        r = requests.get(filetodownload, stream=True, timeout=20)
        util.slow_type(".....", 15)
        print("Saving Update       ", end="")
        with open(downloaddir + "/PMOE.zip", 'wb') as f:
            for chunk in r.iter_content(chunk_size=2): 
                f.write(chunk)
        util.slow_type(".....", 15)
        print("Applying update     ", end="")
        with zipfile.ZipFile(downloaddir + "/PMOE.zip", 'r') as zip_ref:
            zip_ref.extractall(downloaddir)
        util.slow_type(".....", 15)
        os.remove(downloaddir + "/PMOE.zip")
        print(data["latest"] + " Installed Successfully!")
    else:
        print("Declined update, closing...")
except Exception as f:
    errormsg("Main PMOE server down or invalid server.")

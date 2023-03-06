import os
import sys
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="cgi")
from urllib.request import urlopen, urlretrieve
import requests as requests
import zipfile
import shutil

def extract_zip_file(zip_file_path:str, extract_directory:str):
    import zipfile
    """Extracts a zip file from `zip_file_path` to `extract_directory`.

    Args:
        zip_file_path (str): The path of the zip file to be extracted.
        extract_directory (str): The destination of the extracted zip file.
    """
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_directory)

def download_file(url:str, filename:str, block_size:int=1024):
    """Downloads a file at 'url' and saves it to 'filename'.

    Args:
        url (str): The url to the file to download.
        filename (str): The filename to save the data to.
        block_size (int, optional): The saving block size. Lower values conserve memory at cost of more cpu, higher values conserve cpu time at the cost of more memory usage. Defaults to 1024.
    """
    import requests as requests
    r = requests.get(url, stream=True)
    import sys
    try:
        total_size = int(r.headers.get("Content-Length", 0))
        wrote = 0
        with open(filename, 'wb') as f:
            for data in r.iter_content(block_size):
                wrote = wrote + len(data)
                f.write(data)
                done = int(50 * wrote / total_size)
                sys.stdout.write("\r[{}{}]".format("=" * done, " " * (50-done)) + " - GET - " + url)
                sys.stdout.flush()
        if total_size != 0 and wrote != total_size:
            sys.stderr.write("ERROR, something went wrong")
    except:
        ""


def url_to_filename(url:str) ->str:
    """Converts an url to a filename

    Args:
        url (str): A link of the file.

    Returns:
        str: The filename of the link
    """
    from urllib.request import urlopen, urlretrieve
    remotefile = urlopen(url)
    contentdisposition = remotefile.info()['Content-Disposition']
    _, params = cgi.parse_header(contentdisposition)
    return params["filename"]

try:
    action = args[0]
    program = args[1]
    ppt = pmoe_url + "/PPT/"
    pptp = ppt + program
    ppt_temp = os.path.join(rwd, "pptapps", program)
    if not os.path.exists(ppt_temp):
        os.mkdir(ppt_temp)
    pptp_zip = pptp + "/app.zip"
    pptp_desc = pptp + "/description.txt"
    pptp_depn = pptp + "/dependancies.txt"

except Exception as f:
    errormsg("""
             Usage:
             
             ppt <action> <package>
             
             Actions:
             install
             remove
             info""")
try:
    if action.lower() == "install":
        success = False
        try:
            r = requests.get(pptp, timeout=5)
            success = True
        except requests.exceptions.Timeout as f:
            errormsg("PMOE Server down or no network connection")


        if r.status_code == 200 and success:
            print("Downloading Files...")
            download_file(pptp_zip, os.path.join(ppt_temp, "app.zip"), 32)
            print()
            download_file(pptp_desc, os.path.join(ppt_temp, "description.txt"), 32)
            print()
            download_file(pptp_depn, os.path.join(ppt_temp, "dependencies.txt"), 32)
            print()
            with open(os.path.join(ppt_temp, "dependencies.txt"), "r", encoding="utf-8") as f:
                lines = f.readlines()
            for i in lines:
                if i:
                    download_file(i, os.path.join(ppt_temp, url_to_filename(i)))
            print()
            extract_zip_file(os.path.join(ppt_temp, "app.zip"), ppt_temp)
            bootapp_single(os.path.join(ppt_temp, "setup.py"), {})


        elif r.status_code == 404 and success:
            errormsg("The program does not exist")
        elif r.status_code == 500 and success:
            errormsg("PMOE Server experienced an error")
        elif r.status_code == 503 and success:
            errormsg("PMOE Server is unavailable")
    elif action.lower() == "remove":
        if os.path.exists(ppt_temp):
            bootapp_single(os.path.join(ppt_temp, "remove.py"), {})
            shutil.rmtree(ppt_temp)
    elif action.lower() == "info":
        print("Retrieving PMOE package info...")
        try:
            r = requests.get(pptp, timeout=5)
            success = True
        except requests.exceptions.Timeout as f:
            errormsg("PMOE Server down or no network connection")
        if r.status_code == 200 and success:
            print("Program exists, reading info...")
            desc = requests.get(pptp_desc, timeout=5).content
            depn = requests.get(pptp_depn, timeout=5).content
            print(f"Listing info for {program}:")
            print("\nDescription:")
            print(desc)
            print("\nUsed Libraries:")
            print(depn)
        elif r.status_code == 404 and success:
            errormsg("The program does not exist")
        elif r.status_code == 500 and success:
            errormsg("PMOE Server experienced an error")
        elif r.status_code == 503 and success:
            errormsg("PMOE Server is unavailable")
    else:
        errormsg("""
             Usage:
             
             ppt <action> <package>
             
             Actions:
             install
             remove
             info""")
except Exception as f:
    errormsg(f"ERROR: {str(f)}")
        
    
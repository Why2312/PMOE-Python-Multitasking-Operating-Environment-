import requests
import FS.lib.util as util


url = args[0]
tofile = rwd+format_path(args[1])

print("Downloading  ", end="")


try:
    r = requests.get(url, stream=True)
    util.slow_type(".....", 15)
    print("Saving data  ", end="")
    util.slow_type(".....", 15)
    with open(tofile, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192): 
            f.write(chunk)
except Exception as f:
    print()
    errormsg("Error: "+ str(f))

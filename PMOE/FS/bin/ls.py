path = False
import os
import FS.lib.util as util
try:
	path = os.path.abspath(args[0])
except:
	path = os.getcwd()
def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

print("Listing files in: " + format_path(path))

try:
	for i in os.listdir(path):
		full_path = os.path.join(path, i)
		if os.path.isdir(full_path):
			print(util.set_colors((0,0,255), (0,0,0)), end="")
			print(i + "/ - " + str(bytes2human(get_directory_size(full_path))))
			print(util.set_colors((255,255,255), (0,0,0)), end="")
		else:
			print(util.set_colors((0,255,0), (0,0,0)), end="")
			print(i + " - " + str(bytes2human(os.path.getsize(full_path))))
			print(util.set_colors((255,255,255), (0,0,0)), end="")
except:
	errormsg("Invalid path")

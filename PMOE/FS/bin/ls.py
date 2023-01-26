path = False
import os
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

print("Listing files in: " + path)

try:
	for i in os.listdir(path):
		full_path = os.path.join(path, i)
		if os.path.isdir(full_path):
			print(i + "/ - " + str(get_directory_size(full_path)) + " Bytes")
		else:
			print(i + " - " + str(os.path.getsize(full_path)) + " Bytes")
except:
	errormsg("Invalid path")

import zipfile
import os

files2 = ["bios.py", "requirements.txt", "doc.txt", "LICENSE.txt"]
folder = "FS"

print("Making archive of current OS, please wait.")

print(os.getcwd())

ver = input("Input version>")

with open(os.getcwd() + "\\FS\\asset\\version.str", "w") as f:
    f.write(ver)


with zipfile.ZipFile(os.getcwd() + f"\\PMOE_{ver}_.zip", 'w') as archive:
    for root, dirs, files in os.walk(folder):
        for file in files:
            archive.write(os.path.join(root, file), compress_type=zipfile.ZIP_DEFLATED)
    for file in files2:
        absfile = file
        archive.write(absfile, compress_type=zipfile.ZIP_DEFLATED)


print("PMOE compressed!")
input()

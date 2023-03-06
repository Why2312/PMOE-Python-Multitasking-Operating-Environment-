import os
import FS.lib.util as util
print("Installing PMOE-CHAT")
util.copy_file(os.path.join(rwd, "pptapps", "pmoe-chat", "chat.py"), os.path.join(rwd, "bin", "chat.py"))
util.delete_file("chat.py")
wait(1)
print("Installed!")
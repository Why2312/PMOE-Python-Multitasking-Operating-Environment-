from FS.lib.vbuffer import VBuffer
import os
import FS.lib.task as task
import keyboard
from FS.lib.util import set_colors
import time


task.activetask = self.name
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def search_and_boot():
    import os as os
    myapps_folder = os.path.join(rwd, "mtapps")
    folders = [f for f in os.listdir(myapps_folder) if os.path.isdir(os.path.join(myapps_folder, f))]
    print(folders)

    selected_index = 0
    while True:
        print("\033[H")
        print("Select application:")
        for i, folder in enumerate(folders):
            print(i, selected_index)
            if i == selected_index:
                print(f"> {folder}")
            else:
                print(f"  {folder}")
        if keyboard.is_pressed('up arrow'):  # up arrow
            selected_index = max(0, selected_index - 1)
        elif keyboard.is_pressed('down arrow'):  # down arrow
            selected_index = min(len(folders) - 1, selected_index + 1)
        elif keyboard.is_pressed('enter'):  # return/enter key
            print(folders[selected_index])
            return os.path.join(myapps_folder, folders[selected_index])


while True:
    clear()
    selected_folder = search_and_boot()
    clear()
    print("App info:")
    with open(os.path.join(selected_folder, "title.txt"), "r") as f:
        print(os.path.join(selected_folder, "title.txt"))
        print(f"Name        : {f.read()}")
        name=f.read()
    with open(os.path.join(selected_folder, "desc.txt"), "r") as f:
        print(f"Description : {f.read()}")
    with open(os.path.join(selected_folder, "type.txt"), "r") as f:
        print(f"Type        : {f.read()}")
    with open(os.path.join(selected_folder, "main.py"), "r") as f:
        code = f.read()

    print("\n")
    yn = input("Boot App? (y/n)")

    if yn.lower() == "y":
        task = task.task(code, 0, False, name, rwd)
        thread = task.start()
        thread.join()
        clear()
    else:
        continue
    

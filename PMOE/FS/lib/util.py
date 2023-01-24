import sys,random,time
def setansicode(code):
    print(f"\033[{code}", end="")
    
def set_colors(text_color: tuple, bg_color: tuple):
    return f"\033[38;2;{text_color[0]};{text_color[1]};{text_color[2]}m\033[48;2;{bg_color[0]};{bg_color[1]};{bg_color[2]}m"

def slow_type(t,s):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(1*10.0/s)
    print('')
global currentline
currentline = (0,0)

from FS.lib import task,mem,vbuffer,util
import time
buf = vbuffer.VBuffer()


def print(string:str, color:tuple, pos:tuple=(0,currentline)):
    buf.print(string, color, pos)


buf.print("asdf hi", (255,255,255), (0,0))
buf.print("well hello there second line and colored", (255,0,0), (0,1))

rendered = buf.render()

self.video_buffer = rendered

task.activetask = self

while True:
    rendered = buf.render()

    self.video_buffer = rendered

    task.activetask = self
    time.sleep(5)
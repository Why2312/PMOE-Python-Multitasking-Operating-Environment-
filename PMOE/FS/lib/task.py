import threading
import time

global tasks
tasks = {}
global activetask
activetask = None


class task:
    def __init__(self, code:str, runeveryms:int, loop:bool, name:str):
        self.name = name
        self.code = code
        self.runevery = runeveryms
        self.loop = loop
        self.oloop = loop
        self.startexec = None
        self.process = None
        self.lock = threading.Lock()
        self.show_video = False
        self.video_buffer = []
        tasks[self.name] = self
        
    def start(self):
        self.loop = self.oloop
        process = threading.Thread(target=self.run)
        self.process = process
        time.sleep(0.5)
        process.start()
        
    def run(self):
        self.startexec = True
        exec(self.code, {"self":self})
        self.startexec = False
            
    def pause(self):
        self.lock.acquire()
        
    def resume(self):
        self.lock.release()
        
    def toggle_video(self):
        self.show_video = not self.show_video
        if self.show_video:
            activetask = self
        
    def stop(self):
        self.loop = False
        self.process.join()
        
    def delete(self):
        self.stop()
        self = None
#Documentation:
#For safety, DO NOT USE PRINT(), it will overwrite the screen and cause visual artifacts. Instead, use the vbuffer library, get the text, and set your frame buffer to it. This will help you from having issues.

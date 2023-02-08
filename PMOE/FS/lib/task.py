import threading
import time

global tasks
tasks = {}
global activetask
activetask = None


class task:
    def __init__(self, code:str, runeveryms:int, loop:bool, name:str, rwd:str):
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
        self.rwd = rwd
        
    def start(self):
        self.loop = self.oloop
        process = threading.Thread(target=self.run)
        self.process = process
        process.start()
        tasks[self.name] = self
        return process
        
    def run(self):
        self.startexec = True
        exec(self.code, {"self":self,"rwd":self.rwd})
        self.startexec = False
        tasks[self.name] = None
            
    def pause(self):
        self.lock.acquire()
        tasks[self.name] = None
        
    def resume(self):
        self.lock.release()
        tasks[self.name] = self
        
    def toggle_video(self):
        self.show_video = not self.show_video
        if self.show_video:
            activetask = self
        
    def stop(self):
        self.loop = False
        self.process.join()
        tasks[self.name] = None
        
    def delete(self):
        self.stop()
        tasks[self.name] = None
        self = None
#Documentation:
#For safety, DO NOT USE PRINT(), it will overwrite the screen and cause visual artifacts. Instead, use the vbuffer library, get the text, and set your frame buffer to it. This will help you from having issues.

#Mem lib

size = 1 * 1024 * 1024 #1MB of Virtual RAM

class Memory:
    def __init__(self):
        self.memory = [0 for i in range(size)]
    def setval(self, index, data):
        if data < 0: data = 0
        if data > 255: data = 255
        try:
            self.memory[index] = data
            return True
        except:
            return False
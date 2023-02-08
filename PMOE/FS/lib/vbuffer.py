from FS.lib.util import set_colors


sizey = 75
sizex = 200
size = sizey * sizex

class VBuffer:
    def __init__(self):
        self.text_buffer = [" " for i in range(size)]
        self.color_buffer = [(0,0,0) for i in range(size)]

    def reset(self):
        self.text_buffer = [" " for i in range(size)]
        self.color_buffer = [(0,0,0) for i in range(size)]

    def add_text(self, text: str, color: tuple):
        lines = text.split("\n")
        for line in lines:
            for i, char in enumerate(line):
                self.char(char, color, (i, len(self.text_buffer)))
            self.text_buffer.append(" " * sizex)
            self.color_buffer.extend([(0, 0, 0) for i in range(sizex)])

    def char(self, char: str, color: tuple, location: tuple):
        x, y = location
        if len(self.text_buffer) <= y:
            self.text_buffer.append(" " * sizex)
            self.color_buffer.extend([(0, 0, 0) for i in range(sizex)])
        row = self.text_buffer[y]
        row = row[:x] + char + row[x+1:]
        self.text_buffer[y] = row
        row = self.color_buffer[y*sizex:(y+1)*sizex]
        row = row[:x] + [color] + row[x+1:]
        self.color_buffer[y*sizex:(y+1)*sizex] = row

    def print(self, string: str, color: tuple, location:tuple):
        x, y = location
        lines = string.split("\n")
        for line in lines:
            for i, char in enumerate(line):
                self.char(char, color, (x + i, y))
            y += 1

    def render(self):
        rendered_text = ""
        for y in range(sizey):
            row = self.text_buffer[y]
            colors = self.color_buffer[y*sizex:(y+1)*sizex]
            for x, char in enumerate(row):
                color = colors[x]
                rendered_text += set_colors(text_color=color, bg_color=(0,0,0)) + char
            rendered_text += '\n'
        return rendered_text
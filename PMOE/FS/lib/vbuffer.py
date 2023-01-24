from FS.lib.util import set_colors

size = 320*100

class VBuffer:
    def __init__(self):
        self.text_buffer = [" " for i in range(size)]
        self.bg_color_buffer = [(0,0,0) for i in range(size)]
        self.color_buffer = [(0,0,0) for i in range(size)]

    def add_text(self, text: str, color: tuple):
        self.text_buffer.append(text)
        self.color_buffer.append(color)

    def char(self, char: str, color: tuple, location: tuple):
        x, y = location
        if len(self.text_buffer) <= y:
            self.text_buffer.append(" " * x + char)
            self.color_buffer.append([(0, 0, 0)] * x + [color])
        else:
            row = self.text_buffer[y]
            row = row[:x] + char + row[x+1:]
            self.text_buffer[y] = row
            row = self.color_buffer[y]
            row = row[:x] + [color] + row[x+1:]
            self.color_buffer[y] = row

    def print(self, string: str, color: tuple, location: tuple):
        x, y = location
        lines = string.split("\n")
        for line in lines:
            for i, char in enumerate(line):
                self.char(char, color, (x + i, y))
            y += 1

    def render(self):
        rendered_text = ""
        for y in range(len(self.text_buffer)):
            for x in range(len(self.text_buffer[y])):
                text = self.text_buffer[y][x]
                color = self.color_buffer[y][x]
                color2 = self.background_buffer[y][x]
                rendered_text += set_colors(text_color=color, bg_color=color2) + text
            rendered_text += '\n'
        return rendered_text
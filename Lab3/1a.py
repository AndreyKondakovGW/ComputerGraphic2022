from base_filler import BaseFiller
from tkinter import *

class ColorFiller(BaseFiller):
    def __init__(self, root, color):
        super().__init__(root)
        self.fill_color = color

    def next_color(self, x, y):
        return self.fill_color
        
if __name__ == "__main__":
    root = Tk()
    root.title("Для заливки фигуры используйте двойной щелчок мыши")
    color_filler = ColorFiller(root, (0, 255, 0))
    color_filler.start()
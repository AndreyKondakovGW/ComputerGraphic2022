from primitives import *
from dummy import DummyMode
from mouseLine import MouseLineMode
from line_bresenchem import BerthLineMode
from line_wu import WuLineMode
from poli_line import PoligonMode

class Painter():
    def __init__(self, brush_color = (0, 0, 0)):
        super().__init__()
        self.canvas = None
        self.brush_color = brush_color
        self.current_mode = DummyMode()

    def set_canvas(self, canvas):
        self.canvas = canvas

    def switch_mode(self, new_mode_name):
        if new_mode_name == "paint":
            self.current_mode = MouseLineMode(self.canvas, self.brush_color)
            print("paint")
            pass
        elif new_mode_name == "drawline":
            self.current_mode = BerthLineMode(self.canvas, self.brush_color)
            print("drawline")
            pass
        elif new_mode_name == "drawlinewu":
            self.current_mode = WuLineMode(self.canvas, self.brush_color)
            print("drawlinewu")
            pass
        elif new_mode_name == "drawpoligon":
            self.current_mode = PoligonMode(self.canvas, self.brush_color)
            print("drawpoligon")     
            pass
        elif new_mode_name == "clear":
            self.current_mode = DummyMode()
            self.canvas.delete_content()
            print("clear")
            pass
        else:
            pass

    def hanble_moution(self, event):
        self.current_mode.hanble_moution(event)
    def hanble_press(self, event):
        self.current_mode.hanble_press(event)
    def hanble_release(self, event):
        self.current_mode.hanble_release(event)

    
    
from primitives import *
from dummy import DummyMode
from mouseLine import MouseLineMode
from line import LineMode
from poli_line import PoligonMode
from rect import RectangleMode
from rect_selector import RectSelector
from dot import DotMode
from mark_segments_direction import MarkSegmentsDirectionMode
from check_convex import CheckConvexMode

class Painter():
    def __init__(self, brush_color = (0, 0, 0)):
        super().__init__()
        self.canvas = None
        self.brush_color = brush_color
        self.current_mode = DummyMode()

    def set_canvas(self, canvas):
        self.canvas = canvas

    def switch_mode(self, new_mode_name):
        if new_mode_name == "dot":
            self.current_mode = DotMode(self.canvas, self.brush_color)
            print("dot")
        elif new_mode_name == "paint":
            self.current_mode = MouseLineMode(self.canvas, self.brush_color)
            print("paint")
        elif new_mode_name == "drawline":
            self.current_mode = LineMode(self.canvas, self.brush_color, "bresenchem")
            print("drawline")
        elif new_mode_name == "drawlinewu":
            self.current_mode = LineMode(self.canvas, self.brush_color, "wu")
            print("drawlinewu")
        elif new_mode_name == "drawpoligon":
            self.current_mode = PoligonMode(self.canvas, self.brush_color)
            print("drawpoligon")     
        elif new_mode_name == "drawrectangle":
            self.current_mode = RectangleMode(self.canvas, self.brush_color)
            print("drawrectangle")     
        elif new_mode_name == "marksegments":
            self.current_mode = MarkSegmentsDirectionMode(self.canvas, self.brush_color)
            print("marksegments")
        elif new_mode_name == "checkconvex":
            self.current_mode = CheckConvexMode(self.canvas, self.brush_color)
            print("checkconvex")
        elif new_mode_name == "selectrectangle":
            self.current_mode = RectSelector(self.canvas, self.brush_color)
            print("drawrectangle")     
        elif new_mode_name == "delselected":
            #self.current_mode = DummyMode()
            self.canvas.delete_selected()
            print("delselected")
        elif new_mode_name == "clear":
            self.current_mode = DummyMode()
            self.canvas.delete_content()
            print("clear")
        else:
            pass
    
    def hanble_moution(self, event):
        self.current_mode.hanble_moution(event)
    def hanble_press(self, event):
        self.current_mode.hanble_press(event)
    def hanble_release(self, event):
        self.current_mode.hanble_release(event)

    
    
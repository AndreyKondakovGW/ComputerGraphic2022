from functions import *
from primitives import *
from transformation import *

class MoverMode:
    def __init__(self, canvas):
        self.canvas = canvas
        self.should_draw = False
        self.p0 = None

    def hanble_moution(self, event):
        if self.p0 is not None:
            k_x = int(event.x - self.p0[0])
            k_y = int(event.y - self.p0[1])
            fig = self.canvas.content
            for f in fig:
                old_points = f.points
                if f.selected:
                    translation(f, k_x, k_y)
                if intersection_with_scope(f,self.canvas):
                    f.points = old_points
            self.p0 = (event.x, event.y)
            self.canvas.redraw_content()
            

    def hanble_press(self, event):
        self.should_draw = True
        self.p0 = (event.x, event.y)

    def hanble_release(self, _):
        self.should_draw = False
        self.p0 = None

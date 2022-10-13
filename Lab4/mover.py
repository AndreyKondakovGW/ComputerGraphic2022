from .functions import *
from .transformation import *
from src.controller_mode import ControllerMode

def move_figure(fig, dx, dy, max_height, max_width):
    old_points = fig.points
    if fig.selected:
        translation(fig, dx, dy)
        if intersection_with_scope(fig, max_height, max_width):
            fig.points = old_points

class MoverMode(ControllerMode):
    def __init__(self, canvas):
        self.canvas = canvas
        self.should_draw = False
        self.p0 = None

    def hanble_moution(self, event):
        if self.p0 is not None:
            k_x = int(event.x - self.p0[0])
            k_y = int(event.y - self.p0[1])
            max_height, max_width = self.canvas.height, self.canvas.width
            self.canvas.storage.apply(lambda fig: move_figure(fig, k_x, k_y, max_height, max_width))
            self.canvas.redraw()
            self.p0 = (event.x, event.y)

    def hanble_press(self, event):
        self.should_draw = True
        self.p0 = (event.x, event.y)

    def hanble_release(self, _):
        self.should_draw = False
        self.p0 = None

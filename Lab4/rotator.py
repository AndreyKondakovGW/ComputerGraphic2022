from .functions import *
from .transformation import *
from src.controller_mode import ControllerMode

def rotate_figure(fig, angle, point, max_height, max_width):
    old_points = fig.points
    if fig.selected:
        rotation(fig, angle, point)
        if intersection_with_scope(fig, max_height, max_width):
            fig.points = old_points

class RotatorMode(ControllerMode):
    def __init__(self, canvas):
        self.canvas = canvas
        self.p0 = None

    def hanble_mouse_wheel(self, event):
        if self.p0 is not None:
            point = self.p0
        else:
            point = (-1, -1)
        angle = event.delta // 120
        max_height, max_width = self.canvas.height, self.canvas.width
        self.canvas.storage.apply(lambda fig: rotate_figure(fig, angle, point, max_height, max_width))
        self.canvas.redraw()

    def hanble_press(self, event):
        self.p0 = (event.x, event.y)
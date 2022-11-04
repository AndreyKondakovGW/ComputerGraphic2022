from .functions import *
from .transformation import *
from src.controller_mode import ControllerMode
from .dot import Dot
from src.point import Point

def scale_figure(fig, kx, ky, point, max_height, max_width):
    old_points = fig.points
    if fig.selected:
        scaling(fig, kx, ky, point)
        if intersection_with_scope(fig, max_height, max_width):
            fig.points = old_points

class ScalerMode(ControllerMode):
    def __init__(self, canvas):
        self.canvas = canvas
        self.p0 = None
        self.p1 = None

    def hanble_moution(self, event):
        if self.p0 is not None and self.p1 is not None:
            point1 = Dot(self.p1)
            point1.selected = True
            dx = abs(event.x - self.p0.x)
            dy = abs(event.y - self.p0.y)

            kx = dx / abs(self.p1.x - self.p0.x)
            ky = dy / abs(self.p1.y - self.p0.y)

            max_height, max_width = self.canvas.height, self.canvas.width

            self.canvas.storage.apply(lambda fig: scale_figure(fig, kx, ky, self.p0, max_height, max_width))
            
            scale_figure(point1, kx, ky, self.p0, max_height, max_width)
            self.p1 = point1.points[0]
            self.canvas.redraw()
            self.canvas.draw_line((self.p0.x, self.p0.y), (event.x, event.y))
            self.canvas.draw_circle(self.p0.x, self.p0.y, 5, (255, 0, 0))
            self.canvas.draw_circle(self.p1.x, self.p1.y, 5, (255, 0, 0))

    def hanble_press(self, event):
        if self.p0 is None:
            self.p0 = Point(event.x, event.y)
            self.canvas.draw_circle(self.p0.x, self.p0.y, 5, (255, 0, 0))
        else:
            if self.p1 is None:
                self.p1 = Point(event.x, event.y)
                self.canvas.draw_circle(self.p1.x, self.p1.y, 5, (255, 0, 0))
            else:
                self.p0 = None
                self.p1 = None
                self.canvas.redraw()
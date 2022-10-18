import numpy as np
from .point import Point
from Lab6.projections import *

class Drawer:
    def __init__(self, canvas):
        self.mode = "2D"
        self.canvas = canvas
        self.projection = akso_projection()
        pass
    
    def set_mode(self, mode):
        self.mode = mode

    def draw_point(self, point, color=(0, 0, 0)):
        if self.mode == "2D":
            self.canvas.draw_circle(point.x, point.y, 3, color=color)
        elif self.mode == "3D":
            pass
        pass

    def draw_line(self, points):
        if self.mode == "2D":
            self.canvas.draw_line((points[0].x, points[0].y), (points[1].x, points[1].y))
        elif self.mode == "3D":
            points = [self.translate_point(p) for p in points]
            self.canvas.draw_line((points[0].x, points[0].y), (points[1].x, points[1].y))
    
    def translate_point(self, point):
        p0 = [[point.x, point.y, point.z, 1]]
        p = np.dot(p0, self.projection)[0]
        return Point(p[0] / p[3], p[1] / p[3], 0)

    def draw_edge(self, points):
        if self.mode == "2D":
            pass
        elif self.mode == "3D":
            pass
        pass
from tkinter import PhotoImage, Tk,  Canvas
from drawer_point import DrawerPoint
#from transformation import rotation
from typing import Tuple

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
lab4dir = os.path.join(parentdir, "Lab4")
sys.path.insert(0, lab4dir) 

from transformation import rotation
from primitives import line_bresenchem

class Drawer:
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        self.step_size = None
        self.points = []

    def set_starting_point(self, x, y):
        self.clear()
        self.current_point = DrawerPoint(x, y)
        self.points.append((x, y))

    def set_step_size(self, step_size):
        self.step_size = step_size
        if self.direction:
            self.direction = self.direction.normalized() * step_size
        else:
            self.direction = self.default_direction()

    def set_direction(self, direction: Tuple):
        new_direction = DrawerPoint.from_tuple(direction)
        eps = 1e-4
        if new_direction.length() > 1.0 + eps:
            return
        self.direction = new_direction
        if self.step_size:
            self.direction *= self.step_size

    def step(self):
        new_point = self.current_point + self.direction
        x2 = round(new_point.x)
        y2 = round(new_point.y)
        color = (255, 0, 0)
        #line_bresenchem(self.canvas.image, (x1, y1), (x2, y2), color)
        self.points.append((x2, y2))
        self.current_point = DrawerPoint(x2, y2)

    def rotate(self, angle):
        rotation(self.direction, angle, point=(0,0))
        self.direction.x = self.direction.points[0][0]
        self.direction.y = self.direction.points[0][1]

    def default_direction(self):
        return DrawerPoint(self.step_size, 0)

    def clear(self):
        self.points = []

    def draw_from_points(self):
        first_point = self.points[0]
        for point in self.points[1:]:
            line_bresenchem(self.canvas.image, first_point, point)
            first_point = point

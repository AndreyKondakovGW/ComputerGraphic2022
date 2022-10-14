from tkinter import PhotoImage, Tk,  Canvas
from drawer_point import DrawerPoint
#from transformation import rotation
from typing import Tuple
import random

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
        self.edges = []
        self.colors = []
        self.thiknesses = []
        self.last_point_index = -1

    def set_starting_point(self, x, y):
        self.clear()
        brown = (139, 69, 19)
        self.current_color = brown
        self.current_thikness = 6
        self.points.append((x, y))
        self.colors.append(brown)
        self.set_point(x, y)
        self.last_point_index = 0

    def set_point(self, x, y):
        self.current_point = DrawerPoint(x, y)

    def set_drawer_point(self, dp: DrawerPoint):
        self.current_point = dp
        point_tuple = (dp.x, dp.y)
        self.points.append(point_tuple)
        self.colors.append(self.current_color)
        self.thiknesses.append(self.current_thikness)
        self.last_point_index += 1

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

    def set_drawer_direction(self, direction: DrawerPoint):
        self.direction = direction

    def set_random(self, is_random):
        self.is_random = is_random

    def set_dynamic(self, is_dynamic):
        self.is_dynamic = is_dynamic
        self.current_thikness = 6

    def step(self):
        x2, y2 = self.next_point_tuple()
        self.update_points((x2, y2))
        edge = (self.last_point_index, self.last_point_index + 1)
        self.update_edges(edge)
        self.current_point = DrawerPoint(x2, y2)
        self.last_point_index += 1

    def next_point_tuple(self):
        new_point = self.current_point + self.direction
        x2 = round(new_point.x)
        y2 = round(new_point.y)
        return x2, y2

    def update_points(self, point):
        self.points.append(point)
        self.colors.append(self.current_color)
        self.thiknesses.append(self.current_thikness)

    def update_edges(self, edge):
        self.edges.append(edge)

    def rotate(self, angle):
        if self.is_random:
            angle = self.random_angle(angle)
        rotation(self.direction, angle, point=(0,0))
        self.direction.x = self.direction.points[0][0]
        self.direction.y = self.direction.points[0][1]

    def random_angle(self, angle):
        delta_angle = 20
        if angle > 0:
            return random.randint(angle-delta_angle, angle)
        if angle < 0:
            return -random.randint(-angle-delta_angle, -angle)
        return 0;

    def set_color(self, new_color):
        self.current_color = new_color

    def set_thikness(self, thikness):
        if thikness >= 1:
            self.current_thikness = thikness
        else:
            self.current_thikness = 1

    def default_direction(self):
        return DrawerPoint(self.step_size, 0)

    def clear(self):
        self.points = []
        self.edges = []
        self.colors = []

    def draw_from_edges(self):
        print("draw from edges")
        for e in self.edges:
            ind1, ind2 = e
            p1 = self.points[ind1]
            p2 = self.points[ind2]
            c1 = self.colors[ind1]
            c2 = self.colors[ind2]
            thikness = self.thiknesses[ind1]
            self.draw_line(p1, p2, c1, c2, thikness)
            #line_bresenchem(self.canvas.image, p1, p2, c1, c2)

    def draw_line(self, p1, p2, c1, c2, thikness):
        if self.is_dynamic:
            self.draw_thick_line(p1, p2, c1, c2, thikness)
        else:
            line_bresenchem(self.canvas.image, p1, p2, c1, c2)

    def draw_thick_line(self, p1, p2, c1, c2, thikness):
        if thikness == 1:
            line_bresenchem(self.canvas.image, p1, p2, c1, c2)
            return
        for i in range(-thikness // 2, thikness // 2):
            pi1 = self.clamp_point(p1[0] + i, p1[1])
            pi2 = self.clamp_point(p2[0] + i, p2[1])
            line_bresenchem(self.canvas.image, pi1, pi2, c1, c2)

    def clamp_point(self, x, y):
        if x < 0:
            x = 1
        if y < 0:
            y = 1
        return x, y

    def draw_from_points(self):
        first_point = self.points[0]
        first_color = self.colors[0]
        for i in range(1, len(self.points)):
            line_bresenchem(self.canvas.image, first_point, self.points[i], first_color, self.colors[i])
            first_point = self.points[i]

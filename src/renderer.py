import numpy as np
from .point import Point
from Lab6.projections import *

class Renderer:
    def __init__(self, canvas):
        self.canvas = canvas
        self.projection = simple2D_projection()
    
    def set_projection(self, projection):
        self.projection = projection

    def render_scene(self, scene):
        self.canvas.clear()
        for figure in scene.storage:
            figure.draw(self)

    def draw_point(self, point, color=(0, 0, 0)):
        point = self.translate3D_point(point)
        pointC = self.canvas.draw_circle(point.x, point.y, 3, color=color)
        return Point(pointC[0], pointC[1])

    def draw_line(self, points, color=(0, 0, 0)):
        points = [self.translate3D_point(p) for p in points]
        p1, p2 = self.canvas.draw_line((points[0].x, points[0].y), (points[1].x, points[1].y), color)
        return [Point(p1[0], p1[1]), Point(p2[0], p2[1])]
            

    def draw_edge(self, points):
        points = [self.translate3D_point(p) for p in points]
        for i,_ in enumerate(points):
            if i == len(points) - 1:
                self.canvas.draw_line((points[i].x, points[i].y), (points[0].x, points[0].y))
            else:
                self.canvas.draw_line((points[i].x, points[i].y), (points[i+1].x, points[i+1].y))

    def translate3D_point(self, point):
        p0 = [[point.x, point.y, point.z, 1]]
        p = np.dot(p0, self.projection)[0]
        return Point(p[0] / p[3], p[1] / p[3], 0)
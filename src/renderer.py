import numpy as np
from .point import Point
from Lab6.projections import *

class Renderer:
    def __init__(self, canvas):
        self.gridX = True
        self.gridY = False
        self.gridZ = False
        self.camera = None
        self.canvas = canvas
        self.projection = simple2D_projection()
        self.center = Point(self.canvas.width / 2, self.canvas.height / 2)
    
    def set_projection(self, projection):
        self.projection = projection

    def render_scene(self, scene):
        self.canvas.clear()
        self.draw_axes()
        #self.show_grid()
        for figure in scene.storage:
            figure.mark_undrawed()
            figure.draw(self)

    def draw_axes(self):
        self.draw_line([Point(- 200 , 0, 0), Point(200, 0, 0)], color=(255, 0, 0), thickness = 4)
        self.draw_line([Point(0, - 200, 0), Point(0,  200, 0)], color=(0, 255, 0), thickness = 4)
        self.draw_line([Point(0, 0, - 200), Point(0, 0, 200)], color=(0, 0, 255), thickness = 4)

    def show_grid(self):
        if self.gridX:
            self.draw_gridX()
        if self.gridY:
            self.draw_gridY()
        if self.gridZ:
            self.draw_gridZ()

    def draw_direction(self, p, direction, size = 50):
        color = (150 * abs(direction.x), 150 * abs(direction.y), 150 * abs(direction.z))
        direction.x = p.x + direction.x * size
        direction.y = p.y + direction.y * size
        direction.z = p.z + direction.z * size
        self.draw_line([p, direction], color=color, thickness = 4)


    def draw_gridX(self):
        for i in range(-self.canvas.width, self.canvas.width, 50):
            self.draw_line([Point(i, 0, -self.canvas.width), Point(i, 0, self.canvas.width)], color=(200, 200, 200), thickness=1)
            self.draw_line([Point(-self.canvas.width, 0, i), Point(self.canvas.width, 0, i)], color=(200, 200, 200), thickness=1)
    
    def draw_gridY(self):
        for i in range(-self.canvas.width, self.canvas.width, 50):
            self.draw_line([Point(0, -self.canvas.width, i), Point(0, self.canvas.width, i)], color=(200, 200, 200), thickness=1)
            self.draw_line([Point(0, i, -self.canvas.width, i), Point(0, i, self.canvas.width)], color=(200, 200, 200), thickness=1)

    def draw_gridZ(self):
        for i in range(-self.canvas.width, self.canvas.width, 50):
            self.draw_line([Point(i, -self.canvas.width, 0), Point(i, self.canvas.width, 0)], color=(200, 200, 200), thickness=1)
            self.draw_line([Point(-self.canvas.width, i, 0), Point(self.canvas.width, i, 0)], color=(200, 200, 200), thickness=1)

    def draw_point(self, point, color=(0, 0, 0)):
        point = self.translate3D_point(point)
        self.canvas.draw_circle(point.x, point.y, 3, color=color)

    def draw_line(self, points, color=(0, 0, 0), thickness = 2):
        trans_points = [self.translate3D_point(p) for p in points]
        self.canvas.draw_line((trans_points[0].x, trans_points[0].y), (trans_points[1].x, trans_points[1].y), color, thickness=thickness)   

    def translate3D_point(self, point):
        p0 = np.array([[point.x, point.y, point.z, 1]])
        if self.camera:
            p0 = p0.T
            p0 = np.dot(self.camera.lookAtMatrix, p0)
            p0 = np.dot(self.camera.projection_matrix, p0)
            p = (p0.T)[0]
            p[0] = p[0] / p[3]
            p[1] = p[1] / p[3]
            return self.center + Point(p[0] * self.canvas.width // 2, -p[1]*self.canvas.height // 2, 0)
        p0 = np.dot(p0, self.projection)
        p = p0[0]
        return self.center + Point(p[0] / p[3], -(p[1] / p[3]), 0)
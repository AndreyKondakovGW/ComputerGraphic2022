from src.point import Point
import numpy as np
from math import pi, tan, cos, sin, sqrt, asin, acos
class Camera:
    def __init__(self, pos, target = Point(0,0,0), aspect=1):
        self.position = pos
        self.target = target

        self.fov = pi / 2
        self.aspect_ratio = 1 / aspect
        self.near = 1
        self.far = 1000
        self.direction = (self.position - self.target).normalize()
        self.pitch = asin(self.direction.y)
        self.yaw = acos(self.direction.x / cos(self.pitch))

        self.projection_matrix = self.get_projection()
        self.lookAtMatrix = self.count_lookAtMatrix()

    def change_position(self, delta):
        self.position = self.position + delta
        self.direction = (self.position - self.target).normalize()
        self.lookAtMatrix = self.count_lookAtMatrix()
    
    def change_rotation(self, dyaw, dpitch):
        self.yaw += dyaw
        self.pitch += dpitch

        self.direction = Point(cos(self.yaw) * cos(self.pitch), sin(self.pitch), sin(self.yaw) * cos(self.pitch)).normalize()
        self.right = Point(0,1,0).cross(self.direction).normalize()
        self.up = self.direction.cross(self.right)

        self.lookAtMatrix = self.count_lookAtMatrix()


    def count_axis_param(self):
        self.right = Point(0,1,0).cross(self.direction).normalize()
        self.up = self.direction.cross(self.right)

    def count_lookAtMatrix(self):
        self.count_axis_param()
        axis_matrix = np.array([
            [self.right.x, self.right.y, self.right.z, 0],
            [self.up.x, self.up.y, self.up.z, 0],
            [self.direction.x, self.direction.y, self.direction.z, 0],
            [0, 0, 0, 1]
        ])

        position_matrix = np.array([
            [1, 0, 0, -self.position.x],
            [0, 1, 0, -self.position.y],
            [0, 0, 1, -self.position.z],
            [0, 0, 0, 1]
        ])

        return axis_matrix.dot(position_matrix)

    def get_projection(self):
        f = 1 / tan(self.fov / 2)
        aspect = self.aspect_ratio
        a = (self.far + self.near) / (self.far - self.near)
        b = (2 * self.far * self.near) / (self.far - self.near)

        return np.array([
            [f * aspect, 0, 0, 0],
            [0, f, 0, 0],
            [0, 0, -a, -1],
            [0, 0, b, 0]
        ]).T

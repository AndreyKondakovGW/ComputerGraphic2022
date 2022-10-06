from math import radians, sin, cos

import numpy as np


# class AffineTranslation:
#     def __int__(self):
#
#
#     def hanble_moution(self, event):
#
# 
#     def hanble_press(self, event):
#         self.current_mode.hanble_press(event)
#
#     def hanble_release(self, event):
#         self.current_mode.hanble_release(event)

def translation_matrix(dx, dy):
    return [[1, 0, 0],
            [0, 1, 0],
            [dx, dy, 1]]


def rotate_matrix(angle):
    return [[cos(radians(angle)), sin(radians(angle)), 0],
            [-sin(radians(angle)), cos(radians(angle)), 0],
            [0, 0, 1]]


def scale_matrix(kx, ky):
    return [[kx, 0, 0],
            [0, ky, 0],
            [0, 0, 1]]


def translation(fig, dx, dy):
    m = translation_matrix(dx, dy)
    new_points = list()
    for point in fig.points:
        p1, p2 = point
        point1 = np.dot([p1, p2, 1], m).astype(int)
        new_points.append((point1[0], point1[1]))
    fig.points = new_points


def rotation(fig, angle, point=[-1, -1]):
    m = rotate_matrix(angle)
    new_points = list()
    if [-1, -1] == point:
        point = centroid(fig.points)
    translation(fig, -point[0], -point[1])
    for point_f in fig.points:
        p1, p2 = point_f
        point1 = np.dot([p1, p2, 1], m).astype(int)
        new_points.append((point1[0], point1[1]))
    fig.points = new_points
    translation(fig, point[0], point[1])


def scaling(fig, kx, ky, point=[-1, -1]):
    # if point == (0,0):
    #   point =  центр масс
    m = scale_matrix(kx, ky)
    new_points = list()
    if [-1, -1] == point:
        point = centroid(fig.points)
    translation(fig, -point[0], -point[1])
    for point_f in fig.points:
        p1, p2 = point_f
        point1 = np.dot([p1, p2, 1], m).astype(int)
        new_points.append((point1[0], point1[1]))
    fig.points = new_points
    translation(fig, point[0], point[1])


def centroid(vertexes):
    _x_list = [vertex[0] for vertex in vertexes]
    _y_list = [vertex[1] for vertex in vertexes]
    _len = len(vertexes)
    _x = sum(_x_list) / _len
    _y = sum(_y_list) / _len
    return (_x, _y)

import math

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
    return [[math.cos(angle), math.sin(angle), 0],
            [-math.sin(angle), math.cos(angle), 0],
            [0, 0, 1]]


def scale_matrix(kx, ky):
    return [[1//kx, 0, 0],
            [0, 1//ky, 0],
            [0, 0, 1]]


def translation(fig, dx, dy):
    m = translation_matrix(dx, dy)
    new_points = list()
    for f in fig:
        for point in f.points:
            p1, p2 = point
            point1 = np.dot([p1, p2, 1], m)
            new_points.append((point1[0], point1[1]))
        f.points = new_points
    print('end tr')


def rotate(fig, angle, point=[0, 0]):
    m = rotate_matrix(angle)
    for point_f in fig:
        np.dot(m, point_f + point)
    return fig


def scale(fig, kx, ky, point=[0, 0]):
    # if point == (0,0):
    #   point =  центр масс
    for point_f in fig:
        m = scale_matrix(kx, ky)
        np.dot(m, point_f - point)
    return fig

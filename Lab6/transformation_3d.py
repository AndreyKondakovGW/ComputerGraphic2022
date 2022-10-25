from math import radians, sin, cos

from src.point import Point
import numpy as np

def translation_matrix(dx, dy, dz):
    return [[1,  0,  0,  0],
            [0,  1,  0,  0],
            [0,  0,  1,  0],
            [dx, dy, dz, 1]]

def scale_matrix(kx, ky, kz):
    return [[kx, 0,  0,  0],
            [0,  ky, 0,  0],
            [0,  0,  kz, 0],
            [0,  0,  0,  1]]

def rotation_around_vector_matrix(dir, angle):
    x, y, z = dir
    rad_angle = radians(angle)
    cos_angle = cos(rad_angle)
    sin_angle = sin(rad_angle)
    x2 = x*x
    y2 = y*y
    z2 = z*z
    # return [[l2 + cos_angle*(1 - l2), l*(1-cos_angle)*m + n*sin_angle, l*(1-cos_angle)*n + m*sin_angle, 0],
    #         [l*(1-cos_angle)*m - n*sin_angle, m2 + cos_angle*(1-m2),   m*(1-cos_angle)*n + l*sin_angle, 0],
    #         [l*(1-cos_angle)*n + m*sin_angle, m*(1-cos_angle)*n + l*sin_angle, n2 + cos_angle*(1-n2),   0], 
    #         [0, 0, 0, 1]]
    return [[cos_angle + (1-cos_angle)*x2, (1-cos_angle)*x*y - sin_angle*z, (1-cos_angle)*x*z + sin_angle*y, 0],
            [(1-cos_angle)*y*x + sin_angle*z, cos_angle + (1-cos_angle)*y2, (1-cos_angle)*y*z - sin_angle*x, 0],
            [(1-cos_angle)*z*x - sin_angle*y, (1-cos_angle)*z*y + sin_angle*x, cos_angle + (1-cos_angle)*z2, 0],
            [0, 0, 0, 1]]

def rotation_matrix(a, dir, angle):
    x, y, z = a
    translate_to_a = translation_matrix(-x, -y, -z)
    rotation = rotation_around_vector_matrix(dir, angle)
    translate_back = translation_matrix(x, y, z)
    return np.dot(np.dot(translate_to_a, rotation), translate_back)


def apply_matrix_to_point(point, matrix):
    px, py, pz = point.x, point.y, point.z
    point_vector = [px, py, pz, 1]
    new_point_arr = np.dot(point_vector, matrix)
    point.x = new_point_arr[0]
    point.y = new_point_arr[1]
    point.z = new_point_arr[2]

def apply_matrix_to_points(points, matrix):
    for point in points:
        apply_matrix_to_point(point, matrix)

def translate(points, dx, dy, dz):
    matrix = translation_matrix(dx, dy, dz)
    apply_matrix_to_points(points, matrix)

def rotate(points, a, dir, angle):
    dir = normalize_vector_tuple(dir)
    matrix = rotation_matrix(a, dir, angle)
    apply_matrix_to_points(points, matrix)

def normalize_vector_tuple(vector_tuple):
    x, y, z = vector_tuple[0], vector_tuple[1], vector_tuple[2]
    l = (x**2 + y**2 + z**2)**0.5
    return (x/l, y/l, z/l)

def scale(points, kx, ky, kz, scaling_center=None):
    if scaling_center is None:
        scaling_center = centroid(points)
    dx, dy, dz = -scaling_center[0], -scaling_center[1], -scaling_center[2]
    translate(points, dx, dy, dz)
    just_scale(points, kx, ky, kz)
    translate(points, -dx, -dy, -dz)

def just_scale(points, kx, ky, kz):
    matrix = scale_matrix(kx, ky, kz)
    apply_matrix_to_points(points, matrix)

def centroid(points):
    xs = [point.x for point in points]
    ys = [point.y for point in points]
    zs = [point.z for point in points]
    l = len(points)
    x = sum(xs) / l
    y = sum(ys) / l
    z = sum(zs) / l
    return (x, y, z)
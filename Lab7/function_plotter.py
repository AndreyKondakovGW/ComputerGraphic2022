from typing import Callable
from Lab7.function_plotter_modal_window import FunctionPlotterModalWindow
from Lab6.figures.line3D import Line3D
from Lab6.figures.polyhedron import Polyhedron, Face3D
from src.point import Point
from math import *

class Function3D:
    def __init__(self, callable_f, xa, xb, ya, yb):
        self.callable_f = callable_f
        self.xa = xa
        self.xb = xb
        self.ya = ya
        self.yb = yb

def plot(root, points_along_axis_count=100, color=(0,0,0)):
    function = get_plot_data(root)
    poly = get_plot_polygon(function, points_along_axis_count, color)
    print(poly)
    return poly

def get_plot_data(root):
    popup = FunctionPlotterModalWindow(root)
    root.wait_window(popup.popup)
    callable_f = lambda x, y: eval(popup.f)
    xa, xb = popup.xa, popup.xb
    ya, yb = popup.ya, popup.yb
    return Function3D(callable_f, xa, xb, ya, yb)
    
def get_plot_polygon(function: Function3D, points_along_axis_count: int, color=(0,0,0)):
    step_x = (function.xb - function.xa) / points_along_axis_count
    step_y = (function.yb - function.ya) / points_along_axis_count
    xs = get_arguments_list(function.xa, function.xb, step_x)
    ys = get_arguments_list(function.ya, function.yb, step_y)
    points = get_points_matrix(function.callable_f, xs, ys)
    polygon = Polyhedron(color)
    for i in range(0, len(xs) - 1):
        for j in range(0, len(ys) - 1):
            p1 = points[i][j]
            p2 = points[i+1][j]
            p3 = points[i+1][j+1]
            p4 = points[i][j+1]
            polygon.points.append(p1)
            polygon.points.append(p2)
            polygon.points.append(p3)
            polygon.points.append(p4)
            triangle1 = get_triangle(p1, p2, p3)
            triangle2 = get_triangle(p1, p3, p4)
            polygon.faces.append(triangle1)
            polygon.faces.append(triangle2)
    return polygon

def get_points_matrix(f, xs, ys):
    points = []
    for x in xs:
        row = []
        for y in ys:
            row.append(Point(x, f(x, y), y))
        points.append(row)
    return points

def get_arguments_list(a, b, step):
    args = []
    arg = a
    while (arg < b):
        args.append(arg)
        arg += step
    return args

def get_triangle(p1: Point, p2: Point, p3: Point, color=(0,0,0)):
    e1 = Line3D(p1, p2)
    e2 = Line3D(p2, p3)
    e3 = Line3D(p3, p1)
    return Face3D([e1, e2, e3], color)

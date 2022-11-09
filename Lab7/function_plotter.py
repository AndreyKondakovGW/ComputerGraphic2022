from typing import Callable
from Lab7.function_plotter_modal_window import FunctionPlotterModalWindow
from Lab6.figures.line3D import Line3D
from Lab6.figures.polyhedron import Polyhedron, Face3D
from src.point import Point

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
    x = function.xa
    x2 = x + step_x
    f = function.callable_f
    polygon = Polyhedron(color)
    while (x2 < function.xb):
        y = function.ya
        y2 = y + step_y
        while (y2 < function.yb):
            p1 = Point(x, y, f(x, y))
            p2 = Point(x2, y, f(x2, y))
            p3 = Point(x2, y2, f(x2, y2))
            p4 = Point(x, y2, f(x, y2))
            polygon.points.append(p1)
            polygon.points.append(p2)
            polygon.points.append(p3)
            polygon.points.append(p4)
            triangle1 = get_triangle(p1, p2, p3)
            triangle2 = get_triangle(p1, p3, p4)
            polygon.faces.append(triangle1)
            polygon.faces.append(triangle2)
            y = y2
            y2 = y + step_y
        x = x2
        x2 = x + step_x
    return polygon
    
def get_triangle(p1: Point, p2: Point, p3: Point, color=(0,0,0)):
    e1 = Line3D(p1, p2)
    e2 = Line3D(p2, p3)
    e3 = Line3D(p3, p1)
    return Face3D([e1, e2, e3], color)

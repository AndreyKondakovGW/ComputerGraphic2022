from .line_intersector import draw_intersections_with_line
from src.figure import Figure
from src.controller_mode import ControllerMode
from functions import *

class LineMode(ControllerMode):
    def __init__(self, canvas, color = (0,0,0), line_type="bresenchem"):
        self.canvas = canvas
        self.line_type = line_type
        self.brush_color = color
        self.points = []

        self.should_draw = False
        self.p0 = None

    def hanble_moution(self, event):
        if self.p0 is not None:
            self.canvas.redraw()
            self.canvas.draw_line(self.p0, (event.x, event.y), self.brush_color, self.line_type)
            draw_intersections_with_line(self.canvas, self.p0, (event.x, event.y))

    def hanble_press(self, event):
        if self.p0 is None:
            self.p0 = (event.x, event.y)
            self.points.append(self.p0)
        else:
            self.points.append((event.x, event.y))
            self.canvas.storage.add_figure(Line(self.points, self.brush_color))

            self.points = []
            self.p0 = None

class Line(Figure):
    def __init__(self,points, color, line_type="bresenchem"):
        super().__init__(color)
        self.line_type = line_type
        self.points = points

    def draw(self, canvas):
        self.draw_colored(canvas, self.brush_color)

    def draw_colored(self, canvas, color):
        canvas.draw_line(self.points[0], self.points[1], color, self.line_type)

    def find_intersec(self, p1, p2):
        p = find_segments_intersection(p1, p2, self.points[0], self.points[1])
        if p is not None:
            return [p]
        return []

    def draw_marked(self, canvas, p, left_color, right_color):
        if point_from_left(p, self.points[0], self.points[1]):
            color = left_color
        else:
            color = right_color
        self.draw_colored(canvas, color)
        
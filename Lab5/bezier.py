from src.figure import Figure
from src.controller_mode import ControllerMode
from .bezier_curve import draw_bezier_curve

class BezierMode(ControllerMode):
    def __init__(self, canvas, color=(0,0,0)):
        self.canvas = canvas
        self.brush_color = color
        self.points = []

    def hanble_press(self, event):
        self.canvas.redraw()
        p = (event.x, event.y)
        self.points.append((event.x, event.y))
        for p in self.points:
            self.canvas.draw_circle(p[0], p[1], 3, color=(127, 0, 127))
        draw_bezier_curve(self.canvas)


class Dot(Figure):
    def __init__(self, p, color = (0,0,0)):
        super().__init__(color)
        self.points = [p]

    def draw(self, canvas):
        x, y = self.points[0]
        canvas.draw_circle(x, y, 2, self.brush_color)

    def find_intersec(self, p1, p2):
        return []

    def draw_marked(self, canvas, _p, _left_color, _right_color):
        self.draw(canvas)
from src.point import Point
from src.figure import Figure

class Line3D(Figure):
    def __init__(self, points, color=(0, 0, 0)):
        super().__init__(color)
        self.points = points

    def draw(self, drawer):
        self.canvas_points = drawer.draw_line(self.points, self.brush_color)
from src.point import Point
from src.figure import Figure

class Line3D(Figure):
    def __init__(self, p1, p2, color=(0, 0, 0)):
        super().__init__(color)
        self.points = [p1, p2]

    def draw(self, renderer):
        super().draw(renderer)
        self.canvas_points = renderer.draw_line(self.points, self.brush_color)
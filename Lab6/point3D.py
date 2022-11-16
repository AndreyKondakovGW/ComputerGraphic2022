from src.figure import Figure
from src.point import Point

class Point3D(Figure):
    def __init__(self, point, color=(0, 0, 0)):
        super().__init__(color)
        self.points.append(point)
        self.point = point

    def draw(self, drawer):
        canvas_p = drawer.draw_point(self.point, self.brush_color)
        self.canvas_points = [canvas_p]
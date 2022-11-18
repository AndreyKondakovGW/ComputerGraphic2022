from src.point import Point
from src.figure import Figure

class Line3D(Figure):
    def __init__(self, p1, p2, color=(0, 0, 0)):
        super().__init__(color)
        self.points = [p1, p2]
        self.drawed = False

    def draw(self, renderer):
        if not self.drawed:
            super().draw(renderer)
            renderer.draw_line(self.points, self.brush_color)
            self.drawed = True
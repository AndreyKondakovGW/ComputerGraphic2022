from src.figure import Figure
from src.point import Point

class LineM(Figure):
    def __init__(self, points):
        self.points = points

    def draw(self, drawer):
        drawer.draw_line(self.points)
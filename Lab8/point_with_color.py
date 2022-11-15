from src.point import Point

class PointWithColor(Point):
    def __init__(self, x, y, z, color):
        super().__init__(x, y, z)
        self.color = color

    def from_point(point, color=(0,0,0)):
        return PointWithColor(point.x, point.y, point.z, color)
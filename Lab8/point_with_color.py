from src.point import Point

class PointWithColor(Point):
    def __init__(self, x, y, z, color):
        super().__init__(x, y, z)
        self.color = color

    def from_point(point, color=(0,0,0)):
        return PointWithColor(point.x, point.y, point.z, color)

    def __add__(self, other):
        if isinstance(other, PointWithColor):
            color = self.add_colors(self.color, other.color)
        else:
            color = self.color
        return PointWithColor(self.x + other.x, self.y + other.y, self.z + other.z, color) 
    
    def add_colors(self, color1, color2):
        r = color1[0] + color2[0]
        g = color1[1] + color2[1]
        b = color1[2] + color2[2]
        return (r, g, b)
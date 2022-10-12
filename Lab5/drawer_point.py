import math

class DrawerPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.points = [(x, y)]

    def __add__(self, other):
        return DrawerPoint(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return DrawerPoint(-self.x, -self.y)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, number):
        return DrawerPoint(self.x * number, self.y * number)

    def __imul__(self, number):
        self.x *= number
        self.y *= number
        return self

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalized(self):
        normalized_x = self.x / self.length()
        normalized_y = self.y / self.length()
        return DrawerPoint(normalized_x, normalized_y)

    def from_tuple(p):
        x, y = p
        return DrawerPoint(x, y)
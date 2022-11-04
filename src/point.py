import math

class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        return Point(self.x * other, self.y * other, self.z * other)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

def face_midpoint(points):
    return Point(sum([p.x for p in points]) / len(points), sum([p.y for p in points]) / len(points), sum([p.z for p in points]) / len(points))



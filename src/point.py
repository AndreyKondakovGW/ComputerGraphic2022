import math

class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.faces_normals = []
        self.normal = None

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        return Point(self.x * other, self.y * other, self.z * other)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Point(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
    
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def normalize(self):
        return self * (1 / self.distance(Point(0, 0, 0)))

    def update_normal(self, face_normal):
        face_normal_point = Point(face_normal[0], face_normal[1], face_normal[2]).normalize()
        self.faces_normals.append(face_normal_point)
        normal_x, normal_y, normal_z = 0, 0, 0
        for face_normal_p in self.faces_normals:
            normal_x += face_normal_p.x
            normal_y += face_normal_p.y
            normal_z += face_normal_p.z
        count = len(self.faces_normals)
        self.normal = Point(normal_x / count, normal_y / count, normal_z / count)
        self.normal = self.normal.normalize()

def face_midpoint(points):
    return Point(sum([p.x for p in points]) / len(points), sum([p.y for p in points]) / len(points), sum([p.z for p in points]) / len(points))



class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z


def face_midpoint(points):
    return Point(sum([p.x for p in points]) / len(points), sum([p.y for p in points]) / len(points), sum([p.z for p in points]) / len(points))



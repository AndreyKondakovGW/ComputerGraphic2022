from Lab6.point3D import Point3D
from src.point import Point

class PointLight(Point3D):
    def __init__(self, point: Point):
        color = (255, 255, 255)
        super().__init__(point, color)

# point_ligth.point -> position
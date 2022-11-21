from src.figure import Figure
from src.point import Point
from Lab6.figures.line3D import Line3D
from Lab6.figures.polyhedron import Polyhedron, Face3D

class Cube(Polyhedron):
    def __init__(self, center, size, color=(0, 0, 0)):
        super().__init__(color)
        self.center = center
        self.size = size
        self.create_points()
        self.create_faces()

    def create_faces(self):
        self.faces = []
        #нижняя грань
        self.faces.append(Face3D([self.points[0], self.points[1], self.points[2], self.points[3]], self.brush_color, False))
        #верхняя грань
        self.faces.append(Face3D([self.points[4], self.points[5], self.points[6], self.points[7]], self.brush_color))
        #задняя грань x
        self.faces.append(Face3D([self.points[4], self.points[0], self.points[3], self.points[7]], self.brush_color, False))
        #задняя грань z
        self.faces.append(Face3D([self.points[5], self.points[1], self.points[0], self.points[4]], self.brush_color, False))
        #передняя грань x
        self.faces.append(Face3D([self.points[6], self.points[2], self.points[3], self.points[7]], self.brush_color))
        #передняя грань z
        self.faces.append(Face3D([self.points[5], self.points[1], self.points[2], self.points[6]], self.brush_color))

    def create_points(self):
        #Точки нижней грани
        self.points.append(self.center + Point(self.size / 2, -self.size / 2, self.size / 2))
        self.points.append(self.center + Point(self.size / 2, -self.size / 2, -self.size / 2))
        self.points.append(self.center + Point(-self.size / 2, -self.size / 2, -self.size / 2))
        self.points.append(self.center + Point(-self.size / 2, -self.size / 2, self.size / 2))

        #Точки верхней грани
        self.points.append(self.center + Point(self.size / 2, self.size / 2, self.size / 2))
        self.points.append(self.center + Point(self.size / 2, self.size / 2, -self.size / 2))
        self.points.append(self.center + Point(-self.size / 2, self.size / 2, -self.size / 2))
        self.points.append(self.center + Point(-self.size / 2, self.size / 2, self.size / 2))
        

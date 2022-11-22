from src.point import Point

from Lab6.figures.line3D import Line3D
from Lab6.figures.polyhedron import Polyhedron, Face3D

class Tetrahedron(Polyhedron):
    def __init__(self, center, size, color=(0, 0, 0)):
        super().__init__(color)
        self.center = center
        self.size = size
        self.create_points()
        self.create_faces()
    
    def create_faces(self):
        self.faces = []
        self.faces.append(Face3D([self.points[2], self.points[1], self.points[0]], self.brush_color))

        self.faces.append(Face3D([self.points[3], self.points[1], self.points[0]], self.brush_color, False))
        self.faces.append(Face3D([self.points[1], self.points[3], self.points[2]], self.brush_color, False))
        self.faces.append(Face3D([self.points[2], self.points[3], self.points[0]], self.brush_color, False))
    
    def create_points(self):


        self.points.append(self.center + Point(self.size / 2, -self.size / 2, self.size / 2))
        self.points.append(self.center + Point(-self.size / 2, self.size / 2, self.size / 2))
        self.points.append(self.center + Point(self.size / 2, self.size / 2, -self.size / 2))
        self.points.append(self.center + Point(-self.size / 2, -self.size / 2, -self.size / 2))
        
        
        
from src.point import Point

from Lab6.figures.cube import Cube
from Lab6.figures.line3D import Line3D
from Lab6.figures.polyhedron import Polyhedron, Face3D

class Octahedron(Polyhedron):
    def __init__(self, center, size, color=(255, 0, 255)):
        super().__init__(color)
        self.center = center
        self.size = size
        self.create_points()
        self.create_faces()

    def create_faces(self):
        self.faces = []

        self.faces.append(Face3D([self.points[0], self.points[2], self.points[3]], self.brush_color))
        self.faces.append(Face3D([self.points[0], self.points[3], self.points[5]], self.brush_color))
        self.faces.append(Face3D([self.points[0], self.points[5], self.points[4]], self.brush_color))
        self.faces.append(Face3D([self.points[0], self.points[4], self.points[2]], self.brush_color))

        self.faces.append(Face3D([self.points[1], self.points[3], self.points[2]], self.brush_color))
        self.faces.append(Face3D([self.points[1], self.points[5], self.points[3]], self.brush_color))
        self.faces.append(Face3D([self.points[1], self.points[4], self.points[5]], self.brush_color))
        self.faces.append(Face3D([self.points[1], self.points[2], self.points[4]], self.brush_color))


    def create_points(self):
        cube = Cube(self.center, self.size, self.brush_color)
        for face in cube.faces:
            self.points.append(face.get_center())

            

        

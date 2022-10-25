from src.point import Point

from Lab6.figures.line3D import Line3D
from Lab6.figures.polyhedron import Polyhedron, Face3D

class Tetrahedron(Polyhedron):
    def __init__(self, center, size, color=(0, 0, 0)):
        super().__init__(color)
        self.center = center
        self.size = size
        self.create_points()
        self.create_edges()
        self.create_faces()
    
    def create_faces(self):
        self.faces = []

        self.faces.append(Face3D([self.edges[0], self.edges[1], self.edges[2]], self.brush_color))

        self.faces.append(Face3D([self.edges[0], self.edges[3], self.edges[4]], self.brush_color))
        self.faces.append(Face3D([self.edges[1], self.edges[3], self.edges[5]], self.brush_color))
        self.faces.append(Face3D([self.edges[2], self.edges[4], self.edges[5]], self.brush_color))
    
    def create_edges(self):
        self.edges = []

        self.edges.append(Line3D(self.points[1], self.points[2],self.brush_color))
        self.edges.append(Line3D(self.points[2], self.points[3],self.brush_color))
        self.edges.append(Line3D(self.points[3], self.points[1],self.brush_color))

        self.edges.append(Line3D(self.points[0], self.points[1],self.brush_color))
        self.edges.append(Line3D(self.points[0], self.points[2],self.brush_color))
        self.edges.append(Line3D(self.points[0], self.points[3],self.brush_color))
    
    def create_points(self):
        self.points.append(self.center + Point(-self.size / 2, -self.size / 2, -self.size / 2))
        self.points.append(self.center + Point(self.size / 2, self.size / 2, -self.size / 2))
        self.points.append(self.center + Point(self.size / 2, -self.size / 2, self.size / 2))
        self.points.append(self.center + Point(-self.size / 2, self.size / 2, self.size / 2))
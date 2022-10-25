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
        self.create_edges()
        self.create_faces()

    def create_faces(self):
        self.faces = []
        #bottom face
        self.faces.append(Face3D([self.edges[0], self.edges[3], self.edges[6], self.edges[9]], self.brush_color))
        #top face
        self.faces.append(Face3D([self.edges[1], self.edges[4], self.edges[7], self.edges[10]], self.brush_color))
        #back face
        self.faces.append(Face3D([self.edges[0], self.edges[1], self.edges[2], self.edges[5]], self.brush_color))
        #front face
        self.faces.append(Face3D([self.edges[3], self.edges[4], self.edges[5], self.edges[8]], self.brush_color))
        #right face
        self.faces.append(Face3D([self.edges[6], self.edges[7], self.edges[8], self.edges[11]], self.brush_color))
        #left face
        self.faces.append(Face3D([self.edges[9], self.edges[10], self.edges[11], self.edges[2]], self.brush_color))


    def create_edges(self):
        self.edges = []
        #bottom face
        for i in range(4):
            #bottom face
            self.edges.append(Line3D(self.points[i], self.points[(i + 1) % 4],self.brush_color))
            #top face
            self.edges.append(Line3D(self.points[i + 4], self.points[(i + 1) % 4 + 4],self.brush_color))
            #vertical edges
            self.edges.append(Line3D(self.points[i], self.points[i + 4],self.brush_color))

    def create_points(self):
        self.points.append(self.center + Point(-self.size / 2, -self.size / 2, -self.size / 2))
        self.points.append(self.center + Point(self.size / 2, -self.size / 2, -self.size / 2))
        self.points.append(self.center + Point(self.size / 2, self.size / 2, -self.size / 2))
        self.points.append(self.center + Point(-self.size / 2, self.size / 2, -self.size / 2))
        self.points.append(self.center + Point(-self.size / 2, -self.size / 2, self.size / 2))
        self.points.append(self.center + Point(self.size / 2, -self.size / 2, self.size / 2))
        self.points.append(self.center + Point(self.size / 2, self.size / 2, self.size / 2))
        self.points.append(self.center + Point(-self.size / 2, self.size / 2, self.size / 2))
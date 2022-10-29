from src.point import Point

from Lab6.figures.line3D import Line3D
from Lab6.figures.polyhedron import Polyhedron, Face3D

from math import sin, cos, pi

class Icosahedron(Polyhedron):
    def __init__(self, center, size, color=(0, 0, 0)):
        super().__init__(color)
        self.center = center
        self.size = size
        self.create_points()
        self.create_edges()
        self.create_faces()

    def create_faces(self):
        self.faces = []

        #bottom piramid
        self.faces.append(Face3D([self.edges[0], self.edges[1], self.edges[5]], self.brush_color))#0
        self.faces.append(Face3D([self.edges[1], self.edges[2], self.edges[6]], self.brush_color))
        self.faces.append(Face3D([self.edges[2], self.edges[3], self.edges[7]], self.brush_color))
        self.faces.append(Face3D([self.edges[3], self.edges[4], self.edges[8]], self.brush_color))
        self.faces.append(Face3D([self.edges[4], self.edges[0], self.edges[9]], self.brush_color))

        #top piramid
        self.faces.append(Face3D([self.edges[10], self.edges[11], self.edges[15]], self.brush_color))#5
        self.faces.append(Face3D([self.edges[11], self.edges[12], self.edges[16]], self.brush_color))
        self.faces.append(Face3D([self.edges[12], self.edges[13], self.edges[17]], self.brush_color))
        self.faces.append(Face3D([self.edges[13], self.edges[14], self.edges[18]], self.brush_color))
        self.faces.append(Face3D([self.edges[14], self.edges[10], self.edges[19]], self.brush_color))        

        #belt
        self.faces.append(Face3D([self.edges[20], self.edges[21], self.edges[17]], self.brush_color))#10
        self.faces.append(Face3D([self.edges[21], self.edges[22], self.edges[5]], self.brush_color))
        self.faces.append(Face3D([self.edges[22], self.edges[23], self.edges[16]], self.brush_color))
        self.faces.append(Face3D([self.edges[23], self.edges[24], self.edges[6]], self.brush_color))
        self.faces.append(Face3D([self.edges[24], self.edges[25], self.edges[15]], self.brush_color))

        self.faces.append(Face3D([self.edges[25], self.edges[26], self.edges[7]], self.brush_color))
        self.faces.append(Face3D([self.edges[26], self.edges[27], self.edges[19]], self.brush_color))
        self.faces.append(Face3D([self.edges[27], self.edges[28], self.edges[8]], self.brush_color))
        self.faces.append(Face3D([self.edges[28], self.edges[29], self.edges[18]], self.brush_color))
        self.faces.append(Face3D([self.edges[29], self.edges[20], self.edges[9]], self.brush_color))


    
    def create_edges(self):
        self.edges = []
        for i in range(5):
            self.edges.append(Line3D(self.points[10], self.points[i], self.brush_color))

        #bottom round
        for i in range(5):
            self.edges.append(Line3D(self.points[i], self.points[(i + 1) % 5], self.brush_color))

        for i in range(5):
            self.edges.append(Line3D(self.points[11], self.points[i + 5], self.brush_color))

        #top round
        for i in range(5):
            self.edges.append(Line3D(self.points[i + 5], self.points[(i + 1) % 5 + 5], self.brush_color))

        self.edges.append(Line3D(self.points[0], self.points[8], self.brush_color)) #20
        self.edges.append(Line3D(self.points[0], self.points[7], self.brush_color))
        self.edges.append(Line3D(self.points[1], self.points[7], self.brush_color))
        self.edges.append(Line3D(self.points[1], self.points[6], self.brush_color))
        self.edges.append(Line3D(self.points[2], self.points[6], self.brush_color))
        self.edges.append(Line3D(self.points[2], self.points[5], self.brush_color))#25
        self.edges.append(Line3D(self.points[3], self.points[5], self.brush_color))
        self.edges.append(Line3D(self.points[3], self.points[9], self.brush_color))
        self.edges.append(Line3D(self.points[4], self.points[9], self.brush_color))
        self.edges.append(Line3D(self.points[4], self.points[8], self.brush_color))

    def create_points(self):
        #add bottom round point
        for i in range(5):
            x = self.size  * cos(2 * pi * i / 5)
            y = self.size  * sin(2 * pi * i / 5)
            self.points.append(self.center + Point(x, -self.size / 2, y))

        #add top round point
        for i in range(5):
            x = self.size  * cos(2 * pi * i / 5)
            y = self.size  * sin(2 * pi * i / 5)
            self.points.append(self.center + Point(-x, self.size / 2, y))

        self.points.append(self.center + Point(0, -5 * self.size / 4, 0))
        self.points.append(self.center + Point(0, 5 * self.size / 4, 0))
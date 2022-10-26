from src.point import Point

from Lab6.figures.line3D import Line3D
from Lab6.figures.polyhedron import Polyhedron, Face3D
from Lab6.figures.icosahedron import Icosahedron

class Dodecahedron(Polyhedron):
    def __init__(self, center, size, color=(0, 0, 0)):
        super().__init__(color)
        self.center = center
        self.size = size
        self.create_points()
        self.create_edges()
        self.create_faces()

    def create_faces(self):
        self.faces = []

        self.faces.append(Face3D([self.edges[0], self.edges[1], self.edges[2], self.edges[3], self.edges[4]], self.brush_color))
        self.faces.append(Face3D([self.edges[5], self.edges[6], self.edges[7], self.edges[8], self.edges[9]], self.brush_color))
        
        self.faces.append(Face3D([self.edges[4], self.edges[19], self.edges[29], self.edges[20], self.edges[11]], self.brush_color))
        self.faces.append(Face3D([self.edges[0], self.edges[11], self.edges[21], self.edges[22], self.edges[13]], self.brush_color))
        self.faces.append(Face3D([self.edges[1], self.edges[13], self.edges[23], self.edges[24], self.edges[15]], self.brush_color))
        self.faces.append(Face3D([self.edges[2], self.edges[15], self.edges[25], self.edges[26], self.edges[17]], self.brush_color))
        self.faces.append(Face3D([self.edges[3], self.edges[17], self.edges[27], self.edges[28], self.edges[18]], self.brush_color))

        self.faces.append(Face3D([self.edges[5], self.edges[12], self.edges[22], self.edges[23], self.edges[14]], self.brush_color))
        self.faces.append(Face3D([self.edges[6], self.edges[14], self.edges[20], self.edges[21], self.edges[10]], self.brush_color))
        self.faces.append(Face3D([self.edges[7], self.edges[10], self.edges[19], self.edges[28], self.edges[18]], self.brush_color))
        self.faces.append(Face3D([self.edges[8], self.edges[18], self.edges[26], self.edges[27], self.edges[16]], self.brush_color))
        self.faces.append(Face3D([self.edges[9], self.edges[16], self.edges[25], self.edges[24], self.edges[12]], self.brush_color))

    def create_edges(self):
        self.edges = []

        #bottom
        self.edges.append(Line3D(self.points[0], self.points[1], self.brush_color)) #0
        self.edges.append(Line3D(self.points[1], self.points[2], self.brush_color))
        self.edges.append(Line3D(self.points[2], self.points[3], self.brush_color))
        self.edges.append(Line3D(self.points[3], self.points[4], self.brush_color))
        self.edges.append(Line3D(self.points[4], self.points[0], self.brush_color))

        #top
        self.edges.append(Line3D(self.points[5], self.points[6], self.brush_color)) #5
        self.edges.append(Line3D(self.points[6], self.points[7], self.brush_color))
        self.edges.append(Line3D(self.points[7], self.points[8], self.brush_color))
        self.edges.append(Line3D(self.points[8], self.points[9], self.brush_color))
        self.edges.append(Line3D(self.points[9], self.points[5], self.brush_color))

        self.edges.append(Line3D(self.points[7], self.points[10], self.brush_color)) #10
        self.edges.append(Line3D(self.points[0], self.points[11], self.brush_color))
        self.edges.append(Line3D(self.points[6], self.points[12], self.brush_color))
        self.edges.append(Line3D(self.points[1], self.points[13], self.brush_color))
        self.edges.append(Line3D(self.points[5], self.points[14], self.brush_color))

        self.edges.append(Line3D(self.points[2], self.points[15], self.brush_color))#15
        self.edges.append(Line3D(self.points[9], self.points[16], self.brush_color))
        self.edges.append(Line3D(self.points[3], self.points[17], self.brush_color))
        self.edges.append(Line3D(self.points[8], self.points[18], self.brush_color))
        self.edges.append(Line3D(self.points[4], self.points[19], self.brush_color))

        #belt
        self.edges.append(Line3D(self.points[10], self.points[11], self.brush_color)) #20
        self.edges.append(Line3D(self.points[11], self.points[12], self.brush_color))
        self.edges.append(Line3D(self.points[12], self.points[13], self.brush_color))
        self.edges.append(Line3D(self.points[13], self.points[14], self.brush_color))
        self.edges.append(Line3D(self.points[14], self.points[15], self.brush_color))

        self.edges.append(Line3D(self.points[15], self.points[16], self.brush_color))
        self.edges.append(Line3D(self.points[16], self.points[17], self.brush_color))
        self.edges.append(Line3D(self.points[17], self.points[18], self.brush_color))
        self.edges.append(Line3D(self.points[18], self.points[19], self.brush_color))
        self.edges.append(Line3D(self.points[19], self.points[10], self.brush_color))


    def create_points(self):
        ico = Icosahedron(self.center, self.size, self.brush_color)

        for face in ico.faces:
            self.points.append(face.get_center())
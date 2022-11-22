from Lab6.figures.tetrahedron import Tetrahedron
from Lab6.figures.polyhedron import Face3D

class ColoredTetrahedron(Tetrahedron):
    def __init__(self, center, size, color1=(255,0,0), color2=(0,255,0), color3=(0,0,255), color4=(255,0,255)):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.color4 = color4
        super().__init__(center, size)

    def create_faces(self):
        self.faces = []
        self.faces.append(Face3D([self.points[2], self.points[1], self.points[0]], self.color1))

        self.faces.append(Face3D([self.points[3], self.points[1], self.points[0]], self.color2, False))
        self.faces.append(Face3D([self.points[1], self.points[3], self.points[2]], self.color3, False))
        self.faces.append(Face3D([self.points[2], self.points[3], self.points[0]], self.color4, False))
    
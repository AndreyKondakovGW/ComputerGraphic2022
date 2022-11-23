from Lab6.figures.cube import Cube
from Lab6.figures.polyhedron import Face3D

class ColoredCube(Cube):
    def __init__(self, center, size, colors=[]):
        self.colors = [colors[i % len(colors)] for i in range(6)]
        super().__init__(center, size)
    
    def create_faces(self):
        self.faces = []
        #нижняя грань
        self.faces.append(Face3D([self.points[0], self.points[1], self.points[2], self.points[3]], self.colors[0], False))
        #верхняя грань
        self.faces.append(Face3D([self.points[4], self.points[5], self.points[6], self.points[7]], self.colors[1]))
        #задняя грань x
        self.faces.append(Face3D([self.points[4], self.points[0], self.points[3], self.points[7]], self.colors[2], False))
        #задняя грань z
        self.faces.append(Face3D([self.points[5], self.points[1], self.points[0], self.points[4]], self.colors[3], False))
        #передняя грань x
        self.faces.append(Face3D([self.points[6], self.points[2], self.points[3], self.points[7]], self.colors[4]))
        #передняя грань z
        self.faces.append(Face3D([self.points[5], self.points[1], self.points[2], self.points[6]], self.colors[5]))
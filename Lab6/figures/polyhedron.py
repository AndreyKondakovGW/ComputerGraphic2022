from turtle import color
from src.figure import Figure
from src.point import face_midpoint

class Polyhedron(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.faces = []

    def draw(self, renderer):
        super().draw(renderer)
        for point in self.points:
            renderer.draw_point(point, color = (255, 0, 0))
        for face in self.faces:
            face.draw(renderer)

    def select(self):
        super().select()
        for face in self.faces:
            face.select()

    def deselect(self):
        super().deselect()
        for face in self.faces:
            face.deselect()

class Face3D(Figure):
    def __init__(self, edges, color):
        super().__init__(color)
        self.edges = edges
        for edge in edges:
            self.points.append(edge.points[0])
            self.points.append(edge.points[1])
        self.points = list(dict.fromkeys(self.points))

    def draw(self, renderer):
        super().draw(renderer)
        for edge in self.edges:
            edge.brush_color = self.brush_color
            edge.draw(renderer)

    def select(self):
        super().select()
        for edge in self.edges:
            edge.select()

    def deselect(self):
        super().deselect()
        for edge in self.edges:
            edge.deselect()

    def get_center(self):
        return face_midpoint(self.points)
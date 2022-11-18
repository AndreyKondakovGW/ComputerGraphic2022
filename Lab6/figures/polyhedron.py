from turtle import color

import numpy as np

from src.figure import Figure
from src.point import face_midpoint, Point
from Lab6.transformation_3d import centroid, cos_between_vectors

class Polyhedron(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.faces = []

    def draw(self, renderer):
        super().draw(renderer)
        #faces = self.visual_faces(renderer.camera)
        faces = self.faces
        for face in faces:
            face.draw(renderer)

    def mark_undrawed(self):
        for face in self.faces:
            face.mark_undrawed()

    def select(self):
        super().select()
        for face in self.faces:
            face.select()

    def deselect(self):
        super().deselect()
        for face in self.faces:
            face.deselect()

    def visual_faces(self, camera):
        visual_faces = []
        c = centroid(self.points)
        # proection = Point(c[0], c[1], c[2]) - camera_point
        camera_dir = (camera.direction.x, camera.direction.y, camera.direction.z)
        for f in self.faces:
            f.update_normal_vector()
            cos = cos_between_vectors(f.normal_vector, camera_dir)
            if 1 >= cos >= 0:
                visual_faces.append(f)
        return visual_faces


class Face3D(Figure):
    def __init__(self, edges, color):
        super().__init__(color)
        self.edges = edges
        num_point = len(edges)
        p0 = edges[0].points[0]
        p1 = edges[0].points[1]
        for i in range(num_point):
            self.points.append(p0)
            for edge in edges:
                if edge.points[0] == p1:
                    p0 = p1
                    p1 = edge.points[1]
                    break
                if (edge.points[1] == p1 and edge.points[0] != p0):
                    p0 = p1
                    p1 = edge.points[0]
                    break
            
        self.points = list(dict.fromkeys(self.points))

    def draw(self, renderer):
        super().draw(renderer)
        for edge in self.edges:
            edge.brush_color = self.brush_color
            edge.draw(renderer)
        renderer.draw_face(self)

    def mark_undrawed(self):
        for edge in self.edges:
            edge.drawed = False

    def select(self):
        #super().select()
        for edge in self.edges:
            edge.select()

    def deselect(self):
        super().deselect()
        for edge in self.edges:
            edge.deselect()

    def get_center(self):
        return face_midpoint(self.points)

    def update_normal_vector(self):
        v1 = self.points[1] - self.points[-1]
        v2 = self.points[0] - self.points[2]
        self.normal_vector = np.cross((v1.x,v1.y,v1.z),(v2.x,v2.y,v2.z))

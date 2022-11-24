from turtle import color

import numpy as np
from Lab6.figures.line3D import Line3D
from src.figure import Figure
from src.point import face_midpoint, Point
from Lab6.transformation_3d import centroid, cos_between_vectors, angle_between_vectors

class Polyhedron(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.faces = []

    def draw(self, renderer):
        super().draw(renderer)
        # for p in self.points:
        #     p.face_normals = []
        if renderer.camera:
            faces = self.visual_faces(renderer.camera)
        else:
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
        for f in self.faces:
            f.update_normal_vector()
            f_point = Point(f.normal_vector[0], f.normal_vector[1], f.normal_vector[2]).normalize()
            v_point = (camera.position - f.points[1]).normalize()
            if f_point.dot(v_point) >= 0:
                visual_faces.append(f)
            # if 90 > angle > 0 or 270 < angle < 360:
            #     visual_faces.append(f)
        return visual_faces

    def set_texture(self, texture):
        self.texture = texture
        for face in self.faces:
            face.texture = texture


class Face3D(Figure):
    def __init__(self, points, color, front = True):
        # front - является ли грань лицевой
        # поумолчанию точки даются по часовой стрелке
        super().__init__(color)
        if front:
            self.points = points
        else:
            self.points = points[::-1]
        self.edges = []
        p0 = points[0]
        for p in points[1:]:
            self.edges.append(Line3D(p0, p, color))
            p0 = p
        self.edges.append(Line3D(points[-1], points[0], color))

    def draw(self, renderer):
        super().draw(renderer)
        for edge in self.edges:
            edge.brush_color = self.brush_color
            edge.draw(renderer)
        # self.update_normals()
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
        v1 = self.points[0] - self.points[1]
        v2 = self.points[2] - self.points[1]
        self.normal_vector = np.cross((v1.x,v1.y,v1.z),(v2.x,v2.y,v2.z))

    def update_normals(self):
        self.update_normal_vector()
        for p in self.points:
            p.update_normal(self.normal_vector)

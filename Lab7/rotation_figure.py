from Lab6.figures.line3D import Line3D
from Lab6.figures.polyhedron import Polyhedron, Face3D
from Lab6.point3D import Point3D
from Lab6.rotator3D import rotate_figure
from Lab6.transformation_3d import rotate, centroid, angle_between_vectors
from src.point import Point


class RotationFigure(Polyhedron):
    def __init__(self, center, axis, partition, color=(255, 255, 0)):
        super().__init__(color)
        self.center = center
        self.str_axis = None
        self.axis = None
        self.dir = None
        self.update_axis(axis)
        self.partition = partition
        self.angle = 360 / self.partition
        self.forming_points = []
        self.camera = Point(0,0,200)
        self.all_faces = self.faces

    def update_rotation_figure(self, new_point, partition, axis, delete_faces_flag, camera_point):
        self.camera = camera_point
        if new_point not in self.forming_points:
            self.forming_points.append(new_point)
        if partition != self.partition or axis != self.str_axis:  # если меняется разбиение или ось - полностью перестраиваем фигуру
            self.points = []
            self.faces = []
            self.update_axis(axis)
            self.partition = partition
            self.angle = 360 / self.partition
            for p in self.forming_points:
                self.add_point(p)
        else:
            if len(self.forming_points)==2:
                self.faces = []
            self.add_point(new_point)
        if delete_faces_flag:
            self.delete_non_face()

    def add_point(self, point):
        self.points.append(point)
        bubble = Point3D(Point(point.x, point.y, point.z),
                         self.brush_color)  # объект 3D точки,чтобы применять к ней поворот
        for i in range(self.partition - 1):
            # поворачиваем точку относительно оси на заданный угол, чтобы получить следующую
            rotate_figure(bubble, self.dir, self.angle, self.axis)
            self.points.append(Point(bubble.point.x, bubble.point.y, bubble.point.z))
            l = len(self.points)
            edges = []
            if l < self.partition:
                edges.append(Line3D(self.points[l - 2], self.points[l - 1], self.brush_color))
            else:
                edges.append(
                    Line3D(self.points[l - 2 - self.partition], self.points[l - 1 - self.partition], self.brush_color))
                edges.append(Line3D(self.points[l - 2 - self.partition], self.points[l - 2], self.brush_color))
                edges.append(Line3D(self.points[l - 1 - self.partition], self.points[l - 1], self.brush_color))
                edges.append(Line3D(self.points[l - 2], self.points[l - 1], self.brush_color))
            self.faces.append(Face3D(edges, self.brush_color))
        #edges = []
        # обработка последней точки
        l = len(self.points)
        if len(self.forming_points) == 1:
            edges.append(Line3D(self.points[l - 1], self.points[l - self.partition], self.brush_color))
        else:
            edges.append(
                Line3D(self.points[l - 2 * self.partition], self.points[l - 1 - self.partition], self.brush_color))
            edges.append(Line3D(self.points[l - self.partition], self.points[l - 2 * self.partition], self.brush_color))
            edges.append(Line3D(self.points[l - 1 - self.partition], self.points[l - 1], self.brush_color))
            edges.append(Line3D(self.points[l - 1], self.points[l - self.partition], self.brush_color))

    def update_axis(self, axis):
        self.str_axis = axis
        if axis == 'OX':
            self.axis = Line3D(Point(-300, 0, 0), Point(300, 0, 0), self.brush_color)
            self.dir = (1, 0, 0)
        elif axis == 'OY':
            self.axis = Line3D(Point(0, -300, 0), Point(0, 300, 0), self.brush_color)
            self.dir = (0, 1, 0)
        elif axis == 'OZ':
            self.axis = Line3D(Point(0, 0, -300), Point(0, 0, 300), self.brush_color)
            self.dir = (0, 1, 0)

    def delete_non_face(self):
        self.all_faces = self.faces
        self.faces = []
        c = centroid(self.points)
        proection = Point(c[0], c[1], c[2]) - self.camera
        for f in self.all_faces:
            f.update_normal_vector()
            cos = angle_between_vectors(f.normal_vector, (proection.x,proection.y,proection.z))
            if 90 > cos > 0:
                self.faces.append(f)



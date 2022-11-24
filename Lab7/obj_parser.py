import os

from Lab6.figures.polyhedron import Polyhedron, Face3D
from src.point import Point
from Lab6.figures.line3D import Line3D

from tkinter import filedialog

class ObjParser:
    def __init__(self):
        current_dir = os.getcwd()
        self.scale = 50
        self.models_dir = os.path.join(current_dir, 'Lab7', 'models')

    def open_file(self):
        filename = filedialog.askopenfilename(initialdir=self.models_dir, filetypes=[("3D Object", ".obj")])
        if filename is None:
            return
        return self.load_figure(filename)

    def load_figure(self, file_name):
        with open(file_name, 'r') as file:
            self.polyhedron = Polyhedron((0, 0, 0))
            faces = []
            for line in file:
                if line.startswith('v '):
                    self.polyhedron.points.append(self.parse_point(line))
                elif line.startswith('f '):
                    faces.append(self.parse_face(line))
            self.polyhedron.faces = faces
            return self.polyhedron

    def save_figure(self, file_name, figures):
        with open(file_name, 'w') as file:
            for figure in figures:
                for point in figure.points:
                    file.write(f'v {point.x / self.scale} {point.y / self.scale} {point.z / self.scale} \n')
                for face in figure.faces:
                    file.write('f ')
                    """ for face_edge in face.edges:
                        file.write(f'{figure.points.index(face_edge.points[0]) + 1} ')
                        file.write(f'{figure.points.index(face_edge.points[1]) + 1} ') """
                    for face_point in face.points:
                        file.write(f'{figure.points.index(face_point) + 1} ')
                    file.write('\n')

    def parse_point(self, line):
        line = line.replace('v ', '')
        line = line.replace('\n', '')
        line = line.strip()
        line = line.split(' ')
        x = float(line[0]) * self.scale
        y = float(line[1]) * self.scale
        z = float(line[2]) * self.scale
        return Point(x, y, z)

    def parse_face(self, line):
        line = line.replace('f ', '')
        line = line.replace('\n', '')
        line = line.strip()
        line = line.split(' ')
        face_points = [p.split('/')[0] for p in line]
        points = []
        for i in range(len(face_points)):
            points.append(self.polyhedron.points[int(face_points[i]) - 1])
        return Face3D(points, (0, 0, 0))
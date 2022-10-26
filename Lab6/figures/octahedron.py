from src.point import Point

from Lab6.figures.cube import Cube
from Lab6.figures.line3D import Line3D
from Lab6.figures.polyhedron import Polyhedron, Face3D

class Octahedron(Polyhedron):
    def __init__(self, center, size, color=(0, 0, 0)):
        super().__init__(color)
        self.center = center
        self.size = size
        self.create_points()
        self.create_edges()
        self.create_faces()

    def create_faces(self):
        self.faces = []

        self.faces.append(Face3D([self.edges[0], self.edges[2], self.edges[8]], self.brush_color))
        self.faces.append(Face3D([self.edges[2], self.edges[4], self.edges[9]], self.brush_color))
        self.faces.append(Face3D([self.edges[4], self.edges[6], self.edges[10]], self.brush_color))
        self.faces.append(Face3D([self.edges[6], self.edges[0], self.edges[11]], self.brush_color))

        self.faces.append(Face3D([self.edges[1], self.edges[3], self.edges[8]], self.brush_color))
        self.faces.append(Face3D([self.edges[3], self.edges[5], self.edges[9]], self.brush_color))
        self.faces.append(Face3D([self.edges[5], self.edges[7], self.edges[10]], self.brush_color))
        self.faces.append(Face3D([self.edges[7], self.edges[1], self.edges[11]], self.brush_color))

        

    def create_edges(self):
        self.edges = []

        
        self.edges.append(Line3D(self.points[0], self.points[2], self.brush_color))
        self.edges.append(Line3D(self.points[1], self.points[2], self.brush_color))
        self.edges.append(Line3D(self.points[0], self.points[3], self.brush_color))
        self.edges.append(Line3D(self.points[1], self.points[3], self.brush_color))
        self.edges.append(Line3D(self.points[0], self.points[4], self.brush_color))
        self.edges.append(Line3D(self.points[1], self.points[4], self.brush_color))
        self.edges.append(Line3D(self.points[0], self.points[5], self.brush_color))
        self.edges.append(Line3D(self.points[1], self.points[5], self.brush_color))

        self.edges.append(Line3D(self.points[2], self.points[3], self.brush_color))
        self.edges.append(Line3D(self.points[3], self.points[4], self.brush_color))
        self.edges.append(Line3D(self.points[4], self.points[5], self.brush_color))
        self.edges.append(Line3D(self.points[5], self.points[2], self.brush_color))


    def create_points(self):
        cube = Cube(self.center, self.size, self.brush_color)
        for face in cube.faces:
            self.points.append(face.get_center())


# class Octahedron(Figure):
#     def __init__(self,center, a, color=(0, 0, 0)):
#         super().__init__(color)
#         cube_points = [0]
#         self.points = []
#         a = a/2
#         cube_points.append(Point(center.x - a, center.y - a, center.z - a))
#         cube_points.append(Point(center.x - a, center.y + a, center.z - a))
#         cube_points.append(Point(center.x + a, center.y + a, center.z - a))
#         cube_points.append(Point(center.x + a, center.y - a, center.z - a))

#         cube_points.append(Point(center.x - a, center.y - a, center.z + a))
#         cube_points.append(Point(center.x - a, center.y + a, center.z + a))
#         cube_points.append(Point(center.x + a, center.y + a, center.z + a))
#         cube_points.append(Point(center.x + a, center.y - a, center.z + a))

#          #1234 /1256 / 5678  / 2367 3478 / 1458
#         face_point_ind = [[1,2,3,4], [1,2,5,6],[2,3,6,7],[3,4,7,8],[1,4,5,8],[5,6,7,8]]
#         for face in face_point_ind:
#             self.points.append(face_midpoint([cube_points[face[0]],cube_points[face[1]],cube_points[face[2]],cube_points[face[3]]]))

#     def draw(self, drawer):
#         self.canvas_points = self.points.copy()
#         for i in range(1,5):
#             p = drawer.draw_line([self.points[0], self.points[i]], self.brush_color)
#             self.canvas_points[0] = p[0]
#             self.canvas_points[i] = p[1]
#             p = drawer.draw_line([self.points[5], self.points[i]], self.brush_color)
#             self.canvas_points[5] = p[0]
#             self.canvas_points[i] = p[1]

#         p = drawer.draw_line([self.points[1], self.points[2]], self.brush_color)
#         p = drawer.draw_line([self.points[2], self.points[3]], self.brush_color)
#         self.canvas_points[2] = p[0]
#         p = drawer.draw_line([self.points[3], self.points[4]], self.brush_color)
#         self.canvas_points[3] = p[0]
#         p = drawer.draw_line([self.points[4], self.points[1]], self.brush_color)
#         self.canvas_points[4] = p[0]
#         self.canvas_points[1] = p[1]

            

        

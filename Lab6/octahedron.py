from src.figure import Figure
from src.point import Point, face_midpoint

class Octahedron(Figure):
    def __init__(self,center, a, color=(0, 0, 0)):
        super().__init__(color)
        cube_points = [0]
        self.points = []
        a = a/2
        cube_points.append(Point(center.x - a, center.y - a, center.z - a))
        cube_points.append(Point(center.x - a, center.y + a, center.z - a))
        cube_points.append(Point(center.x + a, center.y + a, center.z - a))
        cube_points.append(Point(center.x + a, center.y - a, center.z - a))

        cube_points.append(Point(center.x - a, center.y - a, center.z + a))
        cube_points.append(Point(center.x - a, center.y + a, center.z + a))
        cube_points.append(Point(center.x + a, center.y + a, center.z + a))
        cube_points.append(Point(center.x + a, center.y - a, center.z + a))

         #1234 /1256 / 5678  / 2367 3478 / 1458
        face_point_ind = [[1,2,3,4], [1,2,5,6],[2,3,6,7],[3,4,7,8],[1,4,5,8],[5,6,7,8]]
        for face in face_point_ind:
            self.points.append(face_midpoint([cube_points[face[0]],cube_points[face[1]],cube_points[face[2]],cube_points[face[3]]]))

    def draw(self, drawer):
        self.canvas_points = self.points.copy()
        for i in range(1,5):
            p = drawer.draw_line([self.points[0], self.points[i]], self.brush_color)
            self.canvas_points[0] = p[0]
            self.canvas_points[i] = p[1]
            p = drawer.draw_line([self.points[5], self.points[i]], self.brush_color)
            self.canvas_points[5] = p[0]
            self.canvas_points[i] = p[1]

        p = drawer.draw_line([self.points[1], self.points[2]], self.brush_color)
        p = drawer.draw_line([self.points[2], self.points[3]], self.brush_color)
        self.canvas_points[2] = p[0]
        p = drawer.draw_line([self.points[3], self.points[4]], self.brush_color)
        self.canvas_points[3] = p[0]
        p = drawer.draw_line([self.points[4], self.points[1]], self.brush_color)
        self.canvas_points[4] = p[0]
        self.canvas_points[1] = p[1]

            

        

from src.figure import Figure
from src.point import Point

class Cube(Figure):
    def __init__(self,center, a, color=(0, 0, 0)):
        super().__init__(color)
        self.points = []
        a = a/2
        self.points.append(Point(center.x - a, center.y - a, center.z - a))
        self.points.append(Point(center.x - a, center.y + a, center.z - a))
        self.points.append(Point(center.x + a, center.y + a, center.z - a))
        self.points.append(Point(center.x + a, center.y - a, center.z - a))

        self.points.append(Point(center.x - a, center.y - a, center.z + a))
        self.points.append(Point(center.x - a, center.y + a, center.z + a))
        self.points.append(Point(center.x + a, center.y + a, center.z + a))
        self.points.append(Point(center.x + a, center.y - a, center.z + a))

    def draw(self, drawer):
        self.canvas_points = self.points.copy()
        for i in range(4):
            p = drawer.draw_line([self.points[i], self.points[(i + 1) % 4]], self.brush_color)
            self.canvas_points[i] = p[0]
            self.canvas_points[(i + 1) % 4] = p[1]
            p = drawer.draw_line([self.points[i + 4], self.points[(i + 1) % 4 + 4]], self.brush_color)
            self.canvas_points[i + 4] = p[0]
            self.canvas_points[(i + 1) % 4 + 4] = p[1]
            p = drawer.draw_line([self.points[i], self.points[i + 4]], self.brush_color)
            self.canvas_points[i] = p[0]
            self.canvas_points[i + 4] = p[1]
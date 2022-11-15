from src.renderer import Renderer
from src.point import Point
import math
from Lab8.raster_triangle import raster_triangle
from point_with_color import PointWithColor

class PolyRenderer(Renderer):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.camera_width = canvas.winfo_width()
        self.camera_height = canvas.winfo_height()
        self.screen_points = [[None] * self.camera_height] * self.camera_width
        self.z_buffer = [[math.inf] * self.camera_height] * self.camera_width

    def draw_line(self, points, color=(0,0,0), thickness=2):
        #pass
        super().draw_line(points, color, thickness)

    def draw_face(self, face):
        if len(face.points) == 3:
            color = face.brush_color
            points = [self.colored_screen_point(p, color) for p in face.points]
            p1, p2, p3 = points[0], points[1], points[2]
            face_rasterized = raster_triangle(p1, p2, p3)
            for point in face_rasterized:
                #self.screen_points[point.x][point.y] = point.color
                self.canvas.put_pixel(point.x, point.y, point.color)

    def colored_screen_point(self, point: Point, color = (0,0,0)):
        translated = self.translate3D_point(point)
        rounded_x = int(translated.x)
        rounded_y = int(translated.y)
        rounded_z = int(translated.z)
        return PointWithColor(rounded_x, rounded_y, rounded_z, color)
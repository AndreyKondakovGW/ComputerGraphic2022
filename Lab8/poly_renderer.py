from src.renderer import Renderer
from src.point import Point
import math
from Lab8.raster_triangle import raster_triangle
from Lab8.point_with_color import PointWithColor

class PolyRenderer(Renderer):
    def __init__(self, canvas, use_z_buffer=True):
        super().__init__(canvas)
        canvas.update()
        self.camera_width = canvas.winfo_width()
        self.camera_height = canvas.winfo_height()
        self.colors_buffer = [[None for _ in range(self.camera_height)] for _ in range(self.camera_width)]
        self.z_buffer = [[math.inf for _ in range(self.camera_height)] for _ in range(self.camera_width)]
        self.should_draw_lines = False
        self.show_axis = True
        self.use_z_buffer = use_z_buffer
        
    def clear_buffers(self):
        self.colors_buffer = [[None for _ in range(self.camera_height)] for _ in range(self.camera_width)]
        self.z_buffer = [[math.inf for _ in range(self.camera_height)] for _ in range(self.camera_width)]

    def render_scene(self, scene):
        if not self.use_z_buffer:
            super().render_scene(scene)
        else:
            self.clear_buffers()
            super().render_scene(scene)
            for x in range(0, len(self.colors_buffer)):
                for y in range(0, len(self.colors_buffer[0])):
                    color = self.colors_buffer[x][y]
                    if color is not None:
                        self.canvas.put_pixel(x, y, color)
        if self.show_axis:
            self.draw_axes()
            self.show_grid()

    def show_grid(self):
        self.should_draw_lines = self.show_axis
        super().show_grid()
        self.should_draw_lines = False

    def draw_axes(self):
        self.should_draw_lines = self.show_axis
        super().draw_axes()
        self.should_draw_lines = False

    def draw_line(self, points, color=(0,0,0), thickness=2):
        if self.should_draw_lines or not self.use_z_buffer:
            super().draw_line(points, color, thickness)

    def draw_face(self, face):
        if not self.use_z_buffer:
            super().draw_face(face)
            return

        color = face.brush_color
        # points = [self.colored_screen_point(p, color) for p in face.points]
        points = self.get_shaded_points(face.points)
        if len(face.points) == 3:
            p1, p2, p3 = points[0], points[1], points[2]
            self.draw_triangle(p1, p2, p3)
        # else:
        #     for i in range(2, len(points)):
        #         p1 = points[0]
        #         p2 = points[i-1]
        #         p3 = points[i]
        #         self.draw_triangle(p1, p2, p3)

    def get_shaded_points(self, points):
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
        res = []
        ind = 0
        for point in points:
            if isinstance(point, PointWithColor):
                res.append(self.colored_screen_point(point, point.color))
            else:
                res.append(self.colored_screen_point(point, colors[ind]))
            ind = ind + 1 % 4
        return res

    def draw_triangle(self, p1, p2, p3):
        face_rasterized = raster_triangle(p1, p2, p3)
        for point in face_rasterized:
            z_from_buffer = self.z_buffer[point.x][point.y]
            if point.z < z_from_buffer:
                x, y = point.x, point.y
                self.colors_buffer[x][y] = point.color
                self.z_buffer[x][y] = point.z

    def colored_screen_point(self, point: Point, color = (0,0,0)):
        translated = self.translate3D_point(point)
        rounded_x = int(translated.x)
        rounded_y = int(translated.y)
        rounded_z = int(translated.z)
        return PointWithColor(rounded_x, rounded_y, rounded_z, color)

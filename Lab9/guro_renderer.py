from Lab8.poly_renderer import PolyRenderer
from Lab9.light_source import PointLight
from Lab9.guro_lightning import guro_lightning
from src.point import Point
from Lab6.transformation_3d import centroid

class GuroRenderer(PolyRenderer):
    def __init__(self, canvas):
        super().__init__(canvas)
        light_position = Point(50, 300, 350)
        self.light_source = PointLight(light_position)

    def render_scene(self, scene):
        super().render_scene(scene)
        self.draw_point(self.light_source.point, color=(255, 255, 0))

    def draw_face(self, face):
        normal_vector = Point(face.normal_vector[0], face.normal_vector[1], face.normal_vector[2]).normalize()
        self.debug_face_normals(face, normal_vector)
        for point in face.points:
            point.normal = normal_vector
        super().draw_face(face)

    def debug_face_normals(self, face, face_normal):
        center = centroid(face.points)
        center_point = Point(center[0], center[1], center[2])
        normal_line = [center_point, center_point + face_normal * 50]
        self.should_draw_lines = True
        self.draw_line(normal_line, color=(0, 0, 0))
        self.should_draw_lines = False

    def calculate_point_color(self, point, color):
        # self.debug_point_normals(point)
        return guro_lightning(point, color, self.light_source)

    def debug_point_normals(self, point):
        normal_line = [point, point + point.normal * 50]
        self.should_draw_lines = True
        self.draw_line(normal_line, color=(0, 0, 0))
        self.should_draw_lines = False
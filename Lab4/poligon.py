from .mouseLine import MouseLine
from .functions import *
from src.figure import Figure
from src.point import Point
from src.controller_mode import ControllerMode

from .line_intersector import draw_intersections_with_line

class PoligonMode(ControllerMode):
    def __init__(self, canvas, color = (0,0,0)):
        self.canvas = canvas
        self.brush_color = color
        self.last_poli_point = None
        self.points = []
    
    def hanble_moution(self, event):
        if self.last_poli_point is not None:
            self.canvas.redraw()
            self.canvas.draw_line(self.last_poli_point, (event.x, event.y), self.brush_color)
            draw_intersections_with_line(self.canvas, self.last_poli_point, (event.x, event.y))

    def hanble_press(self, event):
        if self.last_poli_point is None:
            self.last_poli_point = Point(event.x, event.y)
            self.points.append(self.last_poli_point)
            self.canvas.storage.add_figure(MouseLine(self.points, self.brush_color))
        else:
            self.last_poli_point = (event.x, event.y)
            if self.point_is_poli_vertex(self.last_poli_point):
                self.canvas.storage.figs[-1] = Polygon(self.points, self.brush_color)
                self.last_poli_point = None
                self.points = []
                self.canvas.redraw()
            else:
                self.points.append(Point(event.x, event.y))
                self.canvas.storage.figs[-1].points.append(Point(event.x, event.y))

    def point_is_poli_vertex(self, p):
        x0, y0 = p
        for (x,y) in self.points:
            if abs(x-x0) < 10 and abs(y-y0) < 10:
                return True           

class Polygon(Figure):
    def __init__(self, points, color = (0,0,0)):
        super().__init__(color)
        self.points = points
        self.initial_color = color
        self.selected = False
    
    def draw(self, canvas):
        for segment in self.segments():
            seg_p1, seg_p2 = segment
            canvas.draw_line(seg_p1,seg_p2, color=self.brush_color)

    def find_intersec(self, p1, p2):
        intersections = []
        for segment in self.segments():
            seg_p1, seg_p2 = segment
            intersec = find_segments_intersection(seg_p1, seg_p2, p1, p2)
            if intersec is not None:
                intersections.append(intersec)

        return intersections

    def draw_marked_segment(self, canvas, segment, p, left_color, right_color):
        seg_p1, seg_p2 = segment
        from_left = point_from_left(p, seg_p1, seg_p2)
        if from_left:
            canvas.draw_line(seg_p1, seg_p2, left_color)
        else:
            canvas.draw_line(seg_p1, seg_p2, right_color)

    def segments(self):
        round_points = [(round(p.x), round(p.y)) for p in self.points]
        segments = []
        for i in range(len(round_points) - 1):
            seg = (round_points[i], round_points[i + 1])
            segments.append(seg)
        seg = (round_points[-1], round_points[0])
        segments.append(seg)
        return segments
        
    def draw_marked(self, canvas, p, left_color, right_color):
        for segment in self.segments():
            self.draw_marked_segment(canvas, segment, p, left_color, right_color)

    def check_convex(self, p):
        inside_color = (255, 0, 0)
        outside_color = (0, 0, 255)
        inside = True
        for segment in self.segments():
            seg_p1, seg_p2 = segment
            from_right = point_from_right(p, seg_p1, seg_p2)
            if not from_right:
                inside = False
                break
        if inside:
            self.brush_color = inside_color
            return True
        else:
            self.brush_color = outside_color
            return False

    def check_any(self, p):
        inside_color = (255, 0, 0)
        outside_color = (0, 0, 255)
        sum_angle = 0

        for segment in self.segments():
            seg_p1, seg_p2 = segment
            v1 = (seg_p1[0] - p[0], seg_p1[1] - p[1])
            v2 = (seg_p2[0] - p[0], seg_p2[1] - p[1])
            angle = angle_between_vectors(v1, v2)
            vector_product_z = vector_product_z_axis(v1, v2)
            if vector_product_z > 0:
                sum_angle += angle
            else:
                sum_angle -= angle
        
        normalized_sum = round(sum_angle / (2 * math.pi))
        if abs(normalized_sum) == 1:
            self.brush_color = inside_color
            return True
        elif abs(normalized_sum) == 0:
            self.brush_color = outside_color
            return False
        else:
            print("unexpected value")
            self.brush_color = outside_color
            return False
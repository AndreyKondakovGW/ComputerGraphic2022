from primitives import line_bresenchem
from mouseLine import MouseLine
from functions import *
from primitives import *

class PoligonMode:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.brush_color = color
        self.last_poli_point = None
        self.points = []
    
    def hanble_moution(self, event):
        if self.last_poli_point is not None:
            self.canvas.redraw_content()
            self.canvas.draw_intersections_with_line(self.last_poli_point, (event.x, event.y))
            line_bresenchem(self.canvas.image, self.last_poli_point, (event.x, event.y), self.brush_color)

    def hanble_press(self, event):
        if self.last_poli_point is None:
            self.last_poli_point = (event.x, event.y)
            self.points.append(self.last_poli_point)
            self.canvas.content.append(MouseLine(self.points, self.brush_color))
        else:
            #line_bresenchem(self.img, (event.x, event.y), self.last_poli_point, self.brush_color)

            self.last_poli_point = (event.x, event.y)
            if self.find_pint_in_poli(self.last_poli_point):
                self.canvas.content[-1] = Polygon(self.points, self.brush_color)
                self.last_poli_point = None
                self.points = []
                self.canvas.redraw_content()
            else:
                self.points.append((event.x, event.y))
                self.canvas.content[-1].points.append((event.x, event.y))

    def find_pint_in_poli(self, p):
        x0, y0 = p
        for (x,y) in self.points:
            if abs(x-x0) < 10 and abs(y-y0) < 10:
                return True           
    
    def hanble_release(self, _):
        pass

class Polygon:
    def __init__(self, points, color):
        self.points = points
        self.color = color
        self.initial_color = color
        self.selected = False
    
    def draw(self, canvas):
        for segment in self.segments():
            seg_p1, seg_p2 = segment
            canvas.create_line(seg_p1[0], seg_p1[1], seg_p2[0],seg_p2[1], fill=rgb2hex(self.color))
            #line_bresenchem(canvas.image, seg_p1, seg_p2, self.color)

    def find_intersec(self, p1, p2):
        intersections = []
        for segment in self.segments():
            seg_p1, seg_p2 = segment
            intersec = find_segments_intersection(seg_p1, seg_p2, p1, p2)
            if intersec is not None:
                intersections.append(intersec)

        return intersections
    
    def in_rect(self, p1, p2):
        for p in self.points:
            if not point_in_rect(p, p1, p2):
                return False
        return True

    def draw_marked_segment(self, canvas, segment, p, left_color, right_color):
        seg_p1, seg_p2 = segment
        from_left = point_from_left(p, seg_p1, seg_p2)
        if from_left:
            line_bresenchem(canvas.image, seg_p1, seg_p2, left_color)
        else:
            line_bresenchem(canvas.image, seg_p1, seg_p2, right_color)

    def segments(self):
        round_points = [(round(p[0]), round(p[1])) for p in self.points]
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
            self.color = inside_color
        else:
            self.color = outside_color

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
            self.color = inside_color
        elif abs(normalized_sum) == 0:
            self.color = outside_color
        else:
            print("unexpected value")
            self.color = outside_color
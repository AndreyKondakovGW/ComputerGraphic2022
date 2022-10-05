from primitives import line_bresenchem, line_wu
from functions import *

class LineMode:
    def __init__(self, canvas, color, line_type="bresenchem"):
        self.canvas = canvas
        self.line_type = line_type
        self.brush_color = color
        self.should_draw = False
        self.p0 = None

    def hanble_moution(self, event):
        if self.p0 is not None:
            self.canvas.redraw_content()
            self.canvas.draw_intersections_with_line(self.p0, (event.x, event.y))
            self.draw_line(self.p0, (event.x, event.y))

    def hanble_press(self, event):
        if self.p0 is None:
            self.p0 = (event.x, event.y)
        else:
            self.canvas.content.append(Line(self.p0,(event.x, event.y), self.brush_color))
            self.p0 = None
    def hanble_release(self, _):
        pass

    def draw_line(self, p1, p2):
        if self.line_type == "bresenchem":
            line_bresenchem(self.canvas.image, p1, p2, self.brush_color)
        elif self.line_type == "wu":
            line_wu(self.canvas.image, p1[0], p1[1], p2[0], p2[1], (255, 255, 255), self.brush_color)

class Line:
    def __init__(self, p0, p1, color, line_type="bresenchem"):
        self.line_type = line_type
        self.p0 = p0
        self.p1 = p1
        self.color = color

    def draw(self, canvas):
        if self.line_type == "bresenchem":
            line_bresenchem(canvas.image, self.p0, self.p1, self.color)
        elif self.line_type == "wu":
            line_wu(canvas.image, self.p0[0], self.p0[1], self.p1[0], self.p1[1], (255, 255, 255), self.color)

    def find_intersec(self, p1, p2):
        p = find_segments_intersection(p1, p2, self.p0, self.p1)
        if p is not None:
            return [p]
        return []

    
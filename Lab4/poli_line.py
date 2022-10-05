from primitives import line_bresenchem
from mouseLine import MouseLine
from functions import *

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
                self.canvas.content[-1] = Poligon(self.points, self.brush_color)
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

class Poligon:
    def __init__(self, points, color):
        self.points = points
        self.color = color
        self.selected = False
    
    def draw(self, canvas):
        for i in range(len(self.points)-1):
            line_bresenchem(canvas.image, self.points[i], self.points[i+1], self.color)
        line_bresenchem(canvas.image, self.points[0], self.points[-1], self.color)

    def find_intersec(self, p1, p2):
        intersections = []
        for i in range(len(self.points)-1):
            intersec = find_segments_intersection(self.points[i], self.points[i+1], p1, p2)
            if intersec is not None:
                intersections.append(intersec)
        p = find_segments_intersection(self.points[0], self.points[-1], p1, p2)
        if p is not None:
            intersections.append(p)
        return intersections
    
    def in_rect(self, p1, p2):
        for p in self.points:
            if not point_in_rect(p, p1, p2):
                return False
        return True
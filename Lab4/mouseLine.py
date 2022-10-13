from .functions import *
from src.figure import Figure

class MouseLineMode:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.brush_color = color
        self.should_draw = False
        self.points = []
    
    def hanble_moution(self, event):
        new_coords = (event.x, event.y)
        if self.should_draw:
            if self.old_coords:
                self.canvas.draw_line(self.old_coords, new_coords, self.brush_color)
            self.points.append((event.x, event.y))
        self.old_coords = new_coords

    def hanble_press(self, _):
        self.should_draw = True
    
    def hanble_release(self, _):
        self.should_draw = False
        self.canvas.storage.add_figure(MouseLine(self.points, self.brush_color))
        self.points = []

class MouseLine(Figure):
    def __init__(self, points, color):
        super().__init__(color)
        self.points = points
    
    def draw(self, canvas):
        for i in range(len(self.points)-1):
            canvas.draw_line(self.points[i], self.points[i+1], self.brush_color)
    
    def find_intersec(self, p1, p2):
        intersections = []
        for i in range(len(self.points)-1):
            intersec = find_segments_intersection(self.points[i], self.points[i+1], p1, p2)
            if intersec is not None:
                intersections.append(intersec)
        return intersections

    def draw_marked(self, canvas, _p, _left_color, _right_color):
        self.draw(canvas)
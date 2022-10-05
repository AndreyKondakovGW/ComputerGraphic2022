from primitives import line_bresenchem
from functions import find_segments_intersection

class RectangleMode:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.brush_color = color
        self.p0 = None

    def hanble_moution(self, event):
        if self.p0 is not None:
            self.canvas.redraw_content()
            x1, y1 = self.p0
            x2, y2 = event.x, event.y
            line_bresenchem(self.canvas.image, (x1, y1), (x2, y1), self.brush_color)
            line_bresenchem(self.canvas.image, (x2, y1), (x2, y2), self.brush_color)
            line_bresenchem(self.canvas.image, (x2, y2), (x1, y2), self.brush_color)
            line_bresenchem(self.canvas.image, (x1, y2), (x1, y1), self.brush_color)

    def hanble_press(self, event):
        if self.p0 is None:
            self.p0 = (event.x, event.y)
        else:
            self.canvas.content.append(Rectangle(self.p0,(event.x, event.y), self.brush_color))
            self.p0 = None

    def hanble_release(self, _):
        pass

class Rectangle:
    def __init__(self, p0, p1, color):
        self.p0 = p0
        self.p1 = p1
        self.color = color

    def draw(self, canvas):
        x1, y1 = self.p0
        x2, y2 = self.p1
        line_bresenchem(canvas.image, (x1, y1), (x2, y1), self.color)
        line_bresenchem(canvas.image, (x2, y1), (x2, y2), self.color)
        line_bresenchem(canvas.image, (x2, y2), (x1, y2), self.color)
        line_bresenchem(canvas.image, (x1, y2), (x1, y1), self.color)

    def sides(self):
        first_point = self.p0
        second_horizontal_point = (self.p1[0], self.p0[1])
        second_vertical_point = (self.p0[0], self.p1[1])
        diagonal_point = self.p1
        high_side = (first_point, second_horizontal_point)
        right_side = (second_horizontal_point, diagonal_point)
        low_side = (diagonal_point, second_vertical_point)
        left_side = (second_vertical_point, first_point)
        return [high_side, right_side, low_side, left_side]


    def find_intersec(self, p1, p2):
        intersections = []
        sides = self.sides()
        for side in sides:
            side_p1, side_p2 = side
            intersec = find_segments_intersection(side_p1, side_p2, p1, p2)
            if intersec is not None:
                intersections.append(intersec)
        return intersections
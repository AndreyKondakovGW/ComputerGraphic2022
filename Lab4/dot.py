from functions import point_in_rect
from primitives import rgb2hex

class DotMode:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.brush_color = color

    def hanble_moution(self, _):
        pass

    def hanble_press(self, event):
        p = (event.x, event.y)
        dot = Dot(p, self.brush_color)
        self.canvas.content.append(dot)
        dot.draw(self.canvas)
    
    def hanble_release(self, _):
        pass

class Dot:
    def __init__(self, p, color):
        self.points = [p]
        self.color = color

    def draw(self, canvas):
        x, y = self.points[0]
        canvas.draw_circle(x, y, 2, rgb2hex(self.color))

    def find_intersec(self, p1, p2):
        return []

    def in_rect(self, p1, p2):
        return point_in_rect(self.points[0], p1, p2)

    def draw_marked(self, canvas, _p, _left_color, _right_color):
        self.draw(canvas)
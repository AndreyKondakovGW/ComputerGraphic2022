from primitives import line_bresenchem
from functions import *
from poli_line import Poligon

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
            x1, y1 = self.p0
            x2, y2 = event.x, event.y
            rect_p = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
            self.canvas.content.append(Poligon(rect_p, self.brush_color))
            self.p0 = None

    def hanble_release(self, _):
        pass
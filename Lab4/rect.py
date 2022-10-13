from .functions import *
from .poli_line import Polygon
from .line_intersector import draw_intersections_with_line

class RectangleMode:
    def __init__(self, canvas, color=(0,0,0)):
        self.canvas = canvas
        self.brush_color = color
        self.p0 = None

    def hanble_moution(self, event):
        if self.p0 is not None:
            x1, y1 = self.p0
            x2, y2 = event.x, event.y
            self.canvas.redraw()
            self.canvas.draw_line((x1, y1), (x2, y1), self.brush_color)
            self.canvas.draw_line((x2, y1), (x2, y2), self.brush_color)
            self.canvas.draw_line((x2, y2), (x1, y2), self.brush_color)
            self.canvas.draw_line((x1, y2), (x1, y1), self.brush_color)

            draw_intersections_with_line(self.canvas, (x1, y1), (x2, y1))
            draw_intersections_with_line(self.canvas, (x2, y1), (x2, y2))
            draw_intersections_with_line(self.canvas, (x2, y2), (x1, y2))
            draw_intersections_with_line(self.canvas, (x1, y2), (x1, y1))

    def hanble_press(self, event):
        if self.p0 is None:
            self.p0 = (event.x, event.y)
        else:
            x1, y1 = self.p0
            x2, y2 = event.x, event.y
            rect_p = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
            self.canvas.storage.add_figure(Polygon(rect_p, self.brush_color))
            self.p0 = None

    def hanble_release(self, _):
        pass

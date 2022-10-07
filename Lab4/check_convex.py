from dot import Dot
from poli_line import Polygon

class CheckPolygonMode:
    def __init__(self, canvas, color, convex=True):
        self.canvas = canvas
        self.brush_color = color
        self.check_convex = convex

    def hanble_moution(self, event):
        p = (event.x, event.y)
        for fig in self.canvas.content:
            if isinstance(fig, Polygon):
                self.check_polygon(fig, p)
                #fig.check_convex(p)
        self.canvas.redraw_content()

    def hanble_press(self, _):
        for fig in self.canvas.content:
            if isinstance(fig, Polygon):
                fig.color = self.brush_color
        self.canvas.redraw_content()

    def hanble_release(self, _):
        pass

    def check_polygon(self, poly, point):
        if self.check_convex:
            poly.check_convex(point)
        else:
            poly.check_any(point)
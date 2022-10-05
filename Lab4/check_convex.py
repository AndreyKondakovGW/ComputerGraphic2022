from dot import Dot
from poli_line import Polygon

class CheckConvexMode:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.brush_color = color

    def hanble_moution(self, event):
        p = (event.x, event.y)
        for fig in self.canvas.content:
            if isinstance(fig, Polygon):
                fig.check_convex(p)
        self.canvas.redraw_content()

    def hanble_press(self, _):
        for fig in self.canvas.content:
            if isinstance(fig, Polygon):
                fig.color = self.brush_color
        self.canvas.redraw_content()

    def hanble_release(self, _):
        pass
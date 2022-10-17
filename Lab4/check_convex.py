from .poligon import Polygon
from src.controller_mode import ControllerMode

class CheckPolygonMode(ControllerMode):
    def __init__(self, canvas, color = (0,0,0), convex=True):
        self.canvas = canvas
        self.brush_color = color
        self.check_convex = convex

    def hanble_moution(self, event):
        p = (event.x, event.y)
        self.canvas.storage.apply(lambda fig: self.check_polygon(fig, p) if isinstance(fig, Polygon) and not fig.selected else None)
        self.canvas.redraw()

    def hanble_press(self, event):
        p = (event.x, event.y)
        self.canvas.storage.apply(lambda fig: self.select_polygon(fig, p))
        self.canvas.redraw()

    def check_polygon(self, poly, point):
        if self.check_convex:
            return poly.check_convex(point)
        else:
            return poly.check_any(point)

    def select_polygon(self, fig, p):
        if isinstance(fig, Polygon) and not fig.selected:
            if self.check_polygon(fig, p):
                fig.select()
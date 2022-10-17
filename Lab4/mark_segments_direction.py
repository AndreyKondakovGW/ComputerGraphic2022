from .dot import Dot
from src.controller_mode import ControllerMode

class MarkSegmentsDirectionMode(ControllerMode):
    def __init__(self, canvas, color=(255, 0, 0)):
        self.canvas = canvas
        self.brush_color = color

    def hanble_press(self, event):
        p = (event.x, event.y)
        self.canvas.clear()
        self.canvas.storage.add_figure(Dot(p, self.brush_color))
        left_color = (0, 255, 0)
        right_color = (0, 0, 255)
        self.canvas.storage.apply(lambda fig: fig.draw_marked(self.canvas, p, left_color, right_color))
from primitives import *

class RectSelector:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.brush_color = color
        self.should_draw = False
        self.p0 = None

    def hanble_moution(self, event):
        if self.should_draw:
            self.canvas.redraw_content()
            x1, y1 = self.p0
            x2, y2 = event.x, event.y
            self.canvas.create_line(x1, y1, x2, y1, fill=rgb2hex(self.brush_color), dash=(4, 2))
            self.canvas.create_line(x2, y1, x2, y2, fill=rgb2hex(self.brush_color), dash=(4, 2))
            self.canvas.create_line(x2, y2, x1, y2, fill=rgb2hex(self.brush_color), dash=(4, 2))
            self.canvas.create_line(x1, y2, x1, y1, fill=rgb2hex(self.brush_color), dash=(4, 2))

    def hanble_press(self, event):
        if event.widget == self.canvas:
            self.should_draw = True
            self.p0 = (event.x, event.y)
            self.canvas.deselect_figs()

    def hanble_release(self, event):
        if self.should_draw:
            self.should_draw = False
            self.canvas.select_figs_in_rect(self.p0, (event.x, event.y))
            self.p0 = None

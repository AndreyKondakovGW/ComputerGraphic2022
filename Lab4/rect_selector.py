from src.controller_mode import ControllerMode

class RectSelectorMode(ControllerMode):
    def __init__(self, canvas, color=(0,0,0)):
        self.canvas = canvas
        self.brush_color = color
        self.should_draw = False
        self.p0 = None

    def hanble_moution(self, event):
        if self.should_draw:
            x1, y1 = self.p0
            x2, y2 = event.x, event.y

            self.canvas.redraw()
            self.canvas.draw_dash_line((x1, y1), (x2, y1), self.brush_color)
            self.canvas.draw_dash_line((x2, y1), (x2, y2), self.brush_color)
            self.canvas.draw_dash_line((x2, y2), (x1, y2), self.brush_color)
            self.canvas.draw_dash_line((x1, y2), (x1, y1), self.brush_color)

    def hanble_press(self, event):
        self.should_draw = True
        self.p0 = (event.x, event.y)
        self.canvas.storage.apply(lambda fig: fig.deselect())

    def hanble_release(self, event):
        if self.should_draw:
            self.canvas.storage.apply(lambda fig: fig.select() if fig.in_rect(self.p0, (event.x, event.y)) else fig.deselect())
            self.should_draw = False
            self.p0 = None
            self.canvas.redraw()

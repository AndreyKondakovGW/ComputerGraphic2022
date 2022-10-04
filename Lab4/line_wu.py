from primitives import line_wu

class WuLineMode:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.brush_color = color
        self.should_draw = False
        self.p0 = None

    def hanble_moution(self, event):
        if self.p0 is not None:
            self.canvas.redraw_content()
            line_wu(self.canvas.image, self.p0[0], self.p0[1], event.x, event.y, (255, 255, 255), self.brush_color)
    
    def hanble_press(self, event):
        if self.p0 is None:
            self.p0 = (event.x, event.y)
        else:
            #line_wu(self.canvas.image, self.p0[0], self.p0[1], event.x, event.y, (255, 255, 255), self.brush_color)
            self.canvas.content.append(WuLine(self.p0,(event.x, event.y), self.brush_color))
            self.p0 = None
    
    def hanble_release(self, _):
        pass

class WuLine:
    def __init__(self, p0, p1, color):
        self.p0 = p0
        self.p1 = p1
        self.color = color

    def draw(self, canvas):
        line_wu(canvas.image, self.p0[0], self.p0[1], self.p1[0], self.p1[1], (255, 255, 255), self.color)
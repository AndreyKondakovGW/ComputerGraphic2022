from primitives import line_bresenchem

class BerthLineMode:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.brush_color = color
        self.should_draw = False
        self.p0 = None

    def hanble_moution(self, event):
        if self.p0 is not None:
            self.canvas.redraw_content()
            line_bresenchem(self.canvas.image, self.p0, (event.x, event.y), self.brush_color)
    
    def hanble_press(self, event):
        if self.p0 is None:
            self.p0 = (event.x, event.y)
        else:
            #line_bresenchem(self.canvas.image, (self.p1_be[0], self.p1_be[1]), (event.x, event.y), self.brush_color)
            self.canvas.content.append(BerthLine(self.p0,(event.x, event.y), self.brush_color))
            self.p0 = None

    def hanble_release(self, _):
        pass

class BerthLine:
    def __init__(self, p0, p1, color):
        self.p0 = p0
        self.p1 = p1
        self.color = color

    def draw(self, canvas):
        line_bresenchem(canvas.image, self.p0, self.p1, self.color)
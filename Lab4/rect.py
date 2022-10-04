from primitives import line_bresenchem

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
            self.canvas.content.append(Rectangle(self.p0,(event.x, event.y), self.brush_color))
            self.p0 = None

    def hanble_release(self, _):
        pass

class Rectangle:
    def __init__(self, p0, p1, color):
        self.p0 = p0
        self.p1 = p1
        self.color = color

    def draw(self, canvas):
        x1, y1 = self.p0
        x2, y2 = self.p1
        line_bresenchem(canvas.image, (x1, y1), (x2, y1), self.color)
        line_bresenchem(canvas.image, (x2, y1), (x2, y2), self.color)
        line_bresenchem(canvas.image, (x2, y2), (x1, y2), self.color)
        line_bresenchem(canvas.image, (x1, y2), (x1, y1), self.color)
from src.figure import Figure

class DotMode:
    def __init__(self, canvas, color=(0,0,0)):
        self.canvas = canvas
        self.brush_color = color

    def hanble_moution(self, _):
        pass

    def hanble_press(self, event):
        p = (event.x, event.y)
        self.canvas.storage.add_figure(Dot(p, self.brush_color))
    
    def hanble_release(self, _):
        pass

class Dot(Figure):
    def __init__(self, p, color):
        super().__init__(color)
        self.points = [p]

    def draw(self, canvas):
        x, y = self.points[0]
        canvas.draw_circle(x, y, 2, self.brush_color)

    def find_intersec(self, p1, p2):
        return []

    def draw_marked(self, canvas, _p, _left_color, _right_color):
        self.draw(canvas)
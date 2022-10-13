from .dot import Dot

class MarkSegmentsDirectionMode:
    def __init__(self, canvas, color=(255, 0, 0)):
        self.canvas = canvas
        self.brush_color = color

    def hanble_moution(self, _):
        pass

    def hanble_press(self, event):
        p = (event.x, event.y)
        dot = Dot(p, self.brush_color)
        self.canvas.content.append(dot)
        self.canvas.clear()
        dot.draw(self.canvas)
        left_color = (0, 255, 0)
        right_color = (0, 0, 255)
        for fig in self.canvas.content:
            fig.draw_marked(self.canvas, p, left_color, right_color)

    def hanble_release(self, _):
        pass
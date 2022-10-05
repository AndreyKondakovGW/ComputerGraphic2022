from primitives import line_bresenchem

class MouseLineMode:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.brush_color = color
        self.should_draw = False
        self.points = []
    
    def hanble_moution(self, event):
        new_coords = (event.x, event.y)
        if self.should_draw:
            if self.old_coords:
                line_bresenchem(self.canvas.image, new_coords, self.old_coords, self.brush_color)
            self.points.append((event.x, event.y))
        self.old_coords = new_coords

    def hanble_press(self, _):
        self.should_draw = True
    
    def hanble_release(self, _):
        self.should_draw = False
        self.canvas.content.append(MouseLine(self.points, self.brush_color))
        self.points = []

class MouseLine:
    def __init__(self, points, color):
        self.points = points
        self.color = color
    
    def draw(self, canvas):
        for i in range(len(self.points)-1):
            line_bresenchem(canvas.image, self.points[i], self.points[i+1], self.color)
    
    def find_intersec(self, p1, p2):
        return []
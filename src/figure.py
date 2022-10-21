from Lab4.functions import point_in_rect

class Figure:
    def __init__(self, color):
        self.brush_color = color
        self.initial_color = color
        self.selected = False
        self.points = []
        self.canvas_points = []

    def draw(self, _):
        pass

    def find_intersec(self, p1, p2):
        return []

    def in_rect(self, p1, p2):
        if len(self.canvas_points) == 0:
            for p in self.points:
                if not point_in_rect(p, p1, p2):
                    return False
        else:
            for p in self.canvas_points:
                if not point_in_rect(p, p1, p2):
                    return False
        return True

    def select(self):
        self.selected = True
        self.brush_color = (255, 0, 0)

    def deselect(self):
        self.selected = False
        self.brush_color = self.initial_color
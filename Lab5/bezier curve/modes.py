class DummyMode:
    def __init__(self):
        pass

    def handle_motion(self, event):
        pass

    def handle_press(self, event):
        pass

    def handle_release(self, event):
        pass


class AddMode:
    def __init__(self, canvas):
        self.canvas = canvas
        pass

    def handle_motion(self, event):
        pass

    def handle_press(self, event):
        if event.widget == self.canvas:
            self.canvas.points.append((event.x, event.y))
            self.canvas.redraw_points()

    def handle_release(self, event):
        pass


class MoveMode:
    def __init__(self, canvas):
        self.canvas = canvas
        self.index_moving_point = None
        pass

    def handle_motion(self, event):
        pass

    def handle_press(self, event):
        for idx in range(0, len(self.canvas.points)):
            p = self.canvas.points[idx]
            if abs(event.x - p[0]) <= 3 and abs(event.y - p[1]) <= 3:
                self.index_moving_point = idx

    def handle_release(self, event):
        if self.index_moving_point is not None:
            self.canvas.points[self.index_moving_point] = (event.x, event.y)
            self.index_moving_point = None
            self.canvas.redraw_points()


class DeleteMode:
    def __init__(self, canvas):
        self.canvas = canvas
        pass

    def handle_motion(self, event):
        pass

    def handle_press(self, event):
        self.canvas.points = [p for p in self.canvas.points if
                              not (abs(event.x - p[0]) <= 3 and abs(event.y - p[1]) <= 3)]
        self.canvas.redraw_points()

    def handle_release(self, event):
        pass

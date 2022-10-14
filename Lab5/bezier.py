from src.figure import Figure
from src.controller_mode import ControllerMode
from Lab5.bezier_curve import draw_bezier_curve

class BezierMode(ControllerMode):
    def __init__(self, canvas, color=(0,0,0)):
        self.ad_point = None
        self.canvas = canvas
        self.brush_color = color
        self.points = []
        self.moving_inx = None
        self.shold_move = False

    def hanble_press(self, event):
        p = (event.x, event.y)
        if self.moving_inx is not None:
            self.moving_inx = None
        if self.moving_inx is None:
            for idx in range(len(self.points)):
                p = self.points[idx]
                if abs(event.x - p[0]) <= 5 and abs(event.y - p[1]) <= 5:
                    self.moving_inx = idx
                    self.shold_move = True
        if self.moving_inx is None:
            self.points.append((event.x, event.y))
            for p in self.points:
                self.canvas.draw_circle(p[0], p[1], 3, color=(127, 0, 127))
            self.ad_point, self.points = draw_bezier_curve(self.canvas, self.points, self.ad_point)
            if len(self.points) == 1:
                self.canvas.storage.add_figure(BezierCurv(self.points, self.ad_point))
            else:
                self.canvas.storage.figs[-1].points = self.points
                self.canvas.storage.figs[-1].ad_point = self.ad_point
        self.canvas.redraw()

    def hanble_release(self, event):
        print(self.shold_move)
        self.shold_move = False
        self.moving_inx = None

    def hanble_moution(self, event):
        if self.shold_move:
            print(self.moving_inx)
            self.points[self.moving_inx] = (event.x, event.y)
            self.ad_point, self.points = draw_bezier_curve(self.canvas, self.points, self.ad_point)
            if len(self.points) == 1:
                self.canvas.storage.add_figure(BezierCurv(self.points, self.ad_point))
            else:
                self.canvas.storage.figs[-1].points = self.points
                self.canvas.storage.figs[-1].ad_point = self.ad_point
            self.canvas.redraw()

    def hanble_right_press(self, event):
        delidx = -1
        for i in range(len(self.points)):
            p = self.points[i]
            if abs(event.x - p[0]) <= 5 and abs(event.y - p[1]) <= 5:
                delidx = i
        if delidx != -1:
            del self.points[delidx]
            if len(self.points) == 1:
                self.canvas.storage.add_figure(BezierCurv(self.points, self.ad_point))
            else:
                self.canvas.storage.figs[-1].points = self.points
                self.canvas.storage.figs[-1].ad_point = self.ad_point
        self.canvas.redraw()
        pass

class BezierCurv(Figure):
    def __init__(self, points,ad_point, color = (0,0,0)):
        super().__init__(color)
        self.points = points
        self.ad_point = ad_point

    def draw(self, canvas):
        for p in self.points:
            canvas.draw_circle(p[0], p[1], 3, color=(127, 0, 127))
        self.ad_point, self.points = draw_bezier_curve(canvas, self.points, self.ad_point)

    def find_intersec(self, p1, p2):
        return []

    def draw_marked(self, canvas, _p, _left_color, _right_color):
        self.draw(canvas)
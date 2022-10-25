from Lab6.figures.line3D import Line3D
from Lab6.transformation_3d import *
from src.controller_mode import ControllerMode

def rotate_figure(fig, dir, angle, rotation_line):
    if rotation_line:
        p1 = rotation_line.points[0]
        p2 = rotation_line.points[1]

        dir = (p2.x - p1.x, p2.y - p1.y, p2.z - p1.z)
        center = (p1.x, p1.y, p1.z)
    else:
        center =  centroid(fig.points)
    rotate(fig.points, center, dir,  angle)

class RotatorMode3D(ControllerMode):
    def __init__(self, renderer,scene):
        self.renderer = renderer
        self.scene = scene
        self.canvas = self.renderer.canvas
        self.brush_color = (0, 255, 0)
        self.set_default_params()

    def set_default_params(self):
        self.should_draw = False
        self.isXmode = False
        self.isYmode = False
        self.isZmode = False
        self.p0 = None
        self.rotation_line = None

    def hanble_moution(self, event):
        if self.should_draw:
            x1, y1 = self.p0
            x2, y2 = event.x, event.y

            self.renderer.render_scene(self.scene)
            self.canvas.draw_dash_line((x1, y1), (x2, y1), self.brush_color)
            self.canvas.draw_dash_line((x2, y1), (x2, y2), self.brush_color)
            self.canvas.draw_dash_line((x2, y2), (x1, y2), self.brush_color)
            self.canvas.draw_dash_line((x1, y2), (x1, y1), self.brush_color)

    def hanble_press(self, event):
        self.should_draw = True
        self.p0 = (event.x, event.y)
        self.rotation_line = None
        self.renderer.render_scene(self.scene)

    def hanble_release(self, event):
        if self.should_draw:
            self.rotation_line = None
            for fig in self.scene.storage:
                if fig.in_rect(self.p0, (event.x, event.y)):
                    if isinstance(fig,Line3D):
                        self.rotation_line = fig
                        fig.brush_color = (0, 255, 0)
                        break
            self.should_draw = False
            self.p0 = None
            self.renderer.render_scene(self.scene)

    def hanble_x(self, event):
        self.isXmode = True
        self.isYmode = False
        self.isZmode = False

    def hanble_y(self, event):
        self.isYmode = True
        self.isXmode = False
        self.isZmode = False


    def hanble_z(self, event):
        self.isZmode = True
        self.isXmode = False
        self.isYmode = False

    def hanble_left(self, event):
        dir = (int(self.isXmode), int(self.isYmode), int(self.isZmode))
        angle = -5

        for fig in self.scene.storage:
            if fig.selected:
                rotate_figure(fig, dir, angle, self.rotation_line)
        self.renderer.render_scene(self.scene)

    def hanble_right(self, event):
        dir = (int(self.isXmode), int(self.isYmode), int(self.isZmode))
        angle = 5
        for fig in self.scene.storage:
            if fig.selected:
                rotate_figure(fig, dir, angle, self.rotation_line)
        self.renderer.render_scene(self.scene)

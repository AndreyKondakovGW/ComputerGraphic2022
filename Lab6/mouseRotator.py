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

class MouseRotatorMode3D(ControllerMode):
    def __init__(self, renderer,scene):
        self.renderer = renderer
        self.scene = scene
        self.canvas = self.renderer.canvas
        self.brush_color = (0, 255, 0)
        self.set_default_params()
        self.should_draw = False
        self.p0 = None

    def set_default_params(self):
        self.should_draw = False
        self.isXmode = False
        self.isYmode = False
        self.isZmode = False
        self.p0 = None
        self.rotation_line = None

    def hanble_moution(self, event):
        if self.p0 is not None:
            k_x = int(event.x - self.p0[0])
            k_y = int(event.y - self.p0[1])
            dir_x = (0,-1,0)
            dir_y = (-1,0,0)
            for fig in self.scene.storage:
                if fig.selected:
                    rotate_figure(fig,  dir_x, k_x, self.rotation_line)
            for fig in self.scene.storage:
                if fig.selected:
                    rotate_figure(fig,  dir_y, k_y, self.rotation_line)
            self.renderer.render_scene(self.scene)
            self.p0 = (event.x, event.y)

    def hanble_press(self, event):
        self.should_draw = True
        self.p0 = (event.x, event.y)

    def hanble_release(self, _):
        self.should_draw = False
        self.p0 = None

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

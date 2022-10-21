from Lab6.transformation_3d import *
from src.controller_mode import ControllerMode

def move_figure(fig, dx, dy,dz):
    old_points = fig.points
    if fig.selected:
        fig.points = translate(fig.points, dx, dy, dz)

class MoverMode3D(ControllerMode):
    def __init__(self, renderer,scene):
        self.renderer = renderer
        self.scene = scene
        self.should_draw = False
        self.isXmode = False
        self.isYmode = False
        self.isZmode = False

    def hanble_x(self, event):
        self.isXmode = not self.isXmode 

    def hanble_y(self, event):
        self.isYmode = not self.isYmode

    def hanble_z(self, event):
        self.isZmode = not self.isZmode

    def hanble_left(self, event):
        x = int(self.isXmode) * -5
        y = int(self.isYmode) * -5
        z = int(self.isZmode) * -5
        for fig in self.scene.storage:
            if fig.selected:
                move_figure(fig, x, y, z)
        self.renderer.render_scene(self.scene)

    def hanble_right(self, event):
        x = int(self.isXmode) * 5
        y = int(self.isYmode) * 5
        z = int(self.isZmode) * 5
        for fig in self.scene.storage:
            if fig.selected:
                move_figure(fig, x, y, z)
        self.renderer.render_scene(self.scene)

from Lab6.transformation_3d import *
from src.controller_mode import ControllerMode

def scale_figure(fig, kx, ky, kz):
    if fig.selected:
        scale(fig.points, kx, ky, kz)

class ScalerMode3D(ControllerMode):
    def __init__(self, renderer,scene):
        self.renderer = renderer
        self.scene = scene
        self.set_default_params()

    def set_default_params(self):
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
        x = 1 + int(self.isXmode) * -0.1
        y = 1 + int(self.isYmode) * -0.1
        z = 1 + int(self.isZmode) * -0.1
        for fig in self.scene.storage:
            if fig.selected:
                scale_figure(fig, x, y, z)
        self.renderer.render_scene(self.scene)

    def hanble_right(self, event):
        x = 1 + int(self.isXmode) * 0.1
        y = 1 + int(self.isYmode) * 0.1
        z = 1 +  int(self.isZmode) * 0.1
        for fig in self.scene.storage:
            if fig.selected:
                scale_figure(fig, x, y, z)
        self.renderer.render_scene(self.scene)
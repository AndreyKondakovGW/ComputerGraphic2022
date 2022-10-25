from Lab6.transformation_3d import *
from src.controller_mode import ControllerMode

def scale_figure(fig, kx, ky, kz):
    just_scale(fig.points, kx, ky, kz)

class MirrorMode3D(ControllerMode):
    def __init__(self, renderer,scene):
        self.renderer = renderer
        self.scene = scene

    def hanble_x(self, event):
        for fig in self.scene.storage:
            if fig.selected:
                scale_figure(fig, -1, 1, 1)
        self.renderer.render_scene(self.scene)

    def hanble_y(self, event):
        for fig in self.scene.storage:
            if fig.selected:
                scale_figure(fig, 1, -1, 1)
        self.renderer.render_scene(self.scene)
        
    def hanble_z(self, event):
        for fig in self.scene.storage:
            if fig.selected:
                scale_figure(fig, 1, 1, -1)
        self.renderer.render_scene(self.scene)
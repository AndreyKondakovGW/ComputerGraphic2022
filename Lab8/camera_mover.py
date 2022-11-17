from Lab6.transformation_3d import *
from src.controller_mode import ControllerMode
from src.point import *

class CameraMoverMode(ControllerMode):
    def __init__(self, renderer,scene, camera):
        self.renderer = renderer
        self.scene = scene
        self.camera = camera
        self.move_speed = 1
        self.rotate_speed = 0.0001
        self.set_default_params()

    def set_default_params(self):
        self.should_draw = False
        self.p0 = None

    def hanble_w(self, event):
        self.camera.change_position(self.camera.direction * -self.move_speed)
        self.renderer.render_scene(self.scene)

    def hanble_a(self, event):
        self.camera.change_position(self.camera.right * -self.move_speed)
        self.renderer.render_scene(self.scene)

    def hanble_s(self, event):
        self.camera.change_position(self.camera.direction * self.move_speed)
        self.renderer.render_scene(self.scene)

    def hanble_d(self, event):
        self.camera.change_position(self.camera.right * self.move_speed)
        self.renderer.render_scene(self.scene)

    def hanble_q(self, event):
        self.camera.change_position(self.camera.up * self.move_speed)
        self.renderer.render_scene(self.scene)

    def hanble_e(self, event):
        self.camera.change_position(self.camera.up * -self.move_speed)
        self.renderer.render_scene(self.scene)

    def hanble_press(self, event):
        self.should_draw = True
        self.p0 = (event.x, event.y)

    def hanble_release(self, _):
        self.should_draw = False
        self.p0 = None

    def hanble_moution(self, event):
        if self.p0 is not None:
            d_x = int(event.x - self.p0[0])
            d_y = int(event.y - self.p0[1])

            self.camera.change_rotation(d_x * self.rotate_speed, d_y * self.rotate_speed)
            self.renderer.render_scene(self.scene)

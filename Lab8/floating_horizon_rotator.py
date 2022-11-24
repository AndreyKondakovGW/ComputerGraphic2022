from Lab8.floating_horizon import PlotFloatingHorizon
from src.controller_mode import ControllerMode


class FloatingHorizonRotatorMode(ControllerMode):
    def __init__(self, renderer, scene):
        self.renderer = renderer
        self.scene = scene
        self.canvas = self.renderer.canvas
        self.x_angle = 0
        self.y_angle = 0

    def hanble_a(self, event):
        plot = find_plot(self.scene.storage)
        self.x_angle -= 5
        plot.change_x_angle(self.x_angle)
        self.renderer.render_scene(self.scene)

    def hanble_s(self, event):
        plot = find_plot(self.scene.storage)
        self.y_angle -= 5
        plot.change_y_angle(self.y_angle)
        self.renderer.render_scene(self.scene)

    def hanble_d(self, event):
        plot = find_plot(self.scene.storage)
        self.x_angle += 5
        plot.change_x_angle(self.x_angle)
        self.renderer.render_scene(self.scene)

    def hanble_w(self, event):
        plot = find_plot(self.scene.storage)
        self.y_angle += 5
        plot.change_y_angle(self.y_angle)
        self.renderer.render_scene(self.scene)


def find_plot(storage):
    for x in storage:
        if isinstance(x, PlotFloatingHorizon):
            return x

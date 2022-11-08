from Lab6.projections import *


from typing import Callable

class SideMenuController():
    def __init__(self, renderer, scene, default_mode, default_instrument):
        self.mode_name = default_mode
        self.instrument_name = default_instrument
        self.modes = {}
        self.instruments = {}
        self.renderer = renderer
        self.scene = scene

    def add_instrument(self, name: str, figure_creator_instrument: Callable):
        self.instruments[name] = figure_creator_instrument

    def add_mode(self, name: str, command: Callable):
        self.modes[name] = command

    def set_mode(self, mode_name):
        self.mode_name = mode_name
        self.renderer.set_projection(self.modes[mode_name])
        self.renderer.render_scene(self.scene)

    def set_instrument(self, instrument_name):
        self.instrument_name = instrument_name

    def draw_figure(self):
        figure = self.instruments[self.instrument_name]()
        self.scene.add_figure(figure)
        self.renderer.render_scene(self.scene)
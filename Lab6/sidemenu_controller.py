from Lab6.projections import *

from typing import Callable
from Lab7.rotation_figure import RotationFigure
from src.point import Point
from Lab6.point3D import Point3D
from Lab6.figures.line3D import Line3D
from Lab6.figures.cube import Cube
from Lab6.figures.tetrahedron import Tetrahedron
from Lab6.figures.octahedron import Octahedron
from Lab6.figures.icosahedron import Icosahedron
from Lab6.figures.dodecahedron import Dodecahedron


class SideMenu_Controller():
    def __init__(self, renderer, scene, loader, default_mode="2D", default_instrument="Point"):
        self.loader = loader
        self.mode_projection = {
            "2D": simple2D_projection(),
            "3D perspective": perspective_projection(),
            "3D aksonometric": akso_projection(),
            "Camera": None
        }
        self.figures_names = ["Point", "Line", "Cube", "Tetrahedron", "Octahedron", "Icosahedron", "Dodecahedron",
                              "Load Figure"]
        self.renderer = renderer
        self.scene = scene
        self.camera = None
        self.forming_point = None
        self.axes = ['OX', 'OY', 'OZ']
        self.axis = None
        self.rotation_axis = None
        self.partition = None
        self.mode_name = default_mode
        self.instrument_name = default_instrument
        self.modes = {}
        self.instruments = {}

    def add_instrument(self, name: str, figure_creator_instrument: Callable):
        self.instruments[name] = figure_creator_instrument

    def add_mode(self, name: str, command: Callable):
        self.modes[name] = command

    def set_mode(self, mode_name):
        if mode_name == "Camera" and self.camera is not None:
            self.mode_name = mode_name
            self.renderer.camera = self.camera
        else:
            self.renderer.camera = None
            self.mode_name = mode_name
            self.renderer.set_projection(self.modes[mode_name])
        self.renderer.render_scene(self.scene)

    def set_instrument(self, instrument_name):
        self.instrument_name = instrument_name

    def draw_figure(self):
        figure = self.instruments[self.instrument_name]()
        self.scene.add_figure(figure)
        self.renderer.render_scene(self.scene)
        if self.figure_name == "Point":
            self.scene.add_figure(Point3D(Point(0, 50, 0), (255, 0, 0)))
        elif self.figure_name == "Line":
            self.scene.add_figure(Line3D(Point(100, 0, 0), Point(0, 0, 0)))
        elif self.figure_name == "Cube":
            self.scene.add_figure(Cube(Point(50, 50, 50), 100))
        elif self.figure_name == "Tetrahedron":
            self.scene.add_figure(Tetrahedron(Point(50, 50, 50), 100))
        elif self.figure_name == "Octahedron":
            self.scene.add_figure(Octahedron(Point(50, 50, 50), 100))
        elif self.figure_name == "Icosahedron":
            self.scene.add_figure(Icosahedron(Point(50, 50, 50), 100))
        elif self.figure_name == "Dodecahedron":
            self.scene.add_figure(Dodecahedron(Point(50, 50, 50), 100))
        elif self.figure_name == "Load Figure":
            res = self.loader.open_file()
            self.scene.add_figure(res)
        self.renderer.render_scene(self.scene)

    def axis_update(self, event):
        axis = event.widget.get()
        self.axis = axis
    def add_forming_point(self):  # не очень красивый код, но я не придумала лучше
        flag = False
        i = []
        for x in self.scene.storage:
            if isinstance(x, RotationFigure):
                flag = True
                i.append(x)
        if flag:
            for x in i:
                if x.selected:
                    x.update_rotation_figure(self.forming_point, self.partition, self.axis)
        else:
            self.scene.add_figure(RotationFigure(Point(50, 50, 50), self.axis, self.partition))
            self.scene.storage[-1].update_rotation_figure(self.forming_point, self.partition, self.axis)
        self.renderer.render_scene(self.scene)

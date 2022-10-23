from Lab6.projections import *
from src.point import Point
from Lab6.point3D import Point3D
from Lab6.line3D import Line3D
from Lab6.cube import Cube
from Lab6.tetrahedron import Tetrahedron
from Lab6.octahedron import Octahedron

class SideMenu_Controller():
    def __init__(self, renderer, scene):
        self.mode_name = "2D"
        self.instrument_name = "Point"
        self.mode_projection = {
            "2D": simple2D_projection(),
            "3D perspective": perspective_projection(),
            "3D aksonometric": akso_projection(),
        }
        self.figures_names = ["Point", "Line", "Cube", "Tetrahedron", "Octahedron"]
        self.renderer = renderer
        self.scene = scene


    def mode_update(self, event):
        mode_name = event.widget.get()
        self.mode_name = mode_name
        self.renderer.set_projection(self.mode_projection[mode_name])
        self.renderer.render_scene(self.scene)

    def figure_update(self, event):
        figure_name = event.widget.get()
        self.figure_name = figure_name

    def draw_figure(self):
        if self.figure_name == "Point":
            self.scene.add_figure(Point3D(Point(50, 50, 50), (255, 0, 0)))
        elif self.figure_name == "Line":
            self.scene.add_figure(Line3D([Point(100, 0, 0), Point(0, 0, 0)]))
        elif self.figure_name == "Cube":
            self.scene.add_figure(Cube(Point(50,50,50), 100))
        elif self.figure_name == "Tetrahedron":
            self.scene.add_figure(Tetrahedron(Point(50,50,50), 100))
        elif self.figure_name == "Octahedron":
            self.scene.add_figure(Octahedron(Point(50,50,50), 100))
        self.renderer.render_scene(self.scene)

    

from src.controller_mode import ControllerMode
from Indv_Kondakov.delaunay import *
from Lab4.dot import Dot
from Lab4.poligon import Polygon

class TriangulationMode(ControllerMode):
    def __init__(self, canvas):
        self.canvas = canvas
        self.should_draw = False

    def init_params(self):
        points_list = []
        for fig in self.canvas.storage.figs:
            if isinstance(fig, Dot) and fig.selected:
                points_list += fig.points
        
        triangeles = triangulate_delaunay_auto(points_list, self.canvas)

        for t in triangeles:
            self.canvas.storage.add_figure(Polygon(t, self.brush_color))
        pass
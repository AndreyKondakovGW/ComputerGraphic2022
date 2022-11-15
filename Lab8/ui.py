from Lab7.ui import UI7
from src.point import Point
from Lab8.colored_tetrahedron import ColoredTetrahedron
from Lab8.poly_renderer import PolyRenderer

class UI8(UI7):
    def init_sidemenu_instruments(self):
        super().init_sidemenu_instruments()
        self.side_menu_controller.add_instrument("Colored Tetrahedron", lambda: ColoredTetrahedron(Point(50,50,50), 100))

    def create_renderer(self):
        self.renderer = PolyRenderer(self.canv)
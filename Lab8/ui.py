from Lab7.ui import UI7
from src.point import Point
from Lab8.colored_tetrahedron import ColoredTetrahedron
from Lab8.poly_renderer import PolyRenderer

class UI8(UI7):
    def init_sidemenu_instruments(self):
        super().init_sidemenu_instruments()
        self.side_menu_controller.add_instrument("Colored Tetrahedron", lambda: ColoredTetrahedron(Point(50,50,50), 100))

    def add_leftmost_buttons(self):
        super().add_leftmost_buttons()
        self.add_button("Show/Hide axis", command=self.toggle_show_axis)

    def toggle_show_axis(self):
        self.renderer.show_axis = not self.renderer.show_axis
        self.renderer.render_scene(self.scene)

    def create_renderer(self):
        self.renderer = PolyRenderer(self.canv)
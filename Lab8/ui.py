from Lab7.ui import UI7
from src.point import Point
from Lab8.colored_tetrahedron import ColoredTetrahedron
#from Lab8.colored_cube import ColoredCube
from Lab8.poly_renderer import PolyRenderer
from src.renderer import Renderer
from Lab8.camera_mover import CameraMoverMode

class UI8(UI7):
    def __init__(self):
        super().__init__()

    def init_sidemenu_instruments(self):
        super().init_sidemenu_instruments()
        self.side_menu_controller.add_instrument("Colored Tetrahedron", lambda: ColoredTetrahedron(Point(50,50,50), 100))
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
        #self.side_menu_controller.add_instrument("Colored Cube", lambda: ColoredCube(Point(50,50,50), 100, colors))

    def add_leftmost_buttons(self):
        super().add_leftmost_buttons()
        self.add_button("Show/Hide axis", command=self.toggle_show_axis)
        self.add_button("Toggle z-buffer renderer", command=self.toggle_z_buffer_renderer)
        self.add_button("Move Camera", lambda: self.controller.switch_mode("move_camera"))
        
    def toggle_show_axis(self):
        self.renderer.show_axis = not self.renderer.show_axis
        self.renderer.render_scene(self.scene)

    def toggle_z_buffer_renderer(self):
        self.renderer.use_z_buffer = not self.renderer.use_z_buffer
        self.renderer.render_scene(self.scene)

    def create_renderer(self):
        self.renderer = PolyRenderer(self.canv, False)
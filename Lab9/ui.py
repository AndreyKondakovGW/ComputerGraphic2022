from Lab8.ui import UI8
from src.point import Point
from Lab8.colored_tetrahedron import ColoredTetrahedron
#from Lab8.colored_cube import ColoredCube
from Lab8.poly_renderer import PolyRenderer

class UI9(UI8):
    def __init__(self):
        super().__init__()

    def add_leftmost_buttons(self):
        super().add_leftmost_buttons()
        self.add_button("Toggle texture mode", command=self.toggle_texture_mode)
        self.add_button("Apply texture", command=self.apply_texture)

    def toggle_texture_mode(self):
        self.renderer.use_texture = not self.renderer.use_texture
        self.renderer.render_scene(self.scene)

    def apply_texture(self):
        for fig in self.scene.storage:
            if fig.selected:
                fig.set_texture(1)
        self.renderer.render_scene(self.scene)

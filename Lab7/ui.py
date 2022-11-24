from Lab6.ui3D import UI3D
from Lab7.obj_parser import ObjParser
from Lab7.function_plotter import plot


class UI7(UI3D):
    def __init__(self):
        self.loader = ObjParser()
        super().__init__()

    def add_leftmost_buttons(self):
        super().add_leftmost_buttons()
        self.add_button("Save", lambda: self.loader.save_figure("Lab7/models/saved.obj", self.scene.storage))

    def init_sidemenu_instruments(self):
        super().init_sidemenu_instruments()
        self.side_menu_controller.add_instrument("Load Figure", lambda: self.loader.open_file())
        self.side_menu_controller.add_instrument("Plot", lambda: plot(self, 20))

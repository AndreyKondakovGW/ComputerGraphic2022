from src.UI import UI_base
from Lab6.side_menu import SideMenu
from Lab6.sidemenu_controller import SideMenu_Controller

from src.point import Point
from Lab6.line3D import Line3D
from Lab6.selector3D import RectSelector3DMode
from Lab6.scaler3D import ScalerMode3D
from Lab6.mover3D import MoverMode3D
from Lab6.rotator3D import RotatorMode3D
from Lab6.mirror import MirrorMode3D

class UI3D(UI_base):
    def __init__(self):
        super().__init__()
        self.add_button(">", lambda: self.side_menue_layout.grid_remove())
        self.add_button("<", lambda: self.side_menue_layout.grid())
        self.add_button("Select", lambda: self.controller.switch_mode("selectrectangle"))
        self.add_button("Move", lambda: self.controller.switch_mode("move"))
        self.add_button("Scale", lambda: self.controller.switch_mode("scale"))
        self.add_button("Rotate", lambda: self.controller.switch_mode("rotate"))
        self.add_button("Mirror", lambda: self.controller.switch_mode("mirror"))


        self.add_button("Clear", self.del_figures)

        self.create_canvas()
        self.create_renderer()
        self.controller.add_mode("selectrectangle", RectSelector3DMode(self.renderer, self.scene))
        self.controller.add_mode("move", MoverMode3D(self.renderer, self.scene))
        self.controller.add_mode("scale", ScalerMode3D(self.renderer, self.scene))
        self.controller.add_mode("rotate", RotatorMode3D(self.renderer, self.scene))
        self.controller.add_mode("mirror", MirrorMode3D(self.renderer, self.scene))
        self.side_menue_controller = SideMenu_Controller(self.renderer, self.scene)
        self.side_menue_layout = SideMenu(self.side_menue_controller)
        self.side_menue_layout.grid(row=1, column=0)

        
        self.bind("<x>", self.controller.hanble_x)
        self.bind("<y>", self.controller.hanble_y)
        self.bind("<z>", self.controller.hanble_z)

        self.bind("<,>", self.controller.hanble_left)
        self.bind("<.>", self.controller.hanble_right)

    def del_figures(self):
        self.scene.clear()
        self.add_axes()

    def add_axes(self):
        self.scene.add_figure(Line3D([Point(500,0,0), Point(-500,0,0)], (255,0,0)))
        self.scene.add_figure(Line3D([Point(0,-500,0), Point(0,500,0)], (0,255,0)))
        self.scene.add_figure(Line3D([Point(0,0,500), Point(0,0,-500)], (0,0,255)))
        self.renderer.render_scene(self.scene)
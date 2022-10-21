from src.UI import UI_base
from Lab6.side_menu import SideMenu
from Lab6.sidemenu_controller import SideMenu_Controller

from src.point import Point
from Lab6.line3D import Line3D
from Lab6.selector3D import RectSelector3DMode

class UI3D(UI_base):
    def __init__(self):
        super().__init__()
        self.add_button(">", lambda: self.side_menue_layout.grid_remove())
        self.add_button("<", lambda: self.side_menue_layout.grid())
        self.add_button("Select", lambda: self.controller.switch_mode("selectrectangle"))


        self.add_button("Clear", self.del_figures)

        self.create_canvas()
        self.create_renderer()
        self.controller.add_mode("selectrectangle", RectSelector3DMode(self.renderer, self.scene))
        
        self.side_menue_controller = SideMenu_Controller(self.renderer, self.scene)
        self.side_menue_layout = SideMenu(self.side_menue_controller)
        self.side_menue_layout.grid(row=1, column=0)

    def del_figures(self):
        self.scene.clear()
        self.add_axes()

    def add_axes(self):
        self.scene.add_figure(Line3D([Point(300,0,0), Point(-200,0,0)], (255,0,0)))
        self.scene.add_figure(Line3D([Point(0,-300,0), Point(0,300,0)], (0,255,0)))
        self.scene.add_figure(Line3D([Point(0,0,300), Point(0,0,-300)], (0,0,255)))
        self.renderer.render_scene(self.scene)
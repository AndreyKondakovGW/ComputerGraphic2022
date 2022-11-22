from src.UI import UI_base
from Lab6.side_menu import SideMenu
from Lab6.sidemenu_controller import SideMenu_Controller

from Lab6.selector3D import RectSelector3DMode
from Lab6.scaler3D import ScalerMode3D
from Lab6.mover3D import MoverMode3D
from Lab6.rotator3D import RotatorMode3D
from Lab6.mirror import MirrorMode3D
from Lab6.mouseRotator import MouseRotatorMode3D

from src.point import Point
from Lab6.point3D import Point3D
from Lab6.figures.line3D import Line3D
from Lab6.figures.cube import Cube
from Lab6.figures.tetrahedron import Tetrahedron
from Lab6.figures.octahedron import Octahedron
from Lab6.figures.icosahedron import Icosahedron
from Lab6.figures.dodecahedron import Dodecahedron
from Lab6.projections import *

class UI3D(UI_base):
    def __init__(self):
        super().__init__()
        self.add_buttons()
        self.create_canvas()
        self.create_renderer()
        self.init_controller()
        self.init_sidemenu()
        self.init_bindings()

    def run(self):
        self.renderer.render_scene(self.scene)
        super().run()
        

    def add_buttons(self):
        self.add_leftmost_buttons()
        self.add_rightmost_buttons()
        
    # you can modify this in ancestors to add a button before all buttons, 
    #                                                  or after all buttons, but before rightmost buttons    
    def add_leftmost_buttons(self):
        self.add_button(">", lambda: self.side_menu_layout.grid_remove())
        self.add_button("<", lambda: self.side_menu_layout.grid())
        self.add_button("Select", lambda: self.controller.switch_mode("selectrectangle"))
        self.add_button("Move", lambda: self.controller.switch_mode("move"))
        self.add_button("Scale", lambda: self.controller.switch_mode("scale"))
        self.add_button("Rotate", lambda: self.controller.switch_mode("rotate"))
        self.add_button("Mirror", lambda: self.controller.switch_mode("mirror"))

    def add_rightmost_buttons(self):
        self.add_button("Clear", self.del_figures) 

    def init_controller(self):
        self.controller.add_mode("selectrectangle", RectSelector3DMode(self.renderer, self.scene))
        self.controller.add_mode("move", MoverMode3D(self.renderer, self.scene))
        self.controller.add_mode("scale", ScalerMode3D(self.renderer, self.scene))
        self.controller.add_mode("rotate", MouseRotatorMode3D(self.renderer, self.scene))
        self.controller.add_mode("mirror", MirrorMode3D(self.renderer, self.scene))

    def init_sidemenu(self):
        self.side_menu_controller = SideMenu_Controller(self.renderer, self.scene, "2D", "Point")
        self.init_sidemenu_modes()
        self.init_sidemenu_instruments()
        self.side_menu_layout = SideMenu(self.side_menu_controller)
        self.side_menu_layout.grid(row=1, column=0)

    def init_sidemenu_modes(self):
        self.side_menu_controller.add_mode("2D", simple2D_projection())
        self.side_menu_controller.add_mode("3D perspective", perspective_projection())
        self.side_menu_controller.add_mode("3D aksonometric", akso_projection())
        self.side_menu_controller.add_mode("Camera", None)

    def init_sidemenu_instruments(self):
        self.side_menu_controller.add_instrument("Point", lambda: Point3D(Point(0, 50, 0), (255, 0, 0)))
        self.side_menu_controller.add_instrument("Line", lambda: Line3D(Point(100, 0, 0), Point(0, 0, 0)))
        self.side_menu_controller.add_instrument("Cube", lambda: Cube(Point(50,50,50), 100))
        self.side_menu_controller.add_instrument("Tetrahedron", lambda: Tetrahedron(Point(50,50,50), 100))
        self.side_menu_controller.add_instrument("Octahedron", lambda: Octahedron(Point(50,50,50), 100))
        self.side_menu_controller.add_instrument("Icosahedron", lambda: Icosahedron(Point(50,50,50), 100))
        self.side_menu_controller.add_instrument("Dodecahedron", lambda: Dodecahedron(Point(50,50,50), 100))

    def init_bindings(self):
        self.bind("<x>", self.controller.hanble_x)
        self.bind("<y>", self.controller.hanble_y)
        self.bind("<z>", self.controller.hanble_z)
        
        self.bind("<w>", self.controller.hanble_w)
        self.bind("<a>", self.controller.hanble_a)
        self.bind("<s>", self.controller.hanble_s)
        self.bind("<d>", self.controller.hanble_d)
        self.bind("<q>", self.controller.hanble_q)
        self.bind("<e>", self.controller.hanble_e)

        self.bind("<Left>", self.controller.hanble_left)
        self.bind("<Right>", self.controller.hanble_right)

    def del_figures(self):
        self.scene.clear()
        self.renderer.render_scene(self.scene)

    def create_camera(self, pos, target):
        super().create_camera(pos, target)
        self.side_menu_controller.camera = self.camera
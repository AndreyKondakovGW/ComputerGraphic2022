from tkinter import filedialog
from src.controller_mode import ControllerMode
from drawer import Drawer
from l_system_factory import LSystemFactory

class LSystemMode(ControllerMode):
    def __init__(self, canvas):
        self.canvas = canvas
        self.l_system = None
        self.file = None
        self.generation = 0
        self.drawer = Drawer(self.canvas)
        self.l_system_factory = LSystemFactory(self.drawer, self.canvas.width, self.canvas.height)

    def open_file(self):
        filename = filedialog.askopenfilename(initialdir="~/computer_graphics/ComputerGraphic2022/Lab5/LSystems_source/")
        if filename is None:
            return
        self.l_system = self.l_system_factory.build(filename)

    def set_generation(self, generation):
        self.generation = generation

    def draw(self):
        if self.l_system is None:
            return
        self.canvas.clear() 
        self.l_system.update_drawer()      
        self.drawer.set_step_size(100)
        generation = int(self.generation)
        self.l_system.draw(generation)
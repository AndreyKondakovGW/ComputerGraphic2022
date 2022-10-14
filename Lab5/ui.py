from tkinter import PhotoImage, Tk, Button, Frame, Entry, filedialog
from drawer import Drawer
from l_system_factory import LSystemFactory
from canvas import MyCanvas

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
lab4dir = os.path.join(parentdir, "Lab4")
sys.path.insert(0, lab4dir) 

from primitives import line_bresenchem

class UI(Tk):
    def __init__(self):
        super().__init__()
        self.canvas_width = 600
        self.canvas_height = 600
        self.init_ui()
        self.drawer = Drawer(self.canvas)
        self.l_system_factory = LSystemFactory(self.drawer, self.canvas_width, self.canvas_height)

    def init_ui(self):
        self.init_buttons_layout()
        self.init_controls()
        self.init_canvas()

    def init_buttons_layout(self):
        self.buttons_layout = Frame(self)
        self.buttons_layout.grid(row=0, column=0)

    def init_controls(self):
        self.open_file_button = Button(self.buttons_layout, text="Open file", command=self.open_file)
        self.open_file_button.grid(row=0, column=0)
        self.generation_input = Entry(self.buttons_layout, text="Generation")
        self.generation_input.grid(row=0, column=1)
        self.draw_button = Button(self.buttons_layout, text="Draw", command=self.draw)
        self.draw_button.grid(row=0, column=2)

    def init_canvas(self):
        self.canvas = MyCanvas(self, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.grid(row=1, column=0)
        #self.create_image()

    def create_image(self, state="normal"):
        self.image = PhotoImage(width=self.canvas_width, height=self.canvas_height)
        self.canvas.create_image((self.canvas_width / 2, self.canvas_height / 2), image=self.image, state=state)

    def open_file(self):
        filename = filedialog.askopenfilename(initialdir="~/computer_graphics/ComputerGraphic2022/Lab5")
        if filename is None:
            return
        self.l_system = self.l_system_factory.build(filename)

    def draw(self):
        self.canvas.clear()
        # self.drawer.set_direction(self.l_system.starting_direction)
        # self.drawer.set_starting_point(self.l_system.starting_point)  
        self.l_system.update_drawer()      
        self.drawer.set_step_size(10)
        #self.drawer.set_starting_point(50, 300)
        generation = int(self.generation_input.get())
        self.l_system.draw(generation)
from tkinter import PhotoImage, Tk, Button, Scale, Entry,StringVar, Frame

from .canvas import MyCanvas
from .controller import UI_controller
import os
from .renderer import Renderer
from .scene import Scene
from .storage_canvas import StorageCanvas


class UI_base(Tk):
    def __init__(self, titel="Painter", width=0, height=0):
        super().__init__()
        self.variables = []
        if width == 0:
            self.win_width = self.winfo_screenwidth()
        else:
            self.win_width = width
        if height == 0:
            self.win_height = self.winfo_screenheight()
        else:
            self.win_height = height

        self.icons_folder = os.path.join(os.getcwd(), 'static', 'icons')

        photo = PhotoImage(file = os.path.join(self.icons_folder, "rat.png"))
        self.wm_iconphoto(False, photo)
        self.title(titel)

        self.button_num = 0
        self.buttons_layout = Frame(self)
        self.buttons_layout.grid(row=0, column=2)
        self.controller = UI_controller()
        self.buttons = {}

        self.bind('<Motion>', self.controller.hanble_moution)
        self.bind('<ButtonPress-1>', self.controller.hanble_press)
        self.bind('<ButtonRelease-1>', self.controller.hanble_release)
        self.bind("<ButtonPress-3>", self.controller.hanble_right_press)
        self.bind("<MouseWheel>", self.controller.hanble_mouse_wheel)

        self.scene = Scene()
    
    def create_canvas(self, use_storage=False):
        if use_storage:
            self.canv = StorageCanvas(self, width=self.win_width, height=self.win_height, bg="white")
        else:
            self.canv = MyCanvas(self, width=self.win_width, height=self.win_height, bg="white")
        self.canv.grid(row=1, column=2)
        self.controller.set_canvas(self.canv)

    def create_renderer(self):
        self.renderer = Renderer(self.canv)

    def add_button(self, text, command, icon_name=None):
        if icon_name is None:
            button = Button(self.buttons_layout, text=text, command=command)
            button.grid(row=1, column=self.button_num)
        else:
            icon_path = os.path.join(self.icons_folder, icon_name)
            icon = PhotoImage(file=icon_path)
            icon = icon.subsample(10, 10)
            button = Button(self.buttons_layout, width=50,height=50, text=text, command=command, image =icon)
            button.image = icon
            button.grid(row=1, column=self.button_num)
        self.button_num += 1
        self.buttons[text] = button

    def add_slider(self, min_val, max_val, curent_value, command):
        slider = Scale(self.buttons_layout, from_=min_val,to=max_val, orient='horizontal', command=command)
        slider.grid(row=1, column=self.button_num)
        self.button_num += 1

    def add_entry(self, text, command, start_text=""):
        sv = StringVar()
        self.variables.append(sv)
        sv.trace("w", lambda name, index, mode, sv=sv: command(sv.get()))
        e = Entry(self.buttons_layout, text=text, textvariable=sv)
        e.insert(0, start_text)
        e.grid(row=1, column=self.button_num)
        self.button_num += 1

    def add_side_menue(self):
        pass
    def run(self):
        self.mainloop()
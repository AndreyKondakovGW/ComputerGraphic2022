from tkinter import PhotoImage, Tk, Button, Scale
from .canvas import MyCanvas
from .controller import UI_controller
import os

class UI_base(Tk):
    def __init__(self, titel="Painter", width=0, height=0):
        super().__init__()
        if width == 0:
            self.win_width = self.winfo_screenwidth() // 2
        else:
            self.win_width = width
        if height == 0:
            self.win_height = self.winfo_screenheight() // 2
        else:
            self.win_height = height

        self.icons_folder = os.path.join(os.getcwd(), 'static', 'icons')

        photo = PhotoImage(file = os.path.join(self.icons_folder, "rat.png"))
        self.wm_iconphoto(False, photo)
        self.title(titel)
        self.button_num = 0
        self.controller = UI_controller()
        

        self.bind('<Motion>', self.controller.hanble_moution)
        self.bind('<ButtonPress-1>', self.controller.hanble_press)
        self.bind('<ButtonRelease-1>', self.controller.hanble_release)
        self.bind("<ButtonPress-3>", self.controller.hanble_right_press)
        self.bind("<MouseWheel>", self.controller.hanble_mouse_wheel)


    
    def create_canvas(self):
        self.canv = MyCanvas(self, width=self.win_width, height=self.win_height, bg="white")
        self.canv.grid(row=2, columnspan=self.button_num)
        self.controller.set_canvas(self.canv)

    def add_button(self, text, command, icon_name=None):
        if icon_name is None:
            Button(self, text=text, command=command).grid(row=1, column=self.button_num)
        else:
            icon_path = os.path.join(self.icons_folder, icon_name)
            icon = PhotoImage(file=icon_path)
            icon = icon.subsample(10, 10)
            button = Button(self, width=50,height=50, text=text, command=command, image =icon)
            button.image = icon
            button.grid(row=1, column=self.button_num)
        self.button_num += 1

    def add_slider(self, min_val, max_val, curent_value, command):
        slider = Scale(self, from_=min_val,to=max_val, orient='horizontal', command=command)
        slider.grid(row=1, column=self.button_num)
        self.button_num += 1

    def run(self):
        self.mainloop()
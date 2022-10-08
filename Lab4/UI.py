from tkinter import PhotoImage, Tk, Button
from canvas import MyCanvas
from painter import Painter
import os

class MyUI(Tk):
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

        self.icons_folder = os.path.join(os.getcwd(), 'Lab4', 'icons')

        photo = PhotoImage(file = os.path.join(self.icons_folder, "rat.png"))
        self.wm_iconphoto(False, photo)
        self.title(titel)
        self.button_num = 0
        
        
        self.painter = Painter()
        self.create_buttons(self.painter.switch_mode)
        self.create_canvas()
        self.painter.set_canvas(self.canv)

        self.bind('<Motion>', self.painter.hanble_moution)
        self.bind('<ButtonPress-1>', self.painter.hanble_press)
        self.bind('<ButtonRelease-1>', self.painter.hanble_release)

        self.mainloop()

    def create_buttons(self, button_press_f):
        self.add_button("Dot", lambda: button_press_f("dot"), os.path.join(self.icons_folder, 'dot-circle.png'))
        self.add_button("Draw Line", lambda: button_press_f("drawline"), os.path.join(self.icons_folder, 'line-segment.png'))
        self.add_button("Draw Line Wu", lambda: button_press_f("drawlinewu"), os.path.join(self.icons_folder, 'line-segment.png'))
        self.add_button("Draw Poligon", lambda: button_press_f("drawpoligon"), os.path.join(self.icons_folder, 'poligon.png'))
        self.add_button("Draw Rect", lambda: button_press_f("drawrectangle"), os.path.join(self.icons_folder, 'rect.png'))

        self.add_button("Select", lambda: button_press_f("selectrectangle"), os.path.join(self.icons_folder, 'shape.png'))
        self.add_button("Translation", lambda: button_press_f("affine_translation"), os.path.join(self.icons_folder, 'move.png'))
        self.add_button("Rotation", lambda: button_press_f("affine_rotation"), os.path.join(self.icons_folder, 'refresh.png'))
        self.add_button("Scaling", lambda: button_press_f("affine_scaling"), os.path.join(self.icons_folder, 'move.png'))

        self.add_button("Mark Segments", lambda: button_press_f("marksegments"), os.path.join(self.icons_folder, 'blue_line.png'))
        self.add_button("Check Convex", lambda: button_press_f("checkconvex"), os.path.join(self.icons_folder, 'iran.png'))
        self.add_button("Check Polygon", lambda: button_press_f("checkpolygon"),os.path.join(self.icons_folder, 'cursor.png') )

        self.add_button("Delete", lambda: button_press_f("delselected"), os.path.join(self.icons_folder, 'eraser.png'))
        self.add_button("Clear", lambda: button_press_f("clear"), os.path.join(self.icons_folder, 'bin.png'))
        return
    
    def create_canvas(self):
        self.canv = MyCanvas(self, width=self.win_width, height=self.win_height, bg="white")
        self.canv.grid(row=2, columnspan=self.button_num)

    def add_button(self, text, command, icon_name=None):
        if icon_name is None:
            Button(self, text=text, command=command).grid(row=1, column=self.button_num)
        else:
            icon = PhotoImage(file=icon_name)
            icon = icon.subsample(10, 10)
            button = Button(self, width=50,height=50, text=text, command=command, image =icon)
            button.image = icon
            button.grid(row=1, column=self.button_num)
        self.button_num += 1
        return
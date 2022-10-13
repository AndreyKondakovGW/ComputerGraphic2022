from tkinter import PhotoImage, Tk, Button
from canvas import MyCanvas
from Painter import Painter


class MyUI(Tk):
    def __init__(self, title="Bezier curve", width=0, height=0):
        super().__init__()
        if width == 0:
            self.win_width = self.winfo_screenwidth() // 2
        else:
            self.win_width = width
        if height == 0:
            self.win_height = self.winfo_screenheight() // 2
        else:
            self.win_height = height

        self.title(title)
        self.button_num = 0

        self.painter = Painter()
        self.create_buttons(self.painter.switch_mode)
        self.create_canvas()
        self.painter.set_canvas(self.canv)

        self.bind('<Motion>', self.painter.handle_motion)
        self.bind('<ButtonPress-1>', self.painter.handle_press)
        self.bind('<ButtonRelease-1>', self.painter.handle_release)

        self.mainloop()

    def create_buttons(self, button_press_f):
        self.add_button("Add point", lambda: button_press_f("add"))
        self.add_button("Move point", lambda: button_press_f("move"))
        self.add_button("Delete point", lambda: button_press_f("delete"))
        self.add_button("Clear", lambda: button_press_f("clear"))
        return

    def create_canvas(self):
        self.canv = MyCanvas(self, width=self.win_width, height=self.win_height, bg="white")
        self.canv.grid(row=2, columnspan=self.button_num)

    def add_button(self, text, command, icon_name=None):
        Button(self, text=text, command=command).grid(row=1, column=self.button_num)
        self.button_num += 1

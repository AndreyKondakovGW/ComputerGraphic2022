from tkinter import Tk, Button
from canvas import MyCanvas
from painter import Painter

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
        self.add_button("Dot", lambda: button_press_f("dot"))
        self.add_button("Paint", lambda: button_press_f("paint"))
        self.add_button("Draw Line", lambda: button_press_f("drawline"))
        self.add_button("Draw Line Wu", lambda: button_press_f("drawlinewu"))
        self.add_button("Draw Poligon", lambda: button_press_f("drawpoligon"))
        self.add_button("Draw Rect", lambda: button_press_f("drawrectangle"))
        self.add_button("Mark Segments", lambda: button_press_f("marksegments"))
        self.add_button("Check Convex", lambda: button_press_f("checkconvex"))
        self.add_button("Select", lambda: button_press_f("selectrectangle"))
        self.add_button("Delete", lambda: button_press_f("delselected"))
        self.add_button("Clear", lambda: button_press_f("clear"))
        return
    
    def create_canvas(self):
        self.canv = MyCanvas(self, width=self.win_width, height=self.win_height, bg="white")
        self.canv.grid(row=2, columnspan=self.button_num)

    def add_button(self, text, command):
        button1=Button(self, text=text, command=command)
        button1.grid(row=1,column=self.button_num)
        self.button_num += 1
        return
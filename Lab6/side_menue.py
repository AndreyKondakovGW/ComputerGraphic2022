
from tkinter import  Button, Entry,StringVar, Frame
from tkinter.ttk import Combobox, Label 

class SideMenue(Frame):
    def __init__(self):
        super().__init__()
        self.points = []
        self.points_adds = []
        self.mode = "2D"
        self.mode_lable = Label(self, text="Режим")  
        self.mode_lable.grid(column=0, row=0)  
        self.mode_widget = Combobox(self)  
        self.mode_widget['values'] = ("2D", "3D")  
        self.mode_widget.current(0)
        self.mode_widget.bind('<<ComboboxSelected>>', self.mode_update)
        self.mode_widget.grid(column=0, row=1)
        self.fig_lable = Label(self, text="Фигура")  
        self.fig_lable.grid(column=0, row=2)
        self.figure_mode = Combobox(self)
        self.figure_mode['values'] = ("Точка", "Линия", "Грань")
        self.figure_mode.bind('<<ComboboxSelected>>', self.figure_update)
        self.figure_mode.grid(column=0, row=3)
        self.draw_button= Button(self, text="Нарисовать")
        self.draw_button.grid(column=0, row=4)
        self.num_rows = 5

    def mode_update(self, _):
        self.mode = self.mode_widget.get()
        self.clear_adders()


    def figure_update(self, _):
        self.clear_adders()
        if self.figure_mode.get() == "Точка":
            self.add_point_adder()
        elif self.figure_mode.get() == "Линия":
            self.add_point_adder()
            self.add_point_adder()
        elif self.figure_mode.get() == "Грань":
            add_button = Button(self, text="Добавить", command=self.add_point_adder)
            add_button.grid(column=0, row=self.num_rows)
            self.num_rows += 1
            self.add_point_adder()
            

    def add_point_adder(self):
        point_adder = Frame(self)
        point_adder.grid(column=0, row=self.num_rows)
        if self.mode == "2D":
            Label(point_adder, text="X,Y").grid(column=0, row=1)
            entry = Entry(point_adder)
            entry.grid(column=0, row=0)
            entry.insert(0, "0,0") 

        else:
            self.fig_lable = Label(point_adder, text="X,Y,Z").grid(column=0, row=1)
            entry = Entry(point_adder)
            entry.grid(column=0, row=0)
            entry.insert(0, "0,0,0")

            

        self.num_rows += 2
        self.points_adds.append(point_adder) 

    def clear_adders(self):
        self.num_rows = self.num_rows - len(self.points_adds)
        for add in self.points_adds:
            add.destroy()
        self.points_adds = []
        self.points = []
        


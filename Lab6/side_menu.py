
from tkinter import  Button, Frame
from tkinter.ttk import Combobox, Label 

class SideMenu(Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.add_mode_list()
        self.add_figure_list()

    def add_mode_list(self):
        self.mode_lable = Label(self, text="Режим")  
        self.mode_lable.grid(column=0, row=0)  
        self.mode_widget = Combobox(self)  
        self.mode_widget['values'] = list(self.controller.mode_projection.keys())
        self.mode_widget.current(0)
        self.mode_widget.bind('<<ComboboxSelected>>', self.controller.mode_update)
        self.mode_widget.grid(column=0, row=1)

    def add_figure_list(self):
        self.fig_lable = Label(self, text="Фигура")  
        self.fig_lable.grid(column=0, row=2)
        self.figure_mode = Combobox(self)
        self.figure_mode['values'] = self.controller.figures_names
        self.figure_mode.bind('<<ComboboxSelected>>', self.controller.figure_update)
        self.figure_mode.grid(column=0, row=3)
        self.draw_button= Button(self, text="Нарисовать", command=self.controller.draw_figure)
        self.draw_button.grid(column=0, row=4)

        


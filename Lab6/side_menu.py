
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
        self.mode_widget = Combobox(self, state="readonly")  
        self.mode_widget['values'] = list(self.controller.modes.keys())
        self.mode_widget.current(0)
        self.mode_widget.bind('<<ComboboxSelected>>', self.mode_selected)
        self.mode_widget.grid(column=0, row=1)

    def mode_selected(self, event):
        mode_name = event.widget.get()
        self.controller.set_mode(mode_name)

    def figure_selected(self, event):
        figure_name = event.widget.get()
        self.controller.set_instrument(figure_name)

    def add_figure_list(self):
        self.fig_lable = Label(self, text="Фигура")  
        self.fig_lable.grid(column=0, row=2)
        self.figure_mode = Combobox(self, state="readonly")
        self.figure_mode['values'] = list(self.controller.instruments.keys())
        self.figure_mode.bind('<<ComboboxSelected>>', self.figure_selected)
        self.figure_mode.grid(column=0, row=3)
        self.draw_button= Button(self, text="Нарисовать", command=self.controller.draw_figure)
        self.draw_button.grid(column=0, row=4)

        


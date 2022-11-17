from tkinter import Button, Frame, Entry, Checkbutton
from tkinter.ttk import Combobox, Label
import re

from Lab6.point3D import Point3D
from src.point import Point


class SideMenu(Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.add_mode_list()
        self.add_figure_list()
        self.add_rotation_figure_ui()

    def add_mode_list(self):
        self.mode_lable = Label(self, text="Режим")
        self.mode_lable.grid(column=0, row=0)
        self.mode_widget = Combobox(self, state="readonly")
        self.mode_widget['values'] = list(self.controller.mode_projection.keys())
        self.mode_widget.current(0)
        self.mode_widget.bind('<<ComboboxSelected>>', self.controller.mode_update)
        self.mode_widget.grid(column=0, row=1)

    def add_figure_list(self):
        self.fig_lable = Label(self, text="Фигура")
        self.fig_lable.grid(column=0, row=2)
        self.figure_mode = Combobox(self, state="readonly")
        self.figure_mode['values'] = self.controller.figures_names
        self.figure_mode.bind('<<ComboboxSelected>>', self.controller.figure_update)
        self.figure_mode.grid(column=0, row=3)
        self.draw_button = Button(self, text="Нарисовать", command=self.controller.draw_figure)
        self.draw_button.grid(column=0, row=4)

    def add_rotation_figure_ui(self):
        self.rot_fig_lable = Label(self, text='Фигура вращения')
        self.rot_fig_lable.grid(column=0, row=10)

        self.rot_axis = Combobox(self, state="readonly")
        self.rot_axis['values'] = self.controller.axes
        self.rot_axis.bind('<<ComboboxSelected>>', self.controller.axis_update)
        self.rot_axis.grid(column=0, row=11)

        self.partition_label = Label(self, text='Количество разбиений')
        self.partition_label.grid(column=0, row=12)

        self.partition_text = Entry(self)
        self.partition_text.grid(column=0, row=13)

        self.point_label = Label(self, text='Точка образующей')
        self.point_label.grid(column=0, row=14)

        self.forming_point_text = Entry(self)
        self.forming_point_text.grid(column=0, row=15)

        self.draw_rot_fig_button = Button(self, text="Перерисовать", command=lambda: input_handler())
        self.draw_rot_fig_button.grid(column=0, row= 16)

        self.delete_faces_checkbox = Checkbutton(self, text='Отсечь нелицевые грани', variable=self.controller.delete_faces_box)
        self.delete_faces_checkbox.grid(column=0, row= 18)


        def input_handler():
            partition = int(self.partition_text.get())
            if partition > 0:
                self.controller.partition = partition
            fp = self.forming_point_text.get()
            fp = re.match(r'(\-?\d{1,3}),(\-?\d{1,3}),(\-?\d{1,3})', fp)
            if fp:
                self.controller.forming_point = Point(int(fp[1]), int(fp[2]), int(fp[3]))
                self.controller.change_rotation_figure()

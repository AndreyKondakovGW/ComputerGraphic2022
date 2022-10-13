from tkinter import Button, Toplevel, Label, Entry

from .functions import intersection_with_scope
from .transformation import translation, rotation, scaling
from src.controller_mode import ControllerMode

def af_translation(canv):
    a = Toplevel()
    a.geometry('200x100')
    a.title('Параметры смещения')
    Label(a, text="коэффициент по x").grid(column=1, row=1)
    entry_x = Entry(a)
    entry_x.insert(0,'0')
    entry_x.grid(column=2, row=1)
    Label(a, text="коэффициент по y").grid(column=1, row=10)
    entry_y = Entry(a)
    entry_y.insert(0,'0')
    entry_y.grid(column=2, row=10)
    Button(a, height=1, width=10, text="перенести",
           command=lambda: input_handler()).grid(column=1, row=20)

    def input_handler():
        k_x = float(entry_x.get())
        k_y = float(entry_y.get())

        fig = canv.content
        for f in fig:
            old_points = f.points
            if f.selected:
                translation(f, k_x, k_y)
            if intersection_with_scope(f, canv):
                f.points = old_points
        canv.redraw_content()


def af_rotation(canv):
    a = Toplevel()
    a.geometry('200x100')
    a.title('Параметры поворота')
    Label(a, text="угол в градусах").grid(column=1, row=1)
    e_angle = Entry(a)
    e_angle.insert(0,'0')
    e_angle.grid(column=2, row=1)
    Button(a, height=1, width=10, text="повернуть",
           command=lambda: input_handler()).grid(column=1, row=20)

    def input_handler():
        angle = float(e_angle.get())
        fig = canv.content
        for f in fig:
            old_points = f.points
            point = (-1, -1)
            if canv.af_point is not None:
                point = canv.af_point
            if f.selected:
                rotation(f, angle, point)
            if intersection_with_scope(f, canv):
                f.points = old_points
        canv.redraw_content()


def af_scaling(canv):
    a = Toplevel()
    a.geometry('200x100')
    a.title('Параметры масштабирования')
    Label(a, text="коэффициент по x").grid(column=1, row=1)
    entry_x = Entry(a)
    entry_x.insert(0,'1')
    entry_x.grid(column=2, row=1)
    Label(a, text="коэффициент по y").grid(column=1, row=10)
    entry_y = Entry(a)
    entry_y.insert(0,'1')
    entry_y.grid(column=2, row=10)
    Button(a, height=1, width=10, text="масштабировать",
           command=lambda: input_handler()).grid(column=1, row=20)

    def input_handler():
        kx = float(entry_x.get())
        ky = float(entry_y.get())
        fig = canv.content
        point = (-1, -1)
        if canv.af_point is not None:
            point = canv.af_point
        for f in fig:
            old_points = f.points
            if f.selected:
                scaling(f, kx, ky, point)
            if intersection_with_scope(f, canv):
                f.points = old_points
        canv.redraw_content()


class AffinePointMode(ControllerMode):
    def __init__(self, canv):
        self.canv = canv
        self.af_point = None

    def hanble_press(self, event):
        self.canv.af_point = (event.x, event.y)
        self.canv.draw_circle(event.x, event.y, r=2)

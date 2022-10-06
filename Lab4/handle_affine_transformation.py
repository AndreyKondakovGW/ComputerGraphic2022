from tkinter import Button, Toplevel, Label, Entry

from Lab4.functions import intersection_with_scope
from transformation import translation, rotation, scaling



def af_translation(canv):
    a = Toplevel()
    a.geometry('200x100')
    a.title('Параметры смещения')
    Label(a, text="коэффициент по x").grid(column=1, row=1)
    entry_x = Entry(a)
    entry_x.grid(column=2, row=1)
    Label(a, text="коэффициент по y").grid(column=1, row=10)
    entry_y = Entry(a)
    entry_y.grid(column=2, row=10)
    Button(a, height=1, width=10, text="перенести",
           command=lambda: input_handler()).grid(column=1, row=20)

    def input_handler():
        k_x = int(entry_x.get())
        k_y = int(entry_y.get())
        fig = canv.content
        for f in fig:
            old_points = f.points
            if f.selected:
                translation(f, k_x, k_y)
            if intersection_with_scope(f,canv):
                f.points = old_points
        canv.redraw_content()


def af_rotation(canv):
    a = Toplevel()
    a.geometry('200x100')
    a.title('Параметры поворота')
    Label(a, text="угол в градусах").grid(column=1, row=1)
    e_angle = Entry(a)
    e_angle.grid(column=2, row=1)
    Button(a, height=1, width=10, text="повернуть",
           command=lambda: input_handler()).grid(column=1, row=20)

    def input_handler():
        angle = int(e_angle.get())
        fig = canv.content
        for f in fig:
            old_points = f.points
            if f.selected:
                rotation(f, angle)
            if intersection_with_scope(f,canv):
                f.points = old_points
        canv.redraw_content()


def af_scaling(canv):
    a = Toplevel()
    a.geometry('200x100')
    a.title('Параметры масштабирования')
    Label(a, text="коэффициент по x").grid(column=1, row=1)
    entry_x = Entry(a)
    entry_x.grid(column=2, row=1)
    Label(a, text="коэффициент по y").grid(column=1, row=10)
    entry_y = Entry(a)
    entry_y.grid(column=2, row=10)
    Button(a, height=1, width=10, text="масштабировать",
           command=lambda: input_handler()).grid(column=1, row=20)

    def input_handler():
        kx = int(entry_x.get())
        ky = int(entry_y.get())
        fig = canv.content
        for f in fig:
            old_points = f.points
            if f.selected:
                scaling(f, kx, ky)
            if intersection_with_scope(f,canv):
                f.points = old_points
        canv.redraw_content()


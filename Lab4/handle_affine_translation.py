from tkinter import Text, Button, ttk, Toplevel, Label, Entry
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
            translation(f, k_x, k_y)
        canv.redraw_content()


def af_rotation(canv):
    a = Toplevel()
    a.geometry('200x100')
    a.title('Параметры поворота')
    Label(a, text="угол").grid(column=1, row=1)
    entry_angle = Entry(a)
    entry_angle.grid(column=2, row=1)
    Button(a, height=1, width=10, text="повернуть",
           command=lambda: input_handler()).grid(column=1, row=20)

    def input_handler():
        angle = int(entry_angle.get())
        fig = canv.content
        for f in fig:
            rotation(f, angle)
        canv.redraw_content()

from tkinter import Text, Button, ttk, Toplevel, Label, Entry
from transformation import translation


def af_translation(canv):
    k_x = ''
    k_y = ''

    a = Toplevel()
    a.geometry('200x200')
    a.title('Параметры смещения')
    Label(a, text="коэффициент по x").grid(column=1, row=1)
    entry_x = Entry(a)
    entry_x.grid(column=2, row=1)
    Label(a, text="коэффициент по y").grid(column=1, row=10)
    entry_y = Entry(a)
    entry_y.grid(column=2, row=10)
    Button(a, height=1, width=10, text="перенести",
           command=lambda: retrieve_input()).grid(column=2, row=20)

    def retrieve_input():
        k_x = int(entry_x.get())
        k_y = int(entry_y.get())
        fig = canv.content
        translation(fig, k_x, k_y)
        canv.redraw_content()

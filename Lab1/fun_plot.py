from math import *
from tkinter import *
from tkinter import ttk

class Cord_Converter:
    def __init__(self, win_width, win_height):
        self.win_width = win_width
        self.win_height = win_height
        return

    def count_bounds(self, l, r, f_values):
        self.max_y = max(f_values)
        self.min_y = min(f_values)

        self.min_x = l
        self.max_x = r

        self.s_factor_x = self.win_width / (self.max_x - self.min_x) 
        self.s_factor_y = self.win_height / (self.max_y - self.min_y)

    def convert_cords(self, x,y):
        x_pix = int((x - self.min_x) * self.s_factor_x)
        y_pix = int((y - self.min_y) * self.s_factor_y)

        return x_pix, self.win_height - y_pix

def draw_axes(canv, cord_converter):
    x, y_min = cord_converter.convert_cords(0, cord_converter.min_y)
    x, y_max = cord_converter.convert_cords(0, cord_converter.max_y)
    canv.create_line(x,y_min,x,y_max,width=2,arrow=LAST)

    x_min, y = cord_converter.convert_cords(cord_converter.min_x, 0)
    x_max, y = cord_converter.convert_cords(cord_converter.max_x, 0)
    canv.create_line(x_min,y,x_max,y,width=2,arrow=LAST)
    return

def draw_plot(canv, f, l, r, win_width, win_height, num_points=400):
    step = (r - l) / num_points
    f_values = [f(l + x * step) for x in range(num_points)]
    print(f_values)

    cc = Cord_Converter(win_width, win_height)
    cc.count_bounds(l, r, f_values)
    draw_axes(canv, cc)

    x_values = [l + x * step for x in range(num_points)]
    for i,x in enumerate(x_values):
        y = f_values[i]
        pix_x, pix_y = cc.convert_cords(x,y)
        canv.create_oval(pix_x, pix_y, pix_x + 1, pix_y - 1, fill = 'black')
        
        x_zerro, y_zerro = cc.convert_cords(0,0)
        canv.create_line(x_zerro-3, pix_y, x_zerro+3, pix_y, width = 0.5, fill = 'black')
        canv.create_line(pix_x, y_zerro-3, pix_x, y_zerro+3, width = 0.5, fill = 'black')
    return
def draw():
    f_str = fun.get()
    l = int(lb.get())
    r = int(rb.get())
    f_str = fun.get()
    f = eval(f"lambda x: {f_str}")

    root_plot = Tk()

    win_width = root_plot.winfo_screenwidth() // 2
    win_height = root_plot.winfo_screenheight() // 2

    canv = Canvas(root_plot, width = win_width, height = win_height, bg = "lightblue")
    draw_plot(canv, f, l, r, win_width, win_height)

    canv.pack()	
    root_plot.mainloop()
    return 

if __name__ == "__main__":
    root_main = Tk()
    root_main.title("Enter Function")
    root_main.configure(background = "grey")
    root_main.geometry('300x100')
    fun_label = Label(root_main ,text = "F(x):").grid(row = 0,column = 0)
    fun = Entry(root_main)
    fun.grid(row = 0,column = 1)

    lb_label = Label(root_main ,text = "Left bound").grid(row = 1,column = 0)
    lb = Entry(root_main)
    lb.grid(row = 1,column = 1)
    rb_label = Label(root_main ,text = "Right bound").grid(row = 2,column = 0)
    rb = Entry(root_main)
    rb.grid(row = 2,column = 1)
    btn = ttk.Button(root_main ,text="Draw", command=draw).grid(row=4,column=0)
    root_main.mainloop()
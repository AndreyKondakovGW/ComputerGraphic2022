from calendar import c
from tkinter import Tk, Canvas, PhotoImage, Button
from primitives import *

class Painter(Tk):
    def __init__(self):
        super().__init__()
        self.win_width = self.winfo_screenwidth() // 2
        self.win_height = self.winfo_screenheight() // 2

        self.title("RatPainter")
        self.brush_color = (0,0,0)
        self.fig_store = {}
        self.should_draw = False
        self.p1_wu = None
        self.p1_be = None
        self.last_poli_point = None
        self.data = []
        self.mode = "initial"

        self.init_bindings()
        self.create_buttons_palet()
        self.create_canvas()
        
        self.mainloop()

    def create_buttons_palet(self):
        button1=Button(self, text="Paint", command=lambda: self.switch_mode("paint"))
        button1.grid(row=1,column=0)

        button2=Button(self, text="Draw Line", command=lambda: self.switch_mode("drawline"))
        button2.grid(row=1,column=1)

        button3=Button(self, text="Draw Line Wu", command=lambda: self.switch_mode("drawline_wu"))
        button3.grid(row=1,column=2)

        button4=Button(self, text="Draw Poligon", command=lambda: self.switch_mode("draw_poli"))
        button4.grid(row=1,column=3)

        button5=Button(self, text="Clear", command=self.clear_all)
        button5.grid(row=1,column=4)
    
    def clear_all(self):
        self.data = []
        self.switch_mode("initial")
        self.clear_canvas()

    def clear_canvas(self):
        self.canv.delete('all')
        self.create_background()

    def switch_mode(self, mode):
        self.mode = mode
        self.redraw_canvas()
    
    def create_canvas(self):
        self.canv = Canvas(self, width=self.win_width, height=self.win_height, bg="white")
        self.canv.grid(row=2, columnspan=5)
        self.create_background()
    
    def create_background(self):
        self.img = PhotoImage(width=self.win_width, height=self.win_height)
        self.canv.create_image((self.win_width / 2, self.win_height / 2), image=self.img, state="normal")
        self.fill_background()

    def fill_background(self):
        self.canv.configure(background="white")

        """ for x in range(0, self.win_width):
            for y in range(0, self.win_height):
                draw_pix(self.img, (x, y), color) """

    def init_bindings(self):
        self.bind('<Motion>', self.hanble_moution)
        self.bind('<ButtonPress-1>', self.hanble_press)
        self.bind('<ButtonRelease-1>', self.hanble_release)

    def hanble_moution(self, event):
        if self.mode == "paint":
            self.draw_by_lines(event)
            if self.should_draw:
                self.fig_store["points"].append((event.x, event.y))
        elif self.mode == "drawline":
            if self.p1_be is not None:
                self.redraw_canvas()
                line_bresenchem(self.img, (self.p1_be[0], self.p1_be[1]), (event.x, event.y), self.brush_color)
        elif self.mode == "drawline_wu":
            if self.p1_wu is not None:
                self.redraw_canvas()
                line_wu(self.img, self.p1_wu[0], self.p1_wu[1], event.x, event.y, (255, 255, 255), self.brush_color)
        elif self.mode == "draw_poli":
            if self.last_poli_point is not None:
                self.redraw_canvas()
                line_bresenchem(self.img, self.last_poli_point, (event.x, event.y), self.brush_color)
        else:
            pass

    def hanble_press(self, event):
        if self.mode == "paint":
            self.should_draw = True
            self.fig_store = {"type": "point_line", "points": [], "color": self.brush_color}
        elif self.mode == "drawline":
            self.draw_breth(event)
        elif self.mode == "drawline_wu":
            self.draw_wu(event)
        elif self.mode == "draw_poli":
            self.add_poli_point(event)
        else:
            pass
    
    def hanble_release(self, event):
        if self.mode == "paint":
            self.should_draw = False
            if self.fig_store["points"]:
                self.add_fig_to_data(self.fig_store["type"], self.fig_store["points"], self.fig_store["color"])
                self.fig_store = None
        else:
            pass
    def add_poli_point(self, event):
        if self.last_poli_point is None:
            self.last_poli_point = (event.x, event.y)
            self.fig_store = {"type": "poligon", "points": [], "color": self.brush_color}
            self.fig_store["points"].append((event.x, event.y))
            self.add_fig_to_data("point_line", self.fig_store["points"], self.fig_store["color"])
        else:
            line_bresenchem(self.img, (event.x, event.y), self.last_poli_point, self.brush_color)

            self.last_poli_point = (event.x, event.y)
            if self.find_pint_in_poli(self.last_poli_point):
                self.last_poli_point = None
                self.data[-1] = self.fig_store
                self.fig_store = None
                self.redraw_canvas()
            else:
                self.fig_store["points"].append((event.x, event.y))
                self.data[-1]["points"].append((event.x, event.y))
    def find_pint_in_poli(self, p):
        x0, y0 = p
        for (x,y) in self.fig_store["points"]:
            if abs(x-x0) < 10 and abs(y-y0) < 10:
                return True

    def draw_by_lines(self, event):
        new_coords = (event.x, event.y)
        if self.should_draw:
            if self.old_coords:
                line_bresenchem(self.img, new_coords, self.old_coords, self.brush_color)
        self.old_coords = new_coords

    def draw_wu(self, event):
        if self.p1_wu is None:
            self.p1_wu = (event.x, event.y)
        else:
            line_wu(self.img, self.p1_wu[0], self.p1_wu[1], event.x, event.y, (255, 255, 255), self.brush_color)
            self.add_fig_to_data("line_wu", [self.p1_wu, (event.x, event.y)], self.brush_color)
            self.p1_wu = None
        return

    def draw_breth(self, event):
        if self.p1_be is None:
            self.p1_be = (event.x, event.y)
        else:
            line_bresenchem(self.img, (self.p1_be[0], self.p1_be[1]), (event.x, event.y), self.brush_color)
            self.add_fig_to_data("line_be", [self.p1_be, (event.x, event.y)], self.brush_color)
            self.p1_be = None
        return
    
    def redraw_canvas(self):
        self.clear_canvas()
        self.draw_from_data()

    def add_fig_to_data(self, type, points, color):
        fig = {
            "type": type,
            "points": points,
            "color": color
        }
        self.data.append(fig)

    def draw_from_data(self):
        for fig in self.data:
            if fig["type"] == "line_be":
                line_bresenchem(self.img, fig["points"][0], fig["points"][1], fig["color"])
            elif fig["type"] == "line_wu":
                x, y = fig["points"][0]
                x1, y1 = fig["points"][1]
                line_wu(self.img, x, y, x1, y1, (255, 255, 255), fig["color"])
            elif fig["type"] == "point_line":
                p0 = fig["points"][0]
                for p in fig["points"][1:]:
                    line_bresenchem(self.img, p0, p, fig["color"])
                    p0 = p
            elif fig['type'] == "poligon":
                p0 = fig["points"][0]
                for p in fig["points"][1:]:
                    line_bresenchem(self.img, p0, p, fig["color"])
                    p0 = p
                line_bresenchem(self.img, p0, fig["points"][0], fig["color"])
            else:
                pass
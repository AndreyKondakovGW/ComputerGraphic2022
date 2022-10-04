from math import *
import re
from tkinter import *
from tkinter import ttk
from draw_line import *

def get_point_inline(p, p1, p2, c1, c2):
    x, y = p
    x1, y1 = p1
    x2, y2 = p2
    dely = 1 if y2 - y1 > 0 else -1


    x = x + 1
    y = int((x - x1) * (y2 - y1) / (x2 - x1) + y1)

    if x > x2:
        x = x2
    if y*dely > y2*dely:
        y = y
    new_c = count_grad_color(c1, c2, x, x1, x2)
    return (x, y), new_c


def draw_vert_line(img, p1, p2, c1, c2, gradient=False):
    x1, y1 = p1
    x2, y2 = p2

    if y1 > y2:
        y1, y2 = y2, y1
        c1, c2 = c2, c1
    for i in range(y1, y2):
        if gradient:
            new_c = count_grad_color(c1, c2, i, y1, y2)
        else:
            new_c = c1
        draw_pix(img, (x1, i), new_c)
        

def draw_triangel(img, p1, p2, p3, c1, c2, c3):
    p1, p2, p3 = sorted([p1, p2, p3], key=lambda x: x[0])
    op, oc= get_point_inline(p1, p1, p2, c1, c2)
    ap, ac= get_point_inline(p1, p1, p3, c1, c3)

    ostart = p1
    oend = p2
    astart = p1
    aend = p3

    ocstart = c1
    ocend = c2
    acstart = c1
    acend = c3

    while ((op != oend) and (ap != aend)):
        draw_vert_line(img, op, ap, oc, ac, True)

        op, oc = get_point_inline(op, ostart, oend, ocstart, ocend)
        ap, ac = get_point_inline(ap, astart, aend, acstart, acend)

        if (op == p2):
            ostart = p2
            oend = p3
            ocstart = c2
            ocend = c3
            while ((ap != aend)):
                draw_vert_line(img, op, ap, oc, ac, True)
                op, oc = get_point_inline(op, ostart, oend, ocstart, ocend)
                ap, ac = get_point_inline(ap, astart, aend, acstart, acend)
            break
        if (ap == p3):
            ostart = p3
            oend = p2
            ocstart = c3
            ocend = c2
            while ((op != oend)):
                draw_vert_line(img, op, ap, oc, ac, True)
                op, oc = get_point_inline(op, ostart, oend, ocstart, ocend)
                ap, ac = get_point_inline(ap, astart, aend, acstart, acend)
            break

    return

class canvas_control:
    def __init__(self):
        self.root_main = Tk()
        self.root_main.title("Draw Triangle")

        win_width = self.root_main.winfo_screenwidth() // 2
        win_height = self.root_main.winfo_screenheight() // 2

        canv = Canvas(self.root_main, width=win_width, height=win_height, bg="white")
        self.img = PhotoImage(width=win_width, height=win_height)
        canv.create_image((win_width / 2, win_height / 2), image=self.img, state="normal")

        self.root_main.bind("<ButtonRelease-1>", self.set_triangle_point)
        self.root_main.bind("<ButtonRelease-2>", self.save_img)

        self.p1 = None
        self.p2 = None
        self.p3 = None

        canv.pack()
        self.root_main.mainloop()

    def set_triangle_point(self, event):
        c1=(255, 0, 0)
        c2=(0, 0, 255)
        c3=(0, 255, 0)
        if self.p1 == None:
            self.p1 = (event.x, event.y)
        elif self.p2 == None:
            self.p2 = (event.x, event.y)
        else:
            self.p3 = (event.x, event.y)
            draw_triangel(self.img, self.p1, self.p2, self.p3, c1, c2, c3)
            self.p2 = None
            self.p3 = None
            self.p1 = None

    def save_img(self, event):
        self.img.write("output3.png", format="png")
        return



if __name__ == "__main__":
    cc = canvas_control()
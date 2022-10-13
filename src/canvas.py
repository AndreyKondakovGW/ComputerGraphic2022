from tkinter import Canvas, PhotoImage
from .fig_storage import Strage
from Lab3.draw_line import *

class MyCanvas(Canvas):
    def __init__(self, tk, width, height, bg="white"):
        super().__init__(tk, width=width, height=height, bg=bg)
        self.width = width
        self.height = height
        self.storage = Strage([], self)
        self.af_point = None

        self.create_image()
    
    def create_image(self, state="normal"):
        self.image = PhotoImage(width=self.width, height=self.height)
        super().create_image((self.width / 2, self.height / 2), image=self.image, state=state)

    def redraw(self):
        self.clear()
        self.storage.draw(self)

    def delete_content(self):
        self.storage.delete_all()
        self.clear()
    
    def clear(self):
        self.delete('all')
        self.create_image()

    def draw_circle(self, x, y, r=10, color=(255, 0, 0)):
        rx, ry = round(x), round(y)
        self.create_oval(rx-r, ry-r, rx+r, ry+r, fill=rgb2hex(color), outline=rgb2hex(color))

    def draw_line(self, p0, p1, color=(0, 0, 0), line_type = "simple"):
        rp0 = round(p0[0]), round(p0[1])
        rp1 = round(p1[0]), round(p1[1])
        if line_type == "simple":
            self.create_line(rp0[0], rp0[1], rp1[0], rp1[1], fill=rgb2hex(color))
        elif line_type == "bresenchem":
            line_bresenchem(self.image, rp0, rp1, color)
        elif line_type == "wu":
            line_wu(self.image, rp0[0], rp0[1], rp1[0], rp1[1], (255, 255, 255), color)

    def draw_dash_line(self, p0, p1, color=(0, 0, 0), dash=(4, 2)):
        rp0 = round(p0[0]), round(p0[1])
        rp1 = round(p1[0]), round(p1[1])
        self.create_line(rp0[0], rp0[1], rp1[0], rp1[1], fill=rgb2hex(color), dash=dash)
        
def select_figs_in_rect(self, p0, p1):
    for fig in self.content:
        if fig.in_rect(p0, p1):
            fig.color = (255, 0, 0)
            fig.selected = True
    self.redraw_content()
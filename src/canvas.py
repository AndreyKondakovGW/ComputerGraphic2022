from tkinter import Canvas, PhotoImage
from .fig_storage import Storage
from Lab3.draw_line import *
from src.point import Point

class MyCanvas(Canvas):
    def __init__(self, tk, width, height, bg="white"):
        super().__init__(tk, width=width, height=height, bg=bg)
        self.width = width
        self.height = height
        self.af_point = None
        self.create_image()

    def set_center(self, x, y, z=0):
        self.center = Point(x, y, z)
        
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

    def delete_selected(self):
        self.storage.delete_selected()
        self.redraw()

    def draw_circle(self, x, y, r=10, color=(255, 0, 0)):
        rx, ry = round(x),round(y)
        self.create_oval(rx-r, ry-r, rx+r, ry+r, fill=rgb2hex(color), outline=rgb2hex(color))

    def draw_line(self, p0, p1, color=(0, 0, 0), line_type = "simple", thickness = 2):
        rp0 = round(p0[0]),round(p0[1])
        rp1 = round(p1[0]),round(p1[1])
        if line_type == "simple":
            self.create_line(rp0[0], rp0[1], rp1[0], rp1[1], fill=rgb2hex(color), width=thickness)
        elif line_type == "bresenchem":
            line_bresenchem(self.image, rp0, rp1, color)
        elif line_type == "wu":
            line_wu(self.image, rp0[0], rp0[1], rp1[0], rp1[1], (255, 255, 255), color)

    def draw_dash_line(self, p0, p1, color=(0, 0, 0), dash=(4, 2)):
        rp0 = round(p0[0]),round(p0[1])
        rp1 = round(p1[0]),round(p1[1])
        self.create_line(rp0[0], rp0[1], rp1[0], rp1[1], fill=rgb2hex(color), dash=dash)
        
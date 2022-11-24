from tkinter import Canvas, PhotoImage
from .fig_storage import Storage
from Lab3.draw_line import *
from src.point import Point
import numpy as np
from PIL import Image, ImageTk

class MyCanvas(Canvas):
    def __init__(self, tk, width, height, bg="white"):
        super().__init__(tk, width=width, height=height, bg=bg)
        self.width = width
        self.height = height
        self.af_point = None
        self.init_pixels()
        self.show_image()

    def set_center(self, x, y, z=0):
        self.center = Point(x, y, z)

    def init_pixels(self):
        self.pixels = np.ones((self.height,self.width, 3))*255

    def show_image(self, state="normal"):
        self.image = ImageTk.PhotoImage(image=Image.fromarray(self.pixels.astype(np.uint8)))
        super().create_image((self.width / 2, self.height / 2), image=self.image, state=state)
    
    def clear(self):
        self.init_pixels()
        self.delete('all')

    def draw_circle(self, x, y, r=10, color=(255, 0, 0)):
        rx, ry = round(x),round(y)
        self.create_oval(rx-r, ry-r, rx+r, ry+r, fill=rgb2hex(color), outline=rgb2hex(color))

    def put_pixel(self, x, y, color=(0,0,0)):
        if x < 0 or x >= self.pixels.shape[1] or y < 0 or y >= self.pixels.shape[0]:
            return
        self.pixels[y][x] = color
        #draw_pix(self.image, (x,y), color)

    def draw_line(self, p0, p1, color=(0, 0, 0), line_type = "bresenchem", thickness = 1):
        rp0 = round(p0[0]),round(p0[1])
        rp1 = round(p1[0]),round(p1[1])
        if line_type == "simple":
            self.create_line(rp0[0], rp0[1], rp1[0], rp1[1], fill=rgb2hex(color), width=thickness)
        elif line_type == "bresenchem":
            if thickness == 1:
                self.line_bresenchem_canvas(rp0, rp1, color)
            else:
                for i in range(-thickness, thickness):
                    pi1 = self.clamp_point(rp0[0] + i, rp0[1])
                    pi2 = self.clamp_point(rp1[0] + i, rp1[1])
                    self.line_bresenchem_canvas(pi1, pi2, color)
        elif line_type == "wu":
            line_wu(self.image, rp0[0], rp0[1], rp1[0], rp1[1], (255, 255, 255), color)

    def clamp_point(self, x, y):
        if x < 0:
            x = 1
        if y < 0:
            y = 1
        return x, y

    def draw_dash_line(self, p0, p1, color=(0, 0, 0), dash=(4, 2)):
        rp0 = round(p0[0]),round(p0[1])
        rp1 = round(p1[0]),round(p1[1])
        self.create_line(rp0[0], rp0[1], rp1[0], rp1[1], fill=rgb2hex(color), dash=dash)
    
    def line_bresenchem_canvas(self, p1, p2, c1=(0, 0, 0), c2=None):
        '''
        Функция рисования отрезка используя алгоритм Брезенхэма
        - p1, p2  координаты концов отрезка
        - c1, c2  цвета в формате RGB
        - gradient флаг градиентного закрашивания
        если true то отрезок закрашивается градиентом от цвета c1 к цвету c2
        иначе закрашивается красным 
        '''
        x1, y1 = p1
        x2, y2 = p2
        y = y1
        x = x1
        dy = abs(y2 - y1)
        dx = abs(x2 - x1)
        grad = dy / (dx + 0.000001)
        dely = 1 if y2 - y1 > 0 else -1
        delx = 1 if x2 - x1 > 0 else -1

        if grad <= 1:
            di = 2 * dy - dx
            for x in range(x1, x2, delx):
                if c2 is not None:
                    new_c = count_grad_color(c1, c2, x, x1, x2)
                else:
                    # new_c = (255, 0, 0)
                    new_c = c1
                self.put_pixel(x, y, new_c)
                if di < 0:
                    di = di + 2 * dy
                else:
                    y = y + dely
                    di = di + 2 * (dy - dx)
        else:
            di = 2 * dx - dy
            for y in range(y1, y2, dely):
                if c2 is not None:
                    new_c = count_grad_color(c1, c2, y, y1, y2)
                else:
                    # new_c = (255, 0, 0)
                    new_c = c1
                self.put_pixel(x, y, new_c)
                if di < 0:
                    di = di + 2 * dx
                else:
                    x = x + delx
                    di = di + 2 * (dx - dy)
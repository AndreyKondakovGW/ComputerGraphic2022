import pygame as pg
from src.point import Point

class GameCanvas:
    def __init__(self, width, height, bg="white"):
        self.width = width
        self.height = height
        size = (width, height)
        self.screen = pg.display.set_mode(size)

    def set_center(self, x, y, z=0):
        self.center = Point(x, y, z)

    def clear(self):
        self.screen.fill(((255, 255, 255)))
        pg.display.update()


    def draw_circle(self, x, y, r=10, color=(255, 0, 0)):
        pass

    def draw_line(self, p0, p1, color=(0, 0, 0), line_type = "simple", thickness = 2):
        pass

    def draw_dash_line(self, p0, p1, color=(0, 0, 0), dash=(4, 2)):
        pass
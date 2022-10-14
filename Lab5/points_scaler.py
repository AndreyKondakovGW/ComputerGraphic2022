import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
lab4dir = os.path.join(parentdir, "Lab4")
sys.path.insert(0, lab4dir) 

from transformation import translation, scaling

class PointsScaler:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def scale_points(self, drawer):
        points = drawer.points
        self.fill_key_points(points)
        self.move_to_center(drawer)
        self.scale_from_center(drawer)
        self.round_points(drawer)

    def fill_key_points(self, points):
        self.max_x, self.min_x = self.array_extremums(points, "x")
        self.max_y, self.min_y = self.array_extremums(points, "y")
        self.mid_x = (self.min_x + self.max_x) // 2
        self.mid_y = (self.min_y + self.max_y) // 2

    def move_to_center(self, drawer):
        mid_screen_x = self.screen_width // 2
        mid_screen_y = self.screen_height // 2
        translation(drawer, mid_screen_x - self.mid_x, mid_screen_y - self.mid_y)
        
    def scale_from_center(self, drawer):
        midpoint = (self.screen_width // 2, self.screen_height // 2)
        kx = self.screen_width / abs(self.max_x - self.min_x)
        ky = self.screen_height / abs(self.max_y - self.min_y)
        k = min(kx, ky)
        scaling(drawer, k, k, midpoint)

    def round_points(self, drawer):
        rounded_points = [(round(p[0]), round(p[1])) for p in drawer.points]
        drawer.points = rounded_points

    def array_extremums(self, points, attribute):
        ind = 0 if attribute == "x" else 1
        arr = [p[ind] for p in points]
        max_value = 0
        min_value = self.screen_width if attribute == "x" else self.screen_height
        for value in arr:
            if value > max_value:
                max_value = value
            if value < min_value:
                min_value = value
        return max_value, min_value
from Lab4.mouseLine import MouseLine
from src.controller_mode import ControllerMode
import random
import time

class MidePointMode(ControllerMode):
    def __init__(self, canvas, color=(0, 0, 0)):
        self.canvas = canvas
        self.brush_color = color
        self.points = []
        self.p0 = None
        self.roughness = 0.25

    def set_roughness(self, roughness):
        self.roughness = roughness

    def hanble_press(self, event):
        if self.p0 is None:
            self.p0 = (event.x, event.y)
        else:
            #points = interactive_midpoint_displacement(self.canvas, self.p0, (event.x, event.y), self.roughness)
            points = midpoint_displacement(self.p0, (event.x, event.y), self.roughness)
            self.canvas.storage.figs.append(MouseLine(points, self.brush_color))
            self.canvas.redraw()
            self.p0 = None

def displace_point(p1, p2, roughness):
    """Returns a new point displaced from the midpoint of p1 and p2."""
    x1, y1 = p1
    x2, y2 = p2
    x, y = (x1 + x2) / 2, (y1 + y2) / 2
    len = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if abs(x1 - x2) <= 1:
        return p1
    else:
        new_y = y + len * random.uniform(-roughness, roughness)
        return x, new_y

def midpoint_displacement(p1, p2, roughness):
    """Returns a list of points representing a mountain range."""
    pc = displace_point(p1, p2, roughness)
    if pc == p1:
        return [p1, p2]
    else:
        return midpoint_displacement(p1, pc, roughness) + [pc] + midpoint_displacement(pc, p2, roughness)

def interactive_midpoint_displacement(canv, p1, p2, roughness, sleep = 2):
    points = [p1, p2]
    points_new = points.copy()
    flag = True
    canv.storage.figs.append(MouseLine(points, (0, 0, 0)))
    canv.storage.figs[-1].draw(canv)
    canv.update()
    time.sleep(sleep)
    while flag:
        points = points_new.copy()
        for i in range(len(points)-1):
            pc = displace_point(points[i], points[i+1], roughness)
            if pc == points[i]:
                flag = False
                continue
            points_new = points_new[:i+1+i] + [pc] + points_new[i+1+i:]
        canv.storage.figs[-1].points = points_new
        canv.redraw()
        canv.update()
        time.sleep(sleep)
    print("finished")
    return points_new
    

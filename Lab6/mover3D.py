from Lab6.transformation_3d import *
from src.controller_mode import ControllerMode
from src.point import *

def move_figure(fig, dx, dy,dz):
    old_points = fig.points
    if fig.selected:
        fig.points = translate(fig.points, dx, dy, dz)

class MoverMode3D(ControllerMode):
    def __init__(self, renderer,scene):
        self.renderer = renderer
        self.scene = scene
        self.should_draw = False
        self.isXmode = False
        self.isYmode = False
        self.isZmode = False

    def hanble_x(self, event):
        self.isXmode = not self.isXmode
        if self.isXmode or self.isYmode or self.isZmode:
            dir = Point(int(self.isXmode), int(self.isYmode), int(self.isZmode))
            self.renderer.render_scene(self.scene)
            self.renderer.draw_direction(Point(0,0,0), dir)

    def hanble_y(self, event):
        self.isYmode = not self.isYmode
        if self.isXmode or self.isYmode or self.isZmode:
            dir = Point(int(self.isXmode), int(self.isYmode), int(self.isZmode))
            self.renderer.render_scene(self.scene)
            self.renderer.draw_direction(Point(0,0,0), dir)

    def hanble_z(self, event):
        self.isZmode = not self.isZmode
        if self.isXmode or self.isYmode or self.isZmode:
            dir = Point(int(self.isXmode), int(self.isYmode), int(self.isZmode))
            self.renderer.render_scene(self.scene)
            self.renderer.draw_direction(Point(0,0,0), dir)

    def hanble_left(self, event):
        x = int(self.isXmode) * -5
        y = int(self.isYmode) * -5
        z = int(self.isZmode) * -5
        points = []
        for fig in self.scene.storage:
            if fig.selected:
                move_figure(fig, x, y, z)
                points += fig.points
        if len(points) > 0:
            self.renderer.render_scene(self.scene)
            dir = Point(-int(self.isXmode), -int(self.isYmode), -int(self.isZmode))
            self.renderer.draw_direction(face_midpoint(points), dir)

    def hanble_right(self, event):
        x = int(self.isXmode) * 5
        y = int(self.isYmode) * 5
        z = int(self.isZmode) * 5
        points = []
        for fig in self.scene.storage:
            if fig.selected:
                move_figure(fig, x, y, z)
                points += fig.points
        if len(points) > 0:
            self.renderer.render_scene(self.scene)
            dir = Point(int(self.isXmode), int(self.isYmode), int(self.isZmode))
            self.renderer.draw_direction(face_midpoint(points), dir)

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from src.point import Point
from Lab8.camera_mover import CameraMoverMode

from Lab7.ui import UI7

if __name__ == '__main__':
    ui = UI7()
    ui.create_camera(Point(300, 300, 300), Point(0, 0, 0))
    ui.add_button("Move Camera", lambda: ui.controller.switch_mode("move_camera"))
    ui.controller.add_mode("move_camera", CameraMoverMode(ui.renderer, ui.scene, ui.camera))
    ui.run()
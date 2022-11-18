import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from src.point import Point
from Lab8.camera_mover import CameraMoverMode

from Lab8.ui import UI8

if __name__ == '__main__':
    ui = UI8()
    ui.create_camera(Point(300, 300, 300), Point(0, 0, 0))
    ui.controller.add_mode("move_camera", CameraMoverMode(ui.renderer, ui.scene, ui.camera))        
    ui.run()
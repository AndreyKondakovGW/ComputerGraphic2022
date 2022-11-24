import sys
import os

from Lab8.floating_horizon_rotator import FloatingHorizonRotatorMode

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from src.point import Point
from Lab8.camera_mover import CameraMoverMode

from Lab8.ui import UI8

if __name__ == '__main__':
    ui = UI8()
    ui.create_camera(Point(300, 300, 300), Point(0, 0, 0))
    ui.controller.add_mode("move_camera", CameraMoverMode(ui.renderer, ui.scene, ui.camera))
    ui.controller.add_mode('floating_horizon', FloatingHorizonRotatorMode(ui.renderer, ui.scene))
    ui.run()
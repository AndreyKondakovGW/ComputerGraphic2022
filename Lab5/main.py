import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import src
from Lab4.rect_selector import RectSelectorMode
from Lab4.mover import MoverMode
from Lab4.rotator import RotatorMode
from Lab4.scaler import ScalerMode
from midpoint_displacement import MidePointMode
from bezier import BezierMode

ui = src.UI.UI_base()
ui.add_button("",lambda: ui.controller.switch_mode("Mid point"), icon_name='line-segment.png')
ui.add_slider(1,100,50, lambda x: ui.controller.modes["Mid point"].set_roughness(float(x)/ 100))
ui.add_button("",lambda: ui.controller.switch_mode("Mid point int"), icon_name='line-segment.png')
ui.add_slider(1,100,50, lambda x: ui.controller.modes["Mid point int"].set_roughness(float(x)/ 100))
ui.add_button("",lambda: ui.controller.switch_mode("Beizer"), icon_name='blue_line.png')
ui.add_button("Select", lambda: ui.controller.switch_mode("selectrectangle"), icon_name='shape.png')
ui.add_button("Translation", lambda: ui.controller.switch_mode("affine_translation"), icon_name='move.png')
ui.add_button("Rotation", lambda: ui.controller.switch_mode("affine_rotation"), icon_name='refresh.png')
ui.add_button("Scaling", lambda: ui.controller.switch_mode("affine_scaling"), icon_name='move.png')

ui.add_button("Clear",lambda: ui.canv.delete_content(),  icon_name='bin.png')
ui.create_canvas()
ui.controller.add_mode("selectrectangle", RectSelectorMode(ui.canv))
ui.controller.add_mode("affine_translation", MoverMode(ui.canv))
ui.controller.add_mode("affine_rotation", RotatorMode(ui.canv))
ui.controller.add_mode("affine_scaling", ScalerMode(ui.canv))
ui.controller.add_mode("Mid point", MidePointMode(ui.canv))
ui.controller.add_mode("Mid point int", MidePointMode(ui.canv, interactive=True))
ui.controller.add_mode("Beizer", BezierMode(ui.canv))
ui.run()
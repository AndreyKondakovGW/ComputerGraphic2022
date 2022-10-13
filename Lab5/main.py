import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import src
from midpoint_displacement import MidePointMode

ui = src.UI.UI_base()
ui.add_button("",lambda: ui.controller.switch_mode("Mid point"), icon_name='line-segment.png')
ui.add_slider(1,100,50, lambda x: ui.controller.modes["Mid point"].set_roughness(float(x)/ 100))
ui.add_button("Clear",lambda: ui.canv.delete_content(),  icon_name='bin.png')
ui.create_canvas()
ui.controller.add_mode("Mid point", MidePointMode(ui.canv))
ui.run()
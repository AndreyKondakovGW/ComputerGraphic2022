import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from Lab5.l_systemmode import LSystemMode
from src.UI import UI_base
if __name__ == "__main__":
    ui = UI_base()
    ui.add_button("Open file", lambda: ui.controller.current_mode.open_file())
    ui.add_entry("Generation", lambda x: ui.controller.current_mode.set_generation(x),"1")
    ui.add_button("Draw", lambda: ui.controller.current_mode.draw())
    ui.create_canvas()
    ui.controller.current_mode = LSystemMode(ui.canv)
    ui.run()
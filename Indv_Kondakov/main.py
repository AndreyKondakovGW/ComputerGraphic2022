import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import src
from Lab4.dot import DotMode
from Indv_Kondakov.delaunayMode import TriangulationMode
from Lab4.rect_selector import RectSelectorMode

if __name__ == "__main__":

    ui = src.UI.UI_base(titel="RatPainter")
    ui.add_button("Dot", lambda: ui.controller.switch_mode("dot"), icon_name='dot-circle.png')
    ui.add_button("Delanay", lambda: ui.controller.switch_mode("delanay"), icon_name='poligon.png')

    ui.add_button("Select", lambda: ui.controller.switch_mode("selectrectangle"), icon_name='shape.png')
    ui.add_button("Delete", lambda: ui.canv.delete_selected(), icon_name='eraser.png')
    ui.add_button("Clear", lambda: ui.canv.delete_content(), icon_name='bin.png')
    
    ui.create_canvas(use_storage=True)
    ui.controller.add_mode("dot", DotMode(ui.canv))
    ui.controller.add_mode("delanay", TriangulationMode(ui.canv))
    ui.controller.add_mode("selectrectangle", RectSelectorMode(ui.canv))
    ui.run()
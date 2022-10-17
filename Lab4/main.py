import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import src
from Lab4.dot import DotMode
from Lab4.line import LineMode
from Lab4.poligon import PoligonMode
from Lab4.rect import RectangleMode
from Lab4.rect_selector import RectSelectorMode

from Lab4.mover import MoverMode
from Lab4.rotator import RotatorMode
from Lab4.scaler import ScalerMode

from Lab4.mark_segments_direction import MarkSegmentsDirectionMode
from Lab4.check_convex import CheckPolygonMode

if __name__ == "__main__":

    ui = src.UI.UI_base(titel="RatPainter")
    ui.add_button("Dot", lambda: ui.controller.switch_mode("dot"), icon_name='dot-circle.png')
    ui.add_button("Draw Line", lambda: ui.controller.switch_mode("drawline"), icon_name='line-segment.png')
    ui.add_button("Draw Line Wu", lambda:ui.controller.switch_mode("drawlinewu"), icon_name='line-segment.png')
    ui.add_button("Draw Poligon", lambda:  ui.controller.switch_mode("drawpoligon"), icon_name='poligon.png')
    ui.add_button("Draw Rect", lambda: ui.controller.switch_mode("drawrectangle"), icon_name='rect.png')

    ui.add_button("Select", lambda: ui.controller.switch_mode("selectrectangle"), icon_name='shape.png')
    ui.add_button("Translation", lambda: ui.controller.switch_mode("affine_translation"), icon_name='move.png')
    ui.add_button("Rotation", lambda: ui.controller.switch_mode("affine_rotation"), icon_name='refresh.png')
    ui.add_button("Scaling", lambda: ui.controller.switch_mode("affine_scaling"), icon_name='move.png')

    ui.add_button("Mark Segments", lambda: ui.controller.switch_mode("marksegments"), icon_name='blue_line.png')
    ui.add_button("Check Convex", lambda: ui.controller.switch_mode("checkconvex"), icon_name='iran.png')
    ui.add_button("Check Polygon", lambda: ui.controller.switch_mode("checkpolygon"), icon_name='cursor.png')

    ui.add_button("Delete", lambda: ui.canv.delete_selected(), icon_name='eraser.png')
    ui.add_button("Clear", lambda: ui.canv.delete_content(), icon_name='bin.png')
    
    ui.create_canvas()
    ui.controller.add_mode("dot", DotMode(ui.canv))
    ui.controller.add_mode("drawline", LineMode(ui.canv, line_type="bresenchem"))
    ui.controller.add_mode("drawlinewu", LineMode(ui.canv, line_type="wu"))
    ui.controller.add_mode("drawpoligon", PoligonMode(ui.canv))
    ui.controller.add_mode("drawrectangle", RectangleMode(ui.canv))

    ui.controller.add_mode("selectrectangle", RectSelectorMode(ui.canv))
    ui.controller.add_mode("affine_translation", MoverMode(ui.canv))
    ui.controller.add_mode("affine_rotation", RotatorMode(ui.canv))
    ui.controller.add_mode("affine_scaling", ScalerMode(ui.canv))

    ui.controller.add_mode("marksegments", MarkSegmentsDirectionMode(ui.canv))
    ui.controller.add_mode("checkconvex", CheckPolygonMode(ui.canv, convex=True))
    ui.controller.add_mode("checkpolygon", CheckPolygonMode(ui.canv, convex=False))
    ui.run()
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from src.UI import UI_base
from src.point import Point
from Lab6.cube import Cube
from Lab6.modern_line import LineM

#Создать режим создания точек и фигру по точкам
#Создать ражим переключения между 2Д и 3Д(проекции) 
if __name__ == '__main__':
    """ ui = UI_base()
    ui.add_button(">",lambda: ui.side_menue_layout.grid_remove())
    ui.add_button("<",lambda: ui.side_menue_layout.grid())
    ui.create_canvas()
    ui.run() """
    ui = UI_base()
    ui.create_canvas()
    ui.create_drawer()
    ui.drawer.set_mode("3D")
    ui.canv.storage.add_figure(LineM([Point(200,100,0), Point(-200,100,0)]))
    ui.canv.storage.add_figure(LineM([Point(100,-200,0), Point(100,200,0)]))
    ui.canv.storage.add_figure(LineM([Point(100,100,100), Point(100,100,-100)]))
    ui.canv.storage.add_figure(Cube(Point(140,120,110), 100))
    # lineX = LineM([Point(200,100,0), Point(-200,100,0)])
    # lineY = LineM([Point(100,-200,0), Point(100,200,0)])
    # lineZ = LineM([Point(100,100,100), Point(100,100,-100)])
    # lineX.draw(ui.drawer)
    # lineZ.draw(ui.drawer)
    # lineY.draw(ui.drawer)
    # cube = Cube(Point(140,120,110), 100)
    # cube.draw(ui.drawer)
    ui.run()


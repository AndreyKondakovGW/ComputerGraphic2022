from Lab8.ui import UI8
from Lab9.guro_renderer import GuroRenderer

class UI9(UI8):
    def create_renderer(self):
        self.renderer = GuroRenderer(self.canv)

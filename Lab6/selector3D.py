from src.controller_mode import ControllerMode

class RectSelector3DMode(ControllerMode):
    def __init__(self, renderer,scene, color=(0,0,0)):
        self.renderer = renderer
        self.scene = scene
        self.canvas = self.renderer.canvas
        self.brush_color = color
        self.should_draw = False
        self.p0 = None

    def hanble_moution(self, event):
        if self.should_draw:
            x1, y1 = self.p0
            x2, y2 = event.x, event.y

            self.renderer.render_scene(self.scene)
            self.canvas.draw_dash_line((x1, y1), (x2, y1), self.brush_color)
            self.canvas.draw_dash_line((x2, y1), (x2, y2), self.brush_color)
            self.canvas.draw_dash_line((x2, y2), (x1, y2), self.brush_color)
            self.canvas.draw_dash_line((x1, y2), (x1, y1), self.brush_color)

    def hanble_press(self, event):
        self.should_draw = True
        self.p0 = (event.x, event.y)
        for fig in self.scene.storage:
            fig.deselect()
        self.renderer.render_scene(self.scene)

    def hanble_release(self, event):
        if self.should_draw:
            for fig in self.scene.storage:
                if fig.in_rect(self.p0, (event.x, event.y)):
                    fig.select()
                else:
                    fig.deselect()
            self.should_draw = False
            self.p0 = None
            self.renderer.render_scene(self.scene)

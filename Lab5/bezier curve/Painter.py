from modes import *


class Painter():
    def __init__(self, brush_color=(0, 0, 0)):
        super().__init__()
        self.canvas = None
        self.brush_color = brush_color
        self.current_mode = DummyMode()

    def set_canvas(self, canvas):
        self.canvas = canvas

    def switch_mode(self, new_mode_name):
        if new_mode_name == "clear":
            self.current_mode = DummyMode()
            self.canvas.delete_content()
        elif new_mode_name == "add":
            self.current_mode = AddMode(self.canvas)
        elif new_mode_name == 'move':
            self.current_mode = MoveMode(self.canvas)
        elif new_mode_name == 'delete':
            self.current_mode = DeleteMode(self.canvas)
        else:
            pass

    def handle_motion(self, event):
        self.current_mode.handle_motion(event)
 
    def handle_press(self, event):
        self.current_mode.handle_press(event)

    def handle_release(self, event):
        self.current_mode.handle_release(event)

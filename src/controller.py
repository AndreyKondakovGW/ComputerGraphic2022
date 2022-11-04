from src.controller_mode import ControllerMode

class UI_controller():
    def __init__(self, brush_color=(0, 0, 0)):
        super().__init__()
        self.canvas = None
        self.brush_color = brush_color
        self.current_mode = ControllerMode()

        self.modes = {}

    def set_canvas(self, canvas):
        self.canvas = canvas

    def add_mode(self, name, mode):
        self.modes[name] = mode
        mode.brush_color = self.brush_color

    def switch_mode(self, mode_name):
        self.current_mode.set_default_params()
        self.current_mode = self.modes.get(mode_name, ControllerMode())
        self.current_mode.init_params()
    
    def hanble_moution(self, event):
        if event.widget == self.canvas:
            self.current_mode.hanble_moution(event)
        
    def hanble_press(self, event):
        if event.widget == self.canvas:
            self.current_mode.hanble_press(event)

    def hanble_right_press(self, event):
        if event.widget == self.canvas:
            self.current_mode.hanble_right_press(event)

    def hanble_release(self, event):
        if event.widget == self.canvas:
            self.current_mode.hanble_release(event)

    def hanble_mouse_wheel(self, event):
        if event.widget == self.canvas:
            self.current_mode.hanble_mouse_wheel(event)

    def hanble_x(self, event):
        self.current_mode.hanble_x(event)

    def hanble_y(self, event):
        self.current_mode.hanble_y(event)

    def hanble_z(self, event):
        self.current_mode.hanble_z(event)

    def hanble_left(self, event):
        self.current_mode.hanble_left(event)

    def hanble_right(self, event):
        self.current_mode.hanble_right(event)

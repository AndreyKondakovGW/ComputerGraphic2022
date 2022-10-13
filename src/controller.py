from Lab4.dummy import DummyMode


class UI_controller():
    def __init__(self, brush_color=(0, 0, 0)):
        super().__init__()
        self.canvas = None
        self.brush_color = brush_color
        self.current_mode = DummyMode()

        self.modes = {}

    def set_canvas(self, canvas):
        self.canvas = canvas

    def add_mode(self, name, mode):
        self.modes[name] = mode
        mode.brush_color = self.brush_color

    def switch_mode(self, mode_name):
        print("Switching to mode: ", mode_name)
        self.current_mode = self.modes.get(mode_name, DummyMode())
        print(self.current_mode)
    
    def hanble_moution(self, event):
        if event.widget == self.canvas:
            self.current_mode.hanble_moution(event)
        

    def hanble_press(self, event):
        if event.widget == self.canvas:
            self.current_mode.hanble_press(event)

    def hanble_release(self, event):
        if event.widget == self.canvas:
            self.current_mode.hanble_release(event)

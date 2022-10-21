class Scene:
    def __init__(self):
        self.storage = []
        self.camera = None
        self.light = None
    
    def add_figure(self, figure):
        self.storage.append(figure)

    def clear(self):
        self.storage = []
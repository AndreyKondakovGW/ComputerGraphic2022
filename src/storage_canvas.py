from src.canvas import MyCanvas
from src.fig_storage import Storage

class StorageCanvas(MyCanvas):
    def __init__(self, tk, width, height, bg="white"):
        super().__init__(tk, width=width, height=height, bg=bg)
        self.storage = Storage([],self)

    def redraw(self):
        self.clear()
        self.storage.draw(self)

    def delete_content(self):
        self.storage.delete_all()
        self.clear()

    def delete_selected(self):
        self.storage.delete_selected()
        self.redraw()

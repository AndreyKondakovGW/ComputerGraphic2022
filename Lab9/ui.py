from Lab8.ui import UI8
from tkinter import filedialog
from PIL import Image
from Lab9.guro_renderer import GuroRenderer
from numpy import asarray
import os
class UI9(UI8):
    def __init__(self):
        super().__init__()
        current_dir = os.getcwd()
        self.models_dir = os.path.join(current_dir, 'Lab9', 'textures')

    def add_leftmost_buttons(self):
        super().add_leftmost_buttons()
        self.add_button("Toggle texture mode", command=self.toggle_texture_mode)
        self.add_button("Apply texture", command=self.apply_texture)

    def toggle_texture_mode(self):
        self.renderer.use_texture = not self.renderer.use_texture
        self.renderer.render_scene(self.scene)

    def apply_texture(self):
        filename = filedialog.askopenfilename(initialdir=self.models_dir, filetypes=[("Файл 'PNG'", ".png"), ("Файл 'JPG'", ".jpg")])
        if filename is None:
            return
        img = Image.open(filename)
 
        texture_matrix = asarray(img)
        print(texture_matrix.shape)
        for fig in self.scene.storage:
            if fig.selected:
                fig.set_texture(texture_matrix)
        self.renderer.render_scene(self.scene)

    def create_renderer(self):
        self.renderer = GuroRenderer(self.canv)

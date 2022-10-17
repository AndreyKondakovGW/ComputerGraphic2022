from base_filler import BaseFiller
from tkinter import *

from PIL import Image
from PIL import ImageTk

import numpy as np

class MyPhotoImage(ImageTk.PhotoImage):
    def __init__(self, file):
        self.image = Image.open(file)
        self.image_arr = np.array(self.image)
        super().__init__(self.image)

    def get(self, x, y):
        r = self.image_arr[y, x, 0]
        g = self.image_arr[y, x, 1]
        b = self.image_arr[y, x, 2]
        return r, g, b

class ImageFiller(BaseFiller):
    def __init__(self, root, image_path):
        super().__init__(root)
        self.fill_image = MyPhotoImage(file=image_path)

    def next_color(self, x, y):
        image_center_x = self.fill_image.width() // 2
        image_center_y = self.fill_image.height() // 2
        x = x - self.start_x + image_center_x
        y = y - self.start_y + image_center_y
        x %= self.fill_image.width()
        y %= self.fill_image.height()
        return self.fill_image.get(x, y)

if __name__ == "__main__":
    root = Tk()
    root.title("Для заливки фигуры используйте двойной щелчок мыши")
    color_filler = ImageFiller(root, "./test.jpg")
    color_filler.start()
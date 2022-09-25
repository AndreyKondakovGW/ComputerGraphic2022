from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from PIL import Image
from PIL import ImageTk
from hsv_image import HSVImage

import numpy as np

class UI:
    def __init__(self):
        self.root = Tk()
        self.init_ui()

    def open_file(self):
        file = filedialog.askopenfilename(initialdir="./Lab2")
        if file is None:
            return

        img = Image.open(file)
        rgb_image = np.array(img)
        self.canvas.config(width=img.width, height=img.height)
        self.draw_image(img)
        self.hsv_image = HSVImage(rgb_image)
        
    def save_file(self):
        filename = "changed_file.jpg"
        self.image.save("./Lab2/" + filename)
        

    def init_ui(self):
        c_width = 400
        c_height = 400
        self.canvas = Canvas(self.root, width=c_width, height=c_height)
        self.canvas.grid(row=0, column=0)
        
        self.buttons_row = ttk.Frame(self.root)
        self.buttons_row.grid(row=1, column=0, pady=(10,0))
        
        self.open_button = ttk.Button(self.buttons_row, text="Open", command=self.open_file)
        self.open_button.grid(row=0, column=0, padx=10)

        self.save_button = ttk.Button(self.buttons_row, text="Save", command=self.save_file)
        self.save_button.grid(row=0, column=1, padx=10)


        self.sliders_row = ttk.Frame(self.root, padding=10)
        self.sliders_row.grid(row=2, column=0)

        self.labels_col = ttk.Frame(self.sliders_row, padding=10)
        self.sliders_col = ttk.Frame(self.sliders_row, padding=10)
        self.labels_col.grid(row=0, column=0)
        self.sliders_col.grid(row=0, column=1)

        self.apply_buuton = ttk.Button(self.sliders_row, text="Apply", command=self.apply_changes)
        self.apply_buuton.grid(row=0, column=2, sticky=N+S)

        self.h_label = ttk.Label(self.labels_col, text="Hue", padding=12)
        self.s_label = ttk.Label(self.labels_col, text="Saturation", padding=12)
        self.v_label = ttk.Label(self.labels_col, text="Value", padding=12)

        self.h_label.grid(row=0, pady=(17,0))
        self.s_label.grid(row=1)
        self.v_label.grid(row=2)

        self.h_slider = Scale(self.sliders_col, from_=0, to=360, orient=HORIZONTAL,
                                  length=200)
        self.s_slider = Scale(self.sliders_col, from_=-100, to=100, orient=HORIZONTAL,
                                  length=200)
        self.v_slider = Scale(self.sliders_col, from_=-100, to=100, orient=HORIZONTAL,
                                  length=200)
        self.h_slider.grid(row=0)
        self.s_slider.grid(row=1)
        self.v_slider.grid(row=2)

    def apply_changes(self):
        h = self.h_slider.get()
        v = self.v_slider.get()
        s = self.s_slider.get()
        self.hsv_image.change_hsv(h, s, v)
        self.redraw()

    def draw_image(self, image):
        self.photo_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, image=self.photo_image, anchor=NW)

    def draw_image_from_arr(self, arr):
        self.image = Image.fromarray(arr)
        self.draw_image(self.image)

    def redraw(self):
        rgb_image = self.hsv_image.to_rgb()
        self.draw_image_from_arr(rgb_image)
    
    def start_app(self):
        self.root.mainloop()

ui = UI()
ui.start_app()
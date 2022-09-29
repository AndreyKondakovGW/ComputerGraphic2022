from tkinter import Tk, Canvas, PhotoImage
import numpy as np


def rgb2hex(rgb):
    hex_c = "#%02x%02x%02x" % rgb
    return hex_c


def draw_pix(img, point, alpha, bg, color=(255, 0, 0)):
    color = tuple(np.trunc(np.around(np.dot(alpha, color) + np.dot((1 - alpha), bg))).astype(int))

    img.put(rgb2hex(color), point)


def line(img, x1, y1, x2, y2, color, bg):
    if x2 < x1:
        x2, x1 = x1, x2
        y2, y1 = y1, y2
    d_x = x2 - x1
    d_y = y2 - y1
    gradient = d_y / d_x
    x_end = round(x1)
    y_end = y1 + gradient * (x_end - x1)
    x_gap = 1 - (x1 + 0.5) % 1
    x_pxl1 = x_end
    y_pxl1 = int(y_end // 1)
    draw_pix(img, (x_pxl1, y_pxl1), (1 - y_end % 1) * x_gap, bg, color=(255, 0, 0))
    draw_pix(img, (x_pxl1, y_pxl1 + 1), y_end % 1 * x_gap, bg, color=(255, 0, 0))
    inter_y = y_end + gradient

    x_end = round(x2)
    y_end = y2 + gradient * (x_end - x2)
    x_gap = (x2 + 0.5) % 1
    x_pxl2 = x_end
    y_pxl2 = y_end // 1
    draw_pix(img, (x_pxl2, int(y_pxl2)), (1 - y_end % 1) * x_gap, bg, color=(255, 0, 0))
    draw_pix(img, (x_pxl2, int(y_pxl2 + 1)), y_end % 1 * x_gap, bg, color=(255, 0, 0))

    for x in range(x_pxl1 + 1, x_pxl2 - 1):
        draw_pix(img, (x, int(inter_y)), 1 - inter_y % 1, bg, color=(255, 0, 0))
        draw_pix(img, (x, int(inter_y) + 1), inter_y % 1, bg, color=(255, 0, 0))
        inter_y = inter_y + gradient


root_main = Tk()
root_main.title("Line Wu")

win_width = root_main.winfo_screenwidth() // 2
win_height = root_main.winfo_screenheight() // 2
bg = (255, 255, 255)

canv = Canvas(root_main, width=win_width, height=win_height, bg="white")
img = PhotoImage(width=win_width, height=win_height)
canv.create_image((win_width / 2, win_height / 2), image=img, state="normal")

c1 = (255, 0, 0)
x1 = 300
x2 = 100
y1 = 100
y2 = 400
line(img, x1, y1, x2, y2, c1, bg)
canv.pack()
root_main.mainloop()

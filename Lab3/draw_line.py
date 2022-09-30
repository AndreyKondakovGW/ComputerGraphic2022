from tkinter import Tk, Canvas, PhotoImage

import numpy as np


def line_bresenchem(img, p1, p2, c1=(0, 0, 0), c2=None):
    '''
    Функция рисования отрезка используя алгоритм Брезенхэма
    - p1, p2  координаты концов отрезка
    - c1, c2  цвета в формате RGB
    - gradient флаг градиентного закрашивания
    если true то отрезок закрашивается градиентом от цвета c1 к цвету c2
    иначе закрашивается красным 
    '''
    x1, y1 = p1
    x2, y2 = p2
    y = y1
    x = x1
    dy = abs(y2 - y1)
    dx = abs(x2 - x1)
    grad = dy / (dx + 0.000001)
    dely = 1 if y2 - y1 > 0 else -1
    delx = 1 if x2 - x1 > 0 else -1

    if grad <= 1:
        di = 2 * dy - dx
        for x in range(x1, x2, delx):
            if c2 is not None:
                new_c = count_grad_color(c1, c2, x, x1, x2)
            else:
                # new_c = (255, 0, 0)
                new_c = c1
            draw_pix(img, (x, y), new_c)
            if di < 0:
                di = di + 2 * dy
            else:
                y = y + dely
                di = di + 2 * (dy - dx)
    else:
        di = 2 * dx - dy
        for y in range(y1, y2, dely):
            if c2 is not None:
                new_c = count_grad_color(c1, c2, y, y1, y2)
            else:
                # new_c = (255, 0, 0)
                new_c = c1
            draw_pix(img, (x, y), new_c)
            if di < 0:
                di = di + 2 * dx
            else:
                x = x + delx
                di = di + 2 * (dx - dy)


def count_grad_color(c1, c2, p, p1, p2):
    '''
    Подсчитывает средний цвет на градиентном отрезке
    - c1, c2 цвета концов отрезка в RGB
    - p, p1, p2 кординаты концов отрезка и текущей точки цвет 
    которой нужно высчитать, используются для высчитывания сочетания цветов
    '''
    a = abs(p - p1) / abs(p2 - p1)
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    new_c = (delc(a, r1, r2), delc(a, g1, g2), delc(a, b1, b2))
    return new_c


def delc(a, c1, c2):
    if c1 >= c2:
        return max(min(int(c1 - a * abs(c1 - c2)), 255), 0)
    else:
        return max(min(int(a * abs(c1 - c2) + c1), 255), 0)


def rgb2hex(rgb):
    return "#%02x%02x%02x" % rgb


def draw_pix(img, point, color=(255, 0, 0)):
    img.put(rgb2hex(color), point)


def draw_shade_pix(img, point, alpha, bg, color=(255, 0, 0)):
    color = tuple(np.trunc(np.around(np.dot(alpha, color) + np.dot((1 - alpha), bg))).astype(int))
    img.put(rgb2hex(color), point)


def line_wu(img, x1, y1, x2, y2, bg, color=(255, 0, 0)):
    d_x = x2 - x1
    d_y = y2 - y1
    if d_x == 0:
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2):
            draw_pix(img, (x1, y), color)
    elif d_y == 0:
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2):
            draw_pix(img, (x, y1), color)
    elif abs(d_x) > abs(d_y):
        if x2 < x1:
            x2, x1 = x1, x2
            y2, y1 = y1, y2
        gradient = d_y / d_x
        x_end = round(x1)
        y_end = y1 + gradient * (x_end - x1)
        x_gap = 1 - (x1 + 0.5) % 1
        x_pxl1 = x_end
        y_pxl1 = int(y_end // 1)
        draw_shade_pix(img, (x_pxl1, y_pxl1), (1 - y_end % 1) * x_gap, bg, color=color)
        draw_shade_pix(img, (x_pxl1, y_pxl1 + 1), y_end % 1 * x_gap, bg, color=color)
        inter_y = y_end + gradient

        x_end = round(x2)
        y_end = y2 + gradient * (x_end - x2)
        x_gap = (x2 + 0.5) % 1
        x_pxl2 = x_end
        y_pxl2 = y_end // 1
        draw_shade_pix(img, (x_pxl2, int(y_pxl2)), (1 - y_end % 1) * x_gap, bg, color=color)
        draw_shade_pix(img, (x_pxl2, int(y_pxl2 + 1)), y_end % 1 * x_gap, bg, color=color)

        for x in range(x_pxl1 + 1, x_pxl2 - 1):
            draw_shade_pix(img, (x, int(inter_y)), 1 - inter_y % 1, bg, color=color)
            draw_shade_pix(img, (x, int(inter_y) + 1), inter_y % 1, bg, color=color)
            inter_y = inter_y + gradient
    elif abs(d_x) < abs(d_y):
        gradient = d_x / d_y
        y_end = int(y1)
        x_end = x1 + gradient * (y_end - y1)
        y_gap = 1 - (y1 + 0.5) % 1
        x_pxl1 = x_end // 1
        y_pxl1 = y_end
        draw_shade_pix(img, (int(x_pxl1), y_pxl1), (1 - y_end % 1) * y_gap, bg, color=color)
        draw_shade_pix(img, (int(x_pxl1 + 1), y_pxl1), y_end % 1 * y_gap, bg, color=color)
        inter_x = x_end + gradient

        x_end = x2 + gradient * (y_end - y2)
        y_end = int(y2)
        y_gap = (y2 + 0.5) % 1
        x_pxl2 = x_end // 1
        y_pxl2 = y_end
        draw_shade_pix(img, (int(x_pxl2), y_pxl2), (1 - y_end % 1) * y_gap, bg, color=color)
        draw_shade_pix(img, (int(x_pxl2 + 1), y_pxl2), y_end % 1 * y_gap, bg, color=color)

        for y in range(y_pxl1 + 1, y_pxl2 - 1):
            draw_shade_pix(img, (int(inter_x), y), 1 - inter_x % 1, bg, color=color)
            draw_shade_pix(img, (int(inter_x + 1), y), inter_x % 1, bg, color=color)
            inter_x = inter_x + gradient


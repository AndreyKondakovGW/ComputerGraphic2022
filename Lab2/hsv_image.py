import numpy as np
import math

class HSVImage:
    def __init__(self, rgb_pixels_arr):
        # self.rgb_pixels = rgb_pixels_arr
        self.original_hsv = self.to_hsv(rgb_pixels_arr)
        self.hsv_pixels = self.original_hsv

    def __normalize_colors(self, pixel):
        r, g, b = pixel
        return (r / 256, g / 256, b / 256)

    def __rgb_to_hsv(self, pixel):
        r, g, b = self.__normalize_colors(pixel)
        max_color = max(r, g, b)
        min_color = min(r, g, b)
        if max_color == min_color:
            h = 0
        elif max_color == r and g >= b:
            h = 60.0 * (g - b) / (max_color - min_color)
        elif max_color == r and g < b:
            h = 60.0 * (g - b) / (max_color - min_color) + 360.0
        elif max_color == g:
            h = 60.0 * (b - r) / (max_color - min_color) + 120.0
        else:
            h = 60.0 * (r - g) / (max_color - min_color) + 240.0

        s = 0 if max_color == 0 else 1 - (min_color / max_color)
        v = max_color
        return np.array([h, s, v], dtype=np.float)

    def to_hsv(self, rgb_pixels):
        return np.apply_along_axis(self.__rgb_to_hsv, 2, rgb_pixels)

    def __hsv_to_rgb(self, hsv_pixel):
        h, s, v = hsv_pixel
        h_div_60_floor = int(math.floor(h / 60)) 
        hi = h_div_60_floor % 6
        f = h / 60.0 - h_div_60_floor
        p = v * (1 - s)
        q = v * (1 - f * s)
        t = v * (1 - (1 - f) * s)
        if hi == 0:
            r = v; g = t; b = p
        elif hi == 1:
            r = q; g = v; b = p;
        elif hi == 2:
            r = p; g = v; b = t
        elif hi == 3:
            r = p; g = q; b = v
        elif hi == 4:
            r = t; g = p; b = v
        elif hi == 5:
            r = v; g = p; b = q
        return np.array([int(r * 256), int(g * 256), int(b * 256)], dtype=np.uint8)

    def to_rgb(self):
        return np.apply_along_axis(self.__hsv_to_rgb, 2, self.hsv_pixels)

    def change_hsv(self, hue, saturation, value):
        def change_hsv_pixel(pixel, hue, saturation, value):
            h, s, v = pixel
            h = (h + hue) % 360
            saturation = saturation / 100.0 # [-100; 100] => [-1; 1]
            value = value / 100.0 # [-100; 100] => [-1; 1]
            #s = min(abs(s + saturation), 1)
            #v = min(abs(v + value), 1)
            s *= (saturation + 1.0)
            s = min(max(s, 0.0), 1.0)
            if (value < 0.0):
                v *= (value + 1.0)
            else:
                v = v + (value * (1.0 - v))
            s = min(max(s, 0.0), 1.0)
            v = min(max(v, 0.0), 1.0)
            return np.array([h, s, v])

        f = lambda pixel: change_hsv_pixel(pixel, hue, saturation, value)
        self.hsv_pixels = np.apply_along_axis(f, 2, self.original_hsv)
        return self.hsv_pixels

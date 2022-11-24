import math

from src.figure import Figure


class PlotFloatingHorizon(Figure):

    def __init__(self, function, xa, xb, ya, yb, partition=30, color='magenta'):
        super().__init__(color)
        self.function = function
        self.xa = xa
        self.xb = xb
        self.ya = ya
        self.yb = yb
        self.partition = partition
        self.x_angle = 0
        self.y_angle = 0

    def change_x_angle(self, a):
        self.x_angle = a

    def change_y_angle(self, a):
        self.y_angle = a

    def draw(self, renderer):
        super().draw(renderer)
        width = renderer.canvas.width
        height = renderer.canvas.height
        scale = 100
        # массивы верхнего и нижнего горизонтов
        self.top_horizon = [float('-inf') for i in range(renderer.canvas.width)]
        self.bottom_horizon = [float('inf') for i in range(renderer.canvas.width)]

        dy = (self.yb - self.ya) / self.partition  # шаг плоскостей

        cos_x = math.cos(math.radians(self.x_angle))
        sin_x = math.sin(math.radians(self.x_angle))
        cos_y = math.cos(math.radians(self.y_angle))
        sin_y = math.sin(math.radians(self.y_angle))

        y = self.ya
        while y < self.yb:
            previous_point = (0, 0)
            pxl_x = -width // 2
            while pxl_x < width // 2:  # перебор по пикселям x
                x = (pxl_x + self.xa) / scale
                rotated_x = cos_x * y - sin_x * x
                rotated_y = sin_x * y + cos_x * x
                cx = pxl_x + width // 2
                if width > cx > 0:
                    z = cos_y * rotated_x + sin_y * self.function(rotated_x, rotated_y)
                    pxl_y = int(z * scale + height // 2)

                    if height > pxl_y > 0:
                        # если точка "выше" текущего значения при этом аргументе, значит она видимая
                        if z < self.bottom_horizon[cx]:
                            self.bottom_horizon[cx] = z
                            current_point = (cx, pxl_y)
                            d = math.sqrt(
                                (current_point[0] - previous_point[0]) ** 2 + (
                                            current_point[1] - previous_point[1]) ** 2)
                            # если точки достаточно близко - значит принадлежат одному горизонту, рисуем линию от них
                            if d < 20:
                                renderer.canvas.draw_line(previous_point, (cx, pxl_y), color=(255, 0, 255))
                            previous_point = (cx, pxl_y)
                        # если точка "ниже" текущего значения при этом аргументе, значит она видимая
                        if z > self.top_horizon[cx]:
                            self.top_horizon[cx] = z
                            current_point = (cx, pxl_y)
                            d = math.sqrt(
                                (current_point[0] - previous_point[0]) ** 2 + (
                                            current_point[1] - previous_point[1]) ** 2)
                            if d < 25:
                                renderer.canvas.draw_line(previous_point, (cx, pxl_y), color=(0, 0, 0))
                            previous_point = (cx, pxl_y)
                pxl_x += 1
            y += dy

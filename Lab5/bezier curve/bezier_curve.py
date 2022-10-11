import numpy as np


# главная функция
def draw_bezier_curve(canvas):
    points_size = len(canvas.points);
    if points_size == 4:
        curve_four_points(canvas, canvas.points[0], canvas.points[1], canvas.points[2], canvas.points[3])


# матрица безье
def bezier_matrix():
    return [[-1, 3, -3, 1],
            [3, -6, 3, 0],
            [-3, 3, 0, 0],
            [1, 0, 0, 0]]


# кривая для четырех точек
def curve_four_points(canvas, p0, p1, p2, p3):
    t = 0.0
    previous = p0
    while t < 1.0:
        next_p = next_point(p0, p1, p2, p3, t)
        canvas.create_line(previous[0], previous[1], round(next_p[0]), round(next_p[1]))  # рисуем по небольшим отрезкам
        previous = next_p
        t += 0.0001


# следующая точка кривой
def next_point(p0, p1, p2, p3, t):
    list_x = [p0[0], p1[0], p2[0], p3[0]]
    list_y = [p0[1], p1[1], p2[1], p3[1]]
    param = np.dot([t * t * t, t * t, t, 1], bezier_matrix())  # умножение матрицы безье и матрицы параметра t
    return np.dot(param, list_x), np.dot(param, list_y)

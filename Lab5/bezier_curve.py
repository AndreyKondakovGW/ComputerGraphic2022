import numpy as np


# главная функция
def draw_bezier_curve(canvas, points):
    points_size = len(canvas.points)
    if points_size == 4:
        curve_four_points(canvas, canvas.points[0], canvas.points[1], canvas.points[2], canvas.points[3])
    elif points_size > 4:
        if points_size % 2 == 0:
            splain(canvas)
        else:
            additional_point(canvas)
            splain(canvas)


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
        t += 0.01  # шаг


# следующая точка кривой
def next_point(p0, p1, p2, p3, t):
    list_x = [p0[0], p1[0], p2[0], p3[0]]
    list_y = [p0[1], p1[1], p2[1], p3[1]]
    param = np.dot([t * t * t, t * t, t, 1], bezier_matrix())  # умножение матрицы безье и матрицы параметра t
    return np.dot(param, list_x), np.dot(param, list_y)


# сплайн для более 4х точек
def splain(canvas):
    l = len(canvas.points)
    p3 = middle_point(canvas.points[2], canvas.points[3])  # невидимая точка для соединения кривых
    curve_four_points(canvas, canvas.points[0], canvas.points[1], canvas.points[2], p3)

    idx = 3
    while idx < l - 4:
        p0 = p3
        p1 = canvas.points[idx]
        p2 = canvas.points[idx + 1]
        p3 = middle_point(canvas.points[idx + 1], canvas.points[idx + 2])
        curve_four_points(canvas, p0, p1, p2, p3)
        idx += 2

    curve_four_points(canvas, p3, canvas.points[l - 3], canvas.points[l - 2], canvas.points[l - 1])


# дополнительная невидимая точка для нечетного количества точек
def additional_point(canvas):
    l = len(canvas.points)
    if canvas.ad_point is None:
        canvas.ad_point = middle_point(canvas.points[l - 2], canvas.points[l - 1])
        canvas.points.insert(l - 1, canvas.ad_point)
    else:
        canvas.points.remove(canvas.ad_point)
        canvas.ad_point = None


# нахождение точек посередине между двумя
def middle_point(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2

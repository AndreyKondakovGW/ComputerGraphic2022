import numpy as np


# главная функция
def draw_bezier_curve(canvas, points, ad_point):
    points_size = len(points)
    if points_size == 4:
        curve_four_points(canvas, points[0], points[1], points[2], points[3])
    elif points_size > 4:
        if points_size % 2 == 0:
            splain(canvas, points)
        else:
            ad_point, new_points = additional_point(canvas, points)
            splain(canvas, new_points)
    return ad_point, points


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
def splain(canvas, points):
    l = len(points)
    p3 = middle_point(points[2], points[3])  # невидимая точка для соединения кривых
    curve_four_points(canvas, points[0], points[1], points[2], p3)

    idx = 3
    while idx < l - 4:
        p0 = p3
        p1 = points[idx]
        p2 = points[idx + 1]
        p3 = middle_point(points[idx + 1], points[idx + 2])
        curve_four_points(canvas, p0, p1, p2, p3)
        idx += 2

    curve_four_points(canvas, p3, points[l - 3], points[l - 2], points[l - 1])


# дополнительная невидимая точка для нечетного количества точек
def additional_point(canvas, points, ad_point=None):
    new_points = points.copy()
    l = len(points)
    if ad_point is None:
        ad_point = middle_point(points[l - 2], points[l - 1])
        new_points.insert(l - 1, ad_point)
    else:
        new_points.remove(ad_point)
        ad_point = None
    return ad_point, new_points


# нахождение точек посередине между двумя
def middle_point(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2

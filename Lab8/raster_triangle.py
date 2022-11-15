from math import *
from Lab3.task3main import get_point_inline
from Lab3.draw_line import count_grad_color
from Lab8.point_with_color import PointWithColor

def next_point_in_line(current_p: PointWithColor, line_p1: PointWithColor, line_p2: PointWithColor):
    x, y, z = current_p.x, current_p.y, current_p.z

    x1, y1, z1 = line_p1.x, line_p1.y, line_p1.z
    x2, y2, z2 = line_p2.x, line_p2.y, line_p2.z
    
    c1 = line_p1.color
    c2 = line_p2.color

    x = x + 1

    if x > x2:
        return line_p2

    y = int((x - x1) * (y2 - y1) / (x2 - x1) + y1)
    z = int((x - x1) * (z2 - z1) / (x2 - x1) + z1)

    new_c = count_grad_color(c1, c2, x, x1, x2)
    return PointWithColor(x, y, z, new_c)

def get_vertical_line_points(p1: PointWithColor, p2: PointWithColor):
    x1, y1, z1 = p1.x, p1.y, p1.z
    x2, y2, z2 = p2.x, p2.y, p2.z
    c1 = p1.color
    c2 = p2.color

    # debug, should throw error
    # if x1 != x2:
    #     print("x1 != x2")
    #     return None

    if y1 > y2:
        y1, y2 = y2, y1
        c1, c2 = c2, c1

    res = []
    x = x1 # never changes
    y = y1
    z = z1
    c = c1
    res.append(PointWithColor(x, y, z, c))
    while y != y2:
        p, c = get_point_inline((y, z), (y1, z1), (y2, z2), c1, c2)
        y, z = p
        res.append(PointWithColor(x, y, z, c))
    
    return res        

def raster_triangle(p1: PointWithColor, p2: PointWithColor, p3: PointWithColor):
    p1, p2, p3 = sorted([p1, p2, p3], key=lambda p: p.x)
    op = next_point_in_line(p1, p1, p2)
    ap = next_point_in_line(p1, p1, p3)

    ostart = p1
    oend = p2
    astart = p1
    aend = p3

    res_points = []

    while ((op != oend) and (ap != aend)):
        vertical_line_points = get_vertical_line_points(op, ap)
        res_points.extend(vertical_line_points)

        op = next_point_in_line(op, ostart, oend)
        ap = next_point_in_line(ap, astart, aend)

        if (op == p2):
            ostart = p2
            oend = p3
            while ((ap != aend)):
                vertical_line_points = get_vertical_line_points(op, ap)
                res_points.extend(vertical_line_points)
                op = next_point_in_line(op, ostart, oend)
                ap = next_point_in_line(ap, astart, aend)
            break
        if (ap == p3):
            ostart = p3
            oend = p2
            while ((op != oend)):
                vertical_line_points = get_vertical_line_points(op, ap)
                res_points.extend(vertical_line_points)
                op = next_point_in_line(op, ostart, oend)
                ap = next_point_in_line(ap, astart, aend)
            break

    return res_points
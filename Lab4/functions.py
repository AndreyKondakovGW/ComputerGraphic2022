def find_segments_intersection(p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    p = find_lines_intersection(p1, p2, p3, p4)
    if p is not None:
        x, y = p
        if x < min(x1, x2) or x > max(x1, x2) or x < min(x3, x4) or x > max(x3, x4):
            return None
        if y < min(y1, y2) or y > max(y1, y2) or y < min(y3, y4) or y > max(y3, y4):
            return None
        return p
    else:
        return None


def find_rayseg_intersection(ray1, ray2, seg1, seg2):
    x1, y1 = ray1
    x2, y2 = ray2
    x3, y3 = seg1
    x4, y4 = seg2
    p = find_lines_intersection(ray1, ray2, seg1, seg2)
    if p is not None:
        x, y = p
        # Check if intersection is on the ray
        if x1 <= x2 and x < x1:
            return None
        if y1 <= y2 and y < y1:
            return None

        # Check if intersection is on the segment
        if x < min(x3, x4) or x > max(x3, x4) or y < min(y3, y4) or y > max(y3, y4):
            return None
        return p
    else:
        return None


def find_lines_intersection(p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if d == 0:
        return None
    x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / d
    y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / d
    return (x, y)


def point_in_rect(p, p1, p2):
    x, y = p
    x1, y1 = p1
    x2, y2 = p2
    if x < min(x1, x2) or x > max(x1, x2) or y < min(y1, y2) or y > max(y1, y2):
        return False
    return True


def intersection_with_scope(f, canv):
    return f.find_intersec((0, 0), (0, canv.height)) \
           or f.find_intersec((0, 0), (canv.width, 0)) \
           or f.find_intersec((0, canv.height), (canv.width, canv.height)) \
           or f.find_intersec((canv.width, 0), (canv.width, canv.height))

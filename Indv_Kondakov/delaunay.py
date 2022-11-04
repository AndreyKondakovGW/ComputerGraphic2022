from Lab4.functions import point_from_right
import time

def get_leftmost_edge(points):
    left_point = points[0]
    for point in points:
        if point.x < left_point.x:
            left_point = point
        elif point.x == left_point.x:
            if point.y > left_point.y:
                left_point = point

    min_dot = 10000000
    for p in points:
        if left_point.dot(p) < min_dot and p != left_point:
            min_dot = left_point.dot(p)
            second_point = p
    return [left_point, second_point]

def triangulate_delaunay(points):
    start_edge = get_leftmost_edge(points)
    live_edges = [start_edge]
    dead_edges = []
    triangles = []
    while len(live_edges) > 0:
        edge = live_edges.pop()
        dead_edges.append(edge)
        right_points = find_all_right_points(edge, points)
        if len(right_points) != 0:
            next_p = find_right_conjugate_p(edge, right_points)
            triangles.append([edge[0], edge[1], next_p])
            if point_from_right(edge[0], edge[1], next_p):
                if [edge[0], next_p] not in live_edges and [edge[0], next_p] not in dead_edges:
                    live_edges.append([edge[0], next_p])
                if [next_p, edge[1]] not in live_edges and [next_p, edge[1]] not in dead_edges:
                    live_edges.append([next_p, edge[1]])
            else:
                if [edge[1], next_p] not in live_edges and [edge[1], next_p] not in dead_edges:
                    live_edges.append([edge[1], next_p])
                if [next_p, edge[0]] not in live_edges and [next_p, edge[0]] not in dead_edges:
                    live_edges.append([next_p, edge[0]])
    return triangles

def triangulate_delaunay_auto(points, canvas, sleep = 1):
    start_edge = get_leftmost_edge(points)
    live_edges = [start_edge]
    dead_edges = []
    triangles = []
    while len(live_edges) > 0:
        canvas.redraw()
        for edge in live_edges:
            canvas.draw_line((edge[0].x, edge[0].y), (edge[1].x, edge[1].y), (255, 0, 0))
        canvas.update()
        time.sleep(sleep)
        edge = live_edges.pop()
        dead_edges.append(edge)
        
        right_points = find_all_right_points(edge, points)
        if len(right_points) != 0:
            next_p = find_right_conjugate_p(edge, right_points)
            triangles.append([edge[0], edge[1], next_p])
            if point_from_right(edge[0], edge[1], next_p):
                if [edge[0], next_p] not in live_edges and [edge[0], next_p] not in dead_edges:
                    live_edges.append([edge[0], next_p])
                if [next_p, edge[1]] not in live_edges  and [next_p, edge[1]] not in dead_edges:
                    live_edges.append([next_p, edge[1]])
            else:
                if [edge[1], next_p] not in live_edges and [edge[1], next_p] not in dead_edges:
                    live_edges.append([edge[1], next_p])
                if [next_p, edge[0]] not in live_edges and [next_p, edge[0]] not in dead_edges:
                    live_edges.append([next_p, edge[0]])
        else:
            pass
    return triangles

def find_all_right_points(edge, points):
    right_points = []
    for point in points:
        if point != edge[0] and point != edge[1]:
            if point_from_right(point, edge[0], edge[1]):
                right_points.append(point)
    return right_points

def find_right_conjugate_p(edge, right_points):
    min_cos = 10000000
    for p in right_points:
        a = edge[0].distance(edge[1])
        b = edge[0].distance(p)
        c = edge[1].distance(p)
        cos = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)

        if cos < min_cos:
            min_cos = cos
            conjugate_p = p
    return conjugate_p
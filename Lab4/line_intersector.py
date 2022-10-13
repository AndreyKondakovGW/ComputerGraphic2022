
def draw_intersections_with_line(canvas, p0, p1):
    intersections = canvas.storage.call(lambda f: f.find_intersec(p0, p1))

    for p in intersections:
        canvas.draw_circle(p[0], p[1])
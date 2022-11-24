from src.point import Point
def get_next_y(x, p1, p2):
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y
    dely = 1 if y2 - y1 > 0 else -1
    x = x + 1
    y = int((x - x1) * (y2 - y1) / (x2 - x1) + y1)

    if x > x2:
        x = x2
    if y*dely > y2*dely:
        y = y
    return Point(x, y)

def draw_vert_line(canvas, p1, p2):
    x1, y1 = int(p1.x), int(p1.y)
    x2, y2 = p2.x, int(p2.y)

    if y1 > y2:
        y1, y2 = y2, y1
    for i in range(y1, y2):
        canvas.put_pixel(round(x1),round(i), (255, 0, 0))

class Texture_Renderer:
    def __init__(self, canvas, camera):
        self.canvas = canvas
        self.camera = camera

    def apply_texture(self, face_points2d, face_texture2d):
        min_x = self.canvas.width + 1
        max_x = -1
        p0_index = 0
        for i in range(len(face_points2d)):
            if face_points2d[i].x < min_x:
                min_x = face_points2d[i].x
                p0_index = i
            if face_points2d[i].x > max_x:
                max_x = face_points2d[i].x
        p01 = face_points2d[p0_index]
        p02 = p01
        i1 = (p0_index + 1) % len(face_points2d)
        i2 = ((p0_index - 1) + len(face_points2d)) % len(face_points2d)
        p1 = face_points2d[i1]
        p2 = face_points2d[i2]

        max_x = int(max_x)
        min_x = int(min_x)
        d1 = p01
        d2 = p02
        for x in range(min_x, max_x + 1):
            if x == p1.x:
                p01 = p1
                i1 = (i1 + 1) % len(face_points2d)
                p1 = face_points2d[i1]
                draw_vert_line(self.canvas, p1, d2)
                continue
            if x == p2.x:
                p02 = p2
                i2 = (i2 - 1 + len(face_points2d)) % len(face_points2d)
                p2 = face_points2d[i2]
                draw_vert_line(self.canvas, d1, p2)
                continue
            d1 = get_next_y(x, p01, p1)
            d2 = get_next_y(x, p02, p2)
            draw_vert_line(self.canvas, d1, d2)





        
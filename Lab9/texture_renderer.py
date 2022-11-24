from src.point import Point

def interpalate_texture_cord(y, u1, u2):
    u3 = (u1 + u2) / 2

    a0 = u1
    a1 = -3 * u1 - u2 + 4 * u3
    a2 = 2 * u1 + 2 * u2 - 4 * u3

    return a0 + a1 * y + a2 * y * y

def lininterp_texture_cord(x, p1, p2, uv1, uv2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    step_u = (uv2[0] - uv1[0]) / (x2 - x1 + 1)
    step_v = (uv2[1] - uv1[1]) / (x2 - x1 + 1)

    u = uv1[0] + step_u * (x - x1)
    v = uv1[1] + step_v * (x - x1)

    return u, v



def get_y(x, p1, p2):
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y

    if x1 == x2:
        return y2
    dely = 1 if y2 - y1 > 0 else -1
    y = int((x - x1) * (y2 - y1) / (x2 - x1) + y1)

    if y*dely > y2*dely:
        y = y
    return y

def get_color(uv, texture):
    x = int(uv[0] * (texture.shape[1] - 1))
    y = int(uv[1] * (texture.shape[0] - 1))
    return texture[y][x][:3]

def draw_vert_line(canvas, x, y1, y2,x1,x2, uv1, uv2, texture):
    if y1 > y2:
        y1, y2 = y2, y1
        uv1, uv2 = uv2, uv1
    for i in range(int(y1), int(y2) + 1):
        uv = lininterp_texture_cord(i, (y1,x1), (y2,x2), uv1, uv2)
        """ (interpalate_texture_cord((x1 - x) / (x1 - x2+ 10**-5), uv1[0], uv2[0]),
            interpalate_texture_cord((y1 - i) / (y1-y2+ 10**-5), uv1[1], uv2[1])) """
        color = get_color(uv, texture)
        canvas.put_pixel(round(x),round(i), color)

def raster_triangle_texture(canvas,points, t_points, texture):
    ftp1, ftp2, ftp3 = sorted(zip(points,t_points), key=lambda p: p[0].x)
    p1, p2, p3 = ftp1[0], ftp2[0], ftp3[0]
    t1, t2, t3 = ftp1[1], ftp2[1], ftp3[1]
    d2 = p1.y
    d1 = p1.y
    uv1 = t1[0]
    uv2 = t1[0]
    for x in range(int(p1.x), int(p3.x) + 1):
        if x < p2.x:
            d1 = get_y(x, p1, p2)
            uv1 = lininterp_texture_cord(x, (p1.x,p1.y), (p2.x,p2.y), t1, t2)
            """ (interpalate_texture_cord((p1.x - x) / (p1.x - p3.x+ 10**-5), t1[0], t2[0]),
                interpalate_texture_cord((p1.y - d1) / (p1.y - p2.y + 10**-5), t1[1], t2[1])) """
        elif x > p2.x:
            d1 = get_y(x, p2, p3)
            uv1 = lininterp_texture_cord(x, (p2.x,p2.y), (p3.x,p3.y), t2, t3)
            """ uv1 = (interpalate_texture_cord((p2.x - x) / (p2.x - p3.x+ 10**-5), t2[0], t3[0]),
                interpalate_texture_cord((p2.y - d1) / (p2.y - p3.y+ 10**-5), t2[1], t3[1])) """
        else:
            d1 = p2.y
            uv1 = t2
        
        d2 = get_y(x, p1, p3)
        uv2 = lininterp_texture_cord(x, (p1.x,p1.y), (p3.x,p3.y), t1, t3)
        # uv2 = (interpalate_texture_cord((p1.x - x) / (p1.x - p3.x+ 10**-5), t1[0], t3[0]),
        #     interpalate_texture_cord((p1.y - d2) / (p1.y - p3.y+ 10**-5), t1[1], t3[1]))
        draw_vert_line(canvas,x, d1, d2, p1.x, p3.x, uv1, uv2, texture)


class Texture_Renderer:
    def __init__(self, canvas, camera):
        self.canvas = canvas
        self.camera = camera

    def apply_texture(self, face_points2d, texture):
        left_point_index = 0
        for i in range(1, len(face_points2d)):
            if face_points2d[i].x < face_points2d[left_point_index].x:
                left_point_index = i
        p0 = face_points2d[left_point_index]
        p1 = face_points2d[(left_point_index + 1) % len(face_points2d)]
        p2 = face_points2d[(left_point_index + 2) % len(face_points2d)]
        p3 = face_points2d[(left_point_index + 3) % len(face_points2d)]
        if len(face_points2d) == 4:
            raster_triangle_texture(self.canvas,
                [p0, p1, p2], [(0,1), (1,1),(1,0)], texture)
            raster_triangle_texture(self.canvas, [p0,p3,p2], [(0,1), (0,0),(1,0)], texture)
        elif len(face_points2d) == 3:
            raster_triangle_texture(self.canvas,
                [p0, p1, p2], [(0,1), (0.5,0),(1,1)], texture)
        else:
            print("Error: face has more than 4 points")





        
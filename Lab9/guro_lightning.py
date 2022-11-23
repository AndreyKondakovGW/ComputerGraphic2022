def guro_lightning(point, point_color, light_source):
    light_direction = light_source.point - point
    # light_direction = point - light_source.point
    light_direction = light_direction.normalize()
    cos_phi = light_direction.dot(point.normal)
    if cos_phi > 1.0:
        cos_phi = 1.0
    if cos_phi < 0.0:
        cos_phi = 0.0
    r = int(point_color[0] * cos_phi)
    g = int(point_color[1] * cos_phi)
    b = int(point_color[2] * cos_phi)
    return (r, g, b)

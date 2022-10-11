def rgb2hex(rgb):
    return "#%02x%02x%02x" % rgb


def draw_pix(img, point, color=(255, 0, 0)):
    img.put(rgb2hex(color), point)

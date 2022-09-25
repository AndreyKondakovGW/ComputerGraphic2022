
def draw_line(img, p1, p2, c1, c2, gradient=False):
    '''
    Функция рисования отрезка используя алгоритм Брезенхэма
    - p1, p2  координаты концов отрезка
    - c1, c2  цвета в формате RGB
    - gradient флаг градиентного закрашивания
    если true то отрезок закрашивается градиентом от цвета c1 к цвету c2
    иначе закрашивается красным 
    '''
    x1, y1 = p1
    x2, y2 = p2
    y = y1
    x = x1
    dy = abs(y2 - y1)
    dx = abs(x2 - x1)
    grad = dy / (dx + 0.000001)
    dely = 1 if y2 - y1 > 0 else -1
    delx = 1 if x2 - x1 > 0 else -1

    if grad <= 1:
        di = 2*dy - dx
        for x in range(x1, x2, delx):
            if gradient:
                new_c = count_grad_color(c1, c2, x, x1, x2)
            else:
                new_c = (255, 0, 0)
            draw_pix(img, (x,y), new_c)
            if di < 0:
                di = di + 2*dy
            else:
                y = y + dely
                di = di + 2*(dy - dx)
    else:
        di = 2*dx - dy
        for y in range(y1, y2, dely):
            if gradient:
                new_c = count_grad_color(c1, c2, y, y1, y2)
            else:
                new_c = (255, 0, 0)
            draw_pix(img, (x,y), new_c)
            if di < 0:
                di = di + 2*dx
            else:
                x = x + delx
                di = di + 2*(dx - dy)

def count_grad_color(c1, c2, p, p1, p2):
    '''
    Подсчитывает средний цвет на градиентном отрезке
    - c1, c2 цвета концов отрезка в RGB
    - p, p1, p2 кординаты концов отрезка и текущей точки цвет 
    которой нужно высчитать, используются для высчитывания сочетания цветов
    '''
    a = abs(p - p1) / abs(p2 - p1)
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    new_c = (delc(a, r1, r2), delc(a, g1, g2), delc(a, b1, b2))
    return new_c

def delc(a, c1, c2):
    if c1 >= c2:
        return (abs(int(c1 - a * abs(c1 - c2))) + 255) % 255
    else:
        return (abs(int(a * abs(c1 - c2) + c1)) + 255) % 255

def rgb2hex(rgb):
    return "#%02x%02x%02x" % rgb

def draw_pix(img, point, color=(255, 0, 0)):
    img.put(rgb2hex(color), point)

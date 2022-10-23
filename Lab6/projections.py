from math import sin, cos, pi

def simple2D_projection():
    return [[1, 0,0,0],[0, 1,0,0],[0, 0,0,0], [0, 0,0,1]]

def perspective_projection(r = 0.005): # r = 1 / c 
    return [[1, 0,0,0],[0, 1,0,0],[0, 0,0,r], [0, 0,0,1]]

def corner_projection(p = 0.01, q = 0.01):
    return [[1, 0,0,p],[0, 1,0,q],[0, 0,0,0], [0, 0,0,1]]

def akso_projection(f = (pi / 5), m = -(pi / 4)):
    # m  поворот y, f  поворот x
    return [[cos(m), sin(m)*sin(f),0,0],
            [0     , cos(f)       ,0,0],
            [sin(m),-cos(m)*sin(f),0,0],
            [0     ,0             ,0,1]]
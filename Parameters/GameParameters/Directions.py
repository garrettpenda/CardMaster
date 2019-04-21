# coding: utf-8

# DO ENUM INSTEAD OF CLASS ?
class Directions(object):
    
    LU = 0      # LU - U - RU
    U = 1       # |         |
    RU = 2      # |         |
    R = 3       # L         R
    RD = 4      # |         |
    D = 5       # |         |
    LD = 6      # LD - D - RD
    L = 7
    all_directions = [LU, U, RU, R, RD, D, LD, L]


def get_opposite_diretion(number):
    if number == Directions.LU:
        return Directions.RD
    elif number == Directions.U:
        return Directions.D
    elif number == Directions.RU:
        return Directions.LD
    elif number == Directions.R:
        return Directions.L
    elif number == Directions.RD:
        return Directions.LU
    elif number == Directions.D:
        return Directions.U
    elif number == Directions.LD:
        return Directions.RU
    elif number == Directions.L:
        return Directions.R
    else:
        raise Exception

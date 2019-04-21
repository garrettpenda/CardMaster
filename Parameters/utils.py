# coding: utf-8

from random import randint
import pygame

#============
# functions
#============

def Coin():
    return bool(randint(0,1))

def RectCenter(x, y, w, h):
    rect = pygame.Rect(0, 0, w, h)
    rect.center = (x, y)
    return rect


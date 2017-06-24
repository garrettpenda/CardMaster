from random import randint
import pygame
from pygame.locals import *
from Parameters import *
import time

#============
# functions
#============

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(fenetre, msg, x, y, w, h, icolor, acolor, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(fenetre, acolor, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(fenetre, icolor, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    fenetre.blit(textSurf, textRect)

def clickButtonToContinue(message, fenetre):
    hasClickedOnButton = False

    label = pygame.font.SysFont("monospace", 20).render(message, 10, black)
    fenetre.blit(label, (buttonpx + 25, buttonpy +50 ))
    pygame.draw.rect(fenetre, red, pygame.Rect(buttonpx, buttonpy, buttonwidth, buttonheight),2)
    pygame.display.flip()
    while not hasClickedOnButton:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                click_x = event.pos[0]
                click_y = event.pos[1]
                if click_x >= buttonpx and click_x <= buttonpx + buttonwidth and click_y >= buttonpy and click_y <= buttonpy+buttonheight:
                    hasClickedOnButton = True


def Coin():
    # TODO animation de la piece si true
    return bool(randint(0,1))

def getX(number,x):
    if number == 0:
        return x-1
    elif number == 1 :
        return x
    elif number == 2:
        return x+1
    elif number == 3:
        return x+1
    elif number == 4:
        return x+1
    elif number == 5:
        return x
    elif number == 6:
        return x-1
    elif number == 7:
        return x-1

def getY(number,y):
    if number == 0:
        return y-1
    elif number == 1 :
        return y-1
    elif number == 2:
        return y-1
    elif number == 3:
        return y
    elif number == 4:
        return y+1
    elif number == 5:
        return y+1
    elif number == 6:
        return y+1
    elif number == 7:
        return y


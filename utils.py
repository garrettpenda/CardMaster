from random import randint
import math
import time
import pygame
from pygame.locals import *
from Parameters import *

#============
# functions
#============

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

def drawGame(board,fenetre):
    fenetre.fill(white)
    pygame.draw.rect(fenetre, black, pygame.Rect(0, 0, cardwidth, cardheight),2)
    pygame.draw.rect(fenetre, black, pygame.Rect(197, 97, 4*(cardwidth+10)+3, 4*(cardheight+10)+3),2)
    for line in board.board:
        for case in line:
            if not case.crushed:
                pygame.draw.rect(fenetre, black, pygame.Rect(200+(case.x)*(cardwidth+10), 100+(case.y)*(cardheight+10), cardwidth+6, cardheight+6),2)
            if case.occupied:
                case.inside.draw(fenetre)

    for handplaces in range(0,5):

        pygame.draw.rect(fenetre, black, pygame.Rect(100, 50+handplaces*(cardheight+10), cardwidth+6, cardheight+6),2)
        pygame.draw.rect(fenetre, black, pygame.Rect(500, 50+handplaces*(cardheight+10), cardwidth+6, cardheight+6),2)

    for player in board.players:
        for card in player.cards:
            card.draw(fenetre)
    scoresLabel = pygame.font.SysFont("monospace", 20).render(board.players[0].name + " " + str(board.players[0].score) + "  /  " + str(board.players[1].score) + " " + board.players[1].name, 10, black)
    
    roundsLabel = pygame.font.SysFont("monospace", 20).render(board.players[0].name + " " + str(board.players[0].round) + "  /  " + str(board.players[1].round) + " " + board.players[1].name, 10, black)
    fenetre.blit(scoresLabel, (250, 80))
    fenetre.blit(roundsLabel, (250, 50))
    pygame.display.flip()


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


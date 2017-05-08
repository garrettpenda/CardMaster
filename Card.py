from random import randint
import pygame
from pygame.locals import *
from utils import *

class Card(object):

    def __init__(self,n,player,number,color):
	self.number = number
	self.x=None
	self.y=None
	self.px = 103 + (player-1)*400
	self.py = 53 + (number-1)*(cardheight+10)
	self.player = player
        self.color = color
	self.name = str(self.number) + str(self.player)[0]
	self.arrows = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0}
	self.LP = 20-2*n
	self.maxLP = self.LP
	self.isSelected = False
	numberArrows = 0
	while numberArrows != n:
	    random = randint(0, 7)
	    if self.arrows[random]==0:
	         numberArrows += 1
	         self.arrows[random]=1

    def __repr__(self):
	string = "+-------+\n"
	string += "| " + str(self.arrows[0]) + " " + str(self.arrows[1]) + " " + str(self.arrows[2]) + " |\n"
	string += "| " + str(self.arrows[7]) + " " + str(self.player) + " " + str(self.arrows[3]) + " |\n"
	string += "| " + str(self.arrows[6]) + " " + str(self.arrows[5]) + " " + str(self.arrows[4])+ " |\n"
	string += "+-------+\n"
	string += "| "+ str(self.LP).zfill(2) +"/"+ str(self.maxLP).zfill(2) +" |\n"
	string += "+-------+\n"
	return string

    def changePlayer(self,player,color):
	self.player = player
	self.color = color

    def reborn(self):
	self.LP = (self.maxLP)/2

    def fight(self,otherCard):
	print self.name + " fights " + otherCard.name
	attack = True
	if not(self.player==otherCard.player):
	    while(self.LP != 0 and otherCard.LP != 0 ):
		if(attack):
		    otherCard.LP -= 1
		    attack = not attack
		else:
		    self.LP -= 1
		    attack = not attack
	    if self.LP == 0:
		self.reborn() 
		self.changePlayer(otherCard.player, otherCard.color)
		return False
	    else:
		otherCard.reborn()
		otherCard.changePlayer(self.player, self.color)
		return True

    def getName(self):
	return self.name+"("+str(self.LP).zfill(2)+"/"+str(self.maxLP).zfill(2)+self.player

    def draw(self,fenetre):
        pygame.draw.rect(fenetre, self.color, pygame.Rect(self.px, self.py, cardwidth, cardheight))
        for number in self.arrows.keys():
            if (self.arrows[number]==1):
    	       self.drawArrow(fenetre,number)
        label = pygame.font.SysFont("monospace", 20).render(str(self.LP), 10, white)
        fenetre.blit(label, (self.px+cardwidth/2-10, self.py+cardheight/2-10))
	if self.isSelected:
	    pygame.draw.rect(fenetre, red, pygame.Rect(self.px, self.py, cardwidth, cardheight),3)

    def drawArrow(self,fenetre,number):
        if(number == 0):
	    X = self.px+2
	    Y = self.py+2
	    pygame.draw.polygon(fenetre, white, [[X, Y], [X+5, Y], [X, Y+5]], 0)
        if(number == 1):
	    X = self.px+cardwidth/2
	    Y = self.py+2
	    pygame.draw.polygon(fenetre, white, [[X, Y], [X+r2, Y+r2], [X-r2, Y+r2]], 0)
        if(number == 2):
	    X = self.px+cardwidth-2
	    Y = self.py+2
	    pygame.draw.polygon(fenetre, white, [[X, Y], [X-5, Y], [X, Y+5]], 0)
        if(number == 3):
	    X = self.px+cardwidth-2
	    Y = self.py+cardheight/2
	    pygame.draw.polygon(fenetre, white, [[X, Y], [X-r2, Y+r2], [X-r2, Y-r2]], 0)
        if(number == 4):
	    X = self.px+cardwidth-2
	    Y = self.py+cardheight-2
	    pygame.draw.polygon(fenetre, white, [[X, Y], [X-5, Y], [X, Y-5]], 0)
        if(number == 5):
	    X = self.px+cardwidth/2
	    Y = self.py+cardheight-2
	    pygame.draw.polygon(fenetre, white, [[X, Y], [X+r2, Y-r2], [X-r2, Y-r2]], 0)
        if(number == 6):
	    X = self.px+2
	    Y = self.py+cardheight-2
	    pygame.draw.polygon(fenetre, white, [[X, Y], [X+5, Y], [X, Y-5]], 0)
        if(number == 7):
	    X = self.px+2
	    Y = self.py+cardheight/2
	    pygame.draw.polygon(fenetre, white, [[X, Y], [X+r2, Y+r2], [X+r2, Y-r2]], 0)

	



import pygame
from pygame.locals import *
from Hand import *
from utils import *
from Player import *

pygame.init()
pygame.display.set_caption("Card Master")
fenetre = pygame.display.set_mode((640, 640))
fenetre.fill(white)
myfont = pygame.font.SysFont("monospace", 20)
pygame.display.flip()

is_blue = True
card_x = 30
card_y = 30
selected = False

testcard = Card(4,1,4,black)
testcard.px = 50
testcard.py = 50
print testcard

garrett = Player("Garrett",1,black)
print garrett.hand
joueur2 = Player("p2",2,blue)
print joueur2.hand

pygame.key.set_repeat(400, 30)
continuer = 1

def selectCard(x,y):
    return x > card_x and x < card_x+cardwidth and y > card_y and y < card_y+cardheight

def cursorOnBoard(x,y):
    return x > 200 and x < 200+cardwidth*4 and y > 100 and y < 100+cardheight*4

def getCaseX(x):
    return  203 + int((x-200)/cardwidth)*(cardwidth+10)

def getCaseY(y):
    return 103 + int((y-100)/cardheight)*(cardheight+10)

while continuer:

    for event in pygame.event.get():   

        if event.type == QUIT:

            continuer = 0

	if event.type == pygame.MOUSEMOTION:

	    cursor_x = event.pos[0]
            cursor_y = event.pos[1]

        if event.type == MOUSEBUTTONDOWN:

	    if event.button == 1:

                click_x = event.pos[0]
                click_y = event.pos[1]

		if(selectCard(click_x,click_y)):
		    selected = not selected

		if (selected and cursorOnBoard(click_x,click_y)):
		    selected = False
		    testcard.px = getCaseX(click_x)
		    testcard.py = getCaseY(click_y)

	if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

            is_blue = not is_blue

    fenetre.fill(white)
    for row in range(0,4):
	for collum in range (0,4):
	    pygame.draw.rect(fenetre, black, pygame.Rect(200+row*(cardwidth+10), 100+collum*(cardheight+10), cardwidth+6, cardheight+6),2)

    for handplaces in range(0,5):

	pygame.draw.rect(fenetre, black, pygame.Rect(100, 50+handplaces*(cardheight+10), cardwidth+6, cardheight+6),2)
	garrett.hand.cards[handplaces].px = 103
	garrett.hand.cards[handplaces].py = 53 + handplaces*(cardheight+10)
	garrett.hand.cards[handplaces].draw(fenetre)

	pygame.draw.rect(fenetre, black, pygame.Rect(500, 50+handplaces*(cardheight+10), cardwidth+6, cardheight+6),2)
	joueur2.hand.cards[handplaces].px = 503
	joueur2.hand.cards[handplaces].py = 53 + handplaces*(cardheight+10)
	joueur2.hand.cards[handplaces].draw(fenetre)
    

    if (is_blue):
	color = blue
	contour = red
    else:
	color = red
	contour = blue

    testcard.draw(fenetre)

    if (selected):
	pygame.draw.rect(fenetre, contour, pygame.Rect(testcard.px, testcard.py, cardwidth, cardheight),3)

	if (cursorOnBoard(cursor_x,cursor_y)):
	    selected_x = getCaseX(cursor_x)
	    selected_y = getCaseY(cursor_y)
	    pygame.draw.rect(fenetre, contour, pygame.Rect(selected_x, selected_y, cardwidth, cardheight),2)

    label2 = myfont.render(str(selected), 10, black)
    fenetre.blit(label2, (50, 250))
    label3 = myfont.render(str(card_x), 10, black)
    fenetre.blit(label3, (50, 270))
    label4 = myfont.render(str(card_y), 10, black)
    fenetre.blit(label4, (50, 290))

    
    pygame.display.flip()

















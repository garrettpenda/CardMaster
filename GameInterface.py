import pygame
from pygame.locals import *
from Hand import *
from utils import *
from Player import *
from Board import *


# TODO le choix des cartes a combattre
# TODO le menu
# TODO les animations
# TODO l'affichage des scores et des étapes
# TODO masquer les cartes du joueur non actif

pygame.init()
pygame.display.set_caption("Elementz")
fenetre = pygame.display.set_mode((640, 640))
fenetre.fill(white)
myfont = pygame.font.SysFont("monospace", 20)
pygame.display.flip()

cursor_x = 0
cursor_y = 0
selected = False
cardSelected = None

table = Board(4)
garrett = Player("Garrett",1,purple)
joueur2 = Player("p2",2,blue)

allPlayers = []
allPlayers.append(garrett) 
allPlayers.append(joueur2) 
activePlayerNumber = 1
activePlayer = allPlayers[activePlayerNumber-1]

pygame.key.set_repeat(400, 30)
continuer = 1

def selectCard(x,y,player):
    for card in player.hand.cards:
	if x > card.px and x < card.px+cardwidth and y > card.py and y < card.py+cardheight:
	    if card.isSelected :
		card.isSelected = not card.isSelected
		cardSelected = None
	    else :
		for cardtochange in player.hand.cards:
		    cardtochange.isSelected = False
	        card.isSelected = True
		cardSelected = card
    for card in player.hand.cards:
	if card.isSelected:
	    return True
    return False

def getSelectedCard(player):
    for card in player.hand.cards:
	if card.isSelected:
	    return card
    return None

def cursorOnBoard(x,y):
    return x > 203 and x < 203+(cardwidth+10)*4 and y > 103 and y < 103+(cardheight+10)*4

def getCaseX(x):
    return  203 + int((x-203)/(cardwidth+10))*(cardwidth+10)

def getCaseY(y):
    return 103 + int((y-103)/(cardheight+10))*(cardheight+10)

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

		selected = selectCard(click_x,click_y,activePlayer)
		cardSelected = getSelectedCard(activePlayer);

		if (selected and cursorOnBoard(click_x,click_y)):
		    
		    X = int((click_x-203)/(cardwidth+10))
		    Y = int((click_y-103)/(cardheight+10))
		    card = activePlayer.hand.getCard(cardSelected.number)
		    cardIsPlayed = table.play(card,X,Y)
		    if not cardIsPlayed:
	    		activePlayer.hand.addCard(card)
		    else:
			selected = False
			cardSelected = None
			activePlayerNumber = 3-activePlayerNumber
			activePlayer = allPlayers[activePlayerNumber-1]

	if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

            print "functions make details or stuff maybe"

    fenetre.fill(white)
    pygame.draw.rect(fenetre, black, pygame.Rect(0, 0, cardwidth, cardheight),2)
    pygame.draw.rect(fenetre, black, pygame.Rect(197, 97, 4*(cardwidth+10)+3, 4*(cardheight+10)+3),2)
    for line in table.board:
	for case in line:
	    if not case.crushed:
	        pygame.draw.rect(fenetre, black, pygame.Rect(200+(case.x)*(cardwidth+10), 100+(case.y)*(cardheight+10), cardwidth+6, cardheight+6),2)
	    if case.occupied:
		case.inside.draw(fenetre)

    for handplaces in range(0,5):

	pygame.draw.rect(fenetre, black, pygame.Rect(100, 50+handplaces*(cardheight+10), cardwidth+6, cardheight+6),2)
	pygame.draw.rect(fenetre, black, pygame.Rect(500, 50+handplaces*(cardheight+10), cardwidth+6, cardheight+6),2)

    for card in garrett.hand.cards:
	card.draw(fenetre)

    for card in joueur2.hand.cards:
	card.draw(fenetre)

    if (selected):

	if (cursorOnBoard(cursor_x,cursor_y)):
	    selected_x = getCaseX(cursor_x)
	    selected_y = getCaseY(cursor_y)
	    pygame.draw.rect(fenetre, red, pygame.Rect(selected_x, selected_y, cardwidth, cardheight),2)

    label2 = myfont.render(str(getCaseX(cursor_x)), 10, black)
    fenetre.blit(label2, (50, 250))
    label3 = myfont.render(str(getCaseY(cursor_y)), 10, black)
    fenetre.blit(label3, (50, 270))
    label4 = myfont.render(str(cursor_x), 10, black)
    fenetre.blit(label4, (50, 290))
    label4 = myfont.render(str(cardSelected), 10, black)
    fenetre.blit(label4, (50, 310))

    pygame.display.flip()

















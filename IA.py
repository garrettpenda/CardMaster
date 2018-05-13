from Player import *
from Board import *
from utils import *

def playrandomcard(table, player, fenetre):

    random_card = randint(0, len(player.cards)-1)
    number = player.cards[random_card].number
    card = player.getCard(number)
    
    card_is_played = False
    while not card_is_played:
	X = randint(0, size_of_board-1)
	Y = randint(0, size_of_board-1) 
    	card_is_played = auto_play(table,card, X, Y, fenetre)
    table.nextPlayerTurn()

    
def auto_play(table, card,X,Y,fenetre):
    if not (table.board[Y][X].occupied or table.board[Y][X].crushed) :
	table.board[Y][X].add(card)
	cardIsOK = True
	# fights
	fights = table.getFights(card)
	while len(fights)!=0:
	    if len(fights)>1:
		number = fights[randint(0,len(fights)-1)]
	    elif len(fights)==1:
		number = fights[0]

	    if number in fights:
		X = getX(number,card.x)
		Y = getY(number,card.y)
		cardIsOK = card.fight(table.get(X,Y),table,fenetre)
		# combos
		if cardIsOK:
		    table.combo(table.get(X,Y),fenetre) 
		    fights = table.getFights(card)
		else:
		    table.combo(card,fenetre)
		    fights = []
                    
	# attacks
	if cardIsOK:
	    table.attack(card)
	table.actualizeScores()
	return True    
    else :
	table.draw_message(text_case_occupied,fenetre)
	table.actualizeScores()
	return False




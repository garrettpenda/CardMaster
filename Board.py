from Card import *
from Case import *
from utils import *


class Board(object):

    def __init__(self,size):
	self.size = size
	self.board = []
        self.rocksOnBoard = 0
        self.numberOfRocks = 0
	print "Definition du plateau de jeu."

	for y in range(size):
	    line = []
	    for x in range(size):
		line.append( Case(y,x) )
	    self.board.append(line)

	if False:#Coin():
	    self.numberOfRocks = randint(1, 6)
	    print "Number of rock(s) is " + str(self.numberOfRocks) + "."
	else :
	    print "No rocks for this game."
	
	while self.rocksOnBoard != self.numberOfRocks:
	    randomX = randint(0, 3)
	    randomY = randint(0, 3)
	    if not self.board[randomY][randomX].crushed:
	         self.rocksOnBoard+=1
	         self.board[randomY][randomX].crush()

    def __repr__(self):
        for Y in range(len(self.board)):
	    line1 = ""
	    line2 = ""
	    line3 = ""
	    line4 = ""
	    line5 = "  "
	    for X in range(len(self.board[Y])):
		line4 += "  |               "
		line5 += "+-----+-----+-----"
		if (not self.board[Y][X].occupied) or self.board[Y][X].crushed:
		    line1 += "  |  " + str(self.board[Y][X])
		    line2 += "  |  " + str(self.board[Y][X]) 
		    line3 += "  |  " + str(self.board[Y][X])
		else:
		    line1 += "  |  " + str(self.board[Y][X].inside.arrows[0])
		    line1 += "     " + str(self.board[Y][X].inside.arrows[1])
		    line1 += "     " + str(self.board[Y][X].inside.arrows[2])
		    line2 += "  |  " + str(self.board[Y][X].inside.arrows[7])
		    line2 += "   " + str(self.board[Y][X].inside.LP).zfill(2) + " P" + str(self.board[Y][X].inside.player)
		    line2 += "   " + str(self.board[Y][X].inside.arrows[3])
		    line3 += "  |  " + str(self.board[Y][X].inside.arrows[6])
		    line3 += "     " + str(self.board[Y][X].inside.arrows[5])
		    line3 += "     " + str(self.board[Y][X].inside.arrows[4])
	    line1 += "  |" 
	    line2 += "  |" 
	    line3 += "  |"
	    line4 += "  |"
	    line5 += "+"
	    print line5
	    print line1
	    print line4
	    print line2
	    print line4
	    print line3
	print line5
	return ""

    def get(self,X,Y):
	 return self.board[Y][X].inside

    def outOfBoard(self,number,card):
	upperlimit = len(self.board)-1
        if number == 0 and card.x!=0 and card.y!=0:
	    return False
        elif number == 1 and card.y!=0:
	    return False
        elif number == 2 and card.x!=upperlimit and card.y!=0:
	    return False
        elif number == 3 and card.x!=upperlimit:
	    return False
        elif number == 4 and card.x!=upperlimit and card.y!=upperlimit:
	    return False
        elif number == 5 and card.y!=upperlimit:
	    return False
        elif number == 6 and card.x!=0 and card.y!=upperlimit:
	    return False
        elif number == 7 and card.x!=0:
	    return False
        return True

    def getFights(self,card):
	fights = []
	for number in card.arrows.keys():
	    if card.arrows[number] == 1 and not self.outOfBoard(number,card):
		X = getX(number,card.x)
		Y = getY(number,card.y)
		if self.board[Y][X].occupied and self.get(X,Y).player != card.player:
		    if self.get(X,Y).arrows[(number+4)%8]==1:
			fights.append(number)
	return fights

    def combo(self,card):
	for number in card.arrows.keys():
	    if card.arrows[number] == 1 and not self.outOfBoard(number,card):
		X = getX(number,card.x)
		Y = getY(number,card.y)
		if self.board[Y][X].occupied and self.get(X,Y).player != card.player:
		    self.get(X,Y).changePlayer(card.player, card.color)

    def attack(self,card):
	for number in card.arrows.keys():
	    if card.arrows[number] == 1 and not self.outOfBoard(number,card):
		X = getX(number,card.x)
		Y = getY(number,card.y)
		if self.board[Y][X].occupied and self.get(X,Y).player != card.player:
		    if self.get(X,Y).arrows[(number+4)%8]==0:
			self.get(X,Y).changePlayer(card.player, card.color)

    def play(self,card,X,Y):
	if not (self.board[Y][X].occupied or self.board[Y][X].crushed) :
	    print "The player " + str(card.player) + " played the card number " + str(card.number) + " on (" + str(X) + "," + str(Y) + ")."
	    self.board[Y][X].add(card)
	    cardIsOK = True
	    # fights
	    fights = self.getFights(card)
	    while len(fights)!=0:
		if len(fights)>1:
		    print fights
		    number = int(raw_input("Choose the fight : "))
		elif len(fights)==1:
		    number = fights[0]

		if number in fights:
		    X = getX(number,card.x)
		    Y = getY(number,card.y)
		    cardIsOK = card.fight(self.get(X,Y))
		    # combos
		    if cardIsOK:
			self.combo(self.get(X,Y)) 
			fights = self.getFights(card)
		    else:
			self.combo(card)
			fights = []
		else :
		    print "you must choose a card to fight baltringue"
	    # attacks
	    if cardIsOK:
		self.attack(card)
		
	    return True    
	else :
	    print "This case is occupied or crushed."
	    return False




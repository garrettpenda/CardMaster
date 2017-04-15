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

	if Coin():
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

    #0 for fights
    #1 for combos
    #2 for attacks
    def interractions(self,card,fca):
	interractions = []
	for number in card.arrows.keys():
	    if card.arrows[number] == 1 and not outOfBoard(number,card):
		X = getX(number,card.x)
		Y = getY(number,card.y)
		if self.board[Y][X].occupied and self.get(X,Y).player != card.player:
		    if self.get(X,Y).arrows[(number+4)%8]==1 and fca==0:
			interractions.append(number)
		    elif fca == 1:
			self.get(X,Y).changePlayer(card.player)
		    elif self.get(X,Y).arrows[(number+4)%8]==0 and fca==2:
			self.get(X,Y).changePlayer(card.player)
	return interractions

    def play(self,card,X,Y):
	if not (self.board[Y][X].occupied or self.board[Y][X].crushed) :
	    print "The player " + str(card.player) + " played the card number " + str(card.number) + " on (" + str(X) + "," + str(Y) + ")."
	    self.board[Y][X].add(card)
	    cardIsOK = True
	    # fights
	    fights = self.interractions(card,0)
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
			self.interractions(self.get(X,Y),1) 
			fights = self.interractions(card,0)
		    else:
			self.interractions(card,1)
			fights = []
		else :
		    print "you must choose a card to fight baltringue"
	    # attacks
	    if cardIsOK:
		self.interractions(card,2)
		
	    return True    
	else :
	    print "This case is occupied or crushed."
	    return False




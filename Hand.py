from Card import *

class Hand(object):
    
    def __init__(self,player):
	print " hand for player " + str(player)
	self.cards = []
	self.player = player
	arrows1 = randint(1, 2)
	card1 = Card(arrows1,player,1)
	self.cards.append(card1)

	arrows2 = randint(2, 4)
	card2 = Card(arrows2,player,2)
	self.cards.append(card2)

	arrows3 = randint(3, 6)
	card3 = Card(arrows3,player,3)
	self.cards.append(card3)

	card4 = Card(4,player,4)
	self.cards.append(card4)

	arrows5 = 18 - (4 + arrows1+ arrows2+arrows3)
	card5 = Card(arrows5,player,5)
	self.cards.append(card5)

    def getCard(self,number):
	if number > 5 or number < 1:
	    print "number is wrong"
	else:
	    for x in range(len(self.cards)):
		if self.cards[x].number == number:
		     return self.cards.pop(x)
	    print "The player " + str(self.player) + " doesn't have the card number " + str(number) + " on his/her hand."

    def addCard(self,card):
	self.cards.append(card)

    def __repr__(self):
	line0 = ""
	line1 = ""
	line2 = ""
	line3 = ""
	line4 = ""
	line5 = ""
	for card in self.cards:
	    line0 += " |   " + str(card.number) + "   |"
	    line1 += " | " + str(card.arrows[0]) + " " + str(card.arrows[1]) + " " + str(card.arrows[2]) + " |"
	    line2 += " | " + str(card.arrows[7]) + "   " + str(card.arrows[3]) + " |"
	    line3 += " | " + str(card.arrows[6]) + " " + str(card.arrows[5]) + " " + str(card.arrows[4]) + " |"
	    line4 += " | "+ str(card.LP).zfill(2) +"/"+ str(card.maxLP).zfill(2) + " |"
	    line5 += " +-------+"
	return line5 + "\n" + line0 + "\n" + line5 + "\n" + line1 + "\n" + line2 + "\n" + line3 + "\n" + line5 + "\n" + line4 + "\n" + line5

    def hidden(self):
	line1 = ""
	line2 = ""
	for card in self.cards:
	    line1 += " +-------+"
	    line2 += " |       |"
	print line1 + "\n" + line2 + "\n" + line2 + "\n" + line2 + "\n" + line1 + "\n" + line2 + "\n" + line1






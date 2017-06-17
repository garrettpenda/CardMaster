from Card import *
from utils import *

class Player(object):

    def __init__(self,name,number,color):
        self.name = name
        self.number = number
        self.color = color
        # golem, phenix, epee, source, elementaire
        self.cards = []
        arrows1 = 2 #randint(1, 2)
        self.cards.append(Card(arrows1, number, 1, color))
        arrows2 = randint(2, 4)
        self.cards.append(Card(arrows2, number, 2, color))
        arrows3 = randint(3, 6)
        self.cards.append(Card(arrows3, number, 3, color))
        self.cards.append(Card(4, number, 4, color))
        arrows5 = 18 - (4 + arrows1+ arrows2+arrows3)
        self.cards.append(Card(arrows5, number, 5, color))

        self.score = 0
        self.round = 0

    def resetHand(self):
        self.cards = []
        arrows1 = randint(1, 2)
        self.cards.append(Card(arrows1, self.number, 1, self.color))
        arrows2 = randint(2, 4)
        self.cards.append(Card(arrows2, self.number, 2, self.color))
        arrows3 = randint(3, 6)
        self.cards.append(Card(arrows3, self.number, 3, self.color))
        self.cards.append(Card(4, self.number, 4, self.color))
        arrows5 = 18 - (4 + arrows1+ arrows2+arrows3)
        self.cards.append(Card(arrows5, self.number, 5, self.color))

    def changeColor(self):
        number = int(raw_input("1 for red, 2 for blue, 3 for green, 4 for black, 5 for yellow and 6 for purple."))
        self.color = allColors(number)

    def selectCard(self,x,y):
        for card in self.cards:
            if card.isClickedOn(x,y):
                if card.isSelected :
                    card.isSelected = not card.isSelected
                    cardSelected = None
                else :
                    for cardtochange in self.cards:
                        cardtochange.isSelected = False
                    card.isSelected = True
                    cardSelected = card
        for card in self.cards:
            if card.isSelected:
                return True
        return False

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

    def getSelectedCard(self):
        for card in self.cards:
            if card.isSelected:
                return card
        return None

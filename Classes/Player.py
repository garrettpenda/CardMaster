from Card import *
from utils import *



class Player(object):

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.number = None
        self.surrender_game = False
        self.surrender_round = False
        self.cards = []
        self.score = 0
        self.round = 0

    def reset_hand(self):
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

    def __repr__(self):
        return str(self.__dict__)

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

    def set_number(self, number):
        self.number = number

    def getCard(self,number):
        if number > 5 or number < 1:
            print "number is wrong"
        else:
            for x in range(len(self.cards)):
                if self.cards[x].number == number:
                     return self.cards.pop(x)
            print "The player " + str(self.name) + " doesn't have the card number " + str(number) + " on his/her hand."

    def addCard(self,card):
        self.cards.append(card)

    def getSelectedCard(self):
        for card in self.cards:
            if card.isSelected:
                return card
        return None


    def draw(self, screen, card_hidden):

        position = self.number

        # name
        test = pygame.font.SysFont("monospace", 20).render(str(self.name), 10, black)

        screen.blit(test, (225 + position*450, 20))

        # score

        test = pygame.font.SysFont("monospace", 20).render(str(self.score), 10, black)

        screen.blit(test, (225 + position*450, 35))

        # cards in hands
        if card_hidden:
            for card in self.cards:
                card.draw_hidden(screen)
        else:
            for card in self.cards:
                card.draw(screen)


def build_player_from_json(json_data):
    player = Player(json_data['name'], json_data['color'])
    player.number = json_data['number']
    for number in range(1,6):
        card = Card(0, player.number, number, player.color)
        card.set_positions()
        player.cards.append(card)
    return player


ia_player = Player("creator", purple)

if __name__ == '__main__':
    player = build_player_from_json(eval("{'name': 'kebab', 'number': 1, 'color': (255, 0, 0)}"))

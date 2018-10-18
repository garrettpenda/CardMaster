from Player import *
from Case import *
from utils import *
from Card import *
import pygame


class Board(object):

    def __init__(self, size, screen):
        self.screen = screen
        self.rocksOnBoard = 0
        self.numberOfRocks = 0
        self.init_board(size)
        self.message = pygame.font.SysFont("monospace", 20).render('',10, black)

    def init_board(self, size):
        self.size = size
        self.board = [[Case(y,x) for x in range(size)] for y in range(size)]
    
    def set_rocks_on_board(self):

        self.numberOfRocks = randint(1, 6)
        
        while self.rocksOnBoard != self.numberOfRocks:
            randomX = randint(0, self.size-1)
            randomY = randint(0, self.size-1)
            if not self.board[randomY][randomX].crushed:
                 self.rocksOnBoard+=1
                 self.board[randomY][randomX].crush()

    def get(self,X,Y):
        return self.board[Y][X].inside

    def crush(self, X, Y):
        self.board[Y][X].crush()

    def outOfBoard(self,number,card):
        upperlimit = self.size-1
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
            if card.arrows[number] and not self.outOfBoard(number,card):
                X = getX(number,card.x)
                Y = getY(number,card.y)
                if self.board[Y][X].occupied and self.get(X,Y).player != card.player:
                    if self.get(X,Y).arrows[(number+4)%8]:
                        fights.append(number)
        return fights

    def combo(self,card):
        cardsAndColors = []
        for number in card.arrows.keys():
            if card.arrows[number] and not self.outOfBoard(number,card):
                X = getX(number,card.x)
                Y = getY(number,card.y)
                if self.board[Y][X].occupied and self.get(X,Y).player != card.player:
                    cardsAndColors.append([self.get(X,Y),self.get(X,Y).color])
                    self.get(X,Y).changePlayer(card.player, card.color)

        # animation pour les combo ici
        for i in range(1,5):
            for cardandcolor in cardsAndColors:
                cardandcolor[0].color = cardandcolor[1]
            time.sleep( animationTime )
            self.draw_board()
            for cardandcolor in cardsAndColors:
                cardandcolor[0].color = card.color
            time.sleep( animationTime )
            self.draw_board()

    def attack(self,card):
        for number in card.arrows.keys():
            if card.arrows[number] and not self.outOfBoard(number,card):
                X = getX(number,card.x)
                Y = getY(number,card.y)
                if self.board[Y][X].occupied and self.get(X,Y).player != card.player:
                    if not self.get(X,Y).arrows[(number+4)%8]:
                        self.get(X,Y).changePlayer(card.player, card.color)

    def play(self,card,X,Y, order):
        order_fights = []
        self.board[Y][X].add(card)
        cardIsOK = True
        # fights
        fights = self.getFights(card)
        while len(fights)!=0:
            if len(fights)>1:
                if order is not None:
                    number = order[0]
                    order.pop(0)
                else:
                    number = self.chooseCardToFight(fights,card)
                    order_fights.append(number)
            elif len(fights)==1:
                number = fights[0]

            if number in fights:
                X = getX(number,card.x)
                Y = getY(number,card.y)
                cardIsOK = self.fight(card, self.get(X,Y))
                # combos
                if cardIsOK:
                    self.combo(self.get(X,Y))
                    fights = self.getFights(card)
                else:
                    self.combo(card)
                    fights = []
        # attacks
        if cardIsOK:
            self.attack(card)
        return order_fights

    def draw_message(self, message):
        self.message = pygame.font.SysFont("monospace", 20).render(message, 10, black)
        self.draw_board()

    def fight(self, card, otherCard):
        attack = True
        if not(card.player==otherCard.player):
            while(card.LP != 0 and otherCard.LP != 0 ):
                if(attack):
                    otherCard.LP -= 1
                    attack = not attack
                    time.sleep( animationTime )
                    self.draw_board()
                else:
                    card.LP -= 1
                    attack = not attack
                    time.sleep( animationTime )
                    self.draw_board()
            if card.LP == 0:
                card.reborn()
                card.changePlayer(otherCard.player, otherCard.color)
                self.draw_board()
                return False
            else:
                otherCard.reborn()
                otherCard.changePlayer(card.player, card.color)
                self.draw_board()
                return True

    def chooseCardToFight(self, fights, card):
        self.draw_message(text_choose_card_to_fight)
    
        # trouver les cartes
        allCardsToFight = []
        for number in fights:
            X = getX(number,card.x)
            Y = getY(number,card.y)
            allCardsToFight.append([self.get(X,Y), number])
        # les afficher
        for cardAndNumber in allCardsToFight :
            cardToFight = cardAndNumber[0]
            pygame.draw.rect(self.screen, red, pygame.Rect(cardToFight.px, cardToFight.py, cardwidth, cardheight),2)
        pygame.display.flip()
        # en choisir une
        hasSelectACardToFight = False
        number = None
        while not hasSelectACardToFight:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    click_x = event.pos[0]
                    click_y = event.pos[1]
                    for cardAndNumber in allCardsToFight :
                        cardToFight = cardAndNumber[0]
                        if cardToFight.isClickedOn(click_x,click_y):
                            hasSelectACardToFight = True
                            number = cardAndNumber[1]
        return number

    def draw_board(self):
        pygame.draw.rect(self.screen, white, pygame.Rect(board_px, board_py,
                             size_of_board * (cardwidth + card_extern_interval) + boarding,
                             size_of_board * (cardheight + card_extern_interval) + boarding))
        pygame.draw.rect(self.screen, black, pygame.Rect(board_px, 
                             board_py,
                             size_of_board * (cardwidth + card_extern_interval) + boarding,
                             size_of_board * (cardheight + card_extern_interval) + boarding), border)
        for line in self.board:
            for case in line:
                if case.crushed:
                    pygame.draw.rect(self.screen, black, pygame.Rect(board_px + (case.x) * (cardwidth + card_extern_interval) + boarding,
                                                               board_py + (case.y) * (cardheight + card_extern_interval) + boarding,
                                                               cardwidth + 2*card_intern_interval,
                                                               cardheight + 2*card_intern_interval))
                else:
                    pygame.draw.rect(self.screen, black, pygame.Rect(board_px + (case.x) * (cardwidth + card_extern_interval) + boarding,
                                 board_py + (case.y) * (cardheight + card_extern_interval) + boarding,
                                                          cardwidth + 2*card_intern_interval,
                                 cardheight + 2*card_intern_interval), border)
                    if case.occupied:
                        case.inside.draw(self.screen)

        self.screen.blit(self.message, (200, 680))
        pygame.display.update()

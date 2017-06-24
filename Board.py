
from Case import *
from utils import *


class Board(object):

    def __init__(self,size,players):
        self.size = size
        self.board = []
        self.players = players
	self.activePlayerNumber = randint(0,len(self.players)-1)
	self.activePlayer = self.players[self.activePlayerNumber]
        self.rocksOnBoard = 0
        self.numberOfRocks = 0

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
            randomX = randint(0, self.size-1)
            randomY = randint(0, self.size-1)
            # TODO animation de case qui disparaissent
            if not self.board[randomY][randomX].crushed:
                 self.rocksOnBoard+=1
                 self.board[randomY][randomX].crush()

        self.actualizeScores()

    def nextPlayerTurn(self):
        self.activePlayerNumber = (self.activePlayerNumber+1) % len(self.players)
        self.activePlayer = self.players[self.activePlayerNumber]

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
            if card.arrows[number] == 1 and not self.outOfBoard(number,card):
                X = getX(number,card.x)
                Y = getY(number,card.y)
                if self.board[Y][X].occupied and self.get(X,Y).player != card.player:
                    if self.get(X,Y).arrows[(number+4)%8]==1:
                        fights.append(number)
        return fights

    def combo(self,card,fenetre):
        cardsAndColors = []
        for number in card.arrows.keys():
            if card.arrows[number] == 1 and not self.outOfBoard(number,card):
                X = getX(number,card.x)
                Y = getY(number,card.y)
                if self.board[Y][X].occupied and self.get(X,Y).player != card.player:
                    cardsAndColors.append([self.get(X,Y),self.get(X,Y).color])
                    self.get(X,Y).changePlayer(card.player, card.color)
        for i in range(1,5):
            for cardandcolor in cardsAndColors:
                cardandcolor[0].color = cardandcolor[1]
            time.sleep( animationTime )
            self.drawGame(fenetre)
            for cardandcolor in cardsAndColors:
                cardandcolor[0].color = card.color
            time.sleep( animationTime )
            self.drawGame(fenetre)

    def attack(self,card):
        for number in card.arrows.keys():
            if card.arrows[number] == 1 and not self.outOfBoard(number,card):
                X = getX(number,card.x)
                Y = getY(number,card.y)
                if self.board[Y][X].occupied and self.get(X,Y).player != card.player:
                    if self.get(X,Y).arrows[(number+4)%8]==0:
                        self.get(X,Y).changePlayer(card.player, card.color)

    def play(self,card,X,Y,fenetre):
        if not (self.board[Y][X].occupied or self.board[Y][X].crushed) :
            self.board[Y][X].add(card)
            cardIsOK = True
            # fights
            fights = self.getFights(card)
            while len(fights)!=0:
                if len(fights)>1:
                    print fights
                    number = self.chooseCardToFight(fenetre,fights,card)
                    #number = int(raw_input("Choose the fight : "))
                elif len(fights)==1:
                    number = fights[0]

                if number in fights:
                    X = getX(number,card.x)
                    Y = getY(number,card.y)
                    cardIsOK = card.fight(self.get(X,Y),self,fenetre)
                    # combos
                    if cardIsOK:
                        self.combo(self.get(X,Y),fenetre) 
                        fights = self.getFights(card)
                    else:
                        self.combo(card,fenetre)
                        fights = []
                else :
                    print "you must choose a card to fight baltringue"
            # attacks
            if cardIsOK:
                self.attack(card)
            self.actualizeScores()
            return True    
        else :
            print "This case is occupied or crushed."
            self.actualizeScores()
            return False

    def actualizeRounds(self,fenetre):
        winner = self.players[0]
        for player in self.players:
            if player.score > winner.score:
                winner = player
        if winner.score > 5:
            winner.round = winner.round + 1
            clickButtonToContinue("The player " + winner.name + " win the round.", fenetre)

    def actualizeScores(self):
        for player in self.players:
            player.score = 0
        for line in self.board:
            for case in line:
                if case.occupied:
                    for player in self.players:
                        if case.inside.player == player.number:
                            player.score = player.score+1

    def chooseCardToFight(self,fenetre,fights,card):
        # trouver les cartes
        self.drawGame(fenetre)
        allCardsToFight = []
        for number in fights:
            X = getX(number,card.x)
            Y = getY(number,card.y)
            allCardsToFight.append([self.get(X,Y),number])
        # les afficher
        for cardAndNumber in allCardsToFight :
            cardToFight = cardAndNumber[0]
            pygame.draw.rect(fenetre, red, pygame.Rect(cardToFight.px, cardToFight.py, cardwidth, cardheight),2)
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

    def allHandsAreEmpty(self):
        for player in self.players:
            if not len(player.cards)==0:
                return False
        return True

    def aPlayerWonTheGame(self, fenetre):
        for player in self.players:
            if player.round == 2:
                return True
        return False


    def drawGame(self, fenetre):
        fenetre.fill(white)
        pygame.draw.rect(fenetre, black, pygame.Rect(0, 0, cardwidth, cardheight), 2)
        pygame.draw.rect(fenetre, black, pygame.Rect(197, 97, 4 * (cardwidth + 10) + 3, 4 * (cardheight + 10) + 3), 2)
        for line in self.board:
            for case in line:
                if not case.crushed:
                    pygame.draw.rect(fenetre, black,
                                     pygame.Rect(200 + (case.x) * (cardwidth + 10), 100 + (case.y) * (cardheight + 10),
                                                 cardwidth + 6, cardheight + 6), 2)
                if case.occupied:
                    case.inside.draw(fenetre)

        for handplaces in range(0, 5):
            pygame.draw.rect(fenetre, black,
                             pygame.Rect(100, 50 + handplaces * (cardheight + 10), cardwidth + 6, cardheight + 6), 2)
            pygame.draw.rect(fenetre, black,
                             pygame.Rect(500, 50 + handplaces * (cardheight + 10), cardwidth + 6, cardheight + 6), 2)

        for player in self.players:
            for card in player.cards:
                card.draw(fenetre)
        scoresLabel = pygame.font.SysFont("monospace", 20).render(
            self.players[0].name + " " + str(self.players[0].score) + "  /  " + str(self.players[1].score) + " " +
            self.players[1].name, 10, black)

        roundsLabel = pygame.font.SysFont("monospace", 20).render(
            self.players[0].name + " " + str(self.players[0].round) + "  /  " + str(self.players[1].round) + " " +
            self.players[1].name, 10, black)
        fenetre.blit(scoresLabel, (250, 80))
        fenetre.blit(roundsLabel, (250, 50))
        pygame.display.update()





from Case import *
from utils import *


class Board(object):

    def __init__(self,size,players):
        self.size = size
        self.board = []
        self.players = players
        self.active_player_number = randint(0,len(self.players)-1)
        self.active_player = self.players[self.active_player_number]
        self.active_player_name = self.players[self.active_player_number].name
        self.rocksOnBoard = 0
        self.numberOfRocks = 0
	self.message = pygame.font.SysFont("monospace", 20).render('kebab',10, black)

        for y in range(size):
            line = []
            for x in range(size):
                line.append( Case(y,x) )
            self.board.append(line)

        if Coin():
            self.numberOfRocks = randint(1, 6)
        
        while self.rocksOnBoard != self.numberOfRocks:
            randomX = randint(0, self.size-1)
            randomY = randint(0, self.size-1)
            if not self.board[randomY][randomX].crushed:
                 self.rocksOnBoard+=1
                 self.board[randomY][randomX].crush()

        self.actualizeScores()

    def nextPlayerTurn(self):
        self.active_player_number = (self.active_player_number+1) % len(self.players)
        self.active_player = self.players[self.active_player_number]
	self.active_player_name = self.players[self.active_player_number].name
	

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
		    number = self.chooseCardToFight(fenetre,fights,card)
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
                    
            # attacks
            if cardIsOK:
                self.attack(card)
            self.actualizeScores()
            return True    
        else :
	    self.draw_message(text_case_occupied,fenetre)
            self.actualizeScores()
            return False

    def actualizeRounds(self, fenetre):
	
	scores = {}
	for player in [p for p in self.players if not p.surrender_round]:
	    scores[player] = player.score
	draw = not len(scores)==1 and all(scores.values()[0] == item for item in scores.values())
	
	if draw:
	   clickButtonToContinue(text_draw, fenetre)
	else:
	    winner = max(scores, key=lambda key: scores[key])
	    winner.round += 1
	    self.draw_message(text_player_won_round % winner.name, fenetre)
            clickButtonToContinue(text_continue, fenetre)


    def actualizeScores(self):
        for player in self.players:
            player.score = 0
        for line in self.board:
            for case in line:
                if case.occupied:
                    for player in self.players:
                        if case.inside.player == player:
                            player.score = player.score+1

    def draw_message(self, message, fenetre):
	self.message = pygame.font.SysFont("monospace", 20).render(message, 10, black)
	self.drawGame(fenetre)

    def chooseCardToFight(self,fenetre,fights,card):
	self.draw_message(text_choose_card, fenetre)
	
        # trouver les cartes
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

    def aPlayerWonTheGame(self):
        for player in self.players:
            if player.round == rounds_to_win:
                return True
        return False

    def only_one_active_player(self):
        return len([p for p in self.players if not p.surrender_round]) == 1

    def capitulate_round(self):
	self.active_player.score = 0
	self.active_player.cards = []
	self.active_player.surrender_round = True
	for line in self.board:
	    for case in line:
		if case.occupied and case.inside.player == self.active_player:
		    case.crush()


    def drawGame(self, fenetre):
        fenetre.fill(white)
        pygame.draw.rect(fenetre, black, pygame.Rect(board_px, 
						     board_py,
						     size_of_board * (cardwidth + card_extern_interval) + boarding,
						     size_of_board * (cardheight + card_extern_interval) + boarding), border)
        for line in self.board:
            for case in line:
                if case.crushed:
                    pygame.draw.rect(fenetre, black, pygame.Rect(board_px + (case.x) * (cardwidth + card_extern_interval) + boarding,
                                                      		 board_py + (case.y) * (cardheight + card_extern_interval) + boarding,
                                                      		 cardwidth + 2*card_intern_interval,
                                                      		 cardheight + 2*card_intern_interval))
                else:
                    pygame.draw.rect(fenetre, black, pygame.Rect(board_px + (case.x) * (cardwidth + card_extern_interval) + boarding,
								 board_py + (case.y) * (cardheight + card_extern_interval) + boarding,
                                                 		 cardwidth + 2*card_intern_interval,
								 cardheight + 2*card_intern_interval), border)
                    if case.occupied:
                        case.inside.draw(fenetre)

        for handplaces in range(0, 5):
            pygame.draw.rect(fenetre, black, pygame.Rect(hand_p1_px,
							 hand_p1_py + handplaces * (cardheight + card_extern_interval),
							 cardwidth + 2*card_intern_interval,
							 cardheight + 2*card_intern_interval), border)
            pygame.draw.rect(fenetre, black, pygame.Rect(hand_p2_px,
					 		 hand_p2_py + handplaces * (cardheight + card_extern_interval),
							 cardwidth + 2*card_intern_interval,
							 cardheight + 2*card_intern_interval), border)

        for player in self.players:
	    if self.active_player == player:
            	for card in player.cards:
                    card.draw(fenetre)
	    else:
		for card in player.cards:
		    card.draw_hidden(fenetre)

        scoresLabel = pygame.font.SysFont("monospace", 20).render(
            self.players[0].name + " " + str(self.players[0].score) + "  /  " + str(self.players[1].score) + " " +
            self.players[1].name, 10, black)

        roundsLabel = pygame.font.SysFont("monospace", 20).render(
            self.players[0].name + " " + str(self.players[0].round) + "  /  " + str(self.players[1].round) + " " +
            self.players[1].name, 10, black)
        fenetre.blit(scoresLabel, (250, 80))
        fenetre.blit(roundsLabel, (250, 50))

	button(fenetre, text_capitulate_round, buttonpx - 250, buttonpy, self.active_player.color, black, self.capitulate_round )

	fenetre.blit(self.message, (200, 680))

        pygame.display.update()




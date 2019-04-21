# coding: utf-8

import time

from Exceptions.BoardExceptions import *
from GameClasses.Card import *
from GameClasses.Case import *
from Parameters.GameParameters.Directions import *
from Parameters.GameParameters.GameParameters import animation_time, animationTime


class Board(object):

    # PROPERTIES

    # CONSTRUCTORS

    def __init__(self, game, size_x, size_y , rocks=False):

        # add the game in parameter mostly to display message
        self.game = game
        self.screen = self.game.screen

        self.rocksOnBoard = 0
        self.numberOfRocks = 0
        self.init_board(size_x, size_y)

        if rocks:
            self.set_rocks_on_board()

    # FUNCTIONS

    def init_board(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.rect = pygame.Rect(0, 0,
                                self.size_x * case_width + (self.size_x-1) * card_extern_interval + 2*boarding,
                                self.size_y * case_height + (self.size_y-1) * card_extern_interval + 2*boarding)
        self.rect.center = (board_px, board_py)

        self.table = [[Case(x, y, self.rect.x, self.rect.y, self.screen) for x in range(size_x)] for y in range(size_y)]

    def set_rocks_on_board(self):

        # remplacer le nombre max par le
        # nombre de cases -  (le nombre de carte en main * le nombre de joueur )
        self.numberOfRocks = randint(1, 6)
        
        while self.rocksOnBoard != self.numberOfRocks:
            randomX = randint(0, self.size_x-1)
            randomY = randint(0, self.size_y-1)
            if not self.get_case(randomX, randomY).is_crushed:
                 self.rocksOnBoard+=1
                 self.get_case(randomX, randomY).crush()

    def get_case(self, X, Y):
        upperlimit_x = self.size_x - 1
        upperlimit_y = self.size_y - 1
        if (X < 0 or X > upperlimit_x):
            raise OutOfBoardException("Invalid X")
        if (Y < 0 or Y > upperlimit_y):
            raise OutOfBoardException("Invalid Y")
        if self.table is None:
            raise InvalidBoardException("Board is None")
        if len(self.table) != self.size_y:
            raise InvalidBoardException()
        if len(self.table[0]) != self.size_x:
            raise InvalidBoardException()
        case = self.table[Y][X]
        if not isinstance(case, Case) or Case is None:
            raise InvalidBoardException()

        return case

    def out_of_board(self, direction, origin_case):
        upperlimit_x = self.size_x - 1
        upperlimit_y = self.size_y - 1
        if direction == Directions.LU and origin_case.x > 0 and origin_case.y > 0:
            return False
        elif direction == Directions.U and origin_case.y > 0:
            return False
        elif direction == Directions.RU and origin_case.x < upperlimit_x and origin_case.y > 0:
            return False
        elif direction == Directions.R and origin_case.x < upperlimit_x:
            return False
        elif direction == Directions.RD and origin_case.x < upperlimit_x and origin_case.y < upperlimit_y:
            return False
        elif direction == Directions.D and origin_case.y < upperlimit_y:
            return False
        elif direction == Directions.LD and origin_case.x > 0 and origin_case.y < upperlimit_y:
            return False
        elif direction == Directions.L and origin_case.x > 0:
            return False
        return True

    def crush(self, X, Y):
        self.get_case(X, Y).crush()

    def get_player_score(self, player_number):
        score = 0
        for line in self.table:
            for case in line:
                if case.is_occupied() and case.inside.player == player_number:
                        score +=1
        return score

    # GAME FUNCTIONS

    def play(self, card, selected_case, order):

        order_fights = []

        selected_case.put(card)

        card_has_won_fight = True
        # fights
        fight_directions = self.get_fight_directions(selected_case)

        while len(fight_directions) != 0:

            direction = self.choose_direction(fight_directions, selected_case, order)
            order_fights.append(direction)

            opposite_card = self.get_opponent_card_in_direction(direction, selected_case)
            if opposite_card is None:
                raise Exception

            card_has_won_fight = self.fight(card, opposite_card)

            # combos
            if card_has_won_fight:
                opposite_case = self.get_case_in_direction(direction, selected_case)
                self.combo(opposite_case)
                fight_directions = self.get_fight_directions(selected_case)
            else:
                self.combo(selected_case)
                fight_directions = []

        # attacks
        if card_has_won_fight:
            self.attack(selected_case)
        # usefull for online game
        return order_fights

    def get_fight_directions(self, case):

        fights = []
        card = case.inside

        for direction in card.get_arrows_directions():
            opposite_card = self.get_opponent_card_in_direction(direction, case)
            if opposite_card is not None \
                    and opposite_card.player != card.player\
                    and opposite_card.arrows[get_opposite_diretion(direction)]:
                fights.append(direction)
        return fights

    def choose_direction(self, fight_directions, case, order):

        if len(fight_directions) > 1:
            if order is not None:
                direction = order.pop(0)
                if direction not in fight_directions:
                    raise Exception
                return direction
            else:
                return self.choose_card_to_fight(fight_directions, case)

        elif len(fight_directions) == 1:
            return fight_directions[0]

    def choose_card_to_fight(self, fights_direction, case):

        self.game.message.text_key = text_choose_card_to_fight

        self.game.draw()

        # trouver les cartes
        all_cards_to_fight = {}

        for direction in fights_direction:
            case_to_fight = self.get_case_in_direction(direction, case)
            if not case_to_fight:
                raise Exception
            case_to_fight.is_selected = True
            all_cards_to_fight[direction] = case_to_fight

        self.draw()

        while True: # ARGH !!
            # ADD a check to raise an error if no card are selected ?

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click_x = event.pos[0]
                    click_y = event.pos[1]
                    for direction, case_item in all_cards_to_fight.items():
                        if case_item.is_cursor_on(click_x, click_y):
                            self.unselect_all_cases()
                            return direction

    def combo(self, case):
        if case.is_crushed or not case.is_occupied():
            return

        card = case.inside
        cards_to_combo = []
        combo_directions = []
        for direction in card.get_arrows_directions():
            opposite_card = self.get_opponent_card_in_direction(direction, case)
            if opposite_card is not None:
                combo_directions.append(direction)
                cards_to_combo.append(opposite_card)
                opposite_card.combo_color = card.color
                opposite_card.combo_direction = get_opposite_diretion(direction)

        # arrow animation
        change = True
        for i in range(0, 10):
            if change:
                for direction in combo_directions:
                    card.arrows[direction].color = black
            else:
                for direction in combo_directions:
                    card.arrows[direction].color = white
            time.sleep(animationTime)
            self.draw()
            change = not change

        # combo animation
        if cards_to_combo:
            for i in range(0, 101):
                for othercard in cards_to_combo:
                    othercard.combo_percent = i
                time.sleep(animation_time)
                self.draw()

        # finaly, change card player
        for othercard in cards_to_combo:
            othercard.reset_combo()
            othercard.change_player(card.player, card.color)
        self.draw()

    def attack(self, case):

        if case.is_crushed or not case.is_occupied():
            return

        card = case.inside

        for direction in card.get_arrows_directions():
            opposite_card = self.get_opponent_card_in_direction(direction, case)
            if opposite_card is not None:
                if not opposite_card.arrows[get_opposite_diretion(direction)]:
                    opposite_card.change_player(card.player, card.color)

    def fight(self, card, otherCard):
        attack = True
        if card.player == otherCard.player:
            raise Exception

        while(card.life_point != 0 and otherCard.life_point != 0):
            if(attack):
                otherCard.life_point -= 1
                attack = not attack
                time.sleep( animationTime )
                self.draw()
            else:
                card.life_point -= 1
                attack = not attack
                time.sleep( animationTime )
                self.draw()
        if card.life_point == 0:
            card.reborn()
            card.change_player(otherCard.player, otherCard.color)
            self.draw()
            return False
        else:
            otherCard.reborn()
            otherCard.change_player(card.player, card.color)
            self.draw()
            return True

    def get_case_in_direction(self, direction, origin_case):

        if self.out_of_board(direction, origin_case):
            return None

        if direction == Directions.LU:
            return self.get_case(origin_case.x - 1, origin_case.y - 1)
        elif direction == Directions.U:
            return self.get_case(origin_case.x, origin_case.y - 1)
        elif direction == Directions.RU:
            return self.get_case(origin_case.x + 1, origin_case.y - 1)
        elif direction == Directions.R:
            return self.get_case(origin_case.x + 1, origin_case.y)
        elif direction == Directions.RD:
            return self.get_case(origin_case.x + 1, origin_case.y + 1)
        elif direction == Directions.D:
            return self.get_case(origin_case.x, origin_case.y + 1)
        elif direction == Directions.LD:
            return self.get_case(origin_case.x - 1, origin_case.y + 1)
        elif direction == Directions.L:
            return self.get_case(origin_case.x - 1, origin_case.y)

        raise Exception

    def get_opponent_card_in_direction(self, direction, case):

        opponent_case = self.get_case_in_direction(direction, case)
        if not opponent_case:
            return None

        if opponent_case.is_crushed or not opponent_case.is_occupied():
            return None

        card = case.inside
        opponent_card = opponent_case.inside

        if card.player == opponent_card.player:
            return None

        return opponent_card

    def select_case(self, click_x, click_y):

        for line in self.table:
            for case in line:
                if case.is_cursor_on(click_x, click_y):

                    if case.is_occupied() or case.is_crushed:
                        return None
                    if case.is_selected:
                        case.is_selected = False
                        return None
                    else:
                        self.unselect_all_cases()
                        case.is_selected = True
                        return case
                else:
                    case.is_selected = False

        return None

    def unselect_all_cases(self):
        for line in self.table:
            for case in line:
                case.is_selected = False

    def has_click_on_selected_case(self, click_x, click_y):
        for line in self.table:
            for case in line:
                if case.is_selected and case.is_cursor_on(click_x, click_y):
                    return True

        return False

    # DRAWING FUNCTION

    def draw(self, update=True):
        # erase the current board 
        pygame.draw.rect(self.screen, get_color(white), self.rect)
        # redraw the border
        pygame.draw.rect(self.screen, get_color(black), self.rect, border)

        for line in self.table:
            for case in line:
                case.draw()

        if update:
            pygame.display.update()



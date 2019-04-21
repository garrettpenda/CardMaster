# coding: utf-8

from GameClasses.Card import *
from Parameters.utils import *
from Exceptions.PlayerExceptions import *
import pygame


class Player(object):

    # PROPERTIES

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        if not isinstance(value, str):
            raise PlayerParameterException("Player name value must be a string")

        self._name = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):

        # if not isinstance(value, tuple):
        #     raise PlayerParameterException("Player color value must be a tuple")
        #
        # if not len(value) == 3:
        #     raise PlayerParameterException("Player color tuple length must be 3")
        #
        # for c in value :
        #     if not isinstance(c, int):
        #         raise PlayerParameterException("Player color tuple values must be a number")
        #
        #     if c < 0 or c > 255:
        #         raise PlayerParameterException("Player color tuple values must between 0 and 255")

        self._color = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):

        if value is None:
            self._number = value
            return

        if not isinstance(value, int):
            raise PlayerParameterException("Player number value must be a number")

        if value < 0:
            raise PlayerParameterException("Player number value must be positive")

        self._number = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):

        if not isinstance(value, int):
            raise PlayerParameterException("Player score value must be a number")

        if value < 0:
            raise PlayerParameterException("Player score value must be positive")

        self._score = value

    @property
    def round(self):
        return self._round

    @round.setter
    def round(self, value):

        if not isinstance(value, int):
            raise PlayerParameterException("Player round value must be a number")

        if value < 0:
            raise PlayerParameterException("Player round value must be positive")

        self._round = value


    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, value):

        if not isinstance(value, list):
            raise PlayerParameterException("Player polygone value must be a list")

        card_numbers = []
        card_selected = []

        for card in value:

            if not isinstance(card, Card):
                raise PlayerParameterException("Player hand can only contains card")

            if not card.player == self.number:
                raise PlayerParameterException("Player hand can only its own cards")

            if card.is_selected:
                card_selected.append(card.number)
            card_numbers.append(card.number)

        if not len(card_numbers) == len(set(card_numbers)):
            raise PlayerParameterException("Player hand can only contains card with different number")

        if not len(card_selected) == len(set(card_selected)):
            raise PlayerParameterException("Player hand can only contains card with different number")

        self._hand = value


    # CONSTRUCTORS

    def __init__(self, name, color, screen):

        self.name = name
        self.screen = screen
        self.color = color
        self.number = None
        self.hand = []
        self.score = 0
        self.round = 0

        self.rect = None

    def __repr__(self):
        return str(self.__dict__)

    # FUNCTIONS

    def reset_hand(self):

        # definir 5 cases ?

        card1 = Card(1, self.number, self.color, self.screen)
        card2 = Card(2, self.number, self.color, self.screen)
        card3 = Card(3, self.number, self.color, self.screen)
        card4 = Card(4, self.number, self.color, self.screen)
        number = 18 - (card1.number_of_arrows + card2.number_of_arrows + card3.number_of_arrows + card4.number_of_arrows)
        card5 = Card(5, self.number, self.color, self.screen, number_of_arrows=number)
        self.hand = [card1, card2, card3, card4, card5]
        self.reset_hand_positions()

        #for card in self.hand:
        #    card.init_position()
    def reset_hand_positions(self):
        if not self.rect:
            return
        for card in self.hand:
            card.rect.centerx = self.rect.centerx
            card.rect.y = self.rect.y + 60 +card_intern_interval+ (card.number-1) * (case_height + card_extern_interval)
            card.set_arrows_positions()

    def select_card(self, x, y):
        # add check to see if multiple card are selected
        for card in self.hand:
            if card.is_cursor_on(x, y):
                if card.is_selected :
                    card.is_selected = False
                    return None
                else :
                    self.unselect_all_cards()
                    card.is_selected = True
                    return card
            else:
                card.is_selected = False

        return None

    def unselect_all_cards(self):
        for card in self.hand:
            card.is_selected = False

    def get_card(self, number):
        if number > 5 or number < 1:
            print ("number is wrong")
        else:
            for x in range(len(self.hand)):
                if self.hand[x].number == number:
                     return self.hand.pop(x)
            print ("The player " + str(self.name) + " doesn't have the card number " + str(number) + " on his/her hand.")

    def add_card(self, card):
        self.hand.append(card)

    def get_selected_card(self):

        card_selected = None
        for card in self.hand:
            if card.is_selected:
                if card_selected:
                    raise PlayerParameterException("Player have too many selected card in hand")
                else:
                    card_selected = card

        return card_selected

    # DRAWING FUNCTIONS

    def draw(self, card_hidden=False):

        position = self.number

        # name
        self.screen.blit(get_text_image(self.name), (self.rect.x + 10, self.rect.y))

        # round
        player_round_text = get_text(text_player_round, text_completion=str(self.round))
        self.screen.blit(get_text_image(player_round_text), (self.rect.x + 10,self.rect.y + 20))

        # score
        player_score_text = get_text(text_player_score, text_completion=str(self.score))
        self.screen.blit(get_text_image(player_score_text), (self.rect.x + 10,self.rect.y + 40))


        for handplaces in range(0, 5):
            pygame.draw.rect(self.screen, get_color(black), pygame.Rect(self.rect.centerx- case_width/2,
                                                                       self.rect.y + 60 + handplaces * (case_height + card_extern_interval),
                                                                       case_width,
                                                                       case_height), border)
        # cards in hands
        for card in self.hand:
            card.draw(hidden=card_hidden)


def build_player_from_json(json_data):
    player = Player(json_data['name'], json_data['color'], None)
    player.number = json_data['number']
    for number in range(1,6):
        card = Card(0, player.number, number, player.color)

        player.hand.append(card)
    player.reset_hand_positions()
    return player


if __name__ == '__main__':
    player = build_player_from_json(eval("{'name': 'kebab', 'number': 1, 'color': (255, 0, 0)}"))

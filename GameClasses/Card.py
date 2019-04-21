# coding: utf-8


from Exceptions.CardExceptions import *
from GameClasses.Arrow import *
from random import randint
from Parameters.Images.Images import *
from Parameters.Langages.Langages import *

class Card(object):

    # PROPERTIES

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):

        if not isinstance(value, int):
            raise CardParameterException("Card player value must be a number")

        if value < 0:
            raise CardParameterException("Card player value must be positive")

        self._player = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):

        if not isinstance(value, int):
            raise CardParameterException("Card number value must be a number")

        if value not in range(1, 6, 1):
            raise CardParameterException("Card number value must between 1 and 5")

        self._number = value

    @property
    def number_of_arrows(self):
        return self._number_of_arrows

    @number_of_arrows.setter
    def number_of_arrows(self, value):

        if not isinstance(value, int):
            raise CardParameterException("Card number of arrows value must be a number")

        if value not in range(1, 9, 1):
            raise CardParameterException("Card number of arrows value must be between 1 and 8")

        if self.number == 1 and value not in range(1, 3):
            raise CardParameterException("Card number 1 can only have from 1 to 2 arrows : ["+str(value)+"]")

        if self.number == 2 and value not in range(2, 5):
            raise CardParameterException("Card number 2 can only have from 2 to 4 arrows")

        if self.number == 3 and value not in range(3, 7):
            raise CardParameterException("Card number 3 can only have from 3 to 6 arrows")

        if self.number == 4 and not value == 4:
            raise CardParameterException("Card number 4 can only have 4 arrows")

        if self.number == 5 and value not in range(2, 9):
            raise CardParameterException("Card number 5 can only have from 2 to 8 arrows")

        self._number_of_arrows = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):

        # if not isinstance(value, str):
        #     raise CardParameterException("Card color value must be a tuple")
        #
        # if not len(value) == 3:
        #     raise CardParameterException("Card color tuple length must be 3")
        #
        # for c in value :
        #     if not isinstance(c, int):
        #         raise CardParameterException("Card color tuple values must be a number")
        #
        #     if c < 0 or c > 255:
        #         raise CardParameterException("Card color tuple values must between 0 and 255")

        self._color = value

    @property
    def is_selected(self):
        return self._is_selected

    @is_selected.setter
    def is_selected(self, value):

        if not isinstance(value, bool):
            raise CardParameterException("Card is_selected must be a boolean")

        self._is_selected = value

    @property
    def life_point(self):
        return self._life_point

    @life_point.setter
    def life_point(self, value):

        if not isinstance(value, int):
            raise CardParameterException("Card life point must be a number")

        if value not in range(0, 19, 1):
            raise CardParameterException("Card life point must be between 0 and 18")

        self._life_point = value

    @property
    def max_life_point(self):
        return self._max_life_point

    @max_life_point.setter
    def max_life_point(self, value):

        if not isinstance(value, int):
            raise CardParameterException("Card maximum life point must be a number")

        if not value % 2 == 0:
            raise CardParameterException("Card maximum life point must be even")

        if not value in range(4, 19, 1):
            raise CardParameterException("Card maximum life point must be between 4 and 18")

        self._max_life_point = value

    @property
    def arrows(self):
        return self._arrows

    @arrows.setter
    def arrows(self, value):

        if not isinstance(value, dict):
            raise CardParameterException("Card arrows must be a dictionnary")

        if not len(value) == len(Directions.all_directions):
            raise CardParameterException("Card arrows length is not correct")

        #if not value.keys() == Directions.ALL_DIRECTIONS:
        #    raise CardParameterException("Card arrows is incorrect")

        for direction in Directions.all_directions:

            if value.get(direction) is None:
                continue

            if not isinstance(value.get(direction), Arrow):
                raise CardParameterException("Card arrows must be an Arrow")

        self._arrows = value

    @property
    def combo_percent(self):
        return self._combo_percent

    @combo_percent.setter
    def combo_percent(self, value):

        if not isinstance(value, int):
            raise CardParameterException("Card combo percent must be a number")

        if value not in range(0, 101, 1):
            raise CardParameterException("Card combo percent must be between 0 and 100")

        self._combo_percent = value

    @property
    def combo_color(self):
        return self._combo_color

    @combo_color.setter
    def combo_color(self, value):

        if value is None:
            self._combo_color = value
            return

        # if not isinstance(value, tuple):
        #     raise CardParameterException("Card combo color value must be a tuple")
        #
        # if value is None or not isinstance(value, tuple):
        #     raise CardParameterException("Card combo color value must be a tuple")
        #
        # if not len(value) == 3:
        #     raise CardParameterException("Card combo color tuple length must be 3")
        #
        # for c in value:
        #     if not isinstance(c, int):
        #         raise CardParameterException("Card combo color tuple values must be a number")
        #
        #     if c < 0 or c > 255:
        #         raise CardParameterException("Card combo color tuple values must between 0 and 255")
        self._combo_color = value

    @property
    def combo_direction(self):
        return self._combo_direction

    @combo_direction.setter
    def combo_direction(self, value):

        if value is None:
            self._combo_direction = value
            return

        if value not in Directions.all_directions:
            raise CardParameterException("Card combo direction is incorrect")

        self._combo_direction = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        if not isinstance(value, str):
            raise CardParameterException("Card name value must be a string")

        self._name = value

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, value):

        if not isinstance(value, pygame.Rect):
            raise CardParameterException("Card rect value must be a pygame rectangle")

        if not value.x >= 0 or not value.y >= 0:
            raise CardParameterException

        if not value.w == card_width or not value.h == card_height:
            raise CardParameterException

        self._rect = value

    # CONSTANTS

    back_images = ""

    # CONSTRUCTORS

    def __init__(self, card_number, player_number,  color, screen, number_of_arrows=None):

        self.player = player_number
        self.number = card_number
        self.color = color
        self.screen = screen

        if self.number == 1:
            self.number_of_arrows = randint(1, 2)
            self.image_key = golem_image_key
        elif self.number == 2:
            self.number_of_arrows = randint(2, 4)
            self.image_key = golem_image_key
        elif self.number == 3:
            self.number_of_arrows = randint(3, 6)
            self.image_key = golem_image_key
        elif self.number == 4:
            self.number_of_arrows = 4
            self.image_key = golem_image_key
        elif self.number == 5:
            self.number_of_arrows = number_of_arrows
            self.image_key = golem_image_key

        self.is_selected = False

        self.combo_percent = 0
        self.combo_color = None
        self.combo_direction = None

        self.rect = pygame.Rect(0, 0, card_width, card_height)

        self.name = str(self.number) + str(self.player)[0]

        self.life_point = 20 - 2 * self.number_of_arrows
        self.max_life_point = self.life_point

        self.arrows = {direction: None for direction in Directions.all_directions}

        while len(self.get_arrows_directions()) != self.number_of_arrows:
            direction = Directions.all_directions[randint(0, len(Directions.all_directions) - 1)]
            if not self.arrows.get(direction):
                self.arrows[direction] = Arrow(direction, self.rect.x, self.rect.y, self.screen)

    def __repr__(self):
        dict = self.__dict__
        dict_to_send = {}
        for key in dict:
            if key == 'rect':
                dict_to_send[key] = ""
            else:
                dict_to_send[key] = dict[key]
        return str(dict_to_send)

    # FUNCTIONS

    def get_arrows_directions(self):
        # return all direction where the card has an arrow
        return [direction for direction in Directions.all_directions if self.arrows[direction]]

    def set_position(self, px, py):
        self.rect.x = px
        self.rect.y = py
        self.set_arrows_positions()

    def set_arrows_positions(self):
        for direction in self.get_arrows_directions():
            self.arrows[direction].set_position(self.rect.x, self.rect.y)

    def reborn(self):
        self.life_point = int((self.max_life_point) / 2)

    def reset_combo(self):
        self.combo_percent = 0
        self.combo_color = None
        self.combo_direction = None

    def is_cursor_on(self, x, y):

        if x is None or not isinstance(x, int):
            raise CardFunctionParameterException
        if y is None or not isinstance(y, int):
            raise CardFunctionParameterException
        if y < 0 or x < 0:
            raise CardFunctionParameterException

        return self.rect.collidepoint((x, y))

    def change_player(self, player, color):
        self.player = player
        self.color = color

    # DRAWING FUNCTIONS

    def draw(self, hidden=False):

        pygame.draw.rect(self.screen, get_color(self.color), self.rect)

        if hidden:
            return

        if self.combo_color is not None:
            cpw = self.combo_percent * card_width / 100
            cph = self.combo_percent * card_height / 100
            # the combo number is where the combo comes from in the card
            # if the combo number is UP, the combo start from up and finish in DOWN etc
            if self.combo_direction == Directions.LU:
                pygame.draw.rect(self.screen, get_color(self.combo_color), pygame.Rect(self.rect.x, self.rect.y, cpw, cph))

            elif self.combo_direction == Directions.U:
                pygame.draw.rect(self.screen, get_color(self.combo_color), pygame.Rect(self.rect.x, self.rect.y, card_width, cph))

            elif self.combo_direction == Directions.RU:
                pygame.draw.rect(self.screen, get_color(self.combo_color), pygame.Rect(self.rect.x + card_width, self.rect.y, -cpw, cph))

            elif self.combo_direction == Directions.R:
                pygame.draw.rect(self.screen, get_color(self.combo_color), pygame.Rect(self.rect.x + card_width, self.rect.y, -cpw, card_height))

            elif self.combo_direction == Directions.RD:
                pygame.draw.rect(self.screen, get_color(self.combo_color), pygame.Rect(self.rect.x + card_width, self.rect.y + card_height, -cpw, -cph))

            elif self.combo_direction == Directions.D:
                pygame.draw.rect(self.screen, get_color(self.combo_color), pygame.Rect(self.rect.x, self.rect.y + card_height, card_width, -cph))

            elif self.combo_direction == Directions.LD:
                pygame.draw.rect(self.screen, get_color(self.combo_color), pygame.Rect(self.rect.x, self.rect.y + card_height, cpw, -cph))

            elif self.combo_direction == Directions.L:
                pygame.draw.rect(self.screen, get_color(self.combo_color), pygame.Rect(self.rect.x, self.rect.y, cpw, card_height))

        if self.image_key:
            self.screen.blit(get_image(self.image_key, width=card_width - 20, height=card_height - 20),
                             (self.rect.x + 10, self.rect.y + 10))

        for direction in self.get_arrows_directions():
            self.arrows[direction].draw()

        self.screen.blit(get_text_image(str(self.life_point), color_key=white), (self.rect.x + card_width / 2 - 10, self.rect.y + card_height / 2 - 10))

        if self.is_selected:
            pygame.draw.rect(self.screen, get_color(red), self.rect, border)


def build_card_from_json(json_data):

    card = Card(0, json_data['player'], json_data['number'], json_data['color'])
    for key, value in json_data['arrows'].items():
        card.arrows[key] = value
    card.name = json_data['name']
    card.color = json_data['color']
    card.is_selected = json_data['isSelected']
    card.number = json_data['number']
    card.life_point = json_data['LP']
    card.max_life_point = json_data['maxLP']
    return card


if __name__ == '__main__':
    build_card_from_json(eval("{'maxLP': 12, 'name': '21', 'isSelected': False, 'color': (255, 0, 0), 'px': 528, 'py': 248, 'arrows': {0: True, 1: False, 2: False, 3: True, 4: True, 5: False, 6: True, 7: False}, 'number': 2, 'player': 1, 'LP': 12, 'y': 1, 'x': 3}"))

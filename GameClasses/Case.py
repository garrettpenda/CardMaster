# coding: utf-8

import pygame
from Exceptions.CaseException import *
from GameClasses.Card import Card
from Parameters.SizesAndPositions.SizesAndPositions import *
from Parameters.Colors.Colors import *

class Case(object):

    # PROPERTIES

    @property
    def inside(self):
        return self._inside

    @inside.setter
    def inside(self, value):

        if value is None:
            self._inside = value
            return

        if not isinstance(value, Card):
            raise CaseParameterException("Case inside value must be a card")

        self._inside = value

    @property
    def is_crushed(self):
        return self._crushed

    @is_crushed.setter
    def is_crushed(self, value):

        if not isinstance(value, bool):
            raise CaseParameterException("Case is_crushed must be a boolean")

        self._crushed = value

    @property
    def is_selected(self):
        return self._is_selected

    @is_selected.setter
    def is_selected(self, value):

        if not isinstance(value, bool):
            raise CaseParameterException("Case is_selected must be a boolean")

        self._is_selected = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):

        if not isinstance(value, int):
            raise CaseParameterException("Case x value must be a number")

        if value not in range(0, 4):
            raise CaseParameterException("Case x value must be between 0 and 3")

        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):

        if not isinstance(value, int):
            raise CaseParameterException("Case y value must be a number")

        if value not in range(0, 4):
            raise CaseParameterException("Case y value must be between 0 and 3")

        self._y = value

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, value):

        if not isinstance(value, pygame.Rect):
            raise CaseParameterException("Case rect value must be a pygame rectangle")

        if not value.x >= 0 or not value.y >= 0:
            raise CaseParameterException

        if not value.w == case_width or not value.h == case_height:
            raise CaseParameterException

        self._rect = value

    # CONSTRUCTOR
    
    def __init__(self, x, y, board_px, board_py, screen):
        self.inside = None
        self.is_selected = False
        self.is_crushed = False
        self.screen = screen
        self.x = x
        self.y = y
        # seperate into to check the parameter

        self.rect = pygame.Rect(board_px + boarding + self.x * ( case_width + card_extern_interval),
                                board_py + boarding + self.y * ( case_height + card_extern_interval),
                                case_width,
                                case_height)

    
    def __repr__(self):
        if self.is_occupied():
            return self.inside.name
        elif self.is_crushed:
            return "XX"
        else:
            return "  "

    # FUNCTIONS

    def is_occupied(self):
        return self.inside is not None

    def put(self, card):

        if self.is_occupied() or self.is_crushed:
            raise CaseParameterException("Cannot put card inside a crush or occupied case.")

        card.set_position(self.rect.x + card_intern_interval, self.rect.y + card_intern_interval)
        card.is_selected = False

        self.inside = card

    def crush(self):
        self.inside = None
        self.is_crushed = True

    def is_cursor_on(self, x, y):

        if x is None or not isinstance(x, int):
            raise CaseParameterException
        if y is None or not isinstance(y, int):
            raise CaseParameterException
        if y < 0 or x < 0:
            raise CaseParameterException

        return self.rect.collidepoint((x, y))

    # DRAWING FUNCTIONS

    def draw(self):
        if self.is_crushed:
            pygame.draw.rect(self.screen, get_color(black), self.rect)
            return

        if not self.is_selected:
            pygame.draw.rect(self.screen, get_color(black), self.rect, border)
        else :
            pygame.draw.rect(self.screen, get_color(red), self.rect, border)

        if self.is_occupied():
            self.inside.draw()




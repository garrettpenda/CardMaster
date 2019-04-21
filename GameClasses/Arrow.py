# coding: utf-8
import pygame
from Exceptions.ArrowExceptioins import *
from Parameters.GameParameters.Directions import *
from Parameters.Colors.Colors import *
from Parameters.SizesAndPositions.SizesAndPositions import *




class Arrow(object):

    # PROPERTIES

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):

        if value not in Directions.all_directions:
            raise ArrowParameterException("Arrow direction is incorrect")

        self._direction = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        #
        if not isinstance(value, str):
            raise ArrowParameterException("Arrow color value must be a str")

        if not value in all_colors:
            raise Exception("Arrow color value is incorrect")

        self._color = value

    @property
    def polygone(self):
        return self._polygone

    @polygone.setter
    def polygone(self, value):

        if not isinstance(value, list):
            raise ArrowParameterException("Arrows polygone value must be a list")

        if not len(value)== 3:
            raise ArrowParameterException("Arrows polygone length must be 3")

        for point in value:

            if not isinstance(point, list):
                raise ArrowParameterException("Arrows polygone length must be 3")

            if not len(point) == 2:
                raise ArrowParameterException("Arrows point must contain 2 values")

            for coor in point:
                if not (isinstance(coor, float) or isinstance(coor, int)):
                    raise ArrowParameterException("Arrows polygone coor must be a number")

                if coor < 0:
                    raise ArrowParameterException("Arrows polygone coor must be positive")

        self._polygone = value

    # CONSTRUCTORS

    def __init__(self, direction, card_px, card_py, screen, color=white):

        self.direction = direction
        self.color = color
        self.screen = screen
        self.set_position(card_px, card_py)

    def __bool__(self):
        return True

    # FUNCTIONS

    def set_position(self, px, py):

        if self.direction == Directions.LU:
            x = px + arrow_boarding
            y = py + arrow_boarding
            self.polygone = [[x, y], [x + arrow_size, y], [x, y + arrow_size]]
        if self.direction == Directions.U:
            x = px + card_width / 2
            y = py + arrow_boarding
            self.polygone = [[x, y], [x + r2_arrow_size, y + r2_arrow_size],
                                                 [x - r2_arrow_size, y + r2_arrow_size]]
        if self.direction == Directions.RU:
            x = px + card_width - arrow_boarding
            y = py + arrow_boarding
            self.polygone = [[x, y], [x - arrow_size, y], [x, y + arrow_size]]
        if self.direction == Directions.R:
            x = px + card_width - arrow_boarding
            y = py + card_height / 2
            self.polygone = [[x, y], [x - r2_arrow_size, y + r2_arrow_size],
                                                 [x - r2_arrow_size, y - r2_arrow_size]]
        if self.direction == Directions.RD:
            x = px + card_width - arrow_boarding
            y = py + card_height - arrow_boarding
            self.polygone = [[x, y], [x - arrow_size, y], [x, y - arrow_size]]
        if self.direction == Directions.D:
            x = px + card_width / 2
            y = py + card_height - arrow_boarding
            self.polygone = [[x, y], [x + r2_arrow_size, y - r2_arrow_size],
                                                 [x - r2_arrow_size, y - r2_arrow_size]]
        if self.direction == Directions.LD:
            x = px + arrow_boarding
            y = py + card_height - arrow_boarding
            self.polygone = [[x, y], [x + arrow_size, y], [x, y - arrow_size]]
        if self.direction == Directions.L:
            x = px + arrow_boarding
            y = py + card_height / 2
            self.polygone = [[x, y], [x + r2_arrow_size, y + r2_arrow_size],
                                                 [x + r2_arrow_size, y - r2_arrow_size]]

    # DRAWING FUNCTIONS

    def draw(self):
        pygame.draw.polygon(self.screen, get_color(self.color), self.polygone, 0)

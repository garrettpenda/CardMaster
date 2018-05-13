from utils import *

class Case(object):
    
    def __init__(self,y,x):
        self.inside = None
        self.occupied = False
        self.crushed = False
        self.x = x
        self.y = y
        self.px = board_px + boarding + x*(cardwidth + card_extern_interval) + card_intern_interval
        self.py = board_py + boarding + y*(cardheight + card_extern_interval) + card_intern_interval
    
    def __repr__(self):
        if self.occupied:
            return self.inside.getName()
        elif self.crushed:
            return " XXXXXXXXXXX "
        else:
            return "             "

    def add(self,card):
        if not (self.occupied or self.crushed):
            self.occupied = True
            card.x = self.x
            card.y = self.y
            card.px = self.px
            card.py = self.py
            card.isSelected = False
            self.inside = card

    def crush(self):
	self.inside = None
	self.occupied = False
        self.crushed = True


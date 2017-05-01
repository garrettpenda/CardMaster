from Card import *
from Case import *
from Hand import *
from utils import *

class Player(object):

    def __init__(self,name,number,color):
	self.name = name
        self.number = number
	self.color = color
	self.hand = Hand(self.number,self.color)
	self.score = 0

    def changeColor(self):
	number = int(raw_input("1 for red, 2 for blue, 3 for green, 4 for black, 5 for yellow and 6 for purple."))
	self.color = allColors(number)

from random import randint
import math

# all function and globals variables.

#================
# colors
#================
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
yellow = (255,255,0)
purple = (255,0,255)
allColors = {1:red,2:blue,3:green,4:black,5:yellow,6:purple}

#===========
# sizes
#===========
cardwidth = 60
cardheight = 80

r2 = 5.0/math.sqrt(2.0)

#===============
# positions
#===============

#============
# functions
#============

def Coin():
    return bool(randint(0,1))

def getX(number,x):
    if number == 0:
	return x-1
    elif number == 1 :
	return x
    elif number == 2:
	return x+1
    elif number == 3:
	return x+1
    elif number == 4:
	return x+1
    elif number == 5:
	return x
    elif number == 6:
	return x-1
    elif number == 7:
	return x-1

def getY(number,y):
    if number == 0:
	return y-1
    elif number == 1 :
	return y-1
    elif number == 2:
	return y-1
    elif number == 3:
	return y
    elif number == 4:
	return y+1
    elif number == 5:
	return y+1
    elif number == 6:
	return y+1
    elif number == 7:
	return y
    

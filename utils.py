from random import randint

def Coin():
    return bool(randint(0,1))

def outOfBoard(number,card):
    if number == 0 and card.x!=0 and card.y!=0:
	return False
    elif number == 1 and card.y!=0:
	return False
    elif number == 2 and card.x!=3 and card.y!=0:
	return False
    elif number == 3 and card.x!=3:
	return False
    elif number == 4 and card.x!=3 and card.y!=3:
	return False
    elif number == 5 and card.y!=3:
	return False
    elif number == 6 and card.x!=0 and card.y!=3:
	return False
    elif number == 7 and card.x!=0:
	return False
    return True

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
    

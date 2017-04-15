from random import randint

class Card(object):

    def __init__(self,n,player,number):
	self.number = number
	self.x=None
	self.y=None
	self.player = player
	self.name = str(self.number) + str(self.player)[0]
	self.arrows = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0}
	self.LP = 20-2*n
	self.maxLP = self.LP
	numberArrows = 0
	while numberArrows != n:
	    random = randint(0, 7)
	    if self.arrows[random]==0:
	         numberArrows += 1
	         self.arrows[random]=1

    def __repr__(self):
	string = "+-------+\n"
	string += "| " + str(self.arrows[0]) + " " + str(self.arrows[1]) + " " + str(self.arrows[2]) + " |\n"
	string += "| " + str(self.arrows[7]) + " " + str(self.player) + " " + str(self.arrows[3]) + " |\n"
	string += "| " + str(self.arrows[6]) + " " + str(self.arrows[5]) + " " + str(self.arrows[4])+ " |\n"
	string += "+-------+\n"
	string += "| "+ str(self.LP).zfill(2) +"/"+ str(self.maxLP).zfill(2) +" |\n"
	string += "+-------+\n"
	return string

    def changePlayer(self,player):
	self.player = player

    def reborn(self):
	self.LP = (self.maxLP)/2

    def fight(self,otherCard):
	print self.name + " fights " + otherCard.name
	attack = True
	if not(self.player==otherCard.player):
	    while(self.LP != 0 and otherCard.LP != 0 ):
		if(attack):
		    otherCard.LP -= 1
		    attack = not attack
		else:
		    self.LP -= 1
		    attack = not attack
	    if self.LP == 0:
		self.reborn() 
		self.changePlayer(otherCard.player)
		return False
	    else:
		otherCard.reborn()
		otherCard.changePlayer(self.player)
		return True

    def getName(self):
	return self.name+"("+str(self.LP).zfill(2)+"/"+str(self.maxLP).zfill(2)+self.player
	


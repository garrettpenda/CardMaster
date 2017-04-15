class Case(object):
    
    def __init__(self,y,x):
	self.inside = None
	self.occupied = False
	self.crushed = False
	self.x = x
	self.y = y
	
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
	    self.inside = card

    def crush(self):
	if not self.crushed:
	    self.crushed = True


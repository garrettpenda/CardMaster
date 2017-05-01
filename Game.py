from Board import *
from Hand import *

table = Board(4)
main = Hand(1)
main2 = Hand(2)

# todo faire un menu aussi
print main
print table
print main2

print "The game begin"

turn = Coin()
if turn:
    print "The player 1 starts."
else:
    print "The player 2 starts."

while len(main.cards)!=0 or len(main2.cards)!=0 :     
    if turn :
	nbCards = len(main.cards)
	main2.hidden()
	print table
	print main
	number = int(raw_input("number of card:"))
	X = int(raw_input("X:"))
	Y = int(raw_input("Y:"))
	card = main.getCard(number)
	cardIsPlayed = table.play(card,X,Y)
	if cardIsPlayed:
	    turn = not turn
	else:
	    main.addCard(card)
    else :
	nbCards = len(main2.cards)
	main.hidden()
	print table
	print main2
	number = int(raw_input("number of card:"))
	X = int(raw_input("X:"))
	Y = int(raw_input("Y:"))
	card = main2.getCard(number)
	cardIsPlayed = table.play(card,X,Y)
	if cardIsPlayed:
	    turn = not turn
	else:
	    main2.addCard(card)

print table
print "the game is over"

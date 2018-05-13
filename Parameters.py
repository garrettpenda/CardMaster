import math

#================
# colors
#================
white = (255,255,255)
red = (255,0,0) #fire
blue = (0,0,255) #water
green = (0,255,0) # life
black = (0,0,0) # void
grey = (125,125,125) #metal
brown = (128,30,30) #earth
yellow = (255,255,0) #thunder
purple = (255,0,255) # darkness
clearblue = (0,255,255) # ice
# magma
# light

#===========
# sizes
#===========

window_width = 800
window_height = 800

size_of_board = 4



cardwidth = 90
cardheight = 120

board_px = 200
board_py = 100

hand_p1_px = 40
hand_p2_px = 700

hand_p1_py = 50
hand_p2_py = 50

buttonpx = 400
buttonpy = 680

button_width = 200
button_height = 100

boarding = 10
card_extern_interval = 15
card_intern_interval = 3

border = 2

r2 = 5.0/math.sqrt(2.0)

animationTime = 0.1

#==================
# game parameters
#==================

rounds_to_win = 2

#===========
# text
#===========

text_draw ='Draw !'
text_capitulate_round = 'Capitulate Round'


text_continue = "Continue"
text_return_to_menu = "Return to menu"

text_player_won = "The player %s has won the game."
text_player_won_round = "The player %s win the round."
text_case_occupied = "This case is occupied or consumed by the void."

text_start_game = "Start Game"
text_start_game_solo = "Start Game VS IA"
text_story = "Story"
text_options = "Options"
text_tutotial = "Tutorial"
text_quit_game = "Quit Game"
text_choose_card = "You must choose a card to fight"



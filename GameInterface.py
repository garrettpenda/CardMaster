from Player import *
from Board import *
from IA import *


# TODO completer la fonction drawboard
# TODO faire le fond qui change de couleur en fonction de l'element dominant
# faire les cartes vide qui apparaissent

# TODO ajouter des sons

# TODO faire un tutorial explication element "vide", guerre des elements,
# TODO animation de la piece si true

# TODO le menu option
# TODO mettre tous les parametres dans parametre puis dans un fichier conf
# TODO faire internationnnalisation
# TODO faire les dessins sur les cartes golem, chimere, arme, elementaire, source ( a voir comment faire pour debloquer )

# TODO faire le mode 3 joueurs ( sous menu apres avoir faire start game : cas d'egalite a revoir )

# TODO ameliorer IA et faire mode de jeu contre IA avec sous menu
# TODO mettre le jeu en ligne ...

# TODO faire le bouton capituler game

# se souvenir des changement en ligne : bouton capituler, les mains cachees, 


pygame.init()
pygame.display.set_caption("Elementz")
fenetre = pygame.display.set_mode((window_width, window_height))
fenetre.fill(white)
pygame.key.set_repeat(400, 30)

clock = pygame.time.Clock()

def newRound(table):
    for player in table.players:
        player.reset_hand()
	player.surrender_round = False

    return Board(size_of_board, table.players)


def cursorOnBoard(x, y):
    return x > board_px + boarding and x < board_px + boarding + (cardwidth + card_extern_interval) * size_of_board and y > board_py + boarding and y < board_py + boarding + (cardheight + card_extern_interval) * size_of_board


def playGame():

    table = Board(size_of_board, [Player("Garrett", 1, purple), Player("creator", 2, blue)])
    cursor_x = 0
    cursor_y = 0
    cardSelected = None
    selected = False
    playGame = True

    table.drawGame(fenetre)

    while playGame:

	if table.active_player_name == 'creator':
	    playrandomcard(table, table.active_player, fenetre)
	    continue
	

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEMOTION:

                cursor_x = event.pos[0]
                cursor_y = event.pos[1]

            if event.type == MOUSEBUTTONDOWN:

                if event.button == 1:

                    click_x = event.pos[0]
                    click_y = event.pos[1]

                    selected = table.active_player.selectCard(click_x, click_y)
                    cardSelected = table.active_player.getSelectedCard();

                    if (selected and cursorOnBoard(click_x, click_y)):

                        X = int((click_x - board_px - boarding) / (cardwidth + card_extern_interval))
                        Y = int((click_y - board_py - boarding) / (cardheight + card_extern_interval))
			
                        card = table.active_player.getCard(cardSelected.number)
                        cardIsPlayed = table.play(card, X, Y, fenetre)
                        if not cardIsPlayed:
                            table.active_player.addCard(card)
                        else:
                            selected = False
                            cardSelected = None
                            table.nextPlayerTurn()

        if (selected and cursorOnBoard(cursor_x, cursor_y)):
            selected_x = board_px + boarding + int((cursor_x - board_px - boarding) / (cardwidth + card_extern_interval)) * (cardwidth + card_extern_interval) + card_intern_interval
            selected_y = board_py + boarding + int((cursor_y - board_py - boarding) / (cardheight + card_extern_interval)) * (cardheight + card_extern_interval) + card_intern_interval
            pygame.draw.rect(fenetre, red, pygame.Rect(selected_x, selected_y, cardwidth, cardheight), border)
            pygame.display.flip()

        table.drawGame(fenetre)

        label = pygame.font.SysFont("monospace", 20).render(str(table.active_player_name), 10, black)
        fenetre.blit(label, (10, 200))

        pygame.display.flip()

        if (table.allHandsAreEmpty() or table.only_one_active_player()):

	    table.drawGame(fenetre)
            table.actualizeRounds(fenetre)

            if table.aPlayerWonTheGame():
		table.draw_message(text_player_won % 'kebab',fenetre)
                clickButtonToContinue(text_return_to_menu, fenetre)

                break;

            table = newRound(table)
	   

def Quit():
    pygame.quit()
    quit()


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        fenetre.fill(white)

        button(fenetre, text_start_game, 50, 50, blue, red, playGame )

        button(fenetre, text_options, 50, 200, yellow, clearblue , None)

        button(fenetre, text_tutotial, 50, 350, green, purple, None)

        button(fenetre, text_quit_game, 50, 500, grey, brown, Quit)

	button(fenetre, text_story, 300, 50, green, purple, None)

        pygame.display.update()
        clock.tick(15)

game_intro()

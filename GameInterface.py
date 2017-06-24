from Player import *
from Board import *

# TODO mettre tous les parametres dans parametre puis dans un fichier conf
# TODO faire les dessins sur les cartes golem, phoenix, arme, elementaire, source
# TODO faire internationnnalisation
# TODO faire un tutorial explication element "vide", guerre des elements,
# TODO l'affichage des etapes
# TODO masquer les cartes du joueur non actif
# TODO optimiser les imports
# TODO le menu option
# TODO ajouter des sons

pygame.init()
pygame.display.set_caption("Elementz")
fenetre = pygame.display.set_mode((800, 800))
fenetre.fill(white)
pygame.key.set_repeat(400, 30)

clock = pygame.time.Clock()

def newRound(table):
    for player in table.players:
        player.resetHand()

    return Board(4, table.players)


def cursorOnBoard(x, y):
    return x > 203 and x < 203 + (cardwidth + 10) * 4 and y > 103 and y < 103 + (cardheight + 10) * 4


def playGame():
    table = Board(4, [Player("Garrett", 1, purple), Player("p2", 2, blue)])
    cursor_x = 0
    cursor_y = 0
    cardSelected = None
    selected = False
    playGame = 1

    table.drawGame(fenetre)
    # clickButtonToContinue("Start Game", fenetre)

    while playGame:

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEMOTION:

                cursor_x = event.pos[0]
                cursor_y = event.pos[1]

                if (selected and cursorOnBoard(cursor_x, cursor_y)):
                    selected_x = 203 + int((cursor_x - 203) / (cardwidth + 10)) * (cardwidth + 10)
                    selected_y = 103 + int((cursor_y - 103) / (cardheight + 10)) * (cardheight + 10)
                    pygame.draw.rect(fenetre, red, pygame.Rect(selected_x, selected_y, cardwidth, cardheight), 2)

            if event.type == MOUSEBUTTONDOWN:

                if event.button == 1:

                    click_x = event.pos[0]
                    click_y = event.pos[1]

                    selected = table.activePlayer.selectCard(click_x, click_y)
                    cardSelected = table.activePlayer.getSelectedCard();

                    if (selected and cursorOnBoard(click_x, click_y)):

                        X = int((click_x - 203) / (cardwidth + 10))
                        Y = int((click_y - 103) / (cardheight + 10))
                        card = table.activePlayer.getCard(cardSelected.number)
                        cardIsPlayed = table.play(card, X, Y, fenetre)
                        if not cardIsPlayed:
                            table.activePlayer.addCard(card)
                        else:
                            selected = False
                            cardSelected = None
                            table.nextPlayerTurn()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                print "functions make details or stuff maybe"

        # drawGame(table,fenetre)
        table.drawGame(fenetre)

        label = pygame.font.SysFont("monospace", 20).render(str(table.activePlayerNumber), 10, black)
        fenetre.blit(label, (10, 200))

        pygame.display.flip()

        if (table.allHandsAreEmpty()):

            table.actualizeRounds(fenetre)

            if table.aPlayerWonTheGame(fenetre):
                playGame = 0
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

        button(fenetre, "Start Game", 50, 50, 200, 100, blue, red, playGame )

        button(fenetre, "Options", 50, 200, 200, 100, yellow, clearblue , None)

        button(fenetre, "Tutorial", 50, 350, 200, 100, green, purple, None)

        button(fenetre, "Quit", 50, 500, 200, 100, grey, brown, Quit)

        pygame.display.update()
        clock.tick(15)

game_intro()
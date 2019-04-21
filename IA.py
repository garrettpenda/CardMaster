from Parameters.utils import *
from GameClasses.Card import *

# TODO : implementer les fonctions suivantes dans lia
# chercher a faire des attaques
# chercher a faire des combos
# chercher a faire le plus gros scores
# donnner une carte pour faire un combo

# TODO : faire des stats sur la facon de jouer ? ( connection base de donnees )

# level 1 : full random

def play_random_card(table, player, fenetre):

    if len(player.hand) == 0:
        return
    random_card = randint(0, len(player.hand) - 1)
    number = player.hand[random_card].number
    card = player.get_card(number)
    
    card_is_played = False
    while not card_is_played:
        X = randint(0, table.size_x-1)
        Y = randint(0, table.size_y-1)
        card_is_played = auto_play(table,card, X, Y)
    
def auto_play(table, card,X,Y):

    if not (table.get_case(X,Y).is_occupied() or table.get_case(X,Y).is_crushed) :

        case = table.get_case(X, Y)
        case.put(card)
        card_has_won_fight = True
        # fights
        fight_directions = table.get_fight_directions(case)
        while len(fight_directions) != 0:
            if len(fight_directions) > 1:
                direction = fight_directions[randint(0,len(fight_directions)-1)]
            elif len(fight_directions) == 1:
                direction = fight_directions[0]

            opposite_card = table.get_opponent_card_in_direction(direction, case)
            card_has_won_fight = table.fight(card, opposite_card)
            # combos
            if card_has_won_fight:
                opposite_case = table.get_case_in_direction(direction, case)
                table.combo(opposite_case)
                fight_directions = table.get_fight_directions(case)
            else:
                table.combo(case)
                fight_directions = []
        # attacks
        if card_has_won_fight:
            table.attack(case)
        return True
    else :
        table.game.message.text_key = text_IA_playing
        return False




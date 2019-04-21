# coding: utf-8

import pygame
from Parameters.Colors.Colors import *

directory_path = os.getcwd()

# =====================
# TEXTS LIBRARY
# =====================

french_key = "french"
english_key = "english"

_text_library = {}

def load_texts(langage=french_key):
    global _text_library

    with open(directory_path + "/Parameters/Langages/" + langage + ".yaml", 'r') as stream:
        try:
            text_file = yaml.safe_load(stream)
            for key, item in text_file.items():
                _text_library[key] = item
        except yaml.YAMLError as exc:
            print(exc)
    stream.close()

def get_text(key, text_completion=None):
    # load all size from the yaml file
    global _text_library
    text = _text_library.get(key, None)
    if text == None:
        raise Exception("Text key is not define [" + key + "]")
    if text_completion:
        text = text % text_completion
    return text

load_texts()

# TEXT STRING KEYS
text_IA_playing = "text_IA_playing"
text_work_in_progress = "text_work_in_progress"
text_draw = "text_draw"
text_continue = "text_continue"
text_return_to_menu = "text_return_to_menu"
text_return_to_game = "text_return_to_game"
text_player_won = "text_player_won"
text_player_won_round = "text_player_won_round"
text_case_occupied = "text_case_occupied"
text_enter_login = "text_enter_login"
text_enter_password = "text_enter_password"
text_choose_color = "text_choose_color"
text_yes = "text_yes"
text_no = "text_no"
text_quit_game_question = "text_quit_game_question"
text_capitulate_game = "text_capitulate_game"
text_capitulate_game_question = "text_capitulate_game_question"
text_connexion = "text_connexion"
text_start_game = "text_start_game"
text_start_2_players_game = "text_start_2_players_game"
text_start_3_players_game = "text_start_3_players_game"
text_start_game_versus_ia = "text_start_game_versus_ia"
text_start_game_trio = "text_start_game_trio"
text_story = "text_story"
text_options = "text_options"
text_tutotial = "text_tutotial"
text_quit_game = "text_quit_game"
text_choose_card_to_fight = "text_choose_card_to_fight"
text_choose_card = "text_choose_card"
text_opponent_turn = "text_opponent_turn"
text_online_menu = "text_online_menu"
text_offline_menu = "text_offline_menu"
text_next_step = "text_next_step"
text_previous_step = "text_previous_step"
text_validate = "text_validate"
text_chest = "text_chest"
text_choose_case = "text_choose_case"
text_validate_case = "text_validate_case"
text_tutorial_message = "text_tutorial_message_step_%s_message_%s"
text_test_game = "text_test_game"
text_player_round = "text_player_round"
text_player_score = "text_player_score"
text_turn_count = "text_turn_count"
text_replay_tutorial = "text_replay_tutorial"
text_step_count = "text_step_count"


#=====================
# TEXT IMAGE LIBRARY
#=====================

_text_image_library = {}

def get_text_image(word, color_key=black):
    global _text_image_library
    image = _text_image_library.get(word, None)
    if image == None:
        #font = pygame.font.SysFont("monospace", 30)
        font = pygame.font.SysFont("comicsansms", 30)
        image = font.render(word, 10, get_color(color_key))
        #font = get_font(fonts, size)
        #image = font.render(text, True, color)
        _text_image_library[word] = image
    return image
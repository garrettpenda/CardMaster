# coding: utf-8

import yaml
import os
import math
from Parameters.GameParameters.GameParameters import size_of_board

directory_path = os.getcwd()

"""
The following parameters cannot be easly reloaded because we use them when we define the class and others...
"""

#=====================
# SIZES LIBRARY
#=====================


_size_library = {}

def load_sizes(scale=1):
    global _size_library
    with open(directory_path + "/Parameters/SizesAndPositions/SizesAndPositions.yaml", 'r') as stream:
        try:
            size_file = yaml.safe_load(stream)
            for key, item in size_file.items():
                _size_library[key] = item*scale
        except yaml.YAMLError as exc:
            print(exc)
    stream.close()

def get_size(word):
    # load all size from the yaml file
    global _size_library
    size = _size_library.get(word, None)
    if size == None:
        raise Exception("Size is not define [" + word + "]")
    return size


#=======
# SIZES
#=======


with open(directory_path + "/Parameters/SizesAndPositions/SizesAndPositions.yaml", 'r') as stream:
    try:
        sizes_and_positions_file = yaml.safe_load(stream)

        boarding = sizes_and_positions_file.get("boarding")

        card_extern_interval = sizes_and_positions_file.get("card_extern_interval")
        card_intern_interval = sizes_and_positions_file.get("card_intern_interval")

        border = sizes_and_positions_file.get("border")
        arrow_size = sizes_and_positions_file.get("arrow_size")
        arrow_boarding = sizes_and_positions_file.get("arrow_boarding")

        window_width = sizes_and_positions_file.get("window_width")
        window_height = sizes_and_positions_file.get("window_height")

        button_width = sizes_and_positions_file.get("button_width")
        button_height = sizes_and_positions_file.get("button_height")

        card_width = sizes_and_positions_file.get("card_width")
        card_height = sizes_and_positions_file.get("card_height")

        input_box_width = sizes_and_positions_file.get("input_box_width")
        input_box_height = sizes_and_positions_file.get("input_box_height")

        color_box_width = sizes_and_positions_file.get("color_box_width")
        color_box_height = sizes_and_positions_file.get("color_box_height")

        tutorial_message_width = sizes_and_positions_file.get("tutorial_message_width")
        tutorial_message_height = sizes_and_positions_file.get("tutorial_message_height")

        quit_game_menu_width = sizes_and_positions_file.get("quit_game_menu_width")
        quit_game_menu_height = sizes_and_positions_file.get("quit_game_menu_height")

        confirm_capitulate_menu_width = sizes_and_positions_file.get("confirm_capitulate_menu_width")
        confirm_capitulate_menu_height = sizes_and_positions_file.get("confirm_capitulate_menu_height")

        work_in_progress_menu_width = sizes_and_positions_file.get("work_in_progress_menu_width")
        work_in_progress_menu_height = sizes_and_positions_file.get("work_in_progress_menu_height")

        end_round_menu_width = sizes_and_positions_file.get("end_round_menu_width")
        end_round_menu_height = sizes_and_positions_file.get("end_round_menu_height")

        end_game_menu_width = sizes_and_positions_file.get("end_game_menu_width")
        end_game_menu_height = sizes_and_positions_file.get("end_game_menu_height")

        in_game_menu_width = sizes_and_positions_file.get("in_game_menu_width")
        in_game_menu_height = sizes_and_positions_file.get("in_game_menu_height")

        in_game_tutorial_menu_width = sizes_and_positions_file.get("in_game_tutorial_menu_width")
        in_game_tutorial_menu_height = sizes_and_positions_file.get("in_game_tutorial_menu_height")

    except yaml.YAMLError as exc:
        print(exc)
stream.close()


#=================================
# RELATIVE POSITIONS
#=================================


window_width_center = window_width / 2.0
window_height_center = window_height / 2.0


# CASES

case_width = card_width + 2 * card_intern_interval
case_height = card_height + 2 * card_intern_interval

# BOARD
board_px = window_width_center
board_py = window_height_center

max_board_width = size_of_board * case_width + (size_of_board-1) * card_extern_interval + 2*boarding
max_board_height = size_of_board * case_height + (size_of_board-1) * card_extern_interval + 2*boarding

board_max_top = window_height_center - max_board_height/2
board_max_right = window_width_center + max_board_width/2
board_max_bottom = window_height_center + max_board_width/2
board_max_left = window_width_center - max_board_width/2

# ARROWS
r2_arrow_size = arrow_size/math.sqrt(2.0)


# PLAYER ==> redefine with the hand classe
hand_p1_px = window_width/10
hand_p2_px = 4*window_width/5

hand_p1_py = window_height/16
hand_p2_py = window_height/16

# MENUS

# TUTORIAL_MESSAGES

tutorial_message_px = window_width_center
tutorial_message_py = window_height_center

tutorial_message_only_next_button_px = tutorial_message_width/2
tutorial_message_only_next_button_py = tutorial_message_height*4/6

tutorial_message_next_button_px = tutorial_message_width*3/4
tutorial_message_next_button_py = tutorial_message_height*4/6

tutorial_message_previous_button_px = tutorial_message_width/4
tutorial_message_previous_button_py = tutorial_message_height*4/6

tutorial_message_close_button_px = tutorial_message_width*3/4
tutorial_message_close_button_py = tutorial_message_height*4/6


# QUIT MENU

quit_game_menu_px = window_width_center
quit_game_menu_py = window_height_center

quit_game_menu_message_px = 0
quit_game_menu_message_py = quit_game_menu_height/5

quit_game_menu_yes_button_px = quit_game_menu_width/4
quit_game_menu_yes_button_py = quit_game_menu_height*3/5

quit_game_menu_no_button_px = quit_game_menu_width*3/4
quit_game_menu_no_button_py = quit_game_menu_height*3/5


# CONFIRM CAPITULATE MENU

confirm_capitulate_menu_px = window_width_center
confirm_capitulate_menu_py = window_height_center

confirm_capitulate_menu_message_px = 0
confirm_capitulate_menu_message_py = confirm_capitulate_menu_height/5

confirm_capitulate_menu_yes_button_px = confirm_capitulate_menu_width/4
confirm_capitulate_menu_yes_button_py = confirm_capitulate_menu_height*3/5

confirm_capitulate_menu_no_button_px = confirm_capitulate_menu_width*3/4
confirm_capitulate_menu_no_button_py = confirm_capitulate_menu_height*3/5

# WORK IN PROGRESS MENU

work_in_progress_menu_px = window_width_center
work_in_progress_menu_py = window_height_center

work_in_progress_menu_message_px = 0
work_in_progress_menu_message_py = work_in_progress_menu_height/5

work_in_progress_menu_quit_button_px = work_in_progress_menu_width/2
work_in_progress_menu_quit_button_py = work_in_progress_menu_height*3/5


# CONNEXION MENU

connexion_menu_choose_name_message_px = window_width/20
connexion_menu_choose_name_message_py = window_height/16

connexion_menu_choose_element_message_px = window_width/20
connexion_menu_choose_element_message_py = window_height*3/16

connexion_menu_name_input_box_px = window_width*2/10
connexion_menu_name_input_box_py = window_height*2/16

connexion_menu_red_choice_px = window_width/10
connexion_menu_red_choice_py = window_height*5/16

connexion_menu_blue_choice_px = window_width*2/10
connexion_menu_blue_choice_py = window_height*5/16

connexion_menu_yellow_choice_px = window_width*3/10
connexion_menu_yellow_choice_py = window_height*5/16

connexion_menu_green_choice_px = window_width*4/10
connexion_menu_green_choice_py = window_height*5/16

connexion_menu_brown_choice_px = window_width/10
connexion_menu_brown_choice_py = window_height*7/16

connexion_menu_grey_choice_px = window_width*2/10
connexion_menu_grey_choice_py = window_height*7/16

connexion_menu_purple_choice_px = window_width*3/10
connexion_menu_purple_choice_py = window_height*7/16

connexion_menu_clear_blue_choice_px = window_width*4/10
connexion_menu_clear_blue_choice_py = window_height*7/16

connexion_menu_connect_button_px = window_width*3/10
connexion_menu_connect_button_py = window_height*10/16

connexion_menu_quit_button_px = window_width*3/10
connexion_menu_quit_button_py = window_height*13/16

connexion_menu_french_button_px = window_width*8/10
connexion_menu_french_button_py = window_height*3/16

connexion_menu_english_button_px = window_width*8/10
connexion_menu_english_button_py = window_height*6/16


# MAIN MENU

main_menu_play_online_button_px = window_width*2/10
main_menu_play_online_button_py = window_height*2/16

main_menu_play_offline_button_px = window_width*2/10
main_menu_play_offline_button_py = window_height*5/16

main_menu_chest_button_px = window_width*2/10
main_menu_chest_button_py = window_height*8/16

main_menu_option_button_px = window_width*2/10
main_menu_option_button_py = window_height*11/16

main_menu_quit_button_px = window_width*2/10
main_menu_quit_button_py = window_height*14/16


# OPTIONS MENU

options_menu_choose_element_message_px = window_width/10
options_menu_choose_element_message_py = window_height*3/16

options_menu_red_choice_px = window_width/10
options_menu_red_choice_py = window_height*5/16

options_menu_blue_choice_px = window_width*2/10
options_menu_blue_choice_py = window_height*5/16

options_menu_yellow_choice_px = window_width*3/10
options_menu_yellow_choice_py = window_height*5/16

options_menu_green_choice_px = window_width*4/10
options_menu_green_choice_py = window_height*5/16

options_menu_brown_choice_px = window_width/10
options_menu_brown_choice_py = window_height*7/16

options_menu_grey_choice_px = window_width*2/10
options_menu_grey_choice_py = window_height*7/16

options_menu_purple_choice_px = window_width*3/10
options_menu_purple_choice_py = window_height*7/16

options_menu_clear_blue_choice_px = window_width*4/10
options_menu_clear_blue_choice_py = window_height*7/16

options_menu_french_button_px = window_width*8/10
options_menu_french_button_py = window_height*3/16

options_menu_english_button_px = window_width*8/10
options_menu_english_button_py = window_height*6/16

options_online_menu_return_to_main_menu_button_px = window_width*3/10
options_online_menu_return_to_main_menu_button_py = window_height*13/16

# PLAY ONLINE MENU

play_online_menu_2_players_game_button_px = window_width*2/10
play_online_menu_2_players_game_button_py = window_height*2/16

play_online_menu_3_players_game_button_px = window_width*2/10
play_online_menu_3_players_game_button_py = window_height*5/16

oneline_menu_return_to_main_menu_button_px = window_width*2/10
oneline_menu_return_to_main_menu_button_py = window_height*14/16

# PLAY OFFLINE MENU

play_offline_menu_versus_ia_game_button_px = window_width*2/10
play_offline_menu_versus_ia_game_button_py = window_height*2/16

play_offline_menu_tutorial_game_button_px = window_width*2/10
play_offline_menu_tutorial_game_button_py = window_height*5/16

play_offline_menu_test_game_button_px = window_width*2/10
play_offline_menu_test_game_button_py = window_height*8/16

play_offline_menu_return_to_main_menu_button_px = window_width*2/10
play_offline_menu_return_to_main_menu_button_py = window_height*14/16


# END ROUND MENU

end_round_menu_px = window_width_center
end_round_menu_py = window_height_center

end_round_menu_message_px = 0
end_round_menu_message_py = end_round_menu_height/5

end_round_menu_continue_button_px = end_round_menu_width/2
end_round_menu_continue_button_py = end_round_menu_height*4/6

# END GAME MENU

end_game_menu_px = window_width_center
end_game_menu_py = window_height_center

end_game_menu_message_px = 0
end_game_menu_message_py = end_game_menu_height/5

end_game_menu_continue_button_px = end_game_menu_width/2
end_game_menu_continue_button_py = end_game_menu_height*4/6

# IN GAME MENU

in_game_menu_px = window_width_center
in_game_menu_py = window_height_center

in_game_menu_capitulate_button_px = in_game_menu_width/2
in_game_menu_capitulate_button_py = in_game_menu_height*1/6

in_game_menu_options_button_px = in_game_menu_width/2
in_game_menu_options_button_py = in_game_menu_height*3/6

in_game_menu_return_to_game_button_px = in_game_menu_width/2
in_game_menu_return_to_game_button_py = in_game_menu_height*5/6

# IN GAME TUTORIAL MENU

in_game_tutorial_menu_px = window_width_center
in_game_tutorial_menu_py = window_height_center

in_game_tutorial_menu_capitulate_button_px = in_game_tutorial_menu_width/2
in_game_tutorial_menu_capitulate_button_py = in_game_tutorial_menu_height*1/8

in_game_tutorial_menu_replay_tutorial_button_px = in_game_tutorial_menu_width/2
in_game_tutorial_menu_replay_tutorial_button_py = in_game_tutorial_menu_height*3/8

in_game_tutorial_menu_options_button_px = in_game_tutorial_menu_width/2
in_game_tutorial_menu_options_button_py = in_game_tutorial_menu_height*5/8

in_game_tutorial_menu_return_to_game_button_px = in_game_tutorial_menu_width/2
in_game_tutorial_menu_return_to_game_button_py = in_game_tutorial_menu_height*7/8




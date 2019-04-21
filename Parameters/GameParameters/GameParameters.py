# coding: utf-8

import yaml
import os

directory_path = os.getcwd()


#=================
# GAME PARAMETERS
#=================


with open(directory_path + "/Parameters/GameParameters/GameParameters.yaml", 'r') as stream:
    try:
        sizes_and_positions_file = yaml.safe_load(stream)
        size_of_board = sizes_and_positions_file.get("size_of_board")
        rounds_to_win = sizes_and_positions_file.get("rounds_to_win")
        animationTime = sizes_and_positions_file.get("animationTime")
        animation_time = sizes_and_positions_file.get("animation_time")

    except yaml.YAMLError as exc:
        print(exc)
stream.close()
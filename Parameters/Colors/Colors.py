
import yaml
import os

directory_path = os.getcwd()

#===========
# COLORS
#===========

basic_color_key = "basic"

def read_color(dict):
    return (dict.get("r"), dict.get("g"), dict.get("b"))

_color_library = {}

def load_colors(option=basic_color_key):
    global _color_library
    with open(directory_path + "/Parameters/Colors/colors.yaml", 'r') as stream:
        try:
            color_file = yaml.safe_load(stream)
            for key, item in color_file[option].items():
                _color_library[key] = read_color(item)
        except yaml.YAMLError as exc:
            print(exc)
    stream.close()

def get_color(key):
    # load all size from the yaml file
    global _color_library
    color = _color_library.get(key, None)
    if color == None:
        raise Exception("Color key is not define [" + key + "]")
    return color

load_colors()

# COLORS STRING KEYS
white = "white"
black = "black"
red = "red"
blue = "blue"
green = "green"
grey = "grey"
brown = "brown"
yellow = "yellow"
purple = "purple"
clearblue = "clearblue"
all_colors = [white, black, red, blue, green, grey,brown, yellow, purple, clearblue]
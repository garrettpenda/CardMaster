# coding: utf-8

import os
import pygame

directory_path = os.getcwd()

#=================
# IMAGE LIBRARY
#=================

_image_library = {}

def get_image(path, width=None, height=None):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        image_path = directory_path + "/Parameters/Images/" + path
        image = pygame.image.load(image_path).convert_alpha()

        if width and height:
            image = pygame.transform.scale(image, (width, height))

        _image_library[path] = image
    return image

french_flag_image_key = "french_flag.png"
english_flag_image_key = "english_flag.png"
golem_image_key = "golem.png"

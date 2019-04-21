# coding: utf-8

from Parameters.utils import RectCenter
from Parameters.Langages.Langages import *
from Parameters.Colors.Colors import *
from Parameters.Images.Images import *
from Parameters.SizesAndPositions.SizesAndPositions import *



class MenuItem(object):

    # CONSTRUCTOR

    def __init__(self, x, y, w, h, absolute_position=False):

        if not absolute_position:
            self.rect = RectCenter(x, y, w, h)
        else:
            self.rect = pygame.Rect(x, y, w, h)
        self.cursor_y = 0
        self.cursor_x = 0

    # FUNCTIONS

    def cursor_is_on(self):
        return self.rect.collidepoint((self.cursor_x, self.cursor_y))

    def move_to(self, x, y, w=None, h=None):
        if x:
            self.rect.x += x
        if y:
            self.rect.y += y
        if w:
            self.rect.w = w
        if h:
            self.rect.h = h


class Message(MenuItem):

    # PROPERTIES

    # CONSTRUCTOR

    def __init__(self, x, y, text_key='', argument=None):

        MenuItem.__init__(self, x, y, 0, 10, absolute_position=True)
        self.text_key = text_key
        self.argument = argument

    # FUNCTIONS

    def test_text_key(self):
        get_text(self.text_key)

    # DRAWING FUNCTIONS

    def draw(self, screen):

        if self.argument:
            text = get_text(self.text_key, text_completion=self.argument)
        else:
            text = get_text(self.text_key)

        space_img = get_text_image(' ')
        space_img_width = space_img.get_width()
        space_img_height = space_img.get_height()

        # marging
        x = self.rect.x + space_img_width
        y = self.rect.y + space_img_height

        # split the text
        words = text.split(" ")
        for word in words:
            # load the image created from the text
            img = get_text_image(word)
            w = img.get_width()

            if x + w > self.rect.x + self.rect.w:
                # if the image is outside the rectangle, return to the line
                y += space_img_height
                x = self.rect.x + space_img_width

            # display the image
            screen.blit(img, (x, y))
            x += w

            # add a space if its not the last word
            if words.index(word) != len(words) - 1:
                screen.blit(space_img, (x, y))
                x += space_img_width

    def draw_centered(self, screen):

        if self.argument:
            text = get_text(self.text_key, text_completion=self.argument)
        else:
            text = get_text(self.text_key)

        space_img = get_text_image(' ')
        space_img_width = space_img.get_width()
        space_img_height = space_img.get_height()

        x = self.rect.centerx
        y = self.rect.centery - space_img_height/2

        words = text.split(" ")
        lines = []
        line = []
        w = 0

        for word in words:

            # load the image created from the text
            img = get_text_image(word)
            img_width = img.get_width()

            if w + img_width > self.rect.w:
                # if the image is outside the rectangle, return to the line
                lines.append((x, line))
                y -= space_img_height/2
                x = self.rect.centerx
                line = []
                w = 0


            line.append(img)
            x -= img_width/2
            w += img_width

            if words.index(word) != len(words) - 1:
                line.append(space_img)
                x -= space_img_width/2
                w += space_img_width

        lines.append((x, line))

        # print result

        for line in lines:

            x = line[0]
            images_list = line[1]

            for image in images_list:

                image_width = image.get_width()
                screen.blit(image, (x, y))
                x += image_width

            y += space_img_height


class Button(MenuItem):

    # PROPERTIES

    first_color = blue
    second_color = red

    # CONSTRUCTOR

    def __init__(self, message_key, x, y, image=None, action=None, parameters=None):

        MenuItem.__init__(self, x, y, button_width, button_height)

        # WARNING, positions are relative to the menu
        self.action = action
        self.parameters = parameters

        self.image_key = image

        # the message here is only a key
        if message_key:
            self.message = Message(0, 0, message_key)
            self.message.rect.width = self.rect.width
            self.message.rect.center = self.rect.center
        else:
            self.message = None


    # OVERRIDED FUNCTIONS

    def move_to(self, x, y, w=None, h=None):

        if x:
            self.rect.x += x
            if self.message:
                self.message.rect.x += x
        if y:
            self.rect.y += y
            if self.message:
                self.message.rect.y += y
        if w:
            self.rect.w = w
        if h:
            self.rect.h = h

    # ADDITIONNAL FUNCTIONS

    def execute(self):
        if self.action:
            if self.parameters is not None:
                return self.action(self.parameters)
            else:
                return self.action()

    # DRAWING FUNCTION

    def draw(self, screen):

        if self.cursor_is_on():
            pygame.draw.rect(screen, get_color(self.second_color), self.rect)
        else:
            pygame.draw.rect(screen, get_color(self.first_color), self.rect)

        pygame.draw.rect(screen, get_color(black), self.rect, 2)

        if self.image_key:
            image = get_image(self.image_key, width=button_width, height=button_height)
            screen.blit(image, self.rect.topleft)

        if self.message:
            self.message.draw_centered(screen)
            #smallText = pygame.font.SysFont("comicsansms", 30)
            #textSurf, textRect = text_objects(get_text(self.message), smallText)
            #textRect.center = ((self.rect.x + (button_width / 2)), (self.rect.y + (button_height / 2)))
            #screen.blit(textSurf, textRect)


class ColorBox(MenuItem):

    # PROPERTIES

    # CONSTRUCTOR

    def __init__(self, x, y, color=red, name=''):

        MenuItem.__init__(self, x, y, color_box_width, color_box_height)

        self.color_key = color
        self.active = False
        self.name = name

    # DRAWING FUNCTION

    def draw(self, screen):

        pygame.draw.rect(screen, get_color(self.color_key), self.rect)
        if self.active:
            pygame.draw.rect(screen, get_color(black), self.rect, border)


class InputBox(MenuItem):

    active_color = red
    inactive_color = black

    # PROPERTIES

    # CONSTRUCTORS

    def __init__(self, x, y, text='', name=''):

        MenuItem.__init__(self, x, y, input_box_width, input_box_height)
        # WARNING, positions are relative to the menu
        self.name = name

        self.text = text

        self.initial_width = self.rect.width

        self.active = False

        self.update()

    # FUNCTIONS

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.update()

    def update(self):
        # Resize the box if the text is too long.
        self.rect.w = max(self.initial_width, get_text_image(self.text).get_width()+10)

    # DRAWING FUNCTION

    def draw(self, screen):
        color = self.active_color if self.active else self.inactive_color
        # Blit the text.
        screen.blit(get_text_image(self.text), (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, get_color(color), self.rect, 2)

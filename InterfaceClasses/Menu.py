# coding: utf-8

from Parameters.utils import RectCenter
from Parameters.Colors.Colors import *
from Parameters.Langages.Langages import *
from Parameters.SizesAndPositions.SizesAndPositions import *

from InterfaceClasses.MenuItem import Button, ColorBox, InputBox, Message

class Menu(object):

    # PROPERTIES

    @property
    def buttons(self):
        return self._buttons

    @buttons.setter
    def buttons(self, value):

        if not isinstance(value, list):
            raise Exception("Buttons in menu must be a list.")

        for button in value:
            if not isinstance(button, Button):
                raise Exception("Buttons list must contains only buttons.")

            button.move_to(self.rect.x, self.rect.y)

        self._buttons = value

    @property
    def input_boxes(self):
        return self._inputs

    @input_boxes.setter
    def input_boxes(self, value):

        if not isinstance(value, list):
            raise Exception("Inputs in menu must be a list")

        for input_box in value:
            if not isinstance(input_box, InputBox):
                raise Exception("Inputs list must contains only input boxes.")

            input_box.move_to(self.rect.x, self.rect.y)

        self._inputs = value

    @property
    def color_boxes(self):
        return self._color_boxes

    @color_boxes.setter
    def color_boxes(self, value):

        if not isinstance(value, list):
            raise Exception("Color_boxes in menu must be a list")

        for color_box in value:
            if not isinstance(color_box, ColorBox):
                raise Exception("Color_boxes list must contains only color boxes.")

            color_box.move_to(self.rect.x, self.rect.y)

        self._color_boxes = value

    @property
    def messages(self):
        return self._messages

    @messages.setter
    def messages(self, value):

        if not isinstance(value, list):
            raise Exception("Messages in menu must be a list")

        for message in value:
            if not isinstance(message, Message):
                raise Exception("Messages list must contains only messages.")

            message.move_to(self.rect.x, self.rect.y, w=self.rect.w)

        self._messages = value

    @property
    def quit_button(self):
        return self._quit_button

    @quit_button.setter
    def quit_button(self, value):

        if value is None:
            self._quit_button = value
            return

        if not isinstance(value, Button):
            raise Exception("Quit button must be a button")

        value.move_to(self.rect.x, self.rect.y)

        self._quit_button = value

    @property
    def run(self):
        return self._run

    @run.setter
    def run(self, value):

        if not isinstance(value, bool):
            raise Exception("Menu run must be a boolean")

        self._run = value

    @property
    def cursor_x(self):
        return self._cursor_x

    @cursor_x.setter
    def cursor_x(self, value):

        if not isinstance(value, int):
            raise Exception("Menu cursor_x value must be a number")

        if value < 0:
            raise Exception("Menu cursor_x value must be between positive")

        self._cursor_x = value

    @property
    def cursor_y(self):
        return self._cursor_y

    @cursor_y.setter
    def cursor_y(self, value):

        if not isinstance(value, int):
            raise Exception("Menu cursor_x value must be a number")

        if value < 0:
            raise Exception("Menu cursor_x value must be between positive")

        self._cursor_y = value

    # CONSTRUCTOR

    def __init__(self, parent, buttons=[], inputs=[], colors=[], messages=[],
                 quit_button=None, rect=pygame.Rect(0, 0, window_width, window_height)):

        self.parent = parent
        self.screen = parent.screen

        self.rect = rect

        self.buttons = buttons
        self.input_boxes = inputs
        self.color_boxes = colors
        self.messages = messages
        self.quit_button = quit_button

        self.cursor_x = 0
        self.cursor_y = 0

        self.run = False

        self.parameters = {}

    # FUNCTIONS

    def launch(self):

        self.run = True

        while self.run:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.parent.Quit()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        if self.parent is not None and not self.parent:
                            self.parent.Quit()
                        else:
                            self.run = False

                elif event.type == pygame.KEYDOWN:
                    for input in self.input_boxes:
                        if input.active:
                            input.handle_event(event)
                            self.parameters[input.name] = input.text

                elif event.type == pygame.MOUSEMOTION:
                    self.cursor_x = event.pos[0]
                    self.cursor_y = event.pos[1]
                    self.actualise_cursor()

                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.check_clicked()

            mouse = pygame.mouse.get_pos()
            self.cursor_x = mouse[0]
            self.cursor_y = mouse[1]
            self.actualise_cursor()

            self.draw()

    def check_clicked(self):
        for button in self.buttons:
            if button.cursor_is_on():
                button.execute()
                break

        for input in self.input_boxes:
            if input.cursor_is_on():
                input.active = True
                break
            else:
                input.active = False

        for color_choice in self.color_boxes:
            if color_choice.cursor_is_on():
                for color_bis in [color for color in self.color_boxes if color.name == color_choice.name]:
                    color_bis.active = False
                color_choice.active = True
                self.parameters[color_choice.name] = color_choice.color_key
                break

        if self.quit_button and self.quit_button.cursor_is_on():
            self.quit_button.execute()
            self.run = False

    def actualise_cursor(self):

        for button in self.buttons:
            button.cursor_y = self.cursor_y
            button.cursor_x = self.cursor_x

        for input in self.input_boxes:
            input.cursor_y = self.cursor_y
            input.cursor_x = self.cursor_x

        for color in self.color_boxes:
            color.cursor_y = self.cursor_y
            color.cursor_x = self.cursor_x

        if self.quit_button:
            self.quit_button.cursor_y = self.cursor_y
            self.quit_button.cursor_x = self.cursor_x

    def Quit(self):
        self.parent.Quit()

    # DRAWING FUNCTION

    def draw(self, update=True):

        if self.parent:
            self.parent.draw(update=False)

        pygame.draw.rect(self.screen, get_color(white), self.rect)
        pygame.draw.rect(self.screen, get_color(black), self.rect, 2)

        if self.buttons:
            for button in self.buttons:
                button.draw(self.screen)

        if self.input_boxes:
            for input in self.input_boxes:
                input.draw(self.screen)

        if self.color_boxes:
            for color in self.color_boxes:
                color.draw(self.screen)

        if self.messages:
            for message in self.messages:
                message.draw(self.screen)

        if self.quit_button:
            self.quit_button.draw(self.screen)

        if update:
            pygame.display.update()


class MultipleMessagesMenu(Menu):

    # PROPERTIES

    @property
    def buttons(self):
        return self._buttons

    @buttons.setter
    def buttons(self, value):

        if not isinstance(value, list):
            raise Exception("Buttons in menu must be a list.")

        for button in value:
            if not isinstance(button, Button):
                raise Exception("Buttons list must contains only buttons.")

        self._buttons = value

    @property
    def quit_button(self):
        return self._quit_button

    @quit_button.setter
    def quit_button(self, value):

        if value is None:
            self._quit_button = value
            return

        if not isinstance(value, Button):
            raise Exception("Quit button must be a button")

        self._quit_button = value

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value):

        if not isinstance(value, int):
            raise Exception("Tutorial step must be a number")

        if value < 0:
            raise Exception("Tutorial step value must be positive")

        self._step = value

    # CONSTRUCTOR

    def __init__(self, parent, messages=[]):

        Menu.__init__(self, parent,
                      buttons=[], inputs=[], colors=[], messages=messages,
                      quit_button=None,
                      rect=RectCenter(tutorial_message_px, tutorial_message_py,
                                      tutorial_message_width, tutorial_message_height))

        self.step = 0

        self.only_next_button = Button(text_next_step,
                                       tutorial_message_only_next_button_px + self.rect.x,
                                       tutorial_message_only_next_button_py + self.rect.y, action=self.next_step)

        self.next_button = Button(text_next_step,
                                  tutorial_message_next_button_px + self.rect.x,
                                  tutorial_message_next_button_py + self.rect.y, action=self.next_step)

        self.previous_button = Button(text_previous_step,
                                      tutorial_message_previous_button_px + self.rect.x,
                                      tutorial_message_previous_button_py + self.rect.y, action=self.previous_step)

        self.close_button = Button(text_validate,
                                   tutorial_message_close_button_px + self.rect.x,
                                   tutorial_message_close_button_py + self.rect.y)

        self.actualize_buttons()

    # ADDITONNAL FUNCTIONS

    def next_step(self):
        self.step += 1
        self.actualize_buttons()

    def previous_step(self):
        self.step -= 1
        self.actualize_buttons()

    def actualize_buttons(self):

        if self.step == 0:
            self.buttons = [self.only_next_button]
            self.quit_button = None
        elif self.step == len(self.messages) -1:
            self.buttons = [self.previous_button]
            self.quit_button = self.close_button
        else:
            self.buttons = [self.previous_button, self.next_button]
            self.quit_button = None

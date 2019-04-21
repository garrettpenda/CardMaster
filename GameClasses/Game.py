# coding: utf-8

from IA import *
from PodSixNet.Connection import ConnectionListener, connection
from time import sleep
from GameClasses.Board import *
from GameClasses.Player import *
from Parameters.GameParameters.GameParameters import rounds_to_win
from Parameters.Langages.Langages import *
from InterfaceClasses.MenuItem import Button, Message
from InterfaceClasses.Menu import Menu, MultipleMessagesMenu


class Game(object):

    # PROPERTIES

    # CONSTRUCTORS

    def __init__(self, parent, player):

        # Est ce qu'il n'y a pas une meilleur façon d'avoir acces a la couche du dessus ?
        self.parent = parent

        self.screen = self.parent.screen

        self.board = Board(self, size_of_board, size_of_board, rocks=Coin())

        self.rect_up = pygame.Rect(0, 0,
                                   board_max_right, board_max_top)

        self.rect_left = pygame.Rect(0, board_max_top,
                                     board_max_left, board_max_bottom)

        self.rect_bottom = pygame.Rect(board_max_left, board_max_bottom,
                                       board_max_right, board_max_top)

        self.rect_right = pygame.Rect(board_max_right, 0,
                                      board_max_left, board_max_bottom)

        self.message = Message(0, 0, None)
        self.message.rect.width = self.rect_up.width
        self.message.rect.center = self.rect_up.center

        self.last_winner = None

        self.selected_card = None
        self.selected_case = None

        self.game_over = False
        self.round_over = False

        self.selected_case = None
        self.selected_card = None

        self.played = 0
        self.turn_count = 0


        self.rounds = rounds_to_win
        self.number_of_players = 2
        self.turn = bool(Coin())

        self.init_player(player)
        self.init_opponent()
        self.init_in_game_menu()
        self.init_end_round_menu()
        self.init_end_game_menu()
        self.init_confirm_capitulate_menu()

    # FUNCTIONS

    def play_game(self):

        while not self.game_over:

            self.new_round()

            self.message.text_key = text_choose_card

            self.draw()

            while not self.round_over:

                self.game_loop_function()

                if self.turn:
                    self.play_player_turn(self.player)
                else:
                    self.play_opponnent_turn()

                self.draw()

                if self.all_hands_are_empty():
                    self.launch_end_round_menu()

            if self.player.round == self.rounds or self.opponent.round == self.rounds:
                self.launch_end_game_menu()

    def play_player_turn(self, player):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # confirmation message to capitulate.
                self.parent.Quit()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.in_game_menu.launch()

            elif event.type == pygame.MOUSEMOTION:
                pass

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:

                    click_x = event.pos[0]
                    click_y = event.pos[1]

                    if not self.selected_card and not self.selected_case:
                        self.selected_card = player.select_card(click_x, click_y)
                    elif self.selected_card and not self.selected_case:
                        self.selected_case = self.board.select_case(click_x, click_y)
                        if not self.selected_case:
                            self.selected_card = player.select_card(click_x, click_y)
                    elif self.selected_card and self.selected_case:
                        if self.board.has_click_on_selected_case(click_x, click_y):
                            self.play_selected_card(player)
                        else:
                            self.selected_case = self.board.select_case(click_x, click_y)

                    if not self.selected_card and not self.selected_case:
                        self.message.text_key = text_choose_card
                    elif self.selected_card and not self.selected_case:
                        self.message.text_key = text_choose_case
                    elif self.selected_card and self.selected_case:
                        self.message.text_key = text_validate_case

    def actualize_turn_count(self):
        self.played += 1
        if self.played == self.number_of_players:
            self.turn_count += 1
            self.played = 0

    def actualize_scores(self):

        self.player.score = self.board.get_player_score(self.player.number)
        self.opponent.score = self.board.get_player_score(self.opponent.number)

    def all_hands_are_empty(self):
        return len(self.player.hand) == 0 and len(self.opponent.hand) == 0

    # MENUS

    def init_end_round_menu(self):

        end_round_menu_rect = RectCenter(end_round_menu_px, end_round_menu_py,
                                         end_round_menu_width, end_round_menu_height)

        end_round_menu_continue_button = Button(text_continue, end_round_menu_continue_button_px,
                                                end_round_menu_continue_button_py,
                                                action=self.end_round)

        self.end_round_menu = Menu(self,
                                   quit_button=end_round_menu_continue_button,
                                   messages=[],
                                   rect=end_round_menu_rect)

    def launch_end_round_menu(self):

        draw = self.player.score == self.opponent.score

        if draw:
            end_round_menu_message = Message(end_round_menu_message_px,
                               end_round_menu_message_py, text_draw)
        else:
            winner = self.player if self.player.score > self.opponent.score else self.opponent
            winner.round += 1
            self.last_winner = winner
            end_round_menu_message = Message(end_round_menu_message_px, end_round_menu_message_py,
                                             text_player_won_round, argument=winner.name)

        self.end_round_menu.messages = [end_round_menu_message]

        self.end_round_menu.launch()

    def init_end_game_menu(self):

        end_game_menu_rect = RectCenter(end_game_menu_px, end_game_menu_py,
                                        end_game_menu_width, end_game_menu_height)

        end_game_menu_continue_button = Button(text_continue,
                                               end_game_menu_continue_button_px,
                                               end_game_menu_continue_button_py,
                                               action=self.end_game)

        self.end_game_menu = Menu(self,
                                  quit_button=end_game_menu_continue_button,
                                  messages=[],
                                  rect=end_game_menu_rect)

    def launch_end_game_menu(self):

        winner = self.player if self.player.score ==self.rounds else self.opponent

        end_game_menu_message = Message(end_game_menu_message_px,
                                        end_game_menu_message_py,
                                        text_player_won ,argument=winner.name)

        self.end_game_menu.messages=[end_game_menu_message]

        self.end_game_menu.launch()

    def init_confirm_capitulate_menu(self):

        confirm_capitulate_menu_rect = RectCenter(quit_game_menu_px, quit_game_menu_py,
                                                  confirm_capitulate_menu_width, confirm_capitulate_menu_height)

        confirm_capitulate_menu_message = Message(confirm_capitulate_menu_message_px,
                                                  confirm_capitulate_menu_message_py,
                                                  text_capitulate_game_question)

        confirm_capitulate_menu_yes_button = Button(text_yes,
                                                    confirm_capitulate_menu_yes_button_px,
                                                    confirm_capitulate_menu_yes_button_py, action=self.capitulate)
        confirm_capitulate_menu_no_button = Button(text_no,
                                                   confirm_capitulate_menu_no_button_px,
                                                   confirm_capitulate_menu_no_button_py)

        self.confirm_capitulate_menu = Menu(self,
                                            quit_button=confirm_capitulate_menu_no_button,
                                            buttons=[confirm_capitulate_menu_yes_button],
                                            messages=[confirm_capitulate_menu_message],
                                            rect=confirm_capitulate_menu_rect)

    def launch_confirm_capitulate_menu(self):
        self.confirm_capitulate_menu.launch()

    # OVERRIDED FUNCTIONS

    def init_in_game_menu(self):

        in_game_menu_rect = RectCenter(in_game_menu_px, in_game_menu_py,
                                        in_game_menu_width, in_game_menu_height)

        in_game_menu_capitulate_button = Button(text_capitulate_game,
                                                in_game_menu_capitulate_button_px,
                                                in_game_menu_capitulate_button_py,
                                                action=self.launch_confirm_capitulate_menu)

        in_game_menu_options_button = Button(text_options,
                                             in_game_menu_options_button_px,
                                             in_game_menu_options_button_py,
                                             action=self.parent.launch_options_menu)

        in_game_menu_return_to_game_button = Button(text_return_to_game,
                                                    in_game_menu_return_to_game_button_px,
                                                    in_game_menu_return_to_game_button_py)

        self.in_game_menu = Menu(self,
                                 buttons=[in_game_menu_capitulate_button, in_game_menu_options_button],
                                 quit_button=in_game_menu_return_to_game_button,
                                 rect=in_game_menu_rect)

    def init_player(self, player):
        self.player = player
        self.player.number = 0
        self.player.rect = self.rect_left
        self.player.reset_hand()

    def init_opponent(self):
        self.opponent = Player("myself", blue, self.screen)
        self.opponent.number = 1
        self.opponent.rect = self.rect_right
        self.opponent.reset_hand()

    def capitulate(self):

        self.opponent.round = self.rounds

        self.round_over = True
        self.game_over = True
        self.confirm_capitulate_menu.run = False
        self.in_game_menu.run = False
        self.draw()

    def play_selected_card(self, player):

        player.unselect_all_cards()
        self.board.unselect_all_cases()

        card = player.get_card(self.selected_card.number)
        self.draw()
        self.board.play(card, self.selected_case, None)


        self.actualize_scores()
        self.turn = not self.turn
        self.selected_case = None
        self.selected_card = None

        self.actualize_turn_count()

    def play_opponnent_turn(self):

        self.message.text_key = text_opponent_turn
        self.play_player_turn(self.opponent)

    def game_loop_function(self):
        pass

    def new_round(self):

        self.player.reset_hand()
        self.opponent.reset_hand()

        self.board = Board(self, size_of_board, size_of_board, rocks=True)

        if self.last_winner:
            if self.last_winner.number != self.player.number:
                self.turn = True
            else:
                self.turn = False

        self.actualize_scores()
        self.round_over = False
        self.turn_count = 0
        self.played = 0

    def end_round(self):
        self.end_round_menu.run = False
        self.round_over = True

    def end_game(self):

        self.game_over = True
        self.player.round = 0
        self.opponent.round = 0
        self.player.hand = []
        self.opponent.hand = []

    # DRAWING FUNCTION

    def draw(self, update=True):

        self.screen.fill(get_color(white))

        text_turn = get_text(text_turn_count, text_completion=str(self.turn_count))
        self.screen.blit(get_text_image(text_turn), (self.rect_up.x + 10, self.rect_up.y + 10))

        self.player.draw()

        if self.opponent is not None:
            self.opponent.draw(card_hidden=False)

        pygame.draw.rect(self.screen, get_color(black), self.rect_up, border)
        pygame.draw.rect(self.screen, get_color(black), self.rect_left, border)
        pygame.draw.rect(self.screen, get_color(black), self.rect_bottom, border)
        pygame.draw.rect(self.screen, get_color(black), self.rect_right, border)

        self.message.draw(self.screen)

        self.board.draw(update=False)

        if update:
            pygame.display.update()


class GameOffline(Game):

    def __init__(self, parent, player):

        Game.__init__(self, parent, player)

        self.turn = bool(Coin())

    # FUNCTIONS

    def init_opponent(self):
        self.opponent = Player("IA", clearblue, self.screen)
        self.opponent.rect = self.rect_right
        self.opponent.number = 1
        self.opponent.reset_hand()

    def play_opponnent_turn(self):
        self.message.text_key = text_opponent_turn
        self.draw()
        play_random_card(self.board, self.opponent, self.screen)
        self.actualize_turn_count()
        self.actualize_scores()
        self.turn = True


class GameTutorial(Game):

    def __init__(self, parent, player):

        Game.__init__(self, parent, player)

        self.step = 1
        self.rounds = 5

        parameter_path = directory_path + "/Parameters/tutorials.yaml"
        with open(parameter_path, 'r') as stream:
            try:
                self.configuration = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    # OVERRIDED FUNCTIONS

    def init_in_game_menu(self):

        in_game_tutorial_menu_rect = RectCenter(in_game_tutorial_menu_px, in_game_tutorial_menu_py,
                                                in_game_tutorial_menu_width, in_game_tutorial_menu_height)

        in_game_tutorial_menu_capitulate_button = Button(text_capitulate_game,
                                                         in_game_tutorial_menu_capitulate_button_px,
                                                         in_game_tutorial_menu_capitulate_button_py,
                                                         action=self.launch_confirm_capitulate_menu)

        in_game_tutorial_replay_tutorial_button = Button(text_replay_tutorial,
                                                         in_game_tutorial_menu_replay_tutorial_button_px,
                                                         in_game_tutorial_menu_replay_tutorial_button_py,
                                                         action=self.replay_tutorial)


        in_game_tutorial_menu_options_button = Button(text_options,
                                                      in_game_tutorial_menu_options_button_px,
                                                      in_game_tutorial_menu_options_button_py,
                                                      action=self.parent.launch_options_menu)

        in_game_tutorial_menu_return_to_game_button = Button(text_return_to_game,
                                                             in_game_tutorial_menu_return_to_game_button_px,
                                                             in_game_tutorial_menu_return_to_game_button_py)

        self.in_game_menu = Menu(self,
                                 buttons=[in_game_tutorial_menu_capitulate_button,
                                          in_game_tutorial_replay_tutorial_button,
                                          in_game_tutorial_menu_options_button],
                                 quit_button=in_game_tutorial_menu_return_to_game_button,
                                 rect=in_game_tutorial_menu_rect)

    def init_player(self, player):
        self.player = player
        self.player.number = 0
        self.player.rect = self.rect_left

    def init_opponent(self):
        self.opponent = Player("IA",clearblue, self.screen)
        self.opponent.rect = self.rect_right
        self.opponent.number = 1

    def build_card(self, card_configuration, player):
        number = 5 if 'number' not in card_configuration else card_configuration['number']
        custom_card = Card(number, player.number, player.color, self.screen, number_of_arrows=2)

        custom_card.life_point = card_configuration['life_point']

        custom_card.arrows = {direction: None for direction in Directions.all_directions}
        for direction in card_configuration['arrows']:
            custom_card.arrows[eval(direction)] = Arrow(eval(direction), 0, 0, self.screen)
        return custom_card

    def new_round(self):

        round_configuration = self.configuration['round_%s' % str(self.step)]

        board_configuration = round_configuration['board']
        self.board = Board(self, board_configuration['size_x'], board_configuration['size_y'])
        if board_configuration['crushed']:
            for case in board_configuration['crushed']:
                if not case:
                    continue
                self.board.crush(case['x'], case['y'])

        player_1_configuration = round_configuration['player_1']
        if player_1_configuration['board']:
            for card in player_1_configuration['board']:
                custom_card = self.build_card(card, self.player)
                self.board.get_case(card['x'], card['y']).put(custom_card)
        if player_1_configuration['hand']:
            for card in player_1_configuration['hand']:
                if not card:
                    continue
                custom_card = self.build_card(card, self.player)
                self.player.add_card(custom_card)
            self.player.reset_hand_positions()

        player_2_configuration = round_configuration['player_2']

        if player_2_configuration['board']:
            for card in player_2_configuration['board']:
                custom_card = self.build_card(card, self.opponent)
                self.board.get_case(card['x'], card['y']).put(custom_card)

        if player_2_configuration['hand']:
            for card in player_2_configuration['hand']:
                custom_card = self.build_card(card, self.opponent)
                self.opponent.add_card(custom_card)
                self.opponent.reset_hand_positions()

        self.turn = True
        self.actualize_scores()
        self.turn_count = 0
        self.played = 0
        self.round_over = False
        self.displayed_tutorial_message = False

    def end_round(self):

        self.end_round_menu.run = False
        self.round_over = True
        self.step += 1

    def game_loop_function(self):

        if not self.displayed_tutorial_message:

            messages = []
            message_number = 1
            got_all_message = False
            while(not got_all_message):
                try:
                    text_key = text_tutorial_message % (str(self.step), str(message_number))
                    message = Message(0, 0, text_key)
                    message.test_text_key()
                    messages.append(message)
                    message_number += 1
                except Exception:
                    got_all_message = True
            tutorial_message_menu = MultipleMessagesMenu(self, messages=messages)
            tutorial_message_menu.launch()

            self.displayed_tutorial_message = True

    # DRAWING FUNCTION

    def draw(self, update=True):

        self.screen.fill(get_color(white))

        text_step = get_text(text_step_count, text_completion=str(self.step))
        self.screen.blit(get_text_image(text_step), (self.rect_up.x + 10, self.rect_up.y + 10))

        self.player.draw()

        if self.opponent is not None:
            self.opponent.draw(card_hidden=False)

        pygame.draw.rect(self.screen, get_color(black), self.rect_up, border)
        pygame.draw.rect(self.screen, get_color(black), self.rect_left, border)
        pygame.draw.rect(self.screen, get_color(black), self.rect_bottom, border)
        pygame.draw.rect(self.screen, get_color(black), self.rect_right, border)

        self.message.draw(self.screen)

        self.board.draw(update=False)

        if update:
            pygame.display.update()

    # ADDITIONNAL FUNCTIONS

    def replay_tutorial(self):
        self.in_game_menu.run = False
        self.displayed_tutorial_message = False


class GameOnline(Game, ConnectionListener):

    def __init__(self, parent, player):

        Game.__init__(self, parent, player)
        ConnectionListener.__init__(self)

        self.gameid = None
        self.num = None
        self.found_opponnent = False
        self.server_message = None

        # ONLINE

        self.server_message = None
        self.loaded = False

        self.Connect(("localhost", 8000))
        """
        address = raw_input("Address of Server: ")
        try:
            if not address:
                host, port = "localhost", 8000
            else:
                host, port = address.split(":")
            self.Connect((host, int(port)))
        except:
            print "Error Connecting to Server"
            print "Usage:", "host:port"
            print "e.g.", "localhost:31425"
            exit()
        """

        self.running = False
        while not self.running:
            self.Pump()
            connection.Pump()
            pygame.display.update()
            sleep(0.01)

    # NETWORK
    """ The game is first initialize : it just means two players are in the same room
    then, they send their informations to each other and the game then start"""

    def Network_init_game(self, data):
        # game trouvee, chargment des infos
        self.found_opponnent = True
        self.num = data["player"]

        self.player.number = self.num
        self.player.reset_hand()
        self.gameid = data["gameid"]

        self.Send({"action": "init_player", "gameid": self.gameid, "num": self.num, "player": str(self.player)})

    def Network_crushcase(self, data):
        X = data["X"]
        Y = data["Y"]
        self.board.crush(X, Y)

    def Network_init_opponnent(self, data):
        self.opponent = build_player_from_json(eval(str(data['player'])))
        self.loaded = True
        self.Send({"action": "loaded", "gameid": self.gameid, "num": self.num})

    def Network_startgame(self, data):
        self.running = True
        self.turn = data["turn"] == self.num

    def Network_yourturn(self, data):
        self.turn = data["torf"]

    def Network_place(self, data):
        print("place card")
        # get attributes
        x = data["x"]
        y = data["y"]
        order_fights = data["order_fights"]
        card = build_card_from_json(eval(data['card']))
        # card.check()
        self.opponent.get_card(card.number)  # remove the card from the opponnent hands
        case = self.board.get_case(x, y)
        self.board.play(card, case, order_fights)
        self.actualize_scores()

    def Network_end_game(self, data):
        print("game is over")
        if self.loaded:
            self.actualize_rounds()
        else:
            print("should not happened receive message ending a not initiated game.")

    def Network_close(self, data):
        print(
            "We have an engine failure. Emergency systems are offline. Abandon ship, WE'RE GOING DOWN !! There is no time to evacuate, this is the end. ARRRRRRGHHHH !!! THERE IS NO GOD !!!")
        exit()

    # FUNCTIONS

    def play_selected_card(self, player):

        player.unselect_all_cards()
        self.board.unselect_all_cases()

        card = player.get_card(self.selected_card.number)
        card_string = str(card)
        self.draw()
        order_fights = self.board.play(card, self.selected_case, None)

        self.Send({"action": "place", "x": self.selected_case.x, "card": card_string, "y": self.selected_case.y,
                   "gameid": self.gameid,
                   "num": self.num, "order_fights": order_fights})

        self.actualize_scores()
        self.turn = not self.turn
        self.selected_case = None
        self.selected_card = None

    def game_loop_function(self):
        connection.Pump()
        self.Pump()

    def end_round(self):
        self.game_over = True
        self.Send({"action": "no_cards", "gameid": self.gameid, "num": self.num})

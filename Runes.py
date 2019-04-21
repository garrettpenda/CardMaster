# coding: utf-8

from GameClasses.Game import Game, GameOffline, GameOnline, GameTutorial
from GameClasses.Player import *
from Parameters.Langages.Langages import *
from Parameters.Images.Images import *
from InterfaceClasses.Menu import Menu
from InterfaceClasses.MenuItem import Button, ColorBox, InputBox, Message

# TODO : commit sur git lab

# TODO : faire des repos distant pour les classes ?

# TODO : le menu quitter le jeu doit pouvoir se fermer avec echap

# TODO : faire le relation parent pour tout les objects

# TODO : definir les properties pour toutes les classes

# TODO : changement couleur ne doit pas etre possible dans le menu ingame ( faire un menu options special je pense)

# TODO : definir toutes les size relative dans le yaml aussi

# TODO : faire un bouton menu dans le jeu

# TODO : le joueur qui a perdu choisis qui commence

# TODO : faire une classe HAND pour le joueur qui contient 5 cases ( sera utile pour la navigation avec fleche aussi )

# TODO : trouver un moyen de recharger les tailles aussi

# TODO : Refaire une passe sur les variable a mettre dans les yaml

 ## OPTIONS

# TODO : faire un menu pour les langues et un autre pour les couleurs

# TODO : faire une option pour enlever le double click sur les cases

# TODO : faire une option pour desactiver les tips

##  TESTS ( le truc le plus long a faire actuellement )

# TODO : faire/refaire/corriger/finir les tests pour toutes les classes BOARD, GAME, PLAYER, LES INTERFACES ET LA CONF YAML

## SERVEUR ( plus rien ne marche ici mais ca devrait pas être long a réparer )

# TODO : réparer le mode en ligne ( essayer pulsar ? )

# TODO : faire la game contre l'ordi en ligne

# TODO : trouver pourquoi on recoie le end_game quand on rejoue.

# TODO : faire le bouton annuler pendant la recherche d'adversaire

# TODO : faire plusieurs file dans le server

# TODO : faire que le server demande quel type de partie jouer avant de mettre dans la file

# TODO : meilleur gestion des joueurs sur le serveur ( a linitialisation et pendant la game ( en fonction de leur numero en base serai le top )

## IA

# TODO : ameliorer l'ia
# TODO: perfect place( obliger de combattre pour prendre), combo, attack, lose one card to combo next turn etc

## BUGS

## FEATURES

# TODO : mettre des images avec les messages dans le tutoriel

# TODO : afficher des messages pendant les chargements

# TODO : faire des games regle speciales

# TODO : RAJOUTER LA GESTION DU MODE MANETTE / clavier ce qui necessite des coordonnees dans les menu, case etc

# TODO : zoom sur les cartes ou le board ?

# TODO : mettre des sons

# TODO : mettre plus images ( Dos de carte, fond ecran ) == inkscape, gimp

# TODO : faire que le message daffichage du gagnant ne cache pas le terrain

# TODO : faire le mode 3 joueurs

## BASE DE DONNES

# TODO : Faire la base de donnees (enregistrement utilisateur, joueur stats, ia stats )

# TODO : Faire l'enregistremenent de l'historique dans la base de donnees

# TODO : faire le site web avec django derriere


class Runes():

    def __init__(self):
        #1
        pygame.init()
        pygame.font.init()
        #2
        #initialize the screen
        self.screen = pygame.display.set_mode((window_width, window_height))

        pygame.display.set_caption("Runes")

        pygame.key.set_repeat(400, 30)
        #3
        #initialize pygame clock
        self.clock = pygame.time.Clock()

        self.player = None

        self.init_connexion_menu()
        self.init_main_menu()
        self.init_quit_game_menu()
        self.init_options_menu()
        self.init_online_menu()
        self.init_offline_menu()
        self.init_work_in_progress_menu()


    def __bool__(self):
        # To avoid trying to draw this class with menus
        return False


    def create_game(self):
        game = Game(self, self.player)
        game.play_game()

    def create_game_versus_ia(self):
        game = GameOffline(self, self.player, self.screen)
        game.play_game()

    def create_game_tutorial(self):
        game = GameTutorial(self, self.player, self.screen)
        game.play_game()

    def exit(self):
        exit()

    def Quit(self):
        self.quit_game_menu.launch()

    # MENUS

    # CONNEXION MENU

    def init_connexion_menu(self):

        connexion_menu_choose_name_message = Message(connexion_menu_choose_name_message_px,
                                                     connexion_menu_choose_name_message_py,
                                                     text_enter_login)

        connexion_menu_name_input_box = InputBox(connexion_menu_name_input_box_px,
                                                 connexion_menu_name_input_box_py,
                                                 "", name='player_name')

        connexion_menu_choose_element_message = Message(connexion_menu_choose_element_message_px,
                                                        connexion_menu_choose_element_message_py,
                                                        text_choose_color)

        connexion_menu_red_choice = ColorBox(connexion_menu_red_choice_px,
                                             connexion_menu_red_choice_py, red, name='player_color')
        connexion_menu_blue_choice = ColorBox(connexion_menu_blue_choice_px,
                                              connexion_menu_blue_choice_py, blue, name='player_color')
        connexion_menu_yellow_choice = ColorBox(connexion_menu_yellow_choice_px,
                                                connexion_menu_yellow_choice_py, yellow, name='player_color')
        connexion_menu_green_choice = ColorBox(connexion_menu_green_choice_px,
                                               connexion_menu_green_choice_py, green, name='player_color')
        connexion_menu_brown_choice = ColorBox(connexion_menu_brown_choice_px,
                                               connexion_menu_brown_choice_py, brown, name='player_color')
        connexion_menu_grey_choice = ColorBox(connexion_menu_grey_choice_px,
                                              connexion_menu_grey_choice_py, grey, name='player_color')
        connexion_menu_purple_choice = ColorBox(connexion_menu_purple_choice_px,
                                                connexion_menu_purple_choice_py, purple, name='player_color')
        connexion_menu_clear_blue_choice = ColorBox(connexion_menu_clear_blue_choice_px,
                                                    connexion_menu_clear_blue_choice_py, clearblue, name='player_color')

        connexion_menu_connect_button = Button(text_connexion,
                                               connexion_menu_connect_button_px,
                                               connexion_menu_connect_button_py,
                                               action=self.launch_main_menu)

        connexion_menu_quit_button = Button(text_quit_game,
                                            connexion_menu_quit_button_px,
                                            connexion_menu_quit_button_py,
                                            action=self.launch_quit_game_menu)

        connexion_menu_french_button = Button(None,
                                              connexion_menu_french_button_px,
                                              connexion_menu_french_button_py,
                                              image=french_flag_image_key,
                                              action=load_texts, parameters=(french_key))

        connexion_menu_english_button = Button(None,
                                               connexion_menu_english_button_px,
                                               connexion_menu_english_button_py,
                                              image=english_flag_image_key,
                                              action=load_texts, parameters=(english_key))

        self.connexion_menu = Menu(self,
                                   buttons=[connexion_menu_french_button,connexion_menu_english_button,
                                            connexion_menu_connect_button, connexion_menu_quit_button],
                                   inputs=[connexion_menu_name_input_box],
                                   messages=[connexion_menu_choose_name_message, connexion_menu_choose_element_message],
                                   colors=[connexion_menu_red_choice, connexion_menu_blue_choice,
                                           connexion_menu_yellow_choice, connexion_menu_green_choice,
                                           connexion_menu_brown_choice, connexion_menu_grey_choice,
                                           connexion_menu_purple_choice, connexion_menu_clear_blue_choice])

    # MAIN MENU

    def init_main_menu(self):
        main_menu_play_online_button = Button(text_online_menu,
                                              main_menu_play_online_button_px,
                                              main_menu_play_online_button_py,
                                              action=self.launch_online_game_menu)

        main_menu_play_offline_button = Button(text_offline_menu,
                                               main_menu_play_offline_button_px,
                                               main_menu_play_offline_button_py,
                                               action=self.launch_offline_game_menu)

        main_menu_option_button = Button(text_options,
                                         main_menu_option_button_px,
                                         main_menu_option_button_py, action=self.launch_options_menu)

        main_menu_chest_button = Button(text_chest,
                                        main_menu_chest_button_px,
                                        main_menu_chest_button_py, action=self.launch_work_in_progress_menu)

        main_menu_quit_button = Button(text_quit_game,
                                       main_menu_quit_button_px,
                                       main_menu_quit_button_py, action=self.launch_quit_game_menu)

        self.main_menu = Menu(self,
                              buttons=[main_menu_play_online_button,
                                       main_menu_play_offline_button,
                                       main_menu_option_button,
                                       main_menu_chest_button,
                                       main_menu_quit_button])

    def launch_main_menu(self):
        #print(str(self.connexion_menu.parameters))
        name = self.connexion_menu.parameters.get('player_name')
        color = self.connexion_menu.parameters.get('player_color')
        if not name or not color:
            return
        self.player = Player(name, color, self.screen)
        self.connexion_menu.run = False
        self.back_ground_menu = self.main_menu
        self.main_menu.launch()

    # OPTIONS MENU

    def init_options_menu(self):

        options_menu_french_button = Button(None,
                                            options_menu_french_button_px,
                                            options_menu_french_button_py,
                                              image=french_flag_image_key,
                                              action=load_texts, parameters=(french_key))

        options_menu_english_button = Button(None,
                                             options_menu_english_button_px,
                                             options_menu_english_button_py,
                                               image=english_flag_image_key,
                                               action=load_texts, parameters=(english_key))

        options_menu_choose_element_message = Message(options_menu_choose_element_message_px,
                                                      options_menu_choose_element_message_py,
                                                        text_choose_color)

        options_menu_red_choice = ColorBox(options_menu_red_choice_px,
                                           options_menu_red_choice_py, red, name='player_color')
        options_menu_blue_choice = ColorBox(options_menu_blue_choice_px,
                                            options_menu_blue_choice_py, blue, name='player_color')
        options_menu_yellow_choice = ColorBox(options_menu_yellow_choice_px,
                                              options_menu_yellow_choice_py, yellow, name='player_color')
        options_menu_green_choice = ColorBox(options_menu_green_choice_px,
                                             options_menu_green_choice_py, green, name='player_color')
        options_menu_brown_choice = ColorBox(options_menu_brown_choice_px,
                                             options_menu_brown_choice_py, brown, name='player_color')
        options_menu_grey_choice = ColorBox(options_menu_grey_choice_px,
                                            options_menu_grey_choice_py, grey, name='player_color')
        options_menu_purple_choice = ColorBox(options_menu_purple_choice_px,
                                              options_menu_purple_choice_py, purple, name='player_color')
        options_menu_clear_blue_choice = ColorBox(options_menu_clear_blue_choice_px,
                                                  options_menu_clear_blue_choice_py, clearblue, name='player_color')

        options_online_menu_return_to_main_menu_button = Button(text_return_to_menu,
                                                                options_online_menu_return_to_main_menu_button_px,
                                                                options_online_menu_return_to_main_menu_button_py)

        self.options_menu = Menu(self.main_menu,
                                 buttons=[options_menu_french_button,
                                          options_menu_english_button],
                                 colors=[options_menu_red_choice,options_menu_blue_choice,
                                         options_menu_yellow_choice,options_menu_green_choice,
                                         options_menu_brown_choice, options_menu_grey_choice,
                                         options_menu_purple_choice, options_menu_clear_blue_choice],
                                 messages=[options_menu_choose_element_message],
                                 quit_button=options_online_menu_return_to_main_menu_button
                                 )

    def launch_options_menu(self):
        for color_box in self.options_menu.color_boxes:
            if color_box.color_key == self.player.color:
                color_box.active = True
                self.options_menu.parameters['player_color'] = self.player.color
        self.options_menu.launch()
        self.player.color = self.options_menu.parameters.get('player_color')

    # ONLINE MENU

    def init_online_menu(self):

        play_online_menu_2_players_game_button = Button(text_start_2_players_game,
                                                        play_online_menu_2_players_game_button_px,
                                                        play_online_menu_2_players_game_button_py,
                                                        action=self.launch_work_in_progress_menu)

        play_online_menu_3_players_game_button = Button(text_start_3_players_game,
                                                        play_online_menu_3_players_game_button_px,
                                                        play_online_menu_3_players_game_button_py,
                                                        action=self.launch_work_in_progress_menu)

        play_online_menu_return_to_main_menu_button = Button(text_return_to_menu,
                                                         oneline_menu_return_to_main_menu_button_px,
                                                         oneline_menu_return_to_main_menu_button_py)

        self.online_game_menu = Menu(self.main_menu,
                                     buttons=[play_online_menu_2_players_game_button,
                                              play_online_menu_3_players_game_button],
                                     quit_button=play_online_menu_return_to_main_menu_button)

    def launch_online_game_menu(self):
        self.online_game_menu.launch()

    # OFFLINE MENU

    def init_offline_menu(self):

        play_offline_menu_versus_ia_game_button = Button(text_start_game_versus_ia,
                                                         play_offline_menu_versus_ia_game_button_px,
                                                         play_offline_menu_versus_ia_game_button_py,
                                                         action=self.create_game_versus_ia)
        play_offline_menu_tutorial_game_button = Button(text_tutotial, play_offline_menu_tutorial_game_button_px,
                                                        play_offline_menu_tutorial_game_button_py,
                                                        action=self.create_game_tutorial)

        play_offline_menu_test_game_button = Button(text_test_game,
                                                    play_offline_menu_test_game_button_px,
                                                    play_offline_menu_test_game_button_py,
                                                    action=self.create_game)

        play_offline_menu_return_to_main_menu_button = Button(text_return_to_menu,
                                                              play_offline_menu_return_to_main_menu_button_px,
                                                              play_offline_menu_return_to_main_menu_button_py)

        self.offline_game_menu = Menu(self.main_menu,
                                      buttons=[play_offline_menu_versus_ia_game_button,
                                               play_offline_menu_tutorial_game_button,
                                               play_offline_menu_test_game_button],
                                      quit_button=play_offline_menu_return_to_main_menu_button)

    def launch_offline_game_menu(self):
        self.offline_game_menu.launch()

    # WORK IN PROGRESS MENU

    def init_work_in_progress_menu(self):

        work_in_progress_menu_rect = RectCenter(work_in_progress_menu_px, work_in_progress_menu_py,
                                                 work_in_progress_menu_width, work_in_progress_menu_height)

        work_in_progress_menu_message = Message(work_in_progress_menu_message_px,
                                                work_in_progress_menu_message_py,
                                                text_work_in_progress)

        work_in_progress_menu_quit_button = Button(text_validate,
                                                   work_in_progress_menu_quit_button_px,
                                                   work_in_progress_menu_quit_button_py)

        self.work_in_progress_menu = Menu(self.main_menu,
                                          quit_button=work_in_progress_menu_quit_button,
                                          messages=[work_in_progress_menu_message],
                                          rect=work_in_progress_menu_rect)

    def launch_work_in_progress_menu(self):
        self.work_in_progress_menu.launch()

    # QUIT GAME MENU

    def init_quit_game_menu(self):

        quit_game_menu_rect = RectCenter(quit_game_menu_px, quit_game_menu_py,
                                         quit_game_menu_width, quit_game_menu_height)

        quit_game_menu_message = Message(quit_game_menu_message_px,
                                         quit_game_menu_message_py,
                                         text_quit_game_question)

        quit_game_menu_yes_button = Button(text_yes,
                                           quit_game_menu_yes_button_px,
                                           quit_game_menu_yes_button_py, action=self.exit)
        quit_game_menu_no_button = Button(text_no, quit_game_menu_no_button_px,
                                          quit_game_menu_no_button_py)

        self.quit_game_menu = Menu(self,
                                   quit_button=quit_game_menu_no_button,
                                   buttons=[quit_game_menu_yes_button],
                                   messages=[quit_game_menu_message],
                                   rect=quit_game_menu_rect)

    def launch_quit_game_menu(self):
        self.quit_game_menu.launch()

    def draw(self, update=True):
        pass


if __name__ == '__main__':

    runes = Runes()

    runes.connexion_menu.launch()


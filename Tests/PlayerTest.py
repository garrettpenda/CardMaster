from GameClasses.Player import *
import pytest

one = 1
name = "name"
tuple_ones = (one, one, one)


# ========================
# PLAYER PROPERTIES TESTS
# ========================


class TestPlayerNameClass(object):

    def test_player_name_is_none(self):
        with pytest.raises(PlayerParameterException):
            Player(None, tuple_ones)

    def test_player_name_is_not_str(self):
        with pytest.raises(PlayerParameterException):
            Player(2, tuple_ones)


class TestPlayerColorClass(object):

    def test_player_color_is_none(self):
        with pytest.raises(PlayerParameterException):
            Player(name, None)

    def test_player_color_not_tuple(self):
        with pytest.raises(PlayerParameterException):
            Player(name, "Tests")

    def test_player_color_size_too_small(self):
        with pytest.raises(PlayerParameterException):
            Player(name, (1, 1))

    def test_player_color_size_too_high(self):
        with pytest.raises(PlayerParameterException):
            Player(name, (1, 1, 1, 1))

    def test_player_color_r_not_number(self):
        with pytest.raises(PlayerParameterException):
            Player(name, ("Tests", 1, 1))

    def test_player_color_r_negative(self):
        with pytest.raises(PlayerParameterException):
            Player(name, (-1, 1, 1))

    def test_player_color_r_to_big(self):
        with pytest.raises(PlayerParameterException):
            Player(name, (300, 1, 1))

    def test_player_color_r_decimal(self):
        with pytest.raises(PlayerParameterException):
            Player(name, (3.5, 1, 1))

    def test_player_color_g_not_number(self):
        with pytest.raises(PlayerParameterException):
            Player(name, (1, "Tests", 1))

    def test_player_color_g_negative(self):
        with pytest.raises(PlayerParameterException):
            Player(name, (1, -1, 1))

    def test_player_color_g_to_big(self):
        with pytest.raises(PlayerParameterException):
            Player(name, (1, 300, 1))

    def test_player_color_g_decimal(self):
        with pytest.raises(PlayerParameterException):
            Player(name, (1, 3.5, 1))

    def test_player_color_b_not_number(self):
        with pytest.raises(PlayerParameterException):
            Player(name, (1, 1, "Tests"))

    def test_player_color_b_negative(self):
        with pytest.raises(PlayerParameterException):
            Player(name, (1, 1, -1))

    def test_player_color_b_to_big(self):
        with pytest.raises(PlayerParameterException):
            Player(name, (1, 1, 300))

    def test_player_color_b_decimal(self):
        with pytest.raises(PlayerParameterException):
            Player(name, (1, 1, 3.5))


class TestPlayerNumberClass(object):

    def test_player_number_is_not_number(self):
        with pytest.raises(PlayerParameterException):
            player = Player(name, tuple_ones)
            player.number = "Tests"

    def test_player_number_negative(self):
        with pytest.raises(PlayerParameterException):
            player = Player(name, tuple_ones)
            player.number = -1

    def test_player_number_decimal(self):
        with pytest.raises(PlayerParameterException):
            player = Player(name, tuple_ones)
            player.number = 3.5


class TestPlayerScoreClass(object):

    def test_player_score_is_not_number(self):
        with pytest.raises(PlayerParameterException):
            player = Player(name, tuple_ones)
            player.score = "Tests"

    def test_player_score_negative(self):
        with pytest.raises(PlayerParameterException):
            player = Player(name, tuple_ones)
            player.score = -1


    def test_player_score_decimal(self):
        with pytest.raises(PlayerParameterException):
            player = Player(name, tuple_ones)
            player.score = 3.5


class TestPlayerRoundClass(object):

    def test_player_round_is_not_number(self):
        with pytest.raises(PlayerParameterException):
            player = Player(name, tuple_ones)
            player.round = "Tests"

    def test_player_py_negative(self):
        with pytest.raises(PlayerParameterException):
            player = Player(name, tuple_ones)
            player.round = -1

    def test_player_py_decimal(self):
        with pytest.raises(PlayerParameterException):
            player = Player(name, tuple_ones)
            player.round = 3.5


class TestPlayerHandClass(object):
    
    def test_player_hand_is_none(self):
        with pytest.raises(PlayerParameterException):
            Player(name, one).hand = None

    def test_player_hand_is_not_list(self):
        with pytest.raises(PlayerParameterException):
            Player(name, one).hand = "Tests"

    def test_player_hand_is_not_card(self):
        with pytest.raises(PlayerParameterException):
            Player(name, one).hand = ["Tests"]

    def test_player_hand_card_is_not_is_own(self):
        with pytest.raises(PlayerParameterException):
            Player(name, one).hand = [Card(one, 2, tuple_ones)]

    def test_player_hand_card_contains_multiple_cards_selected(self):
        with pytest.raises(PlayerParameterException):
            player = Player(name, one)
            card1 = Card(one, one, tuple_ones)
            card1.is_selected = True
            card2 = Card(2, one, tuple_ones)
            card2.is_selected = True
            player.hand = [card1, card2]

    def test_player_hand_card_contains_multiple_cards_with_same_number(self):
        with pytest.raises(PlayerParameterException):
            Player(name, one).hand = [Card(one, one, tuple_ones),Card(one, one, tuple_ones)]


# =======================
# PLAYER CONSTRUCTORS TEST
# =======================


class TestCardConstructorClass(object):

    def test_card_init_values(self):

        card = Card(1, 2, (20, 60, 100))

        assert card.player == 2
        assert card.number == 1
        assert card.color == (20, 60, 100)

        assert card.px == 0
        assert card.py == 0

        assert card.combo_percent == 0
        assert card.combo_color is None
        assert card.combo_direction is None
        assert card.combo_arrow_directions == []

        assert card.life_point in [16, 18]
        assert card.max_life_point in [16, 18]

        assert not card.is_selected

        assert len(card.arrows) == len(Directions.all_directions)
        for direction in Directions.all_directions:
            assert card.arrows.get(direction) is not None
            assert isinstance(card.arrows.get(direction), bool)

        assert card.rect.x == 0
        assert card.rect.y == 0
        assert card.rect.w == card_width
        assert card.rect.h == card_height

        assert card.name == "12"


# ====================
# PLAYER FUNCTIONS TEST
# ====================


class TestCardFunctionsClass(object):

    # GET ARROWS DIRECTIONS

    def test_card_get_arrows_directions_function(self):

        for number_of_arrows in range(1, 3):

            card = Card(one, one, tuple_ones)

            arrows_direction = card.get_arrows_directions()

            assert isinstance(arrows_direction, list)

            assert len(arrows_direction) == card.number_of_arrows

            for direction in arrows_direction:
                assert direction in Directions.all_directions

    # SET POSITIONS

    def test_card_set_positions_function(self):
        pass

    # REBORN

    def test_card_reborn_function(self):

        for number_of_arrows in range(1, 2):

            card = Card(one, one, tuple_ones)

            maxlp = card.max_life_point

            card.reborn()

            assert card.life_point == int(maxlp / 2)

    # RESET COMBO

    def test_card_reset_combo_function(self):
        card = Card(one, one, tuple_ones)
        card.combo_percent = 2
        card.combo_color = (0, 0, 0)
        card.combo_direction = 2
        card.reset_combo()
        assert card.combo_percent == 0
        assert card.combo_color is None
        assert card.combo_direction is None

    # CHANGE PLAYER

    @staticmethod
    def check_card_change_player_function_arguments(player_number, color):
        card = Card(one, one, tuple_ones)
        try:
            card.change_player(player_number, color)
            return True
        except CardParameterException:
            return False

    def test_card_change_player_function(self):

        assert not self.check_card_change_player_function_arguments("Tests", tuple_ones)
        assert not self.check_card_change_player_function_arguments(-1, tuple_ones)

        assert not self.check_card_change_player_function_arguments(one, "Tests")
        assert not self.check_card_change_player_function_arguments(one, (1, 1))
        assert not self.check_card_change_player_function_arguments(one, (1, 1, 1, 1))

        assert not self.check_card_change_player_function_arguments(one, ("Tests", 1, 1))
        assert not self.check_card_change_player_function_arguments(one, (-1, 1, 1))
        assert not self.check_card_change_player_function_arguments(one, (300, 1, 1))

        assert not self.check_card_change_player_function_arguments(one, (1, "Tests", 1))
        assert not self.check_card_change_player_function_arguments(one, (1, -1, 1))
        assert not self.check_card_change_player_function_arguments(one, (1, 300, 1))

        assert not self.check_card_change_player_function_arguments(one, (1, 1, "Tests"))
        assert not self.check_card_change_player_function_arguments(one, (1, 1, -1))
        assert not self.check_card_change_player_function_arguments(one, (1, 1, 300))

        assert self.check_card_change_player_function_arguments(one, tuple_ones)

        card = Card(one, one, tuple_ones)
        card.change_player(4, (20, 40, 60))
        assert card.player == 4
        assert card.color == (20, 40, 60)

    # IS CURSOR ON

    @staticmethod
    def check_card_is_cursor_on_function_arguments(x, y):
        card = Card(one, one, tuple_ones)
        try:
            card.is_cursor_on(x, y)
            return True
        except CardFunctionParameterException:
            return False

    def test_card_is_cursor_on_function(self):

        assert not self.check_card_is_cursor_on_function_arguments("Tests", one)
        assert not self.check_card_is_cursor_on_function_arguments(-1, one)

        assert not self.check_card_is_cursor_on_function_arguments(one, "Tests")
        assert not self.check_card_is_cursor_on_function_arguments(one, -1)

        card = Card(one, one, tuple_ones)
        for x in range(0, card_width + 100):
            for y in range(0, card_height + 100):
                if x < card_width and y < card_height:
                    assert card.is_cursor_on(x, y)
                else:
                    assert not card.is_cursor_on(x, y)

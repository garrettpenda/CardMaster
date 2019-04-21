import pytest
from GameClasses.Card import *

one = 1
tuple_ones = (one, one, one)


# ======================
# CARD PROPERTIES TESTS
# ======================


class TestCardNumberClass(object):

    @pytest.mark.parametrize("card_number", [None, "Tests", -1, 0, 10, 1.5])
    def test_card_number(self, card_number):
        with pytest.raises(CardParameterException):
            Card(card_number, one, tuple_ones)


class TestCardPlayerClass(object):

    @pytest.mark.parametrize("card_player", [None, "Tests", -1,  1.5])
    def test_card_player(self, card_player):
        with pytest.raises(CardParameterException):
            Card(one, card_player, tuple_ones)


class TestCardColorClass(object):

    @pytest.mark.parametrize("card_color", [None, "Tests", (1,1), (1,1,1,1)])
    def test_card_color(self, card_color):
        with pytest.raises(CardParameterException):
            Card(one, one, card_color)

    @pytest.mark.parametrize("r", [None, "Tests", -1, 300, 3.5])
    def test_card_color_r(self, r):
        with pytest.raises(CardParameterException):
            Card(one, one, (r, one, one))

    @pytest.mark.parametrize("g", [None, "Tests", -1, 300, 3.5])
    def test_card_color_g(self, g):
        with pytest.raises(CardParameterException):
            Card(one, one, (one, g, one))

    @pytest.mark.parametrize("b", [None, "Tests", -1, 300, 3.5])
    def test_card_color_b(self, b):
        with pytest.raises(CardParameterException):
            Card(one, one, (one, one, b))


class TestCardNumberOfArrowsClass(object):

    @staticmethod
    def invalid_number_of_arrows(card, number_of_arrows):
        try:
            card.number_of_arrows = number_of_arrows
            return False
        except CardParameterException:
            return True

    @staticmethod
    def card_5_invalid_number_of_arrows(number_of_arrows):
        try:
            Card(5, one, tuple_ones, number_of_arrows=number_of_arrows)
            return False
        except CardParameterException:
            return True

    @pytest.mark.parametrize("number_of_arrow", [None, "Tests", -1, 0, 10, 3.5])
    def test_card_number_of_arrows_is_none(self, number_of_arrow):
        with pytest.raises(CardParameterException):
            Card(one, one, tuple_ones).number_of_arrows = number_of_arrow

    def test_card_1_invalid_number_of_arrows(self):
        card = Card(1, one, tuple_ones)

        for number_of_arrows in range(1, 9):

            if number_of_arrows in range(1, 3):
                assert not self.invalid_number_of_arrows(card, number_of_arrows)
            else:
                assert self.invalid_number_of_arrows(card, number_of_arrows)

    def test_card_2_invalid_number_of_arrows(self):
        card = Card(2, one, tuple_ones)

        for number_of_arrows in range(1, 9):

            if number_of_arrows in range(2, 5):
                assert not self.invalid_number_of_arrows(card, number_of_arrows)
            else:
                assert self.invalid_number_of_arrows(card, number_of_arrows)

    def test_card_3_invalid_number_of_arrows(self):
        card = Card(3, one, tuple_ones)

        for number_of_arrows in range(1, 9):

            if number_of_arrows in range(3, 7):
                assert not self.invalid_number_of_arrows(card, number_of_arrows)
            else:
                assert self.invalid_number_of_arrows(card, number_of_arrows)

    def test_card_4_invalid_number_of_arrows(self):
        card = Card(4, one, tuple_ones)

        for number_of_arrows in range(1, 9):

            if number_of_arrows == 4:
                assert not self.invalid_number_of_arrows(card, number_of_arrows)
            else:
                assert self.invalid_number_of_arrows(card, number_of_arrows)

    def test_card_5_invalid_number_of_arrows(self):

        for number_of_arrows in range(1, 9):
            if number_of_arrows in range(2, 9):
                assert not self.card_5_invalid_number_of_arrows(number_of_arrows)
            else:
                assert self.card_5_invalid_number_of_arrows(number_of_arrows)


class TestCardPxClass(object):

    @pytest.mark.parametrize("position_x", [None, "Tests", -1, 3.5])
    def test_card_px(self, position_x):
        with pytest.raises(CardParameterException):
            Card(one, one, tuple_ones).px = position_x


class TestCardPyClass(object):

    @pytest.mark.parametrize("position_y", [None, "Tests", -1, 3.5])
    def test_card_py(self, position_y):
        with pytest.raises(CardParameterException):
            Card(one, one, tuple_ones).py = position_y


class TestCardIsSelectedClass(object):

    @pytest.mark.parametrize("selected", [None, "Tests"])
    def test_card_is_selected(self, selected):
        with pytest.raises(CardParameterException):
            Card(one, one, tuple_ones).is_selected = selected


class TestCardLifePointClass(object):

    @pytest.mark.parametrize("life", [None, "Tests", -1, 100, 3.5])
    def test_card_life_point(self, life):
        with pytest.raises(CardParameterException):
            Card(one, one, tuple_ones).life_point = life


class TestCardMaxLifePointClass(object):

    @pytest.mark.parametrize("max_life", [None, "Tests", -1, 3, 3.5, 100])
    def test_card__max_life_point(self, max_life):
        with pytest.raises(CardParameterException):
            Card(one, one, tuple_ones).max_life_point = max_life


class TestCardArrowsClass(object):

    def test_card_arrows_is_none(self):
        with pytest.raises(CardParameterException):
            Card(one, one, tuple_ones).arrows = None

    def test_card_arrows_is_not_dict(self):
        with pytest.raises(CardParameterException):
            Card(one, one, tuple_ones).arrows = "Tests"

    def test_card_arrows_incorrect_length(self):
        with pytest.raises(CardParameterException):
            Card(one, one, tuple_ones).arrows = {0: False, 1: False, 2: False}

    def test_card_arrows_key_not_direction(self):
        with pytest.raises(CardParameterException):
            Card(one, one, tuple_ones).arrows = \
                {0: False, 1: False, 2: False, "Tests": False, 4: False, 5: False, 6: False, 7: False}

    def test_card_arrows_value_not_bool(self):
        with pytest.raises(CardParameterException):
            Card(one, one, tuple_ones).arrows = \
                {0: False, 1: "Tests", 2: False, 3: False, 4: False, 5: False, 6: False, 7: False}


class TestCardComboPercentClass(object):

    @pytest.mark.parametrize("percent", [None, "Tests", -1,  3.5, 1000])
    def test_card_combo_percent(self, percent):
        with pytest.raises(CardParameterException):
            Card(one, one, tuple_ones).combo_percent = percent


class TestCardComboColorClass(object):


    @pytest.mark.parametrize("color", ["Tests", (1,1), (1,1,1,1)])
    def test_card_combo_color(self, color):
        with pytest.raises(CardParameterException):
            Card(one, one, tuple_ones).combo_color = color

    @pytest.mark.parametrize("r", [None, "Tests", -1, 300, 3.5])
    def test_card_combo_color_r(self, r):
        with pytest.raises(CardParameterException):
            Card(one, one, tuple_ones).combo_color = (r, one, one)

    @pytest.mark.parametrize("g", [None, "Tests", -1, 300, 3.5])
    def test_card_combo_color_g(self, g):
        with pytest.raises(CardParameterException):
            Card(one, one, tuple_ones).combo_color = (one, g, one)

    @pytest.mark.parametrize("b", [None, "Tests", -1, 300, 3.5])
    def test_card_combo_color_b(self, b):
        with pytest.raises(CardParameterException):
            Card(one, one, tuple_ones).combo_color = (one, one, b)


class TestCardComboDirectionClass(object):

    @pytest.mark.parametrize("direction", ["Tests", -1, 300, 3.5])
    def test_card_combo_direction(self, direction):
        with pytest.raises(CardParameterException):
            Card(one, one, tuple_ones).combo_direction = direction


class TestCardNameClass(object):

    @pytest.mark.parametrize("card_name", [None, 2])
    def test_card_name_is_none(self, card_name):
        with pytest.raises(CardParameterException):
            Card(one, one, tuple_ones).name = card_name



class TestCardRectClass(object):

    def test_card_rect_is_none(self):
        with pytest.raises(CardParameterException):
            Card(one, one, tuple_ones).rect = None

    def test_card_rect_is_not_rect(self):
        with pytest.raises(CardParameterException):
            Card(one, one, tuple_ones).rect = "Tests"

    def test_card_rect_is_x_is_incorrect(self):
        with pytest.raises(CardParameterException):
            card = Card(one, one, tuple_ones)
            card.rect = pygame.Rect(4, card.py, card_width, card_height)

    def test_card_rect_is_y_is_incorrect(self):
        with pytest.raises(CardParameterException):
            card = Card(one, one, tuple_ones)
            card.rect = pygame.Rect(card.px, 4, card_width, card_height)

    def test_card_rect_is_w_is_incorrect(self):
        with pytest.raises(CardParameterException):
            card = Card(one, one, tuple_ones)
            card.rect = pygame.Rect(card.px, card.py, 4, card_height)

    def test_card_rect_is_h_is_incorrect(self):
        with pytest.raises(CardParameterException):
            card = Card(one, one, tuple_ones)
            card.rect = pygame.Rect(card.px, card.py, card_width, 4)


# =======================
# CARD CONSTRUCTORS TEST
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

        assert card.life_point in [16, 18]
        assert card.max_life_point in [16, 18]

        assert not card.is_selected

        assert len(card.arrows) == len(Directions.all_directions)
        for direction in Directions.all_directions:
            assert card.arrows.get(direction) is None or isinstance(card.arrows.get(direction), Arrow)

        assert card.rect.x == 0
        assert card.rect.y == 0
        assert card.rect.w == card_width
        assert card.rect.h == card_height

        assert card.name == "12"


# ====================
# CARD FUNCTIONS TEST
# ====================

class TestCardGetArrowDirectionsFunctionClass(object):

    def test_card_get_arrow_directions_function_result_is_a_list(self):
        card = Card(one, one, tuple_ones)
        arrows_direction = card.get_arrows_directions()
        assert isinstance(arrows_direction, list)

    def test_card_get_arrow_directions_function_result_length(self):
        card = Card(one, one, tuple_ones, number_of_arrows=2)
        arrows_direction = card.get_arrows_directions()
        assert len(arrows_direction) == card.number_of_arrows

    def test_card_get_arrow_directions_function_result_contains_only_directions(self):
        card = Card(one, one, tuple_ones)
        arrows_direction = card.get_arrows_directions()
        for direction in arrows_direction:
            assert direction in Directions.all_directions


class TestCardSetPositionsFunctionClass(object):

    def test_card_set_positions_function(self):
        pass


class TestCardRebornFunctionClass(object):

    def test_card_reborn_function(self):

        for number_of_arrows in range(1, 2):

            card = Card(one, one, tuple_ones)

            maxlp = card.max_life_point

            card.reborn()

            assert card.life_point == int(maxlp / 2)


class TestCardResetComboFunctionClass(object):

    def test_card_reset_combo_function(self):
        card = Card(one, one, tuple_ones)
        card.combo_percent = 2
        card.combo_color = (0, 0, 0)
        card.combo_direction = 2
        card.reset_combo()
        assert card.combo_percent == 0
        assert card.combo_color is None
        assert card.combo_direction is None


class TestCardChangePlayerFunctionClass(object):

    @pytest.mark.parametrize("card_player", [None, "Tests", -1,  1.5])
    def test_card_card_change_player_function_player(self, card_player):
        with pytest.raises(CardParameterException):
            card = Card(one, one, tuple_ones)
            card.change_player(card_player, tuple_ones)

    @pytest.mark.parametrize("card_color", [None, "Tests", (1, 1), (1, 1, 1, 1)])
    def test_card_card_change_player_function_color(self, card_color):
        with pytest.raises(CardParameterException):
            card = Card(one, one, tuple_ones)
            card.change_player(one, card_color)

    @pytest.mark.parametrize("r", [None, "Tests", -1, 300, 3.5])
    def test_card_card_change_player_function_color_r(self, r):
        with pytest.raises(CardParameterException):
            card = Card(one, one, tuple_ones)
            card.change_player(one, (r, one, one))

    @pytest.mark.parametrize("g", [None, "Tests", -1, 300, 3.5])
    def test_card_card_change_player_function_color_g(self, g):
        with pytest.raises(CardParameterException):
            card = Card(one, one, tuple_ones)
            card.change_player(one, (one, g, one))

    @pytest.mark.parametrize("b", [None, "Tests", -1, 300, 3.5])
    def test_card_card_change_player_function_color_b(self, b):
        with pytest.raises(CardParameterException):
            card = Card(one, one, tuple_ones)
            card.change_player(one, (one, b, one))

    def test_card_change_player_function_work(self):
        card = Card(one, one, tuple_ones)
        card.change_player(4, (20, 40, 60))
        assert card.player == 4
        assert card.color == (20, 40, 60)


class TestCardIsCursorOnFunctionClass(object):

    def test_card_is_cursor_on_function_first_argument_is_not_number(self):
        with pytest.raises(CardFunctionParameterException):
            card = Card(one, one, tuple_ones)
            card.is_cursor_on("Tests", one)

    def test_card_is_cursor_on_function_first_argument_is_negative(self):
        with pytest.raises(CardFunctionParameterException):
            card = Card(one, one, tuple_ones)
            card.is_cursor_on(-1, one)

    def test_card_is_cursor_on_function_first_argument_is_decimal(self):
        with pytest.raises(CardFunctionParameterException):
            card = Card(one, one, tuple_ones)
            card.is_cursor_on(3.5, one)

    def test_card_is_cursor_on_function_second_argument_is_not_number(self):
        with pytest.raises(CardFunctionParameterException):
            card = Card(one, one, tuple_ones)
            card.is_cursor_on(one, "Tests")

    def test_card_is_cursor_on_function_second_argument_is_negative(self):
        with pytest.raises(CardFunctionParameterException):
            card = Card(one, one, tuple_ones)
            card.is_cursor_on(one, -1)

    def test_card_is_cursor_on_function_second_argument_is_decimal(self):
        with pytest.raises(CardFunctionParameterException):
            card = Card(one, one, tuple_ones)
            card.is_cursor_on(one, 3.5)

    def test_card_is_cursor_on_function_work(self):
        card = Card(one, one, tuple_ones)
        for x in range(0, card_width + 100):
            for y in range(0, card_height + 100):
                if x < card_width and y < card_height:
                    assert card.is_cursor_on(x, y)
                else:
                    assert not card.is_cursor_on(x, y)

    @pytest.mark.parametrize("test_input,expected", [
        ("3+5", 8),
        ("2+4", 6),
    ])
    def test_eval(self, test_input, expected):
        assert eval(test_input) == expected

    @pytest.mark.parametrize("x", [0, 1])
    @pytest.mark.parametrize("y", [2, 3])
    def test_foo(self, x, y):
        pass
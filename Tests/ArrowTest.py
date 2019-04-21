
from GameClasses.Arrow import *
import pytest

one = 1
tuple_ones = (one, one, one)


# =================
# PROPERTIES TESTS
# =================


class TestArrowDirectionClass(object):

    def test_arrow_direction_is_not_number(self):
        with pytest.raises(ArrowParameterException):
            Arrow("Tests", one, one)

    def test_arrow_direction_negative(self):
        with pytest.raises(ArrowParameterException):
            Arrow(-1, one, one)

    def test_arrow_direction_too_high(self):
        with pytest.raises(ArrowParameterException):
            Arrow(1000, one, one)

    def test_arrow_direction_decimal(self):
        with pytest.raises(ArrowParameterException):
            Arrow(3.5, one, one)


class TestArrowPxClass(object):

    def test_arrow_px_is_not_number(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, "Tests", tuple_ones)

    def test_arrow_px_negative(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, -1, tuple_ones)

    def test_arrow_px_decimal(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, 3.5, tuple_ones)


class TestArrowPyClass(object):

    def test_arrow_py_is_not_number(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, "Tests")

    def test_arrow_py_negative(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, -1)

    def test_arrow_py_decimal(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, 3.5)


class TestArrowColorClass(object):

    def test_arrow_color_is_none(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one, color=None)

    def test_arrow_color_not_tuple(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one, color="Tests")

    def test_arrow_color_size_too_small(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one, color=(1, 1))

    def test_arrow_color_size_too_high(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one, color=(1, 1, 1, 1))

    def test_arrow_color_r_not_number(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one, color=("Tests", 1, 1))

    def test_arrow_color_r_negative(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one, color=(-1, 1, 1))

    def test_arrow_color_r_to_big(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one, color=(300, 1, 1))

    def test_arrow_color_r_decimal(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one, color=(3.5, 1, 1))

    def test_arrow_color_g_not_number(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one, color=(1, "Tests", 1))

    def test_arrow_color_g_negative(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one, color=(1, -1, 1))

    def test_arrow_color_g_to_big(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one, color=(1, 300, 1))

    def test_arrow_color_g_decimal(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one, color=(1, 3.5, 1))

    def test_arrow_color_b_not_number(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one, color=(1, 1, "Tests"))

    def test_arrow_color_b_negative(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one, color=(1, 1, -1))

    def test_arrow_color_b_to_big(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one, color=(1, 1, 300))

    def test_arrow_color_b_decimal(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one, color=(1, 1, 3.5))


class TestArrowPolygoneClass(object):

    def test_arrow_polygone_is_none(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = None

    def test_arrow_polygone_is_not_list(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = "Tests"

    def test_arrow_polygone_incorrect_length(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = []

    def test_arrow_polygone_1_not_list(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = ["Tests", [one, one], [one, one]]

    def test_arrow_polygone_1_incorect_length(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = [[one], [one, one], [one, one]]

    def test_arrow_polygone_1_coor_1_not_number(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = [["Tests", one], [one, one], [one, one]]

    def test_arrow_polygone_1_coor_2_not_number(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = [[one, "Tests"], [one, one], [one, one]]

    def test_arrow_polygone_1_coor_1_negative(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = [[-1, one], [one, one], [one, one]]

    def test_arrow_polygone_1_coor_2_negative(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = [[one, -1], [one, one], [one, one]]

    def test_arrow_polygone_2_not_list(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = [[one, one], "Tests", [one, one]]

    def test_arrow_polygone_2_incorect_length(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = [[one, one], [one], [one, one]]

    def test_arrow_polygone_2_coor_1_not_number(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = [[one, one], ["Tests", one], [one, one]]

    def test_arrow_polygone_2_coor_2_not_number(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = [[one, one], [one, "Tests"], [one, one]]

    def test_arrow_polygone_2_coor_1_negative(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = [[one, one], [-1, one], [one, one]]

    def test_arrow_polygone_2_coor_2_negative(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = [[one, one], [one, -1], [one, one]]

    def test_arrow_polygone_3_not_list(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = [[one, one], [one, one], "Tests"]

    def test_arrow_polygone_3_incorect_length(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = [[one, one], [one, one], [one]]

    def test_arrow_polygone_3_coor_1_not_number(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = [[one, one], [one, one], ["Tests", one]]

    def test_arrow_polygone_3_coor_2_not_number(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = [[one, one], [one, one], [one, "Tests"]]

    def test_arrow_polygone_3_coor_1_negative(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = [[one, one], [one, one], [-1, one]]

    def test_arrow_polygone_3_coor_2_negative(self):
        with pytest.raises(ArrowParameterException):
            Arrow(one, one, one).polygone = [[one, one], [one, one], [one, -1]]


# =======================
# ARROW CONSTRUCTOR TEST
# =======================


class TestArrowConstructorClass(object):

    def test_arrow_init_values(self):

        arrow = Arrow(1, 2, 3, color=red)
        assert arrow.direction == 1
        assert arrow.px == 2
        assert arrow.py == 3
        assert arrow.color == red
        assert arrow.polygone is not None

    def test_arrow_bool_value(self):
        assert Arrow(one, one, one)


# ====================
# ARROW FUNCTIONS TEST
# ====================


class TestArrowFunctionsClass(object):

    def test_arrow_set_position_function(self):

        arrow = Arrow(one, one, one)
        arrow.set_position(2, 3)
        assert arrow.px == 2
        assert arrow.py == 3

    def test_arrow_reset_polygone_function(self):
        pass

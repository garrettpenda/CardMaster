from GameClasses.Case import *
import pytest
import pygame

one = 1
tuple_ones = (one, one, one)

# =================
# PROPERTIES TESTS
# =================

class TestCaseXClass(object):

    def test_case_x_is_not_number(self):
        with pytest.raises(CaseParameterException):
            Case("Tests", one, one, one)

    def test_case_x_negative(self):
        with pytest.raises(CaseParameterException):
            Case(-1, one, one, one)

    def test_case_x_too_high(self):
        with pytest.raises(CaseParameterException):
            Case(10, one, one, one)

    def test_case_x_decimal(self):
        with pytest.raises(CaseParameterException):
            Case(3.5, one, one, one)


class TestCaseYClass(object):

    def test_case_y_is_not_number(self):
        with pytest.raises(CaseParameterException):
            Case(one, "Tests", one, one)

    def test_case_y_negative(self):
        with pytest.raises(CaseParameterException):
            Case(one, -1, one, one)

    def test_case_y_too_high(self):
        with pytest.raises(CaseParameterException):
            Case(one, 10, one, one)

    def test_case_y_decimal(self):
        with pytest.raises(CaseParameterException):
            Case(one, 3.5, one, one)


class TestCaseBoardPxClass(object):

    def test_case_board_rect_is_None(self):
        with pytest.raises(CaseParameterException):
            Case(one, one, None, one)

    def test_case_board_rect_is_not_number(self):
        with pytest.raises(CaseParameterException):
            Case(one, one, -1, one)

    def test_case_board_rect_is_not_decimal(self):
        with pytest.raises(CaseParameterException):
            Case(one, one, 3.5, one)


class TestCaseBoardPyClass(object):

    def test_case_board_rect_is_None(self):
        with pytest.raises(CaseParameterException):
            Case(one, one, one, None)

    def test_case_board_rect_is_not_number(self):
        with pytest.raises(CaseParameterException):
            Case(one, one, one, -1)

    def test_case_board_rect_is_not_decimal(self):
        with pytest.raises(CaseParameterException):
            Case(one, one, one, 3.5)


class TestCaseInsideClass(object):

    def test_case_is_selected_is_not_bool(self):
        with pytest.raises(CaseParameterException):
            Case(one, one, one, one).inside = "Tests"


class TestCaseIsSelectedClass(object):

    def test_case_is_selected_is_none(self):
        with pytest.raises(CaseParameterException):
            Case(one, one, one, one).is_selected = None

    def test_case_is_selected_is_not_bool(self):
        with pytest.raises(CaseParameterException):
            Case(one, one, one, one).is_selected = "Tests"


class TestCaseIsCrushedClass(object):

    def test_case_is_crushed_is_none(self):
        with pytest.raises(CaseParameterException):
            Case(one, one, one, one).is_crushed = None

    def test_case_is_selected_is_not_bool(self):
        with pytest.raises(CaseParameterException):
            Case(one, one, one, one).is_crushed = "Tests"


class TestCasePxClass(object):

    def test_case_px_is_not_number(self):
        with pytest.raises(CaseParameterException):
            Case(one, one, one, one).px = "Tests"

    def test_case_px_negative(self):
        with pytest.raises(CaseParameterException):
            Case(one, one, one, one).px = -1

    def test_case_px_decimal(self):
        with pytest.raises(CaseParameterException):
            Case(one, one, one, one).px = 3.5


class TestCasePyClass(object):

    def test_case_py_is_not_number(self):
        with pytest.raises(CaseParameterException):
            Case(one, one, one, one).py = "Tests"

    def test_case_py_negative(self):
        with pytest.raises(CaseParameterException):
            Case(one, one, one, one).py = -1

    def test_case_py_decimal(self):
        with pytest.raises(CaseParameterException):
            Case(one, one, one, one).py = 3.5


class TestCaseRectClass(object):

    def test_case_rect_is_none(self):
        with pytest.raises(CaseParameterException):
            Case(one, one, one, one).rect = None

    def test_case_rect_is_not_rect(self):
        with pytest.raises(CaseParameterException):
            Case(one, one, one, one).rect = "Tests"

    def test_case_rect_is_x_is_incorrect(self):
        with pytest.raises(CaseParameterException):
            case = Case(one, one, one, one)
            case.rect = pygame.Rect(4, case.py, case_width, case_height)

    def test_case_rect_is_y_is_incorrect(self):
        with pytest.raises(CaseParameterException):
            case = Case(one, one, one, one)
            case.rect = pygame.Rect(case.px, 4, case_width, case_height)

    def test_case_rect_is_w_is_incorrect(self):
        with pytest.raises(CaseParameterException):
            case = Case(one, one, one, one)
            case.rect = pygame.Rect(case.px, case.py, 4, case_height)

    def test_case_rect_is_h_is_incorrect(self):
        with pytest.raises(CaseParameterException):
            case = Case(one, one, one, one)
            case.rect = pygame.Rect(case.px, case.py, case_width, 4)


# =======================
# CASE CONSTRUCTORS TEST
# =======================


class TestCaseConstructorClass(object):

    def test_case_init_values(self):

        case = Case(1, 2, one, one)
        assert case.x == 2
        assert case.y == 1


# ====================
# CASE FUNCTIONS TEST
# ====================


class TestCasePutFunctionClass(object):

    def test_case_put_function_on_occupied_case(self):
        with pytest.raises(CaseParameterException):
            case = Case(one, one, one, one)
            case.put(Card(one, one, tuple_ones))
            case.put(Card(one, one, tuple_ones))

    def test_case_put_function_on_crushed_case(self):
        with pytest.raises(CaseParameterException):
            case = Case(one, one, one, one)
            case.crush()
            case.put(Card(one, one, tuple_ones))

    def test_case_put_function_change_card_x_value(self):
        case = Case(2, 1, one, one)
        case.put(Card(one, one, tuple_ones))
        assert case.inside.x == 1

    def test_case_put_function_change_card_y_value(self):
        case = Case(1, 2, one, one)
        case.put(Card(one, one, tuple_ones))
        assert case.inside.y == 1

    def test_case_put_function_change_card_px_value(self):
        case = Case(one, one, one, one)
        case.put(Card(one, one, tuple_ones))
        assert case.inside.px == case.px + 2

    def test_case_put_function_change_card_py_value(self):
        case = Case(one, one, one, one)
        case.put(Card(one, one, tuple_ones))
        assert case.inside.py == case.py + 2

    def test_case_put_function_check_card_rect_x(self):
        case = Case(one, one, one, one)
        case.put(Card(one, one, tuple_ones))
        assert case.inside.rect.x == case.px + 2

    def test_case_put_function_check_card_rect_y(self):
        case = Case(one, one, one, one)
        case.put(Card(one, one, tuple_ones))
        assert case.inside.rect.y == case.py + 2

    def test_case_put_function_check_card_rect_width(self):
        case = Case(one, one, one, one)
        case.put(Card(one, one, tuple_ones))
        assert case.inside.rect.w == card_width

    def test_case_put_function_check_card_rect_height(self):
        case = Case(one, one, one, one)
        case.put(Card(one, one, tuple_ones))
        assert case.inside.rect.h == card_height

    def test_case_crush_function_delete_inside(self):
        case = Case(one, one, one, one)
        assert not case.is_occupied()
        case.put(Card(one, one, tuple_ones))
        assert case.is_occupied()


class TestCaseCrushFunctionClass(object):

    def test_case_crush_function_result(self):
        case = Case(one, one, one, one)
        assert not case.is_crushed
        case.crush()
        assert case.is_crushed

    def test_case_crush_function_delete_inside(self):
        case = Case(one, one, one, one)
        case.put(Card(one, one, tuple_ones))
        case.crush()
        assert not case.is_occupied()


class TestCaseIsOccupiedFunctionClass(object):

    def test_case_is_occupied_function_result_is_bool(self):
        case = Case(one, one, one, one)
        assert isinstance(case.is_occupied(), bool)

    def test_case_is_occupied_function_result(self):
        case = Case(one, one, one, one)
        assert not case.is_occupied()
        case.put(Card(one, one, tuple_ones))
        assert case.is_occupied()


class TestCaseIsCursorOnFunctionClass(object):

    def test_case_is_cursor_on_function_first_argument_is_not_number(self):
        with pytest.raises(CaseParameterException):
            case = Case(one, one, one, one)
            case.is_cursor_on("Tests", one)

    def test_case_is_cursor_on_function_first_argument_is_negative(self):
        with pytest.raises(CaseParameterException):
            case = Case(one, one, one, one)
            case.is_cursor_on(-1, one)

    def test_case_is_cursor_on_function_first_argument_is_decimal(self):
        with pytest.raises(CaseParameterException):
            case = Case(one, one, one, one)
            case.is_cursor_on(3.5, one)

    def test_case_is_cursor_on_function_second_argument_is_not_number(self):
        with pytest.raises(CaseParameterException):
            case = Case(one, one, one, one)
            case.is_cursor_on(one, "Tests")

    def test_case_is_cursor_on_function_second_argument_is_negative(self):
        with pytest.raises(CaseParameterException):
            case = Case(one, one, one, one)
            case.is_cursor_on(one, -1)

    def test_case_is_cursor_on_function_second_argument_is_decimal(self):
        with pytest.raises(CaseParameterException):
            case = Case(one, one, one, one)
            case.is_cursor_on(one, 3.5)

    def test_case_is_cursor_on_function_work(self):
        case = Case(one, one, one, one)
        for x in range(0, case_width + 100):
            for y in range(0, case_height + 100):
                if x < case_width and y < case_height:
                    assert case.is_cursor_on(x, y)
                else:
                    assert not case.is_cursor_on(x, y)

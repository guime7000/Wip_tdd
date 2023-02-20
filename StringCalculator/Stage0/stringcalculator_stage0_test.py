from stringcalculator_stage0 import (
    calculate,
    rewrite_empty_expression,
    split_expression,
)


############## rewrite_empty_expression #######################
def test_rewrite_empty_expression() -> None:
    """Returns "0" if input is an empty string"""
    assert rewrite_empty_expression("") == "0"


def test_rewrite_empty_expression() -> None:
    """Doesn't do anything to input if input string's length > 0"""
    assert rewrite_empty_expression("123,456") == "123,456"


############### split_expression #############################
def test_split_comma_separated_expression() -> None:
    """
    Splits a string around comma delimiters
    """
    assert split_expression("1,2,3") == ["1", "2", "3"]


################ calculate ####################################
def test_calculate_empty_string() -> None:
    """If an empty string is given as parameter, should return 0"""
    assert calculate("") == 0


def test_calculate_1_Arg_eq_0() -> None:
    """1 argument equals to 0 returns 0"""
    assert calculate("0") == 0


def test_calculate_1_Arg_eq_123() -> None:
    """1 argument equals to 123 returns 123"""
    assert calculate("123") == 123


def test_calculate_2_comma_sep_Args() -> None:
    """2 comma separated args as entry ("1,4"), returns 5 (= 1 + 4)"""
    assert calculate("1,4") == 5


def test_calculate_3_comma_sep_Args() -> None:
    """3 comma separated args as entry ("1,2,3"), returns 6 (= 1 + 2 + 3)"""
    assert calculate("1,2,3") == 6


def test_calculate_5_comma_sep_Args() -> None:
    """5 comma separated args as entry ("1,2,3,4,5"), returns 15 (= 1 + 2 + 3 + 4 + 5)"""
    assert calculate("1,2,3,4,5") == 15


def test_calculate_tt_delimiter_with_3_sep_Args_() -> None:
    """3 comma separated args as entry ("1,2,3"), returns 6 (= 1 + 2 + 3)"""
    assert calculate("1t2t3", "t") == 6

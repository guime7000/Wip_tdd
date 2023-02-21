from stringcalculator import (
    check_expression_validity,
    rewrite_empty_expression,
    split_expression,
    calculate,
)


# ############# check_expresssion_validity ######################
# def test_check_expresssion_validity() -> None:
#     assert check_expresssion_validity("1,") == "Invalid expression"  # : '1,'"


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
    assert split_expression("1,2,3") == [1, 2, 3]


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


def test_calculate_several_lines() -> None:
    """Includes test of an expression containing \n instruction"""
    assert calculate("1,2\n3") == 6


def test_calculate_invalid_END_comma_expression() -> None:
    """Returns a specific error message if input expression is not ending with a number"""
    assert calculate("1,") == "Invalid expression: '1,'"


def test_calculate_invalid_START_comma_expression() -> None:
    """Returns a specific error message if input expression is not ending with a number"""
    assert calculate(",1") == "Invalid expression: ',1'"


def test_calculate_invalid_user_def_delimiter_expression() -> None:
    assert calculate("//;\n102,5") == "Invalid expression: '//;\n102,5'"


def test_calculate_user_def_1_char_delimiter() -> None:
    assert calculate("//@\n10@20@30") == 60


def test_calculate_negative_numbers_1() -> None:
    assert calculate("1,-2") == "negatives not allowed: -2"


def test_calculate_negative_numbers_2() -> None:
    assert calculate("5,-4,1,-2") == "negatives not allowed: -4, -2"


def test_calculate_eq_1000() -> None:
    assert calculate("1000") == 1000


def test_calculate_greater_1000() -> None:
    assert calculate("1001") == 0


def test_calculate_less_and_great_than_1000() -> None:
    assert calculate("54,1020") == 54

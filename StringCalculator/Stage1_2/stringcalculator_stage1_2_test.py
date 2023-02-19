from stringcalculator_stage1_2 import calculate, parse_expression, converts_to_integer

##################### parse_expression #######################

def test_parse_expression_empty_In() -> None:
    assert parse_expression("") == ['']

def test_parse_expression_1_arg() -> None:
    assert parse_expression("1") == ['1']

def test_parse_expression_2_arg() -> None:
    assert parse_expression("1,2") == ['1','2']

################# converts_to_integer# #############################

def test_converts_to_integer() -> None :
    assert converts_to_integer(['1','2','3']) == [1,2,3]

################ calculate ####################################
def test_calculate_empty_string() -> None:
    """ If an empty string is given as parameter, should return 0 """
    assert calculate("") == 0 

def test_calculate_1_Arg_eq_0() -> None:
    """ 1 argument equals to 0 returns 0"""
    assert calculate("0") == 0

def test_calculate_1_Arg_eq_123() -> None:
    """ 1 argument equals to 123 returns 123"""
    assert calculate("123") == 123

def test_calculate_2_comma_sep_Args() -> None:
    """ 2 comma separated args as entry ("1,4"), returns 5 (= 1 + 4)"""
    assert calculate("1,4") == 5

def test_calculate_3_comma_sep_Args() -> None:
    """ 3 comma separated args as entry ("1,2,3"), returns 6 (= 1 + 2 + 3)"""
    assert calculate("1,2,3") == 6

def test_calculate_5_comma_sep_Args() -> None:
    """ 5 comma separated args as entry ("1,2,3,4,5"), returns 15 (= 1 + 2 + 3 + 4 + 5)"""
    assert calculate("1,2,3,4,5") == 15

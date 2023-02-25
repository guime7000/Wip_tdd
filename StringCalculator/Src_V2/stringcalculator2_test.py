from stringcalculator2 import calculate


def test_calculate_empty_string() -> None:
    assert calculate("") == 0


def test_calculate_1_nb() -> None:
    assert calculate("0") == 0
    assert calculate("2") == 2
    assert calculate("10") == 10


def test_calculate_2_nb() -> None:
    assert calculate("2,3") == 5
    assert calculate("20,30") == 50
    assert calculate("70,123") == 193


def test_calculate_3_nb() -> None:
    assert calculate("1,2,4") == 7
    assert calculate("10,20,40") == 70
    assert calculate("120,25,300") == 445


def test_calculate_4_nb() -> None:
    assert calculate("1,2,4,100") == 107


def test_calculate_with_new_lines() -> None:
    assert calculate("1\n2") == 3
    assert calculate("1,2\n3") == 6
    assert calculate("1\n2,4") == 7


def test_calculate_check_validity() -> None:
    assert calculate("1,") == "Invalid expression : '1,'"
    assert calculate("//;\n102,5") == "Invalid expression : '//;\n102,5'"


def test_1_char_user_delimiter() -> None:
    assert calculate("//;\n1;2") == 3
    assert calculate("//;\n1;2\n3") == 6
    assert calculate("//@\n10@20@30") == 60


def test_calculate_detect_negatives() -> None:
    assert calculate("1,-2") == "negatives not allowed: -2"
    assert calculate("5,-4,1,-2") == "negatives not allowed: -4, -2"


def test_calculate_upon_limit() -> None:
    assert calculate("1001") == 0
    assert calculate("1000") == 1000
    assert calculate("54,1000") == 1054
    assert calculate("54,1001") == 54


def test_1_variable_size_delimiter() -> None:
    assert calculate("//{***}\n5***20") == 25

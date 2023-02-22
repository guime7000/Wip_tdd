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

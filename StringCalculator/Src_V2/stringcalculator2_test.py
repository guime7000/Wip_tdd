from stringcalculator2 import calculate


def test_calculate_1_nb() -> None:
    assert calculate("0") == 0
    assert calculate("2") == 2


def test_calculate_2_nb() -> None:
    assert calculate("2,3") == 5
    assert calculate("20,30") == 50

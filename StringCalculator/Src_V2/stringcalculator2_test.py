from stringcalculator2 import calculate


def test_calculate_1_nb() -> None:
    assert calculate("0") == "0"
    assert calculate("2") == "2"


def test_calculate_2_nb() -> None:
    assert calculate("23,541") == 564

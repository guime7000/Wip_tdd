from katabigbang import bigbang, is_multiple_of

def test_is_multiple_of_3_and_5() -> None :
    """Returns False as 3 is not a multiple of 5"""
    assert is_multiple_of(3,5) == False

def test_is_multiple_of_14_and_7() -> None :
    """Returns True as 14 is a multiple of 7"""
    assert is_multiple_of(14,7) == True


def test_bigbang_multiple_of_5()-> None:
    """Tests if a multiple of 5 is returned as big"""
    assert bigbang(15) == "big"

def test_bigbang_multiple_of_7()-> None:
    """Tests if a multiple of 7 is returned as big"""
    assert bigbang(21) == "bang"

def test_bigbang_multiple_of_11()-> None:
    """Tests if a multiple of 11 is returned as big"""
    assert bigbang(33) == "boom"    

def test_bigbang_multiple_of_5_7_11() -> None :
    """Tests if a multiple of 5 AND 7 AND 11 returns bigbangboom"""
    assert bigbang(385) == "bigbangboom"

def test_bigbang_multiple_of_5_2() -> None:
    """ Tests if a multiple of 5 AND 2 returns big"""
    assert bigbang(10) == "big"

def test_bigbang_multiple_of_11_2() -> None:
    """ Tests if a multiple of 11 AND 2 returns big"""
    assert bigbang(110) == "boombig"

def test_bigbang_odd_non_multiple() -> None:
    """ Tests if an odd integer NOT multiple of 5, 7 or 11 returns its value"""
    assert bigbang(3) == "3"    

def test_bigbang_even_non_multiple() -> None:
    """ Tests if an even integer NOT multiple of 5, 7 or 11 returns its value"""
    assert bigbang(2) == "2"    
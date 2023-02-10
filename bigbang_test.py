from katabigbang import bigbang

def test_bigbang_multiple_of_5()-> None:
    """Tests if a multiple of 5 is returned as big"""
    assert bigbang(15) == "big"

def test_bigbang_multiple_of_7()-> None:
    """Tests if a multiple of 7 is returned as big"""
    assert bigbang(21) == "bang"

def test_bigbang_multiple_of_33()-> None:
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
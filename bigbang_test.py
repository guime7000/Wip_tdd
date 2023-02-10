from katabigbang import bigbang

def test_bigbang_multiple_of_5()-> None:
    """Tests if a multiple of 5 is returned as big"""
    assert bigbang(15) == "big"

def test_bigbang_multiple_of_7()-> None:
    """Tests if a multiple of 7 is returned as big"""
    assert bigbang(21) == "bang"

def test_bigbang_multiple_of_33()-> None:
    """Tests if a multiple of 11 is returned as big"""
    assert bigbang(21) == "bang"    
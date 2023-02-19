def is_multiple_of(testedNumber: int, divisor: int) -> bool :
    """
    Returns true if testedNumber is a multiple of divisor, False otherwise
    """
    return testedNumber % divisor == 0

def divisor_mapping() -> dict :
    """
    Returns a dict containing pairs of divisor / corresponding word

    Modify divisorMap as you wish to fit your needs in bigbang function :
    each key / value pair of the dictionnary corresponds to an int value as key (divisor) and a string as value 
    """
    divisorMap = {5 : "big",
                7 : "bang",
                11 : "boom"}

    return divisorMap

def create_word_list(testedNumber: int, wordMap : dict) -> list :
    """
    Checks if a testedNumber value is a multiple of some divisors.
    If so, appends a specific word to a WordList list 
    Then returns the WordList
    """
    wordList = []
    for key in wordMap.keys():
        if is_multiple_of(testedNumber, key):
            wordList.append(wordMap[key])

    return wordList

def reverse_word_list(testedNumber: int, divisor: int, wordList: list) -> list :
    """
    Returns a reversed wordList if testedNumber is a multiple of divisor
    Returns wordList otherwise
    """
    if is_multiple_of(testedNumber, divisor):
        wordList.reverse()
    
    return wordList


def bigbang(testedNumber : int) -> str :
    """
    Returns a specific string given conditions on the testedNumber integer parameter.
    """

    divisorMapping = divisor_mapping()

    outList = create_word_list(testedNumber, divisorMapping)

    outList = reverse_word_list(testedNumber, 2, outList)

    if len(outList) == 0 : 
        # inInt is not a multiple of 5, 7 or 11
        return str(testedNumber)

    return "".join(outList)

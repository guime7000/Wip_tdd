def is_multiple_of(inInt: int, divisor: int) -> bool :
    """
    Returns true if inInt is a multiple of divisor, False otherwise
    """
    return inInt % divisor == 0

def divisor_mapping() -> dict :
    """
    Returns a dict containing pairs of divisor / corresponding word

    Modify outDict as you wish to fit your needs in bigbang function :
    each key / value pair of the dict corresponds to an int value as key (divisor) and a string as value 
    """
    outDict = {5 : "big",
                7 : "bang",
                11 : "boom"}

    return outDict

def create_word_list(inInt: int, inDict : dict) -> list :
    """
    Checks if an inInt integer value is a multiple of some divisors.
    If so, appends a specific word to a list the fucntion will return
    """
    outList = []
    for key in inDict.keys():
        if is_multiple_of(inInt, key):
            outList.append(inDict[key])

    return outList

def reverse_word_list(inInt: int, divisor: int, inList: list) -> list :
    """
    Returns a reversed inList if inInt is a multiple of divisor
    Returns inList otherwise
    """
    if is_multiple_of(inInt, divisor):
        inList.reverse()
    
    return inList


def bigbang(inInt : int) -> str :
    """
    Returns a specific string given conditions on the inInt integer parameter.
    """

    # Dictionnary to map a divisor and the output word associated to it
    divisorMapping = divisor_mapping()

    outList = create_word_list(inInt, divisorMapping)

    outList = reverse_word_list(inInt, 2, outList)

    if len(outList) == 0 : 
        # inInt is not a multiple of 5, 7 or 11
        outList.append(str(inInt))

    return "".join(outList)

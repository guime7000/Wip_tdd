def is_multiple_of(inInt: int, divisor: int) -> bool :
    """
    Returns true if inInt is a multiple of divisor, False otherwise
    """
    isMultiple = False
    if inInt % divisor == 0 :
        isMultiple = True
    
    return isMultiple

def bigbang(inInt : int) -> str :
    """
    Returns a specific string given conditions on the inInt integer parameter.
    """

    # Dictionnary to map a divisor and the output word associated to it
    # dict item -> divisor : associated_word
    divisorMapping = {5 : "big",
                    7 : "bang",
                    11 : "boom"}
    outList = []

    for key in divisorMapping.keys():
        if is_multiple_of(inInt, key):
            outList.append(divisorMapping[key])

    if len(outList) == 0 : 
        # inInt is not a multiple of 5, 7 or 11
        outList.append(str(inInt))

    if is_multiple_of(inInt, 2):
        #inInt is even
        outList.reverse()

    return "".join(outList)

def bigbang(inInt : int) -> str :
    """
    Returns a specific string given conditions on the inInt integer parameter.
    """
    outList = []

    if inInt%5 == 0: 
        # inInt is multiple of 5
        outList.append("big")
    
    if inInt%7 == 0: 
        # inInt is multiple of 7
        outList.append("bang")

    if inInt%11 == 0: 
        # inInt is multiple of 11
        outList.append("boom")

    if len(outList) == 0 : 
        # inInt is not a multiple of 5, 7 or 11
        outList.append(str(inInt))

    if inInt%2 == 0:
        #inInt is even
        outList.reverse()

    return "".join(outList)

def bigbang(inInt : int) -> str :
    """Return a specific string given conditions on the inInt integer parameter"""
    outList = []

    if inInt%5 == 0:
        outList.append("big")
    
    if inInt%7 == 0:
        outList.append("bang")

        
    return "".join(outList)
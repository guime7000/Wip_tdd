def parse_expression(expression : str, delimiter: str = ",") -> list :
    """
    Parses an expression containing integers separated by a delimiter
    to return a list where delimiters have been removed
    """
    return expression.split(delimiter)

def converts_to_integer(stringList : list) -> list :
    """
    Converts a list of integers given as strings to a list containing integers
    """
    convertedList = []
    for element in stringList :
        convertedList.append(int(element))
    return convertedList

def calculate(expression: str) -> int:
    """
    Returns the sum of integers written in expression
    """

    if len(expression) == 0 :
        return 0
    
    else :
        parsedExpressions = parse_expression(expression)
        integerList = converts_to_integer(parsedExpressions)

    return sum(integerList)

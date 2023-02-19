def parse_expression(expression : str, delimiter: str = ",") -> list :
    """
    Parses a string expression containing integers separated by a delimiter
    to return a list of those integers
    """
    print(delimiter)
    pass

def calculate(expression: str) -> int:
    """
    Returns the sum of integers written in expression
    """
    calculatedSum = 0

    if len(expression) == 0 :
        return calculatedSum
    
    else :
        parse_expression(expression)

    return calculatedSum


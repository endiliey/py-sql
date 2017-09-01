def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    high = len(aStr) - 1
    low = 0
    mid = (high + low) // 2

    if aStr == "":
        return False
    elif len(aStr) == 1:
        return aStr == char
    elif aStr[mid] == char:
        return True
    elif char < aStr[mid]:
        return isIn(char, aStr[:mid])
    else:
        return isIn(char, aStr[mid + 1:])


print(isIn('d', "abc"))


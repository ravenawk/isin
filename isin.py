def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    begining = 0
    middle = len(aStr)//2
    end = len(aStr)
    
    if len(aStr) == 0 or ((len(aStr) == 1) and (char != aStr[0])):
        return False
    elif char == aStr[middle]:
        return True
    elif char < aStr[middle]:
        aStr = aStr[begining:middle]
        return isIn(char,aStr)
    else:
        aStr = aStr[middle:end]
        return isIn(char,aStr)

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:44:01 2021

@author: Jonas
"""


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if aStr == "":
        return False
    # Your code here
    half = len(aStr) // 2
    if char == aStr[half]:
        return True
    elif len(aStr) <= 1:
        return False
    else:
        if char > aStr[half]:
            return isIn(char, aStr[half + 1:])
        else:
            return isIn(char, aStr[:half])


s = "lol"
print(isIn("l", s))

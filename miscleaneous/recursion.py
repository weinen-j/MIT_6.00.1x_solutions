# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:17:43 2021

@author: Jonas
"""


def recur_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 1:
        return base * exp
    else:
        return base * recur_power(base, exp - 1)


print(recur_power(3, 3))

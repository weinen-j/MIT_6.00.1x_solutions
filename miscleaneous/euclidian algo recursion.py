# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 01:10:43 2021

@author: Jonas
"""


def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

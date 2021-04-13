# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 22:04:49 2021

@author: Jonas
"""


def iterPower(base, exp):
    prod = 1
    for i in range(1, exp + 1):
        prod *= base * 1
    return prod


print(iterPower(2, 4))

# for i in range(1, 3):
# print(i)

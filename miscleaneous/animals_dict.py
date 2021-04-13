# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 01:49:34 2021

@author: Jonas
"""

animals = {'a': 1, 'b': 3, 'c': 4}


# def how_many(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.

#     returns: int, how many values are in the dictionary.
#     '''
#     count = 0
#     for i in aDict.keys():
#         count += 1
#     return count

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for i in aDict.values():
        count += i
    return count


print(how_many(animals))

# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 16:50:38 2021

@author: Jonas
"""
group_1 = ['kai', 'abe', 'ada', 'gus', 'zoe']
group_2 = ['jen', 'eva', 'dan', 'isa', 'meg']
pairings = {name: name_2 for name, name_2 in zip(group_1, group_2)}
print(pairings)

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 12:10:28 2021

@author: Jonas
"""
balance = 320000
annualInterestRate = 0.2
Monthlyinterestrate = (annualInterestRate) / 12.0
months = 12
upper = balance * (1 + Monthlyinterestrate)**12 / 12.0
lower = balance / months
pay = 0

# def check(u, l):
#     a = balance
#     for i in range(1, months+1):
#         a += balance * Monthlyinterestrate
#         a -= (u + l)
#     if a < 0:
#         return int(l)
#     else:
#         check(u, (u + l) / 2)
# print(str(check(upper, lower)))

while True:
    a = balance
    pay = (upper + lower) / 2
    for i in range(0, months):
        a -= pay
        a += a * Monthlyinterestrate
    if a < 0.2 and a > 0:
        break
    if a > 0.2:
        lower = (lower + upper) / 2
    elif a < 0.2:
        upper = (upper + lower) / 2
print(round(pay, 2))

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 12:10:28 2021

@author: Jonas
"""
balance = 4773
annualInterestRate = 0.2
months = 12
pay = 0


while True:
    a = balance
    for i in range(1, 13):
        a += (a * annualInterestRate / months)
        a -= pay
    if a <= 0:
        break
    pay += 10


print("Lowest Payment: " + str(pay))

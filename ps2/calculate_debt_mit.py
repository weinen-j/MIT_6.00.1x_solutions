# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 12:10:28 2021

@author: Jonas
"""
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
months = 12

for i in range(0, months):
    balance += (balance * annualInterestRate / months)
    balance -= (balance * monthlyPaymentRate)
print("Remaining balance: " + str(round(balance, 2)))

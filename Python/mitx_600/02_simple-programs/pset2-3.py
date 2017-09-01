# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 02:09:11 2017

@author: User
"""

balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12.0
high = (balance * (1 + monthlyInterestRate)**12)/12.0
low = balance/12
fixedPayment = (high + low)/2

while True:
    updatedBalance = balance
    for month in range(12):    
        updatedBalance -= fixedPayment
        updatedBalance += (monthlyInterestRate * updatedBalance)
        
    if round(updatedBalance) < 0:
        high = fixedPayment
    elif round(updatedBalance) > 0:
        low = fixedPayment
    elif round(updatedBalance) == 0:
        print("Lowest Payment: ", round(fixedPayment, 2))
        break
    fixedPayment = (high + low) / 2.0

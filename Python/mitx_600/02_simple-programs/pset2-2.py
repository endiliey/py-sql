# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 01:58:07 2017

@author: User
"""

monthlyInterestRate = annualInterestRate / 12.0
minimumMonthlyPayment = 0
updatedBalance = balance

while (updatedBalance >= 0):
    updatedBalance = balance
    minimumMonthlyPayment += 10
    for month in range(12):
        monthlyUnpaidBalance = updatedBalance - minimumMonthlyPayment
        updatedBalance = round(monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance), 2)
        
print("Lowest Payment: ", str(minimumMonthlyPayment))
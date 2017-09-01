# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 01:38:35 2017

@author: User
"""

"""
For testing purpose

def minpayment(balance, annualInterestRate, monthlyPaymentRate):
  monthlyInterestRate = annualInterestRate / 12.0
  for month in range(12):
      minimumMonthlyPayment = monthlyPaymentRate * balance
      monthlyUnpaidBalance = balance - minimumMonthlyPayment
      balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
  print('Remaining balance:', round(balance, 2))
  
minpayment(42, 0.2, 0.04)

"""

monthlyInterestRate = annualInterestRate / 12.0
for month in range(12):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
print('Remaining balance:', round(balance, 2))
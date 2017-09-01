# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:00:38 2017

@author: User
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    sum = 0
    for i in range(len(listA)):
        sum += (listA[i] * listB[i])
    return sum
    
listA = [1, 2, 3]
listB = [4, 5, 6]
print(dotProduct(listA, listB))
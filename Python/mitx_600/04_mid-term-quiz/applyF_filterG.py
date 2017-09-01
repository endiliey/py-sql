# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:57:16 2017

@author: User
"""

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Your code here
    maxElement = -1
    originalList = L[:]
    L.clear()
    for i in originalList:
        if g(f(i)):
            L.append(i)
            maxElement = max(maxElement, i)
    
    return maxElement
         
def f(i):
    return i + 2
    
def g(i):
    return i > 5

L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)
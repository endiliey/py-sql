# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 23:46:29 2017

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 23:45:38 2017

@author: User
"""

'''This function is provided from pset'''
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

'''Test case'''
testList = [1, -4, 8, -9]

'''This is the answer'''
applyToEach(testList, abs)

'''For testing answer only'''
print(testList)
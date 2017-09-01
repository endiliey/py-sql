# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 23:19:12 2017

@author: User
"""
def flatAppend(aList, newList):
    if type(aList) is not list:
        newList.append(aList)
    else:
        for inList in aList:
           flatAppend(inList, newList)
           
    return newList

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    newList = []
    return flatAppend(aList, newList)

    
listA = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
#Expect flattening into [1,'a','cat',2,3,'dog',4,5]
print(flatten(listA))
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:47:44 2017

@author: User
"""
def f(a, b):
    return a > b
    
def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    nd1 = {}
    nd2 = {}
    for key1 in d1.keys():
        if key1 in d2.keys():
            nd1[key1] = f(d1[key1], d2[key1])
        else:
            nd2[key1] = d1[key1]
            
    for key2 in d2.keys():
        if key2 not in d1.keys():
            nd2[key2] = d2[key2]

    tupleDict = (nd1, nd2)
    return tupleDict
      
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
print(dict_interdiff(d1, d2))
    

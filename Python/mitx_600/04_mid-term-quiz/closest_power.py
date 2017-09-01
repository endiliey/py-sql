# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 21:49:40 2017

@author: User
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    exponent = 0
    while True:
        diff1 = abs(num - base**exponent)
        diff2 = abs(num - base**(exponent + 1))
        if diff1<= diff2:
            break
        else:
            exponent += 1
    return exponent
            
print(closest_power(4, 1))
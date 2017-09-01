# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 22:22:46 2017

@author: Endilie
"""

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 22:20:15 2017

@author: User
"""

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
# -*- coding: utf-8 -*-
"""
Snippets for Problem 3
@author : Endilie

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s
in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh

n the case of ties, print the first substring. For example,
if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc

"""
s = 'azcbobobegghakl'

temp = s[0] # first letter as first temporary
longest = s[0]

for i in range(1, len(s)):
    # if subsequent next letter is inorder, concat it
    if s[i] >= s[i - 1]:
        temp = temp + s[i]
    # if not, restart building with new letter
    else:
        temp = s[i]
    # if temp string is longer than longest, change it
    if len(temp) > len(longest):
        longest = temp

print("Longest substring in alphabetical order is: " + longest)
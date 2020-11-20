#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:30:41 2019

@author: jlopes

Python program to find the missing and additional elements

Adapted from: https://www.geeksforgeeks.org/python-sets/
"""

# examples of lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

# prints the missing and additional elements in list2
missing = set(list1).difference(list2)
additional = set(list2).difference(list1)

print()
print("Missing values in second list:", missing)
print("Additional values in second list:", additional)

# prints the missing and additional elements in list1
missing = set(list2).difference(list1)
additional = set(list1).difference(list2)

print()
print("Missing values in second list:", missing)
print("Additional values in second list:", additional)

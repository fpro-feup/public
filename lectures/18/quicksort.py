#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 09:49:08 2018

@author: jlopes

David Mertz, Functional Programming in Python
"""

def quicksort(lst):
    """Quicksort over a list-like sequence."""
    #print(lst)
    if len(lst) == 0:
        return lst
    pivot = lst[0]
    pivots = [x for x in lst if x == pivot]
    smaller = quicksort([x for x in lst if x < pivot])
    larger = quicksort([x for x in lst if x > pivot])
    return smaller + pivots + larger


l = [5, 8, 2, 9, 1, 4, 8, 9, 0, 3, 2, 7]
print()
print(l)
print(quicksort(l))

# O(?)

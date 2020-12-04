#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:20:33 2018

@author: jlopes
"""

# converts a distance in the form (ft,in) to inches
def ftin_2_in(ftin):
    feet, inches = ftin
    return 12.0*feet + inches

# some US heights
heights = [(5,8), (5,9), (6,2), (6,1), (6,7)]

print()
print(heights)

# the same in inches
heights2 = map(ftin_2_in, heights)

# print(heights2)
print(list(heights2))  # [68.0, 69.0, 74.0, 73.0, 79.0]

# converts inches to meters
def in_2_m(inches):
    return round(inches * 0.0254, 2)

heights3 = map(in_2_m, map(ftin_2_in, heights))
# [1.73, 1.75, 1.88, 1.85, 2.01]

print(list(heights3))

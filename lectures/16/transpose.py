#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:52:26 2018

@author: jlopes
"""

# 3x4 matrix implemented as a list of 3 lists of length 4
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]

print()
print(matrix)

# list comprehension will transpose rows and columns
transposed = [[row[i] for row in matrix] for i in range(4)]

print()
print(transposed)

# unroll the nested list comp
#mtransposed = []
#for i in range(4):
#    # the following 3 lines implement the nested listcomp
#    transposed_row = []
#    for row in matrix:
#        transposed_row.append(row[i])
#    mtransposed.append(transposed_row)
#
#print()
#print(mtransposed)

# in REAL LIVE, use unpacking
#print()
#print(list(zip(*matrix)))

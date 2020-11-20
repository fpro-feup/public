#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 14:10:51 2018

@author: jlopes
"""

print()
# sparse matrix as a list
matrix = [[0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 2, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 3, 0]]

print(matrix)

# sparse matrix as a dictionary
# For the keys, we can use tuples that contain the row and column numbers
matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}

print()
print(matrix)

# accessing one element
#print()
#print(matrix[(0, 3)])

##print(matrix[(1, 3)])

# The get method solves this problem:
#   The first argument is the key; the second argument is the value get
#   should return if the key is not in the dictionary
#print()
#print(matrix.get((0, 3), 0))
#print(matrix.get((1, 3), 0))

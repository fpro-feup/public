# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 19:42:55 2018

@author: jlopes
"""

coordinate = ['x', 'y', 'z']
value = [3, 4, 5, 0, 9]

result = zip(coordinate, value)
resultList = list(result)
print(resultList)

c, v = zip(*resultList)
print("c =", c)
print("v =", v)

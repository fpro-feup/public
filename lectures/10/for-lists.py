#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 09:56:17 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

print()
# Any list expression can be used in a for loop:
for number in range(20):
    if number % 3 == 0:
        print(number)

#print()
#for fruit in ["banana", "apple", "quince"]:
#    print("I like to eat " + fruit + "s!")

# Since lists are mutable, we often want to traverse a list, changing
# each of its elements
#xs = [1, 2, 3, 4, 5]
#
#for i in range(len(xs)):
#    xs[i] = xs[i]**2
#
#print()
#print(xs)

# often we are interested in the value and also in the index
# there's a pattern in Python for that
#xs = [1, 2, 3, 4, 5]
#
#for (i, val) in enumerate(xs):
#    xs[i] = val**2
#
#print(xs)

# enumerate generates pairs of both (index, value) during the 
# list traversal

#print()
#for (i, v) in enumerate(["banana", "apple", "pear", "lemon"]):
#    print(i, v)

